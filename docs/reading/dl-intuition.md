# Deep learning intuition: find the bottleneck

[Chapter index](index.md) · [Source coverage](sources.md)

You train a detector on aerial tiles. The loss comes down, the validation score looks respectable, and the model still misses most small trucks. A larger model might help. Before changing it, follow one missed truck through the system. Was it visible after resizing? Did it get a positive training assignment? Could the model emit enough boxes for that tile? Did a usable box disappear at the score threshold? Each answer points to a different experiment.

<details>
<summary>Jump to a concept</summary>

- [Follow the signal from input to prediction](#what-makes-a-task-learnable)

- [Anchors: check who gets taught to predict the box](#anchors-and-matching)

- [Queries: count how many answers the model can emit](#query-budget)

- [What changes when you turn a knob?](#architecture-knobs)

- [Make an experiment that can change your mind](#make-a-diagnostic-experiment)

- [Further reading](#sources)

</details>

## Follow the signal from input to prediction

| Question | How learning or prediction can fail | What to look at |
| --- | --- | --- |
| Is the answer visible? | Resize, blur, crop or occlusion removes the distinguishing detail. | Draw labels on the actual model input, including augmented examples. |
| Does the model keep it? | Pooling, coarse grids or a narrow feature bottleneck discard evidence the head needs. | Compare a frozen head on a fine and coarse feature map using the same images. |
| Does the loss ask for it? | Missing labels, weak assignments or overwhelming background give the wrong or infrequent training signal. | Count positives and ignored targets per object and look at their assigned boxes. |
| Can the model learn the mapping? | Optimization is unstable, or the model lacks sufficient capacity or context. | Try to fit a small, clean batch. Log per-loss terms and gradient or parameter updates. |
| Can the system return the answer? | Query capacity, candidate limits, thresholding or suppression remove otherwise usable predictions. | Compare raw outputs, decoded candidates and the final output on the same images. |

Shortcuts can make a task look easier during training. If almost all trucks in training are photographed on gravel, predicting “truck” from gravel is rewarded. Hold out a site and add examples of trucks on pavement and gravel without trucks. This tests whether the model learned a transferable cue.

## Anchors: check who gets taught to predict the box

In an anchor-based detector, anchors are reference boxes. During training an assigner compares candidate anchors with the ground-truth boxes. A positive assignment tells the class branch to recognize an object and gives the regression branch a box to learn. The anchor can be a rough starting point, since the head can predict offsets. What matters first is which targets actually receive useful supervision.

Imagine an 8 × 24 truck and a centered 24 × 24 anchor. The truck is fully inside the anchor. Their intersection area is 192 pixels², the union is 576 pixels², and their IoU is one third. An assigner that requires IoU of at least 0.5 would reject that pair. An assigner that guarantees a best match could keep it anyway. Similar misses can come from center spacing rather than shape. Anchor-free heads also assign supervision, typically using points, center rules or a cost that depends on predictions.

Plot the best candidate IoU and the number of positives per object after preprocessing. Split the plot by size and aspect ratio, and inspect the objects with zero positives. Then compare one change, such as adding a finer feature level, modifying anchor shapes or changing the assignment rule. Check how many positives the change adds and what happens to validation recall and false positives. A bigger anchor set can make the problem worse if it mostly adds redundant candidates.

## Queries: count how many answers the model can emit

In standard DETR-style set prediction, each final object query emits at most one detection and can be matched to at most one labeled object. With 100 output queries and 140 valid objects in one tile, even a perfect set of outputs can recover at most 100/140, or about 71%, before filtering. For a validation slice with object counts nᵢ, add the smaller of nᵢ and the query count for each image, then divide by the total number of objects to get a dataset-level recall ceiling. Use the actual maximum returned by the system if top-k or a downstream cap is lower.

First plot object counts per model input. Then count useful predictions before filtering. If many sparse tiles are missed while most query slots go unused, a larger query budget has a weaker case. Look at feature resolution, matching, query initialization or training instead. If dense tiles routinely hit the ceiling, compare more queries with tiling. More queries increase decoder work and may change the balance between matched and unmatched slots. Tiling changes object scale and context and adds merge work. Evaluate both with scene-level splits and a size- and density-stratified recall report.

## What changes when you turn a knob?

| Change | What the model gets | What you pay or still need to check |
| --- | --- | --- |
| Wider hidden or latent dimension | More feature coordinates at each position, or more coordinates in a pooled embedding. This can relieve a feature bottleneck. | Memory and computation increase. Doubling both dimensions of a dense layer multiplies its weight count by four. A wider projection after a frozen representation can reorganize its information; it cannot distinguish two inputs the frozen encoder represented identically. |
| More layers | More stages of composition and refinement. In a CNN, additional local layers can broaden the receptive field. In a global-attention Transformer, tokens can already exchange information in the first attention layer, and deeper layers can build on those exchanges. | More sequential work and a different optimization problem. Compare training fit, validation gains and inference cost. Extra depth cannot restore spatial detail already discarded. |
| Smaller effective output stride | More spatial sites for small objects or boundaries. At 512 × 512, stride 32 gives 16 × 16 sites and stride 16 gives 32 × 32. | Four times as many sites in this example. A dense head processes more locations. For global attention over the entire grid, the pairwise score matrix has about sixteen times as many entries. |
| Larger input or smaller ViT patches | A larger input can preserve more samples of the object if the source has the detail. Smaller patches give more spatial tokens on the same input. | More feature sites and potentially more memory. Resizing beyond the native image resolution cannot recover details absent from the source. Compare original-scale crops and measure effective object sizes. |
| More queries or more anchor candidates | Queries raise the possible output count. Anchors add candidate starting locations or shapes for assignment and regression. | They solve different problems. Measure the query ceiling for the first, and the number and quality of positive assignments for the second. Account for decoding and post-processing costs. |

Keep three dimensions distinct when reading a config: **feature width** is how many numbers describe each location, **spatial resolution** is how many locations describe the image, and **query count** is how many candidate output slots the decoder can use. Doubling one does not double the others.

## Make an experiment that can change your mind

- **Start with a known batch.** Pick a few clear, fully labeled examples, turn off strong augmentation and inspect the transformed labels. Try to overfit those examples and view the decoded outputs. Failure is a reason to check loss targets, gradients and model constraints. Success only shows the system can fit those inputs.

- **Follow the missed cases.** Choose small, crowded and clean examples. Compare the input, assignments, raw scores and final predictions. Record how many objects never became candidates, how many had a usable low-score box, and how many were lost after filtering.

- **Change a knob with a prediction.** If coarseness is the bottleneck, a finer map should improve small-object recall more than it improves large-object recall. If query capacity is the bottleneck, extra queries should help the densest tiles first. If validation is the only problem and training already fits well, test domain shift, shortcuts and labeling before increasing capacity.

- **Decide using paired evidence.** Keep the split and metric code fixed. Compare results on the same examples, repeat noisy runs when practical, and report latency and memory alongside the improvement. Treat a change that also altered preprocessing or training budget as a combined intervention.

For example, suppose most missed trucks are eight pixels wide after resize. In a fixed run, annotate how often each one gets a positive and whether a decoded candidate overlaps it before thresholding. If the fine head yields more useful raw boxes but final recall stays flat, inspect score ranking and suppression. The model learned something even if the final number failed to move. If raw boxes do not improve and the input no longer shows the trucks clearly, preserving resolution upstream is a more targeted experiment.

### Self-check

A detector with 50 queries misses trucks in scenes with 12 objects, and only eight slots output confident detections. Should you interpret that as a 50-query capacity failure?

<details>
<summary>Show answer and explanation</summary>

The count alone is below the hard limit. Inspect the missing objects at input resolution, their matches during training and low-confidence raw outputs. More queries can change optimization, but this example does not establish that the output count is the binding constraint.

</details>

## Further reading

- [Andrej Karpathy: A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/) for inspecting inputs and establishing a tiny baseline.

- [Jay Alammar: A Visual and Interactive Guide to the Basics of Neural Networks](https://jalammar.github.io/visual-interactive-guide-basics-neural-networks/) for tracing predictions and updates in small examples.

- [Google Research: Deep Learning Tuning Playbook](https://github.com/google-research/tuning_playbook) for experiment design and incremental comparisons.

- [Dive into Deep Learning: Anchor Boxes](https://d2l.ai/chapter_computer-vision/anchor.html) for assignment and offset targets.

- [DETR](https://arxiv.org/abs/2005.12872) for set prediction, [EfficientNet](https://arxiv.org/abs/1905.11946) for studying depth, width and resolution together, and [Roboflow's illustrated small-object tiling guide](https://roboflow.com/blog/detect-small-objects) for the mechanics of slicing and merging.
