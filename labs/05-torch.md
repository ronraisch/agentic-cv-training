# Lab 05 — Make inference explicit and bounded

Estimated active work: 4 hours. Use the approved agent except for the mentor check.

## Read and understand
ENGINEERING.md section 4; installed PyTorch eval/inference_mode docs. Explain relevant concepts from docs/ENGINEERING.md in your own words.

## Assignment
Install CPU Torch. Run repeated embeddings from the same model and batch; inspect requires_grad and model.training. Define an inference contract: finite floating [N,4], empty [0,4] accepted, CPU outputs without graph, input unchanged, caller mode restored. Repair embed; test exception-path restoration too. Compare several batch sizes for numerical agreement. Document peak-memory measurement limits rather than inventing a measurement.

## Constraints
Work from the inherited implementation and preserve unrelated behavior. Use only synthetic data.
Submit one reviewable change; avoid changing tests merely to agree with the current code.
Do not consult instructor/ in learner mode.

## Deliverables
Regression tests for dropout/mode/gradients, batch shape and nonfinite inputs; batch-size comparison; reproducibility manifest.
Include templates/agent-session.md, commands and observed outputs in sanitized artifacts.

## Acceptance evidence
Repeated inference is stable within stated tolerance; no graph retained; outputs on CPU; empty input supported; caller training mode restored after success and failure.
Mentor checks a new input not shown in your submitted examples. Explain limitations explicitly.

## Individual mentor check
Why are eval and inference_mode both needed? Why does a seed not prove cross-device determinism?

## If blocked
Write the smallest failing input, your current hypothesis and one experiment that could disprove it.
After mentor feedback, retry on a fresh example and record what changed in your understanding.
