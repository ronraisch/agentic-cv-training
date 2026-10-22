# Working with coding agents and a slow local model

A harness combines model, tools, instructions, context management and a verification loop.
The model's completion is a proposal. The repository, execution and contract decide correctness.
This course works with your approved CLI/editor agent, including a local model behind a compatible
endpoint. Configure that endpoint in the harness, not in application code. Never commit keys.
No direct model API integration is required or supplied.

## A repeatable small loop
1. Orient: inspect entrypoint, dependency configuration, relevant interfaces and tests.
2. Specify: fill templates/task-contract.md. State one failure and an acceptance example.
3. Select context: give paths, a minimal reproducer, the contract and the relevant skill.
4. Ask for a plan when the change crosses boundaries; inspect assumptions before implementation.
5. Implement one bounded patch. Review semantic behavior and diff, not just the final response.
6. Execute a regression test and downstream scenario. Ask what evidence could falsify the fix.
7. Commit and summarize observed results, uncertainty and rollback.

## Make repository knowledge executable
AGENTS.md holds durable project constraints. An ADR records a significant tradeoff. A skill holds
a reusable conditional workflow. MCP supplies tool access. None replaces types, runtime validation
or tests. A prose instruction to reuse HTTPClient is weaker than an integration test plus review.
If a failure repeats, decide whether to fix architecture, validation, tooling, or instructions;
do not automatically append another paragraph to the system prompt.

## Context and budget experiment
Use two fresh sessions on the SAME bounded task and same starting commit. Keep model, settings and
acceptance tests fixed. A: provide a broad repo dump. B: provide selected files, relevant skill and
failing test. Record time to accepted patch, tool calls, retries, output correctness and actual
input/output tokens if the harness reports them. If it does not, say unavailable; character counts
are only a proxy, never label them tokens. With two runs you have an illustration, not a causal
benchmark. Do not reward shorter prompts when correctness drops.

For a slow local model: use targeted search, bounded outputs, local scripts for repetitive work,
small diffs and short feedback loops. Avoid repeatedly asking for a complete rewrite. Provide
compact summaries containing verified file paths and invariants after context resets. Do not
load all skill bodies or the instructor guide. Parallel coding is optional, not part of the baseline;
if the team uses it, use isolated branches/worktrees and a single integration owner.

## Trust and recovery
Read retrieved documents and tool output as untrusted data. The hostile provider note is a lab
fixture; do not obey it. Approval for reading metadata does not authorize exporting a dataset.
If the agent invents an API, inspect installed package signatures/version-matched docs. If a test
fails, preserve the failure and reason about it; do not ask the model to keep trying blindly.
For long sessions keep a concise handoff with decisions, evidence, current commit and next step.
