# Lab 06 — Control context and verify delegation

Estimated active work: 3 hours. Use the approved agent except for the mentor check.

## Read and understand
[AGENT_WORK.md](../docs/AGENT_WORK.md); [templates/task-contract.md](../templates/task-contract.md). Explain relevant concepts from [docs/ENGINEERING.md](../docs/ENGINEERING.md) in your own words.

## Assignment
Choose an unresolved bounded defect. Write acceptance examples before prompting. Run broad-context and selected-context sessions from the same starting commit using the same model/harness. Preserve first attempts, inspect actual changes, and reject at least one unnecessary abstraction or unsupported claim. Compare correctness before token/time metrics. Record unavailable token counters as unavailable.

## Constraints
Work from the inherited implementation and preserve unrelated behavior. Use only synthetic data.
Submit one reviewable change; avoid changing tests merely to agree with the current code.
Do not consult instructor/ in learner mode.

## Deliverables
Two sanitized session records; small task spec; diff review; measured comparison with limitations.
Include [templates/agent-session.md](../templates/agent-session.md), commands and observed outputs in sanitized artifacts.

## Acceptance evidence
Accepted code passes independent checks. Context selection is justified with paths. No unmeasured throughput or causal claims. A peer can resume from the handoff.
Mentor checks a new input not shown in your submitted examples. Explain limitations explicitly.

## Individual mentor check
Which constraint should become a test instead of a longer prompt? What makes a local-model task too large?

## If blocked
Write the smallest failing input, your current hypothesis and one experiment that could disprove it.
After mentor feedback, retry on a fresh example and record what changed in your understanding.
