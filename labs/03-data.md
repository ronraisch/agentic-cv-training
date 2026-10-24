# Lab 03 — Prevent plausible but wrong results

Estimated active work: 4 hours. Use the approved agent except for the mentor check.

## Read and understand
[ENGINEERING.md](../docs/ENGINEERING.md) section 3; Pandas merge validation documentation. Explain relevant concepts from [docs/ENGINEERING.md](../docs/ENGINEERING.md) in your own words.

## Assignment
Add duplicate feature IDs and a missing sample ID to a temporary fixture. Explain cardinality before running the join. Require unique sample/feature IDs, reject missing features explicitly, and preserve report keys. Replace alternating-row split with a deterministic group split by scene. Add a manifest proposal containing data/preprocessing revisions, seed and split hash.

## Constraints
Work from the inherited implementation and preserve unrelated behavior. Use only synthetic data.
Submit one reviewable change; avoid changing tests merely to agree with the current code.
Do not consult instructor/ in learner mode.

## Deliverables
Data-contract tests; leakage reproducer; deterministic split test; provenance manifest example.
Include [templates/agent-session.md](../templates/agent-session.md), commands and observed outputs in sanitized artifacts.

## Acceptance evidence
Duplicate/missing IDs fail loudly. Train and test scene sets are disjoint; their union preserves all samples. Repeated runs produce the same split. A downstream consumer still reads the report.
Mentor checks a new input not shown in your submitted examples. Explain limitations explicitly.

## Individual mentor check
Can a reproducible split still leak data? Which preprocessing state must only be fitted on train?

## If blocked
Write the smallest failing input, your current hypothesis and one experiment that could disprove it.
After mentor feedback, retry on a fresh example and record what changed in your understanding.
