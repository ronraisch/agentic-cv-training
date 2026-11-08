# CLIP, VLMs, open-vocabulary detection and open-model use

[All training](index.md) · [Source coverage](sources.md)

## When the best text match names an absent object

An image encoder gives “red car” a higher similarity than “bicycle.” If these are the only candidates, red car wins. It may still be absent: the comparison ranks supplied descriptions rather than establishing that one must be true.

![“Red car” wins. There is no red car. “Red car”: 0.31; “Bicycle”: 0.28; Neither may be present](assets/dl-vision-language-toy.svg)

Candidate wording, scene context and crop scale can all affect the result. A whole-image score may reflect the general setting, while a detector or region-level comparison asks a more localized question. The scores are useful only in relation to the task and the way they were evaluated.

This distinction helps separate dual-encoder matching, generative VLM answers and open-vocabulary localization.

<details>
<summary>Jump to a concept</summary>

- [Two ways to connect text and images](#two-ways-to-connect-text-and-images)

- [Zero-shot labels and prompts](#zero-shot-labels-and-prompts)

- [Open-vocabulary localization](#open-vocabulary-localization)

- [VLM reasoning and uncertainty](#vlm-reasoning-and-uncertainty)

- [Using an open model responsibly in an experiment](#using-an-open-model-responsibly-in-an-experiment)

- [Comparing whole-image and region-level evidence](#comparing-whole-image-and-region-level-evidence)

</details>

## Two ways to connect text and images

A dual encoder maps an image and text into a comparable embedding space. CLIP-style training contrasts matching image/text pairs against other pairs. At inference, candidate text labels or descriptions become vectors and similarity gives a relative ranking. A generative vision-language model conditions a language model on visual information and generates tokens. A fluent generated answer and a high embedding similarity are different signals; neither is a guarantee that the described object exists.

## Zero-shot labels and prompts

Zero-shot classification compares an image against text candidates without fitting a task-specific classifier on labeled examples from those classes. The candidate set, wording and context affect results. Softmax over candidate similarities normalizes relative scores within that set; adding another candidate can change probabilities without changing the image. It is not an object-presence probability calibrated for arbitrary deployment scenes.

A whole-image embedding can respond to context while missing a tiny object. Proposal crops localize the comparison but depend on proposal recall and surrounding context. Few-shot supports can provide visual prototypes, and a linear head can adapt an embedding to a known task. Distinguish novel class labels from new instances of classes already seen in pretraining or task supervision.

## Open-vocabulary localization

An open-vocabulary detector connects region-level image evidence with text concepts and outputs localized predictions. OWL-ViT/OWL-V2-style families illustrate text-conditioned localization, with checkpoint-specific architecture and training. A grounding model can associate phrases with boxes. A promptable segmentation model can produce masks from supplied prompts, but the prompt source and semantic verification are separate steps. Combining a VLM with a segmenter does not automatically eliminate hallucination: an erroneous phrase or box can still trigger a plausible mask.

Thresholds depend on classes, prompts, scale and sensor. Evaluate positive recall and confusing negatives on independent target data. An absence of returned boxes may reflect a candidate limit, crop choice or low resolution rather than true absence. Save prompts, scores and model identity with outputs so errors can be diagnosed.

## VLM reasoning and uncertainty

A VLM can describe a scene, compare hypotheses or answer a bounded question. Ask for observable evidence and allow abstention, but verify against annotated examples. It can exploit language priors or overlook fine visual differences. A verbal confidence statement is not a measured uncertainty estimate. Test counterexamples with absent objects, misleading text and changed spatial relations.

## Using an open model responsibly in an experiment

Read the model card for intended tasks, input normalization, supported resolutions, checkpoint loading, output convention and use conditions. Freeze the chosen revision and weights, record their hash and load from an approved local path. Tokenizer/processor versions are part of the model interface. A forward method existing in a repository does not establish that a particular exported checkpoint uses it. Confirm a real loaded checkpoint and a consumed output.

Benchmark the whole path: preprocessing, tiling/cropping, GPU execution, merging and downstream decisions. In a proposal/embedding/classifier system, evaluate each stage and the end-to-end result. A verifier can improve precision while reducing recall or adding substantial latency. Decide its use from measured tradeoffs, and retain a route for uncertain examples to be reviewed.

## Comparing whole-image and region-level evidence

A useful comparison contains both a visible object and a plausible absent one, including a tiny object and a confusing category. Whole-image similarity, crop similarity and a text-conditioned detector can then disagree for understandable reasons. Inspecting their image regions helps distinguish a language prior, a scale problem and a localization failure before deciding which model to use.

<details>
<summary>Original source references and provenance</summary>

Original teaching text covering the cited topics, not a verbatim mirror. These references are provenance; no external reading is required to use this chapter.

- [https://cs231n.stanford.edu/slides/2025/lecture_16.pdf](https://cs231n.stanford.edu/slides/2025/lecture_16.pdf)

</details>
