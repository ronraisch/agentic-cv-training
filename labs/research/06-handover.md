# Hand over a reproducible video inference path

## Start here

Use a clean peer workspace with the declared packages, supplied model checkpoint and an ordinary-camera clip. Ask the mentor for a service reference run. Confirm one new clip runs independently and bring parity evidence and a reproducible command to the handover windows.

## Goal and starting point

A peer can run and understand the completed system without needing your oral explanation.
Close the released product tasks and concept checks with the mentor first. There is no additional
detector implementation at this stage.

Use the ordinary-camera subset and frozen split from the [video lab](05-video.md). Use the service model and preprocessing revision. The detector-training outputs belong to [the SAM3 lab](05b-rabbitmq-sam3-detector.md).
[Relevant data](../../docs/DATASETS.md#ordinary-camera-video-and-handover).

## Prepare the handover

Deliver one self-contained, inference-only notebook. Include the input loader, sampling, transforms,
model construction and checkpoint loading, prediction, postprocessing and output in notebook cells.
Use declared standard packages and supplied data/checkpoint files. The peer runs it from a clean
directory with no repository checkout or imports from the application.

Compare the notebook and service on one shared clip. Record the clip ID, timestamps, preprocessing
and checkpoint revisions, outputs and any agreed numeric tolerance. Explain deviations and show the
unknown/error path.

Check a new input, then Restart and Run All. The run must not depend on hidden notebook state
or runtime downloads. Include the ADR, quality/cost evidence, unresolved assumptions and exact
replay commands. Verify the internal endpoint in the teaching environment with the mentor;
a local container alone does not establish that deployment works.

## Demonstrate and transfer

Use the two planned 40-minute handover windows. Explain the implementation, predict a new result,
investigate a bounded failure and show that a peer can reproduce the path from the supplied
material. Syntax memorization and building another CI/CD pipeline are not assessment goals.
