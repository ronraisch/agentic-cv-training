import argparse
import json
from pathlib import Path

import numpy as np

from researchlab.pipeline import retrieve
from researchlab.sources import from_csv


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, default=Path("data/fixtures"))
    args = parser.parse_args()
    result = retrieve(
        from_csv(args.data / "samples.csv"),
        from_csv(args.data / "features.csv"),
        np.array([1.0, 0.0, 0.0, 0.0]),
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
