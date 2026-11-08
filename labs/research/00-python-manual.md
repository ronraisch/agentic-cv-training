# Manual Python capstone — legacy shapes/parser exercise

Complete this at the start of onboarding, after basic environment setup and before OMP.
Allow approximately three working days (24 hours including review), rather than three short sessions.

## Source and scope

Use the [preserved original Shape Rendering assignment](../../docs/reading/legacy-shape-rendering.html),
converted from the archived original Word handout. Its text and included figures are local;
it specifies the parser, shapes and expected drawings. The old live-document URL could not be
read during migration, so this is the supplied archive copy rather than a claim about an unseen
later revision. Open it before starting and obtain any separate input fixtures from the mentor.
Do not invent a replacement grammar or confuse it with [the later labeling request](01-polygons.md).

The purpose is a shared minimum standard for readable, modular Python and independent coding.
Follow the original exercise requirements; review how parsing, geometry/data representation and
drawing responsibilities are separated, how interfaces are named and how errors are handled.
Prefer clear, small units over unnecessary abstractions.

## Environment and assistance

- Work in your own OpenShift pod through VS Code, with approved Python/uv, Artifactory access,
  dependencies, interpreter and debugger ready. Follow [internal setup](../../docs/GETTING_STARTED_INTERNAL.md).
- Do not install, update or configure OMP until the exercise is completed and reviewed.
  If an agent is already present in the environment, keep it inactive.
- Write, debug and refactor the code yourself. No coding agents or AI code completion.
- Occasional ChatGPT questions about concepts are allowed only within team data policy.
  Do not ask it to write the solution, functions, tests or replacement code, or paste generated
  code into the submission. Documentation and mentor clarification remain available.

## Completion and review

Submit the original exercise's required code and outputs with a short run instruction.
Demonstrate representative valid input and malformed input using the original specification.
Walk the mentor through the module boundaries and a concrete design choice; make a small change
yourself to demonstrate that you understand the code. Review modularity, readability and correctness
together, then make the agreed corrections manually. No model-training or agent-use report is required.

After mentor review, return to [stage 0](00-installations.md) for OMP/local-LLM setup and skills.
