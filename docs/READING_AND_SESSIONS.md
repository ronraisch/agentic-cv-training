# Required learning and individual sessions

[Source collection](https://drive.google.com/drive/folders/1ZfbxunFLoea6JsUIbAiRbDgrkumhGDDA) · [Curated workspace](https://drive.google.com/drive/folders/1MqJ6JWJ5ivd6voElujzTzPhmf7gZp_Jx)

The current source documents have now been read: the New 2025 outline, Advanced Python, ML,
Stanford-2025 DL, the CV/ML/DL mentor guides, and the newer developer primer/questions.
Old 2021-2024 and Archive folders were excluded. No original Drive file was edited or deleted.
Detailed source decisions and mentor-only question selection are kept in the new mentor materials.

## One route per concept

The local material below is the default route. Use the named source section in Drive as a
substitute or targeted reference, not additional mandatory reading. External videos are optional
within the four funded media windows. If they are unavailable internally, use the local exercise.
No lecture timestamps or measured watch-time savings are claimed.

| Block | Required local material | Source section retained selectively | Study cap |
|---|---|---|---:|
| Development and stack | [lessons/01-development.md](lessons/01-development.md); [ENGINEERING.md](ENGINEERING.md) sections 1,2,3,5,6; [AGENT_WORK.md](AGENT_WORK.md); [TEAM_INTEGRATION.md](TEAM_INTEGRATION.md) | Advanced Python: type hints, useful decorators, bounded concurrency; outline: arrays/data | 8 h |
| Classical CV | [lessons/02-classical-cv.md](lessons/02-classical-cv.md) | CV mentor guide: filters, Hough lines, transforms, matching/RANSAC, warping; flow/pyramids at concept level | 6 h |
| Evaluation and ML | [lessons/03-metrics-ml.md](lessons/03-metrics-ml.md) | ML: linear/logistic models, evaluation, SVM intuition, trees/boosting; PCA/clustering intuition | 7 h |
| DL and representations | [lessons/04-torch.md](lessons/04-torch.md); [lessons/05-clouds.md](lessons/05-clouds.md); [lessons/06-video.md](lessons/06-video.md); [lessons/07-open-models.md](lessons/07-open-models.md) | Stanford 2025 chapters 4,5,8,9,10,12,16, selected slides/concepts only | 7 h |
| **Core study** | | | **28 h** |

The hourly caps include relevant code reading, self-checks and questions. A competent learner
should skip an already-demonstrated introductory explanation and use the time on a gap. All core
outcomes remain examinable; scope is bounded while the selected concepts retain deep questioning.

### Explicit DL study allocation

The seven hours are: 3 h training/attention fundamentals, 45 min cloud concepts, 75 min video
concepts and **2 h embeddings, VLMs, open-vocabulary detection and open-model usage** in
[the new local introduction](lessons/07-open-models.md). Its one-hour intuition probe uses one
hour of the existing 19-hour video baseline project budget. No extra mentor meeting or video
playlist is added. References replace repeated introductions and are read selectively.

### Four media windows

1. Development/array self-check: trace a request and an independent numerical example.
2. CV: draw a Hough vote, solve a transform and explain a failure case.
3. Evaluation: compute a metric and design a grouped comparison.
4. DL/video: trace tensor shapes or explain attention/temporal information with a toy example.

Each window is one hour. A mentor may select at most 40 minutes of a single relevant source video
and replace that exercise; pauses/reflection use the remaining 20. Do not assign a whole playlist
or both legacy and current videos. Choose source segments by concept and record actual runtime.

## What was deliberately reduced

- Broad beginner Linux/Python courses become diagnostics plus just-in-time remediation.
- Dozens of NumPy/Pandas exercises become a few failing counterexamples in the real project.
- Streamlit benchmarking, shape rendering and the separate Kaggle score target leave the core.
- Parallel introductory explanations of loss, regularization and linear models are merged once.
- Naive Bayes derivation, EM/GMM, spectral clustering and detailed t-SNE/UMAP become optional.
- RNN/LSTM gate derivations, exhaustive architecture history, generative-models blocks, 3D vision
  and distributed-training implementation become optional role-specific follow-up.
- Preserve attention/ViT, SSL/embeddings, segmentation, video, vision-language and inference
  correctness because they support this team's tasks. Replace many detector-history papers with
  one short comparison; a full detector implementation is no longer a second capstone.
- The developer-oriented primer is a diagnostic/reference for missing foundations, not another
  required 5-6 hours for researchers who have already learned those foundations.

## Teach-back rather than slide replay

The source DL mentor guide explicitly expects the trainee to teach the mentor, with precise terms
and sound arguments. The CV guide asks for cost-effective sessions rather than slide speed-runs.
Keep those principles with shorter scope and a limited question sample.

Before a meeting submit a one-page packet: one concept diagram, two verified claims, an unresolved
question, and a small counterexample. Explain a new example without the agent during the meeting.
Use notes and a debugger; memorizing syntax is not the goal. The mentor samples the required topics,
not every question in the original banks. Missing knowledge triggers a bounded retake.

Only the first session includes a rapid **10-minute basic-understanding check**, followed by the
**30-minute Matt Pocock skill teach-back**. Subsequent sessions focus on difficult question chains
from the existing mentor materials: derivations, counterexamples and research/production decisions.
Do not turn them into a repeated vocabulary quiz.
The weekly plan and the total 12-hour mentor cap are in [CURRICULUM.md](CURRICULUM.md). Product conversations and
reviews share those same windows; a new daily hour is not assumed.

## Independent research learning is part of the work

Use [RESEARCH_WITH_AGENTS](RESEARCH_WITH_AGENTS.md) for two funded hours every week. Ask the
approved repository-aware agent or ChatGPT to explain unfamiliar concepts, challenge hypotheses,
compare methods and propose a falsifying experiment. Verify evidence and explain the result yourself.
Only an approved internal endpoint may receive internal code or data; use synthetic abstractions
for public ChatGPT. A confident answer from a model is not a verified scientific source.
