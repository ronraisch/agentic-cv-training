"""Validate the two course examples from any cwd; not client activation."""

from pathlib import Path

root = Path(__file__).resolve().parents[1] / ".agents/skills"
required = ("research-data-review", "torch-inference-review")
for name in required:
    path = root / name / "SKILL.md"
    if not path.is_file():
        raise ValueError(f"Missing required course skill: {path}")
    text = path.read_text()
    if not text.startswith("---\n") or len(text.split("---", 2)) < 3:
        raise ValueError(f"Missing frontmatter: {path}")
    frontmatter = text.split("---", 2)[1]
    if f"name: {name}\n" not in frontmatter or "description: " not in frontmatter:
        raise ValueError(f"Invalid course skill metadata: {path}")
    if not (path.parent / "references/checks.md").is_file():
        raise ValueError(f"Missing review checklist: {path}")
    print(f"Validated {path.parent.name}")
print(f"Validated {len(required)} required course skills (files only; activation unverified)")
