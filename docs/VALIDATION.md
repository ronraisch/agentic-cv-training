# Validation record 23 October 2026

This update changes curriculum, mentor operations, language and publication materials. It does not
implement the Peanuach application or claim new model-training results.

## Checks for this update

The publication checks verify English active content, local Markdown links, the 240-hour trainee
budget, the 144-hour project allocation and the 12-hour mentor budget. The learner export is checked
for absence of mentor answers, later video releases and Git history. Notebook JSON stays an
unexecuted scaffold. Drive publications are verified after creation. See the final recorded results.

The source folder and active learner/mentor/developer documents were read. Old 2021-2024 and
Archive were not read. Original Drive items were not edited or deleted. Creating a child folder in
the source collection returned 403 insufficient parent permission; a separate My Drive workspace
was created instead. No permission modification or bypass was attempted.

## Limits

No internal GitLab/Artifactory/OpenShift/Confluence/client is accessible here. Approved skill
installation and real client activation are not verified; the curriculum specifies their stage-0
checks. A complete Peanuach baseline must still be supplied by the mentor. Timing is a planning
budget without a cohort pilot. Videos were not watched and precise time savings are not measured.
The skill references were read; the complete upstream packages were not installed or executed here.

Application code and its dependency lock were not changed. No dependency download or attempt to
bypass the prior rejected public-PyPI installation was made. Core pytest/ruff/MCP runtime checks
were not rerun for this documentation change. Older validation results remain in Git history and
must not be represented as fresh test results.

## Recorded results

PASS: active Markdown/CSV/notebook content contains no Hebrew characters; relative Markdown links
resolve; each weekly row totals 40 hours and all six total 240. Category totals are 28 core study,
4 media/substitute, 144 project, 12 research-with-agent, 12 mentor reserve and 40 buffer hours.
Project allocations independently sum to 144; six 120-minute mentor budgets sum to 12 hours.
Notebook cells remain unexecuted with no outputs. Git whitespace checks passed.

PASS: fresh learner export omits instructor files, maintainer notes and Git history. The polygon
brief does not reveal migration, schema or crop/training acceptance requirements.

PASS: three DOCX publication sources were title-sanitized, rendered and visually inspected.
All three were imported as native Google Docs in the new workspace and their content read back.
The public syllabus and workspace links are recorded in [README](../README.md).
These checks validate the published plan, not learner time estimates or internal runtime access.

## Ordinary-camera scope and dataset catalog follow-up

Clarified ordinary ground/handheld/vehicle-camera video independently of satellite/airborne imagery
in the syllabus, learner brief, lesson, system map, mentor preparation and notebook scaffold.
Every research assignment now links to the relevant section of [DATASETS.md](DATASETS.md). Source documentation
and links were checked; archives, data quality, access eligibility and internal transfer were not.
The catalog distinguishes supplied annotations from labels/metadata still needing preparation.
Two existing curated Drive documents were updated in place; original training documents were untouched.
Local-link/anchor, English-content, unchanged-budget, notebook and learner-export checks passed.
Application code/dependencies did not change; no runtime or model-training result is claimed.

## Open-model foundations follow-up

Added a required local introduction to embeddings, generative VLMs, open-vocabulary detection and
approved offline model use. The two-hour study allocation is inside the existing seven-hour DL
block (3 + 0.75 + 1.25 + 2 = 7); its one-hour probe is inside the existing 19-hour video baseline.
Local links/catalog anchor, English content, required-reading integration and unchanged weekly/total
budgets passed. Mentor discussion replaces an existing chain. No model was installed or run here.
The two curated Drive documents were updated in place and read back; original materials were untouched.

## Matt Pocock exposure and navigation correction — 24 October 2026

Replaced the mistaken plotting-skill requirement with pinned Matt Pocock catalog exposure and
selected deep practice. Kept the existing setup/mentor time caps; distributed practice replaces
part of existing work. Catalog metadata was read from the upstream snapshot; this is not evidence
of installed-client behavior. Internal installation and activation remain unverified.
Converted prose file references to relative Markdown links and added the ongoing authoring rule.
Checked local link targets/anchors, skill metadata, learner export and Git whitespace. Application
code and dependencies were unchanged; runtime/model checks were not rerun for this documentation edit.

## OMP and local LLM setup — 24 October 2026

Added the required order: install VS Code, connect it to the trainee's personal OpenShift pod,
then install/configure OMP against the local LLM (currently QWEN 3.8), before skill activation.
Added internal configuration fields and readiness gates for actual model routing, pod workspace
tools and reconnect. No OMP installer, provider protocol, internal endpoint or live connectivity
was verified here. The mentor supplies those deployment-specific values. Existing time allocations
and application code/dependencies are unchanged. Local links and Git whitespace were checked;
no application/runtime/model tests were rerun for this documentation-only change.

## Readiness audit fixes — 25 October 2026

Fixed learner export to recreate an empty artifacts directory without earlier evidence. Removed
the exported validation page's link to the omitted maintainer file. Course-skill file validation
now uses the repository path, requires both examples and reports its count; it does not claim
client activation. Seven tooling regressions cover missing skills, invocation from another cwd,
clean export, local file links and rejection of existing/nested export destinations. On the prior
tools these checks produced five failures and two passes; after the fixes all seven passed.

Added an instructor-only code/data/model/environment supply checklist with per-asset owners,
revisions and executed readiness gates, plus a learner-facing research-environment handoff.
Mapped the required selection from old labs 06/07/09 to existing allocations, leaving other
worksheet deliverables optional, and removed the obsolete weighted-grade reference.

Observed locally on macOS ARM64 / Python 3.11.14: locked dev/MCP/Torch sync succeeded; all 12
starter/tooling tests passed; Ruff and Git whitespace checks passed. The 10 core and two Torch
reference contracts passed. ResearchLab, real stdio MCP discovery/success/invalid-limit checks
and course-skill file validation succeeded. Local Markdown targets/anchors and the unchanged
six 40-hour weeks were checked. Export regression checks include learner local-link integrity.
The MCP invalid-input traceback is expected, not a failed protocol check.

No internal baseline, data/weights, OMP/client skill activation, Artifactory/OpenShift route or
production inference was verified. No intentional application defect or dependency lock was
changed. The supply checklist records preparation requirements, not newly supplied assets.

## PR 1 code review follow-up — 25 October 2026

The original PR clarified the research-environment handoff, preparation ownership/budget and
embedded practice, but its exporter still copied local environment files and scratch material.
Two new regressions reproduced this before the fix. Export now reads an immutable committed
HEAD archive, excludes `.env*` even when tracked, rejects source links and stages output before
publishing the destination. Local edits, untracked files and ignored caches are not distributed.
Maintainers must commit reviewed changes before exporting. The integration fixture also permits
running the tooling suite from a history-free learner copy.

On Linux / Python 3.12.14, the 16 application/tooling tests and 10 core reference checks passed;
Ruff, ResearchLab, course-skill file validation and real stdio MCP checks passed. The optional
Torch reference checks were not rerun in this environment. The pre-cohort checklist now asks for
a baseline notebook replay rather than the trainee's completed final handover notebook.
No research application, model bundle or real dataset was added; internal readiness remains
unverified until the supplied assets and actual commands are exercised in the trainee's pod.
