"""Direct behavior checks; protocol integration lives in tools/check_mcp.py."""

import importlib.util
from pathlib import Path

import pytest

pytest.importorskip("mcp")
spec = importlib.util.spec_from_file_location("training_mcp", Path("tools/mcp_server.py"))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_catalog_bounds():
    assert len(module.list_samples(1)["items"]) == 1
    assert module.list_samples(1)["truncated"]
    with pytest.raises(ValueError):
        module.list_samples(999)
    with pytest.raises(ValueError):
        module.list_samples(1, "anything")
