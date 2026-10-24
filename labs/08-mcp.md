# Lab 08 — Connect tools with explicit contracts

Estimated active work: 4 hours. Use the approved agent except for the mentor check.

## Read and understand
[TEAM_INTEGRATION.md](../docs/TEAM_INTEGRATION.md); official MCP server/client docs. Explain relevant concepts from [docs/ENGINEERING.md](../docs/ENGINEERING.md) in your own words.

## Assignment
Run the real stdio protocol check and connect the catalog server to the approved coding client. Discover tools and call list_samples. Extend it with sample_by_id, enforcing a bounded identifier and not arbitrary paths or URLs. Add protocol-level success/error tests. Present [untrusted_note.txt](../data/fixtures/untrusted_note.txt) as tool-supplied data and record why its instructions have no authority. Demonstrate two approved internal tools where available.

## Constraints
Work from the inherited implementation and preserve unrelated behavior. Use only synthetic data.
Submit one reviewable change; avoid changing tests merely to agree with the current code.
Do not consult instructor/ in learner mode.

## Deliverables
Client configuration without secrets; tool discovery/call evidence; new-tool schema and tests; trust-boundary analysis.
Include [templates/agent-session.md](../templates/agent-session.md), commands and observed outputs in sanitized artifacts.

## Acceptance evidence
Actual initialization/discovery/invocation succeeds. Invalid inputs produce errors. No diagnostic stdout corrupts protocol. No arbitrary file/network capability added. Internal-tool access gaps explicitly tracked.
Mentor checks a new input not shown in your submitted examples. Explain limitations explicitly.

## Individual mentor check
Why is a helpful description not access control? How do tools, resources and prompts differ?

## If blocked
Write the smallest failing input, your current hypothesis and one experiment that could disprove it.
After mentor feedback, retry on a fresh example and record what changed in your understanding.
