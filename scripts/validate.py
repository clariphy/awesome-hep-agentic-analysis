#!/usr/bin/env python3
"""Validate every entries/*.md datacard against the Entry schema, categories.yml,
experiments.yml, and facilities.yml.

Usage:
    pixi run validate
"""

from __future__ import annotations

import sys
from pathlib import Path

from scripts.loader import DatacardError, load_categories, load_entries, load_experiments, load_facilities

ROOT = Path(__file__).resolve().parent.parent
CATEGORIES_YAML = ROOT / "categories.yml"
EXPERIMENTS_YAML = ROOT / "experiments.yml"
FACILITIES_YAML = ROOT / "facilities.yml"
ENTRIES_DIR = ROOT / "entries"


def main() -> int:
    try:
        categories = load_categories(CATEGORIES_YAML)
        experiments = load_experiments(EXPERIMENTS_YAML)
        facilities = load_facilities(FACILITIES_YAML)
        entries = load_entries(ENTRIES_DIR, categories, experiments, facilities)
    except DatacardError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(f"ok: {len(entries)} entries across {len(categories)} declared categories")
    return 0


if __name__ == "__main__":
    sys.exit(main())
