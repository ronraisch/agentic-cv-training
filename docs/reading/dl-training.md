# Neural networks, backpropagation, optimization and reliable training

[All training](index.md) · [Source coverage](sources.md)

**Reading is for you; page completion is optional.** If you can explain the concepts and answer the mentor's questions yourself, that is enough. Use these pages and the course videos to deepen understanding during the exercises with your approved agent. [Learning route and manual-work boundaries](index.md).

### On this page

- [Layers and representational capacity](#layers-and-representational-capacity)

- [Loss and backpropagation](#loss-and-backpropagation)

- [Optimization and regularization](#optimization-and-regularization)

- [Initialization, activations and normalization](#initialization-activations-and-normalization)

- [A training loop you can defend](#a-training-loop-you-can-defend)

- [Checkpoint and operational evidence](#checkpoint-and-operational-evidence)

- [Learn while debugging](#learn-while-debugging)

- [Softmax derivatives and label conventions](#softmax-derivatives-and-label-conventions)

## Layers and representational capacity

A linear layer applies an affine transformation `h = Wx+b`. Composing affine layers without nonlinearities is still an affine transformation, regardless of depth. Activations such as ReLU, sigmoid and tanh change the function family and gradient behavior. A network with sufficient capacity can approximate broad function classes under a theorem's assumptions, but that theorem does not promise a useful optimizer, a small dataset or good extrapolation.

## Loss and backpropagation

A loss compares predictions to targets and defines the optimization objective. Classification cross entropy, regression squared/absolute loss and metric-learning losses express different goals. Backpropagation uses the chain rule to propagate derivatives through a computational graph. At a node with multiple consumers, contributions to its derivative add. For y=wx and squared error L=(y-t)^2/2, the derivative with respect to w is (wx-t)x. Derive this tiny example and check it with finite differences before treating autograd as a black box.

A gradient check perturbs a parameter and compares the numerical change to the analytic derivative, using a small deterministic double-precision example where possible. Kinks, random dropout, state updates and a poor step size can invalidate a naive comparison. A detached tensor or non-differentiable path can quietly stop learning even though the loss still prints.

## Optimization and regularization

Minibatch SGD estimates gradients from subsets. Learning rate controls update size; momentum accumulates directional history; adaptive methods such as Adam scale updates using moment estimates. A schedule changes the rate over training. Batch size affects optimization noise, memory, iteration count and hardware efficiency, so “same epochs” does not necessarily mean the same experiment.

L2 regularization adds a weight-dependent term to the loss. Decoupled weight decay applies a direct shrinkage step; AdamW separates that from adaptive gradient scaling. L2 and decay are equivalent only under restricted optimizer formulations. Dropout samples a subnetwork-like mask during training and uses a defined deterministic scaling convention at inference. Augmentation encodes assumptions about which image changes should preserve the label. A horizontal flip can be inappropriate for text recognition even if useful for generic object classification.

## Initialization, activations and normalization

Poorly scaled initialization can make activations or gradients vanish or explode across depth. Variance-aware initializations help under their assumptions. Sigmoid saturates at large magnitudes; ReLU has zero gradient for negative inputs and can produce inactive units. BatchNorm normalizes using batch statistics during training and commonly stored running statistics during inference; LayerNorm normalizes a different set of dimensions and does not use the same running-batch mechanism. Check the actual model implementation, especially for small batches or domain shifts.

## A training loop you can defend

Load the batch, move data and model to compatible devices, zero gradients, compute predictions and loss, backpropagate and step the optimizer. Gradient accumulation deliberately postpones zeroing/stepping and needs consistent loss scaling. Set train/eval mode for the intended behavior. `eval()` changes module behavior; `no_grad()` or `inference_mode()` controls gradient recording and associated overhead. Neither alone does the other's job.

Overfit a tiny clean subset as a diagnostic, inspect label and tensor shapes, verify that intended parameters change and compare train/validation curves. A decreasing loss is insufficient if labels are shifted by one or preprocessing differs at inference. Mixed precision reduces some costs but introduces scaling and numerical considerations. Record seeds, versions and nondeterministic operations; a seed alone does not guarantee identical results on every machine.

## Checkpoint and operational evidence

Save architecture/config identity, model weights, preprocessing and label mapping. A resumable checkpoint also needs optimizer/scheduler and relevant state. Reload in a fresh process, run a new input and compare outputs with an appropriate tolerance. Do not confuse a Python object still resident in memory with a successful load. For the inference-only handover notebook, preserve all necessary preprocessing, construction, checkpoint loading and postprocessing without importing project internals.

## Learn while debugging

Ask the agent for a falsifiable diagnosis rather than a list of generic tips. Change one controlled factor, show gradients or outputs that support the explanation and retain an error case. Before the mentor session, explain one backward path and one production inference path yourself. “The code uses PyTorch” does not establish that the chosen loss, weights or mode actually reach the executed consumer.

## Softmax derivatives and label conventions

For s_i=exp(z_i)/sum_j exp(z_j), the Jacobian is ds_i/dz_j=s_i(delta_ij-s_j). With a one-hot target and cross entropy, the logit gradient simplifies to s−y. Subtracting the maximum logit before exponentiating preserves probabilities and improves numerical stability. A softmax assumes mutually exclusive alternatives, whereas independent binary labels need a different likelihood. Verify that target indices and class order survive dataset export and checkpoint loading.

### Original source references and provenance

Original teaching text covering the cited topics, not a verbatim mirror. These references are provenance; no external reading is required to use this chapter.

- [http://josh-tobin.com/assets/pdf/troubleshooting-deep-neural-networks-01-19.pdf](http://josh-tobin.com/assets/pdf/troubleshooting-deep-neural-networks-01-19.pdf)

- [http://neuralnetworksanddeeplearning.com](http://neuralnetworksanddeeplearning.com)

- [http://neuralnetworksanddeeplearning.com/chap4.html](http://neuralnetworksanddeeplearning.com/chap4.html)

- [https://cs231n.github.io/optimization-1/](https://cs231n.github.io/optimization-1/)

- [https://cs231n.github.io/optimization-2/](https://cs231n.github.io/optimization-2/)

- [https://cs231n.stanford.edu/slides/2025/lecture_1_part_1.pdf](https://cs231n.stanford.edu/slides/2025/lecture_1_part_1.pdf)

- [https://cs231n.stanford.edu/slides/2025/lecture_1_part_2.pdf](https://cs231n.stanford.edu/slides/2025/lecture_1_part_2.pdf)

- [https://cs231n.stanford.edu/slides/2025/lecture_3.pdf](https://cs231n.stanford.edu/slides/2025/lecture_3.pdf)

- [https://cs231n.stanford.edu/slides/2025/lecture_4.pdf](https://cs231n.stanford.edu/slides/2025/lecture_4.pdf)

- [https://developers.google.com/machine-learning/crash-course/neural-networks/activation-functions](https://developers.google.com/machine-learning/crash-course/neural-networks/activation-functions)

- [https://eli.thegreenplace.net/2016/the-softmax-function-and-its-derivative/](https://eli.thegreenplace.net/2016/the-softmax-function-and-its-derivative/)

- [https://emiliendupont.github.io/2018/01/24/optimization-visualization/](https://emiliendupont.github.io/2018/01/24/optimization-visualization/)

- [https://en.wikipedia.org/wiki/Batch_normalization#Length-Direction_Decoupling](https://en.wikipedia.org/wiki/Batch_normalization#Length-Direction_Decoupling)

- [https://github.com/Jaewan-Yun/optimizer-visualization](https://github.com/Jaewan-Yun/optimizer-visualization)

- [https://twitter.com/itayevron/status/1328421322821693441?s=08](https://twitter.com/itayevron/status/1328421322821693441?s=08)

- [https://twitter.com/ylecun/status/1274782757907030016](https://twitter.com/ylecun/status/1274782757907030016)

- [https://www.cs.toronto.edu/~urtasun/courses/CSC411_Fall16/05_nn.pdf](https://www.cs.toronto.edu/~urtasun/courses/CSC411_Fall16/05_nn.pdf)

- [https://yassin01.medium.com/adam-vs-adamw-understanding-weight-decay-and-its-impact-on-model-performance-b7414f0af8a1](https://yassin01.medium.com/adam-vs-adamw-understanding-weight-decay-and-its-impact-on-model-performance-b7414f0af8a1)
