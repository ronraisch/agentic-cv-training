# Training and inference fundamentals

A tensor has shape, dtype, device and possibly an autograd graph. HWC is not CHW: permute changes
axis meaning; reshape alone does not. Explain convolution channels/stride/padding, receptive fields,
residual paths and normalization using one architecture, not an exhaustive architecture history.

For a training batch: place inputs/targets on the right device, clear gradients according to the
accumulation policy, compute predictions/loss, backward and step. Gradients accumulate by default.
A detach/NumPy conversion in the loss path may cut learning. Check component gradient norms and
parameter updates, not just a decreasing scalar loss. Match logits/probabilities, target dtype,
missing-label masks and reduction semantics to the loss.

Model train/eval state affects modules such as dropout and BatchNorm. It does not switch off
autograd. Use eval plus an appropriate no-grad/inference scope for inference. Restore caller state
on errors when the interface promises that behavior. Retained GPU outputs can retain graphs;
store only needed detached CPU values for reports. Seeds do not guarantee equality across all
versions/devices/kernels.

Debug in order: visualize a batch/GT; inspect shapes/ranges; run one forward/backward; verify an
update; overfit two to eight fixed examples without augmentation; save/reload a fresh instance;
then enlarge data or compute. Tiny overfit tests the pipeline, not generalization.

A checkpoint needs architecture/config, state_dict, class map, preprocessing, data provenance and
selection rule. Optimizer state matters for true training resumption, not ordinary inference.
Partial loading can conceal an uninitialized head: report missing/unexpected keys explicitly.
Record what was actually trained when using a frozen encoder and a small head.

## Attention and representation foundations

Attention scores compare projected queries and keys and aggregate values; explain shapes and
scaling with a toy example. Self-attention without positional information is permutation-equivariant
at token level, not a general claim that every transformer output is invariant. In ordinary decoder
cross-attention, decoder states supply queries and encoder memory supplies keys/values.
Patch resolution, pooling and spatial/temporal information affect small-object and event evidence.

Understand supervised versus self-supervised objectives, embeddings, transfer learning and
contrastive alignment at concept level. A text-aligned representation can support new descriptions,
but similarity is not a verified answer probability. Full RNN/LSTM gates, generative modeling,
distributed-training implementation and architecture-by-architecture derivations are optional.

Self-check: trace one loss to a parameter update; explain eval versus no-grad; compare pooled frame
presence evidence with evidence needed to establish a temporal event.

Required companion: [embeddings, VLMs, open-vocabulary detection and open-model usage](07-open-models.md).
Use its shared introduction instead of repeating the representation basics here.
