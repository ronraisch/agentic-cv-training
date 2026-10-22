"""Inherited adapters. HTTP endpoint is only exercised with a mock transport."""

import sqlite3
from pathlib import Path

import pandas as pd

from researchlab.http import HTTPClient


def from_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


def from_sqlite(path: Path, split: str) -> pd.DataFrame:
    with sqlite3.connect(path) as conn:
        return pd.read_sql_query("SELECT * FROM samples WHERE split = ?", conn, params=(split,))


def from_http(client: HTTPClient, url: str) -> pd.DataFrame:
    page = client.get_json(url)
    return pd.DataFrame(page["items"])
