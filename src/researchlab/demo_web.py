"""Local teaching UI/API. Bind to loopback; internal deployment uses approved ingress/auth."""

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import struct
from urllib.parse import parse_qs, urlparse
import zlib

from researchlab import demo, label_data


def png(image):
    height, width = image.shape[:2]
    def chunk(kind, payload):
        return struct.pack(">I", len(payload)) + kind + payload + struct.pack(">I", zlib.crc32(kind + payload))
    raw = b"".join(b"\0" + row.tobytes() for row in image)
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(raw)) + chunk(b"IEND", b""))


def handler(root, model):
    collections = label_data.load_labeling(root)
    images = {f"{domain}/{sample_id}": (path, sample, manifest["classes"])
              for domain, (path, manifest, samples) in collections.items()
              for sample_id, sample in samples.items()}
    if model is not None:
        if Path(model).suffix.lower() != ".pt":
            raise demo.DemoError(f"{model}: serve expects a trained local YOLO .pt checkpoint. See docs/DETECTOR.md")
        from researchlab.detector import load
        predictor = load(model)
        model_sha256 = demo.digest(model)
    else:
        predictor = None
        model_sha256 = None

    class Handler(BaseHTTPRequestHandler):
        def send(self, status, value, content_type="application/json"):
            body = json.dumps(value).encode() if content_type == "application/json" else value
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self):
            request = urlparse(self.path)
            query = parse_qs(request.query)
            try:
                if request.path == "/":
                    self.send(200, Path(__file__).with_name("static").joinpath("index.html").read_bytes(), "text/html; charset=utf-8")
                elif request.path == "/health":
                    self.send(200, {"status": "ok", "model_sha256": model_sha256})
                elif request.path == "/api/images":
                    self.send(200, {"items": [{"id": key, "dataset": key.split("/", 1)[0],
                                               "split": sample["split"], "classes": classes}
                                              for key, (_, sample, classes) in images.items()]})
                elif request.path in {"/api/image", "/api/annotations"}:
                    sample_id = query.get("id", [""])[0]
                    if sample_id not in images:
                        self.send(404, {"error": "Unknown image ID"})
                        return
                    path, sample, _ = images[sample_id]
                    if request.path == "/api/image":
                        self.send(200, png(demo.pixels(path, sample)), "image/png")
                    else:
                        record = demo.annotations(path, sample["id"])
                        self.send(200, {**record, "image_id": sample_id})
                else:
                    self.send(404, {"error": "Unknown route"})
            except (demo.DemoError, ValueError, OSError) as error:
                self.send(400, {"error": str(error), "setup": "docs/OFFLINE_SETUP.md"})

        def do_POST(self):
            try:
                length = int(self.headers.get("Content-Length", "0"))
                if not 0 < length <= 100000:
                    raise demo.DemoError("Expected a bounded JSON request")
                payload = json.loads(self.rfile.read(length))
                if self.path == "/api/annotations":
                    sample_id = payload["image_id"]
                    if sample_id not in images:
                        self.send(404, {"error": "Unknown image ID"})
                        return
                    path, sample, classes = images[sample_id]
                    image = demo.pixels(path, sample)
                    demo.validate_annotations(payload, image.shape[1], image.shape[0], classes)
                    saved = demo.annotations(path, sample["id"], {**payload, "image_id": sample["id"]})
                    self.send(200, {**saved, "image_id": sample_id})
                elif self.path == "/api/predict":
                    sample_id = payload["sample_id"]
                    if sample_id not in images:
                        self.send(404, {"error": "Unknown image ID"})
                    elif predictor is None:
                        self.send(400, {"error": "Supply a local YOLO checkpoint with serve --model PATH. "
                                                "See docs/DETECTOR.md."})
                    else:
                        from researchlab.detector import predict_image
                        path, sample, _ = images[sample_id]
                        self.send(200, {"sample_id": sample_id, "model_sha256": model_sha256,
                                        "objects": predict_image(predictor, demo.pixels(path, sample))})
                else:
                    self.send(404, {"error": "Unknown route"})
            except (demo.DemoError, ValueError, KeyError, TypeError, OSError, RuntimeError) as error:
                self.send(400, {"error": str(error), "setup": "docs/OFFLINE_SETUP.md"})

    return Handler


def serve(root, model, port):
    server = ThreadingHTTPServer(("127.0.0.1", port), handler(root, model))
    print(f"Labeling UI: http://127.0.0.1:{server.server_port}; model: {model or 'none'}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
