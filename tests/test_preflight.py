"""Check false-green failure modes without requiring real internal services or datasets."""

import csv
import importlib.util
import json
from pathlib import Path
import subprocess
import sys

import pytest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("course_preflight", ROOT / "tools/preflight.py")
preflight = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(preflight)


def readiness_file(tmp_path, mutate=None):
    evidence = tmp_path / "smoke.txt"
    evidence.write_text("Synthetic test transcript, not real internal readiness.\n")
    rows = [
        {"component": name, "owner": "test-owner", "status": "VERIFIED",
         "version_or_commit": "synthetic-revision", "checksum": "",
         "smoke_evidence": "smoke.txt"}
        for name in preflight.REQUIRED_COMPONENTS
    ]
    if mutate:
        mutate(rows)
    path = tmp_path / "readiness.csv"
    with path.open("w", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=sorted(preflight.REQUIRED_COLUMNS))
        writer.writeheader()
        writer.writerows(rows)
    return path


def test_record_presence_does_not_claim_executed_checks(tmp_path):
    records = preflight.readiness_checks(readiness_file(tmp_path))
    assert len(records) == len(preflight.REQUIRED_COMPONENTS)
    assert {record["status"] for record in records} == {"RECORDED"}
    assert preflight.summarize(records) == ("RECORDED", 0)


@pytest.mark.parametrize("field,value", [
    ("owner", ""), ("owner", "FILL_IN"), ("version_or_commit", ""),
    ("status", "NOT_PREPARED"), ("smoke_evidence", "missing.txt"),
    ("smoke_evidence", "https://fixture.invalid/evidence"),
])
def test_incomplete_record_blocks_even_if_marked_verified(tmp_path, field, value):
    path = readiness_file(tmp_path, lambda rows: rows[0].update({field: value}))
    record = preflight.readiness_checks(path)[0]
    assert record["status"] == "BLOCKED"
    assert record["owner"] == (value if field == "owner" else "test-owner")


def test_empty_evidence_blocks(tmp_path):
    path = readiness_file(tmp_path)
    (tmp_path / "smoke.txt").write_text("")
    assert preflight.summarize(preflight.readiness_checks(path)) == ("BLOCKED", 2)


def test_missing_component_blocks(tmp_path):
    path = readiness_file(tmp_path, lambda rows: rows.pop())
    records = preflight.readiness_checks(path)
    assert records[-1]["name"] == preflight.REQUIRED_COMPONENTS[-1]
    assert records[-1]["status"] == "BLOCKED"


def test_duplicate_component_fails(tmp_path):
    path = readiness_file(tmp_path, lambda rows: rows.append(rows[0]))
    assert preflight.summarize(preflight.readiness_checks(path)) == ("FAIL", 1)


def test_bad_csv_schema_fails(tmp_path):
    path = tmp_path / "wrong.csv"
    path.write_text("component,status\nfixture,VERIFIED\n")
    assert preflight.summarize(preflight.readiness_checks(path)) == ("FAIL", 1)


def test_duplicate_status_columns_fail(tmp_path):
    path = readiness_file(tmp_path)
    lines = path.read_text().splitlines()
    path.write_text("\n".join([lines[0] + ",status"] + [row + ",VERIFIED" for row in lines[1:]]))
    assert preflight.summarize(preflight.readiness_checks(path)) == ("FAIL", 1)


def test_missing_readiness_file_blocks(tmp_path):
    records = preflight.readiness_checks(tmp_path / "missing.csv")
    assert preflight.summarize(records) == ("BLOCKED", 2)


def test_unprepared_public_template_is_blocked():
    records = preflight.readiness_checks(ROOT / "templates/readiness.csv")
    assert preflight.summarize(records) == ("BLOCKED", 2)


def test_smoke_zero_exit_with_wrong_report_fails():
    record = preflight.run_smoke(
        "wrong-report", [sys.executable, "-c", "print('[]')"], report=True,
    )
    assert record["status"] == "FAIL"


def test_smoke_failure_does_not_copy_arbitrary_logs():
    record = preflight.run_smoke(
        "failed-fixture", [sys.executable, "-c", "raise RuntimeError('fake-private-log')"],
    )
    assert record["status"] == "FAIL"
    assert "fake-private-log" not in record["detail"]
    assert preflight.summarize([record, {"status": "BLOCKED"}]) == ("FAIL", 1)


def test_smoke_timeout_fails(monkeypatch):
    def timeout(*args, **kwargs):
        raise subprocess.TimeoutExpired("synthetic-command", 30)
    monkeypatch.setattr(preflight.subprocess, "run", timeout)
    assert preflight.run_smoke("timeout", ["synthetic-command"])["status"] == "FAIL"


def test_missing_packages_are_blocked(monkeypatch):
    monkeypatch.setattr(preflight.importlib.util, "find_spec", lambda name: None)
    records = preflight.starter_checks()
    assert records[0]["status"] == records[2]["status"] == "BLOCKED"


def test_output_cannot_destroy_input_csv(tmp_path):
    path = readiness_file(tmp_path)
    before = path.read_bytes()
    with pytest.raises(SystemExit) as error:
        preflight.main(["--readiness", str(path), "--output", str(path)])
    assert error.value.code == 2
    assert path.read_bytes() == before


@pytest.mark.skipif(importlib.util.find_spec("mcp") is None, reason="Install the optional MCP extra")
def test_starter_command_from_another_cwd_saves_json(tmp_path):
    output = tmp_path / "evidence/preflight.json"
    result = subprocess.run(
        [sys.executable, str(ROOT / "tools/preflight.py"), "--scope", "starter",
         "--json", "--output", str(output)],
        cwd=tmp_path, capture_output=True, text=True, timeout=45,
    )
    assert result.returncode == 0, result.stderr + result.stdout
    report = json.loads(result.stdout)
    assert report == json.loads(output.read_text())
    assert report["status"] == "PASS"
    assert len(report["checks"]) == 3
    assert {record["status"] for record in report["checks"]} == {"PASS"}
    assert "UNVERIFIED" in report["internal_integration"]
