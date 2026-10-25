# Original ResearchLab mentor bank

The active mentor route is [RESEARCH_GUIDE.md](RESEARCH_GUIDE.md) with [DEEP_DISCUSSIONS.md](DEEP_DISCUSSIONS.md). The original exercises
below are an optional bank, not another mandatory course or a current time budget.

# Mentor guide — contains spoilers

Before teaching: run all commands in README, create a learner-only export, populate the actual
team tool inventory, and reserve one reviewer per 2–3 learners. Use a private learner repository
if internal tools or sanitized-but-sensitive details are added. This synthetic source can be shared.
Do not copy internal credentials, data or tool descriptions into a public upstream repository.

## Intentional defects and teaching intent
| Component | Defect | Consequence | Required evidence |
|---|---|---|---|
| normalize | In-place division, zero norm, unchecked dtype/rank/nonfinite | Corrupted parent view or invalid features | Input unchanged; zero and invalid cases |
| rank | Unvalidated query/k, unstable ties | Wrong or irreproducible selection | Independent cosine oracle, tie and shape tests |
| retrieve | Unchecked inner join/cardinality | Silent omission or duplicated samples | Duplicate and missing-key counterexamples |
| split_samples | Alternating rows | Same scene on both sides | Disjoint scene sets and preservation |
| from_http | Reads first page only | Incomplete catalog appears valid | Two-page integration test and cycle rejection |
| embed | Training dropout + autograd + output retention | Unstable results, unnecessary graph memory | Eval/inference, CPU/no-grad, exception restoration |
| review patch | Positional join and blanket except | Identity corruption and hidden outages | Reordered rows, 401/timeout counterexamples |

Reference functions are in [reference.py](reference.py). They illustrate core numerical/join/pagination/Torch
contracts, not a completed answer to concurrency, packaging, skills, MCP extension or capstone.
Those are assessed by the worksheet acceptance evidence and peer review. Do not misrepresent
partial reference coverage as a complete solution branch. A learner solution may be simpler/better.

## Commands
```bash
uv run pytest                            # starter smoke and infrastructure, should pass
uv run pytest instructor/test_contracts.py  # deliberately fails on starter
COURSE_IMPL=reference uv run pytest instructor/test_contracts.py
COURSE_IMPL=reference uv run --extra torch pytest instructor/test_torch_contract.py
```
CI intentionally runs reference Torch contract checks (not starter defect checks); learners must
add regression tests for each repair. The starter tests are not a grading oracle.

## Held-out checks (keep out of learner exports)
- Lab 02: pass a view of a parent matrix, extreme finite floats and a zero-row empty matrix.
- Lab 03: reorder feature rows; duplicate one feature; introduce one missing ID; check scene split.
- Lab 04: cycle cursor after a valid page; permanent 401; transient then success; reordered completion.
- Lab 05: exception after one good batch; caller already in eval; empty list; integer/nonfinite tensor.
- Lab 07: unrelated task should not load the skill; tool missing should trigger documented fallback.
- Lab 08: invalid limit/split, unknown sample, protocol error handling and no arbitrary path access.
- Lab 10: build/install outside checkout; new downstream caller that only knows the documented API.

Use 0–4 on each rubric category: 0 absent; 1 demo only; 2 happy-path verified; 3 edge cases and
tradeoffs explained; 4 independent evidence and successful peer maintenance. These are diagnostic
descriptions, not a weighted course grade. The current [syllabus](../docs/CURRICULUM.md#completion-and-fallback)
uses separate concept and implementation gates; it defines no score weights. Record remediation
per gate, with a new example on retake.

Do not award points for number of design patterns or lines generated. A learner may say the
current shared client needs a documented limitation (Retry-After support, total deadline) rather
than designing a generic networking framework. Reward that judgment when justified.

## Schedule

The six-week researcher route in [docs/CURRICULUM.md](../docs/CURRICULUM.md) supersedes the original ten-day schedule.
Use [instructor/RESEARCH_GUIDE.md](RESEARCH_GUIDE.md) for the current 12-hour mentor budget and deep sessions.
Only the [selected outcomes](../docs/SKILLS_STAGE0.md#required-practice-inside-existing-assignments)
are embedded in the research route. Remaining standalone labs 00–11 are an optional bank,
not an additional 46-hour course. Internal setup is guided teaching.
