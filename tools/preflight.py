"""Run local starter smokes and inspect readiness records, without claiming live integration."""

import argparse
import csv
from datetime import datetime, timezone
import importlib.util
import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_COMPONENTS = (
    "teaching_system", "python_uv_lock", "frontend_lock", "model_weights_and_caches",
    "internal_agent_skills_mcp", "artifactory_openshift", "nfs_pvc", "confluence_access",
    "matt_pocock_skills", "personal_openshift_pod", "omp_local_llm_qwen_3_8",
)
REQUIRED_COLUMNS = {
    "component", "owner", "status", "version_or_commit", "checksum", "smoke_evidence",
}
PLACEHOLDERS = {"", "FILL_IN", "TODO", "TBD"}


def check(name, status, detail, **fields):
    return {"name": name, "status": status, "detail": detail, **fields}


def run_smoke(name, args, *, marker=None, report=False):
    """Only fixed repository commands call this; captured logs are never copied into reports."""
    try:
        result = subprocess.run(
            args, cwd=ROOT, capture_output=True, text=True, timeout=30,
        )
    except subprocess.TimeoutExpired:
        return check(name, "FAIL", "Local smoke exceeded 30 seconds.", command=args)
    except OSError:
        return check(name, "FAIL", "Could not launch local smoke.", command=args)
    if result.returncode:
        return check(
            name, "FAIL", f"Local smoke exited {result.returncode}; replay its command for logs.",
            command=args,
        )
    if marker and marker not in result.stdout:
        return check(name, "FAIL", "Smoke success marker is missing.", command=args)
    if report:
        try:
            rows = json.loads(result.stdout)
            valid = (
                isinstance(rows, list) and len(rows) == 3
                and all(isinstance(row, dict)
                        and set(row) == {"sample_id", "scene_id", "split"} for row in rows)
            )
        except (ValueError, TypeError):
            valid = False
        if not valid:
            return check(name, "FAIL", "Fixture report has an unexpected schema.", command=args)
    return check(name, "PASS", "Executed local synthetic smoke.", command=args)


def starter_checks():
    checks = []
    for name, modules, args, options in (
        ("researchlab_cli", ("numpy", "pandas", "httpx", "tenacity"),
         [sys.executable, "-m", "researchlab.cli", "--data", str(ROOT / "data/fixtures")],
         {"report": True}),
        ("course_skill_files", (), [sys.executable, str(ROOT / "tools/check_skills.py")],
         {"marker": "Validated 2 required course skills"}),
        ("mcp_protocol", ("mcp", "pandas"), [sys.executable, str(ROOT / "tools/check_mcp.py")],
         {"marker": "MCP initialized, discovered tools, checked success and invalid-input error"}),
    ):
        missing = [module for module in modules if importlib.util.find_spec(module) is None]
        if missing:
            checks.append(check(
                name, "BLOCKED", "Missing packages: " + ", ".join(missing)
                + "; use the approved locked dev/MCP environment.", command=args,
            ))
        else:
            checks.append(run_smoke(name, args, **options))
    return checks


def same_file(first, second):
    """Compare both paths and existing inode aliases, including hard links."""
    if first.resolve() == second.resolve():
        return True
    try:
        return first.samefile(second)
    except OSError:
        return False


def readiness_checks(path, *, output=None):
    """Inspect record metadata and local evidence-file presence; never execute CSV contents."""
    try:
        with path.open(newline="", encoding="utf-8-sig") as source:
            reader = csv.DictReader(source, strict=True)
            if not REQUIRED_COLUMNS.issubset(reader.fieldnames or ()):
                return [check("readiness_records", "FAIL", "Required CSV columns are missing.")]
            if len(reader.fieldnames) != len(set(reader.fieldnames)):
                return [check("readiness_records", "FAIL", "Duplicate CSV column names.")]
            rows = {}
            for row in reader:
                if None in row or any(value is None for value in row.values()):
                    return [check("readiness_records", "FAIL", "Malformed CSV row.")]
                row = {key: value.strip() for key, value in row.items()}
                name = row["component"]
                if not name or name in rows:
                    return [check("readiness_records", "FAIL", "Empty or duplicate component ID.")]
                rows[name] = row
    except (UnicodeError, csv.Error):
        return [check("readiness_records", "FAIL", "Readiness CSV has invalid syntax or encoding.")]
    except OSError:
        return [check("readiness_records", "BLOCKED", "Readiness CSV cannot be read.")]

    if output:
        # Protect all referenced evidence, including records not yet VERIFIED or required.
        for row in rows.values():
            if row["smoke_evidence"] not in PLACEHOLDERS:
                evidence = Path(row["smoke_evidence"])
                if not evidence.is_absolute():
                    evidence = path.parent / evidence
                if same_file(output, evidence):
                    raise ValueError("Output must not overwrite a smoke evidence file")

    checks = []
    for name in REQUIRED_COMPONENTS:
        row = rows.get(name)
        if row is None:
            checks.append(check(name, "BLOCKED", "Required readiness record is missing."))
            continue
        owner = row["owner"]
        if row["status"] != "VERIFIED":
            checks.append(check(
                name, "BLOCKED", f"Recorded status is {row['status'] or '(empty)'}; expected VERIFIED.",
                owner=owner,
            ))
            continue
        required = (owner, row["version_or_commit"] or row["checksum"], row["smoke_evidence"])
        if any(value in PLACEHOLDERS for value in required):
            checks.append(check(
                name, "BLOCKED", "Owner, revision/checksum or evidence reference is missing.",
                owner=owner,
            ))
            continue
        # HTTP URLs, shell commands and remote references are not evidence this tool can inspect.
        evidence = Path(row["smoke_evidence"])
        if not evidence.is_absolute():
            evidence = path.parent / evidence
        try:
            present = evidence.is_file() and evidence.stat().st_size > 0
        except OSError:
            present = False
        if not present:
            checks.append(check(name, "BLOCKED", "Local evidence file is missing or empty.",
                                owner=owner))
        else:
            checks.append(check(
                name, "RECORDED", "Record and nonempty evidence file are present; not replayed.",
                owner=owner,
            ))
    return checks


def summarize(checks):
    statuses = {item["status"] for item in checks}
    if "FAIL" in statuses:
        return "FAIL", 1
    if "BLOCKED" in statuses:
        return "BLOCKED", 2
    return ("RECORDED" if "RECORDED" in statuses else "PASS"), 0


def source_state():
    if not (ROOT / ".git").exists():
        return None, None  # Learner exports intentionally have no Git history.
    try:
        revision = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, stderr=subprocess.DEVNULL, text=True,
            timeout=5,
        ).strip()
        dirty = subprocess.check_output(
            ["git", "status", "--porcelain"], cwd=ROOT, stderr=subprocess.DEVNULL, text=True,
            timeout=5,
        )
        return revision, bool(dirty.strip())
    except (OSError, subprocess.SubprocessError):
        return None, None


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scope", choices=("starter", "handoff"), default="handoff")
    parser.add_argument("--readiness", type=Path, help="Internal CSV; paths resolve beside this file")
    parser.add_argument("--json", action="store_true", help="Print structured JSON")
    parser.add_argument("--output", type=Path, help="Save JSON evidence locally")
    args = parser.parse_args(argv)
    if args.scope == "starter" and args.readiness:
        parser.error("--readiness requires --scope handoff")
    readiness = args.readiness or ROOT / "templates/readiness.csv"
    if args.output and same_file(args.output, readiness):
        parser.error("Output must not overwrite the readiness CSV")
    records = []
    if args.scope == "handoff":
        try:
            records = readiness_checks(readiness, output=args.output)
        except ValueError as error:
            parser.error(str(error))
    checks = starter_checks()
    checks += records
    status, code = summarize(checks)
    revision, dirty = source_state()
    report = {
        "scope": args.scope, "status": status, "exit_code": code,
        "observed_at": datetime.now(timezone.utc).isoformat(),
        "source_commit": revision, "source_dirty": dirty, "python": sys.version.split()[0],
        "interpreter": sys.executable, "checks": checks,
        "internal_integration": "UNVERIFIED: supplied records are not replayed by this tool.",
    }
    serialized = json.dumps(report, indent=2) + "\n"
    if args.output:
        try:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(serialized, encoding="utf-8")
        except OSError:
            parser.error("Could not write output report")
    if args.json:
        print(serialized, end="")
    else:
        for item in checks:
            owner = f" (owner: {item['owner']})" if item.get("owner") else ""
            print(f"{item['status']} {item['name']}{owner}: {item['detail']}")
        print(f"Overall: {status}; scope: {args.scope}; exit: {code}")
        print(report["internal_integration"])
    return code


if __name__ == "__main__":
    sys.exit(main())
