# Answer three questions about a ten-second clip

## Start here

Use the assigned video checkout and mentor-approved ordinary-camera clips. Start with one clear and one borderline ten-second clip. Inspect timestamps and agree on the decision unit and when to abstain before choosing a model. Bring the baseline demo to the mentor before requesting continuation work. If you get stuck, use the [worked example](../../docs/WORKED_EXAMPLES.md#deep-learning-and-video).

## The request

For an ordinary-camera clip, answer:

- Is there a road?
- Is the view indoors or outdoors?
- Does the clip show only sky?

Use ground, handheld or vehicle-camera video. Satellite and aerial footage are outside this task.
The mentor acts as product owner; clarify what the questions mean and what the input/output
contract should be before choosing the implementation.

## Prepare the data and concepts

Use [the ordinary-camera subset](../../docs/DATASETS.md#ordinary-camera-video-and-handover)
and [the acquisition instructions](../../docs/DATASETS.md#acquire-a-working-subset).
Study the relevant [video](../../docs/lessons/06-video.md),
[ML](../../docs/lessons/03-metrics-ml.md) and [training](../../docs/lessons/04-torch.md) material.

Before the baseline, complete [the open-model introduction and one-hour intuition probe](../../docs/lessons/07-open-models.md).
The probe is already included in the baseline allocation; it does not prescribe the final architecture.

## Build and evaluate a first solution

Start with something small enough to inspect. An available video embedding, a few manual labels
and a small learned head are one possible starting point; justify an alternative if it fits better.

Use the approved agent for both implementation and understanding. Track sampling/timing choices,
model and representation versions, missing information and what the evaluation actually establishes.

## First demonstration and continuation

Show the baseline, its evaluation and runnable prediction on a new clip. Explain your decisions
independently, with the agent closed for the individual explanation. After that demonstration,
the mentor supplies the next part of the product request.

Also complete [the required RabbitMQ/SAM3 detector pipeline](05b-rabbitmq-sam3-detector.md)
before handover. Its initial 24-hour allocation is separate; it does not replace this clip-level
scene-understanding task. It trains one RT-DETR or YOLO detector, not both.
