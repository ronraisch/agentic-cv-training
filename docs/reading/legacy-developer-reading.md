# Original developer reading guide

[All training](index.md) · [Source coverage](sources.md)

**Reading is for you; page completion is optional.** If you can explain the concepts and answer the mentor's questions yourself, that is enough. Use these pages and the course videos to deepen understanding during the exercises with your approved agent. [Learning route and manual-work boundaries](index.md).

### On this page

- [Reading & Viewing Materials](#reading-amp-viewing-materials)

- [A. Learning Paradigms & Task Types](#a-learning-paradigms-amp-task-types)

- [B. Neural Network Fundamentals](#b-neural-network-fundamentals)

- [C. Evaluation & Metrics](#c-evaluation-amp-metrics)

- [D. Language Model Building Blocks](#d-language-model-building-blocks)

- [E. Retrieval & Applied LLM Systems](#e-retrieval-amp-applied-llm-systems)

- [F. Training, Deployment & Optimization](#f-training-deployment-amp-optimization)

**Historical handout, preserved in full.** This records the older learner text; historical schedules and instructions to complete every reading or old assignment are superseded by the stage syllabus above. Reading links now point to local explanations. Video links retain their source destinations. The current required exercises are linked from the stage syllabus.

## Reading & Viewing Materials

For each topic, one or two short resources — enough to follow a researcher's explanation, not to become an expert. Total watch/read time is roughly 5-6 hours if done end to end.

## A. Learning Paradigms & Task Types

1. Supervised, unsupervised & self-supervised learning

Article: Google for Developers — [What is Machine Learning?](ml-foundations.md) — the core split: supervised learning uses labeled data, unsupervised learning finds structure in unlabeled data, and where self-supervised learning (creating its own labels from the data itself — the approach behind most modern LLM pretraining) fits in.

Article: IBM — [Five machine learning types to know](ml-foundations.md) — broader reference covering supervised, unsupervised, self-supervised, and reinforcement learning side by side.

2. Common task types: classification, regression, clustering, segmentation, etc.

Article: Medium (Analytics Vidhya) — [Image Classification vs. Object Detection vs. Image Segmentation](dl-detection.md) — clear visual comparison of three commonly confused task types.

Article: Medium — [Regression, Classification, and Clustering: Understanding Core Machine Learning Concepts](ml-unsupervised.md) — ties task type back to the supervised/unsupervised distinction above (classification & regression are supervised; clustering is unsupervised).

## B. Neural Network Fundamentals

3. Linear layer & 4. Activation function

Video: 3Blue1Brown — [But what is a neural network? (Ch. 1)](https://www.youtube.com/watch?v=aircAruvnKk) — 19 min. Shows what a "layer" of weights and biases actually is, and why a non-linear activation function has to sit between layers.

Article: [Google ML Crash Course — Activation Functions](dl-training.md) — short reference on ReLU/sigmoid/tanh with interactive plots.

5. Loss functions & gradient descent

Video: StatQuest — [Gradient Descent, Step-by-Step](https://www.youtube.com/watch?v=sDv4f4s2SB8) — 24 min. How a loss function measures "wrongness" and how the model's weights get nudged to reduce it. This is what "training" a model means, mechanically.

6. Overfitting & regularization

Video: StatQuest — [Regularization Part 1: Ridge (L2) Regression](https://www.youtube.com/watch?v=Q81RR3yKn30) — 20 min. Explains overfitting and how regularization counters it; the same idea (penalizing complexity) shows up as weight decay/dropout in neural nets.

7. CNN

Video: 3Blue1Brown — [But what is a convolution? (CNN chapter)](https://www.youtube.com/watch?v=KuXjwB4LzSA) — 23 min. Visual build-up of what a convolution does to an image, the operation CNNs are built on.

## C. Evaluation & Metrics

8. Evaluation & basic metrics: accuracy, precision, recall — why isn't accuracy enough?

Article: Google for Developers — [Classification: Accuracy, recall, precision, and related metrics](ml-metrics.md) — the classic tumor-classifier example showing how a model can have 99% accuracy and still be useless on an imbalanced dataset.

Video: StatQuest — [Machine Learning Fundamentals: Sensitivity and Specificity](https://www.youtube.com/watch?v=vP06aMoz4v8) — 15 min. Same ideas as precision/recall, walked through with a confusion matrix.

## D. Language Model Building Blocks

9. Tokens

Video: Andrej Karpathy — [Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE) — long (2h13m); watching the first 20-30 minutes is enough to get why text is split into tokens and why that causes weird LLM behavior (e.g. bad at arithmetic/spelling).

10. Embeddings

Article: Jay Alammar — [The Illustrated Word2vec](dl-attention.md) — how words (and tokens generally) become vectors that encode meaning; foundational for understanding embeddings used everywhere downstream.

11. Attention

Video: 3Blue1Brown — [Attention in transformers, visually explained (Ch. 6)](https://www.youtube.com/watch?v=eMlx5fFNoYc) — 26 min. The mechanism that lets a model decide which other tokens are relevant to each token.

12. Encoder & 13. Decoder

Article: Jay Alammar — [The Illustrated Transformer](dl-attention.md) — the classic reference diagraming the encoder and decoder stacks and how they connect.

14. Transformer architecture — putting it together

Video: 3Blue1Brown — [But what is a GPT? Visual intro to Transformers (Ch. 5)](https://www.youtube.com/watch?v=wjZofJX0v4M) — 27 min. Ties tokens, embeddings, attention, and decoders together into "how GPT actually works."

## E. Retrieval & Applied LLM Systems

15. Vector quantization

Article: Qdrant — [What is Vector Quantization?](dl-retrieval.md) — why and how vectors get compressed for storage/search at scale.

16. Retrieval by vector similarity

Article: Pinecone — [Introduction to Faiss](dl-retrieval.md) and [Nearest Neighbor Indexes for Similarity Search](dl-retrieval.md) — how "find the closest vectors" search actually works under the hood.

17. Retrieval-Augmented Generation (RAG)

Article: Pinecone — [Retrieval-Augmented Generation](dl-retrieval.md) — connects retrieval + embeddings + an LLM into the RAG pattern that ties sections D and E together.

## F. Training, Deployment & Optimization

18. Model inference vs evaluation in PyTorch

Docs: PyTorch — [Saving and Loading Models](dl-deployment.md) — covers model.train() vs model.eval() and why forgetting to switch modes silently breaks inference (dropout/batchnorm behave differently).

19. Fine-tuning & transfer learning (incl. LoRA/PEFT)

Docs: Hugging Face — [Fine-tuning a pretrained model](dl-deployment.md) — what fine-tuning means as a follow-on to pretraining.

Docs: Hugging Face — [LoRA conceptual guide](dl-deployment.md) — why teams fine-tune a small set of extra parameters instead of the whole model.

20. Model optimization

Article: Ultralytics — [Inference Latency](dl-deployment.md) — plain-language definitions of latency vs throughput and the main levers (batching, quantization, distillation, pruning) used to optimize inference.

21. Model quantization

Article: Hugging Face — [A Gentle Introduction to 8-bit Matrix Multiplication](dl-deployment.md) — the "why" of quantization (smaller, faster, small accuracy cost) with a concrete int8 example.

22. Compiling models (general concept — no specific tool)

Article: Medium (Geek Culture) — [AI Compilers Demystified](dl-deployment.md) — what "compiling" a model means in general: turning a graph of operations into optimized machine instructions via steps like operator fusion and kernel generation, which is why a compiled model runs faster with no change to its architecture. The specific tool (PyTorch, TensorFlow/XLA, TVM, etc.) matters less than this underlying idea.

23. Model parallelism vs data parallelism

Docs: Hugging Face — [Parallelism methods](dl-deployment.md) — the core distinction: copying the model across GPUs (data parallelism) vs splitting the model itself across GPUs (model parallelism).
