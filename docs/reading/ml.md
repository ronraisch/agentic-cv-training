# 3 · Machine learning and evaluation

[All training](index.md) · [Source coverage](sources.md)

**Reading is for you; page completion is optional.** If you can explain the concepts and answer the mentor's questions yourself, that is enough. Use these pages and the course videos to deepen understanding during the exercises with your approved agent. [Learning route and manual-work boundaries](index.md).

<details>
<summary>On this page</summary>

- [Learning route and expected understanding](#learning-route-and-expected-understanding)

- [Practical work](#practical-work)

- [Videos and course selection](#videos-and-course-selection)

- [Mentor conversations](#mentor-conversations)

- [Original learner material](#original-learner-material)

</details>

## Learning route and expected understanding

Recommended first-pass study: 14–22 active hours; viewing/reflection: 3–5 active hours. These are planning ranges, not deadlines or measured full-course runtimes. Skip known explanations; deepen gaps. Record actual time.

| Topic | Local reading | What to understand and apply |
| --- | --- | --- |
| Paradigms, estimation and linear models | [Learning paradigms, probability, estimation and linear models](ml-foundations.md) | Explain MLE/MAP, linear/polynomial/logistic regression, regularization and dimensionality. |
| Bias, validation and shift | [Bias, variance, dataset shift and trustworthy validation](ml-bias-validation.md) | Distinguish statistical bias and human/data biases; design grouped splits, bootstrap/CV and drift audits. |
| Evaluation across task types | [Classification, detection, regression, ranking and selective prediction](ml-metrics.md) | Compute classification/detection, regression, ranking, calibration and risk-coverage metrics. |
| Generative classifiers, neighbors and SVM | [Naive Bayes, Gaussian discriminants, KNN and kernels](ml-generative-neighbors.md) | Explain Gaussian discriminants, Naive Bayes, KNN, kernel regression and margin/kernel choices. |
| Trees and ensembles | [Trees, forests, AdaBoost, gradient boosting and model combination](ml-trees-ensembles.md) | Compare trees, forests, bagging, AdaBoost, gradient boosting, XGBoost/LightGBM, voting and stacking. |
| Unsupervised learning and visualization | [PCA, clustering, EM/GMM, t-SNE and UMAP](ml-unsupervised.md)<br>[NumPy, Pandas, data contracts and visual exploration](arrays-data.md) | Use PCA, K-means, hierarchical/DBSCAN/spectral clustering, EM/GMM, t-SNE/UMAP and clear plots. |

## Practical work

- [LPR evaluation, tracklets and rescoring](../../labs/research/03-evaluation-ml.md)

Read selectively before and during implementation; discuss hypotheses with your agent, verify one counterexample and explain the evidence yourself. The manual Python capstone and first SAM2 service retain their existing manual rules.

## Videos and course selection

Use the original topic videos below, pausing to derive an example or inspect your experiment. Do not replace substantial theory with four short generic media windows. A familiar learner can choose relevant sections; no duplicate viewing is required.

- [Itay’s lecture](https://www.youtube.com/watch?v=aClpa7VORrE&list=PLuS9MY73SUnKeZQBk5LWxZah_-njyk-gV&index=12)

- [Ron’s AAAI](https://youtu.be/-KWgXpDZVoI?si=Za38DBG7d9ppzUdZ)

## Mentor conversations

Session 1: estimation, model choice, leakage and bias. Session 2: metric hand calculation, comparison uncertainty and error analysis; probe unsupervised assumptions and explain an alternative model. The mentor selects deeper chains from the existing question bank.

The mentor keeps the existing theory questions and probes your reasoning with a new example. Reading-page completion is not assessed. If you can answer and explain the assigned concepts yourself, your learning route is sufficient. Gaps lead to targeted study and another discussion, not an obligation to reread every source.

## Original learner material

Complete historical handouts are preserved locally with their reading links redirected. Historical project requirements are not added to the current workload.

- [Original ML training handout](legacy-ml.md)

- [Original ML topics and links](legacy-ml-topics.md)

- [Original earlier ML program](legacy-ml-program.md)

- [Original additional ML readings](legacy-ml-additional.md)

- [Original team metrics notes](legacy-metrics.md)

- [Original broad ML topic checklist](legacy-hundred-page-topics.md)
