# 4 · Deep learning, open models and video

[All training](../TRAINING_INDEX.md) · [Reading syllabus](../reading/deep.md)

Reading is a resource for you, not mandatory page completion. If you can answer the mentor’s questions and explain a new example yourself, that is enough. Theory and videos remain substantial parts of the program. Use the approved agent to deepen understanding during exercises; respect the manual assignments.

## Topics and local reading

| Topic | Reading in this repository | Apply and explain |
|---|---|---|
| Classification, loss and training | [Neural networks, backpropagation, optimization and reliable training](../reading/dl-training.md); [Learning paradigms, probability, estimation and linear models](../reading/ml-foundations.md) | Follow CS231n lectures 1–4: linear classifiers, regularization, optimization, neural nets and backprop. |
| CNNs, training practice and architectures | [CNNs, receptive fields and efficient architecture families](../reading/dl-cnns.md); [Neural networks, backpropagation, optimization and reliable training](../reading/dl-training.md) | Lectures 5–6: convolution, receptive fields, normalization, initialization and efficient architectures. |
| Feature maps and transfer | [Feature maps: what the backbone keeps](../reading/dl-feature-maps.md) | Read a spatial tensor, compare strides and choose a feature layer for transfer. |
| Sequences | [RNNs, LSTMs, temporal models and video understanding](../reading/dl-sequences.md) | Explain recurrent state and temporal context for video. |
| Transformers and ViT | [The Transformer: from translation to self-attention](../reading/dl-attention.md); [Vision Transformers: from image patches to features](../reading/dl-vit.md) | Trace translation through encoder and decoder, then turn image patches into contextualized features. |
| Task heads on visual embeddings | [Classification heads on CNN and Transformer embeddings](../reading/dl-classification-head.md); [Detection heads: dense CNNs and DETR-style decoders](../reading/dl-detection-head.md); [Segmentation heads: feature grids, skip connections and mask queries](../reading/dl-segmentation-head.md) | Follow CNN maps or patch tokens through pooling, box prediction or mask decoding. |
| Architecture and training intuition | [Deep learning intuition: find the bottleneck](../reading/dl-intuition.md) | Diagnose missing training signal, anchor assignment, query limits and architecture trade-offs. |
| Detection and segmentation survey | [Detection, segmentation, OCR and the retained paper families](../reading/dl-detection.md) | Lecture 9 and wider families, including two-stage and single-stage detection, OCR and face embeddings. |
| Self-supervision and embeddings | [Self-supervision, contrastive learning, DINO and transferable embeddings](../reading/dl-self-supervision.md) | Lecture 12: contrastive/triplet objectives, teacher/student learning and DINO encoders. |
| Generative models and 3D | [Autoencoders, VAEs, ELBO, GANs and diffusion](../reading/dl-generative.md); [3D vision, depth, reconstruction and learned scene representations](../reading/dl-3d.md) | Lectures 13–15 remain available: autoencoders, VAE/ELBO, GAN/CycleGAN, diffusion and 3D representations. |
| Vision-language and retrieval | [CLIP, VLMs, open-vocabulary detection and open-model use](../reading/dl-vision-language.md); [Vector search, quantization, RAG and retrieval evaluation](../reading/dl-retrieval.md) | Lecture 16 plus the developer primer: CLIP/VLM/open-vocabulary localization, vectors, quantization, ANN and RAG. |
| Adaptation, optimization and handover | [Transfer learning, LoRA, quantization, compilation and parallel execution](../reading/dl-deployment.md) | Fine-tuning, LoRA, quantization, compilation, loading and verified standalone inference. |

## Practical work

- [Cloud segmentation proposal](../../labs/research/04-clouds.md)
- [Ordinary-camera video](../../labs/research/05-video.md)
- [RabbitMQ/SAM3 and detector training](../../labs/research/05b-rabbitmq-sam3-detector.md)
- [Operational handover](../../labs/research/06-handover.md)

## Viewing and study

Recommended first-pass study: 16–26 h; viewing/reflection: 18–28 h. These ranges are estimates, not hard caps or measured course runtimes. Record actual effort and deepen unfamiliar subjects.
Use [the full course/video list](../reading/deep.md#videos-and-course-selection). Exact source URLs and legacy alternatives are preserved there.

Retained Stanford CS231n 2025 selection: lectures 1–16. Keep 11 and 13–15 at initial survey depth when appropriate. Michigan 2019 is an alternative. Robot/Human-Centered AI and DDPM implementation retain the historical skip status.

## Mentor conversations

Session 1: tensors, gradients, CNNs, attention and a checkpoint-to-consumer trace. Session 2: representations, detection/video, open-model failures and project choices. Retain generative/3D/distributed theory as selected mentor discussion; final handover has its own verified demonstration.

The mentor continues using the existing theory questions. Understanding is assessed, not reading completion.
