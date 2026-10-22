"""Feature operations used by downstream researchers."""

import numpy as np


def normalize(features: np.ndarray) -> np.ndarray:
    features /= np.linalg.norm(features, axis=1, keepdims=True)
    return features


def rank(features: np.ndarray, query: np.ndarray, k: int) -> np.ndarray:
    scores = normalize(features) @ query
    return np.argsort(scores)[::-1][:k]
