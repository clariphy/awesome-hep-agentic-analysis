"""Pydantic models for datacards (entries/*.md) and the category taxonomy (categories.yml)."""

from __future__ import annotations

import re

from pydantic import BaseModel, Field, HttpUrl, field_validator

_SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

# awesome-lint convention: short, no trailing period, so it reads well as a bullet.
MAX_DESCRIPTION_LENGTH = 150


class Category(BaseModel):
    """One section of the generated README, declared in categories.yml."""

    id: str
    title: str
    blurb: str

    @field_validator("id")
    @classmethod
    def _id_is_slug(cls, value: str) -> str:
        if not _SLUG_RE.match(value):
            raise ValueError(f"category id {value!r} must be a lowercase, hyphenated slug")
        return value


class ScopeTagDef(BaseModel):
    """One canonical name in experiments.yml or facilities.yml.

    Entries reference these by exact string match (see Entry.experiments/facilities), so
    the registry is what keeps "UChicago" from also showing up as "uchicago" or
    "U Chicago" somewhere else.
    """

    name: str

    @field_validator("name")
    @classmethod
    def _name_is_clean(cls, value: str) -> str:
        if value != value.strip() or not value:
            raise ValueError(f"name {value!r} must be non-empty with no leading/trailing whitespace")
        return value


class Entry(BaseModel):
    """One datacard: the frontmatter plus body of a single entries/*.md file.

    `slug` and `body` are not part of the YAML frontmatter -- they are derived from the
    filename and the markdown content below the frontmatter, and supplied by the loader
    (scripts/loader.py) rather than by the file's frontmatter itself.
    """

    name: str
    url: HttpUrl
    description: str
    categories: list[str] = Field(min_length=1)
    # Empty means generic/universal: usable by anyone, tied to no specific experiment or
    # facility. A non-empty list means the tool, as it exists and is actually usable
    # today, requires membership in that experiment or access to that facility -- e.g. an
    # ATLAS-only metadata service, or an MCP server only deployed at one analysis
    # facility. See CONTRIBUTING.md for how to choose these.
    experiments: list[str] = Field(default_factory=list)
    facilities: list[str] = Field(default_factory=list)
    # False (default): `url` is source code -- a repo someone builds/deploys/runs. True:
    # `url` is a live, already-running endpoint you connect an MCP client to directly,
    # with nothing to install. The same software can be both: e.g. AF MCP Platform is
    # the (generic, unhosted) code, while a separate hosted entry covers a specific
    # live deployment of it.
    hosted: bool = False
    slug: str
    body: str

    @field_validator("description")
    @classmethod
    def _description_is_a_single_clean_line(cls, value: str) -> str:
        if "\n" in value:
            raise ValueError("description must be a single line")
        if value.endswith("."):
            raise ValueError("description must not end with a period (awesome-lint convention)")
        if len(value) > MAX_DESCRIPTION_LENGTH:
            raise ValueError(
                f"description is {len(value)} characters, longer than the "
                f"{MAX_DESCRIPTION_LENGTH}-character limit"
            )
        return value

    @field_validator("body")
    @classmethod
    def _body_is_non_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("body must not be empty -- a card with no detail is not a card")
        return value

    @field_validator("experiments", "facilities")
    @classmethod
    def _scope_tags_are_clean_and_unique(cls, value: list[str]) -> list[str]:
        if any(not tag.strip() for tag in value):
            raise ValueError("scope tags must not be blank")
        if len(value) != len(set(value)):
            raise ValueError("scope tags must not repeat")
        return value
