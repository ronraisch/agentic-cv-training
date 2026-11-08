"""Check local reading navigation and the original-source destination inventory."""

import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
READING = ROOT / "docs" / "reading"


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.targets = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag in {"a", "link", "img", "script"}:
            target = attrs.get("href") or attrs.get("src")
            if target:
                self.targets.append(target)


def check():
    pages = {}
    errors = []
    for path in READING.glob("*.html"):
        page = Page()
        page.feed(path.read_text())
        pages[path.resolve()] = page
    for path, page in pages.items():
        for target in page.targets:
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            dest = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if not dest.is_relative_to(ROOT):
                errors.append(f"{path.name}: target outside repository: {target}")
            elif not dest.exists():
                errors.append(f"{path.name}: missing {target}")
            elif parsed.fragment and dest in pages:
                if unquote(parsed.fragment) not in pages[dest].ids:
                    errors.append(f"{path.name}: missing anchor {target}")
    chapters = json.loads((READING / "chapters.json").read_text())
    for chapter in chapters:
        target = chapter["slug"] + ".html"
        path = (READING / target).resolve()
        stage = (READING / (chapter["stage"] + ".html")).resolve()
        if path not in pages or stage not in pages:
            errors.append(f"Missing chapter or syllabus for {target}")
        elif target not in pages[stage].targets:
            errors.append(f"Chapter not linked by its stage: {target}")
    records = json.loads((READING / "source-map.json").read_text())
    for record in records:
        if record["kind"] in {"needs-review", "legacy-reference", "archive-navigation"}:
            errors.append(f"Unresolved source disposition: {record['url']}")
        targets = [record.get("local")] + record.get("also", [])
        if record["kind"] in {"reading", "retained-handout"} and not targets[0]:
            errors.append(f"Reading has no local destination: {record['url']}")
        for target in targets:
            if target and not (READING / target).is_file():
                errors.append(f"Source map destination missing: {target}")
    if errors:
        raise SystemExit("\n".join(sorted(set(errors))))
    print(
        f"Reading navigation passed: {len(pages)} HTML pages, "
        f"{len(chapters)} chapters, {len(records)} source occurrences."
    )


if __name__ == "__main__":
    check()
