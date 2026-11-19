"""Checks for the detector's data conversion and evaluation contracts."""

import json

import numpy as np
import pytest
from PIL import Image

from researchlab import demo, detector, label_data


def test_export_reads_saved_labels_and_preserves_grouped_test(tmp_path):
    root = tmp_path / "labeling" / "satellite"
    root.mkdir(parents=True)
    samples = []
    for i, split in enumerate(["train"] * 4 + ["validation"] * 2 + ["test"]):
        image = root / f"{i}.png"
        Image.fromarray(np.full((20, 40, 3), i, dtype="uint8")).save(image)
        samples.append({"id": str(i), "group_id": split, "split": split, "path": image.name,
                        "annotations": [{"type": "rectangle", "label": "ship", "bounds": [4, 4, 20, 12],
                                         "obb": [[4, 4], [20, 4], [20, 12], [4, 12]]}]})
    label_data.write_manifest(root, "satellite", "export contract fixture", ["ship"], samples)
    demo.initialize_store(root, demo.load_manifest(root))
    record = demo.annotations(root, "0")
    record["annotations"][0]["bounds"] = [4, 4, 12, 12]
    demo.annotations(root, "0", record)

    output = tmp_path / "hbb"
    detector.export(root.parent, "satellite", output, policy="grouped")
    _, manifest = detector.read_export(output)
    row = (output / "labels/train/000000.txt").read_text().split()
    assert list(map(float, row)) == [0, .2, .4, .2, .4]
    assert manifest["samples"]["test/000000"]["id"] == "6"
    assert manifest["train_validation_group_overlap"] == []

    output = tmp_path / "obb"
    detector.export(root.parent, "satellite", output, task="obb")
    assert len((output / "labels/train/000000.txt").read_text().split()) == 9
    assert json.loads((output / "export.json").read_text())["train_validation_group_overlap"]


def test_evaluation_matches_only_once_and_uses_confidence():
    targets = [{"label": "ship", "bounds": [0, 0, 10, 10]}]
    predictions = [{**targets[0], "score": score} for score in (.1, .9)]
    matches = detector.match_predictions(predictions, targets, .9)
    assert matches == [(.9, True), (.1, False)]
    assert detector.roc(matches)[0] == 1
    assert detector.roc([(.5, False)])[0] is None
    assert detector.match_predictions([{**predictions[0], "label": "car"}], targets, .5) == [(.1, False)]


def test_detector_missing_model_and_runtime(monkeypatch, tmp_path):
    with pytest.raises(ValueError, match="Missing YOLO.*OFFLINE_SETUP"):
        detector.load(tmp_path / "absent.pt")
    monkeypatch.setattr(detector.importlib.util, "find_spec", lambda name: None)
    with pytest.raises(ValueError, match="Missing dependency: ultralytics.*OFFLINE_SETUP"):
        detector.runtime()


def test_real_coco_cpu_training_and_fresh_evaluation(tmp_path):
    import os
    from pathlib import Path
    import shutil

    source = os.environ.get("RESEARCHLAB_COCO8")
    if source is None:
        pytest.skip("Stage the COCO8 real-image fixture for the detector integration test")
    pytest.importorskip("torch").set_num_threads(2)
    detector.runtime()
    import ultralytics

    root = tmp_path / "coco"
    root.mkdir()
    original = Path(source)
    images = sorted((original / "images").glob("*/*.jpg"))
    assert len(images) == 8
    samples = []
    splits = ("train",) * 4 + ("validation",) * 2 + ("test",) * 2
    for image, split in zip(images, splits):
        with Image.open(image) as frame:
            width, height = frame.size
        annotations = []
        labels = original / "labels" / image.parent.name / f"{image.stem}.txt"
        for row in labels.read_text().splitlines():
            _, x, y, w, h = map(float, row.split())
            bounds = [max(0, (x - w / 2) * width), max(0, (y - h / 2) * height),
                      min(width, (x + w / 2) * width), min(height, (y + h / 2) * height)]
            annotations.append({"type": "rectangle", "label": "object", "bounds": bounds})
        shutil.copyfile(image, root / image.name)
        samples.append({"id": image.stem, "group_id": image.stem, "path": image.name,
                        "split": split, "annotations": annotations})
    label_data.write_manifest(root, "coco", "COCO8 / COCO 2017", ["object"], samples)
    architecture = tmp_path / "yolo11n.yaml"
    shutil.copyfile(Path(ultralytics.__file__).parent / "cfg/models/11/yolo11.yaml", architecture)
    data = tmp_path / "export"
    detector.export(tmp_path, "coco", data, policy="grouped")
    output = tmp_path / "run"
    result = detector.train(data, architecture, output, epochs=2, batch=2, imgsz=96)
    assert Path(result["loss_plot"]).is_file()
    checkpoint = Path(result["checkpoint"])
    report = detector.evaluate(data, checkpoint, output / "eval", split="test", imgsz=96)
    assert report["images"] == 2 and report["ground_truth"] > 0
    assert report["checkpoint_sha256"] == demo.digest(checkpoint)
    assert (output / "eval/localization.png").is_file()
