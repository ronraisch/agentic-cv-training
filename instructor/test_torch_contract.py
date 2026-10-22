import os

import pytest
import torch

from researchlab.torch_model import build_model

if os.environ.get("COURSE_IMPL") == "reference":
    from instructor.reference import embed
else:
    from researchlab.torch_model import embed


def test_eval_no_graph_restores_mode():
    model = build_model()
    x = torch.ones((8, 4))
    a, b = embed(model, [x]), embed(model, [x])
    torch.testing.assert_close(a, b)
    assert not a.requires_grad
    assert a.device.type == "cpu"
    assert model.training


def test_empty_and_error_restoration():
    model = build_model()
    assert embed(model, []).shape == (0, 4)
    with pytest.raises(ValueError):
        embed(model, [torch.ones((2, 5))])
    assert model.training
    with pytest.raises(ValueError):
        embed(model, [torch.full((1, 4), float("nan"))])
