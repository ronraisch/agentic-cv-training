# Required DL assignment — RabbitMQ, SAM3 pseudo-labels and detector training

Build a resumable batch-labeling pipeline for ordinary-camera video frames, then train one
detector on its output. This belongs in the deep-learning/video block, after
[training fundamentals](../../docs/lessons/04-torch.md) and before final
[video handover](06-handover.md). Use the approved agent/local LLM.
Initial allocation: 24 trainee hours; measure actual effort separately from unattended GPU runtime.

## Outcome and scope

Deploy a teaching RabbitMQ broker and a containerized SAM3 consumer on the existing OpenShift
stack. Write a producer that submits a manifest of approved frames. Use messages to carry the
image reference and prompt configuration; do not require the entire dataset in a notebook session.
Run real SAM3 inference and persist pseudo-labels. Export the accepted training data for one
mentor-agreed RT-DETR or YOLO detector, train it, reload its checkpoint and run inference on new
video frames. Choose one detector, not both. Reuse existing image/registry/deployment knowledge
from [the SAM2 service](01b-sam2-service.md).

Agree with the mentor on target classes, prompt wording, dataset volume, device budget and detector
variant before starting. Start with a tiny verified batch, then run a substantially larger batch
whose frame count and runtime budget are recorded. The full batch must execute; a queued job count
alone is not completion. No invented universal image count or accuracy target is required.

## Queue and worker contract

Define and version a message schema: job ID, dataset/frame ID, authorized shared image path or
object reference, prompts, prompt-to-class mapping/config revision, model revision and output
reference. Freeze the job configuration so retries remain traceable. Credentials are secret
references, not message values. Keep images/checkpoints/results in approved shared storage.

Use durable queue/storage configuration and publisher confirmation appropriate to the selected
RabbitMQ version. Acknowledge work only after its result is durably saved. Bound in-flight work
and consumer concurrency to available GPU memory. Define finite retry behavior, a dead-letter
destination for permanent failures and observable job states. Duplicate delivery must not create
duplicate training examples or silently overwrite results from a different model/prompt revision.
Do not claim exactly-once inference; demonstrate idempotent committed outputs.

The trainee configures the teaching broker's image, persistent storage, credentials and internal
Service, plus the worker Deployment and model/data mounts. AMQP remains internal; an external
HTTP Route is not a requirement for this broker. Use approved base images/packages and local SAM3
assets without runtime downloads. Do not administer or modify a production broker.

## Pseudo-labels and learning quality

Store model/checkpoint, prompt, class mapping and preprocessing provenance with each labeling run.
Make mask-to-box conversion, coordinate conventions and filtering explicit for detector training.
Review a sample of labels and record class-specific errors, missed objects and corrections.
An absent SAM3 prediction is not proof that the image contains no target objects; define how
incomplete labels and background examples are handled rather than silently treating all misses
as verified negatives.

Split by source video/scene before frame sampling or pseudo-label production. Keep neighboring
frames from the same source out of different splits. Use a bounded independently human-checked
validation/test set; agreement with SAM3 pseudo-labels alone does not establish detector accuracy.
Report a detector metric on that set alongside qualitative examples and its limitations.

## Required demonstration

Show producer submission, real SAM3 processing, durable labels and a reconciled manifest of
successful, failed and pending jobs. Record processed count, throughput and labeling configuration.
Stop a worker mid-job, restart it and demonstrate recovery without duplicate committed labels.
Replay a job and submit one invalid reference to demonstrate deduplication and bounded failure
handling. Explain acknowledgment, redelivery, prefetch/backpressure and dead-letter behavior.

Then show exported examples, actual detector parameter updates, saved-checkpoint reload and
inference on held-out video frames. Submit code, schemas, Dockerfiles/manifests and reproducible
submit/status/resume/export/train/predict instructions with sanitized evidence.
A notebook may inspect results; it must not be the long-running queue consumer or batch orchestrator.

The mentor supplies approved RabbitMQ/SAM3/detector assets, compute and teaching namespace access
through [the environment handoff](../../docs/RESEARCH_ENVIRONMENT.md).
Unavailable prerequisites are BLOCKED with an owner, not a reason to replace the pipeline with mocks.
This assignment specifies required work; the repository's synthetic baseline does not implement it.
