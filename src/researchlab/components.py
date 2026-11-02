"""Frozen CPU inference components for plate, tracking and rescoring work.

Only the explicit ``fetch`` command accesses the model release hosts.
"""

import argparse
import hashlib
import json
from pathlib import Path
import sys

import httpx
import numpy as np


ASSETS = {
    "plate": {
        "url": "https://github.com/ankandrew/open-image-models/releases/download/assets/"
               "yolo-v9-t-384-license-plates-end2end.onnx",
        "sha256": "888397b96d761c89db40bc9c305838e8652660f5e282c2cadebbe8d2951a77a8",
    },
    "ocr": {
        "url": "https://github.com/ankandrew/cnn-ocr-lp/releases/download/arg-plates/"
               "cct_xs_v2_global.onnx",
        "sha256": "8031afb5fdc6b4d80462c9d542f1284ebd2cfddf5dbacd62609848d7e2855f44",
    },
    "objects": {
        "url": "https://github.com/ankandrew/open-image-models/releases/download/assets/"
               "rf-detr-nano-384-coco.onnx",
        "sha256": "fdcdd1c566ed4ab4d3700ca1ce6f03edadfec2a0655432e40e4c2734623feaec",
    },
}
VEHICLES = {2: "bicycle", 3: "car", 4: "motorcycle", 6: "bus", 8: "truck"}
ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_"


def digest(path):
    value = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def fetch(root, names):
    root.mkdir(parents=True, exist_ok=True)
    for name in names:
        path = root / f"{name}.onnx"
        asset = ASSETS[name]
        if path.is_file() and digest(path) == asset["sha256"]:
            continue
        temporary = path.with_suffix(".part")
        try:
            with httpx.stream("GET", asset["url"], follow_redirects=True, timeout=60) as response:
                response.raise_for_status()
                with temporary.open("wb") as target:
                    for block in response.iter_bytes():
                        target.write(block)
            if digest(temporary) != asset["sha256"]:
                raise ValueError(f"Checksum mismatch for {name}; retain the pinned model revision")
            temporary.replace(path)
        finally:
            temporary.unlink(missing_ok=True)
    available = {name: spec for name, spec in ASSETS.items()
                 if (root / f"{name}.onnx").is_file()
                 and digest(root / f"{name}.onnx") == spec["sha256"]}
    (root / "manifest.json").write_text(json.dumps(available, indent=2))


def runtime():
    try:
        import cv2
        import onnxruntime as ort
    except ImportError as error:
        raise ValueError("Install the approved components extra: uv sync --locked --extra "
                         "components; see docs/COMPONENTS.md and docs/OFFLINE_SETUP.md") from error
    return cv2, ort


class Models:
    def __init__(self, root):
        self.root = Path(root)
        self.sessions = {}

    def session(self, name):
        if name not in self.sessions:
            path = self.root / f"{name}.onnx"
            if not path.is_file():
                raise ValueError(f"Missing model {path}. On an approved connected workstation run "
                                 f"researchlab-components fetch --root {self.root} --models {name}, "
                                 "or transfer that bundle; see docs/COMPONENTS.md")
            if digest(path) != ASSETS[name]["sha256"]:
                raise ValueError(f"Model checksum mismatch: {path}; see docs/COMPONENTS.md")
            _, ort = runtime()
            options = ort.SessionOptions()
            options.intra_op_num_threads = 1
            self.sessions[name] = ort.InferenceSession(
                str(path), sess_options=options, providers=["CPUExecutionProvider"]
            )
        return self.sessions[name]

    def run(self, name, values):
        session = self.session(name)
        return session.run(None, {session.get_inputs()[0].name: values})

    def recognize(self, crop):
        """Recognize a BGR uint8 crop; Latin uppercase letters/digits only."""
        cv2, _ = runtime()
        if crop.size == 0:
            raise ValueError("Cannot recognize an empty crop")
        rgb = cv2.cvtColor(cv2.resize(crop, (128, 64)), cv2.COLOR_BGR2RGB)
        scores = self.run("ocr", rgb[None].astype(np.uint8))[0][0]
        indexes = scores.argmax(axis=-1)
        text = "".join(ALPHABET[i] for i in indexes).rstrip("_")
        return {"text": text, "character_confidence": scores.max(axis=-1).tolist()}

    def plates(self, image, threshold=.25):
        cv2, _ = runtime()
        height, width = image.shape[:2]
        ratio = min(384 / width, 384 / height)
        w, h = round(width * ratio), round(height * ratio)
        dw, dh = (384 - w) / 2, (384 - h) / 2
        resized = cv2.resize(image, (w, h))
        padded = cv2.copyMakeBorder(resized, round(dh - .1), round(dh + .1),
                                   round(dw - .1), round(dw + .1), cv2.BORDER_CONSTANT,
                                   value=(114, 114, 114))
        tensor = padded[:, :, ::-1].transpose(2, 0, 1)[None].astype(np.float32) / 255
        output = self.run("plate", tensor)[0]
        detections = []
        for row in output:
            if row[6] < threshold:
                continue
            box = (row[1:5] - np.array([dw, dh, dw, dh])) / ratio
            box = np.clip(box, 0, [width, height, width, height]).astype(int).tolist()
            if box[2] > box[0] and box[3] > box[1]:
                detections.append({"box_xyxy": box, "score": float(row[6]), "class": "plate"})
        return detections

    def vehicles(self, image, threshold=.1):
        """RF-DETR COCO vehicle queries; image coordinates, without GT inputs."""
        cv2, _ = runtime()
        rgb = cv2.cvtColor(cv2.resize(image, (384, 384)), cv2.COLOR_BGR2RGB)
        values = rgb.astype(np.float32) / 255
        values = (values - np.array([.485, .456, .406], dtype=np.float32)) / np.array(
            [.229, .224, .225], dtype=np.float32
        )
        boxes, logits = self.run("objects", values.transpose(2, 0, 1)[None])[:2]
        class_ids = np.array(list(VEHICLES))
        probabilities = 1 / (1 + np.exp(-np.clip(logits[0][:, class_ids], -80, 80)))
        selected = probabilities.argmax(axis=1)
        scores = probabilities[np.arange(len(selected)), selected]
        height, width = image.shape[:2]
        detections = []
        for index in np.argsort(-scores, kind="stable"):
            if scores[index] < threshold:
                continue
            cx, cy, w, h = boxes[0, index]
            box = np.array([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2])
            box = np.clip(box * [width, height, width, height], 0,
                          [width, height, width, height]).tolist()
            if box[2] > box[0] and box[3] > box[1]:
                label = int(class_ids[selected[index]])
                detections.append({"box_xyxy": box, "score": float(scores[index]),
                                   "class": VEHICLES[label], "class_id": label})
        return detections


def overlap(a, b):
    left, top = max(a[0], b[0]), max(a[1], b[1])
    right, bottom = min(a[2], b[2]), min(a[3], b[3])
    intersection = max(0, right - left) * max(0, bottom - top)
    union = (a[2] - a[0]) * (a[3] - a[1]) + (b[2] - b[0]) * (b[3] - b[1]) - intersection
    return intersection / union if union > 0 else 0


class IoUTracker:
    """Frozen greedy same-class IoU baseline; retains tracks for five missed frames."""
    def __init__(self):
        self.tracks = {}
        self.next_id = 1

    def update(self, detections, frame):
        self.tracks = {k: v for k, v in self.tracks.items() if frame - v[1] <= 6}
        available = set(self.tracks)
        output = []
        for detection in detections:
            candidates = [(overlap(detection["box_xyxy"], self.tracks[k][0]["box_xyxy"]), k)
                          for k in sorted(available)
                          if detection["class"] == self.tracks[k][0]["class"]]
            score, track_id = max(candidates, default=(0, 0))
            if score < .3:
                track_id = self.next_id
                self.next_id += 1
            else:
                available.remove(track_id)
            record = {**detection, "track_id": track_id}
            self.tracks[track_id] = (record, frame)
            output.append(record)
        return output


def manifest_rows(path):
    seen = set()
    with path.open() as stream:
        for line in stream:
            record = json.loads(line)
            if not isinstance(record.get("id"), str) or record["id"] in seen:
                raise ValueError("Manifest image IDs must be unique strings")
            seen.add(record["id"])
            image = Path(record["path"])
            if not image.is_absolute():
                image = path.parent / image
            yield record, image


def write_images(models, manifest, output, mode, threshold, overlay_dir=None):
    cv2, _ = runtime()
    output.parent.mkdir(parents=True, exist_ok=True)
    if overlay_dir:
        overlay_dir.mkdir(parents=True, exist_ok=True)
    count = 0
    with output.open("w") as target:
        for record, path in manifest_rows(manifest):
            image = cv2.imread(str(path))
            if image is None:
                raise ValueError(f"Cannot decode {path}; see docs/DATASETS.md")
            if mode == "lpr":
                predictions = models.plates(image, threshold)
                for item in predictions:
                    x1, y1, x2, y2 = item["box_xyxy"]
                    item.update(models.recognize(image[y1:y2, x1:x2]))
                used = ("plate", "ocr")
            else:
                predictions = models.vehicles(image, threshold)
                used = ("objects",)
            data = {"id": record["id"], "scene_id": record.get("scene_id"),
                    "path": str(path.resolve()), "image_size_hw": list(image.shape[:2]),
                    "gsd_m": record.get("gsd_m"), "view_angle_deg": record.get("view_angle_deg"),
                    "models": {name: ASSETS[name]["sha256"] for name in used},
                    "detections": [{**p, "detection_id": f"{record['id']}:{i}"}
                                   for i, p in enumerate(predictions)]}
            target.write(json.dumps(data) + "\n")
            if overlay_dir:
                for item in predictions:
                    x1, y1, x2, y2 = map(int, item["box_xyxy"])
                    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(image, item.get("text", item["class"]), (x1, max(15, y1)),
                                cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 255, 0), 1)
                if not cv2.imwrite(str(overlay_dir / f"{count:06d}.png"), image):
                    raise ValueError("Failed to write overlay")
            count += 1
    return {"images": count, "output": str(output)}


def write_tracks(models, video, output, sequence_id, threshold=.5):
    cv2, _ = runtime()
    capture = cv2.VideoCapture(str(video))
    if not capture.isOpened():
        raise ValueError(f"Cannot open video {video}; verify local video/codec")
    fps = capture.get(cv2.CAP_PROP_FPS)
    total = capture.get(cv2.CAP_PROP_FRAME_COUNT)
    if not np.isfinite(fps) or fps <= 0:
        capture.release()
        raise ValueError("Missing FPS; supply a video with a valid constant-rate time base")
    tracker = IoUTracker()
    output.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    try:
        with output.open("w") as target:
            while True:
                ok, image = capture.read()
                if not ok:
                    break
                detections = tracker.update(models.vehicles(image, threshold), count)
                target.write(json.dumps({"sequence_id": sequence_id, "frame_index": count,
                                         "timestamp_s": count / fps, "fps": fps,
                                         "model_sha256": ASSETS["objects"]["sha256"],
                                         "tracker": "greedy-iou-v1", "detections": detections}) + "\n")
                count += 1
    finally:
        capture.release()
    if not count or (total > 0 and count < int(total)):
        raise ValueError(f"Video decode incomplete: {count} frames, container advertises {total}")
    return {"frames": count, "output": str(output)}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["fetch", "check", "lpr", "recognize", "detect", "track"])
    parser.add_argument("--root", type=Path, default=Path(".local/models"))
    parser.add_argument("--models", nargs="+", choices=ASSETS, default=list(ASSETS))
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--crop", type=Path)
    parser.add_argument("--video", type=Path)
    parser.add_argument("--sequence-id")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--overlay-dir", type=Path)
    parser.add_argument("--threshold", type=float)
    args = parser.parse_args(argv)
    if args.threshold is not None and not 0 <= args.threshold <= 1:
        parser.error("--threshold must be between 0 and 1")
    try:
        models = Models(args.root)
        if args.command == "fetch":
            fetch(args.root, args.models)
            result = {"models": args.models, "root": str(args.root)}
        elif args.command == "check":
            result = {name: {"sha256": ASSETS[name]["sha256"],
                             "inputs": [item.shape for item in models.session(name).get_inputs()]}
                      for name in args.models}
        elif args.command == "recognize":
            if not args.crop:
                parser.error("recognize requires --crop PATH")
            cv2, _ = runtime()
            image = cv2.imread(str(args.crop))
            if image is None:
                raise ValueError(f"Cannot decode {args.crop}")
            result = models.recognize(image)
        elif args.command == "track":
            if not args.video or not args.output or not args.sequence_id:
                parser.error("track requires --video, --output and --sequence-id")
            result = write_tracks(models, args.video, args.output, args.sequence_id,
                                  .5 if args.threshold is None else args.threshold)
        else:
            if not args.manifest or not args.output:
                parser.error("lpr/detect requires --manifest and --output")
            result = write_images(models, args.manifest, args.output, args.command,
                                  (.25 if args.command == "lpr" else .1)
                                  if args.threshold is None else args.threshold, args.overlay_dir)
        print(json.dumps(result, indent=2))
        return 0
    except (ValueError, OSError, ImportError, RuntimeError, httpx.HTTPError) as error:
        print(f"ERROR: {error}\nSee docs/COMPONENTS.md", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
