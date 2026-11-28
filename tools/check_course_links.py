"""Check repository-local links and heading fragments in the course's Markdown."""

import re
from collections import defaultdict
from functools import cache
from pathlib import Path
from urllib.parse import unquote, urlsplit

from check_reading import Page

ROOT = Path(__file__).resolve().parents[1]
COURSE_DIRS = ("docs", "labs", "templates", ".github", ".gitlab", ".agents")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
HEADING = re.compile(r"^ {0,3}#{1,6}[ \t]+(.+?)\s*#*\s*$")
SETEXT = re.compile(r"^ {0,3}(?:=+|-+)\s*$")
DESTINATION = r"<([^>]+)>|((?:[^\s()<>]|\([^()\n]*\))+)"
INLINE_LINK = re.compile(r"\]\(\s*(?:" + DESTINATION + r")")
REFERENCE = re.compile(r"^ {0,3}\[[^\]]+\]:\s*(?:" + DESTINATION + r")")
CODE_SPAN = re.compile(r"(`+)(?!`)(.*?)\1(?!`)")
HTML_TAG = re.compile(r"</?[A-Za-z][^>]*>")


@cache
def markdown_lines(path):
    """Yield numbered prose lines outside code fences and HTML comments."""
    source = re.sub(
        r"<!--.*?-->", lambda match: "\n" * match[0].count("\n"), path.read_text(), flags=re.S
    )
    lines = []
    fence = None
    for number, line in enumerate(source.splitlines(), 1):
        marker = FENCE.match(line)
        if marker:
            token, rest = marker.groups()
            if fence is None:
                fence = token
                continue
            if token[0] == fence[0] and len(token) >= len(fence) and not rest.strip():
                fence = None
                continue
        if fence is None:
            lines.append((number, line))
    return lines


def heading_slug(heading):
    heading = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", heading)
    heading = HTML_TAG.sub("", heading).lower()
    # GitHub drops punctuation, keeps hyphens and converts each space to a hyphen.
    return re.sub(r"[^\w -]", "", heading).strip().replace(" ", "-")


@cache
def anchors(path):
    page = Page()
    if path.suffix.lower() in {".html", ".htm", ".svg"}:
        page.feed(path.read_text())
        return page.ids
    if path.suffix.lower() != ".md":
        return set()

    used = set()
    suffixes = defaultdict(int)
    last_number, previous = 0, ""
    for number, line in markdown_lines(path):
        page.feed(CODE_SPAN.sub("", line) + "\n")
        atx = HEADING.match(line)
        heading = atx[1] if atx else None
        if SETEXT.fullmatch(line) and number == last_number + 1 and previous.strip():
            if not HEADING.match(previous):
                heading = previous.strip()
        if heading:
            base = slug = heading_slug(heading)
            while slug in used:
                suffixes[base] += 1
                slug = f"{base}-{suffixes[base]}"
            used.add(slug)
        last_number, previous = number, line
    return used | page.ids


def links(path):
    for number, line in markdown_lines(path):
        # Keep Markdown link brackets outside inline code, as in [`name`](path).
        prose = CODE_SPAN.sub("", line)
        for pattern in (INLINE_LINK, REFERENCE):
            for match in pattern.finditer(prose):
                yield number, match[1] or match[2]
        page = Page()
        page.feed(prose)
        for target in page.targets:
            yield number, target


def check(root=ROOT):
    paths = [root / "README.md", root / "AGENTS.md"]
    paths.extend(path for folder in COURSE_DIRS for path in (root / folder).rglob("*.md"))
    errors = []
    checked = 0
    for source in sorted(paths):
        for number, target in links(source):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            checked += 1
            relative = unquote(parsed.path)
            if not relative:
                dest = source
            elif relative.startswith("/"):
                dest = (root / relative.lstrip("/")).resolve()
            else:
                dest = (source.parent / relative).resolve()
            if not dest.is_relative_to(root):
                problem = "target outside repository"
            elif not dest.exists():
                problem = "missing target"
            elif parsed.fragment and dest.suffix.lower() in {".md", ".html", ".htm", ".svg"}:
                if unquote(parsed.fragment) in anchors(dest):
                    continue
                problem = "missing fragment"
            else:
                continue
            errors.append(f"{source.relative_to(root)}:{number}: {problem}: {target}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Course Markdown links passed: {checked} local links across {len(paths)} files.")


if __name__ == "__main__":
    check()
