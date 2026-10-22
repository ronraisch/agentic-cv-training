"""Read-only synthetic catalog; stdout belongs to the MCP protocol."""

from pathlib import Path

import pandas as pd
from mcp.server import MCPServer

mcp = MCPServer("research-training-catalog")
FIXTURE = Path(__file__).resolve().parents[1] / "data/fixtures/samples.csv"


@mcp.tool()
def list_samples(limit: int = 3, split: str = "train") -> dict:
    """List synthetic sample metadata. Limit 1..20; split train or test."""
    if not 1 <= limit <= 20:
        raise ValueError("limit must be between 1 and 20")
    if split not in {"train", "test"}:
        raise ValueError("unsupported split")
    data = pd.read_csv(FIXTURE)
    selected = data[data["split"] == split]
    return {
        "items": selected.head(limit).to_dict("records"),
        "truncated": len(selected) > limit,
        "source": "synthetic-fixture-v1",
    }


if __name__ == "__main__":
    mcp.run()
