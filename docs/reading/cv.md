# 2 · Classical computer vision

[Chapter index](index.md) · [Source coverage](sources.md)

**Reading is for you; page completion is optional.** If you can explain the concepts and answer the mentor's questions yourself, that is enough. Use these pages and the course videos to deepen understanding during the exercises with your approved agent. [Learning route and manual-work boundaries](index.md).

<details>
<summary>On this page</summary>

- [Learning route and expected understanding](#learning-route-and-expected-understanding)

- [Practical work](#practical-work)

- [Videos and course selection](#videos-and-course-selection)

- [Mentor conversations](#mentor-conversations)

- [Original learner material](#original-learner-material)

</details>

## Learning route and expected understanding

Recommended first-pass study: 12–18 active hours; viewing/reflection: 8–12 active hours. These are planning ranges, not deadlines or measured full-course runtimes. Skip known explanations; deepen gaps. Record actual time.

| Topic | Local reading | What to understand and apply |
| --- | --- | --- |
| Images, convolution, correlation and filters | [Signals, filters, edges and Fourier analysis](cv-filtering.md) | Explain sampling, padding, Gaussian/separable filters, normalized correlation and edge detection. |
| Hough and Fourier | [Hough voting, cameras, stereo and projective geometry](cv-geometry.md)<br>[Signals, filters, edges and Fourier analysis](cv-filtering.md) | Draw line/circle voting, accumulator discretization and frequency-domain filtering. |
| Cameras, perspective and stereo | [Hough voting, cameras, stereo and projective geometry](cv-geometry.md) | Use homogeneous coordinates, transforms, epipolar constraints and depth/disparity assumptions. |
| Corners, descriptors and robust matching | [Features, RANSAC, warping, optical flow and tracking](cv-matching-motion.md) | Explain Harris/SIFT, ambiguous matches, RANSAC and geometric model failure. |
| Warping, pyramids, flow and tracking | [Features, RANSAC, warping, optical flow and tracking](cv-matching-motion.md)<br>[Signals, filters, edges and Fourier analysis](cv-filtering.md) | Inspect inverse warp, interpolation, aliasing, brightness constancy and temporal confidence. |

## Practical work

- [LPR rectification and two-image stitching](../../labs/research/02-classical-cv.md)

Read selectively before and during implementation; discuss hypotheses with your agent, verify one counterexample and explain the evidence yourself. The manual Python capstone and first SAM2 service retain their existing manual rules.

## Videos and course selection

Retain Udacity UD810 / CS4495 units 1, 2, 3, 4 and 6 in full, plus 7A, 9A and 9B. Other units remain optional. Use [the original course](https://www.udacity.com/enrollment/ud810) and [the original unit/video index](https://docs.google.com/spreadsheets/d/1ecUGIyhYOfQPi3HPXb-7NndrLgpX_zgkwsqzfqHPaus/pubhtml). The old standalone PS exercises are historical alternatives; the required LPR/stitching work is linked above.

## Mentor conversations

Session 1: filters/Hough and a new toy derivation. Session 2: geometry, matching, warping and a difficult image pair; include flow/stereo reasoning even when the main implementation uses homography.

The mentor keeps the existing theory questions and probes your reasoning with a new example. Reading-page completion is not assessed. If you can answer and explain the assigned concepts yourself, your learning route is sufficient. Gaps lead to targeted study and another discussion, not an obligation to reread every source.

## Original learner material

Complete historical handouts are preserved locally with their reading links redirected. Historical project requirements are not added to the current workload.

- [Original 2025 program outline](legacy-outline.md)
