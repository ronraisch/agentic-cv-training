# Retained advanced topics: learning setups, ranking and recommendation

[All training](index.md) · [Source coverage](sources.md)

## Choosing the next few examples to label

You have time to label three more images. The three most uncertain predictions are almost identical crops from one video; other candidates cover several different failure groups. Choosing solely by uncertainty may spend the whole budget on nearly the same case.

![You can label only three more images. Three near-duplicates; Three distinct groups; Same label budget](assets/ml-advanced-learning-toy.svg)

Active learning treats the choice of observations as part of the learning process. Diversity, representativeness and the cost of annotation can matter alongside uncertainty. A small random audit remains useful because a model can be confidently wrong in a region it never asks anyone to label.

The learning setups below make different assumptions about which labels and relationships are available.

<details>
<summary>Jump to a concept</summary>

- [Choose the target structure](#choose-the-target-structure)

- [Limited supervision](#limited-supervision)

- [One-class and anomaly detection](#one-class-and-anomaly-detection)

- [Metric learning, ranking and recommendation](#metric-learning-ranking-and-recommendation)

- [Multiple inputs, outputs and losses](#multiple-inputs-outputs-and-losses)

- [Reading the broader learning setups](#reading-the-broader-learning-setups)

</details>

## Choose the target structure

Multiclass classification chooses among mutually exclusive labels. Multilabel classification permits multiple labels per example and needs both per-label and per-example evaluation. Multiple-output regression predicts several numerical targets. A sequence-labeling system emits a label per token or time step, while sequence-to-sequence learning produces an output sequence with a potentially different length. Input/output structure determines losses, masks and metrics; replacing a final layer alone may not define the correct task.

## Limited supervision

Active learning chooses which examples to label next, often using uncertainty, diversity or expected gain. Uncertainty-only selection can oversample outliers and overlook confidently wrong regions. Evaluate label efficiency on independent data and retain random sampling as an audit. Semi-supervised learning combines labeled and unlabeled observations through assumptions such as smoothness, consistency or low-density class boundaries. Pseudo-label thresholds can reinforce existing biases; unlabeled data is not guaranteed to improve a misspecified task.

One-shot/few-shot learning uses very few labeled supports for a new task or class. Meta-learning can optimize adaptation across tasks, while pretrained embeddings with prototypes are a simpler alternative. Zero-shot learning uses semantic descriptions or other transferable supervision without task-class examples in the declared adaptation set. Clarify whether “unseen” means unseen during a small adaptation run or unseen anywhere in pretraining. Test novel categories and acquisition conditions separately.

## One-class and anomaly detection

One-class methods model accepted/normal observations and score departures. Density estimation, one-class SVMs, isolation approaches and reconstruction-based methods define normality differently. A high-dimensional Gaussian can have most of its probability mass far from its mean; density at a point is not an intuitive universal typicality score. Set thresholds against the operational false-alarm budget and a representative reference population. New legitimate conditions may look anomalous.

## Metric learning, ranking and recommendation

Metric learning shapes a space so selected relationships correspond to distance or similarity. Pair/triplet construction defines the supervision and can leak identity or acquisition context. Learning to rank optimizes ordering, with pointwise relevance, pairwise comparisons or listwise objectives. Recommendation adds user/item interaction data, exposure effects and cold-start constraints. A missing interaction is not always a negative preference: a user may never have seen an item.

Market-basket analysis finds co-occurring items. Support measures how often an itemset appears; confidence estimates a conditional frequency; lift compares that confidence to the consequent's base frequency. A high-confidence rule can merely predict a very common item. Co-occurrence is not causality, and repeated exploratory searches need independent validation. These ideas were present in the legacy primer even though they are not required current projects.

## Multiple inputs, outputs and losses

Combining image, metadata and text can improve predictions but also introduces missingness, synchronization and leakage risks. A multi-task network shares some parameters and has task-specific outputs. Loss weights, sampling frequencies and gradient scales determine which task dominates. Apparent regularization from auxiliary supervision can disappear if the auxiliary target leaks the main answer. Evaluate each output and relevant subgroups, not only a weighted training objective.

## Reading the broader learning setups

The older broad syllabus included these topics without making each one a separate project. They remain useful vocabulary for choices that arise in motion classification, rescoring and retrieval. For a role-specific extension, the useful depth is enough to explain the supervision available, the method’s main assumption and a case in which that assumption fails.

<details>
<summary>Original source references and provenance</summary>

Original teaching text covering the cited topics, not a verbatim mirror. These references are provenance; no external reading is required to use this chapter.

- [https://file.ai100.com.cn/files/file-code/original/cd136ebe-0e34-4e43-966b-224acff83005/100MLBOOK/The+Hundred-Page+Machine+Learning+Book.pdf](https://file.ai100.com.cn/files/file-code/original/cd136ebe-0e34-4e43-966b-224acff83005/100MLBOOK/The+Hundred-Page+Machine+Learning+Book.pdf)

</details>
