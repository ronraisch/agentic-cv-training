"""Optional CPU model path. No weights or downloads required."""

import torch
from torch import nn


def build_model(seed: int = 7):
    torch.manual_seed(seed)
    return nn.Sequential(nn.Linear(4, 4), nn.Dropout(0.5))


def embed(model, batches):
    outputs = []
    for batch in batches:
        outputs.append(model(batch))
    return torch.cat(outputs)
