# Lab 07 — Use and evaluate reusable team knowledge

Estimated active work: 4 hours. Use the approved agent except for the mentor check.

## Read and understand
[TEAM_INTEGRATION.md](../docs/TEAM_INTEGRATION.md); .agents/skills; Agent Skills specification. Explain relevant concepts from [docs/ENGINEERING.md](../docs/ENGINEERING.md) in your own words.

## Assignment
Complete the selected deeper practice from [stage 0](../docs/SKILLS_STAGE0.md): use the spec/ticket/implementation/review flow on one bounded existing task and finish with an evidence-based retro. Use ask-matt to justify the flow; do not execute every catalog entry. Wayfinder can use a small decision-map example rather than a large implementation. This replaces part of the existing four-hour exercise, not extra time.

Use research-data-review on a real connector/data diff and torch-inference-review on the optional Torch patch. Record actual activation evidence. Select at least two real team skills from the inventory and demonstrate success, failure and fallback for each. Improve one example skill from an observed failure: keep the trigger precise, core short and detailed checks in references. Evaluate original and revised versions on the same task plus an unrelated negative case.

## Constraints
Work from the inherited implementation and preserve unrelated behavior. Use only synthetic data.
Submit one reviewable change; avoid changing tests merely to agree with the current code.
Do not consult instructor/ in learner mode.

## Deliverables
Skill-use traces; one justified skill edit; before/after evaluation; negative-trigger case; internal-tool teach-back.
Include [templates/agent-session.md](../templates/agent-session.md), commands and observed outputs in sanitized artifacts.

## Acceptance evidence
Skill metadata validates. The changed skill improves the target case without activating on unrelated work. Real team tools are demonstrated or gate explicitly BLOCKED with owner.
Mentor checks a new input not shown in your submitted examples. Explain limitations explicitly.

## Individual mentor check
How does a skill differ from [AGENTS.md](../AGENTS.md), an MCP tool and a test? How do you know it was actually loaded?

## If blocked
Write the smallest failing input, your current hypothesis and one experiment that could disprove it.
After mentor feedback, retry on a fresh example and record what changed in your understanding.
