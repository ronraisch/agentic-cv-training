# Mentor handbook

Keep this file out of the learner distribution. The original source collection has now been read;
[SOURCE_REVIEW.md](SOURCE_REVIEW.md) records the current scope and prioritization. Original Drive files remain unchanged.
The new syllabus preserves the source expectation that the trainee teaches the mentor precisely.
It reduces repeated resources and topic breadth, not the depth of selected scientific questions.

## Twelve hours including preparation

Schedule two windows a week, never more than one hour on one day. A typical week uses 45 minutes
for a deep discussion, 35 for product/review and 40 for preparation/asynchronous review. Six weeks
cost 12 hours. A required weekly 15-minute team-lead check-in is folded into product/review.

The first session alone includes a rapid ten-minute basic-understanding check. Use its remaining
30 minutes for the stage-0 Matt Pocock skill teach-back and five minutes for next steps. The other
week-1 window is 35 minutes. After that, do not spend sessions repeatedly defining precision,
convolution or embeddings. Use the original question banks for difficult follow-up reasoning.
Week 6 splits notebook defense/transfer into two 40-minute windows plus 40 minutes of prep/review.

Before a deep session read the one-page trainee packet and select two question chains from
[DEEP_DISCUSSIONS.md](DEEP_DISCUSSIONS.md). Each should take roughly 15-18 minutes, leaving time to challenge a claim
and record a gap. Keep the complete original banks as extension/reference; do not pretend every
question can be discussed within this schedule. A short independent derivation can precede the
meeting. The meeting tests the argument on a new case rather than replaying its worked solution.

Product questions are queued asynchronously with a decision needed, inspected paths, options and
recommended next step. Do not make a trainee wait for tomorrow merely to confirm an obvious safe
experiment, but do not let the agent approve product requirements. Review bounded MRs, not entire
repositories. If preparation starts exceeding 40 minutes weekly, narrow the session's scope.

## Prepare the teaching baseline before the cohort

The Peanuach system is still a specification, not working application code in this repository.
Provide a rectangle-only labeling UI/API/store and training-crop consumer; plate detector and
recognizer; overlapping/nonoverlapping airborne pairs; tracklets and motion labels; frozen
satellite detections/GT/metadata; ten-second clips; approved encoder weights; safe deployment and
storage. Map actual paths in [PRODUCT_AND_PREPARATION.md](PRODUCT_AND_PREPARATION.md). Prepared data is not a model solution.
Preparing a missing baseline is mentor/course-development work, not a hidden learner assignment.

## Stage 0

Guide VS Code, GitLab, Artifactory, OpenShift, Confluence and Jupyter readiness. Teach expected
outputs and escalation owners. The stack already exists internally. Do not assess cluster setup,
runner administration or YAML. GitLab needs a brief MR/pipeline/job-log walkthrough only.
The 30-minute Matt Pocock skill discussion is inside the first meeting; see [SKILLS_STAGE0](../docs/SKILLS_STAGE0.md).
Use the selected deep-practice list in [SKILLS_STAGE0](../docs/SKILLS_STAGE0.md); catalog exposure does not require reading every skill body.

## Polygon assignment with product discovery

The learner receives only: "Just add polygon support to the labeling website."
Do not expose the downstream checklist before discovery. Be a consistent product owner and answer
real questions; do not mutate requirements to manufacture failure.

Hold these decisions and disclose them when asked: a simple polygon without holes is sufficient
unless another scope is agreed; existing annotations and researchers must keep working; geometry
needs explicit coordinates/image revision/version; old boxes can become four-corner rectangles
without claiming exact object outlines; a real downstream consumer prepares training crops.
Clarify envelope crop versus masked crop versus special quadrilateral rectification. A general
polygon cannot be flattened by one homography. A reasonable teaching default is an envelope plus
mask/offset when that matches the actual consumer, not an unstated answer the agent should guess.

The trainee should discover UI, API validation, persistence/edit/reload, old data/migration,
export/loader and training-crop effects by reading code and asking product questions.
Keep acceptance tests mentor-only: polygon editing/undo/zoom coordinates; storage roundtrip;
versioned old/new data; a tested migration/compatibility plan with counts, provenance, idempotence
and rollback; training-loader smoke; correct crop/mask/original-coordinate mapping; malformed or
degenerate shapes; independent geometric fixtures. Do not require a large training run.
A compatibility reader alone without a migration plan/test does not satisfy the requested change.
If stuck, first ask "who consumes this output?" and record hints rather than immediately revealing
the map. Assess discovery and evidence, not whether the learner guessed your preferred architecture.

## Classical CV and evaluation sequence

Hough must actually contribute to plate-boundary estimation. Check character/frame confusion,
corner order, ROI truncation, warp geometry and fallback. Part 2 needs sanity checks, not a
statistically defensible improvement claim before evaluation has been taught. Return in part 3
to paired baseline/variant evaluation with the same recognizer/detector, grouped splits, exact match,
CER, latency and all failure/fallback cases included.

Two-image stitching is mandatory; more requires your approval. Check transform direction, inlier
coverage, independent control points, canvas, parallax and no-overlap rejection. A blended seam is
not a registration proof. Full georeferencing/orthomosaic construction is outside the core scope.

## Classical ML and rescoring

Tracklets need motion labels, decision time, units, camera-motion/fragmentation reasoning and no
future features. Prefer a small baseline plus classical model with held-out evaluation over broad
hyperparameter search. Ask about a new video/sensor distribution rather than library syntax.

Rescoring freezes the detector and uses independent GT with a defined matching target. Check
training/calibration/test independence, metadata ablations, missingness, physical-size assumptions
and angle conventions. A more vertical angle is not universally worse. Better ranking is not
probability calibration, and rescoring cannot recover absent proposals. Follow the chosen estimator
through saved hash and loaded service model. The SVM-C mismatch is one useful deep discussion.

## Cloud proposal

Budget eight hours: a simple baseline and two plausible sourced alternatives, architecture, data,
training and evaluation. No full training project. Discuss spectral channels, sensor/GSD shift,
cloud/shadow/no-data definitions and partial-tile policy. Pixel IoU alone does not establish net
compute savings or object recall retained after gating. Unmeasured impact must remain unmeasured.
Skipped coverage is not evidence of zero objects.

## Staged ordinary-camera video requirements

Use ordinary ground/handheld/vehicle-camera clips, not satellite or aerial video.
Start only with the three questions in the learner brief. After a baseline demonstration, release
[releases/video-02.md](releases/video-02.md). After initial handling release [video-03.md](releases/video-03.md). Do not expose the entire backlog
in advance or insist that the only correct solution is a VLM.

Budget 19 hours for a small baseline and 15 for subsequent requests: roughly five for the first
change, seven for a focused alternative probe and three for regression/decision. At least one added
question must run. Twenty questions describe a scaling demand, not twenty fully trained heads.
A heavy unavailable model can receive a proposal/small substitute probe with unverified status,
not fabricated runtime results. Compare annotation cost, question-addition time, latency, semantics
and preservation of existing answers. Fixed academic benchmarks and evolving product definitions
exercise different constraints; both still need sound empirical validation.

## Final two windows

First 40 minutes: 10 clean run and artifact trace, 25 explain difficult lines/helpers and a new
input, 5 record uncertainty. Second 40: 15 bounded failure, 15 peer transfer, 10 feedback.
Do not add another long grilling day outside the budget. Independent learning remains deep; the
mentor samples high-value reasoning instead of examining every historical question.

Dataset selection and offline preparation: [catalog](../docs/DATASETS.md), with small prepared
subsets and explicit missing-label/metadata limits. No new mandatory benchmark is added.

## Open-model foundations within the existing budget

Require lessons/07-open-models before the video baseline. Two study hours replace repeated
representation introductions in the seven-hour DL block; the one-hour probe is inside the existing
19-hour baseline budget. Prepare one approved local embedder and saved detector/VLM runs with
complete provenance; optional live heavy inference must not become three deployment projects.
Use one existing week-5 question chain for cosine/softmax, spatial evidence and language priors.
Do not add another first-session basics check or leak later video requests.
