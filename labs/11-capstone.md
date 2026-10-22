# Lab 11 — Own and hand over a research feature

Estimated active work: 6 hours. Use the approved agent except for the mentor check.

## Read and understand
All local concept guides; mentor-assigned held-out scenario. Explain relevant concepts from docs/ENGINEERING.md in your own words.

## Assignment
Add a second synthetic provider with paginated metadata and embedding batches. Integrate it through existing boundaries, retain provenance, and expose a bounded MCP metadata tool. Use the appropriate skills and a task contract. Mentor reveals a late change: renamed provider field, repeated cursor, scene leakage or model failure. A peer inherits your branch and completes that change. Finish with the individual defense.

## Constraints
Work from the inherited implementation and preserve unrelated behavior. Use only synthetic data.
Submit one reviewable change; avoid changing tests merely to agree with the current code.
Do not consult instructor/ in learner mode.

## Deliverables
Reviewed feature PR; acceptance tests; manifest; skill/MCP evidence; late-change patch by peer; defense notes.
Include templates/agent-session.md, commands and observed outputs in sanitized artifacts.

## Acceptance evidence
End-to-end scenario survives late change; numerical/data invariants hold; no duplicate retry stack or unbounded tensor retention; peer can work without oral context; all gates pass.
Mentor checks a new input not shown in your submitted examples. Explain limitations explicitly.

## Individual mentor check
Trace one report row to provider data. Diagnose a new small failure without AI. Explain one design you intentionally kept simple.

## If blocked
Write the smallest failing input, your current hypothesis and one experiment that could disprove it.
After mentor feedback, retry on a fresh example and record what changed in your understanding.
