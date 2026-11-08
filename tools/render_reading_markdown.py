"""Publish GitHub-readable mirrors of the offline HTML reading shelf."""

import argparse
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
READING = ROOT / 'docs' / 'reading'


class Node:
    def __init__(self, tag='', attrs=None):
        self.tag = tag
        self.attrs = dict(attrs or [])
        self.children = []


class Document(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node()
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs)
        self.stack[-1].children.append(node)
        if tag not in {'img', 'br', 'meta', 'link', 'hr', 'input', 'wbr'}:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                return

    def handle_data(self, data):
        self.stack[-1].children.append(data)


def walk(node):
    if isinstance(node, Node):
        yield node
        for child in node.children:
            yield from walk(child)


def local_link(url):
    parts = urlsplit(url)
    if not parts.scheme and not parts.netloc and parts.path.endswith('.html'):
        return urlunsplit(parts._replace(path=parts.path[:-5] + '.md'))
    return url


def math(node):
    if isinstance(node, str):
        return node
    children = [math(c) for c in node.children]
    if node.tag == 'mfrac':
        return r'\frac{' + children[0] + '}{' + children[1] + '}'
    if node.tag in {'msub', 'msup'}:
        return '{' + children[0] + '}' + ('_' if node.tag == 'msub' else '^') + '{' + children[1] + '}'
    if node.tag == 'msubsup':
        return '{' + children[0] + '}_{' + children[1] + '}^{' + children[2] + '}'
    if node.tag == 'msqrt':
        return r'\sqrt{' + ''.join(children) + '}'
    if node.tag == 'munderover':
        return children[0] + '_{' + children[1] + '}^{' + children[2] + '}'
    text = ''.join(children)
    for char, command in {'∑':r'\sum ', '∞':r'\infty ', '∈':r'\in ', '≥':r'\ge ', '≤':r'\le ', '−':'-', '×':r'\times ', 'α':r'\alpha ', 'β':r'\beta ', 'θ':r'\theta '}.items():
        text = text.replace(char, command)
    return text


def render(node):
    if isinstance(node, str):
        return node
    tag = node.tag
    if tag == 'math':
        return '$' + math(node).strip() + '$'
    content = ''.join(render(c) for c in node.children)
    if tag in {'script', 'style', 'nav'}:
        return ''
    if tag in {'h1', 'h2', 'h3', 'h4'}:
        return '\n\n' + '#' * int(tag[1]) + ' ' + content.strip() + '\n\n'
    if tag in {'p', 'div', 'section', 'details', 'ul', 'ol'}:
        return '\n\n' + content.strip() + '\n\n'
    if tag == 'summary':
        return '\n\n### ' + content.strip() + '\n\n'
    if tag == 'li':
        return '\n- ' + content.strip() + '\n'
    if tag == 'br':
        return '<br>'
    if tag == 'strong' or tag == 'b':
        return '**' + content + '**'
    if tag in {'em', 'i'}:
        return '*' + content + '*'
    if tag == 'pre':
        return '\n\n```text\n' + content.strip('`\n') + '\n```\n\n'
    if tag == 'code':
        return '`' + content + '`'
    if tag == 'a':
        return '[' + content.strip() + '](' + local_link(node.attrs.get('href', '')) + ')'
    if tag == 'img':
        return '![' + node.attrs.get('alt', 'Figure') + '](' + node.attrs.get('src', '') + ')'
    if tag == 'table':
        rows = []
        for row in walk(node):
            if row.tag == 'tr':
                cells = [re.sub(r'\s+', ' ', render(c)).strip().replace('|', r'\|') for c in row.children if isinstance(c, Node) and c.tag in {'th', 'td'}]
                if cells:
                    rows.append(cells)
        if not rows:
            return ''
        width = max(map(len, rows))
        rows = [row + [''] * (width - len(row)) for row in rows]
        lines = ['| ' + ' | '.join(row) + ' |' for row in rows]
        lines.insert(1, '| ' + ' | '.join(['---'] * width) + ' |')
        return '\n\n' + '\n'.join(lines) + '\n\n'
    return content


def convert(path):
    document = Document()
    document.feed(path.read_text())
    nodes = list(walk(document.root))
    title = next(n for n in nodes if n.tag == 'h1')
    main = next(n for n in nodes if n.tag == 'main')
    body = render(title) + '\n[All training](index.md) · [Source coverage](sources.md)\n\n' + render(main)
    return re.sub(r'\n{3,}', '\n\n', body).strip() + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    stale = []
    for path in sorted(READING.glob('*.html')):
        target = path.with_suffix('.md')
        content = convert(path)
        if args.check:
            if not target.exists() or target.read_text() != content:
                stale.append(str(target.relative_to(ROOT)))
        else:
            target.write_text(content)
    if stale:
        raise SystemExit('Regenerate reading Markdown: python tools/render_reading_markdown.py\n' + '\n'.join(stale))
    print('GitHub reading mirrors verified.' if args.check else 'GitHub reading mirrors generated.')


if __name__ == '__main__':
    main()
