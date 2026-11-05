"""Contracts for the frozen image/video components."""

import json
import os
from pathlib import Path

import numpy as np
import pytest

from researchlab.components import IoUTracker, Models, digest, manifest_rows, write_images


def test_manifest_keeps_order_and_resolves_paths(tmp_path):
    manifest = tmp_path / "images.jsonl"
    records = [{"id": value, "path": f"{value}.png"} for value in ["b", "a"]]
    manifest.write_text("\n".join(map(json.dumps, records)))
    rows = list(manifest_rows(manifest))
    assert [row[0]["id"] for row in rows] == ["b", "a"]
    assert rows[0][1] == tmp_path / "b.png"


def test_manifest_rejects_duplicate_identity(tmp_path):
    path = tmp_path / "images.jsonl"
    row = json.dumps({"id": "same", "path": "image.png"})
    path.write_text(row + "\n" + row)
    with pytest.raises(ValueError, match="unique"):
        list(manifest_rows(path))


def test_missing_or_different_model_has_recovery_message(tmp_path):
    models = Models(tmp_path)
    with pytest.raises(ValueError, match="fetch"):
        models.session("plate")
    (tmp_path / "plate.onnx").write_bytes(b"different artifact")
    with pytest.raises(ValueError, match="checksum mismatch"):
        models.session("plate")


def test_tracker_reuses_only_matching_class_and_expires_tracks():
    tracker = IoUTracker()
    car = {"box_xyxy": [10, 10, 50, 50], "class": "car", "score": .9}
    first = tracker.update([car], 0)[0]
    moved = {**car, "box_xyxy": [12, 10, 52, 50]}
    assert tracker.update([moved], 1)[0]["track_id"] == first["track_id"]
    assert tracker.update([{**car, "class": "bus"}], 2)[0]["track_id"] != first["track_id"]
    assert tracker.update([car], 9)[0]["track_id"] != first["track_id"]
    assert "track_id" not in car


def test_image_writer_retains_empty_predictions_and_identity(tmp_path):
    cv2 = pytest.importorskip("cv2")
    pytest.importorskip("onnxruntime")
    path = tmp_path / "sample.png"
    assert cv2.imwrite(str(path), np.zeros((30, 40, 3), np.uint8))
    manifest = tmp_path / "images.jsonl"
    manifest.write_text(json.dumps({"id": "a", "path": path.name}) + "\n")

    class EmptyDetector:
        def vehicles(self, image, threshold):
            return []

    output = tmp_path / "output.jsonl"
    write_images(EmptyDetector(), manifest, output, "detect", .5)
    row = json.loads(output.read_text())
    assert row["id"] == "a" and row["detections"] == []
    assert row["gsd_m"] is None and row["image_size_hw"] == [30, 40]


@pytest.mark.skipif(not os.environ.get("RESEARCHLAB_COMPONENT_MODELS")
                    or not os.environ.get("RESEARCHLAB_COMPONENT_IMAGE"),
                    reason="Requires local pinned models and a real positive plate image")
def test_real_models_reload_and_video_roundtrip(tmp_path):
    cv2 = pytest.importorskip("cv2")
    from researchlab.components import ASSETS, write_tracks

    root = Path(os.environ["RESEARCHLAB_COMPONENT_MODELS"])
    image_path = Path(os.environ["RESEARCHLAB_COMPONENT_IMAGE"])
    image = cv2.imread(str(image_path))
    assert image is not None
    manifest = tmp_path / "images.jsonl"
    manifest.write_text(json.dumps({"id": "real", "path": str(image_path)}) + "\n")
    outputs = []
    for index in range(2):
        output = tmp_path / f"lpr-{index}.jsonl"
        write_images(Models(root), manifest, output, "lpr", .25)
        outputs.append(json.loads(output.read_text()))
    assert outputs[0] == outputs[1]
    assert outputs[0]["detections"] and outputs[0]["detections"][0]["text"]
    assert digest(root / "plate.onnx") == ASSETS["plate"]["sha256"]
    assert Models(root).vehicles(image, .5)
    video = tmp_path / "sequence.avi"
    h, w = image.shape[:2]
    image = cv2.resize(image, (w // 2 * 2, h // 2 * 2))
    writer = cv2.VideoWriter(str(video), cv2.VideoWriter_fourcc(*"MJPG"), 5,
                             (image.shape[1], image.shape[0]))
    assert writer.isOpened()
    for shift in range(3):
        writer.write(np.roll(image, shift, axis=1))
    writer.release()
    output = tmp_path / "tracks.jsonl"
    result = write_tracks(Models(root), video, output, "sequence")
    rows = [json.loads(line) for line in output.read_text().splitlines()]
    assert result["frames"] == 3
    assert [row["frame_index"] for row in rows] == [0, 1, 2]
    assert [row["timestamp_s"] for row in rows] == [0, .2, .4]
    assert all(row["detections"] for row in rows)
    first_id = rows[0]["detections"][0]["track_id"]
    assert any(p["track_id"] == first_id for p in rows[2]["detections"])
