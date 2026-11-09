# Propose a cloud-segmentation approach

## Start here

Use approved sensor examples and public sources in your research workspace. Ask the mentor which bands are available and for one representative image with a cloud boundary. Inspect the bands, then agree on the two downstream error costs and the runtime measurement. If you get stuck, use the [worked example](../../docs/WORKED_EXAMPLES.md#deep-learning-and-video).

## Goal

A detector spends work on cloudy regions that contain little useful observation. Propose a way
to identify those regions and support a decision about where the detector should run.
This is a focused research proposal: eight hours, separate from shared core study.

## What to investigate

Start with the sensors and channels available at inference. Review primary sources and compare
a simple baseline with two plausible research alternatives, recording dated revisions.
Explain the proposed architecture, data, training and evaluation and how they fit this setting.

Use the approved agent to help break down the problem and challenge candidate experiments.
The aim is a defensible choice between a few options, rather than a long model ranking or an
unsupported claim that one architecture will win.

## Submit and discuss

Deliver a concise proposal, an evidence table and limitations. Include a minimal experiment
that could run internally and would reveal a weakness in the proposal. Full cloud-model training
requires mentor approval; it is not part of the default deliverable.

[Cloud concepts](../../docs/lessons/05-clouds.md) ·
[Training concepts](../../docs/lessons/04-torch.md) ·
[Cloud data](../../docs/DATASETS.md#cloud-segmentation) ·
[Acquisition steps](../../docs/DATASETS.md#acquire-a-working-subset)
