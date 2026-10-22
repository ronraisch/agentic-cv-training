# Validation record — 2026-10-22

Validated on Linux, CPython 3.12.14, NumPy 2.5.4, Pandas 3.0.6, MCP 2.3.0,
and optional Torch 2.14.1+cpu. Other supported Python/OS combinations were not run here.

- Locked core+dev+MCP installation: passed.
- Starter smoke/infrastructure suite: 5 passed.
- Reference contract suite: 10 core + 2 Torch tests passed.
- Starter advanced core contracts: 9 failures, 1 pass, as intended.
- Starter Torch contract suite: 2 failures, as intended.
- Real stdio MCP initialization, tool discovery, invocation and invalid-limit error: passed.
  The invalid-limit call deliberately produces an error log on stderr.
- Ruff static checks: passed.
- Python sdist and wheel build: passed.
- Wheel installed in a separate fresh environment outside checkout; downstream report: passed.
- CLI fixture report and deterministic 10,000-row CSV/SQLite generation: passed.
- Bad-review patch: git apply --check passed.
- Learner export strips instructor directory and Git history; removes instructor CI steps.
- Skill metadata and referenced files: checked; real learner/harness behavior not user-tested.

The core runtime is verified. Curriculum timing, learning outcomes and internal team tool onboarding
still require a first cohort/mentor pilot. This is not a completed student solution. Concurrency,
additional source integration, the MCP extension and final handover are intentionally assignments.
GitHub Actions configuration is included but has not run on GitHub before repository publication.
