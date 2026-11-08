# Tokens, attention, Transformers and vision Transformers

[All training](index.md) · [Source coverage](sources.md)

## Change a value. Keep the attention.

A query gives three tokens weights 0.1, 0.7 and 0.2. With scalar values 1, 5 and 0, the output is 3.6.

![Change a value. Keep the attention. Key/value A: 0.1; Key/value B: 0.7; Key/value C: 0.2](assets/dl-attention-toy.svg)

| Notice | Interpret | Check |
| --- | --- | --- |
| Q and K choose weights | V carries the content | 0.1×1 + 0.7×5 + 0.2×0 = 3.6 |

<details>
<summary>Reveal the catch</summary>

Changing V changes the output without changing these weights. Changing K can change the weights.

</details>

### In code: Keep weights fixed; change the content

```python
import numpy as np

weights = np.array([0.1, 0.7, 0.2])
values = np.array([1.0, 5.0, 0.0])
print(round(float(weights @ values), 2))
values[1] = 2.0
print(round(float(weights @ values), 2))
```

**Expected output:**

```text
3.6
1.5
```

This isolates the weighted-sum step after Q and K have produced attention weights. A full attention layer also computes projections, scores, scaling and softmax.

**Try it in 60 seconds:** Change only the middle value to 2. Compute the new output before running code.

Read for understanding, not page completion. Skip what you can already explain.

<details>
<summary>Jump to a concept</summary>

- [Tokens and embeddings](#tokens-and-embeddings)

- [Attention from shapes](#attention-from-shapes)

- [Order, heads and architecture](#order-heads-and-architecture)

- [Vision Transformers](#vision-transformers)

- [What attention does not prove](#what-attention-does-not-prove)

- [A useful manual example](#a-useful-manual-example)

</details>

## Tokens and embeddings

A tokenizer maps input into discrete units with IDs. Text tokens can be subwords or byte-based pieces, not necessarily whole words. Token count affects sequence length and cost; unusual strings and languages can tokenize differently. An embedding table maps IDs to learned vectors. Word2vec learns word representations from context prediction/discrimination; the objective shapes which similarities the vectors preserve. A static word embedding does not by itself resolve every context-dependent meaning.

## Attention from shapes

For input tokens X with shape N-by-d, learned projections create Q, K and V. Scaled dot-product attention is `softmax(Q K^T / sqrt(d_k) + mask) V`. Q and K determine which items interact; V carries the aggregated content. In self-attention they are projected from the same token sequence, not generally equal tensors. In cross-attention, queries come from the sequence being updated and keys/values from a separate memory. For a translation decoder, its current states query the encoder's representation.

The scaling is applied before softmax to moderate score variance under common initialization assumptions. Scaling after softmax changes output magnitude instead of the distribution's sharpness. A causal mask blocks future positions. A padding mask blocks absent tokens. A broadcasted mask with the wrong axis can allow forbidden information while producing the expected output shape.

## Order, heads and architecture

Without positional information, ordinary self-attention is permutation equivariant: permuting input tokens permutes corresponding outputs. An aggregate pooled representation may then be invariant. Absolute/relative positions or rotary schemes supply order or geometry in different ways. Multihead attention learns several projections and attention maps; it permits distinct relationships but does not guarantee every head learns a unique interpretable role.

A Transformer block also includes feedforward layers, residual connections and normalization. An encoder typically permits bidirectional context. An autoregressive decoder uses causal attention, and an encoder-decoder architecture additionally connects decoder queries to encoder memory. “Decoder” names an architectural role and does not mean every decoder performs text generation. A DETR decoder produces object representations through a related but task-specific design.

## Vision Transformers

A ViT turns patches into tokens and processes them with attention. Patch size controls sequence length and the granularity of direct input tokens. A class token or pooling summarizes the image for classification; dense tasks may consume spatial tokens. Doubling both image dimensions at fixed patch size roughly quadruples token count and can multiply full attention's pairwise score work by about sixteen. Memory and practical kernels also matter.

Changing resolution changes the spatial token grid and may require positional adaptation. Padding, interpolation and windowing rules must match the implementation. Swin uses local windows, shifted interaction patterns and hierarchical feature scales to reduce cost and build multiscale representations. CNNs encode stronger local weight-sharing structure; ViTs offer flexible long-range interaction. Data, pretraining and compute determine the actual tradeoff.

## What attention does not prove

An attention heatmap is a pattern of aggregation, not an automatic causal explanation or a segmentation mask. Global receptive access does not guarantee a tiny object remains detectable after patchification and preprocessing. Model output can attend to context shortcuts. Evaluate controlled occlusions and example-level behavior if making interpretability claims.

## A useful manual example

Create three two-dimensional keys and a single query, compute the three dot products and softmax weights, then form a weighted sum of values. Change only one value: weights stay fixed but content changes. Change a key: the weights change. Ask your agent to construct a masking bug, then locate it with dimensions and a toy sequence. Bring the hand calculation and a trace through the actual model to the mentor.

<details>
<summary>Original source references and provenance</summary>

Original teaching text covering the cited topics, not a verbatim mirror. These references are provenance; no external reading is required to use this chapter.

- [https://cs231n.stanford.edu/slides/2025/lecture_8.pdf](https://cs231n.stanford.edu/slides/2025/lecture_8.pdf)

- [https://jalammar.github.io/illustrated-transformer/](https://jalammar.github.io/illustrated-transformer/)

- [https://jalammar.github.io/illustrated-word2vec/](https://jalammar.github.io/illustrated-word2vec/)

- [https://lilianweng.github.io/posts/2018-06-24-attention/](https://lilianweng.github.io/posts/2018-06-24-attention/)

</details>
