# Peanuach research workspace

Labeling, image geometry and ordinary-camera video in one Python workspace. Start with the
working baseline, then implement the assigned product request and demonstrate its effects.

<!-- maintainer-only:start -->
## Maintainer distribution reminder

Keep the baseline working and preserve the course's intentional minor rough edges. Follow
[the persistent maintainer policy](AGENTS.md) and [maintainer operations](MAINTAINERS.md).
Exact teaching scenarios and answers belong only in the restricted Drive registry.
**Before giving this to a trainee: remove this maintainer section, private links and maintainer
agent instructions by running the learner exporter. Do not distribute source Git history.**
Ask the owner to confirm this reminder on every cohort handoff. Do not add an answer catalogue.
<!-- maintainer-only:end -->

## First run

Install the approved environment using [offline setup](docs/OFFLINE_SETUP.md). For a connected
public development workstation only, the locked installation is:

```bash
uv sync --extra dev --extra mcp --locked
```

Then run without dependency resolution or downloads:

```bash
uv run --no-sync researchlab-demo prepare --root data/local-demo
uv run --no-sync researchlab-demo train --root data/local-demo
uv run --no-sync researchlab-demo evaluate --root data/local-demo
uv run --no-sync researchlab-demo predict --root data/local-demo --sample video-030
uv run --no-sync researchlab-demo serve --root data/local-demo
```

Open the loopback URL printed by the server. Draw rectangles, save and reload annotations.
Training reads the persisted records. The selected artifact is loaded for prediction; use its
reported SHA-256 to trace a response to the saved model. The same commands can use an approved
local data bundle conforming to [the data contracts](docs/DATA_FORMATS.md).

The included procedural fixture requires no dataset download or external weights. It exercises
real CPU optimization, artifact persistence and inference, and does not establish accuracy on
real cameras. For real assignments use the prepared [dataset bundles](docs/DATASETS.md).
Missing packages, files or model artifacts must stop with a path, recovery action and setup link.

```bash
uv run --no-sync researchlab-demo smoke --root artifacts/baseline-check
uv run --no-sync pytest
uv run --no-sync python tools/preflight.py --scope starter
```

[Start here](docs/START_HERE.md) · [Six-week syllabus](docs/CURRICULUM.md)
· [Required learning](docs/READING_AND_SESSIONS.md) · [System map](docs/SYSTEM_MAP.md)
· [Internal setup](docs/GETTING_STARTED_INTERNAL.md) · [Research environment](docs/RESEARCH_ENVIRONMENT.md)
· [Preflight scope](docs/PREFLIGHT.md) · [Verification practice](docs/PITFALLS.md)

The ordinary-camera video task is distinct from the satellite/airborne image assignments.
Budget: 240 trainee hours including 40 infrastructure/transfer hours, and 12 recurring mentor
hours. External libraries/data/models are transferred and approved before the cohort; learners
are not expected to rebuild the team's infrastructure.

For an executable CNN localization baseline, see [the local detector](docs/DETECTOR.md).
It includes offline training, saved-weight inference and held-out box/class/presence evaluation.
