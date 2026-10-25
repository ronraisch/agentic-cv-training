# Peanuach Researcher Onboarding

Six weeks of research learning, individual teach-back sessions and agent-assisted work in one
monorepo covering both ordinary-camera video and remote sensing. Video scene understanding uses
ground/handheld/vehicle cameras, not satellite video. Tasks and reproducible evidence live here; reading and viewing
may also live in Drive. Active materials use English to avoid mixed-direction Markdown problems.

[Start here](docs/START_HERE.md) · [Six-week syllabus](docs/CURRICULUM.md)
· [Drive syllabus](https://docs.google.com/document/d/1shy8IhFa-Vri5SSCuN03x-ktt4gtwfal3Bp9Gnvwlvo/edit)
· [Required learning](docs/READING_AND_SESSIONS.md) · [Internal setup](docs/GETTING_STARTED_INTERNAL.md)
· [Original Drive collection](https://drive.google.com/drive/folders/1ZfbxunFLoea6JsUIbAiRbDgrkumhGDDA) · [New curated Drive workspace](https://drive.google.com/drive/folders/1MqJ6JWJ5ivd6voElujzTzPhmf7gZp_Jx)

| Part | Practical work |
|---|---|
| 0 | VS Code → personal OpenShift pod → OMP + local QWEN 3.8; GitLab, Artifactory, Confluence, Jupyter and Matt Pocock skills |
| 1 | A product request for the existing labeling application |
| 2 | Hough-based license-plate rectification and stitching two airborne images |
| 3 | LPR evaluation, tracklet motion classification and detection rescoring |
| 4 | A cloud-segmentation research proposal and ten-second video classification |
| Handover | Explain the deployed video inference path and reproduce it from a notebook |

Budget: **240 trainee hours**, including **40 hours of infrastructure/transfer buffer**.
Mentor budget: **12 hours total**, normally two scheduled windows a week, no more than
one hour on any day. Preparation and asynchronous review count against this limit.
The syllabus replaces duplicate courses and exercises; it does not add another course on top.

## Implementation status

This repository contains a synthetic Python ResearchLab and onboarding specifications. A working
Peanuach labeling/training/serving system has not been implemented here. The mentor supplies a
working teaching baseline or maps the existing team code before the cohort starts.
Model training results, internal deployment and installed-skill activation are not claimed.

```bash
uv sync --extra dev --extra mcp --locked
uv run researchlab
uv run pytest
uv run python tools/preflight.py --scope starter
```

These commands apply to the existing ResearchLab environment. Internal users follow the approved
Artifactory/CA/lock setup rather than assuming a public lock can resolve offline.
The full research tasks require a separately prepared
[research environment](docs/RESEARCH_ENVIRONMENT.md), working team code, data and model bundles.
Use [preflight](docs/PREFLIGHT.md) to separate local smoke results from missing internal handoff
records. Its default handoff scope reports the public template as blocked.

[Datasets by assignment](docs/DATASETS.md) · [Research learning with agents](docs/RESEARCH_WITH_AGENTS.md) · [Skills lab](docs/SKILLS_STAGE0.md)
· [Known pitfalls](docs/PITFALLS.md) · [Validation](docs/VALIDATION.md)

Original Drive files remain unchanged. The source folder allowed reading but rejected child-folder
creation; the new workspace was created separately in My Drive. Move it into the original collection
only after obtaining write access. Previous curricula remain in Git history.

Required foundation: [embeddings, VLMs, open-vocabulary detection and using open models](docs/lessons/07-open-models.md),
with a small shared-data probe inside the existing six-week budget.
