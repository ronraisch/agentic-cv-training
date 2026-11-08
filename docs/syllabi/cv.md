# 2 · Classical computer vision

[All training](../TRAINING_INDEX.md) · [Reading syllabus](../reading/cv.md)

Reading is a resource for you, not mandatory page completion. If you can answer the mentor’s questions and explain a new example yourself, that is enough. Theory and videos remain substantial parts of the program. Use the approved agent to deepen understanding during exercises; respect the manual assignments.

## Topics and local reading

| Topic | Reading in this repository | Apply and explain |
|---|---|---|
| Images, convolution, correlation and filters | [Signals, filters, edges and Fourier analysis](../reading/cv-filtering.md) | Explain sampling, padding, Gaussian/separable filters, normalized correlation and edge detection. |
| Hough and Fourier | [Hough voting, cameras, stereo and projective geometry](../reading/cv-geometry.md); [Signals, filters, edges and Fourier analysis](../reading/cv-filtering.md) | Draw line/circle voting, accumulator discretization and frequency-domain filtering. |
| Cameras, perspective and stereo | [Hough voting, cameras, stereo and projective geometry](../reading/cv-geometry.md) | Use homogeneous coordinates, transforms, epipolar constraints and depth/disparity assumptions. |
| Corners, descriptors and robust matching | [Features, RANSAC, warping, optical flow and tracking](../reading/cv-matching-motion.md) | Explain Harris/SIFT, ambiguous matches, RANSAC and geometric model failure. |
| Warping, pyramids, flow and tracking | [Features, RANSAC, warping, optical flow and tracking](../reading/cv-matching-motion.md); [Signals, filters, edges and Fourier analysis](../reading/cv-filtering.md) | Inspect inverse warp, interpolation, aliasing, brightness constancy and temporal confidence. |

## Practical work

- [LPR rectification and two-image stitching](../../labs/research/02-classical-cv.md)

## Viewing and study

Recommended first-pass study: 12–18 h; viewing/reflection: 8–12 h. These ranges are estimates, not hard caps or measured course runtimes. Record actual effort and deepen unfamiliar subjects.
Use [the full course/video list](../reading/cv.md#videos-and-course-selection). Exact source URLs and legacy alternatives are preserved there.

Retained UD810 / CS4495 selection: units 1, 2, 3, 4, 6, 7A, 9A and 9B.

## Mentor conversations

Session 1: filters/Hough and a new toy derivation. Session 2: geometry, matching, warping and a difficult image pair; include flow/stereo reasoning even when the main implementation uses homography.

The mentor continues using the existing theory questions. Understanding is assessed, not reading completion.
