# Part 3 Evaluation and classical models

Required learning: [Evaluation and ML](../../docs/lessons/03-metrics-ml.md).

## Did LPR rectification help

Evaluate the part-2 change against the original path using the same detector, recognizer and examples.
Predefine splits, metrics and thresholds. Include failed rectification, fallback, regressions and
processing time. Do not report only successful crops.

## Tracklet motion classification

Use the supplied [tracklet producer](../../docs/COMPONENTS.md#tracklets-for-motion-classification)
or a documented frozen source export. Acquiring videos and independently labeling motion is part
of the work; implementing a detector/tracker is not.

Given tracklets and independent motion labels, clarify the target, decision time and available
information. Train a small classical model such as XGBoost against a simple baseline. Evaluate it,
store feature computation and reload the selected artifact. Do not retrain the detector/tracker.

## Detection rescoring

Use the supplied [vehicle prediction export](../../docs/COMPONENTS.md#vehicle-predictions-for-rescoring)
with independent dataset GT. Record source-class mapping and the box representation before comparing.

Given a frozen detector's predictions, independent GT and detection/satellite-image metadata,
learn a new score from the old score and useful metadata. Physical size relative to GSD and viewing
angle are hypotheses, not universal rules. Compare raw score, a simple baseline and the model;
ablate metadata. State whether the aim is ranking, an operating threshold or probability calibration.
Use a small prepared dataset and limited configurations, not a new detector project.

For all three deliver target definition, grouped data/split provenance, baseline, experiment, metrics
and limitations. For learned models include feature schema, artifact and fresh-load inference.
Use an agent to challenge leakage and confounders; verify its argument with a source or small example.
A valid non-improvement is acceptable. The individual teach-back is separate from the MR review.

[Relevant data sources](../../docs/DATASETS.md#evaluation-and-classical-ml).
Follow [the acquisition steps](../../docs/DATASETS.md#acquire-a-working-subset).
