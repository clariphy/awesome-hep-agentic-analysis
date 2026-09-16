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
