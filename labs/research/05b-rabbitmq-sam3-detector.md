# Label a video batch with SAM3, then train one detector

## Start here

Use the teaching namespace and approved worker, broker, model and data paths from the mentor. Start with three inspectable frames and verify one message can be followed to a saved output. Demonstrate recovery and audit a small label sample before scaling. See the [worked example](../../docs/WORKED_EXAMPLES.md#queue-to-training) before starting.

## Goal and scope

Build a batch-labeling pipeline that can resume after a worker failure. It processes ordinary-camera
frames with real SAM3 inference, saves pseudo-labels and supplies training data for one RT-DETR
or YOLO detector. Then reload that detector's saved checkpoint and predict on held-out frames.

This exercise is required in the DL/video block, after [training fundamentals](../../docs/lessons/04-torch.md)
and before [handover](06-handover.md). Use the approved agent/local LLM.
The initial allocation is 24 active trainee hours; record unattended GPU runtime separately.

## Before starting

Agree with the mentor on classes, prompt wording, data volume, detector variant and device budget.
The mentor supplies approved broker/model/detector assets, compute and teaching-namespace access
through [the environment handoff](../../docs/RESEARCH_ENVIRONMENT.md).

Split by source video/scene before sampling frames or generating pseudo-labels. Keep neighbouring
frames from one source out of different splits. Reserve a bounded, independently human-checked
validation/test set. Agreement with SAM3 alone is not an accuracy evaluation.

## 1. Bring up the broker and worker

Deploy a teaching RabbitMQ broker and a containerized SAM3 consumer on the existing OpenShift
stack. Reuse what you learned in [the SAM2 service](01b-sam2-service.md).
Configure broker image, persistent storage, credentials and internal Service, plus worker
Deployment and model/data mounts. AMQP stays internal; no external HTTP Route is required.

Use approved packages/base images and local assets without runtime downloads. Production-broker
administration is outside the exercise. A notebook can inspect results, but is not the long-running
consumer or batch orchestrator.

## 2. Define what a job means and how it recovers

Write a producer that submits an approved frame manifest. Messages carry references and
configuration rather than requiring the dataset to stay in a notebook session.
Define a versioned schema containing:

- Job ID and dataset/frame ID.
- Authorized shared image path or object reference.
- Prompts, prompt-to-class mapping and configuration revision.
- Model revision and output reference.

Freeze that configuration for retries. Keep images, checkpoints and results in approved shared
storage; credentials remain secret references, not message values.

Use durable queue/storage settings and publisher confirmation appropriate to the chosen RabbitMQ
version. Acknowledge only after a result is durably saved. Bound in-flight work and concurrency
to GPU memory. Define finite retries, a dead-letter destination for permanent failures and
observable job states.

A duplicate delivery must not add a duplicate training example or overwrite a result from a
different prompt/model revision. Demonstrate idempotent committed outputs; do not claim
exactly-once inference.

## 3. Verify a small batch, then execute the larger batch

Start with a tiny batch whose inputs, outputs and failures you can inspect. Then execute a
substantially larger batch with a recorded frame count and runtime budget. The batch must
actually process: a count of queued jobs alone is not completion. There is no universal required
image count or accuracy target.

Persist labeling provenance: checkpoint/model, prompts, class mapping and preprocessing.
Explain mask-to-box conversion, coordinates and filters used for the detector export. Audit a
sample for class-specific errors, missed objects and needed corrections. Define how incomplete
labels and background cases are treated; a missing SAM3 prediction is not a verified negative.

## 4. Export, train and evaluate

Export the accepted data for the one agreed detector. Show actual parameter updates during
training, save the checkpoint, reload it and run held-out inference. Report a detector metric
on the independently checked set, with representative outputs and limitations.

## Submit and demonstrate

Submit code, schemas, Dockerfiles/manifests and reproducible commands for
submit/status/resume/export/train/predict, with sanitized evidence. Demonstrate:

- Producer submission, real SAM3 processing and durable labels. Reconcile successful, failed
  and pending jobs, and record processed count, throughput and configuration.
- A worker stopped mid-job and restarted, recovering without duplicate committed labels.
- A replayed job and an invalid reference, showing deduplication and bounded failure handling.
- Exported training examples, real detector updates, checkpoint reload and held-out inference.

Explain acknowledgement, redelivery, prefetch/backpressure and dead-letter handling.
If prerequisites are missing, mark the exercise BLOCKED with an owner. Mocks do not replace
the required pipeline, and the repository's synthetic baseline does not implement it.
