"""Release checks for the operational baseline and actionable offline setup errors."""

from http.server import ThreadingHTTPServer
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import threading
from urllib.request import Request, urlopen

import numpy as np
import pytest

from researchlab import demo, demo_cli, demo_web


def baseline(tmp_path):
    root = tmp_path / "bundle"
    demo.prepare(root)
    model = root / "models/baseline.npz"
    demo.train(root, model)
    return root, model


def test_training_updates_weights_and_reloads_in_new_process(tmp_path):
    root, model = baseline(tmp_path)
    arrays, metadata = demo.load_model(model)
    for kind in ("crop", "video"):
        assert np.any(arrays[kind + "_weights"] != 0)
        assert metadata["history"][kind]["final_loss"] < metadata["history"][kind]["initial_loss"]
    for result in demo.evaluate(root, model)["metrics"].values():
        assert result["test"]["accuracy"] >= .9
    prediction = demo.predict(root, model, "video-030")
    fresh = subprocess.run(
        [sys.executable, "-m", "researchlab.demo_cli", "predict", "--root", str(root),
         "--model", str(model), "--sample", "video-030"],
        capture_output=True, text=True, check=True,
    )
    assert json.loads(fresh.stdout) == prediction
    assert prediction["model_sha256"] == demo.digest(model)


def test_current_saved_annotations_reach_training(tmp_path):
    root, model = baseline(tmp_path)
    before, before_meta = demo.load_model(model)
    record = demo.annotations(root, "image-000")
    record["annotations"][0]["label"] = "building"
    demo.annotations(root, "image-000", record)
    assert demo.annotations(root, "image-000") == record
    x, y, ids = demo.crop_rows(root, demo.load_manifest(root), "train")
    assert y[ids.index("image-000")].tolist() == [0., 1.]
    assert np.isfinite(x).all()
    demo.train(root, model)
    after, after_meta = demo.load_model(model)
    assert before_meta["annotation_sha256"] != after_meta["annotation_sha256"]
    assert not np.array_equal(before["crop_weights"], after["crop_weights"])
    demo.prepare(root)
    assert demo.annotations(root, "image-000") == record


def test_labeling_api_save_reload_and_loaded_model(tmp_path):
    root, model = baseline(tmp_path)
    server = ThreadingHTTPServer(("127.0.0.1", 0), demo_web.handler(root, model))
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base = f"http://127.0.0.1:{server.server_port}"
    def get(path):
        with urlopen(base + path, timeout=5) as response:
            return json.load(response)
    def post(path, body):
        request = Request(base+path, json.dumps(body).encode(), {"Content-Type": "application/json"})
        with urlopen(request, timeout=5) as response:
            return json.load(response)
    try:
        with urlopen(base, timeout=5) as response:
            assert b"Peanuach labeling" in response.read()
        with urlopen(base+"/api/image?id=image-000", timeout=5) as response:
            assert response.read().startswith(b"\x89PNG")
        record = get("/api/annotations?id=image-000")
        record["annotations"][0]["bounds"] = [7, 6, 39, 24]
        assert post("/api/annotations", record) == record
        assert get("/api/annotations?id=image-000") == record
        assert demo.annotations(root, "image-000") == record
        assert get("/health")["model_sha256"] == demo.digest(model)
        assert post("/api/predict", {"sample_id": "image-000"})["objects"]
        assert post("/api/predict", {"sample_id": "video-030"})["model_sha256"] == demo.digest(model)
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)


@pytest.mark.parametrize("asset", ["manifest", "array", "model", "store"])
def test_missing_assets_stop_with_path_and_setup_instructions(tmp_path, capsys, asset):
    root = tmp_path / "bundle"
    model = root / "models/baseline.npz"
    if asset != "manifest":
        demo.prepare(root)
    if asset == "array":
        (root / "image-000.npy").unlink()
    if asset == "store":
        (root / "labels.sqlite").unlink()
    command = "train" if asset != "model" else "predict"
    assert demo_cli.main([command, "--root", str(root), "--model", str(model)]) == 2
    error = capsys.readouterr().err
    assert str(root) in error
    assert "docs/OFFLINE_SETUP.md" in error
    assert "No runtime download was attempted" in error


def test_missing_python_dependency_has_offline_remediation(monkeypatch, capsys):
    monkeypatch.setattr(importlib.util, "find_spec", lambda module: None)
    assert demo_cli.main(["train"]) == 2
    assert "docs/OFFLINE_SETUP.md#python-runtime" in capsys.readouterr().err


def test_bundle_groups_and_file_checksums_are_checked(tmp_path):
    root = tmp_path / "bundle"
    manifest = demo.prepare(root)
    assert len(manifest["samples"]) == 96
    groups = {}
    for sample in manifest["samples"]:
        groups.setdefault(sample["group_id"], set()).add(sample["split"])
    assert all(len(splits) == 1 for splits in groups.values())
    (root / "image-000.npy").write_bytes(b"broken transfer")
    with pytest.raises(demo.DemoError, match="Checksum mismatch"):
        demo.load_manifest(root)


def test_packaged_ui_exists():
    assert Path(demo_web.__file__).with_name("static").joinpath("index.html").is_file()


def test_catalog_missing_fixture_has_recovery_message(tmp_path, capsys):
    from researchlab.cli import main
    assert main(["--data", str(tmp_path)]) == 2
    message = capsys.readouterr().err
    assert str(tmp_path / "samples.csv") in message
    assert "docs/OFFLINE_SETUP.md" in message
