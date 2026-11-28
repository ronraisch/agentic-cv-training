"""Read-only catalog MCP server. Stdout carries only the stdio protocol."""

import argparse
from pathlib import Path

import pandas as pd
from mcp.server import MCPServer

mcp = MCPServer("research-training-catalog")
CATALOG = Path("data/catalog/samples.csv")
REQUIRED_COLUMNS = {"sample_id", "scene_id", "split"}


@mcp.tool()
def list_samples(limit: int = 3, split: str = "train") -> dict:
    """List local sample metadata. Limit 1..20. Use train, validation or test."""
    if not 1 <= limit <= 20:
        raise ValueError("limit must be between 1 and 20")
    if split not in {"train", "validation", "test"}:
        raise ValueError("unsupported split")
    if not CATALOG.is_file():
        raise ValueError(f"Missing catalog CSV: {CATALOG}. Supply --catalog PATH with "
                         "sample_id,scene_id,split columns. See docs/reference/DATA_FORMATS.md#retrieval-catalog.")
    data = pd.read_csv(CATALOG)
    if not REQUIRED_COLUMNS <= set(data.columns):
        raise ValueError(f"{CATALOG} must contain sample_id,scene_id,split columns")
    selected = data[data["split"] == split][["sample_id", "scene_id", "split"]]
    return {
        "items": selected.head(limit).to_dict("records"),
        "truncated": len(selected) > limit,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=CATALOG)
    CATALOG = parser.parse_args().catalog
    mcp.run()
