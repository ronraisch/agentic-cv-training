"""Public checks for the supported local detector path."""

import subprocess
import sys

import numpy as np
import pytest

from researchlab import detector


@pytest.fixture(scope="module")
def trained(tmp_path_factory):
    pytest.importorskip("torch")
    path = tmp_path_factory.mktemp("detector") / "model.npz"
    result = detector.train(path)
    return path, result


def test_detector_training_reload_and_new_input(trained, tmp_path):
    torch = pytest.importorskip("torch")
    path, result = trained
    assert result["final_loss"] < result["initial_loss"] * .1
    heldout = detector.evaluate(detector.load(path), detector.fixture(80, 172))
    assert heldout["mean_iou"] > .65
    assert heldout["class_accuracy"] > .95
    assert heldout["presence_accuracy"] > .95
    images = detector.fixture(3, 999)[0]
    actual = detector.predict_batches(path, images)
    assert len(actual["boxes_xyxy"]) == 3
    assert all(0 <= p <= 1 for p in actual["object_probability"])
    box = torch.tensor(actual["boxes_xyxy"])
    assert (box[:, 2:] >= box[:, :2]).all()
    input_path = tmp_path / "input.npy"
    np.save(input_path, images.numpy())
    process = subprocess.run([sys.executable, "-m", "researchlab.detector", "predict",
                              "--model", str(path), "--input", str(input_path)],
                             capture_output=True, text=True)
    assert process.returncode == 0, process.stderr
    import json
    assert json.loads(process.stdout) == actual


def test_detector_missing_model_and_input(trained, tmp_path, capsys):
    with pytest.raises(ValueError, match="Missing detector artifact.*OFFLINE_SETUP"):
        detector.load(tmp_path / "absent.npz")
    assert detector.main(["predict", "--model", str(trained[0])]) == 2
    assert "OFFLINE_SETUP.md" in capsys.readouterr().err


def test_detector_missing_runtime(monkeypatch):
    monkeypatch.setattr(detector.importlib.util, "find_spec", lambda name: None)
    with pytest.raises(ValueError, match="Missing dependency: torch.*OFFLINE_SETUP"):
        detector.runtime()
