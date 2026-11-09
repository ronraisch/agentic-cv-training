# Rectify a licence plate and stitch two airborne images

## Start here

Use the approved research checkout and the mentor-confirmed [CV fixture subset](../../docs/DATASETS.md#classical-cv-and-lpr-evaluation). Open one annotated plate image and one overlapping pair. Run raw LPR first and inspect the crop coordinates. Bring intermediate overlays and a failure case to the first review. See the [worked example](../../docs/WORKED_EXAMPLES.md#classical-cv) before starting.

## Goal and preparation

Use classical geometry in two existing image-processing tasks. For both, show the intermediate
results that explain how the output was produced, including a failure case.

Read selectively from [the CV syllabus](../../docs/syllabi/cv.md) and
[the practical CV lesson](../../docs/lessons/02-classical-cv.md).
Acquire [the CV/LPR subset](../../docs/DATASETS.md#classical-cv-and-lpr-evaluation) using
[the dataset instructions](../../docs/DATASETS.md#acquire-a-working-subset).

## Task 1: rectify a plate before recognition

First run [the supplied raw LPR path](../../docs/COMPONENTS.md#lpr-baseline-and-crop-recognition)
on your subset. Save its output, model hashes and configuration as the comparison baseline.

The detector returns an axis-aligned box, but the plate inside may be tilted or projectively
distorted. Add preprocessing that uses Hough lines to estimate its boundaries, then rectifies it
to a rectangle before recognition. Clarify the integration contract and failure behaviour with product.

Show the input, candidate lines, selected boundaries/corners, transform and resulting crop.
Explain the assumptions and retain failed cases. This stage checks working geometry and sanity;
[part 3](03-evaluation-ml.md) formally evaluates recognition. A straighter-looking plate alone
does not establish an improvement.

## Task 2: stitch two images from one flight

Use two sequential, overlapping airborne images to produce a larger image. Explain the feature
matching and geometric model. Also show an input pair for which reliable stitching is impossible
and explain the failure rather than forcing a plausible output.

Two images are required. Additional images need explicit mentor approval. A full orthomosaic
product and a claim of unmeasured geospatial accuracy are outside this task.

## Submit and explain

Submit bounded MRs with reproducible inputs/configurations and the intermediate visual evidence.
Use the allocated research-agent time to resolve one missing geometric concept, then explain it
independently in the individual session. Keep the saved LPR baseline for the next exercise.

## Handoff to ML

Save per-item IDs, original detector outcomes, raw and processed crop references and fallback reasons. Keep detector misses visible in the original manifest for [paired OCR evaluation](03-evaluation-ml.md).
