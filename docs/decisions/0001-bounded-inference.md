# Bounded detector inference

Status: accepted

## Context

The image consumer may submit more images than fit comfortably in one forward pass. Training
and inference use an explicit saved artifact, and consumers retain the original image ordering.

## Decision

The detector CLI delegates to `predict_batches` with a default batch size of 256. Each forward
pass handles a bounded slice, and the CLI concatenates the output fields in input order. Partial
final batches are included, so the result contains one box, class-probability vector and object
probability per submitted image. Consumers can pair these arrays directly with their input IDs.

The API does not search for another checkpoint or retry against a different model. A missing
artifact is a setup error rather than an empty scene.

## Consequences

The CLI bounds forward-pass memory, while retaining the combined output in memory. Very large
jobs may need an incremental writer. Changing the batch size is an execution choice; it does not
change the consumer's ordering or output schema. See [the detector interface](../DETECTOR.md).
