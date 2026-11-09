# Remote Sensing and Computer Vision Onboarding

Training for research engineers working with remote sensing imagery and ordinary-camera video.
[Start here](docs/START_HERE.md) for the onboarding sequence.

## Trainee syllabus

Start at [the training index](docs/TRAINING_INDEX.md): **Development · CV · ML · Deep Learning**.
Each part has its own syllabus, local HTML theory, original video links and current exercises.
Read [the formatted reading home](docs/reading/index.md) directly on GitHub, with all
chapters and syllabi linked as rendered Markdown. HTML remains available for local browser reading.
The reading is optional when you can answer the mentor's
questions and explain the concepts yourself. Theory and viewing remain substantial parts of learning.

See [the practical trainee guide](docs/TRAINEE_GUIDE.md) for manual-work boundaries and active effort,
sessions and corrections. Original Drive materials are preserved; [source coverage](docs/reading/sources.md)
records the migration and any unresolved internal reading.

## First run

See the [local ResearchLab demo](docs/BASELINE.md#run-the-demo) for commands and expected output.

[Start here](docs/START_HERE.md) · [Syllabus](docs/CURRICULUM.md)
· [Required learning](docs/READING_AND_SESSIONS.md) · [System map](docs/SYSTEM_MAP.md)
· [Internal setup](docs/GETTING_STARTED_INTERNAL.md) · [Research environment](docs/RESEARCH_ENVIRONMENT.md)
· [Preflight scope](docs/PREFLIGHT.md) · [Verification practice](docs/PITFALLS.md)

The ordinary-camera video task is distinct from the satellite/airborne image assignments.
Planning range: 312–358 active trainee hours, with a 332–378 h scheduling envelope including
16 h contingency and 4 h separately reserved mentor preparation. This replaces the older reduced
study estimate; actual learning time depends on prior knowledge and chosen viewing depth.
Practical work remains 208 h including feedback corrections. The DL block requires
[RabbitMQ/SAM3 batch pseudo-labeling and detector training](labs/research/05b-rabbitmq-sam3-detector.md).
External libraries/data/models are transferred and approved before the cohort; learners are not
expected to rebuild the team's infrastructure. Unattended compute/agent waiting is tracked separately.

For an executable CNN localization baseline, see [the local detector](docs/DETECTOR.md).
It includes offline training, saved-weight inference and held-out box/class/presence evaluation.

The [frozen research components](docs/COMPONENTS.md) supply raw plate detection/recognition,
vehicle predictions for rescoring and tracklets for motion classification. Acquire task data
using [the per-task steps](docs/DATASETS.md#acquire-a-working-subset). Model acquisition is
explicit; inference reads verified local artifacts.
