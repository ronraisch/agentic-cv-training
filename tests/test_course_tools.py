"""Validation of course skills and Markdown navigation."""

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


def test_course_links_checks_paths_and_fragments(tmp_path):
    root, script = tool_copy(tmp_path, "check_course_links.py")
    shutil.copyfile(ROOT / "tools/check_reading.py", root / "tools/check_reading.py")
    (root / "docs").mkdir()
    (root / "AGENTS.md").write_text("[Setup guide](/docs/setup.md#repeat-1)\n")
    (root / "docs/setup.md").write_text(
        '# Python & uv\n\n## Repeat\n\n## Repeat\n\n<a name="source-anchor"></a>\n'
    )
    readme = root / "README.md"
    valid = (
        "[`Python`](docs/setup.md#python--uv)\n"
        "[Source][source]\n\n[source]: <docs/setup.md#source-anchor>\n"
        '<a href="docs/setup.md#source-anchor">HTML link</a>\n'
        "`[Code example](absent.md)`\n\n~~~md\n[Code example](absent.md)\n~~~\n"
    )
    readme.write_text(valid)
    result = run(script, tmp_path)
    assert result.returncode == 0, result.stderr
    assert "4 local links" in result.stdout

    readme.write_text(valid + "[Missing fragment](docs/setup.md#missing)\n")
    (root / "AGENTS.md").write_text("[Missing file](docs/missing.md)\n")
    result = run(script, tmp_path)
    assert result.returncode != 0
    assert "AGENTS.md:1: missing target: docs/missing.md" in result.stderr
    assert "README.md:11: missing fragment: docs/setup.md#missing" in result.stderr
