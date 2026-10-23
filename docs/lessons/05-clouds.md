# Cloud segmentation as an operational decision

The consumer wants to avoid object-detector work where imagery is unusable. A cloud mask does not
mean there are no objects. Define thick/thin clouds, shadows, haze, snow, no-data and partial cover,
and whether output is a mask, probability map or tile decision. A skipped area is unobserved.

Compare sensors, channels, GSD, acquisition geography and label protocols. A method needing bands
absent from the RGB service is not a drop-in replacement. Split by scene/acquisition, not overlapping
tiles. Consider domain shift explicitly. A short survey needs a baseline and two plausible research
alternatives, not a ranking of dozens of papers.

A light segmentation head or encoder-decoder may be a reasonable proposal depending on data and
compute. Explain freeze/fine-tune, sampling, augmentation, imbalance and loss. Keep target masks,
ignore labels, resizing and reduction semantics explicit. A tiny-overfit/overlay check precedes a
large training plan. Do not promise that a published architecture will transfer successfully.

Evaluate pixel metrics plus consumer impact: false cloud on clear areas, missed cloud, boundary
behavior, new sensors, net detector work saved and object recall lost through gating. Include the
segmentation overhead. Object annotations are needed to measure false-cloud harm; if absent,
state that the operational effect is unmeasured rather than fabricate it.

Define partial-tile behavior and the tradeoff between skipping, expanding a mask, processing uncertain
areas or falling back. Save the reason for skipped coverage, model/mask revision and acquisition time.
The proposal ends with a small falsifiable experiment, data/resource requirements and a conditional
recommendation. Training a full cloud system is not a core assignment.
