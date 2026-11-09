# Curriculum and scheduling

See the [training index](TRAINING_INDEX.md) for the four syllabi and [the trainee guide](TRAINEE_GUIDE.md) for assignment links and hours.

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

Complete the [open-model probe](lessons/07-open-models.md) as part of the video baseline. See the [skills practice map](SKILLS_STAGE0.md#required-practice-inside-existing-assignments) for practice embedded in assignments.

## Trainee time budget

Use the [trainee guide's time budget](TRAINEE_GUIDE.md#total-time-and-waiting) as the source for scheduling. Count study, viewing, corrections and active work once each. Schedule around readiness and record unattended compute separately.

## Mentor availability

Schedule the [two mentor conversations for each part](READING_AND_SESSIONS.md#two-conversations-for-each-part) around trainee readiness. Reserve four hours separately for mentor preparation.

## Completion and fallback

Record concept understanding and practical verification separately. If access is blocked, record
the missing prerequisite and its owner. Use the 16-hour contingency for access and remediation.
If it runs out, agree on a smaller dataset or a prepared component with the mentor while keeping
the core learning goals.
