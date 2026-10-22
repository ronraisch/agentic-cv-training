# Lab 02 — Repair scientific array contracts

Estimated active work: 4 hours. Use the approved agent except for the mentor check.

## Read and understand
ENGINEERING.md sections 2 and 5; installed NumPy documentation. Explain relevant concepts from docs/ENGINEERING.md in your own words.

## Assignment
Investigate normalize and rank using zero vectors, a view into a larger array, integers, empty batches, NaN/Inf, ties and invalid k/query shapes. Implement the documented numerical contract. Compare vectorized ranking to an independent small cosine oracle. Show a failing test BEFORE the fix. Avoid silently filtering invalid rows because that changes identity alignment.

## Constraints
Work from the inherited implementation and preserve unrelated behavior. Use only synthetic data.
Submit one reviewable change; avoid changing tests merely to agree with the current code.
Do not consult instructor/ in learner mode.

## Deliverables
Parameterized regression tests; before/after output; memory/mutation notes; bounded implementation diff.
Include templates/agent-session.md, commands and observed outputs in sanitized artifacts.

## Acceptance evidence
Input is unchanged; zero rows remain finite; invalid inputs raise ValueError; ties retain input order; k=0 works; outputs agree with an independent oracle.
Mentor checks a new input not shown in your submitted examples. Explain limitations explicitly.

## Individual mentor check
Why is nan_to_num at the end insufficient? When would a copy be worth its memory cost?

## If blocked
Write the smallest failing input, your current hypothesis and one experiment that could disprove it.
After mentor feedback, retry on a fresh example and record what changed in your understanding.
