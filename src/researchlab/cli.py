import argparse
import json
from pathlib import Path
import sys


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, default=Path("data/fixtures"))
    args = parser.parse_args(argv)
    for name in ("samples.csv", "features.csv"):
        path = args.data / name
        if not path.is_file():
            print(f"Missing catalog fixture: {path}. Restore the fixture directory from the selected "
                  "source revision or pass --data PATH. See docs/OFFLINE_SETUP.md#local-fixture-data. "
                  "No runtime download was attempted.", file=sys.stderr)
            return 2
    try:
        import numpy as np
        from researchlab.pipeline import retrieve
        from researchlab.sources import from_csv
    except ModuleNotFoundError as error:
        print(f"Missing dependency: {error.name}. Install the approved locked environment; "
              "see docs/OFFLINE_SETUP.md#python-runtime. No runtime installation was attempted.",
              file=sys.stderr)
        return 2
    result = retrieve(
        from_csv(args.data / "samples.csv"),
        from_csv(args.data / "features.csv"),
        np.array([1.0, 0.0, 0.0, 0.0]),
    )
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
