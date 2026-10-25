# Lab 09 — Reject a green but wrong patch

For the six-week research route, follow only the
[embedded practice selection](../docs/SKILLS_STAGE0.md#required-practice-inside-existing-assignments).
The standalone estimate and full deliverable list below are optional worksheet material.

Estimated active work: 3 hours. Use the approved agent except for the mentor check.

## Read and understand
[reviews/bad_patch.diff](../reviews/bad_patch.diff); [ENGINEERING.md](../docs/ENGINEERING.md) sections 5 and 7. Explain relevant concepts from [docs/ENGINEERING.md](../docs/ENGINEERING.md) in your own words.

## Assignment
Review the supplied patch without applying it. Rank findings by concrete consequences and propose minimal counterexamples. Then apply it in a disposable worktree and demonstrate why green smoke tests do not establish correctness. For two earlier fixes, temporarily restore the original defective behavior and verify the new tests fail. Restore clean state before commit.

## Constraints
Work from the inherited implementation and preserve unrelated behavior. Use only synthetic data.
Submit one reviewable change; avoid changing tests merely to agree with the current code.
Do not consult instructor/ in learner mode.

## Deliverables
Review with file/function references; two defect-restoration results; corrected tests; clean diff.
Include [templates/agent-session.md](../templates/agent-session.md), commands and observed outputs in sanitized artifacts.

## Acceptance evidence
Identify silent missing-data behavior and identity corruption. Test failures correspond to the intended defect, not unrelated import/environment failures.
Mentor checks a new input not shown in your submitted examples. Explain limitations explicitly.

## Individual mentor check
What evidence would make you approve? Why might a high coverage number coexist with these failures?

## If blocked
Write the smallest failing input, your current hypothesis and one experiment that could disprove it.
After mentor feedback, retry on a fresh example and record what changed in your understanding.
