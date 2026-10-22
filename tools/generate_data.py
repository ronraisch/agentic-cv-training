"""Deterministic local stress dataset. Run from the repository root."""

import argparse
import sqlite3
from pathlib import Path

import numpy as np
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--rows", type=int, default=10000)
args = parser.parse_args()
if args.rows < 1:
    parser.error("rows must be positive")
root = Path("data/generated")
root.mkdir(parents=True, exist_ok=True)
rng = np.random.default_rng(42)
data = pd.DataFrame(
    {
        "sample_id": [f"s{i}" for i in range(args.rows)],
        "scene_id": [f"scene-{i // 8}" for i in range(args.rows)],
        "split": ["train" if i % 2 else "test" for i in range(args.rows)],
        "value": rng.normal(size=args.rows),
    }
)
data.to_csv(root / "samples.csv", index=False)
with sqlite3.connect(root / "catalog.sqlite") as conn:
    data.to_sql("samples", conn, if_exists="replace", index=False)
print(f"Wrote {args.rows} rows to {root}")
