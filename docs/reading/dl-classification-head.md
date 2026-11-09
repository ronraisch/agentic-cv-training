# Classification heads on CNN and Transformer embeddings

[Chapter index](index.md) · [Source coverage](sources.md)

A model sees a crop and returns a vector. Your job is to decide whether the crop shows a car, a truck or background. The **backbone** computes the representation. The **head** is the task-specific part that turns that representation into an answer. Start by identifying what one training label refers to. Here it refers to the whole crop.

For the distinction between a spatial embedding and a pooled vector, see [Feature maps: what the backbone keeps](dl-feature-maps.md).

<details>
<summary>Jump to a concept</summary>

- [One vector, one decision](#one-vector-one-decision)

- [CNN and Transformer inputs](#cnn-and-transformer)

- [What a frozen linear probe tells you](#linear-probe)

</details>

## One vector, one decision

Suppose an encoder produces one 768-dimensional vector per crop. A linear head learns one row of 768 weights and a bias for each of the three classes. Each row produces one score, or logit. For a crop embedding *x*, a weight matrix *W* and bias vector *b*, the whole head is

$$
z=Wx+b
$$

The scores can be negative and their sum need not be one. With mutually exclusive labels, cross-entropy trains the three logits together. At inference, softmax gives a distribution across the classes and the largest logit chooses the class.

If an image can contain both a truck and a car, one label no longer excludes the other. A multi-label head can have one independent logit per category, trained with a binary loss for each known label. Apply a sigmoid and decide a threshold for each category. A missing label can mean either “absent” or “unknown” depending on your dataset. That distinction changes which loss terms you can trust.

## CNN and Transformer inputs

| Backbone output | How the head gets a vector | What it throws away |
| --- | --- | --- |
| CNN feature map, B × D × H × W | Global average pooling over H and W gives B × D | The explicit coordinates of activations |
| Original ViT output, B × (N+1) × D | Read the contextualized class token | The explicit patch-by-patch output |
| Spatial ViT tokens, B × N × D | Mean-pool the valid patches if that matches your head design | Which patch supplied a feature |

A crop head can reuse a detector's proposals. First obtain a representation per region, from a crop encoder or by pooling a region of a shared map. Then classify each proposal independently. Changing that classifier can recover misclassified proposals, but a missed proposal never reaches the classifier.

## What a frozen linear probe tells you

Freeze the backbone, train only the head and compare on held-out scenes. If a linear head separates pickups from vans, the pretrained representation already exposes a useful direction. If it fails, inspect nearest neighbors and examples before trying a larger head. A poor crop, an image resolution mismatch and a frozen feature that ignores the distinguishing detail can produce similar scores. A nonlinear head can learn more complex boundaries if you have enough labeled examples. Fine-tuning also changes the embedding itself, so it answers a different question.

The same linear layer can receive vectors from either family. The difference is how you reduce the backbone's output.

```python
from torch import nn

head = nn.Linear(768, 3)
cnn_logits = head(cnn_map.mean(dim=(-2, -1)))  # [B, 768, H, W]
vit_logits = head(vit_tokens[:, 0])            # [B, N + 1, 768], CLS first
```

The shared layer here only illustrates the shape contract. Train or validate a head separately for each backbone. Matching dimensions do not mean the two representations use the same coordinates.

### Self-check

A classifier distinguishes trucks and cars on cropped proposals, but misses every truck in one camera view. What do you inspect first?

<details>
<summary>Show answer and explanation</summary>

Check whether the proposal stage produced usable truck crops in that view. If it did, inspect those crops and their classifier logits. If it did not, retraining the crop classifier cannot fix those misses.

</details>
