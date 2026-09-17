"""Unit tests for scripts/loader.py: parsing entries/*.md and categories.yml."""

import pytest

from scripts.loader import (
    DatacardError,
    load_categories,
    load_entries,
    load_experiments,
    load_facilities,
)

CATEGORIES_YAML = """
categories:
  - id: mcp-servers
    title: MCP Servers
    blurb: Servers.
  - id: agent-frameworks
    title: Agent Frameworks
    blurb: Frameworks.
"""

EXPERIMENTS_YAML = """
experiments:
  - name: ATLAS
  - name: CMS
"""

FACILITIES_YAML = """
facilities:
  - name: UChicago
  - name: BNL
"""

VALID_CARD = """---
name: Rucio MCP
url: https://github.com/kratsg/rucio-mcp
description: MCP server exposing Rucio data-management operations to agents
categories: [mcp-servers]
---

Wraps the Rucio client so an agent can list datasets and resolve replicas.
"""


def _write(path, content):
    path.write_text(content, encoding="utf-8")
    return path


def test_load_categories_parses_ordered_list(tmp_path):
    categories_path = _write(tmp_path / "categories.yml", CATEGORIES_YAML)
    categories = load_categories(categories_path)
    assert [c.id for c in categories] == ["mcp-servers", "agent-frameworks"]


def test_load_entries_parses_valid_card(tmp_path):
    categories_path = _write(tmp_path / "categories.yml", CATEGORIES_YAML)
    entries_dir = tmp_path / "entries"
    entries_dir.mkdir()
    _write(entries_dir / "rucio-mcp.md", VALID_CARD)

    categories = load_categories(categories_path)
    entries = load_entries(entries_dir, categories)

    assert len(entries) == 1
    assert entries[0].slug == "rucio-mcp"
    assert entries[0].name == "Rucio MCP"
    assert entries[0].body.strip() == (
        "Wraps the Rucio client so an agent can list datasets and resolve replicas."
    )


def test_load_entries_rejects_missing_frontmatter(tmp_path):
    categories_path = _write(tmp_path / "categories.yml", CATEGORIES_YAML)
    entries_dir = tmp_path / "entries"
    entries_dir.mkdir()
    _write(entries_dir / "broken.md", "no frontmatter here\n")

    categories = load_categories(categories_path)
    with pytest.raises(DatacardError, match="frontmatter"):
        load_entries(entries_dir, categories)


def test_load_entries_rejects_unknown_category(tmp_path):
    categories_path = _write(tmp_path / "categories.yml", CATEGORIES_YAML)
    entries_dir = tmp_path / "entries"
    entries_dir.mkdir()
    bad_card = VALID_CARD.replace("categories: [mcp-servers]", "categories: [not-a-real-category]")
    _write(entries_dir / "rucio-mcp.md", bad_card)

    categories = load_categories(categories_path)
    with pytest.raises(DatacardError, match="not-a-real-category"):
        load_entries(entries_dir, categories)


def test_load_entries_rejects_duplicate_url(tmp_path):
    categories_path = _write(tmp_path / "categories.yml", CATEGORIES_YAML)
    entries_dir = tmp_path / "entries"
    entries_dir.mkdir()
    _write(entries_dir / "rucio-mcp.md", VALID_CARD)
    _write(entries_dir / "rucio-mcp-again.md", VALID_CARD.replace("Rucio MCP", "Rucio MCP Mirror"))

    categories = load_categories(categories_path)
    with pytest.raises(DatacardError, match="duplicate url"):
        load_entries(entries_dir, categories)


def test_load_experiments_parses_ordered_names(tmp_path):
    experiments_path = _write(tmp_path / "experiments.yml", EXPERIMENTS_YAML)
    assert load_experiments(experiments_path) == ["ATLAS", "CMS"]


def test_load_facilities_parses_ordered_names(tmp_path):
    facilities_path = _write(tmp_path / "facilities.yml", FACILITIES_YAML)
    assert load_facilities(facilities_path) == ["UChicago", "BNL"]


def test_load_experiments_rejects_duplicate_names(tmp_path):
    experiments_path = _write(
        tmp_path / "experiments.yml", "experiments:\n  - name: ATLAS\n  - name: ATLAS\n"
    )
    with pytest.raises(DatacardError, match="duplicate"):
        load_experiments(experiments_path)


def test_load_entries_rejects_unknown_experiment(tmp_path):
    categories_path = _write(tmp_path / "categories.yml", CATEGORIES_YAML)
    entries_dir = tmp_path / "entries"
    entries_dir.mkdir()
    bad_card = VALID_CARD.replace("categories: [mcp-servers]", "categories: [mcp-servers]\nexperiments: [DUNE]")
    _write(entries_dir / "rucio-mcp.md", bad_card)

    categories = load_categories(categories_path)
    with pytest.raises(DatacardError, match="DUNE"):
        load_entries(entries_dir, categories, experiments=["ATLAS", "CMS"])


def test_load_entries_rejects_unknown_facility(tmp_path):
    categories_path = _write(tmp_path / "categories.yml", CATEGORIES_YAML)
    entries_dir = tmp_path / "entries"
    entries_dir.mkdir()
    bad_card = VALID_CARD.replace("categories: [mcp-servers]", "categories: [mcp-servers]\nfacilities: [Purdue]")
    _write(entries_dir / "rucio-mcp.md", bad_card)

    categories = load_categories(categories_path)
    with pytest.raises(DatacardError, match="Purdue"):
        load_entries(entries_dir, categories, facilities=["UChicago", "BNL"])


def test_load_entries_skips_scope_check_when_registry_not_given(tmp_path):
    # No experiments=/facilities= passed -- callers that don't care about scope (e.g.
    # existing tests written before this feature) shouldn't have to opt in.
    categories_path = _write(tmp_path / "categories.yml", CATEGORIES_YAML)
    entries_dir = tmp_path / "entries"
    entries_dir.mkdir()
    bad_card = VALID_CARD.replace("categories: [mcp-servers]", "categories: [mcp-servers]\nexperiments: [MADE-UP]")
    _write(entries_dir / "rucio-mcp.md", bad_card)

    categories = load_categories(categories_path)
    entries = load_entries(entries_dir, categories)
    assert entries[0].experiments == ["MADE-UP"]
