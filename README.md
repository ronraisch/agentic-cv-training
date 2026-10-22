# Research Engineering with AI

**Inherit a research system. Understand it. Change it. Prove it. Hand it over.**

A Python onboarding repository for research teams using coding agents. ResearchLab is an
existing, deliberately imperfect dataset retrieval and embedding pipeline. NumPy, Pandas,
SQLite, mocked HTTP, optional CPU PyTorch, real local MCP, and reusable agent skills.
No cloud account, GPU, model download, or API key is required. Use your approved coding agent.

**Start with [the learner guide](docs/START_HERE.md).** עברית: [מדריך לחונך ולחניך](docs/README_HE.md).

```bash
uv sync --extra dev --extra mcp --locked
uv run researchlab
uv run pytest
uv run python tools/check_mcp.py
```

Optional PyTorch CPU track (Linux):
```bash
uv pip install torch --index-url https://download.pytorch.org/whl/cpu
uv run --no-sync python -m pytest instructor/test_torch_contract.py
```
The final command deliberately exposes inherited Torch defects. See the learner lab first;
instructor tests are an answer-bearing resource. On Mac use the platform's normal Torch wheel.
For dependency-managed installs use `uv sync --extra dev --extra torch --locked`;
the default PyPI Linux Torch distribution can download large accelerator dependencies.

## Route

| Lab | Work | Hours |
|---|---|---:|
| 00 | Environment, Python diagnostic, first run, Git | 2 |
| 01 | Inherit a repo and verify an architecture map | 3 |
| 02 | NumPy contracts, views, nonfinite values, ranking | 4 |
| 03 | Data contracts, joins, provenance, scene leakage | 4 |
| 04 | CSV/SQLite/HTTP adapters, pagination, resilience | 5 |
| 05 | CPU Torch inference, determinism, memory | 4 |
| 06 | Bounded agent work, context and local-model budgets | 3 |
| 07 | Use, improve, and evaluate skills; team tools | 4 |
| 08 | Connect and extend MCP; trust boundaries | 4 |
| 09 | Review a misleading patch; test the tests | 3 |
| 10 | Distribution, compatibility, handover, maintenance | 4 |
| 11 | Capstone, peer maintenance, individual defense | 6 |

Approximately 46 active hours, plus selected readings and mentor reviews; schedule across
2–3 weeks or spread over a month. Times are planning estimates, not measured completion times.
[Curriculum and gates](docs/CURRICULUM.md) · [Concept lessons](docs/ENGINEERING.md) ·
[Agent practice](docs/AGENT_WORK.md) · [Team tools](docs/TEAM_INTEGRATION.md) ·
[Mentor guide](instructor/GUIDE.md) · [Sources](docs/SOURCES.md)

The core suite is intentionally incomplete and initially green. Green is a baseline, not a
certificate of correctness. Instructor contract tests should fail on the starter and pass on
the reference implementation. Instructor content is visible in this repo; create a learner-only
copy with `python tools/export_learner.py /tmp/researchlab-learner` before assessment.

This is an original curriculum inspired by public Penn, Stanford and Carpentries materials;
not affiliated with or endorsed by those institutions, and not a claim to reproduce every class.
Original code and text: MIT. See [LICENSE](LICENSE) and source mapping for upstream licenses.
