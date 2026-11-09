# Tokens, attention, Transformers and vision Transformers

[All training](index.md) · [Source coverage](sources.md)

A model reading a sentence or a picture receives a collection of input units. A word may depend on another word far away, and one image patch may need context from another part of the scene. Attention computes a different weighted combination of available information for each position.

<details>
<summary>Jump to a concept</summary>

- [Tokens and embeddings](#tokens-and-embeddings)

- [Attention from shapes](#attention-from-shapes)

- [Order, heads and architecture](#order-heads-and-architecture)

- [Vision Transformers](#vision-transformers)

- [What attention does not prove](#what-attention-does-not-prove)

- [Seeing a mask change the computation](#seeing-a-mask-change-the-computation)

</details>

## Tokens and embeddings

Before the model can compare positions, it needs a representation for each input unit. A text tokenizer assigns IDs to units that may be subwords or byte-based pieces rather than whole words. A learned embedding table turns those IDs into vectors. This also explains why text length in characters is not the same as sequence length: unusual strings and different languages may produce different token counts. Word2vec provides an earlier example of learning vectors through context prediction or discrimination; its training objective determines which similarities are useful, and its static word vectors do not resolve every context-dependent meaning.

## Attention from shapes

In a full attention layer, the weights in the opening example are computed from the input. For N token vectors collected in X, learned projections produce queries Q, keys K and values V. The operation is `softmax(Q K^T / sqrt(d_k) + mask) V`. The Q–K comparison produces a weight for each available position; multiplying by V combines the content at those positions. Self-attention creates all three projections from the same sequence, but they are generally different tensors. Cross-attention uses a separate memory for keys and values: a translation decoder, for example, queries the encoder’s representation.

The division by sqrt(d_k) happens before softmax. Under common initialization assumptions it moderates the growth in score variance as key dimension increases, helping avoid an excessively sharp distribution. Multiplying the result after softmax would change its magnitude rather than serve the same purpose. Masks change which positions are available: a causal mask excludes future positions, while a padding mask excludes absent tokens. A mask broadcast along the wrong axis can leave the output shape unchanged while letting forbidden information through.

### Build the weights before multiplying the values

Start with one two-dimensional query `[1, 0]` and keys `[1, 0]`, `[0, 1]` and `[−1, 0]`. The dot products are 1, 0 and −1. After division by the square root of 2, softmax exponentiates the three scaled scores and divides each by their sum. This gives positive weights that add to one. The first position receives the most weight because its key aligns best with the query.

Give the three positions scalar values of 10, 20 and 30. The output is the weighted sum of those numbers. Now mask the third position. Its weight becomes zero and the remaining weights are renormalized. The output can change even if the first two scores and all the values stay fixed, because the set competing for weight changed.

| Change one part | What can change in the result |
| --- | --- |
| Change a key while keeping the query fixed | That position's score and the distribution across positions |
| Change a value while keeping scores and masks fixed | The content of the sum, with the same weights |
| Mask a position | Which positions contribute and how the remaining weights are normalized |

In a real layer there are many queries, and the values are vectors. The same calculation runs for each query. Tracking the score matrix as query positions by key positions is especially helpful when constructing masks.

## Separating where attention looks from what it reads

Suppose attention has assigned three input positions weights of 0.1, 0.7 and 0.2. Their scalar values are 1, 5 and 0. The weighted sum is 3.6.

![Change a value. Keep the attention. Key/value A: 0.1; Key/value B: 0.7; Key/value C: 0.2](assets/dl-attention-toy.svg)

Now change only the middle value from 5 to 2. With those weights unchanged, the result becomes 1.5. The example separates two jobs inside attention: queries and keys determine the weights, while values supply the content being combined.

```python
import numpy as np

weights = np.array([0.1, 0.7, 0.2])
values = np.array([1.0, 5.0, 0.0])
print(round(float(weights @ values), 2))
values[1] = 2.0
print(round(float(weights @ values), 2))
```

This prints:

```text
3.6
1.5
```

This small weighted sum is the last step of attention. The rest of the layer explains how the model learns the projections and produces the weights.

### Self-check

Keep Q, K and the mask fixed, and change only V. What can change in that attention operation?

- A. The weighted output, with the same weights

- B. The weights, with the same output guaranteed

- C. The mask only

- D. The QK scores only

<details>
<summary>Show answer and explanation</summary>

**A. The weighted output, with the same weights**

Q, K and the mask determine the weights. V supplies the content of the weighted sum.

</details>

Change a key or a value and compare the attention weights with the weighted output. [Attention map playground](../playgrounds/attention-map.html)

## Order, heads and architecture

The comparisons alone do not tell the model where a token appeared. Ordinary self-attention without positional information is permutation equivariant: rearranging the inputs rearranges the corresponding outputs. Pooling can then produce an invariant summary. Absolute or relative positions, including rotary schemes, introduce order or geometry in different ways. Multiple heads allow different learned projections and interaction maps, although that does not guarantee a distinct interpretable role for every head.

A Transformer block also includes feedforward layers, residual connections and normalization. An encoder typically permits bidirectional context. An autoregressive decoder uses causal attention, and an encoder-decoder architecture additionally connects decoder queries to encoder memory. “Decoder” names an architectural role and does not mean every decoder performs text generation. A DETR decoder produces object representations through a related but task-specific design.

## Vision Transformers

For an image, patches can play the role of tokens. A Vision Transformer projects each patch into a vector and applies attention to the resulting sequence. A class token or pooling can summarize the image; a dense task can instead use the spatial tokens. Patch size therefore affects both sequence length and the detail directly represented by each input token. Doubling image height and width at fixed patch size gives roughly four times as many tokens, and the pairwise score work in full attention can grow by about sixteen times. Actual memory and latency also depend on the implementation.

Changing resolution changes the spatial token grid and may require positional adaptation. Padding, interpolation and windowing rules must match the implementation. Swin uses local windows, shifted interaction patterns and hierarchical feature scales to reduce cost and build multiscale representations. CNNs encode stronger local weight-sharing structure; ViTs offer flexible long-range interaction. Data, pretraining and compute determine the actual tradeoff.

### How image size turns into a sequence length

With non-overlapping 16-by-16 patches, a 224-by-224 image gives a 14-by-14 patch grid, or 196 patch tokens. Doubling both image dimensions gives a 28-by-28 grid, or 784 patch tokens. Ignoring special tokens, full attention compares about 38,416 pairs in the first case and 614,656 in the second. The number of tokens grows fourfold and the pair count grows sixteenfold. This calculation describes the number of score entries, rather than a measured runtime.

The resolution can still be worthwhile if it preserves a small object that would disappear after resize. Decide what spatial evidence the downstream task needs, then measure the impact of resolution on quality, memory and throughput. Local windows and hierarchical stages change which pairs are compared and how information travels across the image.

### Self-check

With a fixed patch size, you double the image width and height. Ignoring special tokens, how many times more score entries does full attention compute?

- A. 2

- B. 4

- C. 16

- D. 8

<details>
<summary>Show answer and explanation</summary>

**C. 16**

There are four times as many patches. The number of query–key pairs scales with the square of the token count, so it grows by 4² = 16.

</details>

## What attention does not prove

An attention heatmap is a pattern of aggregation, not an automatic causal explanation or a segmentation mask. Global receptive access does not guarantee a tiny object remains detectable after patchification and preprocessing. Model output can attend to context shortcuts. Evaluate controlled occlusions and example-level behavior if making interpretability claims.

## Seeing a mask change the computation

To inspect attention beyond the weighted sum, use one query and three short key vectors. Compute their dot products, scale them and apply softmax, then compare the weighted values. Masking one key should remove its contribution and redistribute the remaining weights. This small calculation is also a practical way to detect an axis error that a larger model’s output shape would not reveal.

<details>
<summary>Original source references and provenance</summary>

Original teaching text covering the cited topics, not a verbatim mirror. These references are provenance; no external reading is required to use this chapter.

- [https://cs231n.stanford.edu/slides/2025/lecture_8.pdf](https://cs231n.stanford.edu/slides/2025/lecture_8.pdf)

- [https://jalammar.github.io/illustrated-transformer/](https://jalammar.github.io/illustrated-transformer/)

- [https://jalammar.github.io/illustrated-word2vec/](https://jalammar.github.io/illustrated-word2vec/)

- [https://lilianweng.github.io/posts/2018-06-24-attention/](https://lilianweng.github.io/posts/2018-06-24-attention/)

</details>
