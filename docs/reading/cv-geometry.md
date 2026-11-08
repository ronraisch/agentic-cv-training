# Hough voting, cameras, stereo and projective geometry

[All training](index.md) · [Source coverage](sources.md)

## When one warp aligns the road but misses the roof

Two airborne images show the same street from different viewpoints. After fitting a homography, road markings overlap neatly while building roofs remain doubled. This can look like a poor fit even when the estimated road alignment is correct.

![Why do roads align but roofs drift? View A; One planar warp; View B](assets/cv-geometry-toy.svg)

A homography can describe the relationship between views of one plane. An elevated roof lies on a different surface; camera translation can shift it differently through parallax. More iterations cannot make that single planar model describe arbitrary scene depth.

This is why transformation families and camera geometry matter when choosing what to fit, before worrying about the optimizer.

<details>
<summary>Jump to a concept</summary>

- [Voting for a geometric explanation](#voting-for-a-geometric-explanation)

- [Homogeneous coordinates and transformations](#homogeneous-coordinates-and-transformations)

- [Camera projection](#camera-projection)

- [Stereo and epipolar geometry](#stereo-and-epipolar-geometry)

- [Reading an airborne alignment](#reading-an-airborne-alignment)

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

## Reading an airborne alignment

An unblended overlay can be more informative than a finished panorama. In the two-image stitching assignment, residuals distributed across the overlap help distinguish a local matching failure from a global model mismatch. Roads and roofs behaving differently suggest parallax; a uniformly reversed displacement suggests checking the transform direction. The same visual symptom can therefore lead to very different repairs.
