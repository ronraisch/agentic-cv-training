# Curriculum and assessment

Read the assigned lab, its concept material, and selected upstream references. All labs require
an agent-session evidence sheet and a bounded PR. Maintain a decision log, not a transcript dump.
Lab order is dependency order; 06 can run alongside 02–05; 07–08 follow a first reviewed patch.

The detailed worksheets are in labs/. Each has outcomes, reading, constraints, deliverables,
acceptance evidence, mentor questions and a time estimate. These are active coding hours.

## Gates
- G0, labs 00–01: explain and run existing code; no code-generation-only pass.
- G1, labs 02–05: reproduce numerical/data/service/model failures and prevent regression.
- G2, labs 06–08: bound agent tasks, measure budget honestly, demonstrate skills and MCP calls.
- G3, labs 09–11: reject a bad patch, distribute a package and maintain a peer's change.

## Scoring (100)
Correctness and scientific validity 30; architecture/compatibility 20; evidence and testing 20;
agent/tool judgment 15; maintainability and handover 15. Pass: >=75 AND all gates met.
A reproducible wrong scientific result, inability to explain own changes, or bypassing a required
review/test gate requires remediation regardless of total. The mentor records concrete examples,
not impressions of how fluent the learner sounds.

## Individual defense, 20–30 minutes
Without an agent: trace one result to its source, predict a small array operation, explain a tool
boundary, diagnose one new failure with a debugger, and make a small justified edit. Documentation
is allowed. Then discuss one rejected agent suggestion and its consequences. This is not a speed
or memorization test. Retake after focused practice using a new input.

## Python remediation (before G0)
If lab 00 exposes gaps, spend 2–4 extra hours tracing mutable defaults, list versus iterator,
exception propagation, with-statements and imports. For NumPy, use shape/axis/views exercises;
for Pandas, reason about duplicate keys and nulls. Link a small worked example to each repaired gap.
Torch may be scheduled later for a non-ML role, but it is a required gate for ML researchers.
