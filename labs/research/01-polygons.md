# Add polygons to the labeling application

## Start here

Use the internal Remote Sensing checkout. Get the revision, run command, access and a known image from the mentor. Create, save and reopen one existing rectangle and locate its downstream consumer. Bring this trace and open product questions to the mentor before implementing. If you get stuck, use the [worked example](../../docs/WORKED_EXAMPLES.md#rectangle-and-service).

## What to build

Add polygon annotations to the existing labeling app. A user should be able to draw a polygon
on an image, edit its vertices, save it, and reopen the image with the polygon in the same
position. The existing downstream consumer should be able to read the saved polygon.
Existing rectangle annotations should still open and save as before.

## Before implementing

Follow a rectangle through the editor, API, storage and downstream consumer. Review that
path with your mentor and agree on interaction details such as how to finish drawing and
how to handle a polygon with too few vertices. Use the existing app conventions where they
already answer those questions. Work in the internal monorepo with the approved agent.

Use the [development syllabus](../../docs/reading/development.md) for the associated theory and
individual discussion. Reading and the teach-back are separate from the code review.

## Submit and demonstrate

Submit a bounded, reviewable MR. On a fresh, non-square image, create an asymmetric polygon,
edit a vertex, save and reload it. Check the downstream result and reopen a rectangle from
before the change. If the polygon shifts, compare the vertices in the save request, the stored
record and the reload response before inspecting how the editor draws them. Record what you
verified and any paths you could not test.

## What follows

Continue with [the required SAM2 annotation service](01b-sam2-service.md).
Its separate initial allocation is 16 hours.

[Labeling data](../../docs/DATASETS.md#labeling-application) ·
[Acquisition steps](../../docs/DATASETS.md#acquire-a-working-subset)
