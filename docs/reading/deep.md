# 4 · Deep learning, open models and video

[All training](index.md) · [Source coverage](sources.md)

**Reading is for you; page completion is optional.** If you can explain the concepts and answer the mentor's questions yourself, that is enough. Use these pages and the course videos to deepen understanding during the exercises with your approved agent. [Learning route and manual-work boundaries](index.md).

<details>
<summary>On this page</summary>

- [Learning route and expected understanding](#learning-route-and-expected-understanding)

- [Practical work](#practical-work)

- [Videos and course selection](#videos-and-course-selection)

- [Mentor conversations](#mentor-conversations)

- [Original learner material](#original-learner-material)

- [Source limitations](#source-limitations)

</details>

## Learning route and expected understanding

Recommended first-pass study: 16–26 active hours; viewing/reflection: 18–28 active hours. These are planning ranges, not deadlines or measured full-course runtimes. Skip known explanations; deepen gaps. Record actual time.

| Topic | Local reading | What to understand and apply |
| --- | --- | --- |
| Classification, loss and training | [Neural networks, backpropagation, optimization and reliable training](dl-training.md)<br>[Learning paradigms, probability, estimation and linear models](ml-foundations.md) | Follow CS231n lectures 1–4: linear classifiers, regularization, optimization, neural nets and backprop. |
| CNNs, training practice and architectures | [CNNs, receptive fields and efficient architecture families](dl-cnns.md)<br>[Neural networks, backpropagation, optimization and reliable training](dl-training.md) | Lectures 5–6: convolution, receptive fields, normalization, initialization and efficient architectures. |
| Sequences and attention | [RNNs, LSTMs, temporal models and video understanding](dl-sequences.md)<br>[Tokens, attention, Transformers and vision Transformers](dl-attention.md) | Lectures 7–8: RNN/LSTM, encoder/decoder, masking, attention, ViT and hierarchical vision. |
| Detection, segmentation and explanations | [Detection, segmentation, OCR and the retained paper families](dl-detection.md)<br>[CNNs, receptive fields and efficient architecture families](dl-cnns.md) | Lecture 9 and retained paper families: R-CNN/Fast/Faster, SSD, YOLO, FPN/EfficientDet, DETR, FCN/U-Net, OCR and faces. |
| Video and distributed execution | [RNNs, LSTMs, temporal models and video understanding](dl-sequences.md)<br>[Transfer learning, LoRA, quantization, compilation and parallel execution](dl-deployment.md) | Lectures 10–11: temporal context, data/model parallelism and measured system cost. |
| Self-supervision and embeddings | [Self-supervision, contrastive learning, DINO and transferable embeddings](dl-self-supervision.md) | Lecture 12: contrastive/triplet objectives, teacher/student learning and DINO encoders. |
| Generative models and 3D | [Autoencoders, VAEs, ELBO, GANs and diffusion](dl-generative.md)<br>[3D vision, depth, reconstruction and learned scene representations](dl-3d.md) | Lectures 13–15 remain available: autoencoders, VAE/ELBO, GAN/CycleGAN, diffusion and 3D representations. |
| Vision-language and retrieval | [CLIP, VLMs, open-vocabulary detection and open-model use](dl-vision-language.md)<br>[Vector search, quantization, RAG and retrieval evaluation](dl-retrieval.md) | Lecture 16 plus the developer primer: CLIP/VLM/open-vocabulary localization, vectors, quantization, ANN and RAG. |
| Adaptation, optimization and handover | [Transfer learning, LoRA, quantization, compilation and parallel execution](dl-deployment.md) | Fine-tuning, LoRA, quantization, compilation, loading and verified standalone inference. |

## Practical work

- [Cloud segmentation proposal](../../labs/research/04-clouds.md)

- [Ordinary-camera video](../../labs/research/05-video.md)

- [RabbitMQ/SAM3 and detector training](../../labs/research/05b-rabbitmq-sam3-detector.md)

- [Operational handover](../../labs/research/06-handover.md)

Read selectively before and during implementation; discuss hypotheses with your agent, verify one counterexample and explain the evidence yourself. The manual Python capstone and first SAM2 service retain their existing manual rules.

## Videos and course selection

Retain Stanford CS231n 2025 lectures 1–16, in order. Lectures 11 and 13–15 can be studied at survey depth initially, as in the old mentor guide, but their subjects remain in the syllabus. Robot Learning/Human-Centered AI and DDPM implementation retain their old skip status. Michigan 2019 recordings are alternatives for corresponding topics, not a second course to watch in full. The list below preserves the exact URLs found in the source handouts; availability and runtimes have not been re-measured.

- [here](https://www.youtube.com/watch?v=T-smYxIQGDw)

- [ViT](https://www.youtube.com/watch?v=TrdevFK_am4)

- [DeTR](https://www.youtube.com/watch?v=T35ba_VXkMY)

- [DINO](https://www.youtube.com/watch?v=h3ij3F3cPIk)

- [CLIP](https://www.youtube.com/watch?v=T9XSU0pKX2E)

- [Lecture Videos](https://www.youtube.com/playlist?list=PLqYmG7hTraZDNJre23vqCGIVpfZ_K2RZs)

- [Video](https://www.youtube.com/watch?v=XtCNNwDi9xg)

- [Stanford CS231N Deep Learning for Computer Vision | Spring 2025 | Lecture 1: Introduction](https://www.youtube.com/watch?v=2fq9wYslV0A&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=1)

- [Lecture 1: Introduction to Deep Learning for Computer Vision](https://www.youtube.com/watch?v=dJYGatp4SvA&list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r)

- [Stanford CS231N | Spring 2025 | Lecture 2: Image Classification with Linear Classifiers](https://www.youtube.com/watch?v=pdqofxJeBN8&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=2)

- [Lecture 2: Image Classification](https://www.youtube.com/watch?v=0nqvO3AM2Vw&list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r)

- [Lecture 3: Linear Classifiers](https://www.youtube.com/watch?v=qcSEP17uKKY&list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r)

- [Stanford CS231N | Spring 2025 | Lecture 3: Regularization and Optimization](https://www.youtube.com/watch?v=dyNGd06MWn4&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=3)

- [Lecture 4: Optimization](https://www.youtube.com/watch?v=YnQJTfbwBM8&list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r)

- [Stanford CS231N | Spring 2025 | Lecture 4: Neural Networks and Backpropagation](https://www.youtube.com/watch?v=25zD5qJHYsk&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=4)

- [Lecture 5: Neural Networks](https://www.youtube.com/watch?v=g6InpdhUblE&list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r)

- [Lecture 6: Backpropagation](https://www.youtube.com/watch?v=dB-u77Y5a6A&list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r)

- [Stanford CS231N | Spring 2025 | Lecture 5: Image Classification with CNNs](https://www.youtube.com/watch?v=f3g1zGdxptI&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=5)

- [Lecture 7: Convolutional Networks](https://www.youtube.com/watch?v=ANyxBVxmdZ0&list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r&index=7)

- [Stanford CS231N Deep Learning for Computer Vision | Spring 2025 | Lecture 6: CNN Architectures](https://www.youtube.com/watch?v=aVJy4O5TOk8&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=6)

- [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](https://www.youtube.com/watch?v=OioFONrSETc)

- [Lecture 8: CNN Architectures](https://www.youtube.com/watch?v=XaZIlVrIO-Q&list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r&index=8)

- [Lecture 10: Training Neural Networks I](https://www.youtube.com/watch?v=lGbQlr1Ts7w&list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r)

- [Lecture 11: Training Neural Networks II](https://www.youtube.com/watch?v=WUazOtlti0g&list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r&index=11)

- [Stanford CS231N | Spring 2025 | Lecture 7: Recurrent Neural Networks](https://www.youtube.com/watch?v=kG2lAPBF7zA&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=7)

- [Stanford CS231N | Spring 2025 | Lecture 8: Attention and Transformers](https://www.youtube.com/watch?v=RQowiOF_FvQ&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=8)

- [Stanford CS231N | Spring 2025 | Lecture 9: Object Detection, Image Segmentation, Visualizing](https://www.youtube.com/watch?v=PTypu6GqEd4&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=9)

- [Lecture 15: Object Detection](https://www.youtube.com/watch?v=TB-fdISzpHQ&list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r)

- [Lecture 16: Detection and Segmentation](https://www.youtube.com/watch?v=9AyMR4IhSWQ&list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r)

- [Lecture 14: Visualizing and Understanding](https://www.youtube.com/watch?v=G1hGwHVykDU&list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r)

- [Stanford CS231N Deep Learning for Computer Vision | Spring 2025 | Lecture 10: Video Understanding](https://www.youtube.com/watch?v=wElqklprhPE&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=10)

- [Lecture 18: Videos](https://www.youtube.com/watch?v=A9D6NXBJdwU&list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r)

- [Stanford CS231N | Spring 2025 | Lecture 11: Large Scale Distributed Training](https://www.youtube.com/watch?v=9MvD-XsowsE&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=11)

- [Stanford CS231N | Spring 2025 | Lecture 12: Self-Supervised Learning](https://www.youtube.com/watch?v=4howBU7THbM&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=13)

- [Stanford CS231N Deep Learning for Computer Vision | Spring 2025 | Lecture 13: Generative Models 1](https://www.youtube.com/watch?v=zbHXQRUNlH0&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=13)

- [Lecture 19: Generative Models I](https://www.youtube.com/watch?v=Q3HU2vEhD5Y&list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r)

- [Stanford CS231N Deep Learning for Computer Vision| Spring 2025 | Lecture 14: Generative Models 2](https://www.youtube.com/watch?v=Edr4uZFh4EE&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=14)

- [Stanford CS231N Deep Learning for Computer Vision | Spring 2025 | Lecture 15: 3D Vision](https://www.youtube.com/watch?v=7lxrKDKtykM&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=15)

- [Lecture 17: 3D Vision](https://www.youtube.com/watch?v=S1_nCdLUQQ8&list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r)

- [Stanford CS231N Deep Learning for Computer Vision | Spring 2025 | Lecture 16: Vision and Language](https://www.youtube.com/watch?v=mQOK0Mfyrkk&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=16)

- [But what is a neural network? (Ch. 1)](https://www.youtube.com/watch?v=aircAruvnKk)

- [Gradient Descent, Step-by-Step](https://www.youtube.com/watch?v=sDv4f4s2SB8)

- [Regularization Part 1: Ridge (L2) Regression](https://www.youtube.com/watch?v=Q81RR3yKn30)

- [But what is a convolution? (CNN chapter)](https://www.youtube.com/watch?v=KuXjwB4LzSA)

- [Machine Learning Fundamentals: Sensitivity and Specificity](https://www.youtube.com/watch?v=vP06aMoz4v8)

- [Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE)

- [Attention in transformers, visually explained (Ch. 6)](https://www.youtube.com/watch?v=eMlx5fFNoYc)

- [But what is a GPT? Visual intro to Transformers (Ch. 5)](https://www.youtube.com/watch?v=wjZofJX0v4M)

- [https://www.youtube.com/watch?v=OioFONrSETc&ab_channel=YannicKilcher](https://www.youtube.com/watch?v=OioFONrSETc&ab_channel=YannicKilcher)

- [https://www.youtube.com/watch?v=aircAruvnKk&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi&ab_channel=3Blue1Brown](https://www.youtube.com/watch?v=aircAruvnKk&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi&ab_channel=3Blue1Brown)

## Mentor conversations

Session 1: tensors, gradients, CNNs, attention and a checkpoint-to-consumer trace. Session 2: representations, detection/video, open-model failures and project choices. Retain generative/3D/distributed theory as selected mentor discussion; final handover has its own verified demonstration.

The mentor keeps the existing theory questions and probes your reasoning with a new example. Reading-page completion is not assessed. If you can answer and explain the assigned concepts yourself, your learning route is sufficient. Gaps lead to targeted study and another discussion, not an obligation to reread every source.

## Original learner material

Complete historical handouts are preserved locally with their reading links redirected. Historical project requirements are not added to the current workload.

- [Original DL training handout](legacy-dl.md)

- [Original developer reading guide](legacy-developer-reading.md)

## Source limitations

The archive names internal items YOSO, pSp, FUN, Bukch/Bukchin, Penta-AI, Clipster and the internal Ron Korin book without sufficient identifiers or supplied contents. Their identities/full text cannot be verified from those names alone. They remain recorded in [source coverage](sources.md#unresolved-internal-material); no substitute paper or internal walkthrough has been invented. General theory around them is available above.
