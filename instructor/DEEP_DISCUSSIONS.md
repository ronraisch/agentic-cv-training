# Deep discussion selection

Only the first meeting uses a rapid basics screen. Later meetings should investigate two difficult
question chains, not a list of definitions. These chains adapt themes from the current CV/ML/DL
mentor guides and add production/evidence cases. The original full banks stay in Drive unchanged.
A typical chain is 15-18 minutes with an unfamiliar follow-up and a precise boundary of certainty.

## Development and research correctness

A training log says SVM C was tuned. What evidence would establish that the winning estimator is
what consumers use? Trace selection, serialization, artifact/image identity and loaded runtime
parameters. Supply a counterexample where every unit test is green but the reported improvement
belongs to a different artifact. What experiment would falsify your explanation?

An array optimization preserves output shape and improves speed. Can it alter the scientific result?
Construct a parent-view mutation or row-order join counterexample. Explain a small independent
oracle and how to distinguish numerical tolerance from actual semantic corruption.

## Geometry and classical CV

Draw the image-space/parameter-space relation for collinear points. What do Hough bin size and
support threshold do differently? Explain how to refine a detected line and why text strokes can
win the vote instead of the plate boundary. What observation would reject the selected quadrilateral?

Derive the degrees of freedom and minimum nondegenerate correspondences for a planar mapping.
Why can four visually correct corners still give unstable rectification? Contrast forward/inverse
warping, interpolation and missing source pixels. Give a plate example where no warp can help.

Two airborne images have many RANSAC inliers and a smooth seam. Why may the stitch still be wrong?
Reason about repeated patterns, inlier spatial distribution, parallax and independent control points.
How does changing the camera/terrain assumption change the appropriate transformation model?

Connect filter separability, smoothing/downsampling and aliasing. Construct an image where changing
kernel scale suppresses the target itself. How would the same error propagate into an LPR metric?

## Evaluation and classical models

Keep recall and false-positive rate fixed while class prevalence changes. Derive how precision
changes and explain why a previously adequate threshold may violate a consumer contract. Propose a
small paired/grouped LPR comparison and show how dropping rectification failures fabricates a gain.

Rescale a feature in unregularized least squares, ridge and a tree model. Which predictions,
coefficients, penalties and optimization behavior may change? Why do correlated features complicate
importance? Reject both "normalization always changes the solution" and "scaling never matters."

Compare bagging, bootstrap resampling and boosting through a counterexample with correlated errors.
Why might an ensemble fail to improve? What is the right validation unit for motion tracklets from
one moving camera, and which seemingly excellent feature leaks the future?

The rescoring model improves PR. Has it produced reliable probabilities? Design a case where
ranking and calibration disagree. Explain missing GSD/angle metadata, physically implausible boxes,
partial objects and sensor shortcuts; propose an ablation that tests the claimed mechanism.

## Deep learning and representation

Trace a gradient through a tiny head and encoder. What would a detached tensor, unregistered
module or wrong accumulation policy look like? How can decreasing loss coexist with a frozen
component? Explain tiny-overfit versus generalization and the artifact reloading check.

Compare a spatially flattened FC layer with an equivalent convolution on a fixed feature volume.
State the weight mapping and output shapes on a larger input. Explain receptive fields, parameter
sharing and pooling for tiny targets without claiming max pooling is universally superior.

Write attention's Q/K/V shapes, justify the scaling and explain self versus cross-attention.
Without positional information, what is equivariant and what may become invariant after pooling?
How can a model be text-aligned yet fail a temporal question or negated prompt in our domain?

A consumer keeps adding video questions. Which costs grow with independent heads, a shared text-
aligned representation and a VLM? Construct a presence/event counterexample, define unknown/error,
and design a small comparison that preserves existing consumers. Do not prescribe the architecture.

A cloud model has high pixel IoU. Could skipping its mask lose important objects or cost more
compute than it saves? Define the denominators, missing GT and a testable partial-tile policy.

## Coverage rather than shallow speed

Week 2: development evidence plus one data/geometry chain. Week 3: two geometry chains. Week 4:
two evaluation/ML chains. Week 5: gradient/architecture and attention/representation. Week 6:
video/product reasoning inside the notebook defense. Unselected deep questions become bounded
independent derivations or role-specific follow-up, not extra compulsory mentor meetings.

For each discussion record: claim, derivation/assumption, counterexample, empirical check and what
remains unverified. The trainee teaches and defends; the mentor does not lecture through slides.
Use PRIMARY sources to correct doubtful answer keys. See SOURCE_REVIEW for examples needing care.
