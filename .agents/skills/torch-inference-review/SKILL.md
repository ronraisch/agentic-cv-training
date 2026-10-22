---
name: torch-inference-review
description: Review PyTorch research inference changes. Use when editing model execution, batching, device movement, dropout, or embedding retention.
---

Read the model and caller contracts. Trace tensor shape/dtype/device, model mode and graph retention. Use the existing inference boundary instead of duplicating wrappers. Load references/checks.md for targeted cases. Ask for tests that distinguish eval behavior from autograd behavior, and measure rather than assert performance. Report evidence and uncertainty. Do not download models or allocate GPU for this course.
