# Research environment handoff

The README's locked command installs the working procedural CPU baseline, catalog examples and
checks. The [baseline](BASELINE.md) can label, train, reload and predict without external assets.
The optional locked `components` extra and [frozen model bundle](COMPONENTS.md) supply plate
detection/recognition, vehicle predictions and tracklet generation. The trainee acquires the
task data using [the dataset instructions](DATASETS.md#acquire-a-working-subset). Internal
connectivity, transfer paths, credentials and platform permissions are supplied by the owner.
Other capabilities below use the separately approved environment; see [offline installation](OFFLINE_SETUP.md).

The mentor supplies an approved internal image/digest or environment lock, actual paths and
commands in [the environment map](../templates/internal-environment.example.md). Use the
[internal installation procedure](GETTING_STARTED_INTERNAL.md); do not install arbitrary public
packages or re-lock from inside the closed network. The trainee does not rebuild the shared stack. For the mandatory
[SAM2 assignment](../labs/research/01b-sam2-service.md), the trainee builds and deploys a bounded
inference service on that stack. In the DL block the trainee also deploys a teaching RabbitMQ
broker and SAM3 worker for [batch labeling and detector training](../labs/research/05b-rabbitmq-sam3-detector.md).

| Work | Capabilities the approved environment must provide | Readiness evidence |
|---|---|---|
| Existing labeling application | Its actual frontend runtime/package lock, Python API, store and consumer dependencies | Known UI/API/save/reload and consumer commands work at the selected revision |
| Hough, warping and stitching | Locked headless OpenCV in `components`; supplied raw LPR detector/recognizer and crop interface | Decode an acquired image, run [raw LPR](COMPONENTS.md#lpr-baseline-and-crop-recognition), save/read an overlay; trainee implements geometry |
| Tracklets and rescoring | Supplied [frozen vehicle detector and tracklet producer](COMPONENTS.md); approved small estimator runtime, e.g. scikit-learn with XGBoost only if selected | Export predictions/tracklets from acquired data; trainee fits the assigned head, saves and reloads it |
| Video | Actual decoder with required codecs, timestamp handling, selected representation and head runtime | Decode a ten-second fixture with timestamps; run one forward pass and fresh-load inference |
| Open-model probe | Approved local embedder with matching processor/tokenizer and offline loading support | Known sample and fresh-process replay without runtime network downloads |
| Required SAM2 annotation service | Approved SAM2 code/config and checkpoint, compatible inference dependencies, device/memory allocation, internal base image, registry push and teaching namespace/Route permissions | Actual mask inference from the deployed image through its Route, application save/reload and teaching-pod restart |
| Required RabbitMQ/SAM3 detector pipeline | Approved RabbitMQ image/client and persistent broker storage; teaching broker/worker permissions; SAM3 code/config/checkpoint; prompt/class config; shared frame/output storage; GPU allocation; one approved RT-DETR or YOLO training environment and weights | Publish/consume real jobs, save labels, recover interrupted/duplicate jobs, export data, train and reload detector, evaluate on human-checked held-out video frames |
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
