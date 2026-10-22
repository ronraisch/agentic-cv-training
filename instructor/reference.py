"""Executable reference for core contracts, not the only acceptable design."""

import numpy as np
import pandas as pd


def normalize(features):
    x = np.asarray(features)
    if x.ndim != 2 or not np.issubdtype(x.dtype, np.floating) or not np.isfinite(x).all():
        raise ValueError("Expected a finite floating rank-2 array")
    # Scale before taking norms to avoid overflow/underflow for extreme finite values.
    scale = np.max(np.abs(x), axis=1, keepdims=True) if x.shape[1] else np.zeros((len(x), 1))
    scaled = np.divide(x, scale, out=np.zeros_like(x), where=scale != 0)
    norms = np.linalg.norm(scaled, axis=1, keepdims=True)
    return np.divide(scaled, norms, out=np.zeros_like(x), where=norms != 0)


def rank(features, query, k):
    x = normalize(features)
    q = np.asarray(query)
    if q.shape != (x.shape[1],) or not np.issubdtype(q.dtype, np.floating):
        raise ValueError("Query shape/dtype mismatch")
    if not np.isfinite(q).all() or not np.any(q):
        raise ValueError("Query must be finite and nonzero")
    if isinstance(k, bool) or not isinstance(k, (int, np.integer)) or not 0 <= k <= len(x):
        raise ValueError("Invalid k")
    q = normalize(q[None])[0]
    return np.argsort(-(x @ q), kind="stable")[:k]


def retrieve(samples, features, query, k=3):
    if not samples.sample_id.is_unique or not features.sample_id.is_unique:
        raise ValueError("Duplicate sample_id")
    joined = samples.merge(features, on="sample_id", how="left", validate="one_to_one")
    if joined.embedding.isna().any():
        raise ValueError("Missing embeddings")
    if joined.empty:
        if k != 0:
            raise ValueError("Invalid k for empty data")
        return []
    matrix = np.stack(joined.embedding.map(lambda s: np.array(s.split(), dtype=float)))
    return joined.iloc[rank(matrix, query, k)][["sample_id", "scene_id", "split"]].to_dict(
        "records"
    )


def split_samples(samples):
    scenes = sorted(samples.scene_id.unique())
    held_out = set(scenes[::2])
    mask = samples.scene_id.isin(held_out)
    return samples.loc[~mask].copy(), samples.loc[mask].copy()


def from_http(client, url):
    rows, seen, cursor = [], set(), None
    for _ in range(1000):
        page = client.get_json(url, params={"cursor": cursor} if cursor is not None else None)
        if not isinstance(page, dict) or not isinstance(page.get("items"), list):
            raise ValueError("Invalid page schema")
        if not all(isinstance(row, dict) and "sample_id" in row for row in page["items"]):
            raise ValueError("Invalid item schema")
        rows.extend(page["items"])
        cursor = page.get("next_cursor")
        if cursor is None:
            return pd.DataFrame(rows)
        if not isinstance(cursor, str) or not cursor or cursor in seen:
            raise ValueError("Invalid or repeated cursor")
        seen.add(cursor)
    raise ValueError("Pagination limit exceeded")


def embed(model, batches):
    import torch

    original_mode = model.training
    outputs = []
    device = next(model.parameters()).device
    try:
        model.eval()
        with torch.inference_mode():
            for batch in batches:
                if batch.ndim != 2 or batch.shape[1] != 4:
                    raise ValueError("Expected [N,4]")
                if not batch.is_floating_point() or not torch.isfinite(batch).all():
                    raise ValueError("Expected finite floating values")
                outputs.append(model(batch.to(device)).cpu())
        return torch.cat(outputs) if outputs else torch.empty((0, 4))
    finally:
        model.train(original_mode)
