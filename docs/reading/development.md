# 1 · Development

[Chapter index](index.md) · [Source coverage](sources.md)

This part of onboarding covers the software development work behind our computer vision projects. You'll learn to organize and debug Python code, follow data through a web application, and package and deploy a model as a service.

You'll start in your own OpenShift workspace, write a small program from scratch, then extend the team's labeling app and connect it to SAM2.

## Learning material

Allow 10–14 active hours for first-pass reading and 3–5 for viewing and reflection. Use the chapters alongside the exercises and bring questions to your mentor.

- [Linux, Git, containers and Python foundations](development-foundations.md) covers working directories, debugging, environments and how to split a program into modules.

- [NumPy, Pandas and data contracts](arrays-data.md) covers image axes, array shapes and types, views and copies, and table joins.

- [Types, decorators and concurrency](python-tools.md) covers type hints, function wrappers and how to choose between threads, processes and vectorized operations.

- [HTTP, SQL, services and application boundaries](development-interfaces.md) follows a request from the UI through an API to storage and explains what happens when a request fails or gets retried.

## Exercises

Start with [workspace setup](../../labs/research/00-installations.md). Connect VS Code to your OpenShift pod, configure Python and the debugger, and run the setup fixture.

- **Shape rendering in Python.** Read the provided XML, validate it, draw the described shapes and save an image. Keep parsing, validation and drawing separate. At review, run one valid input and one malformed input and explain how the program handles each. Complete this exercise by hand. [Shape-rendering instructions](../../labs/research/00-python-manual.md).

- **Polygons in the labeling app.** Add a way to draw, edit and save a polygon annotation. Show that the polygon reopens with the correct vertices, that the existing downstream consumer can use it and that rectangle annotations still work. [Polygon instructions](../../labs/research/01-polygons.md).

- **First SAM2 service.** Connect the labeling app to a deployed model that returns a mask for an image and prompt. Show that a user can accept or edit the result, save it and reopen it. Build the container, deploy to OpenShift and set up the first GitLab build, push and deploy pipeline by hand. [SAM2 instructions](../../labs/research/01b-sam2-service.md).

## Mentor reviews and agent use

At the Python review, walk through an unseen input and explain one design choice. After sign-off, return to workspace setup to configure OMP, the approved local model and the selected skills. When agent use is allowed, [ask it to explain a concept](../RESEARCH_WITH_AGENTS.md#when-you-get-stuck) and check the explanation with a fresh input or the actual code path.

At the service review, trace a request from the app to the deployed model, show the saved result after reopening and explain what the app shows if inference fails.

## Videos and original handouts

The earlier C++ videos are listed in the [original 2025 program outline](legacy-outline.md). For historical exercises and background, see the [advanced Python handout](legacy-python.md), [original shape-rendering exercise](legacy-shape-rendering.md) and [Boids exercise](legacy-boids.md).
