"""Export learner materials without mentor answers, staged briefs or Git history."""

import argparse
import shutil
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("destination", type=Path)
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
dest = args.destination.resolve()
if dest.exists() or root == dest or root in dest.parents:
    parser.error("Choose a new destination outside this checkout")
shutil.copytree(
    root,
    dest,
    ignore=shutil.ignore_patterns(
        "instructor",
        "MAINTAINERS.md",
        ".git",
        ".venv",
        "__pycache__",
        ".pytest_cache",
        ".ruff_cache",
        "artifacts",
        "generated",
        "dist",
        "*.egg-info",
    ),
)
# Instructor-only Torch CI job is absent from learner distribution.
workflow = dest / ".github/workflows/ci.yml"
workflow.write_text(
    "\n".join(
        line
        for line in workflow.read_text().split("  torch:\n")[0].splitlines()
        if "instructor/" not in line
    )
    + "\n"
)
print(f"Learner copy: {dest}; initialize a new repository before distribution")
