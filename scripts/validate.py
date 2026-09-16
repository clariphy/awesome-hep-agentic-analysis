#!/usr/bin/env python3
"""Validate every entries/*.md datacard against the Entry schema and categories.yml.

Usage:
    pixi run validate
"""

from __future__ import annotations

import sys
from pathlib import Path

from scripts.loader import DatacardError, load_categories, load_entries

ROOT = Path(__file__).resolve().parent.parent
CATEGORIES_YAML = ROOT / "categories.yml"
ENTRIES_DIR = ROOT / "entries"


def main() -> int:
    try:
        categories = load_categories(CATEGORIES_YAML)
        entries = load_entries(ENTRIES_DIR, categories)
    except DatacardError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(f"ok: {len(entries)} entries across {len(categories)} declared categories")
    return 0


if __name__ == "__main__":
    sys.exit(main())
