# Learning paradigms, probability, estimation and linear models

[All training](index.md) · [Source coverage](sources.md)

## A straight line can bend.

Fit y = 1 + 2x². Is this a linear model? It is linear in its fitted coefficients, even though the curve bends in x.

![A straight line can bend. x; x²; y = 1 + 2x²](assets/ml-foundations-toy.svg)

| Notice | Interpret | Check |
| --- | --- | --- |
| 0 → 0 → 1 | 1 → 1 → 3 | 2 → 4 → 9 |

<details>
<summary>Reveal the catch</summary>

The representation changes the question the learner can answer.

</details>

**Try it in 60 seconds:** Compare fitting x with fitting [x, x²]. Keep the held-out inputs identical.

Read for understanding, not page completion. Skip what you can already explain.

<details>
<summary>Jump to a concept</summary>

- [Define the task and the data-generating process](#define-the-task-and-the-data-generating-process)

- [Probability and estimation](#probability-and-estimation)

- [Linear and polynomial regression](#linear-and-polynomial-regression)

- [Logistic regression and decisions](#logistic-regression-and-decisions)

- [Dimensionality and feature choices](#dimensionality-and-feature-choices)

- [Connect to your experiment](#connect-to-your-experiment)

</details>

## Define the task and the data-generating process

Supervised learning uses input/target pairs; classification predicts discrete labels and regression predicts numerical quantities. Unsupervised learning seeks structure such as density or clusters without those targets. Self-supervised learning creates training signals from the data, such as predicting masked content or matching augmented views. Semi-supervised learning combines labeled and unlabeled examples. Reinforcement learning optimizes action decisions through rewards and interaction. These describe how supervision is obtained, not a fixed list of architectures.

A parameter is fitted from data, such as a linear model's weights. A hyperparameter controls model structure or learning, such as regularization strength or neighbor count. An instance-based method such as KNN retains examples and predicts from nearby cases; a model-based method compresses evidence into fitted parameters. Both can overfit and both require a defined input representation.

## Probability and estimation

A random variable describes possible outcomes and their probabilities. Conditional probability distinguishes `P(y|x)` from `P(x|y)`. Bayes' rule combines a likelihood with a prior to obtain a posterior. Maximum likelihood chooses parameters maximizing the observed-data likelihood. Maximum a posteriori estimation also includes a prior: `argmax log p(data|theta) + log p(theta)`. A point estimate is not the full posterior distribution.

An estimator is unbiased if its expectation over repeated datasets equals the true quantity. This is not the same as a dataset being representative or socially unbiased. An estimator with some bias can have lower mean-squared error by reducing variance. State which randomness is being averaged over when discussing an expected error or confidence interval.

## Linear and polynomial regression

Linear regression predicts `y_hat = w^T x + b`. With independent Gaussian observation noise of fixed variance, maximizing likelihood corresponds to minimizing squared residuals. The gradient of mean squared loss with respect to w is proportional to `X^T(Xw-y)`. Gradient descent subtracts a learning-rate-scaled gradient. Solve least squares with QR/SVD or an appropriate numerical solver rather than blindly forming a matrix inverse. Collinear features make individual coefficients unstable even when predictions remain similar.

Polynomial regression adds features such as x squared and x cubed while remaining linear in its fitted coefficients. More features increase flexibility, but extrapolation can become unstable. Fit feature transforms and normalization only on training folds. Ridge adds an L2 penalty and shrinks weights; lasso adds L1 and can set some coefficients to zero. Under suitable likelihood assumptions these correspond to Gaussian and Laplace priors. The intercept is often left unpenalized. Feature scaling changes how a shared penalty treats each coefficient.

## Logistic regression and decisions

A binary logistic model maps a linear score through a sigmoid. Its negative log likelihood is binary cross entropy. A linear score of zero gives probability 0.5, but the best operational decision threshold depends on error costs and prevalence. Train the scoring model and choose the threshold on validation data; do not choose it from the final test labels. For multiple mutually exclusive classes, softmax produces normalized class scores and multiclass cross entropy trains them. Independent sigmoid outputs suit multilabel tasks where several labels can be true.

Numerically stable implementations operate on logits rather than explicitly taking a log of an underflowed probability. A large classification margin is not automatically a calibrated probability. Compare calibration on independent data if a downstream policy uses probabilities as expected costs.

## Dimensionality and feature choices

In high dimensions, a fixed number of observations covers a tiny fraction of the possible input space. Distances can become less discriminating and irrelevant features can overwhelm useful ones. Domain features, regularization, more representative data and learned embeddings can help, but each changes assumptions. Feature selection uses labels when evaluating predictive usefulness, so it belongs inside the cross-validation pipeline. A feature selected using all labels leaks information even if the final estimator is fitted only on a training subset.

## Connect to your experiment

For tracklet motion, define the target and decision unit, derive candidate velocity/shape features, and build a simple linear baseline. Explain which feature encodes actual motion and which may identify a camera or collection session. Ask your agent for a counterexample where a seemingly helpful feature becomes leakage, then test it yourself.

<details>
<summary>Original source references and provenance</summary>

Original teaching text covering the cited topics, not a verbatim mirror. These references are provenance; no external reading is required to use this chapter.

- [http://cs.stanford.edu/people/karpathy/convnetjs/demo/classify2d.html](http://cs.stanford.edu/people/karpathy/convnetjs/demo/classify2d.html)

- [http://cs229.stanford.edu/notes2019fall/cs229-notes1.pdf](http://cs229.stanford.edu/notes2019fall/cs229-notes1.pdf)

- [http://deeplearning.stanford.edu/tutorial/](http://deeplearning.stanford.edu/tutorial/)

- [http://www.ai.mit.edu/courses/6.867-f04/lectures/lecture-2.pdf](http://www.ai.mit.edu/courses/6.867-f04/lectures/lecture-2.pdf)

- [http://www.ai.mit.edu/courses/6.867-f04/lectures/lecture-3.pdf](http://www.ai.mit.edu/courses/6.867-f04/lectures/lecture-3.pdf)

- [http://www.ai.mit.edu/courses/6.867-f04/lectures/lecture-5.pdf](http://www.ai.mit.edu/courses/6.867-f04/lectures/lecture-5.pdf)

- [https://bjlkeng.github.io/posts/probabilistic-interpretation-of-regularization/](https://bjlkeng.github.io/posts/probabilistic-interpretation-of-regularization/)

- [https://cs231n.github.io/classification/](https://cs231n.github.io/classification/)

- [https://cs231n.github.io/linear-classify/](https://cs231n.github.io/linear-classify/)

- [https://cs231n.stanford.edu/slides/2025/lecture_2.pdf](https://cs231n.stanford.edu/slides/2025/lecture_2.pdf)

- [https://developers.google.com/machine-learning/crash-course/linear-regression/gradient-descent-exercise](https://developers.google.com/machine-learning/crash-course/linear-regression/gradient-descent-exercise)

- [https://developers.google.com/machine-learning/crash-course/linear-regression/quiz](https://developers.google.com/machine-learning/crash-course/linear-regression/quiz)

- [https://developers.google.com/machine-learning/intro-to-ml/what-is-ml](https://developers.google.com/machine-learning/intro-to-ml/what-is-ml)

- [https://drive.google.com/file/d/13_HENQfNwAG1dOlZHsy4De7wJbm9vNYx/view](https://drive.google.com/file/d/13_HENQfNwAG1dOlZHsy4De7wJbm9vNYx/view)

- [https://medium.com/datadriveninvestor/l1-l2-regularization-7f1b4fe948f2](https://medium.com/datadriveninvestor/l1-l2-regularization-7f1b4fe948f2)

- [https://see.stanford.edu/materials/aimlcs229/cs229-notes5.pdf](https://see.stanford.edu/materials/aimlcs229/cs229-notes5.pdf)

- [https://www.cs.cmu.edu/~hn1/documents/machine-learning/notes.pdf](https://www.cs.cmu.edu/~hn1/documents/machine-learning/notes.pdf)

- [https://www.geeksforgeeks.org/machine-learning/curse-of-dimensionality-in-machine-learning/](https://www.geeksforgeeks.org/machine-learning/curse-of-dimensionality-in-machine-learning/)

- [https://www.geeksforgeeks.org/machine-learning/difference-between-supervised-and-unsupervised-learning/](https://www.geeksforgeeks.org/machine-learning/difference-between-supervised-and-unsupervised-learning/)

- [https://www.ibm.com/think/topics/machine-learning-types](https://www.ibm.com/think/topics/machine-learning-types)

</details>
