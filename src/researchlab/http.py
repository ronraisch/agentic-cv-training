"""Shared transport. Connectors own schemas; transport owns transient GET failures."""

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential


class TransientHTTPError(Exception):
    pass


class HTTPClient:
    def __init__(self, client: httpx.Client):
        self.client = client

    @retry(
        retry=retry_if_exception_type((httpx.TransportError, TransientHTTPError)),
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=0.01, max=0.05),
        reraise=True,
    )
    def get_json(self, url: str, params: dict | None = None) -> dict:
        response = self.client.get(url, params=params, timeout=2.0)
        if response.status_code == 429 or 500 <= response.status_code <= 599:
            raise TransientHTTPError(f"Temporary status {response.status_code}")
        response.raise_for_status()
        return response.json()
