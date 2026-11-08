# 3D vision, depth, reconstruction and learned scene representations

[All training](index.md) · [Source coverage](sources.md)

## One pixel of disparity can matter a lot.

Take focal length f=100 pixels and baseline B=1 metre. Disparity 10 gives depth 10 m; disparity 9 gives about 11.1 m.

![One pixel of disparity can matter a lot. d=10 → Z=10 m; d=9 → Z≈11.1 m; Z=fB/d](assets/dl-3d-toy.svg)

| Notice | Interpret | Check |
| --- | --- | --- |
| Same one-pixel change | Different depth uncertainty | Calibration and units matter |

<details>
<summary>Reveal the catch</summary>

Depth is inferred through geometry and assumptions. Small image errors can become large world errors.

</details>

**Try it in 60 seconds:** Repeat the calculation at disparities 2 and 1. Why is the depth change larger?

Read for understanding, not page completion. Skip what you can already explain.

<details>
<summary>Jump to a concept</summary>

- [Geometry before architecture](#geometry-before-architecture)

- [Depth and ambiguity](#depth-and-ambiguity)

- [3D representations](#3d-representations)

- [Differentiable rendering and neural fields](#differentiable-rendering-and-neural-fields)

- [Data and evaluation](#data-and-evaluation)

- [Connection to airborne imagery](#connection-to-airborne-imagery)

</details>

## Geometry before architecture

A 2D image collapses depth through projection, so reconstructing a 3D scene requires extra observations or assumptions. Calibrated stereo provides two rays; structure from motion estimates camera poses and sparse points from multiple views; multiview stereo densifies geometry given sufficient overlap and reliable appearance. Bundle adjustment jointly refines camera/point parameters by minimizing reprojection error. Its gauge freedoms, outliers and initialization need explicit handling.

## Depth and ambiguity

A monocular network can learn depth-related priors from data, but the image alone does not uniquely determine metric depth in every scene. A model may infer typical object size or camera height and fail when those priors change. Relative depth ordering and metric depth are different targets. Aligning predictions to ground truth with a fitted scale/shift changes what the metric claims; declare that protocol. Evaluate boundaries, reflective surfaces, occlusions and depth ranges rather than one global mean.

## 3D representations

A point cloud stores sampled locations, optionally colors, features and uncertainty. A voxel grid discretizes space and becomes costly as resolution increases in three dimensions. A mesh represents surfaces using vertices and faces; its connectivity can express shape compactly but requires topology decisions. Implicit fields represent quantities such as occupancy or signed distance as a function of position. Each representation supports different rendering, editing and loss calculations.

Distances between point sets, such as Chamfer-like objectives, depend on sampling density and can hide topological problems. A dense point cloud can be systematically offset. Metric units, coordinate axes and world-to-camera conventions need the same care as array layouts in 2D. A left-handed/right-handed mismatch can yield a recognizable but reflected reconstruction.

## Differentiable rendering and neural fields

Differentiable rendering connects a scene representation to predicted images and propagates image losses toward scene parameters. A neural radiance field models viewing-dependent radiance and volume density and renders by integrating along camera rays. It can synthesize novel views when trained with suitable images/poses, but visual agreement does not automatically give an accurate physical surface or generalize to unseen lighting. Gaussian-splat-style scene representations use explicit spatial primitives with learned appearance for efficient rendering; visibility and geometry assumptions still matter.

## Data and evaluation

Learned reconstruction may memorize scene identity or infer hidden surfaces from a prior. Test novel viewpoints separately from novel scenes. Record camera calibration, exposure, motion blur and rolling-shutter considerations when relevant. Check geometric consistency, held-out image rendering and metric measurements according to the application. A good rendered view can coexist with poor depth behind an observed surface.

## Connection to airborne imagery

Buildings and elevated structures produce viewpoint-dependent displacement. A planar warp that aligns roads may misalign roofs, which can mimic construction change. Use multiview geometry and metadata to reason about parallax before labeling a difference as semantic. For a bounded exercise, project a few known 3D points into two synthetic cameras, triangulate them and perturb image locations to inspect depth uncertainty.

The old 3D lecture remains in the course map. No separate reconstruction project is required by this syllabus. Ask the agent to explain the geometric ambiguity of one image and then demonstrate it using two different 3D configurations that produce similar projections. Bring that example to the mentor instead of only listing model names.

<details>
<summary>Original source references and provenance</summary>

Original teaching text covering the cited topics, not a verbatim mirror. These references are provenance; no external reading is required to use this chapter.

- [https://cs231n.stanford.edu/slides/2025/lecture_15.pdf](https://cs231n.stanford.edu/slides/2025/lecture_15.pdf)

</details>
