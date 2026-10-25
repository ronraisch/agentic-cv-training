# Research environment handoff

The README's locked command installs the working procedural CPU baseline, catalog examples and
checks. The [baseline](BASELINE.md) can label, train, reload and predict without external assets.
Real research datasets, codecs, notebook kernels and pretrained model families require the
separately approved environment below. See [offline installation](OFFLINE_SETUP.md).

The mentor supplies an approved internal image/digest or environment lock, actual paths and
commands in [the environment map](../templates/internal-environment.example.md). Use the
[internal installation procedure](GETTING_STARTED_INTERNAL.md); do not install arbitrary public
packages or re-lock from inside the closed network. No additional full stack is a trainee task.

| Work | Capabilities the approved environment must provide | Readiness evidence |
|---|---|---|
| Existing labeling application | Its actual frontend runtime/package lock, Python API, store and consumer dependencies | Known UI/API/save/reload and consumer commands work at the selected revision |
| Hough, warping and stitching | Image decoder, numerical and CV operations, plotting/overlay output; often OpenCV/Pillow/Matplotlib or team equivalents | Decode a prepared image, check channel order/range, run a known geometric fixture and save/read an overlay |
| Tracklets and rescoring | Feature/table tooling, a small classical estimator and artifact serialization; e.g. scikit-learn, with XGBoost only if selected | Fit a tiny approved fixture; save and load a fresh instance with identical feature schema/output |
| Video | Actual decoder with required codecs, timestamp handling, selected representation and head runtime | Decode a ten-second fixture with timestamps; run one forward pass and fresh-load inference |
| Open-model probe | Approved local embedder with matching processor/tokenizer and offline loading support | Known sample and fresh-process replay without runtime network downloads |
| Notebook | Jupyter/ipykernel supplied by the approved environment and a registered project kernel | Correct sys.executable, restart and run all, saved output |

Torch is an existing optional ResearchLab extra. If the optional CPU exercise is assigned, its
public development command is `uv sync --extra dev --extra mcp --extra torch --locked`; internally
use the approved equivalent. This does not install the remaining research capabilities above.
Only the actual selected libraries belong in the internal lock; the examples in the table are
not a requirement to install every named framework.

Record OS/architecture, Python and package versions, device/memory budget, image digest/lock hash,
model/processor revisions, local mounts and exact successful commands. Use secret references,
never secret values. Record expected output and actual output, plus owner/status when blocked.
An import alone is insufficient: the representative operation must run in the trainee's pod.

Run [preflight](PREFLIGHT.md) for local synthetic smokes and coarse readiness-record checks.
Recorded evidence is reported separately from executed checks; internal integrations still need
their actual owner-run commands and review.
