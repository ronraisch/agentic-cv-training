# Working baseline

The procedural bundle contains 60 RGB images with rectangle annotations and 36 short RGB frame sequences.
Its split/group manifest is deterministic and training, validation and test groups are separate.
This small fixture exercises the full path without an internet connection or external weights.

## Run the demo

Install the approved environment using [offline setup](OFFLINE_SETUP.md). For a connected
public development workstation only, the locked installation is:

```bash
uv sync --extra dev --extra mcp --locked
```

Then run without dependency resolution or downloads:

```bash
uv run --no-sync researchlab-demo prepare --root data/local-demo
uv run --no-sync researchlab-demo train --root data/local-demo
uv run --no-sync researchlab-demo evaluate --root data/local-demo
uv run --no-sync researchlab-demo predict --root data/local-demo --sample video-030
uv run --no-sync researchlab-demo serve --root data/local-demo
```

Open the loopback URL printed by the server. Draw rectangles, save and reload annotations.
Training reads the persisted records. The selected artifact is loaded for prediction; use its
reported SHA-256 to trace a response to the saved model. The same commands can use an approved
local data bundle conforming to [the data contracts](DATA_FORMATS.md).

The included procedural fixture requires no dataset download or external weights. It exercises
real CPU optimization, artifact persistence and inference, and does not establish accuracy on
real cameras. For real assignments use the prepared [dataset bundles](DATASETS.md).
Missing packages, files or model artifacts must stop with a path, recovery action and setup link.

```bash
uv run --no-sync researchlab-demo smoke --root artifacts/baseline-check
uv run --no-sync pytest
uv run --no-sync python tools/preflight.py --scope starter
```

## What the commands do

`prepare` writes arrays, a SHA-256 manifest and the initial SQLite annotation store. It refuses an
unrecognized existing directory and reuses a valid bundle without overwriting edited annotations.
For an imported compatible manifest, `initialize-store` seeds missing annotation rows; it does
not replace existing rows. See [data contracts](DATA_FORMATS.md).

`train` reads current persisted rectangle records, extracts image crops and fits a two-class head.
It also fits three independent video-question heads. CPU logistic optimization updates weights
and records initial/final loss. Input scaling is fitted on training data. The artifact contains
weights, scaling, feature version, class/question mapping and training/data fingerprints.

`evaluate` reports validation/test sample counts and accuracy. These procedural examples are
easy; high fixture accuracy says nothing about performance on real imagery. Use the assignment's
independent data and evaluation protocol for research claims.

`predict` reloads the selected local artifact. Image prediction uses current persisted rectangles;
video prediction uses the selected clip's frames. Both report the model checksum. The default
artifact is `<root>/models/baseline.npz`; `--model` selects another explicit file. No checkpoint
search or public download occurs at inference.

`serve` provides the loopback labeling UI and API:

| Method/path | Behavior |
|---|---|
| GET / | Labeling interface, rectangle drawing, class, undo, save and reload |
| GET /api/images | Known image IDs and split |
| GET /api/image?id=ID | Local RGB image as PNG |
| GET /api/annotations?id=ID | Current persisted record |
| POST /api/annotations | Save a valid record and return it |
| POST /api/predict | Predict a known sample ID with the selected artifact |
| GET /health | Health and the selected artifact's checksum |

The API is a local teaching service. Use the team's ingress/auth and persistent mounts for an
internal deployment; do not expose the local server publicly as a production service.
Read its implementation and callers before changing a product behavior. Missing assets must
point to [offline setup](OFFLINE_SETUP.md), rather than appear as a negative prediction.

The existing catalog/retrieval and optional Torch modules remain available for assigned work.
Run the bounded [preflight](PREFLIGHT.md) and tests separately from any internal-system claim.

The separate [local CNN detector](DETECTOR.md) provides actual box localization, class and object
presence training, saved weights and inference. Use it to verify detector plumbing; crop
classification above does not implement detection.
