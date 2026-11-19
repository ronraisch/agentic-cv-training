# YOLO11 detection baseline

The starter uses YOLO11n with axis-aligned detections. It reads local real-image labels from the
[same mounted collections as the annotation app](DATA_FORMATS.md#labeling-collections).
Stage 1 adds oriented boxes to the annotation workflow. The
[stage 4 lab](../labs/research/04-oriented-detection.md) connects YOLO11n-OBB to that workflow.

Install the locked `detector` extra and mount an approved [local checkpoint or architecture
YAML](OFFLINE_SETUP.md#detector-runtime). Export one domain per run so class maps stay explicit.
Use a fresh output directory for each export and training run.

```bash
uv run --no-sync researchlab-demo check-data --root /approved/labeling
uv run --no-sync researchlab-detector export --root /approved/labeling --domain satellite --output artifacts/sat-examples
uv run --no-sync researchlab-detector train --data artifacts/sat-examples --model /approved/models/yolo11n.pt --output artifacts/sat-sgd --epochs 10 --device cpu
uv run --no-sync researchlab-detector evaluate --data artifacts/sat-examples --model artifacts/sat-sgd/weights/last.pt --output artifacts/sat-sgd/eval
uv run --no-sync researchlab-detector predict --model artifacts/sat-sgd/weights/last.pt --input /approved/labeling/satellite/images/new-image.png
```

Use `--device 0` in the approved CUDA environment. Exports snapshot saved labels, class order,
sample provenance and split group overlap. Keep the export in its original location because
Ultralytics resolves images relative to its absolute dataset path. Export again after label changes.
The application accepts a trained local checkpoint through `serve --model PATH`. Predictions use
original-image pixel coordinates, names and confidence, with every surviving detection returned.

## Starting experiment artifacts

| Starting choice | Where to inspect it |
|---|---|
| Fixed learning rate, SGD, no warmup | `args.yaml`, LR columns, and `training-loss.png` in the training run |
| Unshuffled, aspect-ratio-sorted batches (`rect=True`) | Training call in [detector.py](../src/researchlab/detector.py). Look for batches dominated by one source or resolution. Rectangular batching can save padding, so measure its trade-offs. |
| Default example-level train/validation split | `export.json` records the original group IDs and their overlap. `--split-policy grouped` keeps the supplied groups. The test split stays fixed. |
| ROC AUC at matching IoU 0.90 | `evaluation.json`, `iou-sweep.csv` and `localization.png`. ROC ranks matched and unmatched predictions and omits ground-truth objects with no prediction. Recall accounts for missed objects. ROC AUC is undefined when every prediction has the same match outcome. |

Detector evaluation uses class-aware, confidence-ordered, one-to-one matching and reports
the effect of changing matching IoU. Matching IoU is independent of inference NMS IoU.
The starter evaluator uses HBB geometry even with the optional OBB export. Improving the
evaluation with AP, PR curves and oriented IoU is part of stage 4. Low matching thresholds
can be useful for a proposal operating point, while higher thresholds answer localization questions.
Tune on validation and inspect test after the experiment design is frozen.

`export --task obb` requires an independent four-corner annotation for every labeled instance
in that export. Stage 4 compares HBB and OBB on the same source imagery, choosing compatible
class sets, group splits and checkpoint initialization. The starter UI shows axis-aligned
annotations. See [stage 4](../labs/research/04-oriented-detection.md) for the model-to-UI task.

For frozen plate/vehicle inference in other labs, use [the research components](COMPONENTS.md).
The [clip and crop models](BASELINE.md#what-the-commands-do) are separate classifiers.
