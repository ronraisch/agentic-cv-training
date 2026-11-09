# Evaluate a change and train two small classical models

## Goal and preparation

Complete three comparisons: the license-plate recognition (LPR) preprocessing change, a motion classifier and a detection
rescorer. A well-supported non-improvement is a valid result.

Use [the ML syllabus](../../docs/syllabi/ml.md),
[the practical lesson](../../docs/lessons/03-metrics-ml.md) and
[the prepared data sources](../../docs/DATASETS.md#evaluation-and-classical-ml).
Follow [the acquisition steps](../../docs/DATASETS.md#acquire-a-working-subset).

## Task 1: did plate rectification help?

Compare your part-2 path with the original path on the same examples, detector and recognizer.
Decide the splits, metrics and thresholds before looking at the final comparison.
Include failed rectification, fallback cases, regressions and processing time. Reporting only the
successfully rectified crops would answer a narrower question than whether the change helps.

## Task 2: classify tracklet motion

A **tracklet** is a short sequence of observations that the tracker links to one apparent object.
For example, five boxes following the same car across five frames form one tracklet. In the
supplied per-frame export, gather its observations by `(sequence_id, track_id)` and order them
by timestamp. Check for gaps or switches to another object before computing motion features.

Use [the supplied tracklet producer](../../docs/COMPONENTS.md#tracklets-for-motion-classification)
or a documented frozen export. Acquire videos and label motion independently; implementing or
retraining the detector/tracker is not part of this exercise.

Clarify the target, decision time and information available at that moment. Define features and
train a small classical model, such as XGBoost, against a simple baseline. Evaluate it, save the
feature computation and model, and verify inference after loading the selected artifact afresh.

## Task 3: rescore frozen detections

Use [the vehicle prediction export](../../docs/COMPONENTS.md#vehicle-predictions-for-rescoring)
with independent ground truth. Record the source-to-target class mapping and box representation.

Learn a new score from the detector's original score and useful image/detection metadata.
Physical size relative to ground sample distance (GSD, ground distance per image pixel) and viewing angle are hypotheses to test, not universal rules.
State whether the goal is better ranking, an operating threshold or probability calibration.

Compare the raw score, a simple baseline and your learned model. Ablate the metadata so its
contribution is visible. Use a small prepared dataset and limited configurations; keep the detector
frozen rather than turning this into a new detector-training project.

## Submit and explain

For each comparison include the target, grouped split/data provenance, baseline, experiment,
metrics and limitations. For the learned models also include the feature schema, saved artifact
and fresh-load inference example.

Use the agent to challenge possible leakage or confounding, then check its argument against a
source or a small example. The individual theory explanation is separate from the MR review.
