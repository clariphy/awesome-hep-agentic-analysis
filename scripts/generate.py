#!/usr/bin/env python3
"""Regenerate the README's generated block and llms.txt from entries/ and categories.yml.

Usage:
    pixi run generate         # rewrite README.md and llms.txt in place
    pixi run check-generated  # (--check) exit 1 if either file is out of date
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from scripts.loader import load_categories, load_entries
from scripts.models import Category, Entry

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
LLMS_TXT = ROOT / "llms.txt"
CATEGORIES_YAML = ROOT / "categories.yml"
ENTRIES_DIR = ROOT / "entries"

README_START_MARKER = "<!-- UPDATE:START -->"
README_END_MARKER = "<!-- UPDATE:END -->"

_LLMS_TXT_HEADER = """\
# awesome-hep-agentic-analysis

> Flat index of every entry in this list, for agents that want to discover it in one
> fetch. Each line is `name | url | description | card path`. Read the linked card
> (entries/<slug>.md) before recommending an entry -- the one-liner here is a shortlist,
> not a verdict. See AGENTS.md for the full retrieval protocol.
"""


def _entries_by_category(entries: list[Entry], category: Category) -> list[Entry]:
    matching = [entry for entry in entries if category.id in entry.categories]
    return sorted(matching, key=lambda entry: entry.name.casefold())


_EMPTY_CATEGORY_INVITE = "_No entries yet. [Contributions welcome!](CONTRIBUTING.md)_"


def render_readme_block(entries: list[Entry], categories: list[Category]) -> str:
    """Render the per-category sections that live between the README markers.

    Categories are emitted in the order given (the declared order in categories.yml). A
    category with no matching entries still gets a section -- with an invite to
    contribute instead of bullets -- so the full taxonomy is visible up front.
    """
    by_category = [(category, _entries_by_category(entries, category)) for category in categories]

    toc_lines = [f"- [{category.title}](#{_anchor(category.title)})" for category, _ in by_category]
    sections = []
    for category, matches in by_category:
        body = (
            "\n".join(f"- [{entry.name}]({entry.url}) - {entry.description}" for entry in matches)
            if matches
            else _EMPTY_CATEGORY_INVITE
        )
        sections.append(f"### {category.title}\n\n{category.blurb}\n\n{body}")

    return "\n".join(toc_lines) + "\n\n" + "\n\n".join(sections) + "\n"


def _anchor(title: str) -> str:
    """GitHub's markdown heading-anchor algorithm: lowercase, spaces to hyphens, strip punctuation."""
    slug = title.lower().replace(" ", "-")
    return "".join(ch for ch in slug if ch.isalnum() or ch == "-")


def render_llms_txt(entries: list[Entry]) -> str:
    """Render llms.txt: a flat, agent-readable index of every entry with its card path."""
    lines = [
        f"{entry.name} | {entry.url} | {entry.description} | entries/{entry.slug}.md"
        for entry in sorted(entries, key=lambda entry: entry.name.casefold())
    ]
    return _LLMS_TXT_HEADER + "\n" + "\n".join(lines) + "\n"


def rewrite_readme(original: str, block: str) -> str:
    """Replace only the text between the README markers, leaving hand-written prose untouched."""
    before, sep_start, rest = original.partition(README_START_MARKER)
    if not sep_start:
        raise ValueError(f"README is missing {README_START_MARKER!r}")
    _, sep_end, after = rest.partition(README_END_MARKER)
    if not sep_end:
        raise ValueError(f"README is missing {README_END_MARKER!r}")
    return f"{before}{README_START_MARKER}\n{block}{README_END_MARKER}{after}"


def _load() -> tuple[list[Entry], list[Category]]:
    categories = load_categories(CATEGORIES_YAML)
    entries = load_entries(ENTRIES_DIR, categories)
    return entries, categories


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="exit 1 if README.md or llms.txt would change, without writing anything",
    )
    args = parser.parse_args(argv)

    entries, categories = _load()
    new_readme = rewrite_readme(README.read_text(encoding="utf-8"), render_readme_block(entries, categories))
    new_llms_txt = render_llms_txt(entries)

    if args.check:
        stale = []
        if README.read_text(encoding="utf-8") != new_readme:
            stale.append(README.name)
        if not LLMS_TXT.exists() or LLMS_TXT.read_text(encoding="utf-8") != new_llms_txt:
            stale.append(LLMS_TXT.name)
        if stale:
            print(f"out of date: {', '.join(stale)} (run `pixi run generate`)", file=sys.stderr)
            return 1
        return 0

    README.write_text(new_readme, encoding="utf-8")
    LLMS_TXT.write_text(new_llms_txt, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
