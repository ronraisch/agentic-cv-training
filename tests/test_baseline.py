from pathlib import Path

import numpy as np

from researchlab.numerics import normalize
from researchlab.pipeline import retrieve
from researchlab.sources import from_csv


def test_normalize_happy_path():
    np.testing.assert_allclose(normalize(np.array([[3.0, 4.0]])), [[0.6, 0.8]])


def test_public_result_shape():
    root = Path("data/fixtures")
    out = retrieve(
        from_csv(root / "samples.csv"),
        from_csv(root / "features.csv"),
        np.array([1.0, 0.0, 0.0, 0.0]),
        k=2,
    )
    assert len(out) == 2
    assert set(out[0]) == {"sample_id", "scene_id", "split"}
