# Internal readiness preparation

The existing stack includes VS Code, Jupyter, Docker, OpenShift, GitLab, Artifactory and Confluence.
The mentor prepares real paths, identities, locks and expected fixture outputs before teaching.
Use [GETTING_STARTED_INTERNAL](GETTING_STARTED_INTERNAL.md) for learner-facing guidance. Record owner, request date, next check
and fallback for blocked items; do not publish internal addresses or secrets.

| Resource | Evidence of readiness |
|---|---|
| GitLab | Chosen commit, internal clone, MR and safe job log |
| VS Code / personal OpenShift pod | Approved remote connection; terminal and repo verified inside the assigned pod |
| OMP / local LLM | Approved OMP version installed in the pod; current QWEN 3.8 endpoint/model route, workspace tools and reconnect verified |
| Jupyter / Python | Same project interpreter; breakpoint and clean notebook restart |
| Artifactory/uv | Approved internal lock/index/CA and imports without public downloads |
| Confluence | Team page and owner information accessible |
| Matt Pocock skills | Approved complete bundle, source revision and actual activation trace |
| Docker/registry | Known internal image/digest runs with expected output |
| OpenShift/storage | Fixture through teaching route; persistent output after safe restart |
| Data/weights | Manifests and approved LPR/tracklet/scoring/video resources |
| Agent/MCP | Approved endpoint and observed success/error/fallback |

Follow the [required setup order](GETTING_STARTED_INTERNAL.md#required-setup-order): VS Code,
personal-pod connection, then OMP/local LLM, before skill activation. The mentor provides the
internal OMP installation recipe and exact served model ID; no per-trainee model server is assumed.

Use uv for Python. The existing public ResearchLab lock is not the full Peanuach environment.
`--offline` is a cache check, not an Artifactory connection fix. Transfer only missing items with
versions, hashes, platform, transitive dependencies, weights/config/caches, fixtures and licenses.
Public-download snippets inside upstream skills do not override the internal environment policy.
The mentor validates the complete bundle; learners do not build registries or infrastructure.

Infrastructure buffer remains 40 hours, distributed 18/8/4/4/3/3. Ordinary research/debugging is
already in project time. A local container does not count as verified internal deployment.
