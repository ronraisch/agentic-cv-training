# Teaching system and evidence scope

Peanuach is a fictional team working on video, satellite and airborne imagery in one monorepo.
The existing runtime is a small synthetic ResearchLab retrieval/embedding pipeline with numerical,
data, HTTP and optional Torch examples. A complete labeling/training/serving system is not
implemented here. A mentor must prepare a working baseline or map actual team code before teaching.

| Area | What the trainee should understand |
|---|---|
| Development | React/TypeScript, Python API, data contracts, MR review and agent boundaries |
| Imagery/video | Coordinates, timestamps, metadata, input/output meaning and failure states |
| Research | Labels, splits/manifests, model artifacts, experiments and evaluation |
| Operations | Docker, Artifactory, OpenShift, storage and the actual loaded model |
| Knowledge | Repository tasks, linked Drive learning, internal Confluence context |

Inside the network use GitLab and approved internal resources. Outside, maintain the public
curriculum in GitHub. Internal Confluence content does not belong in the public repository.
Required Drive resources need an approved internal copy or a local-text substitute.

For each claim mark observed, inferred, unverified or blocked with commit/file or input/command/
output evidence. Reading code proves what is written, not which code executes. Trace training
configuration and selection through the saved artifact, image digest, loaded model and request.
Do not describe an incomplete chain as verified production behavior.
