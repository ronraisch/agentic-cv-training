# Internal supply and cohort readiness checklist

Mentor/data/platform owners complete this before the cohort. This is a supply list, not a claim
that these assets exist or were tested. Keep the completed copy inside the approved network.
Do not publish internal addresses, data, credentials or model weights here. The source contains
templates and synthetic examples; it does not implement the teaching application.

Preparation is one-time course/environment work, separate from the recurring 12-hour mentor
budget and the trainee's 240 hours. Record actual preparation time. Map existing team assets
instead of asking the trainee to build the missing stack. Later product briefs, labels and
acceptance fixtures stay mentor-only until their release. Do not disclose polygon acceptance
answers in the initial learner brief.

## Delivery record for every item

Fill one record per asset, not just one row saying "data ready". Use this table in an internal
copy, linking evidence and manifests rather than embedding dataset contents in a prompt.

| Field | Required value |
|---|---|
| Asset ID and assignment | Stable identifier; which checks depend on it |
| Owner / escalation | Named supplying owner and support contact |
| Location and access | Real repo/path/mount/image/endpoint and trainee read/write permissions |
| Immutable revision | Commit, lock hash, image digest, release and/or SHA-256; mutable tag alone is insufficient |
| Contract | Schema, shape/dtype, coordinates/units/time, missing/unknown/error policy |
| Size and resources | Bytes/counts, CPU/GPU/RAM/VRAM, expected storage and measured example runtime |
| Smoke command | Exact command from the trainee's assigned pod/workspace |
| Expected result | Stable IDs/shapes/tolerances or semantic assertions; avoid unexplained full logs |
| Observed evidence | Date, actual command/revision/output, exit status and sanitized evidence link |
| Status | NOT_SUPPLIED, BLOCKED or VERIFIED; only an executed check earns VERIFIED |
| Blocker / next action | Owner, next check date and approved fallback; a substitute has its own evidence scope |

Use [the internal environment map](../templates/internal-environment.example.md) for shared
configuration and [the team-tool inventory](../templates/team-tool-inventory.csv) for tools.
Initial state for all assets below is **NOT_SUPPLIED in this public repository**; internal status
must be established by its owner. An asset may be optional only where explicitly stated below.

## 1. Code and working baseline

| ID | Supply from the internal environment | Minimum evidence before releasing the assignment |
|---|---|---|
| C1 | Teaching repo URL, chosen commit/branch, clone access, module map, README and exact start/test commands | New identity clones the correct revision; baseline tests run; documented entrypoints exist |
| C2 | Rectangle-only labeling UI, its frontend runtime/package lock, API, store, old annotations and actual export/training consumer | Known fixture can be opened, annotated, saved, edited and reloaded; existing export/loader consumes it; old records still work |
| C3 | LPR detector/recognizer wrappers, preprocessing, baseline config and prediction/evaluation commands | One approved image produces identified detector ROI, recognized text and traceable model IDs; baseline can be replayed |
| C4 | Image loader/visualization helpers and coordinate conventions for the two-image task | Both selected frames decode, orientation/channel order are known, control points can be overlaid; do not supply a solved stitching implementation as a prerequisite |
| C5 | Tracklet reader, independent label join and frozen detector/tracker-output schema | A short track is read with timestamps/group ID and its label; learner still builds the feature pipeline/classifier |
| C6 | Frozen detection/GT/metadata loaders, class mapping, box convention and agreed one-to-one matching contract | A tiny independent matching fixture gives the expected TP/FP/FN; learner still builds and evaluates the rescorer |
| C7 | Video reader, approved representation interface, runnable baseline service boundary and notebook import paths | Known clip decodes and runs through the baseline API; model/processor IDs and output schema are visible; learner builds the requested solution |
| C8 | Safe teaching image/build/run recipe, deployment/service configuration and rollback/restart instructions | Known request reaches the teaching route from outside the pod and reports loaded artifact identity |

For C2 the mentor separately prepares product decisions and held-out acceptance checks from
[the mentor handbook](RESEARCH_GUIDE.md#polygon-assignment-with-product-discovery), including
compatibility and downstream behavior. Those are not an initial learner specification. Map real
paths in [the preparation map](PRODUCT_AND_PREPARATION.md); suggested directory names are not evidence.

## 2. Prepared data bundles

Select approved internal data or one bounded subset from [the dataset catalog](../docs/DATASETS.md).
Suggested counts below are starting targets from that catalog, not a requirement to download the
whole public collection or a claim that those counts establish statistical power.

| ID | Task and supplied assets | Required annotations/metadata and checks |
|---|---|---|
| D1 | Labeling: about 20–40 images and existing annotations in the baseline's actual format | Image dimensions/revisions, stable IDs, coordinate convention and source information; independent ordinary and malformed geometry fixtures retained by mentor |
| D2 | LPR: about 200–400 varied plate images; frozen detector and recognizer outputs plus original images | Plate text and evaluation corners/boxes, alphabet/normalization, vehicle/video/acquisition group and split; corners/filename text are GT, never inference features; audit recognizer compatibility |
| D3 | Stitching: exactly two sequential overlapping airborne frames plus a no-overlap or strong-parallax failure pair | Flight/sequence ID, timestamps, orientation and manually checked independent correspondences; confirm meaningful overlap and mostly planar region; dataset choice alone does not guarantee a suitable pair |
| D4 | Motion: about 6–10 sequences and a few hundred usable tracklets with frozen tracker outputs | Track/group/camera IDs, timestamp units, gaps/fragmentation, coordinates, camera-motion context and independently audited motion labels; agree taxonomy and decision time; split complete sequences/cameras |
| D5 | Rescoring: about 50–100 parent images, frozen predictions including false positives, independent GT and missed objects | Parent/crop/group IDs, class/box/score schemas, detector revision and fitting provenance, matching policy; actual GSD and angle values with units/conventions/missingness; keep overlapping crops together |
| D6 | Clouds: about 50–100 prepared patches for proposal inspection, not a required training archive | Exact sensor/bands/GSD, release/label protocol, dense GT versus scribble/unlabeled status, cloud/shadow/no-data/ignore definitions; group ROI and related dates; object GT is needed only for measured detector-recall harm |
| D7 | Ordinary-camera video: about 120–200 ten-second RGB clips from multiple cameras/recordings, plus held-out new inputs | Clip/source/camera IDs, absolute source time ranges, duration/fps/timestamps, initial question labels with unknown/ambiguous masks; audit road/indoor/outdoor/sky coverage; group neighboring/overlapping clips and avoid source-label shortcuts |
| D8 | Open-model probe: 12–20 reusable image examples, a few small-object examples and clips already selected above | Presence/location GT where available; prompt-development versus untouched check IDs; identify unannotated categories rather than treating them as absent |

### Per-bundle manifest and loader

Supply these fields in the team's existing format; document its schema with one synthetic row:

- Bundle/source ID, exact release, source item IDs, access/terms approval, attribution and data owner.
- Relative file path, actual SHA-256, byte size and decode result after internal transfer.
- Stable sample, parent, camera/sequence/acquisition and geographic grouping fields as applicable.
- Media dimensions/channels and video source window/timestamp units where applicable.
- Annotation path/revision/schema, label definitions, missing/unknown/ignore representation.
- Frozen train/validation/test membership and group identifiers, selection seed/method and manifest hash.
- Prediction source/model/preprocessing revision, and detector-training overlap status where relevant.
- Actual metadata values and units; unavailable GSD/angle stays missing, not invented from a category.
- Loader command that validates file/annotation joins, missing/duplicate IDs, split/group overlap,
  decode and per-question/class label counts. Log denominators and failures, not only successful rows.

Before release, the owner runs the loader on the transferred files and manually audits a small
sample. Verify that the selected estimator's training split contains usable labels/classes and
that evaluation groups can test the intended question. Tiny or absent groups remain a limitation;
do not invent confidence estimates. Hand over an approved resize/crop/time contract and one known
failure case. The trainee still designs the scientific method and verifies its evaluation.

## 3. Models, weights and cached evidence

| ID | Supply | Smoke / scope |
|---|---|---|
| M1 | LPR detector and recognizer, architecture/config, weights, vocabulary/alphabet, resize/normalization and postprocessing | Known plate works on the chosen data source; fresh process produces compatible output and correct original-image ROI coordinates |
| M2 | Frozen detector/tracker identities and prepared outputs for D4/D5; runtime weights only if actual inference/replay requires them | Outputs join by stable IDs; selected predictions are independently checked; no detector/tracker retraining is required |
| M3 | Small approved image/text embedder for the probe, plus encoder/representation chosen for the video baseline | Local load, known image/clip, feature shape/dtype/device and fresh-process replay; state whether text alignment or temporal modeling is supported |
| M4 | Provenance-rich saved open-vocabulary detector and generative VLM runs on D8; live heavy models are optional | Include original inputs, prompts, outputs, misses, model/processor revisions, thresholds and generation/postprocessing settings; trainee distinguishes inspected saved output from live execution |
| M5 | Cloud baseline/alternative model cards or primary-source excerpts, available channels and feasibility constraints | Proposal can be researched offline; full cloud weights/training are not required by the eight-hour assignment |

For each live bundle include repository/checkpoint revision, hashes, architecture/config, complete
weights, processor/tokenizer/chat template where used, class map and preprocessing/postprocessing
code. Record dependency versions, dtype/device, memory budget, terms/access approval and offline
loading flags supported by the exact runtime. Review any required custom code before approval.
Weights alone are not a runnable bundle. Validate local loading with outbound downloads disabled,
then reload in a new process. Record tolerances and actual output/artifact IDs.

The fitted motion classifier, rescorer and video head are trainee deliverables, not pretrained
answers the mentor must supply. Provide only a simple working teaching fallback if chosen to
reduce scope, and mark that substitution. Preserve model/preprocessing hashes in feature-cache
keys. Later video labels and staged releases remain mentor-only until the scheduled request.

## 4. Installation, configuration and permissions

| ID | Supply exact approved values internally | Verification |
|---|---|---|
| E1 | VS Code distribution/extensions, personal OpenShift pod/namespace, supported remote connection, user identity, persistent repo path and CPU/RAM/storage quota | Remote indicator, terminal and repo point to assigned pod; reconnect preserves workspace |
| E2 | OMP package/version/source, installation command, config location, provider/protocol, endpoint and exact served model ID; authentication secret reference and support owner | Fresh session has observed route metadata, reads a synthetic file and executes a harmless tool; repeat after reconnect; display name/self-description alone is insufficient |
| E3 | Approved OS/architecture/Python/uv and frontend runtimes, internal indexes/CA/lock or image digest, build dependencies and all selected transitive packages | Clean install from approved resources; no public-host fetches; run imports plus representative CV, ML and video operations from [the environment handoff](../docs/RESEARCH_ENVIRONMENT.md) |
| E4 | Image/video decoder and codecs, plotting destination, Jupyter/ipykernel and registered project kernel | Decode image/video timestamps, save/reopen an overlay, verify interpreter, Restart and Run All; imports alone are insufficient |
| E5 | Complete pinned Matt Pocock snapshot with support files/license/hash inventory, actual client's supported installation method, tracker/documentation destinations and selected tool inventory | Discovery/invocation trace and negative trigger in OMP; synthetic examples' file checks do not establish activation; report unsupported workflows/tools honestly |
| E6 | GitLab project/branch permissions, MR reviewer and safe CI log example; Confluence entry page and access owner | New trainee locates correct repo/MR/job result and actual Confluence content; no runner administration required |
| E7 | Teaching registry/image digest/run command, namespace/workload/service/route/health/prediction paths and safe rollback | Known image emits expected smoke output; fixture from outside pod returns expected prediction and actual loaded artifact ID |
| E8 | Data/model/PVC/NFS mount paths, UID/access, persistent write destination, safe teaching restart and scratch/output locations | Read sample/weights, save known checksum, restart only teaching workload and read same checksum; no production restart |
| E9 | Offline local copies of selected model docs/source excerpts and required internal learning context, with revision/date | Required readings and examples open from the pod without public internet; named support owner resolves missing content |

Use secret mechanisms; record reference names, not tokens, passwords or kubeconfig. Never treat a
local container, a 200 health check or a discovered tool list as proof of end-to-end internal inference.
Choose CPU fixtures where possible; do not require a GPU merely to prove setup. If the selected
research model needs accelerator access, record its actual quota/queue and an approved small fallback.

## 5. Final rehearsal and release gates

- [ ] C1–C8 are mapped to existing working paths; any substitution is explicit and demonstrated.
- [ ] D1–D8 are transferred/decoded with manifests, independent labels, grouped splits and audited counts.
- [ ] Required M1–M5 resources are available with provenance; optional live heavy runs are identified.
- [ ] E1–E9 are filled and exercised as a trainee identity in the assigned pod, including reconnect.
- [ ] A person who did not prepare the bundle follows the exact commands and opens a new input.
- [ ] Stage 0 has a known ResearchLab smoke and separate real-system smoke with expected output.
- [ ] Each assignment's prerequisites are VERIFIED before release; a blocked item has an owner and next action.
- [ ] Product decisions are answered consistently; later briefs/acceptance labels remain staged.
- [ ] Baseline inference modules/artifact can be replayed in a clean notebook with known output;
      the trainee completes the operational handover notebook during the final assignment.
- [ ] Learner export has empty artifacts, intact local links, no instructor/history and passing tooling checks.
- [ ] Preparation and rehearsal time are recorded; weekly and total trainee/mentor budgets remain unchanged.

The rehearsal checks prerequisite readiness, not whether the trainee's future research method
will improve accuracy. A valid non-improvement remains acceptable. Do not mark the cohort fully
ready while a mandatory prerequisite is NOT_SUPPLIED or BLOCKED; resolve it or record an explicit
scope substitution before release.
