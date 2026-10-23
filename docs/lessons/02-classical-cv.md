# Classical CV for plates and airborne imagery

## Filtering and coordinates

An image has channel order, dtype, range and spatial meaning. RGB and BGR are different; uint8
arithmetic can overflow. Convolution aggregates a neighborhood with a kernel. Blur can suppress
noise and erase small details. Sobel measures local changes; Canny produces edges, not guaranteed
object boundaries. Letters and bolts may create stronger edges than a plate frame.

Explain correlation versus convolution, Gaussian scale, separable filtering and why smoothing
before downsampling reduces aliasing. Use one small example rather than a full second signal course.
Morphology changes binary shapes: erosion shrinks, dilation expands, opening erodes then dilates,
and closing reverses the order. The kernel can remove true small objects or merge adjacent ones.
Preserve class IDs when resizing label masks. Keep the coordinate/inverse-transform contract.

## Hough and plate rectification

A useful line representation is rho = x*cos(theta) + y*sin(theta). Edge points vote in parameter
space; compatible support forms candidate lines. Standard Hough produces line parameters;
probabilistic Hough may produce segments. Bin size, support threshold, segment length and gaps
control different tradeoffs. Select plausible plate boundaries, not blindly the four strongest lines.
Show candidate overlays as well as the final crop.

Four consistent nondegenerate correspondences can determine a planar projective mapping, but
four points alone do not establish stable estimation. Check corner ordering, convexity, area,
orientation and degeneracy. An affine map cannot represent every perspective distortion.
Homogeneous coordinates allow translation and projection to be expressed with matrices.

An axis-aligned detector ROI may truncate the true plate. A warp cannot recover pixels that were
removed; clarify margins and use of the original image. Keep x/y, width/height, resize and padding
conventions explicit. Missing reliable boundaries require a documented failure/fallback policy.
Part 2 checks geometry and examples. Formal evidence of improved recognition comes in part 3.

## Stitching exactly two images

Find features and descriptors, match with a suitable distance and reject ambiguous matches.
RANSAC reduces the effect of outliers under its assumed model; repeated patterns, poor spatial
coverage or the wrong geometry can still produce a bad transform. Inspect inlier distribution,
not just count. Explain a corner detector/descriptor at a conceptual level; exhaustive Harris/SIFT
and optical-flow derivations are optional follow-up.

State the direction of the homography. Transform image corners to compute a canvas and translation
that preserve negative coordinates, then warp and blend the overlap. A smooth seam does not repair
bad registration. Use independent check points, reprojection error and an explicit no-overlap case.

An airborne sensor translates; buildings and terrain introduce parallax. A single homography is
a planar approximation, not a general orthomosaic. Lens distortion, rolling shutter, scene motion
and exposure changes may matter. Explain when to reject a stitch or choose another model; do not
claim geospatial accuracy without reference-system checks and independent measurements.

Self-check: intersect known lines, map a point forward/backward and explain a parallax counterexample.
Two-image stitching is required; extending to more images requires explicit mentor approval.
