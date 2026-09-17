"""Loading and cross-validating datacards (entries/*.md) against categories.yml,
experiments.yml, and facilities.yml.

Both scripts/generate.py and scripts/validate.py need the same load-and-check logic, so
it lives here once rather than being duplicated between the two entry points.
"""

from __future__ import annotations

from pathlib import Path

import yaml

from scripts.models import Category, Entry, ScopeTagDef

_FRONTMATTER_FENCE = "---"


class DatacardError(ValueError):
    """Raised when a registry file or an entries/*.md file fails to parse or cross-validate."""


def load_categories(path: Path) -> list[Category]:
    """Load the ordered category taxonomy from categories.yml."""
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return [Category.model_validate(raw) for raw in data["categories"]]


def _load_scope_registry(path: Path, key: str) -> list[str]:
    """Load the canonical name list from experiments.yml or facilities.yml."""
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    names = [ScopeTagDef.model_validate(raw).name for raw in data[key]]
    if len(names) != len(set(names)):
        raise DatacardError(f"{path}: duplicate names in the registry")
    return names


def load_experiments(path: Path) -> list[str]:
    """Load the canonical experiment name list from experiments.yml."""
    return _load_scope_registry(path, "experiments")


def load_facilities(path: Path) -> list[str]:
    """Load the canonical facility name list from facilities.yml."""
    return _load_scope_registry(path, "facilities")


def _split_frontmatter(text: str, source: Path) -> tuple[dict, str]:
    """Split a datacard into its YAML frontmatter (as a dict) and markdown body."""
    header = f"{_FRONTMATTER_FENCE}\n"
    if not text.startswith(header):
        raise DatacardError(f"{source}: missing YAML frontmatter (must start with '---')")
    _, _, rest = text.partition(header)
    frontmatter_text, fence_found, body = rest.partition(f"\n{_FRONTMATTER_FENCE}\n")
    if not fence_found:
        raise DatacardError(f"{source}: unterminated YAML frontmatter (missing closing '---')")
    frontmatter = yaml.safe_load(frontmatter_text) or {}
    return frontmatter, body.strip("\n")


def load_entry(path: Path) -> Entry:
    """Load and validate a single entries/*.md datacard (without cross-checking categories)."""
    frontmatter, body = _split_frontmatter(path.read_text(encoding="utf-8"), path)
    try:
        return Entry.model_validate({**frontmatter, "slug": path.stem, "body": body})
    except Exception as exc:  # re-raise with the offending file named, per RTK.md
        raise DatacardError(f"{path}: {exc}") from exc


def _check_all_known(
    tags: list[str], known: set[str], singular: str, plural: str, path: Path, registry_file: str
) -> None:
    unknown = [tag for tag in tags if tag not in known]
    if unknown:
        noun = singular if len(unknown) == 1 else plural
        raise DatacardError(f"{path}: unknown {noun} {unknown!r} (not declared in {registry_file})")


def load_entries(
    directory: Path,
    categories: list[Category],
    experiments: list[str] | None = None,
    facilities: list[str] | None = None,
) -> list[Entry]:
    """Load every entries/*.md datacard, sorted by filename, cross-validated against categories.

    `experiments`/`facilities` are the canonical name lists from experiments.yml/
    facilities.yml. Passing None (the default) skips that particular check -- callers
    that don't care about scope tags don't have to load registries they won't use.
    """
    known_category_ids = {category.id for category in categories}
    paths = sorted(directory.glob("*.md"))
    entries = [load_entry(path) for path in paths]
    for entry, path in zip(entries, paths):
        _check_all_known(entry.categories, known_category_ids, "category", "categories", path, "categories.yml")
        if experiments is not None:
            _check_all_known(
                entry.experiments, set(experiments), "experiment", "experiments", path, "experiments.yml"
            )
        if facilities is not None:
            _check_all_known(
                entry.facilities, set(facilities), "facility", "facilities", path, "facilities.yml"
            )
    _check_no_duplicate_urls(entries)
    return entries


def _check_no_duplicate_urls(entries: list[Entry]) -> None:
    seen: dict[str, str] = {}
    for entry in entries:
        url = str(entry.url)
        if url in seen:
            raise DatacardError(
                f"{entry.slug}.md: duplicate url {url!r}, also used by {seen[url]}.md"
            )
        seen[url] = entry.slug
