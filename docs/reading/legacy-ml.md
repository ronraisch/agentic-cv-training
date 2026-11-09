# Original ML training handout

[Chapter index](index.md) · [Source coverage](sources.md)

**Reading is for you; page completion is optional.** If you can explain the concepts and answer the mentor's questions yourself, that is enough. Use these pages and the course videos to deepen understanding during the exercises with your approved agent. [Learning route and manual-work boundaries](index.md).

**Historical handout, preserved in full.** This records the older learner text; historical schedules and instructions to complete every reading or old assignment are superseded by the stage syllabus above. Reading links now point to local explanations. Video links retain their source destinations. The current required exercises are linked from the stage syllabus.

Machine Learning Training Program

Topics and Exercises

Below is a detailed syllabus by topic with questions and notes for each topic.

Most topics have a complementary mini-exercise. After covering the topics in the links below, make sure to complete the necessary mini-exercise for that topic.

All exercises should be completed in the provided Jupyter notebook.

The data for all exercises can be found here: [data](https://drive.google.com/drive/folders/1P1MFkVfQTT8F4g3D0ejp5ocVDMyFeZLc?usp=sharing)

All required datasets are also provided.

Please make sure to make a local copy of all notebooks and datasets!

[Machine Learning Training Program](legacy-ml.md)

[Topics and Exercises](legacy-ml.md)

[1. Supervised Learning and Discriminative Algorithms](legacy-ml.md)

[Resources](legacy-ml.md)

[Exercises](legacy-ml.md)

[2. Model Evaluation and Selection](legacy-ml.md)

[Resources](legacy-ml.md)

[Exercises](legacy-ml.md)

[3. Generative Algorithms](legacy-ml.md)

[Resources](legacy-ml.md)

[Exercises](legacy-ml.md)

[4. Fundamental Algorithms](legacy-ml.md)

[Resources](legacy-ml.md)

[Exercises](legacy-ml.md)

[5. Unsupervised Learning](legacy-ml.md)

[Resources](legacy-ml.md)

[Exercises](legacy-ml.md)

[6. Visualizations](legacy-ml.md)

1. Supervised Learning and Discriminative Algorithms

Resources

Read about [Supervised Learning VS Unsupervised Learning](ml-foundations.md)

In the [following lecture notes](ml-foundations.md) read:

Part 1: MLE vs MAP: Pages 4-6

Part 2: KNN: Pages 7-9 (without kernel regression)

Read about [Curse of Dimensionality](ml-foundations.md)

Part 3: Linear Regression: Pages 11-15

[Quiz](ml-foundations.md) yourself!

Part 4: Classification and Logistic Regression: Pages 16-19

[Play](ml-foundations.md) with gradient descent

Exercises

None for now.

2. Model Evaluation and Selection

Resources

[Bias-Variance Tradeoff](ml-bias-validation.md)

[Data Split and Tweaking models](ml-bias-validation.md)

[Overfitting](ml-bias-validation.md)

[Imbalanced Data](ml-bias-validation.md)

[Types of biases](ml-bias-validation.md), read until “Group attribution bias”

[Data Drift and Data Shift](ml-bias-validation.md)

Bonus: [Statistical Tests](ml-bias-validation.md)

Evaluation Metrics:

Topics: Precision, Recall, FAR, F-Score, Confusion Matrix, ROC Curve, PR Curve, AUC,  AP etc.

In the following read all the optional sections and play with the interactive part: [thresholding](ml-metrics.md), [Main Metrics](ml-metrics.md) and [Curves](ml-metrics.md)

take a look at the [metric summary written by the mador](legacy-metrics.md)! And [Lecture Slides](ml-metrics.md)

How much data is enough for a test set? Watch [Itay’s lecture](https://www.youtube.com/watch?v=aClpa7VORrE&list=PLuS9MY73SUnKeZQBk5LWxZah_-njyk-gV&index=12) on error estimation in metrics

Exercises

In the jupyter notebook, complete the sections on Linear Regression and Logistic Regression.

3. Generative Algorithms

Resources

In the [following lecture notes](ml-foundations.md) read:

Generative algorithms and Naïve Bayes: Pages 20-23 (skip text classification)

Exercises

In the jupyter notebook, complete the section on Naive Bayes

4. Fundamental Algorithms

This chapter will overview the standard algorithms used in ML

Resources

In the [following lecture notes](ml-foundations.md) read about SVM: Pages 33-41

Complete the Course about [Decision Trees and Forests](ml-trees-ensembles.md) (skip full example)

Understand the methods used for ensemble models:

[Bagging and boosting](ml-trees-ensembles.md)

[Stacking, Voting and Blending](ml-trees-ensembles.md)

Read about [AdaBoost](ml-trees-ensembles.md)

Read about [XGBoost](ml-trees-ensembles.md)

Read about [LightGBM](ml-trees-ensembles.md)

Watch [Ron’s AAAI](https://youtu.be/-KWgXpDZVoI?si=Za38DBG7d9ppzUdZ) about modern techniques in ML

Exercises

In the jupyter notebook, complete the sections on KNN, SVM, Trees, and Ensembles.

5. Unsupervised Learning

Resources

Read [Principal Component Analysis](ml-unsupervised.md) – change to Ron’s blog

Read [Clustering Algorithms Blog](ml-unsupervised.md)

Read [Spectreal Clustering](ml-unsupervised.md) (example is optional)

Read on [EM](ml-unsupervised.md) and [GMM](ml-unsupervised.md)

Read the following [Distill post on TSNE](ml-unsupervised.md) (get the vibes only)

Read the following [post on UMAP](ml-unsupervised.md)

Exercises

In the jupyter notebook, complete the sections on PCA and Clustering.

6. Visualizations

Go over this [plotly notebook](arrays-data.md) and this [plotly notebook](arrays-data.md)

Visualize your favorite datasets using [plotly express](arrays-data.md) – Show your shampoeer your beautiful plots!

7. Final Exercise

The final exercise is to solve [this Kaggle challenge](https://www.kaggle.com/competitions/2024-b2sw-ml/overview). The details of the challenge can be found [here](https://indico.belle2.org/event/11190/contributions/76556/attachments/29202/43141/ML%20Hands-on%20session%202024.pdf).

Your mission (choose to accept it) is to achieve a score of at least 0.918 in the leaderboards. Good Luck!
