"""Run with COURSE_IMPL=reference for oracle self-check, otherwise starter."""

import os
from pathlib import Path

import httpx
import numpy as np
import pandas as pd
import pytest

from researchlab.http import HTTPClient

if os.environ.get("COURSE_IMPL") == "reference":
    from instructor.reference import from_http, normalize, rank, retrieve, split_samples
else:
    from researchlab.numerics import normalize, rank
    from researchlab.pipeline import retrieve, split_samples
    from researchlab.sources import from_http


def test_no_mutation_and_finite_zero():
    x = np.array([[3.0, 4.0], [0.0, 0.0]])
    before = x.copy()
    out = normalize(x)
    np.testing.assert_array_equal(x, before)
    np.testing.assert_allclose(out, [[0.6, 0.8], [0.0, 0.0]])
    assert not np.shares_memory(x, out)


@pytest.mark.parametrize(
    "x",
    [
        np.array([[1, 2]]),
        np.array([1.0, 2.0]),
        np.array([[np.nan, 0.0]]),
        np.array([[np.inf, 0.0]]),
    ],
)
def test_invalid_arrays(x):
    with pytest.raises(ValueError):
        normalize(x)


def test_rank_ties_and_k():
    x = np.array([[1.0, 0.0], [1.0, 0.0], [0.0, 1.0]])
    assert rank(x, np.array([1.0, 0.0]), 2).tolist() == [0, 1]
    assert rank(x, np.array([1.0, 0.0]), 0).size == 0
    with pytest.raises(ValueError):
        rank(x, np.array([1.0, 0.0]), -1)
    with pytest.raises(ValueError):
        rank(x, np.array([0.0, 0.0]), 1)


def test_scene_split():
    s = pd.read_csv(Path("data/fixtures/samples.csv"))
    a, b = split_samples(s)
    assert not set(a.scene_id) & set(b.scene_id)
    assert set(a.sample_id) | set(b.sample_id) == set(s.sample_id)


def test_join_rejects_missing_and_duplicate_ids():
    s = pd.read_csv("data/fixtures/samples.csv")
    f = pd.read_csv("data/fixtures/features.csv")
    with pytest.raises(ValueError):
        retrieve(s, pd.concat([f, f.iloc[:1]]), np.array([1.0, 0.0, 0.0, 0.0]))
    with pytest.raises(ValueError):
        retrieve(s, f.iloc[:1], np.array([1.0, 0.0, 0.0, 0.0]))


def test_pagination():
    calls = []

    def handler(request):
        cursor = request.url.params.get("cursor")
        calls.append(cursor)
        return httpx.Response(
            200,
            json={
                "items": [{"sample_id": "s2" if cursor else "s1"}],
                "next_cursor": None if cursor else "p2",
            },
        )

    with httpx.Client(transport=httpx.MockTransport(handler)) as raw:
        result = from_http(HTTPClient(raw), "https://fixture.invalid/data")
    assert result.sample_id.tolist() == ["s1", "s2"]
    assert calls == [None, "p2"]


def test_cursor_cycle():
    def handler(request):
        return httpx.Response(200, json={"items": [], "next_cursor": "same"})

    with httpx.Client(transport=httpx.MockTransport(handler)) as raw, pytest.raises(ValueError):
        from_http(HTTPClient(raw), "https://fixture.invalid/data")
