# Video representations and consumer questions

A ten-second clip has timestamps and frame order, not merely N images. Define window, sampling,
stride, resolution and short/corrupt-input behavior. A still frame can support road presence but
not establish that a vehicle passed. Indoor/outdoor may refer to the camera location or visible
content. Sky-only and useful-information labels depend on the consumer's definitions.

Several questions need not be mutually exclusive. Use independent targets where appropriate;
a single softmax can introduce false competition. Missing labels are not automatically negatives.
Define unknown, insufficient evidence and error separately. Annotate a small diverse set using a
clear protocol and inspect ambiguous cases before expanding labels.

A frozen video embedding plus a small head is a possible baseline. Record exactly what the encoder
sees, its temporal/spatial sampling, pooling and revision. Frame pooling may work for presence and
fail on ordered events. Not every video embedding is text-aligned. Keep overlapping clips from one
source out of opposite splits. Evaluate per question and check camera/source shortcuts.

A shared text/video space needs learned semantic alignment, not just equal vector dimensions.
Similarity to text is not a calibrated probability. Check negation, near-synonyms and temporal claims
on this domain. A VLM needs structured answers, parsing, uncertainty and independent evaluation;
fluent output is not evidence. Sampling a few frames with an image VLM is not automatically temporal
video reasoning. No larger model is universally the right next step.

Compare annotation cost, time to add capability, latency, memory, internal availability and maintenance.
A benchmark with a fixed ontology does not settle a consumer's evolving definitions or service
contract. New model/encoder revisions may invalidate features, heads and caches. Preserve existing
answers during changes and record what was tested versus inferred.

The inference path includes decode, sampling, transforms, representation, decision and serialization.
The notebook must call the same modules and artifacts as the service, explain intermediate shapes,
handle unknown/error and survive a clean restart. Use an approved agent to learn unfamiliar concepts;
explain every critical line and imported helper yourself during the teach-back.
