# Start here

Begin with the manual Python exercise below; use the approved agent only after that exercise is reviewed. Start from [the training index](TRAINING_INDEX.md). Reading is available locally in HTML; videos keep their original links. Use the material to deepen understanding; reading completion is optional when you can answer the mentor’s questions yourself.

1. Open [the four-part training index](TRAINING_INDEX.md), then read [the short trainee guide](TRAINEE_GUIDE.md): all tasks, study/viewing, active hours,
   sessions and correction allowances are summarized there without needing Drive. Use
   [CURRICULUM.md](CURRICULUM.md) and [READING_AND_SESSIONS.md](READING_AND_SESSIONS.md) for details.
2. Complete [stage 0](../labs/research/00-installations.md) with the mentor, in this order: VS Code installation, connection
   to your own OpenShift pod, then Python/uv through Artifactory, interpreter/debugger and required access.
   Complete [the manual Python capstone](../labs/research/00-python-manual.md) before installing,
   updating or configuring OMP. After mentor review, complete OMP/local-LLM readiness (currently
   QWEN 3.8), Matt Pocock skills and the remaining setup checks.
3. Run the [working local baseline](BASELINE.md), or obtain the mapped internal system and paths from the mentor. [SYSTEM_MAP.md](SYSTEM_MAP.md) records what
   is specified versus implemented; a filename in a plan is not evidence of working code.
   Verify the [research environment handoff](RESEARCH_ENVIRONMENT.md) for the assigned task;
   the synthetic ResearchLab installation does not provide the full research stack.
   Run [preflight](PREFLIGHT.md) to collect local smoke results and identify missing handoff records;
   a successful starter smoke is not evidence that internal prerequisites are ready.
4. Receive the [labeling product request](../labs/research/01-polygons.md), then complete the
   mandatory [SAM2 annotation service](../labs/research/01b-sam2-service.md), including image build,
   registry push, OpenShift Deployment/Service/Route and application integration.
5. Continue with [CV](../labs/research/02-classical-cv.md), [ML](../labs/research/03-evaluation-ml.md),
   [clouds](../labs/research/04-clouds.md), [video](../labs/research/05-video.md) and
   [handover](../labs/research/06-handover.md) as released by the mentor. In the DL/video block,
   complete [RabbitMQ/SAM3 batch pseudo-labeling and detector training](../labs/research/05b-rabbitmq-sam3-detector.md)
   before handover; this is mandatory.

After the manual Python capstone, use an agent for research learning as well as coding. Follow [RESEARCH_WITH_AGENTS.md](RESEARCH_WITH_AGENTS.md); bring a
small hypothesis and evidence packet to the scheduled mentor window. Queue product questions
instead of assuming the mentor is available every day. Do not guess requirements silently.

Use only the authorized workspace and released task materials. Submit a bounded MR, inspect its
diff and show scope-specific evidence.

Label claims observed, inferred, unverified or blocked. A swallowed exception is not a negative
result, a read function is not a verified live path, and a local test is not an internal deployment.
Only add small sanitized evidence from artifacts/. Never send internal data to an unapproved model.

The team covers remote sensing and ordinary-camera video. The video assignment is not satellite
video. Use [the per-assignment dataset catalog](DATASETS.md); external URLs identify sources,
while acquire the task data using those instructions and use approved local copies for training and inference.
