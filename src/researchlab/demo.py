"""CPU teaching baseline: persisted labels, real fitting, artifacts and inference."""

import hashlib
import json
from pathlib import Path
import sqlite3

import numpy as np


CLASSES = ["vehicle", "building"]
QUESTIONS = ["road", "outdoor", "sky_only"]
FEATURE_VERSION = "rgb-regions-v1"


class DemoError(ValueError):
    """An actionable asset or input error suitable for the CLI and teaching API."""


def missing(asset, path, action):
    return DemoError(
        f"Missing {asset}: {path}. {action} "
        "See docs/OFFLINE_SETUP.md for preparation, transfer and installation locations. "
        "No runtime download was attempted."
    )


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def asset_path(root, relative):
    root = Path(root).resolve()
    path = (root / relative).resolve()
    if not path.is_relative_to(root):
        raise DemoError("Asset path must stay inside the selected data bundle")
    return path


def prepare(root):
    """Prepare a small procedural fixture, without network access or model weights."""
    root = Path(root)
    if root.exists():
        if (root / "manifest.json").is_file():
            return load_manifest(root)
        raise DemoError(f"Choose a new bundle directory; {root} already exists without a manifest")
    root.mkdir(parents=True)
    rng = np.random.default_rng(21)
    samples = []
    for kind, count, train_end, val_end in [("image", 60, 36, 48), ("video", 36, 24, 30)]:
        for i in range(count):
            split = "train" if i < train_end else "validation" if i < val_end else "test"
            sample = {"id": f"{kind}-{i:03d}", "kind": kind, "split": split,
                      "group_id": f"{kind}-recording-{i:03d}"}
            if kind == "image":
                label = CLASSES[i % 2]
                image = np.full((32, 48, 3), 45., dtype=float)
                image[7:25, 8:40] = [210, 70, 25] if label == "vehicle" else [25, 80, 220]
                pixels = np.clip(image + rng.normal(0, 9, image.shape), 0, 255).astype("uint8")
                sample["annotations"] = [{"type": "rectangle", "label": label,
                                          "bounds": [8, 7, 40, 25]}]
            else:
                scene = i % 3
                color = [[90, 100, 90], [165, 95, 50], [70, 155, 235]][scene]
                frames = np.broadcast_to(np.array(color, dtype=float), (4, 32, 48, 3)).copy()
                if scene == 0:
                    frames[:, :16] = [75, 150, 210]
                pixels = np.clip(frames + rng.normal(0, 8, frames.shape), 0, 255).astype("uint8")
                sample["targets"] = [scene == 0, scene != 1, scene == 2]
                sample["timestamps_seconds"] = [0., 3., 6., 9.]
                sample["duration_seconds"] = 10.
            sample["path"] = f"{sample['id']}.npy"
            path = root / sample["path"]
            np.save(path, pixels, allow_pickle=False)
            sample["sha256"] = digest(path)
            samples.append(sample)
    manifest = {"schema_version": 1, "source": "procedural-demo-v1", "samples": samples}
    (root / "manifest.json").write_text(json.dumps(manifest, indent=2))
    initialize_store(root, manifest)
    return manifest


def load_manifest(root):
    path = Path(root) / "manifest.json"
    if not path.is_file():
        raise missing("dataset manifest", path,
                      f"Run researchlab-demo prepare --root {root}, or transfer the approved bundle here.")
    try:
        manifest = json.loads(path.read_text())
        if manifest["schema_version"] != 1 or not manifest["samples"]:
            raise ValueError("schema")
        seen, groups = set(), {}
        for item in manifest["samples"]:
            if item["id"] in seen or item["kind"] not in {"image", "video"}:
                raise ValueError("identity/kind")
            seen.add(item["id"])
            group = item["group_id"]
            if group in groups and groups[group] != item["split"]:
                raise ValueError("group overlap")
            groups[group] = item["split"]
            if item["split"] not in {"train", "validation", "test"}:
                raise ValueError("split")
            asset = asset_path(root, item["path"])
            if not asset.is_file():
                raise missing("dataset asset", asset, "Restore it from the approved bundle manifest.")
            if digest(asset) != item["sha256"]:
                raise DemoError(f"Checksum mismatch: {asset}; restore the approved version. See docs/OFFLINE_SETUP.md")
        return manifest
    except DemoError:
        raise
    except (KeyError, TypeError, ValueError) as error:
        raise DemoError(f"Invalid dataset manifest: {path}; see docs/DATA_FORMATS.md") from error


def pixels(root, sample):
    image = np.load(asset_path(root, sample["path"]), allow_pickle=False)
    expected_rank = 3 if sample["kind"] == "image" else 4
    if image.ndim != expected_rank or image.shape[-1] != 3 or image.dtype != np.uint8:
        raise DemoError("Expected RGB uint8 HWC image or THWC video; see docs/DATA_FORMATS.md")
    return image


def validate_annotations(record, width, height):
    if record.get("schema_version") != 1 or not isinstance(record.get("annotations"), list):
        raise DemoError("Unsupported annotation schema; see docs/DATA_FORMATS.md")
    for annotation in record["annotations"]:
        if annotation.get("type") != "rectangle" or annotation.get("label") not in CLASSES:
            raise DemoError("Expected a rectangle and a supported class")
        box = np.asarray(annotation.get("bounds"), dtype=float)
        if box.shape != (4,) or not np.isfinite(box).all():
            raise DemoError("Rectangle bounds must contain four finite coordinates")
        x1, y1, x2, y2 = box
        if not (0 <= x1 < x2 <= width and 0 <= y1 < y2 <= height):
            raise DemoError("Rectangle is empty or outside the image")
    return record


def initialize_store(root, manifest):
    with sqlite3.connect(Path(root) / "labels.sqlite") as connection:
        connection.execute("CREATE TABLE IF NOT EXISTS annotations (image_id TEXT PRIMARY KEY, record TEXT NOT NULL)")
        for sample in manifest["samples"]:
            if sample["kind"] == "image":
                record = {"schema_version": 1, "image_id": sample["id"],
                          "annotations": sample["annotations"]}
                connection.execute("INSERT OR IGNORE INTO annotations VALUES (?, ?)",
                                   (sample["id"], json.dumps(record)))


def annotations(root, image_id, record=None):
    path = Path(root) / "labels.sqlite"
    if not path.is_file():
        raise missing("annotation database", path,
                      f"Run researchlab-demo initialize-store --root {root} to import prepared annotations, or restore the database.")
    with sqlite3.connect(path) as connection:
        if record is not None:
            connection.execute("UPDATE annotations SET record = ? WHERE image_id = ?",
                               (json.dumps(record), image_id))
        row = connection.execute("SELECT record FROM annotations WHERE image_id = ?", (image_id,)).fetchone()
    if row is None:
        raise DemoError(f"Unknown image ID: {image_id}")
    return json.loads(row[0])


def image_features(image):
    x = image.astype(float) / 255.
    middle = len(x) // 2
    return np.concatenate([x.mean((0, 1)), x.std((0, 1)),
                           x[:middle].mean((0, 1)), x[middle:].mean((0, 1))])


def crop_rows(root, manifest, split):
    features, targets, ids = [], [], []
    for sample in manifest["samples"]:
        if sample["kind"] != "image" or sample["split"] != split:
            continue
        image = pixels(root, sample)
        record = validate_annotations(annotations(root, sample["id"]), image.shape[1], image.shape[0])
        for annotation in record["annotations"]:
            x1, y1, x2, y2 = annotation["bounds"]
            crop = image[int(np.floor(y1)):int(np.ceil(y2)), int(np.floor(x1)):int(np.ceil(x2))]
            features.append(image_features(crop))
            targets.append([annotation["label"] == label for label in CLASSES])
            ids.append(sample["id"])
    if not features:
        raise DemoError(f"No labeled crops in {split}; supply annotations before training")
    return np.array(features), np.array(targets, dtype=float), ids


def video_rows(root, manifest, split):
    selected = [s for s in manifest["samples"] if s["kind"] == "video" and s["split"] == split]
    if not selected:
        raise DemoError(f"No video samples in {split}; see docs/OFFLINE_SETUP.md")
    features = [np.mean([image_features(frame) for frame in pixels(root, s)], axis=0) for s in selected]
    return np.array(features), np.array([s["targets"] for s in selected], dtype=float), [s["id"] for s in selected]


def sigmoid(value):
    return 1 / (1 + np.exp(-np.clip(value, -40, 40)))


def fit(x, y):
    mean, scale = x.mean(0), x.std(0)
    scale[scale < 1e-6] = 1.
    design = np.column_stack([(x - mean) / scale, np.ones(len(x))])
    weights = np.zeros((design.shape[1], y.shape[1]))
    losses = []
    for _ in range(250):
        p = sigmoid(design @ weights)
        losses.append(float(-np.mean(y * np.log(p + 1e-12) + (1-y) * np.log(1-p + 1e-12))))
        weights -= .25 * design.T @ (p-y) / len(y)
    return mean, scale, weights, losses


def probabilities(arrays, kind, x):
    design = np.column_stack([(x-arrays[kind+"_mean"])/arrays[kind+"_scale"], np.ones(len(x))])
    return sigmoid(design @ arrays[kind+"_weights"])


def train(root, model):
    manifest = load_manifest(root)
    arrays, history, ids = {}, {}, {}
    for kind, loader in [("crop", crop_rows), ("video", video_rows)]:
        x, y, ids[kind] = loader(root, manifest, "train")
        mean, scale, weights, loss = fit(x, y)
        arrays.update({kind+"_mean": mean, kind+"_scale": scale, kind+"_weights": weights})
        history[kind] = {"examples": len(x), "initial_loss": loss[0], "final_loss": loss[-1]}
    label_records = [annotations(root, s["id"]) for s in manifest["samples"] if s["kind"] == "image"]
    metadata = {"schema_version": 1, "feature_version": FEATURE_VERSION, "classes": CLASSES,
                "questions": QUESTIONS, "manifest_sha256": digest(Path(root)/"manifest.json"),
                "annotation_sha256": hashlib.sha256(json.dumps(label_records, sort_keys=True).encode()).hexdigest(),
                "training_ids": ids, "history": history, "source": manifest["source"]}
    model = Path(model)
    model.parent.mkdir(parents=True, exist_ok=True)
    with model.open("wb") as output:
        np.savez(output, metadata=json.dumps(metadata), **arrays)
    return {"model": str(model), "sha256": digest(model), "history": history}


def load_model(path):
    path = Path(path)
    if not path.is_file():
        raise missing("trained model", path,
                      f"Run researchlab-demo train --root PATH_TO_BUNDLE --model {path}, or transfer the selected artifact.")
    try:
        with np.load(path, allow_pickle=False) as archive:
            arrays = {key: archive[key].copy() for key in archive.files if key != "metadata"}
            metadata = json.loads(str(archive["metadata"]))
        if (metadata["schema_version"] != 1 or metadata["feature_version"] != FEATURE_VERSION
                or metadata["classes"] != CLASSES or metadata["questions"] != QUESTIONS):
            raise ValueError("model contract")
        for kind, outputs in [("crop", 2), ("video", 3)]:
            if arrays[kind+"_weights"].shape != (13, outputs):
                raise ValueError("weights")
            if arrays[kind+"_mean"].shape != (12,) or arrays[kind+"_scale"].shape != (12,):
                raise ValueError("features")
            if np.any(arrays[kind+"_scale"] <= 0):
                raise ValueError("scale")
        if not all(np.isfinite(a).all() for a in arrays.values()):
            raise ValueError("nonfinite artifact")
        return arrays, metadata
    except (KeyError, ValueError, OSError) as error:
        raise DemoError(f"Invalid model artifact: {path}; restore/retrain it. See docs/OFFLINE_SETUP.md#model-artifacts") from error


def evaluate(root, model):
    manifest = load_manifest(root)
    arrays, _ = load_model(model)
    results = {}
    for kind, loader in [("crop", crop_rows), ("video", video_rows)]:
        results[kind] = {}
        for split in ["validation", "test"]:
            x, y, _ = loader(root, manifest, split)
            predicted = probabilities(arrays, kind, x)
            accuracy = np.mean(predicted.argmax(1) == y.argmax(1)) if kind == "crop" else np.mean((predicted >= .5) == y)
            results[kind][split] = {"examples": len(x), "accuracy": float(accuracy)}
    return {"model_sha256": digest(model), "data_source": manifest["source"], "metrics": results}


def predict(root, model, sample_id):
    manifest = load_manifest(root)
    sample = next((s for s in manifest["samples"] if s["id"] == sample_id), None)
    if sample is None:
        raise DemoError(f"Unknown sample ID: {sample_id}")
    arrays, _ = load_model(model)
    image = pixels(root, sample)
    kind = "crop" if sample["kind"] == "image" else "video"
    if kind == "crop":
        record = validate_annotations(annotations(root, sample_id), image.shape[1], image.shape[0])
        objects = []
        for annotation in record["annotations"]:
            x1, y1, x2, y2 = annotation["bounds"]
            crop = image[int(np.floor(y1)):int(np.ceil(y2)), int(np.floor(x1)):int(np.ceil(x2))]
            scores = probabilities(arrays, kind, image_features(crop)[None])[0]
            objects.append({"bounds": annotation["bounds"], "scores": dict(zip(CLASSES, map(float, scores)))})
        return {"sample_id": sample_id, "model_sha256": digest(model),
                "feature_version": FEATURE_VERSION, "objects": objects}
    x = np.mean([image_features(f) for f in image], axis=0)
    scores = probabilities(arrays, kind, x[None])[0]
    return {"sample_id": sample_id, "model_sha256": digest(model),
            "feature_version": FEATURE_VERSION,
            "scores": dict(zip(CLASSES if kind == "crop" else QUESTIONS, map(float, scores))),
            "scope": "procedural CPU baseline; no real-world accuracy claim"}
