# 4 · Deep learning, open models and video

[All training](../TRAINING_INDEX.md) · [HTML syllabus](../reading/deep.html)

Reading is a resource for you, not mandatory page completion. If you can answer the mentor’s questions and explain a new example yourself, that is enough. Theory and videos remain substantial parts of the program. Use the approved agent to deepen understanding during exercises; respect the manual assignments.

## Topics and local reading

| Topic | Reading in this repository | Apply and explain |
|---|---|---|
| Classification, loss and training | [Neural networks, backpropagation, optimization and reliable training](../reading/dl-training.html); [Learning paradigms, probability, estimation and linear models](../reading/ml-foundations.html) | Follow CS231n lectures 1–4: linear classifiers, regularization, optimization, neural nets and backprop. |
| CNNs, training practice and architectures | [CNNs, receptive fields and efficient architecture families](../reading/dl-cnns.html); [Neural networks, backpropagation, optimization and reliable training](../reading/dl-training.html) | Lectures 5–6: convolution, receptive fields, normalization, initialization and efficient architectures. |
| Sequences and attention | [RNNs, LSTMs, temporal models and video understanding](../reading/dl-sequences.html); [Tokens, attention, Transformers and vision Transformers](../reading/dl-attention.html) | Lectures 7–8: RNN/LSTM, encoder/decoder, masking, attention, ViT and hierarchical vision. |
| Detection, segmentation and explanations | [Detection, segmentation, OCR and the retained paper families](../reading/dl-detection.html); [CNNs, receptive fields and efficient architecture families](../reading/dl-cnns.html) | Lecture 9 and retained paper families: R-CNN/Fast/Faster, SSD, YOLO, FPN/EfficientDet, DETR, FCN/U-Net, OCR and faces. |
| Video and distributed execution | [RNNs, LSTMs, temporal models and video understanding](../reading/dl-sequences.html); [Transfer learning, LoRA, quantization, compilation and parallel execution](../reading/dl-deployment.html) | Lectures 10–11: temporal context, data/model parallelism and measured system cost. |
| Self-supervision and embeddings | [Self-supervision, contrastive learning, DINO and transferable embeddings](../reading/dl-self-supervision.html) | Lecture 12: contrastive/triplet objectives, teacher/student learning and DINO encoders. |
| Generative models and 3D | [Autoencoders, VAEs, ELBO, GANs and diffusion](../reading/dl-generative.html); [3D vision, depth, reconstruction and learned scene representations](../reading/dl-3d.html) | Lectures 13–15 remain available: autoencoders, VAE/ELBO, GAN/CycleGAN, diffusion and 3D representations. |
| Vision-language and retrieval | [CLIP, VLMs, open-vocabulary detection and open-model use](../reading/dl-vision-language.html); [Vector search, quantization, RAG and retrieval evaluation](../reading/dl-retrieval.html) | Lecture 16 plus the developer primer: CLIP/VLM/open-vocabulary localization, vectors, quantization, ANN and RAG. |
| Adaptation, optimization and handover | [Transfer learning, LoRA, quantization, compilation and parallel execution](../reading/dl-deployment.html) | Fine-tuning, LoRA, quantization, compilation, loading and verified standalone inference. |

## Practical work

- [Cloud segmentation proposal](../../labs/research/04-clouds.md)
- [Ordinary-camera video](../../labs/research/05-video.md)
- [RabbitMQ/SAM3 and detector training](../../labs/research/05b-rabbitmq-sam3-detector.md)
- [Operational handover](../../labs/research/06-handover.md)

## Viewing and study

Recommended first-pass study: 16–26 h; viewing/reflection: 18–28 h. These ranges are estimates, not hard caps or measured course runtimes. Record actual effort and deepen unfamiliar subjects.
Use [the full course/video list](../reading/deep.html#videos-and-course-selection). Exact source URLs and legacy alternatives are preserved there.

Retained Stanford CS231n 2025 selection: lectures 1–16. Keep 11 and 13–15 at initial survey depth when appropriate. Michigan 2019 is an alternative. Robot/Human-Centered AI and DDPM implementation retain the historical skip status.

## Mentor conversations

Session 1: tensors, gradients, CNNs, attention and a checkpoint-to-consumer trace. Session 2: representations, detection/video, open-model failures and project choices. Retain generative/3D/distributed theory as selected mentor discussion; final handover has its own verified demonstration.

The mentor continues using the existing theory questions. Understanding is assessed, not reading completion.
