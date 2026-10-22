"""Minimal course-format validation; behavior is evaluated in lab 07."""

from pathlib import Path

for path in Path(".agents/skills").glob("*/SKILL.md"):
    text = path.read_text()
    assert text.startswith("---\n")
    frontmatter = text.split("---", 2)[1]
    assert f"name: {path.parent.name}\n" in frontmatter
    assert "description: " in frontmatter
    assert (path.parent / "references/checks.md").is_file()
    print(f"Validated {path.parent.name}")
