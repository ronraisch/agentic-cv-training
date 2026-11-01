# Researcher syllabus — seven working weeks

The teaching scenario covers two domains: remote sensing (satellite and airborne imagery) and
video from ordinary cameras (ground, handheld, indoor/outdoor or vehicle-mounted). The video
scene-understanding assignment is not satellite video and does not require aerial footage.
Dataset sources and bounded preparation are in [Datasets by assignment](DATASETS.md).
Required concepts are assessed through short individual teach-back sessions. Practical delivery
is assessed separately. After the initial manual Python capstone, agent-assisted research learning is expected, not just code generation.

## Scope and priorities

Keep Python/array/data contracts, evidence discipline, image geometry, evaluation, classical ML,
training/inference fundamentals, embeddings, generative VLMs, open-vocabulary detection,
open-model usage, video/time and customer-facing decisions.
Choose one learning route per concept. Do not watch both Stanford 2025 and Michigan 2019, read
several introductory blogs and then repeat the same explanation in a mentor session.
See [the reading plan](READING_AND_SESSIONS.md) for exact local sections and substitutions.

| Part | Practical assignment |
|---|---|
| 0a | Guided pod/VS Code/Python/Artifactory setup; [manual Python capstone](../labs/research/00-python-manual.md), about three working days, without coding agents |
| 0b | OMP/local-LLM setup after capstone review; Matt Pocock skill installation/teach-back |
| 1 | Product request in the labeling application |
| 1b | [Required SAM2-assisted annotation service](../labs/research/01b-sam2-service.md): Docker image, Deployment, Service, Route and application integration |
| 2 | Hough-based LPR preprocessing; stitch two airborne images |
| 3 | Evaluate the LPR change; classify tracklet motion; learn a detection rescorer |
| 4 | Short cloud-segmentation proposal; video classification with staged customer requests |
| 4C | [Required RabbitMQ/SAM3 batch pseudo-labeling and RT-DETR or YOLO training](../labs/research/05b-rabbitmq-sam3-detector.md) in the DL/video block |
| Handover | Reproducible operational video notebook and peer transfer |

Two-image stitching is required. More images require mentor approval and replace another optional
extension. Cloud work is an eight-hour proposal, not another full training project. Rescoring uses
a frozen detector and prepared data. The [SAM2 service assignment](../labs/research/01b-sam2-service.md) is mandatory after polygon support.
EfficientDet/RF-DETR assignments remain outside the required route.

Before Part 4, complete [the open-model introduction](lessons/07-open-models.md): two study hours
inside the existing seven-hour DL block and a one-hour intuition probe inside the 19-hour video
baseline portion of its 34-hour project. The probe does not add a detector-training project.

## Trainee time budget

Plan 35 working days at eight hours: 280 hours. SAM2 adds 16 hours and the mandatory
RabbitMQ/SAM3 detector pipeline adds 24 hours to the previous 240-hour plan. Retain the
remaining 16-hour buffer. These are planning caps, not measured cohort times.

| Week | Focus | Core study | Video or substitute | Project work | Research with agent | Mentor contact/prep budget | Buffer | Total |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | Setup and manual Python; agent hours only after capstone review | 5 | 1 | 30 | 2 | 2 | 0 | 40 |
| 2 | Python review, OMP/skills, labeling and geometry | 6 | 1 | 27 | 2 | 2 | 2 | 40 |
| 3 | LPR, stitching and LPR evaluation | 5 | 1 | 26 | 2 | 2 | 4 | 40 |
| 4 | Tracklets, rescoring and evaluation | 5 | 0 | 27 | 2 | 2 | 4 | 40 |
| 5 | Cloud proposal and video baseline | 5 | 1 | 27 | 2 | 2 | 3 | 40 |
| 6 | Video requirements and handover | 2 | 0 | 31 | 2 | 2 | 3 | 40 |
| Added allocation | SAM2 service, scheduled after polygon support; shift later work accordingly | 0 | 0 | 16 | 0 | 0 | 0 | 16 |
| Added DL allocation | RabbitMQ/SAM3 pseudo-labels and detector training, before handover | 0 | 0 | 24 | 0 | 0 | 0 | 24 |
| **Total** | | **28** | **4** | **208** | **12** | **12** | **16** | **280** |

The mentor column reserves capacity conservatively: preparation/review time does not require
trainee attendance, but those hours are not double-booked with a separate trainee task. Contact
may be shorter. Use any released trainee time for remediation or reflection, not more requirements.

Study includes targeted code reading and self-checks. Four media windows each allow up to
40 minutes of video and 20 minutes of pauses/reflection, or one hour of the local text exercise.
There is no requirement to watch a full external lecture. Time spent discussing research with an
agent is explicitly funded: two hours weekly, additional to implementation time. Waiting for a
training job while reading counts once. Ordinary debugging belongs to project work; the remaining buffer
covers access, transfer, queues and unusual setup failures.

### Project allocations

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
move to follow readiness and mentor windows. The manual Python capstone uses 24 hours of the former 40-hour buffer, leaving 16 hours;
SAM2 adds 16 project hours and RabbitMQ/SAM3 adds 24, bringing the plan to 280 hours.
The 24-hour DL estimate includes implementation and review; record unattended batch/training
runtime separately and overlap it only where compute and dependencies permit. No full CS231n assignments, Kaggle leaderboard target or duplicate
Python exercise bank is added on top. The legacy shapes/parser exercise is this single capstone.
For the exact required selection from older labs 06/07/09 and the time it replaces, use
[the embedded practice map](SKILLS_STAGE0.md#required-practice-inside-existing-assignments).
The required SAM2 service supersedes any earlier optional SAM wording.
Other deliverables in those standalone worksheets are optional unless the mentor explicitly
substitutes them for existing work.

## Mentor availability

Plan two windows a week: typically 45 minutes of teach-back and 35 minutes of product/review,
plus 40 minutes of preparation/asynchronous review. This is 12 total recurring mentor hours across the original six-week blocks; the added work uses those
existing review windows. This does not assume an additional mentor week.
Week 1 uses a 45-minute first session: 10 minutes of basic understanding, 30 minutes of manual-code review or, after capstone completion, skill
teach-back and 5 minutes of next steps, plus a separate 35-minute setup/product window.
The final handover uses two separate 40-minute handover/defense windows and 40 minutes of prep/review.
Never assume a daily meeting; leave product questions in a concise queue and record decisions.
The existing weekly 15-minute team-lead check-in is folded into a review window if required,
not scheduled as an extra meeting. One person holding both roles still has the same total budget.

The trainee teaches the concept; the mentor asks discriminating questions. Do not replay slides.
Unresolved topics become a bounded independent-learning task followed by one new check.

## Completion and fallback

Each part records concept readiness and implementation readiness separately. Infrastructure is
guided learning, not a DevOps examination. No average score excuses leakage, inability to explain
a critical line, or an unverified operational claim.

If the remaining 16-hour buffer is exhausted, drop optional breadth, reduce experiments/data size and use
a prepared encoder/detector. Do not silently cut core knowledge. Record blocked access honestly;
a local container is not an internally deployed service. If the teaching baseline is absent,
report the blocked assignment rather than requiring a novice to build the whole team stack.
