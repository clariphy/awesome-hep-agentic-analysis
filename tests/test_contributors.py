"""End-to-end checks on .all-contributorsrc and README.md's All Contributors markers.

Doesn't invoke the all-contributors-cli itself (that's a network-calling Node tool, run
via `pixi run contributors-add`/`contributors-generate`) -- just guards the checked-in
config and markers against going out of sync or getting hand-edited into something the
CLI can no longer parse.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ALL_CONTRIBUTORSRC = ROOT / ".all-contributorsrc"
README = ROOT / "README.md"

REQUIRED_CONTRIBUTOR_KEYS = {"login", "name", "avatar_url", "profile", "contributions"}


def _load_config() -> dict:
    return json.loads(ALL_CONTRIBUTORSRC.read_text(encoding="utf-8"))


def test_config_is_valid_json_with_required_fields():
    config = _load_config()
    assert config["projectName"] == "awesome-hep-agentic-analysis"
    assert config["projectOwner"] == "clariphy"
    assert config["repoType"] == "github"
    assert "README.md" in config["files"]
    assert isinstance(config["contributors"], list)


def test_config_does_not_auto_commit():
    # We commit ourselves after reviewing the diff -- the CLI must never do it for us.
    assert _load_config()["commit"] is False


def test_every_contributor_has_required_fields_and_at_least_one_contribution():
    for contributor in _load_config()["contributors"]:
        missing = REQUIRED_CONTRIBUTOR_KEYS - contributor.keys()
        assert not missing, f"{contributor.get('login', '?')}: missing {missing}"
        assert len(contributor["contributions"]) > 0

    logins = [c["login"] for c in _load_config()["contributors"]]
    assert len(logins) == len(set(logins)), "duplicate contributor login"


def test_readme_has_all_contributors_markers():
    text = README.read_text(encoding="utf-8")
    assert "<!-- ALL-CONTRIBUTORS-BADGE:START" in text
    assert "<!-- ALL-CONTRIBUTORS-BADGE:END" in text
    assert "<!-- ALL-CONTRIBUTORS-LIST:START" in text
    assert "<!-- ALL-CONTRIBUTORS-LIST:END" in text
