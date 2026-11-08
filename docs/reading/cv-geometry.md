# Hough voting, cameras, stereo and projective geometry

[All training](index.md) · [Source coverage](sources.md)

## Why do roads align but roofs drift?

Two airborne images share the same buildings. One homography aligns the road perfectly, yet roof edges remain doubled.

![Why do roads align but roofs drift? View A; One planar warp; View B](assets/cv-geometry-toy.svg)

| Notice | Interpret | Check |
| --- | --- | --- |
| Road: near the fitted plane | Roof: elevated surface | Translation creates parallax |

<details>
<summary>Reveal the catch</summary>

More RANSAC iterations cannot make a single plane describe every depth.

</details>

**Try it in 60 seconds:** Draw a road point and a roof point viewed from two camera positions.

Read for understanding, not page completion. Skip what you can already explain.

<details>
<summary>Jump to a concept</summary>

- [Voting for a geometric explanation](#voting-for-a-geometric-explanation)

- [Homogeneous coordinates and transformations](#homogeneous-coordinates-and-transformations)

- [Camera projection](#camera-projection)

- [Stereo and epipolar geometry](#stereo-and-epipolar-geometry)

- [Reason about an actual pair](#reason-about-an-actual-pair)

</details>

## Voting for a geometric explanation

Hough transforms convert local evidence into votes for model parameters. A point (x,y) lies on every line satisfying `rho = x cos(theta) + y sin(theta)`. It therefore traces a sinusoid in parameter space. Collinear points vote at a common parameter pair. Unlike slope/intercept coordinates, polar parameters include vertical lines without infinite slopes. Choose consistent ranges for signed rho and angle so equivalent lines are not mistakenly counted twice.

An accumulator discretizes parameter space. Coarse bins merge nearby lines; very fine bins fragment noisy evidence. Nonmaximum suppression finds separated peaks, and fitting around a peak or refitting supporting pixels improves localization. Gradient orientation can restrict plausible votes. A large vote count does not prove a line is the desired plate edge: text, background fences and shadows can all vote strongly.

A known-radius circle has two center parameters. A boundary point votes for possible centers at that radius. Unknown radius adds a third parameter and increases computation and ambiguity. Concentric circles share centers but differ in radius; suppressing peaks across too wide a radius range can remove a real second circle. Accumulator neighborhoods should reflect the geometry and desired object separation.

## Homogeneous coordinates and transformations

Represent a 2D point as (x,y,1), with any nonzero scalar multiple representing the same projective point. Translation becomes matrix multiplication. A rigid planar transform rotates and translates; a similarity also scales uniformly. An affine transform allows shear and independent linear scaling while preserving parallel lines. A projective homography has eight degrees of freedom up to scale and maps lines to lines, but need not preserve parallelism or angles.

For generic nondegenerate point correspondences, a similarity can be determined from two points, an affine transform from three noncollinear points and a homography from four with no problematic collinear configuration. More correspondences allow a noisy fit and validation. Parameter count is necessary but not sufficient: repeated, collinear or poorly spread points can make the estimate unstable. Normalize coordinates, inspect conditioning and measure residuals in meaningful units.

## Camera projection

A pinhole camera maps a 3D homogeneous point through `p ~ K [R | t] X`. K describes intrinsics such as focal length in pixels and principal point; R and t describe the world-to-camera pose under a declared convention. Perspective division converts homogeneous coordinates to image coordinates. Lens distortion is a separate model and can break a simple projective fit at wide fields of view. A planar scene or pure camera rotation supports a global inter-image homography. A scene with depth variation and camera translation usually produces parallax that one homography cannot remove.

## Stereo and epipolar geometry

Two cameras observe the same 3D point along two rays. The plane through that point and both camera centers intersects each image in an epipolar line. Thus a point in one image constrains its match to a line in the other, expressed by `x2^T F x1 = 0`. The fundamental matrix applies to pixel coordinates; the essential matrix applies after intrinsic normalization. Rectification warps the pair so corresponding epipolar lines align, often horizontally. Parallel image planes alone should not be treated as a complete calibration specification.

In a rectified ideal pair, disparity is inversely proportional to depth: `Z = f B / d` for compatible units and conventions. Small disparity errors at long distance create large depth errors. Occlusion, repeated textures and non-Lambertian surfaces make matching difficult. A larger matching window reduces noise but crosses depth boundaries; a smaller window preserves detail but lacks evidence.

## Reason about an actual pair

For the two-airborne-image stitching task, declare coordinate direction and the surface assumptions before fitting. Plot correspondences across the full overlap and inspect reprojection errors on held-out matches. If tall buildings align differently from roads, consider parallax before increasing RANSAC iterations. An image warp may be visually smooth while still being geographically wrong.
