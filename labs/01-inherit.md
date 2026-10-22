# Lab 01 — Understand before changing

Estimated active work: 3 hours. Use the approved agent except for the mentor check.

## Read and understand
ENGINEERING.md sections 1 and 7; AGENT_WORK.md. Explain relevant concepts from docs/ENGINEERING.md in your own words.

## Assignment
Ask an agent for an architecture map, then verify every edge with file/function references and a debugger trace. Identify the public report contract and the existing HTTP transport. Record five risks as hypotheses with reproduction ideas. Write an ADR comparing a function-based source interface with a class hierarchy; choose based on current consumers.

## Constraints
Work from the inherited implementation and preserve unrelated behavior. Use only synthetic data.
Submit one reviewable change; avoid changing tests merely to agree with the current code.
Do not consult instructor/ in learner mode.

## Deliverables
Verified component map; end-to-end trace; risk register; ADR; minimal task contract for the first repair.
Include templates/agent-session.md, commands and observed outputs in sanitized artifacts.

## Acceptance evidence
No speculative rewrite. Each claimed dependency exists. A peer can find the extension point and explain which module should own retries.
Mentor checks a new input not shown in your submitted examples. Explain limitations explicitly.

## Individual mentor check
Which agent claim was wrong? Which abstraction would you decline to add today, and why?

## If blocked
Write the smallest failing input, your current hypothesis and one experiment that could disprove it.
After mentor feedback, retry on a fresh example and record what changed in your understanding.
