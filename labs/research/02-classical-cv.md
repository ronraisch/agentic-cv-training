# Part 2 Classical CV tasks

Required learning: [Classical CV](../../docs/lessons/02-classical-cv.md).

## Plate rectification before LPR

The detector returns an axis-aligned plate box, while the actual plate may be tilted or projectively
distorted. Add preprocessing that uses Hough lines to estimate plate boundaries and rectifies the
plate to a rectangle before recognition. Clarify the system contract and failure behavior with product.

Show input, candidate lines, chosen boundaries/corners, transform and output. Retain failures and
explain assumptions. Looking straighter does not prove improved recognition. Here we require working
geometry and sanity checks; formal evaluation comes in part 3. Preserve baseline/configuration.

## Two images from one airborne flight

Stitch two sequential overlapping images into a larger image. Explain matching and geometry, and
show a case where reliable stitching is impossible. Do not force a plausible-looking output.
Two images are required. More images are a bonus requiring explicit mentor approval.
A full orthomosaic product or unmeasured geospatial accuracy is not required.

Submit bounded MRs, reproducible examples and evidence. Use the funded research-agent slot to learn
one missing geometric concept, then explain it independently in the individual session.

[Relevant data sources](../../docs/DATASETS.md#classical-cv-and-lpr-evaluation). Use the mentor-prepared internal subset.
