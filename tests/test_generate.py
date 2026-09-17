"""Integration tests for scripts/generate.py: rendering the README block and llms.txt."""

from scripts.generate import (
    README_END_MARKER,
    README_START_MARKER,
    render_llms_txt,
    render_readme_block,
    rewrite_readme,
)
from scripts.models import Category, Entry

CATEGORIES = [
    Category(id="agent-frameworks", title="Agent Frameworks", blurb="Frameworks that orchestrate agents."),
    Category(id="mcp-servers", title="MCP Servers", blurb="Servers exposing HEP infra to agents."),
    Category(id="skills-plugins", title="Standalone Skills & Plugins", blurb="Individual skills."),
]

ENTRIES = [
    Entry(
        name="Rucio MCP",
        url="https://github.com/kratsg/rucio-mcp",
        description="MCP server exposing Rucio data-management operations to agents",
        categories=["mcp-servers"],
        slug="rucio-mcp",
        body="Body for Rucio MCP.",
    ),
    Entry(
        name="AMI MCP",
        url="https://github.com/kratsg/ami-mcp",
        description="MCP server exposing ATLAS AMI metadata to agents",
        categories=["mcp-servers"],
        experiments=["ATLAS"],
        slug="ami-mcp",
        body="Body for AMI MCP.",
    ),
    Entry(
        name="JFC",
        url="https://github.com/jfc-mit/jfc",
        description="Multi-agent framework for end-to-end HEP analysis",
        categories=["agent-frameworks", "mcp-servers"],
        slug="jfc",
        body="Body for JFC.",
    ),
    Entry(
        name="AF Filesystem MCP",
        url="https://github.com/maniaclab/af-filesystem-mcp",
        description="MCP server for a user's own analysis-facility files",
        categories=["mcp-servers"],
        experiments=["ATLAS"],
        facilities=["UChicago"],
        slug="af-filesystem-mcp",
        body="Body for AF Filesystem MCP.",
    ),
    Entry(
        name="UChicago AF MCP Portal",
        url="https://mcp-portal.af.uchicago.edu/",
        description="Live UChicago AF MCP portal, connect directly",
        categories=["mcp-servers"],
        experiments=["ATLAS"],
        facilities=["UChicago"],
        hosted=True,
        slug="uchicago-af-mcp-portal",
        body="Body for UChicago AF MCP Portal.",
    ),
]


def test_render_readme_block_orders_categories_as_declared():
    block = render_readme_block(ENTRIES, CATEGORIES)
    assert block.index("Agent Frameworks") < block.index("MCP Servers")


def test_render_readme_block_invites_contributions_for_empty_categories():
    block = render_readme_block(ENTRIES, CATEGORIES)
    empty_section = block.split("### Standalone Skills & Plugins")[1]
    assert "contribution" in empty_section.lower()
    assert "CONTRIBUTING.md" in empty_section


def test_render_readme_block_toc_includes_empty_categories():
    block = render_readme_block(ENTRIES, CATEGORIES)
    toc = block.split("###")[0]
    assert "Standalone Skills & Plugins" in toc


def test_render_readme_block_sorts_entries_by_name_within_category():
    block = render_readme_block(ENTRIES, CATEGORIES)
    mcp_section = block.split("### MCP Servers")[1]
    assert mcp_section.index("AMI MCP") < mcp_section.index("Rucio MCP")


def test_render_readme_block_lists_cross_category_entry_in_both_sections():
    block = render_readme_block(ENTRIES, CATEGORIES)
    assert block.count("[JFC]") == 2


def test_render_readme_block_links_use_entry_url_and_description():
    block = render_readme_block(ENTRIES, CATEGORIES)
    assert "[Rucio MCP](https://github.com/kratsg/rucio-mcp)" in block
    assert "MCP server exposing Rucio data-management operations to agents" in block


def test_render_llms_txt_lists_every_entry_with_card_path():
    text = render_llms_txt(ENTRIES)
    assert "entries/rucio-mcp.md" in text
    assert "entries/ami-mcp.md" in text
    assert "entries/jfc.md" in text
    assert "https://github.com/kratsg/rucio-mcp" in text


def test_render_readme_block_shows_no_scope_suffix_for_generic_entry():
    block = render_readme_block(ENTRIES, CATEGORIES)
    rucio_line = next(line for line in block.splitlines() if "Rucio MCP" in line)
    assert not rucio_line.rstrip().endswith(")")


def test_render_readme_block_shows_experiment_tag():
    block = render_readme_block(ENTRIES, CATEGORIES)
    ami_line = next(line for line in block.splitlines() if "AMI MCP" in line)
    assert "(ATLAS)" in ami_line


def test_render_readme_block_shows_experiment_and_facility_tags():
    block = render_readme_block(ENTRIES, CATEGORIES)
    af_line = next(line for line in block.splitlines() if "AF Filesystem MCP" in line)
    assert "(ATLAS · UChicago)" in af_line


def test_render_llms_txt_marks_generic_entries_explicitly():
    text = render_llms_txt(ENTRIES)
    rucio_line = next(line for line in text.splitlines() if "Rucio MCP" in line)
    assert "| generic |" in rucio_line


def test_render_llms_txt_lists_scope_tags():
    text = render_llms_txt(ENTRIES)
    af_line = next(line for line in text.splitlines() if "AF Filesystem MCP" in line)
    assert "| ATLAS, UChicago |" in af_line


def test_render_readme_block_marks_hosted_entries():
    block = render_readme_block(ENTRIES, CATEGORIES)
    portal_line = next(line for line in block.splitlines() if "UChicago AF MCP Portal" in line)
    assert "(hosted · ATLAS · UChicago)" in portal_line


def test_render_readme_block_does_not_mark_non_hosted_entries():
    block = render_readme_block(ENTRIES, CATEGORIES)
    af_line = next(line for line in block.splitlines() if "AF Filesystem MCP" in line and "Portal" not in line)
    assert "hosted" not in af_line


def test_render_llms_txt_marks_hosted_entries():
    text = render_llms_txt(ENTRIES)
    portal_line = next(line for line in text.splitlines() if "UChicago AF MCP Portal" in line)
    assert "| hosted, ATLAS, UChicago |" in portal_line


def test_rewrite_readme_replaces_only_between_markers():
    original = (
        "# Title\n\nHand-written intro.\n\n"
        f"{README_START_MARKER}\nstale content\n{README_END_MARKER}\n\n"
        "Hand-written outro.\n"
    )
    updated = rewrite_readme(original, "fresh content\n")
    assert "Hand-written intro." in updated
    assert "Hand-written outro." in updated
    assert "stale content" not in updated
    assert "fresh content" in updated


def test_rewrite_readme_is_idempotent():
    original = (
        f"# Title\n\n{README_START_MARKER}\nfresh content\n{README_END_MARKER}\n"
    )
    once = rewrite_readme(original, "fresh content\n")
    twice = rewrite_readme(once, "fresh content\n")
    assert once == twice
