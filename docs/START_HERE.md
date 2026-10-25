# Start here

Open the repository alongside the approved agent. Start from the syllabus and the required-learning
map; reading/video resources may live in Drive, while tasks and reproducible evidence live here.

1. Read [CURRICULUM.md](CURRICULUM.md) and [READING_AND_SESSIONS.md](READING_AND_SESSIONS.md).
2. Complete [stage 0](../labs/research/00-installations.md) with the mentor, in this order: VS Code installation, connection
   to your own OpenShift pod, then OMP with the local LLM (currently QWEN 3.8). Continue with
   Matt Pocock skills, GitLab, Artifactory, Confluence and Jupyter.
3. Obtain the working teaching baseline and real paths from the mentor. [SYSTEM_MAP.md](SYSTEM_MAP.md) records what
   is specified versus implemented; a filename in a plan is not evidence of working code.
   Verify the [research environment handoff](RESEARCH_ENVIRONMENT.md) for the assigned task;
   the synthetic ResearchLab installation does not provide the full research stack.
   Run [preflight](PREFLIGHT.md) to collect local smoke results and identify missing handoff records;
   a successful starter smoke is not evidence that internal prerequisites are ready.
4. Receive the [labeling product request](../labs/research/01-polygons.md).
5. Continue with [CV](../labs/research/02-classical-cv.md), [ML](../labs/research/03-evaluation-ml.md),
   [clouds](../labs/research/04-clouds.md), [video](../labs/research/05-video.md) and
   [handover](../labs/research/06-handover.md) as released by the mentor.

Use an agent for research learning as well as coding. Follow [RESEARCH_WITH_AGENTS.md](RESEARCH_WITH_AGENTS.md); bring a
small hypothesis and evidence packet to the scheduled mentor window. Queue product questions
instead of assuming the mentor is available every day. Do not guess requirements silently.

Do not read mentor materials or supply them to a learner agent. The distribution tool removes
mentor files, later product releases and Git history; the original public repository itself is
not access-controlled. Submit a bounded MR, inspect its diff and show scope-specific evidence.

Label claims observed, inferred, unverified or blocked. A swallowed exception is not a negative
result, a read function is not a verified live path, and a local test is not an internal deployment.
Only add small sanitized evidence from artifacts/. Never send internal data to an unapproved model.

The team covers remote sensing and ordinary-camera video. The video assignment is not satellite
video. Use [the per-assignment dataset catalog](DATASETS.md); external URLs identify sources,
while actual training and inference use the prepared internal data bundle.
