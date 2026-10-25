# Teaching baseline preparation

These are proposed areas, not implemented paths. Map them to a working teaching system before the cohort.
Keep this map out of the initial learner product brief.
Use [the internal supply checklist](INTERNAL_READINESS.md) for per-asset contracts, owners,
immutable versions, manifests and executed readiness gates.

| Area | Suggested location | Prepared baseline |
|---|---|---|
| Labeling | apps/labeling | Rectangle tool, zoom/pan, storage and old annotations |
| Data/API | services/labeling | Versioned schema and held-out migration fixtures |
| Training consumer | training/crops and dataset | Real export/loader and a documented product crop decision |
| LPR | src/lpr and services/lpr | Frozen detector/recognizer, baseline, varied plate examples |
| Image stitching | src/imagery | Overlap pairs plus no-overlap/parallax examples |
| Tracklets | src/motion | Timestamps, motion labels, camera information, group IDs |
| Rescoring | src/rescoring | Frozen predictions, independent GT, GSD/angle conventions |
| Clouds | research/clouds | Available sources/data for proposal feasibility |
| Video | src/video and services/video | Ordinary-camera clips, approved encoder weights and service boundary |
| Operations | deploy | Internal image, teaching namespace/route/storage |

Prepare an approved pinned Matt Pocock bundle with support files and licenses. The mentor reviews
the selected entry files and rehearses the short activation demonstration before the first cohort.
This one-time curriculum preparation is distinct from the recurring 12-hour mentor budget; record
its actual cost rather than hiding it in learner time.

## Data preparation before the cohort

Use [the dataset catalog](../docs/DATASETS.md). The team covers ordinary-camera video as well as
remote sensing. Keep ground-camera video separate from satellite/airborne image tasks.
Prepare small, approved local subsets and frozen split manifests before the cohort; access requests
and a full benchmark download are not new trainee assignments. Record preparation cost separately.
Provide independent GT plus frozen predictions for rescoring; public GT is not detector output.
For video, prefer a single MEVA ground-camera collection with both indoor/outdoor views; BDD100K
or VIRAT ground footage is optional supplementation. Avoid making dataset identity equal the label.
Prepare a few real sky-only/ceiling/empty clips if missing; unknown labels are not negatives.
Keep later question labels/releases mentor-only until their scheduled product request.

For the open-model foundations probe prepare a small approved embedder bundle plus tiny COCO/DOTA
examples reused from the catalog. Supply provenance-rich saved Grounding DINO-like and generative
VLM examples if live heavy models are unavailable. Include failures, original images/prompts and
processor/postprocessing/generation settings. Saved runs do not count as trainee-executed inference.
