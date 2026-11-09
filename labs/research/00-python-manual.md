# Build the original shape renderer by hand

## Start here

Use the assigned Python workspace in your pod. Open the inline XML from the [handout](../../docs/reading/legacy-shape-rendering.md) and ask the mentor for any separate panda fixtures. Save and reopen one render as your first check. Bring one valid and one malformed input to review. Python approval releases OMP setup. See the [worked example](../../docs/WORKED_EXAMPLES.md#python-modularity) before starting.

## Goal and starting point

Build the parser and renderer specified in [the original Shape Rendering handout](../../docs/reading/legacy-shape-rendering.md).
The point is to practise readable, modular Python and understand the code you write.
Allow about three working days: 24 hours including review.

Start after basic environment setup and before OMP installation/configuration. The local handout
contains the archived original text and figures; its old live-document URL was unavailable during
migration. Obtain any separate input fixtures from the mentor. Follow its grammar, shapes and
expected drawings, including the panda examples, rather than inventing a replacement specification.
This is separate from [the later labeling application request](01-polygons.md).

## How to work

Work in your own pod through VS Code with Python/uv, Artifactory, interpreter and debugger ready.
Use [the internal setup guide](../../docs/GETTING_STARTED_INTERNAL.md) if needed.

Write, debug and refactor the code yourself. Keep coding agents and AI completion inactive;
do not install, update or configure OMP until review is complete. Documentation and mentor
clarification are available. Occasional ChatGPT questions about concepts are allowed within team
data policy, but not requests for solution code, functions, tests or a generated replacement to paste.

As you implement, keep parsing, validation, geometry/data representation and drawing responsibilities
clear. Prefer small, well-named units with explicit interfaces and useful errors. There is no need
to introduce abstractions that do not help the exercise.

## Submit and demonstrate

Use this lab's submission instructions. The legacy design review and per-stage branches/MRs are historical. In the pod, write the drawing to an image file and preview it in VS Code or Jupyter. Record the command and path so the mentor can reopen it.

Submit the required code and drawings with a short run instruction. At review:

- Run representative valid input and malformed input from the original specification.
- Trace one input through the modules and explain one design choice.
- Make a small change yourself, then address the agreed review corrections manually.

Review covers modularity, readability and correctness. No model-training or agent-use report is
required. After approval, return to [workspace setup](00-installations.md) for OMP and skills.
