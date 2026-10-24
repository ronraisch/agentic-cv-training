# Lab 04 — Extend sources without duplicating infrastructure

Estimated active work: 5 hours. Use the approved agent except for the mentor check.

## Read and understand
[ENGINEERING.md](../docs/ENGINEERING.md) sections 1 and 3; [sources.py](../src/researchlab/sources.py) and [http.py](../src/researchlab/http.py). Explain relevant concepts from [docs/ENGINEERING.md](../docs/ENGINEERING.md) in your own words.

## Assignment
Generate SQLite data with [tools/generate_data.py](../tools/generate_data.py). Add a common source interface only as needed by the consumer. Repair HTTP pagination using next_cursor. Use MockTransport to simulate two pages, empty pages, malformed schemas, repeated cursors, 401, 429, 503 and timeout. Add a bounded-concurrency bulk retrieval function with explicit partial-failure semantics and stable identity/order; test the bound with an active-call counter. All HTTP goes through HTTPClient; do not stack retry decorators.

## Constraints
Work from the inherited implementation and preserve unrelated behavior. Use only synthetic data.
Submit one reviewable change; avoid changing tests merely to agree with the current code.
Do not consult instructor/ in learner mode.

## Deliverables
CSV/SQLite/HTTP contract tests; request-count assertions; concurrency evidence; schema ownership ADR.
Include [templates/agent-session.md](../templates/agent-session.md), commands and observed outputs in sanitized artifacts.

## Acceptance evidence
Both pages returned once; cursor cycles rejected; no retry on 401; transient retries bounded; transport errors are not empty datasets; SQL parameters remain bound; concurrency bound verified.
Mentor checks a new input not shown in your submitted examples. Explain limitations explicitly.

## Individual mentor check
What happens if the server completed a write before a timeout? How would you support Retry-After without sleeping in tests?

## If blocked
Write the smallest failing input, your current hypothesis and one experiment that could disprove it.
After mentor feedback, retry on a fresh example and record what changed in your understanding.
