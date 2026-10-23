# Evaluation and classical ML

## One valid experiment

Define the target, sampling unit, grouped splits, baseline and metric before tuning. Frames and
tracklets from one video, overlapping satellite tiles and images from one flight can be dependent.
Do not split only by rows. Fit preprocessing on training data; choose thresholds/hyperparameters
on validation; evaluate the frozen decision on test. Preserve data/split hashes and model versions.

Know linear/logistic regression, regularization, nearest-neighbor and SVM intuition, and tree/
boosting behavior. These foundations are learned once, not repeated in ML and DL lectures.
A linear model's coefficients are not generally causal feature importance. Scaling affects units,
optimization and regularization; it need not change fitted predictions of equivalent unregularized
least squares. Correlated features can make coefficients unstable without necessarily ruining
predictions. PCA/clustering concepts are useful; full EM/spectral/visualization algorithm exercises
are optional. High-dimensional separation on tiny data is not evidence of generalization.

Precision = TP/(TP+FP), recall = TP/(TP+FN). Accuracy alone can hide rare-class failure. Show PR,
confusion, denominators and slices; define behavior for absent classes or zero denominators.
Threshold selection and calibration are distinct from ranking. A confident score is not automatically
a probability. A metric does not encode the consumer's costs until an operating decision is defined.

## Paired LPR evaluation

Hold the detector and recognizer fixed and compare identical examples with and without Hough
rectification. Freeze text normalization. Report exact-plate match and CER: summed edit distances
divided by summed ground-truth character counts, with an explicit empty-GT policy. Include failure,
fallback, coverage and latency. Do not score only examples that rectified successfully.

Separate evaluation on supplied plate ROIs from end-to-end evaluation including detector misses.
Inspect helped and harmed examples by angle, size and lighting. If estimating uncertainty, resample
independent vehicles/videos/flight groups rather than individual dependent frames. Few groups limit
the conclusion; do not invent confidence. Preserve a locked final test set.

## Motion from tracklets

A row may summarize speed, direction change, duration, stops and stability. Define timestamps,
missing frames, fragmentation, camera motion and units. Pixel displacement may reflect camera
motion; meters per second require geometry/calibration. For an online decision at two seconds,
features from the completed track leak the future. Offline use is valid only if that is the contract.

Start with a simple rule/majority and a small model such as XGBoost. Boosting adds learners
sequentially; bootstrapping is resampling, not boosting. Limit configurations, inspect failure
slices, save feature order/missingness rules and reload the selected artifact. A successful search
log does not prove that best_estimator was what the service loaded.

## Detection rescoring

Freeze the detector and define correctness against independently annotated GT with a stated
class/IoU one-to-one matching protocol. Do not use predicted classes/scores as truth. Use detections
from groups held out from detector fitting or a planned out-of-fold procedure, and reserve an
independent test for the combined decision. Rescoring cannot recover absent proposals.

Candidate features include raw score, class, geometry, GSD, sensor, viewing angle and quality.
Define angle convention, units and missing values. There is no universal rule that more vertical
imagery is worse; test that hypothesis on this data. Pixels times GSD approximate a footprint only
under suitable geometry. Axis-aligned boxes, clipping, partial objects and incorrect metadata can
make physically implausible dimensions misleading.

Compare raw score, a simple rule and the learned model; ablate metadata and check new scenes/sensors.
If claiming probability calibration, use reliability analysis and suitable scoring rules; better
PR or lower Brier alone does not establish better calibration. Track source assumptions explicitly.
