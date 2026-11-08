# Bias, variance, dataset shift and trustworthy validation

[All training](index.md) · [Source coverage](sources.md)

**Reading is for you; page completion is optional.** If you can explain the concepts and answer the mentor's questions yourself, that is enough. Use these pages and the course videos to deepen understanding during the exercises with your approved agent. [Learning route and manual-work boundaries](index.md).

### On this page

- [Three meanings of bias](#three-meanings-of-bias)

- [Bias and variance in prediction](#bias-and-variance-in-prediction)

- [How datasets acquire bias](#how-datasets-acquire-bias)

- [Shift and drift](#shift-and-drift)

- [Split by the actual independence unit](#split-by-the-actual-independence-unit)

- [Uncertainty and comparison](#uncertainty-and-comparison)

- [During the project](#during-the-project)

## Three meanings of bias

An additive model intercept is sometimes called a bias. Statistical estimation bias describes a systematic difference between an estimator's expectation and its target. Dataset and human biases concern how observations, labels and decisions represent the intended population. These are distinct ideas: reducing model approximation bias does not fix a biased sample or a biased labeling policy.

## Bias and variance in prediction

For squared-error regression, expected prediction error can be decomposed into squared bias, variance and irreducible noise under stated assumptions. A rigid model can underfit even its training set. A very flexible model can fit noise and vary strongly between training samples. More data often reduces variance; a better representation can reduce approximation bias. The familiar U-shaped curve is a teaching pattern, not a universal law for every modern model and training regime. Diagnose with learning curves and independent errors instead of assigning a model to a slogan.

## How datasets acquire bias

Reporting bias arises when recorded events differ from actual frequencies: a log of reported incidents omits unreported ones. Historical bias carries earlier inequities or policies into labels. Automation bias is undue trust in an automated suggestion; annotators accepting every SAM mask can reinforce its systematic misses. Selection bias comes from who or what is sampled. Coverage bias leaves parts of the target population out; nonresponse bias reflects who fails to provide data; sampling bias reflects a nonrepresentative collection process. Group attribution bias generalizes properties of individuals to groups or assumes group averages describe each individual. Implicit assumptions can influence category definitions and ambiguous labels.

For imagery, imagine a vehicle dataset collected only in clear weather and labeled from detector proposals. It underrepresents clouds and occlusion, and objects missed by the proposal model may never be reviewed. Add random spatial audits rather than inspecting predictions alone. Record sensor, geography, time and annotation protocol so performance can be stratified. A balanced class count does not guarantee representative nuisance conditions or equivalent label quality.

## Shift and drift

Covariate shift changes P(x), label/prior shift changes P(y), and concept shift changes P(y|x). Their clean theoretical forms hold other distributions fixed; real deployments can combine them. Data drift describes observed distribution change over time, while performance degradation requires labels or an appropriate audit to establish. A different embedding histogram is an alert, not proof of reduced recall. Monitor input quality, scores, subgroup errors and delayed labels. Changing class prevalence can change precision even if class-conditional score behavior stays the same.

## Split by the actual independence unit

Training fits parameters, validation chooses models and policies, and a final held-out test estimates the chosen system's performance. Split videos, donors, sessions, geographic neighborhoods or time periods according to the intended deployment. Randomly splitting near-duplicate tiles or neighboring frames leaks scene information. Perform imputation, normalization, feature selection and calibration within each training fold. Use nested cross-validation if reporting performance after substantial hyperparameter search with no separate untouched test set.

Stratification preserves class proportions but does not enforce group independence. A temporal split asks about future data and may legitimately expose distribution shift. The same benchmark can become an implicit validation set through repeated manual decisions. Keep an independent final check and record what influenced model selection.

## Uncertainty and comparison

A bootstrap resamples observed units with replacement to estimate variability. If frames are correlated, bootstrap videos or sessions rather than individual frames. Cross-validation estimates generalization under a split design and supports model selection; it is not the same operation as bootstrapping. Compare two systems on the same held-out units and report paired differences, effect sizes and uncertainty. A small p-value is not a large practical improvement, and repeated unplanned testing increases false discoveries.

For an independent Bernoulli proportion p estimated from n trials, the rough standard error is `sqrt(p(1-p)/n)`. This approximation can be poor for small n or rare events; use suitable intervals and report counts. Zero misses among n positives does not prove perfect recall. Correlation reduces effective sample size. Decide test-set size from the precision needed around the operating point, not from a fixed percentage of the whole dataset.

## During the project

Have the agent propose three splits and try to falsify each with a leakage example. Write a short audit of the chosen split and manually trace a few sample IDs through it. Bring to the mentor a failure that survives a better split, not just the highest score from an easier split.

### Original source references and provenance

Original teaching text covering the cited topics, not a verbatim mirror. These references are provenance; no external reading is required to use this chapter.

- [http://scott.fortmann-roe.com/docs/BiasVariance.html](http://scott.fortmann-roe.com/docs/BiasVariance.html)

- [http://www.r2d3.us/visual-intro-to-machine-learning-part-1/](http://www.r2d3.us/visual-intro-to-machine-learning-part-1/)

- [http://www.r2d3.us/visual-intro-to-machine-learning-part-2/](http://www.r2d3.us/visual-intro-to-machine-learning-part-2/)

- [https://abhishek-reddy.medium.com/detecting-and-managing-data-distribution-shifts-in-the-mlops-lifecycle-for-machine-learning-models-1ea33ce84c3c](https://abhishek-reddy.medium.com/detecting-and-managing-data-distribution-shifts-in-the-mlops-lifecycle-for-machine-learning-models-1ea33ce84c3c)

- [https://datascience.stackexchange.com/questions/32264/what-is-the-difference-between-bootstrapping-and-cross-validation](https://datascience.stackexchange.com/questions/32264/what-is-the-difference-between-bootstrapping-and-cross-validation)

- [https://daviddalpiaz.github.io/r4sl/biasvariance-tradeoff.html](https://daviddalpiaz.github.io/r4sl/biasvariance-tradeoff.html)

- [https://developers.google.com/machine-learning/crash-course/fairness/types-of-bias](https://developers.google.com/machine-learning/crash-course/fairness/types-of-bias)

- [https://developers.google.com/machine-learning/crash-course/overfitting/dividing-datasets#additional_problems_with_test_sets](https://developers.google.com/machine-learning/crash-course/overfitting/dividing-datasets#additional_problems_with_test_sets)

- [https://developers.google.com/machine-learning/crash-course/overfitting/imbalanced-datasets](https://developers.google.com/machine-learning/crash-course/overfitting/imbalanced-datasets)

- [https://developers.google.com/machine-learning/crash-course/overfitting/overfitting](https://developers.google.com/machine-learning/crash-course/overfitting/overfitting)

- [https://github.com/rasbt/stat479-machine-learning-fs19/blob/master/08_model-eval-1/08-model-eval-1-intro__notes.pdf](https://github.com/rasbt/stat479-machine-learning-fs19/blob/master/08_model-eval-1/08-model-eval-1-intro__notes.pdf)

- [https://github.com/rasbt/stat479-machine-learning-fs19/blob/master/09_eval2-ci/09-eval2-ci__notes.pdf](https://github.com/rasbt/stat479-machine-learning-fs19/blob/master/09_eval2-ci/09-eval2-ci__notes.pdf)

- [https://github.com/rasbt/stat479-machine-learning-fs19/blob/master/10_eval3-cv/10-eval3-cv__notes.pdf](https://github.com/rasbt/stat479-machine-learning-fs19/blob/master/10_eval3-cv/10-eval3-cv__notes.pdf)

- [https://github.com/rasbt/stat479-machine-learning-fs19/blob/master/11_eval4-algo/11-eval4-algo__notes.pdf](https://github.com/rasbt/stat479-machine-learning-fs19/blob/master/11_eval4-algo/11-eval4-algo__notes.pdf)

- [https://medium.com/data-science/understanding-the-bias-variance-tradeoff-165e6942b229](https://medium.com/data-science/understanding-the-bias-variance-tradeoff-165e6942b229)
