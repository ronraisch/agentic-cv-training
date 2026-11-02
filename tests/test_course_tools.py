"""Course skill file validation."""

from pathlib import Path
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
