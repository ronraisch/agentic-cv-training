# Part 4B Describe ten seconds of video

An ordinary-camera video consumer currently needs three answers for a ten-second clip.
Use ground, handheld or vehicle-camera video, not satellite or aerial footage:

- Is there a road?
- Is the view indoors or outdoors?
- Does the clip show only sky?

Clarify question meanings and input/output requirements with product. Start with a small testable
solution, for example an available video embedding, a few manual labels and a small learned head.
That is a possible starting point, not a mandatory architecture. Justify a better-fitting alternative.

Deliver a baseline, evaluation and runnable prediction on a new clip. Explain sampling/time,
model and representation versions, missing information and what the metrics establish.
The mentor supplies the next part of the request after the first demonstration.

Required learning: [video](../../docs/lessons/06-video.md), [ML](../../docs/lessons/03-metrics-ml.md)
and [training](../../docs/lessons/04-torch.md). Use the agent for research explanation as well as
implementation; close it for the individual explanation.

[Relevant data sources](../../docs/DATASETS.md#ordinary-camera-video-and-handover). Use the mentor-prepared internal subset.

Before building the baseline, complete [the open-model introduction and one-hour intuition probe](../../docs/lessons/07-open-models.md).
The probe is part of the existing baseline time allocation and does not select your final architecture.
