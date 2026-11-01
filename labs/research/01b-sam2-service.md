# Required SAM2-assisted annotation service

Complete after [polygon support](01-polygons.md). The first service setup must be done manually,
as described below; approved agent use elsewhere does not override this requirement.
This is mandatory. Plan an initial 16 hours for implementation, deployment and verification;
record actual time and blockers. The mentor supplies any original SAM2 handout internally.

## Product outcome

Add SAM2-assisted annotation to the labeling application. Agree with the mentor which prompt
interaction is required (for example points or a box), how a proposed mask becomes an editable
annotation, and how the user accepts, corrects or rejects it. Preserve manual labeling.
Use actual SAM2 inference with an approved local checkpoint; a mock response does not complete
the assignment. Bound this task to image annotation; video propagation is not an extra requirement.

## First service: hands-on ownership

For the trainee: set up this first SAM2 service yourself, by hand. Write and edit the Dockerfile
and Deployment/Service/Route configuration, run the image build and registry push, deploy the
service, inspect logs and diagnose the initial failures yourself. Do not delegate this work to
OMP, another coding agent or AI code completion, or ask AI to generate the setup files or command
sequence for you. OMP can remain installed for other assignments; keep it inactive for this work.

Documentation, approved organizational examples, conceptual ChatGPT questions within team data
policy and mentor guidance are allowed. Understand and adapt examples yourself. The point is
first-hand experience of bringing a service up, not a rigid quota of manually typed lines.
Agent assistance for other application work can resume outside this setup phase; the first
successful SAM2 deployment and its verification remain your own work.

For the mentor: state this boundary before the exercise. Explain concepts, point to documentation,
help with access and ask diagnostic questions, while leaving the setup edits, commands and
debugging to the trainee. Do not have an agent or another person deliver a ready-made deployment
for them. During review, ask the trainee to show how they built and brought up the service,
explain the files and request path, and make a small configuration change themselves.
Judge understanding and ownership with practical judgment; no mathematical authorship score
or extra formal reporting is required. Agent-assisted RabbitMQ/SAM3 work later does not replace
this first manual deployment.

## Build and deploy

The trainee implements the inference API and its application integration, writes a Dockerfile,
builds a versioned image, pushes it to the approved Artifactory registry and deploys it in the
teaching OpenShift namespace. Use the existing cluster and approved base image/dependency sources.

Create and explain the Deployment, Service and Route manifests. Configure the container port,
resource requests/limits, checkpoint mount, health/readiness checks and service selectors.
Pin the deployed image digest; keep credentials in approved secret references. The mentor supplies
namespace access, registry permissions, approved model/config revisions, checkpoint location and
a suitable device/memory allocation before work begins. No cluster administration is required.

Define the image/prompt and mask/coordinate contracts, including dimensions and resizing.
The application must call the deployed service through the approved Route or application-backend
path that exercises it; a notebook-only call or localhost-only demo is insufficient.
Handle unavailable inference visibly without losing existing annotations.

## Completion evidence

Submit a bounded MR with API/application changes, Dockerfile, deployment manifests and concise
build/push/deploy/verify instructions using internal placeholders in public documentation.

Demonstrate a fresh image and prompt in the application: request crosses the deployed Route,
SAM2 produces a mask, the user accepts or edits it, and the annotation survives save/reload.
Trace the response to the running image digest and model revision. Show the pod is Ready,
the Service has the intended endpoints and the Route reaches inference.
Restart only the teaching pod and repeat inference from the local checkpoint without downloads.
Check one invalid prompt and one unavailable-service case. Record observations and failures;
a Running pod or health 200 alone is not proof of the annotation flow.

The mentor reviews the deployment and asks the trainee to explain image versus container,
Deployment versus Service versus Route, and where model files and saved annotations persist.
Review fits existing product/review windows. If infrastructure/assets are unavailable, mark this
required assignment BLOCKED with an owner; do not silently turn it into an optional exercise.

See [environment handoff](../../docs/RESEARCH_ENVIRONMENT.md) and
[internal setup](../../docs/GETTING_STARTED_INTERNAL.md).
