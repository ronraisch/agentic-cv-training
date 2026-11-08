# Hand over a reproducible video inference path

## Goal and starting point

A peer can run and understand the completed system without needing your oral explanation.
Close the released product tasks and concept checks with the mentor first. There is no additional
detector implementation at this stage.

Use the ordinary-camera video subset and frozen split from part 4B. Keep the current service's
actual inference code and artifact revision; do not switch to satellite footage or another benchmark.
[Relevant data](../../docs/DATASETS.md#ordinary-camera-video-and-handover).

## Prepare the handover

Create a notebook that runs the current video inference path and makes the following visible:
input/timestamps, sampling, transforms, representation, decisions, unknown/error handling and
service output. Explain critical lines and any imported helpers.

Check a new input, then Restart and Run All. The run must not depend on hidden notebook state
or runtime downloads. Include the ADR, quality/cost evidence, unresolved assumptions and exact
replay commands. Verify the internal endpoint in the teaching environment with the mentor;
a local container alone does not establish that deployment works.

## Demonstrate and transfer

Use the two planned 40-minute handover windows. Explain the implementation, predict a new result,
investigate a bounded failure and show that a peer can reproduce the path from the supplied
material. Syntax memorization and building another CI/CD pipeline are not assessment goals.
