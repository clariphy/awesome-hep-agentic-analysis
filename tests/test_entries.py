"""End-to-end test: parse the *real* entries/ and categories.yml, no mocks."""

from pathlib import Path

from scripts.loader import load_categories, load_entries

ROOT = Path(__file__).resolve().parent.parent


def test_real_entries_all_validate_and_cross_reference_cleanly():
    categories = load_categories(ROOT / "categories.yml")
    entries = load_entries(ROOT / "entries", categories)

    assert len(entries) > 0

    slugs = [entry.slug for entry in entries]
    assert len(slugs) == len(set(slugs)), "duplicate slugs found"

    urls = [str(entry.url) for entry in entries]
    assert len(urls) == len(set(urls)), "duplicate urls found"

    known_ids = {category.id for category in categories}
    for entry in entries:
        assert set(entry.categories) <= known_ids, f"{entry.slug}: unknown category"
