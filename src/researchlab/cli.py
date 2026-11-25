import argparse
import json
from pathlib import Path
import sys


def main(argv=None):
    parser = argparse.ArgumentParser(description="Search a local image metadata and embedding catalog")
    parser.add_argument("--data", type=Path, default=Path("data/catalog"))
    parser.add_argument("--query", nargs="+", type=float,
                        help="Embedding components in the same order and dimension as features.csv")
    parser.add_argument("--top-k", type=int, default=3)
    args = parser.parse_args(argv)
    for name, schema in (("samples.csv", "sample_id,scene_id,split"),
                         ("features.csv", "sample_id,embedding (space-separated numeric components)")):
        path = args.data / name
        if not path.is_file():
            print(f"Missing catalog file: {path}. Expected CSV columns {schema}. "
                  "Mount an approved catalog at --data PATH. See docs/reference/DATA_FORMATS.md#retrieval-catalog.",
                  file=sys.stderr)
            return 2
    if args.query is None or args.top_k < 1:
        parser.error("supply a query embedding with --query and a positive --top-k")
    try:
        import numpy as np
        from researchlab.pipeline import retrieve
        from researchlab.sources import from_csv

        result = retrieve(from_csv(args.data / "samples.csv"), from_csv(args.data / "features.csv"),
                          np.asarray(args.query), k=args.top_k)
    except ModuleNotFoundError as error:
        print(f"Missing dependency: {error.name}. Install the approved locked environment; "
              "see docs/setup/OFFLINE_SETUP.md#python-runtime.", file=sys.stderr)
        return 2
    except (ValueError, KeyError, AttributeError, OSError) as error:
        print(f"Invalid catalog or query at {args.data}: {error}. "
              "See docs/reference/DATA_FORMATS.md#retrieval-catalog.", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
