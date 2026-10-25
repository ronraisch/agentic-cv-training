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
    destination = tmp_path / "learner"
    result = run(ROOT / "tools/export_learner.py", tmp_path, destination)
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
    destination = tmp_path / "learner"
    result = run(script, tmp_path, destination)
    assert result.returncode == 0, result.stderr
    assert sorted(p.name for p in (destination / "artifacts").iterdir()) == [".gitkeep"]


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
