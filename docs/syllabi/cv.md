# 2 · Classical computer vision

[Training index](../TRAINING_INDEX.md)

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
See [course videos](../reading/cv.md#videos-and-course-selection).

Retained UD810 / CS4495 selection: units 1, 2, 3, 4, 6, 7A, 9A and 9B.

## Mentor conversations

Session 1: filters/Hough and a new toy derivation. Session 2: geometry, matching, warping and a difficult image pair; include flow/stereo reasoning even when the main implementation uses homography.

The mentor continues using the existing theory questions. Understanding is assessed, not reading completion.
