# Validation scope

A release must exercise the working baseline from approved local inputs through persisted
annotations, model fitting, saved-artifact reload and inference. Run:

```bash
uv run --no-sync pytest
uv run --no-sync ruff check .
uv run --no-sync researchlab-demo smoke --root artifacts/baseline-check
uv run --no-sync python tools/preflight.py --scope starter
```

The CPU fixture is procedural, not evidence of research accuracy on real camera data or internal
deployment. Internal code/data/model/platform owners must execute their own representative checks
in the trainee's pod. Preflight reports supplied records separately from executed local checks.
Do not infer internal readiness from local success or a file-presence check.

Export only reviewed committed source. Validate installation, local links, model reload and the
baseline in a fresh learner copy without source history or earlier artifacts. Private assessment
material is not a public validation suite. Historical records are maintained separately.
