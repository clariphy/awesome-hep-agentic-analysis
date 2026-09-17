"""Unit tests for scripts/models.py: the Entry and Category pydantic models."""

import pytest
from pydantic import ValidationError

from scripts.models import Category, Entry, ScopeTagDef

VALID_ENTRY = {
    "name": "Rucio MCP",
    "url": "https://github.com/kratsg/rucio-mcp",
    "description": "MCP server exposing Rucio data-management operations to agents",
    "categories": ["mcp-servers"],
    "slug": "rucio-mcp",
    "body": "Wraps the Rucio client so an agent can list datasets and resolve replicas.",
}


def test_valid_entry_round_trips():
    entry = Entry.model_validate(VALID_ENTRY)
    assert entry.name == "Rucio MCP"
    assert str(entry.url) == "https://github.com/kratsg/rucio-mcp"
    assert entry.categories == ["mcp-servers"]


@pytest.mark.parametrize(
    "url",
    ["not-a-url", "ftp://example.com/x", ""],
)
def test_entry_rejects_bad_url(url):
    with pytest.raises(ValidationError):
        Entry.model_validate({**VALID_ENTRY, "url": url})


def test_entry_rejects_empty_categories():
    with pytest.raises(ValidationError):
        Entry.model_validate({**VALID_ENTRY, "categories": []})


def test_entry_rejects_multiline_description():
    with pytest.raises(ValidationError):
        Entry.model_validate({**VALID_ENTRY, "description": "line one\nline two"})


def test_entry_rejects_description_ending_in_period():
    with pytest.raises(ValidationError):
        Entry.model_validate({**VALID_ENTRY, "description": "Ends with a period."})


def test_entry_rejects_overlong_description():
    with pytest.raises(ValidationError):
        Entry.model_validate({**VALID_ENTRY, "description": "x" * 200})


def test_entry_rejects_empty_body():
    with pytest.raises(ValidationError):
        Entry.model_validate({**VALID_ENTRY, "body": "   "})


def test_entry_defaults_to_generic_scope():
    entry = Entry.model_validate(VALID_ENTRY)
    assert entry.experiments == []
    assert entry.facilities == []


def test_entry_defaults_to_not_hosted():
    assert Entry.model_validate(VALID_ENTRY).hosted is False


def test_entry_accepts_hosted_flag():
    entry = Entry.model_validate({**VALID_ENTRY, "hosted": True})
    assert entry.hosted is True


def test_entry_accepts_experiment_and_facility_tags():
    entry = Entry.model_validate(
        {**VALID_ENTRY, "experiments": ["ATLAS"], "facilities": ["UChicago"]}
    )
    assert entry.experiments == ["ATLAS"]
    assert entry.facilities == ["UChicago"]


@pytest.mark.parametrize("field", ["experiments", "facilities"])
def test_entry_rejects_blank_scope_tag(field):
    with pytest.raises(ValidationError):
        Entry.model_validate({**VALID_ENTRY, field: ["ATLAS", "  "]})


@pytest.mark.parametrize("field", ["experiments", "facilities"])
def test_entry_rejects_duplicate_scope_tags(field):
    with pytest.raises(ValidationError):
        Entry.model_validate({**VALID_ENTRY, field: ["ATLAS", "ATLAS"]})


def test_category_accepts_valid_slug():
    category = Category.model_validate(
        {"id": "mcp-servers", "title": "MCP Servers", "blurb": "Servers."}
    )
    assert category.id == "mcp-servers"


@pytest.mark.parametrize("bad_id", ["MCP-Servers", "mcp_servers", "mcp servers", "-mcp", "mcp-"])
def test_category_rejects_non_slug_id(bad_id):
    with pytest.raises(ValidationError):
        Category.model_validate({"id": bad_id, "title": "x", "blurb": "y"})


def test_scope_tag_def_accepts_a_clean_name():
    assert ScopeTagDef.model_validate({"name": "ATLAS"}).name == "ATLAS"


@pytest.mark.parametrize("bad_name", ["", "   ", " ATLAS", "ATLAS "])
def test_scope_tag_def_rejects_blank_or_padded_name(bad_name):
    with pytest.raises(ValidationError):
        ScopeTagDef.model_validate({"name": bad_name})
