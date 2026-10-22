# Lab 10 — Ship to another research team

Estimated active work: 4 hours. Use the approved agent except for the mentor check.

## Read and understand
ENGINEERING.md section 6; package build docs. Explain relevant concepts from docs/ENGINEERING.md in your own words.

## Assignment
Build a wheel and install it into a fresh environment outside the checkout. Invoke the public pipeline with caller-provided DataFrames and run a tiny downstream script against report keys. Decide whether CLI fixtures are packaged or must be supplied explicitly; document and test the decision. Write release notes, dependency policy, compatibility policy, reproducibility manifest and rollback instructions. Have a peer follow the instructions.

## Constraints
Work from the inherited implementation and preserve unrelated behavior. Use only synthetic data.
Submit one reviewable change; avoid changing tests merely to agree with the current code.
Do not consult instructor/ in learner mode.

## Deliverables
Wheel/install transcript; downstream consumer; release notes; peer feedback and one follow-up improvement.
Include templates/agent-session.md, commands and observed outputs in sanitized artifacts.

## Acceptance evidence
Imports work away from the repo. No hidden source-path or fixture dependency. Public schema remains compatible or has an explicit migration/version decision.
Mentor checks a new input not shown in your submitted examples. Explain limitations explicitly.

## Individual mentor check
What belongs in a lockfile versus package metadata? How will a user reproduce an old result?

## If blocked
Write the smallest failing input, your current hypothesis and one experiment that could disprove it.
After mentor feedback, retry on a fresh example and record what changed in your understanding.
