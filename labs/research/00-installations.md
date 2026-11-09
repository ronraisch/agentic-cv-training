# Set up your research workspace

## Start here

Use your workstation for VS Code and its attached pod terminal for Python. The mentor supplies your namespace, Artifactory path and a small Python fixture. Run it in the pod and hit a breakpoint. Review the [setup order](../../docs/GETTING_STARTED_INTERNAL.md). Confirm Python readiness now and return for OMP only after manual Python approval.

## Goal

Run and debug Python in your own OpenShift pod, then prepare the approved agent workflow.
Do this with the mentor using [the internal setup guide](../../docs/GETTING_STARTED_INTERNAL.md).
This is guided setup, not a DevOps exam.

## First: prepare Python and complete the manual exercise

1. Obtain access to VS Code, OpenShift, GitLab, Artifactory, Confluence and Jupyter.
2. Install VS Code and connect it to your own development pod.
3. Prepare Python/uv through Artifactory. Select the pod's interpreter and check the debugger.
4. Complete [the manual Python capstone](00-python-manual.md), allowing about three working days.

Keep coding agents and AI code completion inactive during this phase. Install, update or configure
OMP only after the mentor has reviewed the capstone.

## Then: prepare OMP and skills

Follow [the OMP readiness checks](../../docs/GETTING_STARTED_INTERNAL.md#omp-and-the-local-llm)
with the approved local model service, currently QWEN 3.8. Check a real model request, workspace
tool use and reconnection before activating skills.

Complete [the Matt Pocock skill lab](../../docs/SKILLS_STAGE0.md): install the approved bundle,
skim the catalog descriptions and do the selected deeper practice. Show a successful activation
and an example that should not trigger a skill. Installing a Python package does not install a
skill. The 30-minute teach-back stays inside the existing week-one allocation.

## Show that the workspace is ready

Demonstrate the selected interpreter, a notebook restart, an internal fixture request, an accessible
Confluence page and a safe GitLab job log. For each readiness check, record expected versus actual
output and what the evidence establishes. If access is missing, record the blocker and its owner.

Use the existing stack; rebuilding it or fetching public packages from the closed network is not
part of this exercise.

[Setup data and fixtures](../../docs/DATASETS.md#setup-and-skills) ·
[How to acquire an approved subset](../../docs/DATASETS.md#acquire-a-working-subset)
