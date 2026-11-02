# Trainee guide — syllabus at a glance

Updated 1 November 2026. This is the short learner-facing overview; it is complete without Drive.
[Detailed syllabus](CURRICULUM.md) · [Reading map](READING_AND_SESSIONS.md) ·
[Dataset catalog](DATASETS.md).

## Order and working rules

Start with VS Code, your own OpenShift pod and Python/uv through Artifactory. Do the legacy Python
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
The existing 208 project hours are split into 184 work + 24 corrections; nothing is added twice.

| Assignment, in order | Work (h) | Corrections (h) | What you deliver |
|---|---:|---:|---|
| [Guided environment + OMP/skills](../labs/research/00-installations.md) | 6 | 0 | VS Code/pod, Python/Artifactory first; OMP only after Python review |
| [Manual Python capstone](../labs/research/00-python-manual.md) | 22 | 2 | Legacy point/polygon parser and panda drawing; modularity |
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

Required local reading is available in the repository. Read once, then apply it in the assignment;
the times below are separate from the practical-work table.

| Block | Material and topics | Active study |
|---|---|---:|
| Development | [Development](lessons/01-development.md), [engineering](ENGINEERING.md), [agent work](AGENT_WORK.md), [team integration](TEAM_INTEGRATION.md): Python/data contracts, modularity, Git/debugger, stack and evidence | 8 h |
| Classical CV | [CV lesson](lessons/02-classical-cv.md): filters, Hough, transforms, matching/RANSAC, warping and stitching | 6 h |
| Evaluation and ML | [ML lesson](lessons/03-metrics-ml.md): metrics/splits, linear/logistic models, SVM, trees/boosting, calibration; PCA/clustering intuition | 7 h |
| DL and open models | [Torch](lessons/04-torch.md), [clouds](lessons/05-clouds.md), [video](lessons/06-video.md), [open models](lessons/07-open-models.md): training/attention 3 h; clouds 45 min; video 75 min; embeddings/VLM/open-vocabulary models 2 h | 7 h |
| **Total** | | **28 h** |

There is no mandatory full lecture playlist. Four one-hour windows cover:
(1) Python/arrays and tracing a request; (2) Hough and image geometry;
(3) metrics and grouped evaluation; (4) DL tensors/attention/video.
Each uses up to 40 minutes of a mentor-selected relevant video plus 20 minutes of reflection,
or a one-hour local exercise. Across all four: at most 2 h 40 min actual viewing + 1 h 20 min
reflection, within the same 4 h allowance. The default is the local exercise until a video is assigned.

The existing source reference is selected Stanford CS231n 2025 material, chapters
4, 5, 8, 9, 10, 12 and 16, not the entire course. Exact recordings and timestamps have not been
selected/verified. Before assigning video, the mentor records its title, link, start/end and topic
in the internal learning copy; it replaces one of the four windows and does not add hidden hours.
A missing external video does not block learning: use the linked repository lesson.

## Mentor sessions and corrections

Reserve twelve windows across the program: normally six 45-minute concept teach-backs and six
35-minute product/code reviews, totaling **8 h trainee attendance**. Two final 40-minute handover
windows may replace the last 45/35 pair. Schedule around readiness, not assumed daily availability.
Preparation for the trainee's explanation is inside the relevant study/work allocation.

The first teach-back starts with a 10-minute basic check. Use the remainder for manual Python
review or, once ready, the Matt Pocock skill explanation. Later meetings focus on reasoning,
counterexamples and decisions. Bring a small evidence packet; explain a new example without an agent.
The mentor samples the actual work and can ask for a small change performed by you.

After each review, record the requested correction and resolve it from the table's **24 h total
correction allowance**. Unused allowance stays available; a retake uses this allowance, not a new
unbudgeted project. Mentor preparation/asynchronous review is **4 h separately**, making 12 h
mentor effort in total; those 4 h are not trainee attendance or active work.

## Total time and waiting

| Category | Hours |
|---|---:|
| Practical work | 184 |
| Feedback corrections | 24 |
| Required study | 28 |
| Viewing/local-exercise windows | 4 |
| Active research discussions with agent | 12 |
| Trainee attendance at mentor sessions | 8 |
| **Planned active trainee total** | **260** |
| Access/remediation contingency, used only when needed | 16 |
| Mentor prep capacity previously reserved in trainee schedule; not trainee work | 4 |
| **Conservative scheduling envelope** | **280** |

The previous seven-week label describes 280 scheduled hours, not seven measured weeks or 280 h
of net trainee effort. Calendar completion depends on actual active effort, mentor windows,
compute and what can overlap; revise estimates after the first cohort.

Agent generation, image builds, downloads/transfers, GPU inference/training and queue waits are
recorded as **unattended elapsed time separately** when no active attention is required. No fixed
wait estimate is claimed before the actual model, hardware and batch are known. Start with a small
batch, measure throughput and estimate the remaining run. Overlap independent study/work when
possible; count trainee time once. Monitoring, reviewing output and diagnosing failures are active.

For each assignment record: active work, feedback corrections, unattended waiting and elapsed
start/end. An agent working for 40 minutes while you do another assignment is not 40 minutes of
your work on both tasks. A blocked resource may still extend the calendar even with zero active work.

## Completion

Show working outputs on a new input, persistence/checkpoint reload where relevant and a concise
MR with scope-specific evidence. Distinguish observed, inferred, unverified and blocked claims.
Use the linked original Python handout and acquire data using the dataset guide. The owner supplies
internal paths, permissions, approved model assets and any original SAM handout;
do not invent missing specifications or treat a synthetic local smoke as internal deployment.
