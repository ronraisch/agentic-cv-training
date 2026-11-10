# Trainee guide — syllabus at a glance

When an idea is unclear, try the [agent explanation and teach-back routine](RESEARCH_WITH_AGENTS.md#when-you-get-stuck), then bring any remaining gap to your mentor.

[All four training parts](TRAINING_INDEX.md) · [Detailed syllabus](CURRICULUM.md) · [Reading map](READING_AND_SESSIONS.md) ·
[Dataset catalog](DATASETS.md).

## Order and working rules

Start with VS Code, your own OpenShift pod and Python/uv through Artifactory. Do the Shape Rendering
capstone manually before installing/updating/configuring OMP. After review, configure OMP with
the approved local LLM and learn the selected Matt Pocock workflows.

Then complete labeling/polygons and the first SAM2 service. Build that first service and its
minimal GitLab build/push/deploy pipeline by hand: Dockerfile, image, registry push, OpenShift
Deployment/Service/Route, logs and verification. ChatGPT explanations and illustrative examples,
documentation and mentor guidance are allowed; you assemble, run and explain the work yourself.

Continue through CV, ML, DL/video and handover in the order below. Agent assistance is expected
outside the explicitly manual work. Review its diffs, check its claims against executed evidence
and explain your own decisions. Use only approved internal models for internal data/code.
The later RabbitMQ/SAM3 exercise may use the agent.

## Practical work — active hours, not elapsed runtime

These are initial planning estimates, not measured cohort results or promised AI speedups.
“Work” includes design, prompting, reading agent output, implementation, debugging and verification.
“Corrections” is a separate allowance for addressing mentor/review feedback; ordinary debugging
belongs in work. Both columns count only time the trainee is actively engaged.

| Assignment, in order | Work (h) | Corrections (h) | What you deliver |
|---|---:|---:|---|
| [Guided environment + OMP/skills](../labs/research/00-installations.md) | 6 | 0 | VS Code/pod, Python/Artifactory first; OMP only after Python review |
| [Manual Python capstone](../labs/research/00-python-manual.md) | 22 | 2 | XML shape parser and panda drawing; modularity |
| [Labeling application](../labs/research/01-polygons.md) | 20 | 4 | Polygon support, persistence and consumer checks |
| [First SAM2 service + GitLab CI/CD](../labs/research/01b-sam2-service.md) | 14 | 2 | Manual Docker/image/push, Deployment/Service/Route and build/push/deploy pipeline |
| [LPR preprocessing](../labs/research/02-classical-cv.md) | 11 | 2 | Hough-based rectification |
| [Two-image stitching](../labs/research/02-classical-cv.md) | 10 | 2 | Matching, robust geometry and warp |
| [LPR evaluation](../labs/research/03-evaluation-ml.md) | 6 | 1 | Independent comparison of the preprocessing change |
| [Tracklet motion classifier](../labs/research/03-evaluation-ml.md) | 12 | 2 | Features, grouped splits, estimator and error analysis |
| [Detection rescoring](../labs/research/03-evaluation-ml.md) | 9 | 1 | Frozen detector, learned rescorer and evaluation |
| [Cloud segmentation proposal](../labs/research/04-clouds.md) | 7 | 1 | Bounded literature review and research proposal |
| [Ordinary-camera video](../labs/research/05-video.md) | 30 | 4 | Clip baseline, open-model probe and subsequent product requests |
| [RabbitMQ + SAM3 + detector](../labs/research/05b-rabbitmq-sam3-detector.md) | 22 | 2 | Queued pseudo-labeling, recovery, export and one YOLO/RT-DETR training run |
| [Operational notebook + transfer](../labs/research/06-handover.md) | 15 | 1 | Inference-only notebook, parity and peer handover |
| **Total** | **184** | **24** | |

The final video work uses ordinary cameras, not satellite video. Train one YOLO or RT-DETR in the
RabbitMQ/SAM3 exercise; no requirement to implement both. Audit pseudo-label quality and evaluate
on independently checked frames split by source video. All tasks above are required.

## Study, lectures and viewing

Use [one starting point](TRAINING_INDEX.md) for the four parts: Development, CV, ML and DL.
Each syllabus links to readings, videos, exercises and mentor conversations.

**The reading is for you, not a required completion checklist.** If you understand the concepts
and can answer the mentor's questions and explain an unseen example yourself, you can skip known
material. Theory, videos and learning with your agent remain significant parts of onboarding.
Use the reading during the exercises to deepen the ideas behind your choices.

| Part | Suggested study | Suggested viewing/reflection |
|---|---:|---:|
| [Development](reading/development.md) | 10–14 h | 3–5 h |
| [CV](syllabi/cv.md) | 12–18 h | 8–12 h |
| [ML](syllabi/ml.md) | 14–22 h | 3–5 h |
| [DL](syllabi/deep.md) | 16–26 h | 18–28 h |
| **Total first-pass range** | **52–80 h** | **32–50 h** |

Adjust these estimates with your mentor based on prior knowledge and how much of each course you watch.

## Mentor sessions and corrections

Use one foundations/application conversation and one deeper conversation for each of the four
parts. The mentor continues asking theory questions from the existing material, including
derivations, failure cases and gotchas. Only the first session starts with a quick basic check.
Explain a new example yourself, without the agent answering for you. Bring concise evidence from
your exercise and an unresolved question. A gap triggers targeted study and a follow-up check.

Eight suggested 45-minute conversations use 6 h contact. Reserve another 2 h from the existing
8 h contact allocation for targeted product/code review and final handover, with 4 h mentor
preparation separately. Schedule extra time explicitly when needed. The exercise table already
includes 24 h feedback corrections; do not double-count them as new implementation time.

## Total time and waiting

| Category | Hours |
|---|---:|
| Practical work | 184 |
| Feedback corrections | 24 |
| Theory study and derivations | 52–80 |
| Viewing/reflection | 32–50 |
| Active research learning with agent | 12 |
| Mentor attendance | 8 |
| **First-pass planned active trainee total** | **312–358** |
| Access/remediation contingency | 16 |
| Separately reserved mentor prep; not trainee work | 4 |
| **Conservative scheduling envelope** | **332–378** |

Unattended agent generation, builds, transfers,
inference/training and queue waits are recorded separately when no active attention is needed.
Reading during an unattended job counts as study once, not simultaneously as implementation.
Record actual active work, corrections, study/viewing, unattended waiting and elapsed start/end.

## Completion

Show working outputs on a new input, persistence/checkpoint reload where relevant and a concise
MR with scope-specific evidence. Distinguish observed, inferred, unverified and blocked claims.
Use the linked original Python handout and acquire data using the dataset guide. The owner supplies
internal paths, permissions, approved model assets and any original SAM handout;
do not invent missing specifications or treat a synthetic local smoke as internal deployment.
