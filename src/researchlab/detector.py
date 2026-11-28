"""Train, evaluate and run a local YOLO11 detector on the labeling datasets."""

import argparse
from contextlib import redirect_stdout
import csv
import importlib.util
import json
import os
from pathlib import Path
import random
import sys

import numpy as np
from PIL import Image

from researchlab import demo, label_data


def runtime():
    if importlib.util.find_spec("ultralytics") is None:
        raise demo.DemoError("Missing dependency: ultralytics. Install the locked detector extra; "
                             "see docs/setup/OFFLINE_SETUP.md#detector-runtime.")
    os.environ["YOLO_AUTOINSTALL"] = "false"
    os.environ["YOLO_OFFLINE"] = "true"
    from ultralytics import YOLO, settings

    settings.update({"sync": False})
    return YOLO


def load(path):
    path = Path(path)
    if not path.is_file():
        raise demo.missing("YOLO checkpoint or architecture", path,
                           "Supply an approved local YOLO11 artifact. See docs/reference/DETECTOR.md.")
    if path.suffix.lower() not in {".pt", ".yaml"}:
        raise demo.DemoError(f"{path}: expected a local YOLO .pt checkpoint or .yaml architecture")
    return runtime()(str(path.resolve()))


def split_samples(samples, policy):
    partitions = {split: [s for s in samples if s["split"] == split] for split in label_data.SPLITS}
    if not all(partitions.values()):
        raise demo.DemoError("Training exports need train, validation and test images in the source manifest")
    if policy == "examples":
        candidates = partitions["train"] + partitions["validation"]
        random.Random(7).shuffle(candidates)
        boundary = len(partitions["train"])
        partitions["train"], partitions["validation"] = candidates[:boundary], candidates[boundary:]
    return partitions


def yolo_row(annotation, class_ids, width, height, task):
    x1, y1, x2, y2 = annotation["bounds"]
    if task == "obb":
        # Only independent source annotations can supply orientation for the OBB experiment.
        if "obb" not in annotation:
            raise demo.DemoError("OBB export requires oriented ground truth for every labeled object")
        coords = (np.asarray(annotation["obb"]) / [width, height]).ravel()
    else:
        coords = [(x1 + x2) / (2 * width), (y1 + y2) / (2 * height),
                  (x2 - x1) / width, (y2 - y1) / height]
    return f"{class_ids[annotation['label']]} " + " ".join(f"{v:.8f}" for v in coords)


def export(root, domain, output, policy="examples", task="detect"):
    from tempfile import TemporaryDirectory

    path, manifest, samples = label_data.load_collection(root, domain)
    demo.initialize_store(path, manifest)
    snapshot = demo.annotation_snapshot(path)
    partitions = split_samples(list(samples.values()), policy)
    classes = manifest["classes"]
    class_ids = {name: i for i, name in enumerate(classes)}
    output = Path(output).resolve()
    if output.exists():
        raise demo.DemoError(f"Choose a new export directory; {output} already exists")
    output.parent.mkdir(parents=True, exist_ok=True)
    groups = {split: {s["group_id"] for s in rows} for split, rows in partitions.items()}
    provenance = {"domain": domain, "source": manifest["source"], "task": task, "split_policy": policy,
                  "manifest_sha256": demo.digest(path / "manifest.json"), "classes": classes,
                  "train_validation_group_overlap": sorted(groups["train"] & groups["validation"]),
                  "samples": {}}
    with TemporaryDirectory(dir=output.parent) as staging:
        dataset = Path(staging) / "dataset"
        for split, rows in partitions.items():
            images = dataset / "images" / split
            labels = dataset / "labels" / split
            images.mkdir(parents=True)
            labels.mkdir(parents=True)
            has_objects = False
            for i, sample in enumerate(rows):
                image = demo.pixels(path, sample)
                height, width = image.shape[:2]
                record = demo.validate_annotations(snapshot[sample["id"]], width, height, classes)
                try:
                    lines = [yolo_row(item, class_ids, width, height, task) for item in record["annotations"]]
                except demo.DemoError as error:
                    raise demo.DemoError(f"{domain}/{sample['id']}: {error}") from error
                has_objects |= bool(lines)
                name = f"{i:06d}"
                Image.fromarray(image).save(images / f"{name}.png")
                (labels / f"{name}.txt").write_text("\n".join(lines))
                provenance["samples"][f"{split}/{name}"] = {
                    "id": sample["id"], "group_id": sample["group_id"], "sha256": sample["sha256"]}
            if not has_objects:
                raise demo.DemoError(f"{domain}/{split}: no annotated objects after splitting")
        # JSON is valid YAML. Explicit paths and split keys prevent upstream download fallbacks.
        config = {"path": str(output), "train": "images/train", "val": "images/validation",
                  "test": "images/test", "names": classes}
        (dataset / "dataset.yaml").write_text(json.dumps(config, indent=2))
        (dataset / "export.json").write_text(json.dumps(provenance, indent=2))
        dataset.rename(output)
    return {"data": str(output / "dataset.yaml"), **{k: v for k, v in provenance.items() if k != "samples"}}


def read_export(directory):
    directory = Path(directory).resolve()
    config_path = directory / "dataset.yaml"
    meta_path = directory / "export.json"
    for path in (config_path, meta_path):
        if not path.is_file():
            raise demo.missing("detector export", path, "Run researchlab-detector export; see docs/reference/DETECTOR.md.")
    meta = json.loads(meta_path.read_text())
    config = json.loads(config_path.read_text())
    expected = {"path": str(directory), "train": "images/train", "val": "images/validation",
                "test": "images/test", "names": meta["classes"]}
    if config != expected:
        raise demo.DemoError(f"{config_path}: export path or config changed; export at the final location")
    for split in label_data.SPLITS:
        images = {p.stem for p in (directory / "images" / split).glob("*.png")}
        labels = {p.stem for p in (directory / "labels" / split).glob("*.txt")}
        names = {key.split("/", 1)[1] for key in meta["samples"] if key.startswith(f"{split}/")}
        if not names or images != names or labels != names:
            raise demo.DemoError(f"{directory}: missing or unexpected images/labels in {split}; re-export the dataset")
    return directory, meta


def train(data, model, output, *, epochs=10, batch=8, imgsz=640, device="cpu"):
    directory, meta = read_export(data)
    output = Path(output).resolve()
    if output.exists():
        raise demo.DemoError(f"Choose a new run directory; {output} already exists")
    yolo = load(model)
    if yolo.task != meta["task"]:
        raise demo.DemoError(f"Model task {yolo.task} does not match export task {meta['task']}")
    from matplotlib import font_manager
    from ultralytics.utils import USER_CONFIG_DIR

    font = "Arial.ttf" if str(meta["classes"]).isascii() else "Arial.Unicode.ttf"
    font_path = USER_CONFIG_DIR / font
    if not font_path.is_file() and not any(Path(path).name == font for path in font_manager.findSystemFonts()):
        raise demo.missing("Ultralytics font", font_path,
                           f"Stage the approved {font} in this directory or set YOLO_CONFIG_DIR "
                           "to the directory containing it. See docs/reference/DETECTOR.md.")
    # Teaching baseline: fixed-LR SGD and aspect-ratio-sorted, unshuffled batches.
    yolo.train(data=str(directory / "dataset.yaml"), project=str(output.parent), name=output.name,
               epochs=epochs, batch=batch, imgsz=imgsz, device=device, optimizer="SGD",
               lr0=0.01, lrf=1.0, warmup_epochs=0, rect=True, amp=False, workers=0,
               seed=7, val=False, plots=False)
    saved = Path(yolo.trainer.save_dir)
    (saved / "export.json").write_text(json.dumps(meta, indent=2))
    loss_csv = saved / "results.csv"
    with loss_csv.open(newline="") as stream:
        rows = [{key.strip(): float(value) for key, value in row.items()} for row in csv.DictReader(stream)]
    losses = [field for field in rows[0] if field.startswith("train/")]
    from matplotlib.figure import Figure

    figure = Figure(figsize=(8, 3 * len(losses)), layout="constrained")
    for field, axis in zip(losses, figure.subplots(len(losses), 1, squeeze=False).flat):
        axis.plot([row["epoch"] for row in rows], [row[field] for row in rows], marker=".")
        axis.set(xlabel="Epoch", ylabel=field)
    loss_plot = saved / "training-loss.png"
    figure.savefig(loss_plot, dpi=140)
    return {"checkpoint": str(saved / "weights/last.pt"), "loss_csv": str(loss_csv),
            "loss_plot": str(loss_plot), "export": str(saved / "export.json")}


def predict_image(model, image, *, device="cpu", imgsz=640, confidence=0.25):
    result = model.predict(source=Image.fromarray(image), conf=confidence, max_det=300, imgsz=imgsz,
                           device=device, verbose=False)[0]
    detections = result.obb if result.obb is not None else result.boxes
    objects = []
    polygons = result.obb.xyxyxyxy.tolist() if result.obb is not None else [None] * len(detections)
    for bounds, label, score, corners in zip(detections.xyxy.tolist(), detections.cls.tolist(),
                                              detections.conf.tolist(), polygons):
        item = {"type": "rectangle", "bounds": bounds, "label": result.names[int(label)], "score": score}
        if corners is not None:
            item["obb"] = corners
        objects.append(item)
    return objects


def iou(left, right):
    lo = np.maximum(left[:2], right[:2])
    hi = np.minimum(left[2:], right[2:])
    intersection = np.maximum(hi - lo, 0).prod()
    area = np.prod(np.subtract(left[2:], left[:2])) + np.prod(np.subtract(right[2:], right[:2]))
    return float(intersection / (area - intersection)) if area > intersection else 0.0


def match_predictions(predictions, targets, threshold):
    matches, available = [], set(range(len(targets)))
    for prediction in sorted(predictions, key=lambda item: -item["score"]):
        candidates = [(iou(prediction["bounds"], targets[i]["bounds"]), i)
                      for i in sorted(available) if targets[i]["label"] == prediction["label"]]
        overlap, index = max(candidates, default=(0, -1))
        matched = overlap >= threshold and index >= 0
        if matched:
            available.remove(index)
        matches.append((prediction["score"], matched))
    return matches


def roc(matches):
    ordered = sorted(matches, key=lambda item: -item[0])
    tp = np.cumsum([0] + [int(matched) for _, matched in ordered])
    fp = np.arange(len(tp)) - tp
    if not tp[-1] or not fp[-1]:
        return None, [], []
    ends = [i for i in range(1, len(ordered)) if ordered[i - 1][0] != ordered[i][0]]
    points = [0, *ends, len(ordered)]
    x, y = fp[points] / fp[-1], tp[points] / tp[-1]
    return float(np.trapezoid(y, x)), x.tolist(), y.tolist()


def evaluate(data, model, output, *, split="validation", imgsz=640, device="cpu"):
    directory, meta = read_export(data)
    yolo = load(model)
    if yolo.task != meta["task"] or list(yolo.names.values()) != meta["classes"]:
        raise demo.DemoError("The checkpoint task and class map must match the labeled export")
    frames = []
    for path in sorted((directory / "images" / split).glob("*.png")):
        with Image.open(path) as picture:
            pixels = np.asarray(picture.convert("RGB"))
        height, width = pixels.shape[:2]
        targets = []
        for row in (directory / "labels" / split / f"{path.stem}.txt").read_text().splitlines():
            label, *coords = row.split()
            if meta["task"] == "obb":
                corners = np.asarray(coords, dtype=float).reshape(4, 2) * [width, height]
                bounds = [*corners.min(0), *corners.max(0)]
            else:
                x, y, w, h = map(float, coords)
                bounds = [(x - w / 2) * width, (y - h / 2) * height,
                          (x + w / 2) * width, (y + h / 2) * height]
            targets.append({"label": meta["classes"][int(label)], "bounds": bounds})
        frames.append((predict_image(yolo, pixels, device=device, imgsz=imgsz, confidence=0.001), targets))
    ground_truth = sum(len(targets) for _, targets in frames)
    if not ground_truth:
        raise demo.DemoError(f"{directory}/labels/{split}: no labeled objects; export again.")
    reports = []
    for threshold in (0.2, 0.5, 0.75, 0.9):
        matches = [pair for preds, targets in frames for pair in match_predictions(preds, targets, threshold)]
        auc, fpr, tpr = roc(matches)
        true_positives = sum(matched for _, matched in matches)
        reports.append({"iou": threshold, "roc_auc": auc, "fpr": fpr, "tpr": tpr,
                        "true_positives": true_positives, "recall": true_positives / ground_truth})
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    from matplotlib.figure import Figure

    figure = Figure(figsize=(10, 4), layout="constrained")
    roc_axis, recall_axis = figure.subplots(1, 2)
    for entry in reports:
        if entry["roc_auc"] is not None:
            roc_axis.plot(entry["fpr"], entry["tpr"],
                          label=f"IoU {entry['iou']:.2f} (AUC {entry['roc_auc']:.2f})")
    if roc_axis.lines:
        roc_axis.legend()
    else:
        roc_axis.text(.5, .5, "ROC undefined: missing a positive or negative match class",
                      ha="center", wrap=True, transform=roc_axis.transAxes)
    roc_axis.set(xlabel="False-positive rate among predictions",
                 ylabel="True-positive rate among predictions", xlim=(0, 1), ylim=(0, 1))
    recall_axis.plot([entry["iou"] for entry in reports], [entry["recall"] for entry in reports], marker="o")
    recall_axis.set(xlabel="Matching IoU", ylabel="Matched fraction of ground truth", ylim=(0, 1))
    figure.savefig(output / "localization.png", dpi=140)

    report = {"data": str(directory), "split_policy": meta["split_policy"], "split": split,
              "checkpoint_sha256": demo.digest(model), "images": len(frames), "ground_truth": ground_truth,
              "roc_auc_at_iou_90": reports[-1]["roc_auc"], "iou_geometry": "axis_aligned",
              "confidence_floor": 0.001, "max_detections_per_image": 300,
              "iou_sweep": reports}
    (output / "evaluation.json").write_text(json.dumps(report, indent=2))
    with (output / "iou-sweep.csv").open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=["iou", "roc_auc", "true_positives", "recall"],
                                extrasaction="ignore")
        writer.writeheader()
        writer.writerows(reports)
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    exporter = commands.add_parser("export")
    exporter.add_argument("--root", type=Path, default=Path("data/labeling"))
    exporter.add_argument("--domain", choices=label_data.DOMAINS, required=True)
    exporter.add_argument("--output", type=Path, required=True)
    exporter.add_argument("--split-policy", choices=("examples", "grouped"), default="examples")
    exporter.add_argument("--task", choices=("detect", "obb"), default="detect")
    for command in ("train", "evaluate", "predict"):
        sub = commands.add_parser(command)
        sub.add_argument("--model", required=True, type=Path)
        sub.add_argument("--device", default="cpu")
        sub.add_argument("--imgsz", default=640, type=int)
        if command == "predict":
            sub.add_argument("--input", required=True, type=Path)
            continue
        sub.add_argument("--data", required=True, type=Path)
        sub.add_argument("--output", required=True, type=Path)
        if command == "train":
            sub.add_argument("--epochs", default=10, type=int)
            sub.add_argument("--batch", default=8, type=int)
        else:
            sub.add_argument("--split", choices=("validation", "test"), default="validation")
    args = parser.parse_args(argv)
    try:
        with redirect_stdout(sys.stderr):
            if args.command == "export":
                result = export(args.root, args.domain, args.output, args.split_policy, args.task)
            elif args.command == "train":
                result = train(args.data, args.model, args.output, epochs=args.epochs,
                               batch=args.batch, imgsz=args.imgsz, device=args.device)
            elif args.command == "evaluate":
                result = evaluate(args.data, args.model, args.output, split=args.split,
                                  imgsz=args.imgsz, device=args.device)
            else:
                with Image.open(args.input) as image:
                    result = predict_image(load(args.model), np.asarray(image.convert("RGB")),
                                           imgsz=args.imgsz, device=args.device)
        print(json.dumps(result, indent=2))
        return 0
    except (ValueError, OSError, KeyError, RuntimeError, ImportError) as error:
        print(f"ERROR: {error}\nSee docs/setup/OFFLINE_SETUP.md#detector-runtime", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
