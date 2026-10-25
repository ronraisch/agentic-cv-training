# Offline installation and asset preparation

Prepare and verify the environment before the cohort. Use an internet-connected staging machine
only where downloads are approved. Transfer through the organization's approved process into
the closed network. Runtime never installs dependencies, downloads datasets or replaces a model.
The mentor/platform/data owner supplies real approved paths and support contacts in
[the environment map](../templates/internal-environment.example.md).

## Python runtime

ResearchLab requires Python 3.11+; use the approved exact Python/OS/architecture and matching lock
or image. `numpy` is enough for the local training/UI baseline. The existing locked installation
also provides Pandas/HTTP helpers; `dev` supplies tests/build/lint and `mcp` supplies the local
protocol probe. Jupyter, image/video codecs and large research models are separate capabilities
of the [approved research environment](RESEARCH_ENVIRONMENT.md).

### Preferred image route

1. On a matching approved connected staging machine, clone the chosen code revision. Install
   Python/uv from approved distributions; run `uv sync --extra dev --extra mcp --locked`.
2. Run tests and `uv run --no-sync researchlab-demo smoke --root artifacts/baseline-check`.
3. Package that verified code/environment in the team's teaching image. Record the source commit,
   Python/OS/architecture, package versions, image digest, mount paths and successful commands.
4. Export/import the image with the team's registry or `docker save` / `docker load` process.
   The image must include the installed runtime; a source-only image is not a dependency bundle.
5. In the trainee's pod, run with the approved data/model/storage mounts and no public network.
   Check the actual image digest and execute the same baseline commands.

### Wheelhouse alternative

Prepare on the same target OS/architecture/Python. Do not assume wheels downloaded for a Mac
will install in a Linux pod. On the connected staging machine:

```bash
uv sync --extra dev --extra mcp --locked
mkdir -p staging/wheels
python3 -m venv staging/download-env
uv export --locked --extra dev --extra mcp --no-emit-project --format requirements-txt -o staging/requirements.txt
staging/download-env/bin/python -m pip download --only-binary=:all: -r staging/requirements.txt -d staging/wheels
uv run --no-sync python -m build --wheel
```

Include a reviewed learner source export with its local docs, the project wheel from `dist/`,
the complete wheelhouse, exported hashed requirements,
approved Python/uv distributions and a SHA-256 inventory in the transfer bundle. Build dependencies
are needed on the staging machine; the closed-network installation uses the built project wheel.
If a dependency has no wheel for the target, have the environment owner build/approve one or use
the image route; do not silently omit it or compile against an unknown system library.

Inside the network, replace `/approved/bundle` and the interpreter with the supplied paths:

```bash
uv venv .venv --python /approved/python/bin/python3.11
uv pip install --python .venv/bin/python --no-index --find-links /approved/bundle/wheels --require-hashes -r /approved/bundle/requirements.txt
uv pip install --python .venv/bin/python --no-index --no-deps /approved/bundle/research_engineering_onboarding-0.1.0-py3-none-any.whl
uv run --no-sync researchlab-demo smoke --root artifacts/baseline-check
```

Use `--no-sync` for runtime commands. The public lock contains public artifact URLs; it is not an
internal mirror configuration. For Artifactory-based installation use the separately approved
internal lock/index/CA, not a public installer, TLS bypass or an arbitrary re-lock. `--offline`
alone cannot supply uncached dependencies.

## Local fixture data

The working baseline needs no external dataset:

```bash
uv run --no-sync researchlab-demo prepare --root data/local-demo
uv run --no-sync researchlab-demo train --root data/local-demo
```

This creates 96 deterministic procedural assets, a manifest with file hashes and initial persisted
labels. Run the commands inside the closed network after dependency installation. Alternatively
prepare once on staging, train, transfer the complete bundle and verify its hashes. Preserve the
SQLite store if annotations have been edited. `prepare` does not reset existing records.

## External datasets

Use [the per-assignment catalog](DATASETS.md) for the exact source entry points: COCO for labeling,
CCPD/approved alternative for LPR, selected overlapping airborne frames, motion-labeled tracklets,
frozen detections plus independent GT, cloud patches and ordinary-camera clips. Download the
selected release on approved connected staging only, resolve access/terms there, and record
source IDs, release, license/approval, counts, bytes and SHA-256 values after transfer.

Before a task starts, the data owner prepares one small subset and its annotations, grouped
train/validation/test manifest and decoder/loader smoke. Do not ask a trainee inside the closed
network to visit a public dataset site. Transfer inputs into the assigned data mount, for example
`data/imported/<bundle-id>/` or its approved external mount. Use that path with `--root`.

For the local training baseline, convert approved images to RGB uint8 `.npy` using the staging
environment's approved decoder; convert sampled video frames to RGB uint8 THWC arrays and retain
their original timestamps. Supply the manifest in [the documented format](DATA_FORMATS.md), with
actual hashes, compatible labels and groups. Keep decoder versions and source provenance. Do not
rename an arbitrary COCO/DOTA/MEVA archive and treat it as a compatible bundle.

Initialize a compatible imported annotation store once, then train:

```bash
uv run --no-sync researchlab-demo initialize-store --root data/imported/BUNDLE_ID
uv run --no-sync researchlab-demo train --root data/imported/BUNDLE_ID
```

Other assignment sources may use team-specific loaders and models; supply their schema and
commands explicitly. Missing files must report the bundle/path and this guide, not trigger a
network fallback or be interpreted as an empty/negative scientific result.

## Model artifacts

The procedural baseline trains locally and writes `<root>/models/baseline.npz`. It needs no public
weights. If this file is missing, run `researchlab-demo train --root ROOT` or transfer the selected
artifact to the exact `--model` path; verify its SHA-256 and fresh-process prediction.

For an external model, the supplying owner prepares the complete approved bundle: exact model
revision, weights, architecture/config, processor/tokenizer/chat template if used, class maps,
pre/postprocessing, runtime versions, terms and memory/device requirements. Download on staging,
review required custom code, then transfer to the approved model mount. Use explicit local paths
and the exact runtime's offline controls. Never infer a missing model from a display name or
enable arbitrary remote code as an installation fix.

## Expected missing-asset behavior

Every first-use error must identify what is absent, where it was expected, a preparation/transfer
or training command, and this document. Missing Python packages are environment errors; a missing
manifest/array is a data error; a missing artifact is a model error. Do not represent any as a
successful prediction. Ask the named owner when the approved internal value has not been supplied.
