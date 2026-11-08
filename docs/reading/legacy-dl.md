# Original DL training handout

[All training](index.md) · [Source coverage](sources.md)

**Reading is for you; page completion is optional.** If you can explain the concepts and answer the mentor's questions yourself, that is enough. Use these pages and the course videos to deepen understanding during the exercises with your approved agent. [Learning route and manual-work boundaries](index.md).

<details>
<summary>On this page</summary>

- [Deep Learning Training](#deep-learning-training)

- [Introduction](#introduction)

- [Image Classification with Linear Classifiers](#image-classification-with-linear-classifiers)

- [Regularization and Optimization](#regularization-and-optimization)

- [Neural Networks and Backpropagation](#neural-networks-and-backpropagation)

- [Image Classification with CNNs](#image-classification-with-cnns)

- [CNN Architectures](#cnn-architectures)

- [Recurrent Neural Networks](#recurrent-neural-networks)

- [Attention and Transformers](#attention-and-transformers)

- [Object Detection, Image Segmentation, Visualizing and Understanding](#object-detection-image-segmentation-visualizing-and-understanding)

- [Video Understanding](#video-understanding)

- [Large Scale Distributed Training (brief)](#large-scale-distributed-training-brief)

- [Self-supervised Learning](#self-supervised-learning)

- [Generative Models 1](#generative-models-1)

- [Generative Models 2](#generative-models-2)

- [3D Vision](#3d-vision)

- [Vision and Language](#vision-and-language)

- [Robot Learning + Human-Centered AI - Skip those chapters](#robot-learning-human-centered-ai-skip-those-chapters)

- [<br>](#)

- [Assignments](#assignments)

</details>

**Historical handout, preserved in full.** This records the older learner text; historical schedules and instructions to complete every reading or old assignment are superseded by the stage syllabus above. Reading links now point to local explanations. Video links retain their source destinations. The current required exercises are linked from the stage syllabus.

## Deep Learning Training

Complete the entire course of [CS231n from Stanford](deep.md).

We recommend completing a chapter a day and combining the assignments after completing the relevant chapters.

Previously, this part was taught using UMichigan 2019 course videos; now it will be based on the Stanford 2025 videos, making it smoother to follow :)

Each chapter should be taught to your shampooer using the CS231N slides as the main resource. Before every session with your shampooer, make sure you are confident in presenting the slides and can explain the key concepts clearly.

The complete list of topics and materials can be found [here](deep.md)

Also, there’s a project led by Ron Korin (CV researcher from 81 and Psagot) of open source book covering the entire course material and much more. It is currently a draft and should be accessible within our network. Reach out if you're having trouble finding it.

## Introduction

[Stanford CS231N Deep Learning for Computer Vision | Spring 2025 | Lecture 1: Introduction](https://www.youtube.com/watch?v=2fq9wYslV0A&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=1)

[CS231n: Deep Learning for Computer Vision Lecture 1: part 1](dl-training.md)

[CS231n: Deep Learning for Computer Vision Lecture 1: part 2](dl-training.md)

Legacy (UMichigan 2019) [Lecture 1: Introduction to Deep Learning for Computer Vision](https://www.youtube.com/watch?v=dJYGatp4SvA&list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r)<br>

## Image Classification with Linear Classifiers

[Stanford CS231N | Spring 2025 | Lecture 2: Image Classification with Linear Classifiers](https://www.youtube.com/watch?v=pdqofxJeBN8&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=2)

[Image Classification](ml-foundations.md)

[Linear Classification](ml-foundations.md)

[Lecture 2: - Image Classification with Linear Classifiers](ml-foundations.md)

Legacy (UMichigan 2019)

[Lecture 2: Image Classification](https://www.youtube.com/watch?v=0nqvO3AM2Vw&list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r)

[Lecture 3: Linear Classifiers](https://www.youtube.com/watch?v=qcSEP17uKKY&list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r)until regularization (excluding)

## Regularization and Optimization

[Stanford CS231N | Spring 2025 | Lecture 3: Regularization and Optimization](https://www.youtube.com/watch?v=dyNGd06MWn4&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=3)

[Adam vs. AdamW: Understanding Weight Decay and Its Impact on Model Performance | by Ahmed Yassin](dl-training.md)

[Interactive Visualization of Optimization Algorithms in Deep Learning | Emilien Dupont](dl-training.md)

[Optimization](dl-training.md)

[Lecture 3: Regularization and Optimization](dl-training.md)

Legacy (UMichigan 2019)

[Lecture 3: Linear Classifiers](https://www.youtube.com/watch?v=qcSEP17uKKY&list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r)from regularization (including)

[Lecture 4: Optimization](https://www.youtube.com/watch?v=YnQJTfbwBM8&list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r)

## Neural Networks and Backpropagation

[Stanford CS231N | Spring 2025 | Lecture 4: Neural Networks and Backpropagation](https://www.youtube.com/watch?v=25zD5qJHYsk&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=4)

[Backpropagation](dl-training.md)

[Lecture 4: Neural Networks and Backpropagation](dl-training.md)

[A visual proof that neural nets can compute any function](dl-training.md)

Question: You showed in ML course, that RBF SVM can approximate any function; now you learned that two linear layers (using the universal approximation theorem) you can also approximate any function. When will you use SVM, and when will you use a Neural Network? Write as many points as you can and convince your shampooer.

Legacy (UMichigan 2019)

[Lecture 5: Neural Networks](https://www.youtube.com/watch?v=g6InpdhUblE&list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r)

[Lecture 6: Backpropagation](https://www.youtube.com/watch?v=dB-u77Y5a6A&list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r)

## Image Classification with CNNs

[Stanford CS231N | Spring 2025 | Lecture 5: Image Classification with CNNs](https://www.youtube.com/watch?v=f3g1zGdxptI&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=5)

[Convolutional Neural Networks (CNNs / ConvNets)](dl-cnns.md)

[Lecture 5: Image Classification with CNNs](dl-cnns.md)

Legacy (UMichigan 2019)

[Lecture 7: Convolutional Networks](https://www.youtube.com/watch?v=ANyxBVxmdZ0&list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r&index=7)

## CNN Architectures

[Stanford CS231N Deep Learning for Computer Vision | Spring 2025 | Lecture 6: CNN Architectures](https://www.youtube.com/watch?v=aVJy4O5TOk8&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=6)

[Lecture 6: Training CNNs and Architectures](dl-cnns.md)

Task: Compute the receptive field in each layer of VGG-16 and show it to your shampooer at your meeting.

Task: Come up with a closed formulation of the receptive field of a network with L conv layers of stride S and kernel size K.

[Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](https://www.youtube.com/watch?v=OioFONrSETc)

Legacy (UMichigan 2019)

[Lecture 8: CNN Architectures](https://www.youtube.com/watch?v=XaZIlVrIO-Q&list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r&index=8)

[Lecture 10: Training Neural Networks I](https://www.youtube.com/watch?v=lGbQlr1Ts7w&list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r)

[Lecture 11: Training Neural Networks II](https://www.youtube.com/watch?v=WUazOtlti0g&list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r&index=11)<br>

## Recurrent Neural Networks

[Stanford CS231N | Spring 2025 | Lecture 7: Recurrent Neural Networks](https://www.youtube.com/watch?v=kG2lAPBF7zA&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=7)

[Understanding LSTM Networks - colah's blog](dl-sequences.md)

[Lecture 7: Recurrent Neural Networks](dl-sequences.md)<br>

## Attention and Transformers

[Stanford CS231N | Spring 2025 | Lecture 8: Attention and Transformers](https://www.youtube.com/watch?v=RQowiOF_FvQ&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=8)

[Lecture 8: Attention and Transformers](dl-attention.md)

[Attention? Attention! | Lil'Log](dl-attention.md)

[AAAI - Transformers](https://www.youtube.com/watch?v=T-smYxIQGDw)

[An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale (Paper Explained)](https://www.youtube.com/watch?v=TrdevFK_am4)<br>

## Object Detection, Image Segmentation, Visualizing and Understanding

[Stanford CS231N | Spring 2025 | Lecture 9: Object Detection, Image Segmentation, Visualizing](https://www.youtube.com/watch?v=PTypu6GqEd4&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=9)

[Lecture 9: Detection, Segmentation, Visualization, and Understanding](dl-detection.md)

[DETR: End-to-End Object Detection with Transformers (Yannic Kilcher)](https://www.youtube.com/watch?v=T35ba_VXkMY)

Legacy (UMichigan 2019)

[Lecture 15: Object Detection](https://www.youtube.com/watch?v=TB-fdISzpHQ&list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r)

[Lecture 16: Detection and Segmentation](https://www.youtube.com/watch?v=9AyMR4IhSWQ&list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r)

[Lecture 14: Visualizing and Understanding](https://www.youtube.com/watch?v=G1hGwHVykDU&list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r)

## Video Understanding

[Stanford CS231N Deep Learning for Computer Vision | Spring 2025 | Lecture 10: Video Understanding](https://www.youtube.com/watch?v=wElqklprhPE&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=10)

[Lecture 10: Video Understanding](dl-sequences.md)

Legacy (UMichigan 2019)

[Lecture 18: Videos](https://www.youtube.com/watch?v=A9D6NXBJdwU&list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r)

## Large Scale Distributed Training (brief)

[Stanford CS231N | Spring 2025 | Lecture 11: Large Scale Distributed Training](https://www.youtube.com/watch?v=9MvD-XsowsE&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=11)

[Lecture 11: Large-Scale Distributed Training](dl-deployment.md)

## Self-supervised Learning

[Stanford CS231N | Spring 2025 | Lecture 12: Self-Supervised Learning](https://www.youtube.com/watch?v=4howBU7THbM&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=13)

[Lecture 12: Self-Supervised Learning](dl-self-supervision.md)

[DINO: Emerging Properties in Self-Supervised Vision Transformers (Facebook AI Research Explained)](https://www.youtube.com/watch?v=h3ij3F3cPIk)

[Self-supervised Learning](dl-self-supervision.md) (up to Video-Based, not including)

[Contrastive Learning](dl-self-supervision.md)

Training Objectives (go over only Contrastive Loss and Triplet Loss)

Key Ingredients

Vision: Image Embedding

## Generative Models 1

[Stanford CS231N Deep Learning for Computer Vision | Spring 2025 | Lecture 13: Generative Models 1](https://www.youtube.com/watch?v=zbHXQRUNlH0&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=13)

[Lecture 13: Generative Models (part 1)](dl-generative.md)

[ELBO — What & Why | Yunfan’s Blog](dl-generative.md) - Optional

Legacy (UMichigan 2019)

[Lecture 19: Generative Models I](https://www.youtube.com/watch?v=Q3HU2vEhD5Y&list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r)

## Generative Models 2

[Stanford CS231N Deep Learning for Computer Vision| Spring 2025 | Lecture 14: Generative Models 2](https://www.youtube.com/watch?v=Edr4uZFh4EE&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=14)

[Lecture 14: Generative Models (part 2)](dl-generative.md)

## 3D Vision

[Stanford CS231N Deep Learning for Computer Vision | Spring 2025 | Lecture 15: 3D Vision](https://www.youtube.com/watch?v=7lxrKDKtykM&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=15)

[Lecture 15: 3D Vision](dl-3d.md)

Legacy (UMichigan 2019)

[Lecture 17: 3D Vision](https://www.youtube.com/watch?v=S1_nCdLUQQ8&list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r)

## Vision and Language

[Stanford CS231N Deep Learning for Computer Vision | Spring 2025 | Lecture 16: Vision and Language](https://www.youtube.com/watch?v=mQOK0Mfyrkk&list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16&index=16)

[Lecture 16: Vision and Language](dl-vision-language.md)

[OpenAI CLIP: ConnectingText and Images (Paper Explained)](https://www.youtube.com/watch?v=T9XSU0pKX2E)

## Robot Learning + Human-Centered AI - Skip those chapters

## <br>

## Assignments

### Assignment 1 - Image Classification, kNN, Softmax, Fully-Connected Neural Network, Fully-Connected Nets

In this assignment, you will practice putting together a simple image classification pipeline based on the k-Nearest Neighbor or the SVM/Softmax classifier

Complete the following notebooks:

knn.ipynb

softmax.ipynb

two_layer_net.ipynb

features.ipynb

FullyConnectedNets.ipynb

### Assignment 2 - [Batch Normalization, Dropout, Convolutional Nets, Network Visualization, Image Captioning with RNNs](dl-cnns.md)

In this assignment you will practice writing backpropagation code, and training Neural Networks and Convolutional Neural Networks.

Complete the following notebooks:

BatchNormalization.ipynb

Dropout.ipynb

ConvolutionalNetworks.ipynb

PyTorch.ipynb

RNN_Captioning_pytorch.ipynb

### Assignment 3 - Image Captioning with Transformers, Self-Supervised Learning, Diffusion Models, CLIP and DINO Models

In this assignment, you will implement language networks and apply them to image captioning on the COCO dataset. Then you will be introduced to self-supervised learning to automatically learn the visual representations of an unlabeled dataset. Next, you will explore CLIP and DINO, two self-supervised learning methods that leverage large amounts of unlabeled data to learn visual representations.

Complete the following notebooks:

Transformer_Captioning.ipynb

Self_Supervised_Learning.ipynb

DDPM.ipynb - Skip

CLIP_DINO.ipynb

### Final assignment - Object Detection

Congrats, you have done all the assignments and (hopefully) all the course lectures. Thank your shampooer and pack your stuff from the shampooing team room, go to your team leader, and start papers shampooing.

Later, you will plan and implement an object detector all by yourself using your team’s data! You will also deploy it E2E - it will be your first shampooing project in your team 😄
