"""Entry point with offline remediation before loading numerical dependencies."""

import argparse
import importlib.util
import json
from pathlib import Path
import sys


def main(argv=None):
    parser = argparse.ArgumentParser(description="Teaching application: prepare, train, evaluate and serve")
    parser.add_argument("command", choices=["prepare", "initialize-store", "train", "evaluate", "predict", "serve", "check-data", "import-labels", "smoke"])
    parser.add_argument("--root", type=Path, default=None)
    parser.add_argument("--model", type=Path)
    parser.add_argument("--head", choices=["both", "crop", "video"], default="both")
    parser.add_argument("--sample", help="Sample ID from the local bundle for predict")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--domain", choices=["coco", "video", "drone", "satellite"])
    parser.add_argument("--index", type=Path, help="Prepared JSON index for import-labels")
    args = parser.parse_args(argv)
    if importlib.util.find_spec("numpy") is None:
        print("Missing Python dependency: numpy. Install the approved locked environment before running. "
              "See docs/setup/OFFLINE_SETUP.md#python-runtime; no public installation was attempted.", file=sys.stderr)
        return 2
    if args.root is None:
        if args.command in {"serve", "check-data", "import-labels"}:
            args.root = Path("data/labeling")
        elif args.command == "smoke":
            args.root = Path("artifacts/baseline-check")
        else:
            parser.error("specify --root PATH for the local bundle; see docs/reference/DATA_FORMATS.md")
    from researchlab import demo
    model = args.model or args.root / "models/baseline.npz"
    try:
        if args.command == "prepare":
            manifest = demo.prepare(args.root)
            result = {"root": str(args.root), "source": manifest["source"], "samples": len(manifest["samples"])}
        elif args.command == "initialize-store":
            demo.initialize_store(args.root, demo.load_manifest(args.root))
            result = {"store": str(args.root / "labels.sqlite"), "status": "initialized"}
        elif args.command == "train":
            result = demo.train(args.root, model, head=args.head)
        elif args.command == "evaluate":
            result = demo.evaluate(args.root, model)
        elif args.command == "predict":
            if args.sample is None:
                parser.error("predict requires --sample with a known ID from the local manifest")
            result = demo.predict(args.root, model, args.sample)
        elif args.command == "import-labels":
            from researchlab import label_data
            if args.domain is None or args.index is None:
                parser.error("import-labels requires --domain and --index")
            index = json.loads(args.index.read_text())
            samples = label_data.write_manifest(args.root / args.domain, args.domain, index["source"],
                                                index["classes"], index["samples"])
            result = {"dataset": args.domain, "images": len(samples)}
        elif args.command == "check-data":
            from researchlab import label_data
            result = {name: len(samples) for name, (_, _, samples)
                      in label_data.load_labeling(args.root).items()}
        elif args.command == "serve":
            from researchlab.demo_web import serve
            serve(args.root, args.model, args.port)
            return 0
        else:
            demo.prepare(args.root)
            training = demo.train(args.root, model)
            evaluation = demo.evaluate(args.root, model)
            prediction = demo.predict(args.root, model, "video-030")
            if any(v["final_loss"] >= v["initial_loss"] for v in training["history"].values()):
                raise demo.DemoError("Training smoke failed: loss did not decrease")
            if any(v["test"]["accuracy"] < .9 for v in evaluation["metrics"].values()):
                raise demo.DemoError("Training smoke failed on the procedural held-out fixture")
            result = {"status": "PASS", "training": training, "evaluation": evaluation,
                      "fresh_load_prediction": prediction,
                      "scope": "Executed procedural fixture, not an internal deployment or real-world benchmark"}
        print(json.dumps(result, indent=2))
        return 0
    except (demo.DemoError, OSError, ValueError, KeyError, TypeError, ImportError, RuntimeError) as error:
        print(f"ERROR: {error}\nSetup and asset locations: docs/setup/OFFLINE_SETUP.md", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
