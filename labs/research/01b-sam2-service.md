# Add SAM2-assisted annotation and deploy your first service

## Goal

A user can request a SAM2 mask in the labeling application, accept or edit it, and save the
annotation. The application calls your deployed service using a real approved local checkpoint.
Manual labeling continues to work.

Complete this after [polygon support](01-polygons.md). It is required, with an initial 16-hour
allocation covering implementation, deployment, the first CI/CD pipeline and verification.
Record actual work and blockers. The mentor supplies any original internal SAM2 handout.

## Before you start

Agree with the mentor on the prompt interaction—such as points or a box—and how a mask becomes
an editable annotation. Include accepting, correcting and rejecting a suggestion. This task covers
image annotation; video propagation is not an additional requirement.

The mentor supplies teaching-namespace and registry access, approved model/config revisions,
checkpoint location, suitable device/memory and existing runner/build access. Use approved base
images, dependencies and shared model assets. Cluster administration, runner provisioning and
privileged Docker setup are not trainee requirements.

## First service: hands-on ownership

Build and bring up this first service yourself. Write the Dockerfile and Deployment/Service/Route
configuration; run the build, push and deployment; inspect logs and diagnose failures. Keep OMP,
other coding agents and AI completion inactive for this setup. Do not ask them to generate the
setup files or command sequence, or to deliver the deployment for you.

Documentation, approved organizational examples, mentor guidance and ChatGPT explanations or
small illustrative examples are allowed within team data policy. Read and adapt them yourself.
The goal is first-hand understanding, not a quota of manually typed lines. Agent assistance may
resume for application work outside this setup phase; the first successful deployment and its
verification remain your own work. The later agent-assisted SAM3 exercise does not replace this.

The mentor helps with access and concepts and asks diagnostic questions. At review, be ready to
explain your files and request path and make a small configuration change yourself. No additional
formal authorship report is needed.

## 1. Define the API and application flow

Define the image/prompt and mask/coordinate contracts, including dimensions and resizing.
Implement actual SAM2 inference and connect it to the agreed annotation interaction.
Handle unavailable inference visibly while preserving existing annotations.

The application request must cross the deployed Route or approved backend path to the service.
A mock, a notebook-only call or a localhost-only demonstration does not complete this flow.

## 2. Build and deploy

Build a versioned image, push it to the approved Artifactory registry and deploy it to the
teaching OpenShift namespace. Create and explain the Deployment, Service and Route manifests.
Configure ports, selectors, resource requests/limits, checkpoint mount and health/readiness checks.
Pin the running image digest and use approved secret references for credentials.

Check what each layer establishes: a Running pod, a Ready pod, a Service with endpoints and a
Route reaching inference are different observations. The full application flow is the final check.

## 3. Add the first GitLab pipeline by hand

After the manual deployment, write a minimal CI/CD configuration and any short shell script
yourself. One build/push job and one deploy job are enough; deployment may be manually triggered.
Deploy the same image revision that the pipeline built and pushed.

Use the existing runner/build mechanism and approved CI secret variables. Understand jobs/stages,
the runner environment, variables, registry authentication, image tags/digests and image selection.
ChatGPT can explain syntax and small examples; assemble, run and diagnose the pipeline yourself.

Run it on a learning commit and trace commit → pushed image → running workload. Make a small
change and show its effect. For a failed job, locate and diagnose the failing command before
asking a model to fix it. This stays within the service allocation and existing review window.

## Submit and demonstrate

Submit a bounded MR containing the API/application change, Dockerfile, manifests and concise
build/push/deploy/verify instructions. Use internal placeholders in public documentation.

Demonstrate:

- A fresh image/prompt reaches deployed SAM2; the accepted or edited mask survives save/reload.
- The response traces to the running image digest and model revision; the pod is Ready,
  Service endpoints are correct and the Route reaches inference.
- Restarting only the teaching pod still allows inference from the local checkpoint, without downloads.
- An invalid prompt and an unavailable service produce the intended visible behaviour.

Explain image versus container, Deployment versus Service versus Route, and where checkpoints
and annotations persist. Record failures and unverified claims. If an asset or permission is missing,
mark the required exercise BLOCKED with an owner; it remains required.

[Environment handoff](../../docs/RESEARCH_ENVIRONMENT.md) ·
[Internal setup](../../docs/GETTING_STARTED_INTERNAL.md)
