"""CSV, SQLite and HTTP adapters for local or team catalog sources."""

import sqlite3
from pathlib import Path

import pandas as pd

from researchlab.http import HTTPClient


def from_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


def from_sqlite(path: Path, split: str) -> pd.DataFrame:
    path = Path(path).resolve()
    if not path.is_file():
        raise ValueError(f"Missing catalog database {path}. Expected SQLite with a samples table "
                         "including a split column. See docs/reference/DATA_FORMATS.md#retrieval-catalog.")
    with sqlite3.connect(f"{path.as_uri()}?mode=ro", uri=True) as conn:
        return pd.read_sql_query("SELECT * FROM samples WHERE split = ?", conn, params=(split,))


def from_http(client: HTTPClient, url: str) -> pd.DataFrame:
    page = client.get_json(url)
    return pd.DataFrame(page["items"])
