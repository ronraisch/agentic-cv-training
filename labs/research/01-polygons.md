# Add polygons and oriented boxes to the labeling application

[Development syllabus](../../docs/syllabi/development.md) · [Companion lesson](../../docs/lessons/01-development.md) · Previous: [OMP and skills setup](00-installations.md#then-prepare-omp-and-skills) · Next: [First SAM2 service](01b-sam2-service.md)

## Start here

Use the [labeling application](../../docs/reference/BASELINE.md#label-real-imagery) in the assigned checkout.
Mount the four [real collections](../../docs/reference/DATA_FORMATS.md#labeling-collections) and start on an
annotated satellite image. Confirm the assigned revision and data mount with the mentor. Create, save and reopen one existing rectangle and locate its downstream consumer. Bring this trace and open product questions to the mentor before implementing. If you get stuck, use the [worked example](../../docs/reference/WORKED_EXAMPLES.md#rectangle-and-service).

## The request

> Add polygon and oriented bounding box support to the labeling website. For an oriented box,
> the annotator must be able to create and adjust its orientation, save it and reopen it in place.

Work in the assigned checkout with the approved agent. The mentor is the product owner
for this request. The short brief is intentional: clarify the intended interactions and completion
criteria with them before deciding what “support” includes.

## Start with the existing behaviour

Find the relevant application path and inspect how its current annotations are created, saved and
consumed. Use this to make the product questions concrete. Agree on the scope, implement the
change and verify it through a real downstream consumer. Compare an existing HBB, an oriented box
and a free-form polygon. Confirm validation, save/reload and the coordinates the consumer reads.
The detector starts with HBB outputs. You will connect real oriented model predictions in
[stage 4](04-oriented-detection.md).

Use the [development syllabus](../../docs/syllabi/development.md) for the associated theory and
individual discussion. Reading and the teach-back are separate from the code review.

## Submit and demonstrate

Submit a bounded, reviewable MR and show that the agreed request is complete on a new example.
Separate behaviour you actually verified from assumptions or paths you have not tested.

## What follows

Continue with [the required SAM2 annotation service](01b-sam2-service.md).
Its separate initial allocation is 16 hours.

[Labeling data](../../docs/reference/DATASETS.md#labeling-application) ·
[Acquisition steps](../../docs/reference/DATASETS.md#acquire-a-working-subset)
