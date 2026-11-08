# Researcher syllabus — active effort and scheduling envelope

Start with [the training index](TRAINING_INDEX.md), then [the concise trainee guide](TRAINEE_GUIDE.md), which separates active work,
feedback corrections, mentor attendance and unattended waiting.

The teaching scenario covers two domains: remote sensing (satellite and airborne imagery) and
video from ordinary cameras (ground, handheld, indoor/outdoor or vehicle-mounted). The video
scene-understanding assignment is not satellite video and does not require aerial footage.
Dataset sources and bounded preparation are in [Datasets by assignment](DATASETS.md).
Required concepts are assessed through short individual teach-back sessions. Practical delivery
is assessed separately. After the initial manual Python capstone, agent-assisted research learning is expected, not just
code generation, except for the first SAM2 service setup, which must be completed by hand.

## Scope and priorities

Keep Python/array/data contracts, evidence discipline, image geometry, evaluation, classical ML,
training/inference fundamentals, embeddings, generative VLMs, open-vocabulary detection,
open-model usage, video/time and customer-facing decisions.
Preserve the subjects from the old development, CV, ML and DL programs. Each has a
[stage syllabus](TRAINING_INDEX.md) with local HTML reading and original video links.
The material is optional as a reading route: understanding and the ability to answer the mentor's
questions are expected. Keep learning theory while implementing with the agent. The previous
selective reduction of Naive Bayes, EM/GMM, bias topics, generative models and 3D is superseded.
Avoid duplicated explanations when a learner already understands the concept.

| Part | Practical assignment |
|---|---|
| 0a | Guided pod/VS Code/Python/Artifactory setup; [manual Python capstone](../labs/research/00-python-manual.md), about three working days, without coding agents |
| 0b | OMP/local-LLM setup after capstone review; Matt Pocock skill installation/teach-back |
| 1 | Product request in the labeling application |
| 1b | [Required SAM2-assisted annotation service](../labs/research/01b-sam2-service.md): first Docker image and Deployment/Service/Route setup by hand; application integration |
| 2 | Hough-based LPR preprocessing; stitch two airborne images |
| 3 | Evaluate the LPR change; classify tracklet motion; learn a detection rescorer |
| 4 | Short cloud-segmentation proposal; video classification with staged customer requests |
| 4C | [Required RabbitMQ/SAM3 batch pseudo-labeling and RT-DETR or YOLO training](../labs/research/05b-rabbitmq-sam3-detector.md) in the DL/video block |
| Handover | Reproducible operational video notebook and peer transfer |

Two-image stitching is required. More images require mentor approval and replace another optional
extension. Cloud work is an eight-hour proposal, not another full training project. Rescoring uses
a frozen detector and prepared data. The [SAM2 service assignment](../labs/research/01b-sam2-service.md) is mandatory after polygon support.
EfficientDet/RF-DETR assignments remain outside the required route.

Before Part 4, use [the DL syllabus](syllabi/deep.md), including training, representations,
embeddings, VLMs and open-vocabulary detection. The existing open-model intuition probe remains
inside the video baseline project; the restored reading does not add another detector project.

## Trainee time budget

The practical assignments retain **208 h**: 184 h active implementation and 24 h feedback
corrections. The restored theory route suggests 52–80 h study and 32–50 h viewing/reflection,
plus 12 h active agent learning discussions and 8 h mentor attendance. This gives a first-pass
**312–358 h active trainee planning range**. With the existing 16 h contingency and 4 h separately
reserved mentor preparation, the conservative scheduling envelope becomes **332–378 h**.

These are unmeasured planning estimates, not a promise of completion time or a limit on learning.
Full course viewing may exceed them. Familiar learners can skip already understood reading;
novices may need extra study. Record actual work, corrections, study/viewing and unattended
waiting separately; overlap counts once. The former 260/280 h totals and four short media windows
are superseded, because they assumed reduced theory breadth.

| Category | Active trainee hours |
|---|---:|
| Practical work including feedback corrections | 208 |
| Theory study and derivations | 52–80 |
| Viewing and reflection | 32–50 |
| Active research learning with agent | 12 |
| Mentor attendance | 8 |
| **Planned active total** | **312–358** |

### Project allocations

The following totals include feedback corrections: 184 active implementation hours + 24 active
feedback-correction hours = 208. See [the per-task split](TRAINEE_GUIDE.md#practical-work--active-hours-not-elapsed-runtime).
The 12-hour mentor column splits into 8 hours trainee attendance and 4 hours mentor preparation.
Trainee preparation stays inside study/project allocations; do not count it again.

| Work | Hours |
|---|---:|
| Guided setup, including skills (OMP only after manual capstone review) | 6 |
| Manual Python capstone and review | 24 |
| Labeling request | 24 |
| Required SAM2 service and application integration | 16 |
| Hough-based LPR rectification | 13 |
| Stitch two images | 12 |
| LPR evaluation | 7 |
| Tracklet motion classifier | 14 |
| Detection rescoring and evaluation | 10 |
| Cloud literature review and proposal | 8 |
| Video baseline and subsequent customer requests | 34 |
| Required RabbitMQ/SAM3 batch labeling and detector training | 24 |
| Notebook, integration and transfer | 16 |
| **Total** | **208** |

These include implementation, tests, experiments and evidence. Their placement within a week may
move to follow readiness and mentor windows. Keep the 16 h access/remediation contingency. The SAM2 and RabbitMQ/SAM3 assignments remain
mandatory and are already included in 208 project hours. The restored reading and videos are
counted separately above. Historical full CS231n assignments, Kaggle score targets and optional
Python exercise banks are retained as references rather than added as mandatory projects.
For the exact required selection from older labs 06/07/09 and the time it replaces, use
[the embedded practice map](SKILLS_STAGE0.md#required-practice-inside-existing-assignments).
The required SAM2 service supersedes any earlier optional SAM wording.
Other deliverables in those standalone worksheets are optional unless the mentor explicitly
substitutes them for existing work.

## Mentor availability

Use two concept conversations for each of the four parts: one foundations/application session
and one deeper discussion, with theory questions throughout. Eight suggested 45-minute sessions
use 6 h contact, leaving 2 h from the existing 8 h attendance budget for targeted reviews and
handover. Reserve 4 h mentor preparation separately. Schedule around readiness and record extra
time explicitly if needed. No daily meeting is assumed.

Use [the session guidance](READING_AND_SESSIONS.md#two-conversations-for-each-part) and the
existing mentor theory banks. The trainee explains a new example; the mentor probes assumptions,
derivations and errors. Reading completion is not assessed. Keep first-service setup manual as
specified in [the SAM2 assignment](../labs/research/01b-sam2-service.md#first-service-hands-on-ownership).

## Completion and fallback

Each part records concept readiness and implementation readiness separately. Infrastructure is
guided learning, not a DevOps examination. No average score excuses leakage, inability to explain
a critical line, or an unverified operational claim.

If the remaining 16-hour buffer is exhausted, drop optional breadth, reduce experiments/data size and use
a prepared encoder/detector. Do not silently cut core knowledge. Record blocked access honestly;
a local container is not an internally deployed service. If the teaching baseline is absent,
report the blocked assignment rather than requiring a novice to build the whole team stack.
