"""Join metadata and feature rows into the public retrieval report."""

import numpy as np
import pandas as pd

from researchlab.numerics import rank


def retrieve(samples: pd.DataFrame, features: pd.DataFrame, query: np.ndarray, k: int = 3):
    joined = samples.merge(features, on="sample_id")
    matrix = np.stack(joined["embedding"].map(lambda s: np.array(s.split(), dtype=float)))
    selected = rank(matrix, query, k)
    return joined.iloc[selected][["sample_id", "scene_id", "split"]].to_dict("records")


def split_samples(samples: pd.DataFrame):
    return samples.iloc[::2], samples.iloc[1::2]
