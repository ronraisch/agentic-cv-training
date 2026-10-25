"""Small offline, single-object detector and procedural localization fixture."""

import argparse
import importlib.util
import json
from pathlib import Path
import sys


def runtime():
    if importlib.util.find_spec("torch") is None:
        raise ValueError("Missing dependency: torch. Supply the locked torch extra in the approved "
                         "image/wheelhouse; see docs/OFFLINE_SETUP.md#detector-runtime. "
                         "No runtime installation was attempted.")
    import torch
    return torch


def network():
    torch = runtime()
    nn = torch.nn
    return nn.Sequential(
        nn.Conv2d(3, 8, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
        nn.Conv2d(8, 16, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
        nn.Flatten(), nn.Linear(16 * 8 * 12, 64), nn.ReLU(), nn.Linear(64, 7),
    )


def fixture(count, seed):
    """RGB BCHW, normalized xyxy boxes, binary class and presence targets."""
    import numpy as np
    torch = runtime()
    rng = np.random.default_rng(seed)
    images = rng.uniform(.03, .12, (count, 3, 32, 48)).astype("float32")
    boxes, classes, present = [], [], []
    for i in range(count):
        x, y = int(rng.integers(1, 27)), int(rng.integers(1, 17))
        w, h = int(rng.integers(10, 21)), int(rng.integers(8, 15))
        label = i % 2
        exists = i % 5 != 0
        if exists:
            images[i, :, y:y+h, x:x+w] = np.array(
                [1., .25, .1] if label == 0 else [.1, .3, 1.], dtype="float32")[:, None, None]
        boxes.append([x/48, y/32, (x+w)/48, (y+h)/32])
        classes.append(label)
        present.append(float(exists))
    return (torch.from_numpy(images), torch.tensor(boxes),
            torch.tensor(classes), torch.tensor(present))


def decoded(output):
    torch = runtime()
    edges = output[:, :4].sigmoid()
    lo = torch.minimum(edges[:, :2], edges[:, 2:])
    hi = torch.maximum(edges[:, :2], edges[:, 2:])
    return torch.cat([lo, hi], dim=1)


def evaluate(model, data):
    torch = runtime()
    images, boxes, classes, present = data
    model.eval()
    with torch.inference_mode():
        out = model(images)
        pred = decoded(out)
        mask = present.bool()
        intersection = (torch.minimum(pred[:, 2:], boxes[:, 2:]) -
                        torch.maximum(pred[:, :2], boxes[:, :2])).clamp(min=0).prod(dim=1)
        area = (pred[:, 2:] - pred[:, :2]).prod(dim=1)
        gt_area = (boxes[:, 2:] - boxes[:, :2]).prod(dim=1)
        iou = intersection / (area + gt_area - intersection).clamp(min=1e-6)
        return {"samples": len(images), "foreground_samples": int(mask.sum()),
                "mean_iou": float(iou[mask].mean()),
                "class_accuracy": float((out[mask, 4:6].argmax(1) == classes[mask]).float().mean()),
                "presence_accuracy": float(((out[:, 6] > 0) == mask).float().mean())}


def train(path, steps=180):
    import numpy as np
    torch = runtime()
    torch.manual_seed(7)
    torch.set_num_threads(1)
    model = network()
    optimizer = torch.optim.Adam(model.parameters(), lr=.003)
    images, boxes, classes, present = fixture(160, 71)
    mask = present.bool()
    losses = []
    for _ in range(steps):
        model.train()
        optimizer.zero_grad()
        out = model(images)
        loss = (10 * torch.nn.functional.mse_loss(decoded(out)[mask], boxes[mask]) +
                torch.nn.functional.cross_entropy(out[mask, 4:6], classes[mask]) +
                torch.nn.functional.binary_cross_entropy_with_logits(out[:, 6], present))
        loss.backward()
        optimizer.step()
        losses.append(float(loss.detach()))
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    arrays = {k: v.detach().cpu().numpy() for k, v in model.state_dict().items()}
    arrays["metadata"] = np.array(json.dumps({"architecture": "tiny-single-object-v1",
        "classes": ["vehicle", "building"], "input": "RGB float32 BCHW 32x48, range 0..1",
        "boxes": "normalized xyxy", "training_source": "procedural-detector-v1",
        "train_seed": 71, "heldout_seed": 172, "steps": steps}))
    with path.open("wb") as stream:
        np.savez_compressed(stream, **arrays)
    return {"model": str(path), "initial_loss": losses[0], "final_loss": losses[-1],
            "heldout": evaluate(model, fixture(80, 172)),
            "scope": "Single-object procedural fixture; not a pretrained research detector"}


def load(path):
    import numpy as np
    torch = runtime()
    path = Path(path)
    if not path.is_file():
        raise ValueError(f"Missing detector artifact: {path}. Run researchlab-detector train "
                         f"--model {path}, or transfer the approved artifact to this exact path. "
                         "See docs/OFFLINE_SETUP.md#detector-runtime; no download was attempted.")
    with np.load(path, allow_pickle=False) as saved:
        if json.loads(str(saved["metadata"]))["architecture"] != "tiny-single-object-v1":
            raise ValueError("Unsupported detector architecture; see docs/DETECTOR.md")
        model = network()
        model.load_state_dict({k: torch.from_numpy(saved[k].copy())
                               for k in saved.files if k != "metadata"})
    return model.eval()


def predict(path, images):
    """Infer local RGB BCHW images, returning normalized boxes and class probabilities."""
    torch = runtime()
    if images.ndim != 4 or tuple(images.shape[1:]) != (3, 32, 48):
        raise ValueError("Detector input must be RGB BCHW 32x48; see docs/DETECTOR.md")
    if not torch.isfinite(images).all() or images.min() < 0 or images.max() > 1:
        raise ValueError("Detector pixels must be finite float values in 0..1")
    with torch.inference_mode():
        out = load(path)(images.float())
        return {"boxes_xyxy": decoded(out).tolist(),
                "class_probabilities": out[:, 4:6].softmax(1).tolist(),
                "object_probability": out[:, 6].sigmoid().tolist()}


def predict_batches(path, images, batch_size=256):
    """Run bounded-memory inference and combine per-image output fields."""
    if len(images) == 0 or batch_size < 1:
        raise ValueError("Supply at least one image and a positive batch size")
    result = {"boxes_xyxy": [], "class_probabilities": [], "object_probability": []}
    for start in range(0, max(1, len(images) - 1), batch_size):
        batch = predict(path, images[start:start + batch_size])
        for field in result:
            result[field].extend(batch[field])
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["train", "evaluate", "predict", "smoke"])
    parser.add_argument("--model", type=Path, default=Path("artifacts/detector/model.npz"))
    parser.add_argument("--input", type=Path, help="Local float32 RGB BCHW .npy input")
    args = parser.parse_args(argv)
    try:
        torch = runtime()
        torch.set_num_threads(1)
        if args.command in {"train", "smoke"}:
            result = train(args.model)
            if args.command == "smoke":
                result["reloaded_heldout"] = evaluate(load(args.model), fixture(80, 172))
                if result["final_loss"] >= result["initial_loss"] or any([
                    result["reloaded_heldout"]["mean_iou"] < .65,
                    result["reloaded_heldout"]["presence_accuracy"] < .95,
                    result["reloaded_heldout"]["class_accuracy"] < .95,
                ]):
                    raise ValueError("Detector smoke failed held-out localization/class/presence checks")
                result["status"] = "PASS"
        elif args.command == "evaluate":
            result = evaluate(load(args.model), fixture(80, 172))
        else:
            import numpy as np
            if args.input is None or not args.input.is_file():
                raise ValueError(f"Missing detector input: {args.input}. Supply --input PATH to a local "
                                 "RGB BCHW .npy array; see docs/DETECTOR.md and docs/OFFLINE_SETUP.md")
            result = predict_batches(args.model, torch.from_numpy(np.load(args.input, allow_pickle=False)))
        print(json.dumps(result, indent=2))
        return 0
    except (ValueError, OSError, RuntimeError, KeyError, ImportError) as error:
        print(f"ERROR: {error}\nSee docs/OFFLINE_SETUP.md#detector-runtime", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
