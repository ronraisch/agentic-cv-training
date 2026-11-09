# Worked examples for the research labs

These small examples use illustrative inputs. Use the lab's approved fixtures and contracts to verify behavior on the actual system. For an interactive explanation, use the [agent prompts](RESEARCH_WITH_AGENTS.md#when-you-get-stuck) and [offline playgrounds](playgrounds/README.md).

## Python modularity

Suppose a temperature report reads `room,21.5` from CSV, checks the range, converts Celsius to Fahrenheit and prints a line. The CSV reader and a new JSON reader can both return the same room and Celsius reading. The range check, conversion and report then work unchanged. A malformed number fails at parsing. A valid number outside the permitted range fails validation with the room ID. Try predicting which code changes if only the output format changes. Explore the [design-pattern playground](playgrounds/README.md) with a generic example.

## Rectangle and service

Start with a rectangle you can recognize. Record its image ID and coordinates in the UI, find the save request, locate the persisted record, reload it and inspect one consumer's interpretation. If the UI still draws it but the consumer drops it, you have evidence for a persistence or compatibility investigation. Ask the mentor which consumer and polygon behaviors matter before editing.

For an adjacent service exercise, use an approved echo service. Check the process and its port inside the pod, then inspect whether the Service selector finds a ready endpoint and whether the Route forwards to that Service. A ready pod with no endpoints points to selector or readiness wiring. A successful health request with a failing inference request calls for inspecting the actual payload, service logs and loaded checkpoint. Follow the deployed image digest back to its CI build and commit.

With a 1000 × 500 image resized directly to 500 × 250, a point at (400, 200) maps to (200, 100). A mask contour vertex at (201, 100) maps back to (402, 200). Padding or cropping adds an offset that must be undone as well. Check the returned polygon against the original image and then save and reload it.

## Classical CV

**Plate trace.** A detector crop starts at (100, 50) in the full image. A corner at (8, 6) in the crop is at (108, 56) in the image. Overlay the detected lines in crop coordinates, reject strong interior lines from lettering, then order the four border intersections consistently before applying the warp. If a border is clipped and the quadrilateral is unreliable, record the fallback. Inspect the warped image and pass BGR to the [frozen OCR](COMPONENTS.md#lpr-baseline-and-crop-recognition). A visually straight crop that trims the first character can reduce exact match. Keep the item ID, original detector outcome, original and processed crop references, and fallback status for the paired ML comparison.

**Stitch trace.** Suppose the transform from B into A is a translation of −30 pixels in x. B's (10, 8) becomes (−20, 8) in A's coordinates. If the combined canvas starts at x = −30, shift both layers by +30, so that point is at (10, 8) on the canvas and A's origin is at (30, 0). Plot the inlier locations and check residuals at landmarks outside the fitted cluster. If road landmarks line up and nearby roofs consistently shift, inspect parallax. If both layers move the wrong way even on a synthetic translation, inspect transform direction and canvas offset first.

## ML evaluation

**Plate denominators.** Illustrative exact match on three images with one target plate each.

| Case | Ground truth | Raw OCR | With rectification |
| --- | --- | --- | --- |
| A | 1234 | 1284 | 1234 |
| B | 4567 | 4567 | 4567 via fallback |
| C | 9999 | No detection | No detection |

Conditional on a detector crop, exact match goes from 1/2 to 2/2. End to end it goes from 1/3 to 2/3. An analysis limited to successful warps would discard the fallback and answer a different question.

**Tracklet feature row.** Group by sequence and track and sort by timestamp. At decision time 1.0 s, centers at x = 10 at 0.0 s and x = 14 at 1.0 s yield a horizontal image velocity of 4 px/s. The missing 0.5 s observation is recorded as a gap. A center at 1.5 s is unavailable at decision time. A human label from the clip supplies independent ground truth. If the background also shifts right, image velocity alone is ambiguous. A sudden jump to another vehicle warrants inspecting an ID switch. Split by vehicle or sequence to avoid nearby observations crossing folds, or hold out cameras if the deployment claim is about unseen cameras.

**Rescoring.** Assume one-to-one matching in the fixed detector's score order with IoU ≥ 0.5.

| Candidate | Observation | Training target under this policy |
| --- | --- | --- |
| P1 | IoU 0.8 with GT A | Positive |
| P2 | IoU 0.7 with GT A, already matched | Negative duplicate |
| P3 | No eligible match, GSD missing | Negative, with missing GSD handled by a policy fitted on training data |
| GT B | No candidate | No training row, counts as an end-to-end miss |

Check [the frozen export and box conventions](COMPONENTS.md) before computing IoU. A ranking gain on these rows leaves the uncovered GT B unchanged. Measure the end-to-end operating point or calibration only if it addresses the product decision.

## Deep learning and video

A toy 256 × 256 image becomes a `[1, 128, 16, 16]` feature map at stride 16. A classifier can pool to `[1, 128]` and predict clip-frame scores. A DETR-style decoder can read flattened image features `[1, 256, 128]` with 100 object slots and predict one class distribution and box per slot. A segmentation head can use spatial features to predict a pixel grid. An object query represents a slot, while the attention query is the projection used to score keys inside attention. Attention heads read values in parallel and prediction heads map representations to task outputs. Trace the arrows in the [DETR figure](reading/dl-detection-head.md) or change one control in the [attention playground](playgrounds/README.md) and predict the effect.

For one missed target, measure its size after resize. Inspect the pre-threshold predictions. A matching box below threshold suggests checking scores and filtering. A missing candidate on a sparse image gives little reason to raise the query count first. Compare resolution or assignment behavior under a controlled change and record what remains unverified.

For cloud gating, compare the ungated baseline and gated path on the same images and available bands. Time both end to end and count independently labeled targets lost under the mask. A bright roof masked as cloud is an example of a costly false positive even when pixel IoU is high.

For video, inspect three example clips with the mentor: persistent road, road visible briefly, and a transition from inside to outside. For each, record which timestamps support the decision and what a sampler would see. Use disagreements to agree on the label policy, unknown behavior and unit of decision before comparing models.

## Queue to training

Follow three jobs by hand before increasing volume. For one illustrative job, message `clip7/frame3` with model revision `m1` and prompt revision `p2` yields output key `clip7/frame3/m1/p2`. A mask covering x = 12–30 and y = 8–21 in the frame yields an illustrative extent of (12, 8, 30, 21). Confirm endpoint conventions and coordinate normalization in the chosen detector format. Reopen the emitted row and overlay the decoded box on the original frame.

Inject a crash after durable output and before acknowledgement. Redelivery should recognize the same completed key and avoid duplicating the training row. A different model or prompt revision should have a distinct key. See the [redelivery example](reading/development-interfaces.md#handling-a-job-that-arrives-a-second-time).

Inspect both frames with proposals and a small independent sample of frames with no proposals. An empty queue with complete output files proves processing completed for the checked jobs. It says little about missed labels. Review overlays and manual labels before scaling, then verify export, train one detector and reload its checkpoint for held-out inference.
