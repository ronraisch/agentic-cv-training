# Theory, viewing and mentor conversations

Start at [the training index](TRAINING_INDEX.md). Each of the four syllabi links directly to
HTML reading in this repository, exact source video URLs, exercises and mentor conversations.

## Learning policy

The material is for the trainee, not a compulsory reading checklist. A trainee who can explain
the concepts, solve a new example and answer the mentor's questions may skip familiar pages.
The expected understanding remains; exercises and agent-generated explanations do not replace it.
Reading, course viewing, derivations and discussion are substantial parts of the learning process.

Use the agent for active learning while implementing: ask why a method works, compare approaches,
construct counterexamples and test a hypothesis. Verify the answer and explain it yourself.
Use approved endpoints for internal code/data, and preserve the existing manual boundaries for
the Python capstone and the first SAM2 service setup.

## Four study routes

| Part | Syllabus and topic map | Suggested study | Suggested viewing/reflection |
|---|---|---:|---:|
| Development | [Development](reading/development.md) | 10–14 h | 3–5 h |
| Classical CV | [CV](syllabi/cv.md) | 12–18 h | 8–12 h |
| ML and evaluation | [ML](syllabi/ml.md) | 14–22 h | 3–5 h |
| Deep learning, open models and video | [DL](syllabi/deep.md) | 16–26 h | 18–28 h |
| **First-pass planning range** | | **52–80 h** | **32–50 h** |

Adjust the estimates with your mentor based on prior knowledge. The syllabi link to the selected UD810/CS4495 units and Stanford CS231n lectures. Use Michigan 2019 as an alternative explanation where it helps.

## Two conversations for each part

Arrange one foundations/application conversation and one deeper conversation for each of the
four parts, around actual readiness. This gives eight concept conversations. A suggested
45 minutes each uses 6 h trainee attendance; reserve the remaining 2 h from the existing
8 h contact allocation for targeted product/code review and final handover. These are scheduling
suggestions, not a limit on the mentor's theory questions. If more time is needed, update the
schedule explicitly rather than inventing an extra daily meeting.

Only the first conversation begins with a brief basic-understanding check. Later discussion
focuses on derivations, counterexamples, difficult cases and research/production choices from
the existing question banks. The mentor can ask theory throughout and does not have to replay
all slides or inspect a page-completion log.

Bring one concept you can explain, evidence from the exercise and one unresolved question.
Explain an unseen example without the agent. A gap leads to targeted reading/viewing and another
check. Practical correctness and conceptual understanding are recorded separately.

## First-pass readiness by lab

Use the lab's start card to obtain the first fixture. Try the prompt aloud before adding reading.
Bring one answer and one checked result to the first relevant mentor session. For the deeper
session, bring a new input or counterexample and explain which claim the evidence supports.
The lab's start card identifies any approval needed before continuing.

| Lab | Reference if needed | Try before the meeting |
| --- | --- | --- |
| Setup | [Required setup order](GETTING_STARTED_INTERNAL.md#required-setup-order) | Which interpreter does the attached debugger use? Show it at a breakpoint. |
| Manual Python | [Python modularity example](WORKED_EXAMPLES.md#python-modularity) and [shape handout](reading/legacy-shape-rendering.md) | If only the input format changes, which responsibilities should stay the same? |
| Polygons and SAM2 | [Trace one image from request to response](reading/development-interfaces.md#trace-one-image-from-request-to-response) | Where would you verify a record after reload? What would you inspect after a health check passes but inference fails? |
| Classical CV | [Plate rectification](lessons/02-classical-cv.md#hough-and-plate-rectification) and [stitching](lessons/02-classical-cv.md#stitching-exactly-two-images) | Follow one coordinate through each transform and say where it is expressed. |
| ML | [Split by the actual independence unit](reading/ml-bias-validation.md#split-by-the-actual-independence-unit) and [worked tables](WORKED_EXAMPLES.md#ml-evaluation) | Which rows enter the metric and which group must stay together? |
| Clouds and video | [Cloud and video examples](WORKED_EXAMPLES.md#deep-learning-and-video) and [open-model outputs](lessons/07-open-models.md#three-tools-three-output-contracts) | Name one downstream effect of a false cloud mask and one clip where sampling changes the answer. |
| RabbitMQ and SAM3 | [Redelivery](reading/development-interfaces.md#handling-a-job-that-arrives-a-second-time) | Predict what survives a crash between saving and acknowledgement. |
| Handover | [Notebook contract](../labs/research/06-handover.md#prepare-the-handover) | Name the exact files a peer needs and one output they can compare with the service. |

## Check the route before a cohort starts

Ask someone with introductory academic programming experience and someone with research ML
experience to walk through the route independently. Give each a first fixture and one seeded
failure. Record where they can locate the reading, reproduce the first output, diagnose the
failure and say what to bring to review. Record every point where a mentor had to supply an
instruction that could live in the repo. Have a mentor with internal access check the actual
Remote Sensing and OpenShift paths, permissions, fixture availability and deployment evidence separately.
