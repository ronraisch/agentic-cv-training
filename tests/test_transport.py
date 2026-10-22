import httpx
import pytest

from researchlab.http import HTTPClient


def test_transient_retry_then_success():
    calls = []

    def handler(request):
        calls.append(request)
        return httpx.Response(503 if len(calls) < 3 else 200, json={"ok": True})

    with httpx.Client(transport=httpx.MockTransport(handler)) as raw:
        assert HTTPClient(raw).get_json("https://fixture.invalid/data") == {"ok": True}
    assert len(calls) == 3


def test_permanent_error_is_not_retried():
    calls = []

    def handler(request):
        calls.append(request)
        return httpx.Response(401)

    with httpx.Client(transport=httpx.MockTransport(handler)) as raw:
        with pytest.raises(httpx.HTTPStatusError):
            HTTPClient(raw).get_json("https://fixture.invalid/data")
    assert len(calls) == 1
