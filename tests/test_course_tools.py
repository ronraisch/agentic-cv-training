"""Distribution and file-validation regressions, independent of application defects."""

from pathlib import Path
import re
import shutil
import subprocess
import sys

import pytest


ROOT = Path(__file__).resolve().parents[1]


def run(script, cwd, *args):
    return subprocess.run(
        [sys.executable, str(script), *map(str, args)],
        cwd=cwd, capture_output=True, text=True, timeout=30,
    )


def tool_copy(tmp_path, name):
    root = tmp_path / "source"
    tools = root / "tools"
    tools.mkdir(parents=True)
    path = tools / name
    shutil.copyfile(ROOT / "tools" / name, path)
    return root, path


def commit_source(root):
    subprocess.run(["git", "init", "-q", str(root)], check=True, capture_output=True)
    subprocess.run(["git", "-C", str(root), "add", "."], check=True, capture_output=True)
    subprocess.run(
        ["git", "-C", str(root), "-c", "user.name=Course test",
         "-c", "user.email=course-test@example.invalid", "commit", "-qm", "Teaching source"],
        check=True, capture_output=True,
    )


def test_skills_check_works_outside_checkout(tmp_path):
    result = run(ROOT / "tools/check_skills.py", tmp_path)
    assert result.returncode == 0, result.stderr
    assert "Validated research-data-review" in result.stdout
    assert "Validated torch-inference-review" in result.stdout
    assert "Validated 2 required course skills" in result.stdout


@pytest.mark.parametrize("missing", ["all", "torch-inference-review"])
def test_skills_check_rejects_absent_required_files(tmp_path, missing):
    root, script = tool_copy(tmp_path, "check_skills.py")
    if missing != "all":
        shutil.copytree(ROOT / ".agents/skills", root / ".agents/skills")
        shutil.rmtree(root / ".agents/skills" / missing)
    result = run(script, tmp_path)
    assert result.returncode != 0
    assert "Missing required course skill" in result.stderr


def test_learner_export_preserves_empty_output_directory_and_links(tmp_path):
    # Build a source fixture so this regression also runs in a history-free export.
    root, script = tool_copy(tmp_path, "export_learner.py")
    for name in ("AGENTS.md", "README.md", "LICENSE", "pyproject.toml", "uv.lock", ".gitignore"):
        shutil.copyfile(ROOT / name, root / name)
    for name in (".agents", ".github", "docs", "labs", "templates", "src", "tests", "tools",
                 "data", "reviews"):
        shutil.copytree(
            ROOT / name, root / name, dirs_exist_ok=True,
            ignore=shutil.ignore_patterns("__pycache__", ".env*"),
        )
    (root / "instructor").mkdir()
    (root / "instructor/answer.txt").write_text("synthetic mentor-only marker")
    (root / "MAINTAINERS.md").write_text("synthetic maintainer-only marker")
    commit_source(root)
    destination = tmp_path / "learner"
    result = run(script, tmp_path, destination)
    assert result.returncode == 0, result.stderr
    assert sorted(p.name for p in (destination / "artifacts").iterdir()) == [".gitkeep"]
    assert not (destination / "instructor").exists()
    assert not (destination / "MAINTAINERS.md").exists()
    assert not (destination / ".git").exists()
    workflow = (destination / ".github/workflows/ci.yml").read_text()
    assert "instructor/" not in workflow
    assert "  torch:\n" not in workflow
    assert "uv run pytest" in workflow
    missing = []
    for document in destination.rglob("*.md"):
        for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", document.read_text()):
            target = link.split("#", 1)[0]
            if target and "://" not in target and not target.startswith("mailto:"):
                if not (document.parent / target).exists():
                    missing.append((str(document.relative_to(destination)), link))
    assert not missing


def test_export_never_distributes_previous_artifacts(tmp_path):
    root, script = tool_copy(tmp_path, "export_learner.py")
    (root / "artifacts").mkdir()
    (root / "artifacts/prior-learner.txt").write_text("must not distribute")
    workflow = root / ".github/workflows/ci.yml"
    workflow.parent.mkdir(parents=True)
    workflow.write_text("jobs:\n  core:\n    steps: []\n")
    commit_source(root)
    destination = tmp_path / "learner"
    result = run(script, tmp_path, destination)
    assert result.returncode == 0, result.stderr
    assert sorted(p.name for p in (destination / "artifacts").iterdir()) == [".gitkeep"]


def test_export_uses_committed_source_without_local_files(tmp_path):
    root, script = tool_copy(tmp_path, "export_learner.py")
    workflow = root / ".github/workflows/ci.yml"
    workflow.parent.mkdir(parents=True)
    workflow.write_text("jobs:\n  core:\n    steps: []\n")
    (root / "README.md").write_text("Committed teaching material\n")
    (root / ".gitignore").write_text("private-cache/\n")
    commit_source(root)
    (root / "README.md").write_text("Unreleased local changes\n")
    for name in (".env", ".env.local", "notes.txt", "work/private.txt", "private-cache/item.txt"):
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("AUDIT_FAKE_SECRET=synthetic-only\n")
    destination = tmp_path / "learner"
    result = run(script, tmp_path, destination)
    assert result.returncode == 0, result.stderr
    assert (destination / "README.md").read_text() == "Committed teaching material\n"
    for name in (".env", ".env.local", "notes.txt", "work", "private-cache"):
        assert not (destination / name).exists(), name


def test_export_omits_env_files_even_when_committed(tmp_path):
    root, script = tool_copy(tmp_path, "export_learner.py")
    workflow = root / ".github/workflows/ci.yml"
    workflow.parent.mkdir(parents=True)
    workflow.write_text("jobs:\n  core:\n    steps: []\n")
    for name in (".env", ".env.local", "docs/.env.production"):
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("AUDIT_FAKE_SECRET=synthetic-only\n")
    commit_source(root)
    destination = tmp_path / "learner"
    result = run(script, tmp_path, destination)
    assert result.returncode == 0, result.stderr
    assert not list(destination.rglob(".env*"))


def test_export_rejects_tracked_symlinks_without_partial_destination(tmp_path):
    root, script = tool_copy(tmp_path, "export_learner.py")
    outside = tmp_path / "outside.txt"
    outside.write_text("synthetic-private-material\n")
    (root / "linked.txt").symlink_to(outside)
    commit_source(root)
    destination = tmp_path / "learner"
    result = run(script, tmp_path, destination)
    assert result.returncode != 0
    assert "Unsupported source archive entry" in result.stderr
    assert not destination.exists()
    assert outside.read_text() == "synthetic-private-material\n"


def test_export_requires_committed_source_checkout(tmp_path):
    _, script = tool_copy(tmp_path, "export_learner.py")
    destination = tmp_path / "learner"
    result = run(script, tmp_path, destination)
    assert result.returncode != 0
    assert "Export requires Git and a committed source checkout" in result.stderr
    assert not destination.exists()


@pytest.mark.parametrize("target", ["existing", "inside_source"])
def test_export_rejects_existing_or_nested_destination(tmp_path, target):
    root, script = tool_copy(tmp_path, "export_learner.py")
    destination = tmp_path / "existing" if target == "existing" else root / "nested"
    if target == "existing":
        destination.mkdir()
        (destination / "keep.txt").write_text("unchanged")
    result = run(script, tmp_path, destination)
    assert result.returncode != 0
    assert "Choose a new destination outside this checkout" in result.stderr
    if target == "existing":
        assert (destination / "keep.txt").read_text() == "unchanged"
    else:
        assert not destination.exists()
