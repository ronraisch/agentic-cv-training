"""Export committed learner materials, excluding mentor files and local state."""

import argparse
from fnmatch import fnmatch
from io import BytesIO
from pathlib import Path
import subprocess
import tarfile
from tempfile import TemporaryDirectory

parser = argparse.ArgumentParser()
parser.add_argument("destination", type=Path)
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
dest = args.destination.resolve()
if dest.exists() or root == dest or root in dest.parents:
    parser.error("Choose a new destination outside this checkout")

# Archive HEAD rather than walking a used workspace: ignore untracked/ignored files
# and local edits, including edits to tracked files replaced by local symlinks.
try:
    top = subprocess.check_output(
        ["git", "rev-parse", "--show-toplevel"], cwd=root, stderr=subprocess.PIPE, text=True
    ).strip()
    if Path(top).resolve() != root:
        parser.error("Run the exporter from its source Git checkout")
    revision = subprocess.check_output(
        ["git", "rev-parse", "--verify", "HEAD"], cwd=root, text=True
    ).strip()
    archive = subprocess.check_output(
        ["git", "archive", "--format=tar", revision], cwd=root, stderr=subprocess.PIPE
    )
except (subprocess.CalledProcessError, FileNotFoundError):
    parser.error("Export requires Git and a committed source checkout")

excluded = (
    "instructor", "MAINTAINERS.md", ".git", ".venv", ".env*", "__pycache__",
    ".pytest_cache", ".ruff_cache", "artifacts", "generated", "dist", "*.egg-info",
)
dest.parent.mkdir(parents=True, exist_ok=True)
with TemporaryDirectory(prefix=".learner-export-", dir=dest.parent) as temporary:
    staged = Path(temporary) / "learner"
    staged.mkdir()
    with tarfile.open(fileobj=BytesIO(archive)) as source:
        for member in source:
            path = Path(member.name)
            if path.is_absolute() or ".." in path.parts:
                parser.error("Unsafe path in source archive")
            if any(fnmatch(part, pattern) for part in path.parts for pattern in excluded):
                continue
            if member.isdir():
                continue
            # Do not follow or distribute links to material outside the learner copy.
            if not member.isfile():
                parser.error(f"Unsupported source archive entry: {member.name}")
            target = staged / path
            target.parent.mkdir(parents=True, exist_ok=True)
            with source.extractfile(member) as content:
                target.write_bytes(content.read())
            target.chmod(member.mode & 0o777)
    # Keep an empty evidence destination, never previous cohorts' artifacts.
    (staged / "artifacts").mkdir()
    (staged / "artifacts/.gitkeep").touch()
    # Instructor-only Torch CI job is absent from learner distribution.
    workflow = staged / ".github/workflows/ci.yml"
    workflow.write_text(
        "\n".join(
            line
            for line in workflow.read_text().split("  torch:\n")[0].splitlines()
            if "instructor/" not in line
        )
        + "\n"
    )
    staged.rename(dest)
print(f"Learner copy: {dest}; source commit: {revision}; initialize a new repository")
