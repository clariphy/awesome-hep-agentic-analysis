# Contributing

Thanks for wanting to add to this list. A few rules keep it useful instead of
turning into a link dump.

## The first-hand rule

**Only submit a tool you personally use or maintain.** State which in your PR
description. This is deliberately stricter than most awesome-lists: this repo is
meant to be read (by humans and by agents) as a set of recommendations someone
can stand behind, not a scrape of "things that exist." If you've only heard
about a tool, open an issue instead of a PR so someone who actually uses it can
add it.

## AI assistance

AI assistance is fine for _drafting and formatting_ a datacard — writing a first
pass of the description, cleaning up prose, running the generator. It does not
change who is accountable for the entry:

- **A human opens the PR.**
- **That human has visited every URL in the entry** and confirms it's live and
  says what it claims to say.
- **That human vouches for the description and the first-hand rule above** — an
  agent cannot satisfy "you use it or maintain it" on your behalf.
- No bulk or drive-by agent-generated submissions. One entry, one PR, one
  accountable human.

The PR template asks you to confirm each of these explicitly.

## Adding an entry

1. Pick (or propose, in your PR description, if none fit) a category from
   [`categories.yml`](categories.yml).
2. Add `entries/<slug>.md`, where `<slug>` is a lowercase, hyphenated filename
   (this becomes the entry's internal identifier — it does not need to match the
   tool's name). Frontmatter:

   ```yaml
   ---
   name: Tool Name
   url: https://github.com/org/tool # the canonical source repo -- prefer GitHub/GitLab/etc.
   # over that repo's own docs site: most source repos already link their docs, so we
   # don't maintain a second URL that can drift out of sync.
   description: One line, no trailing period, under ~150 characters
   categories: [some-category-id]
   experiments: [ATLAS] # optional -- see "Scoping an entry" below
   facilities: [UChicago] # optional -- see "Scoping an entry" below
   hosted: true # optional, default false -- see "Code vs. a live service" below
   ---

   A short paragraph on what the tool actually does.

   Useful when: ...

   Not useful when: ...
   ```

   The body is the point of this format — write enough that someone (or an
   agent, see [AGENTS.md](AGENTS.md)) can tell whether the tool actually fits
   their situation without leaving this repo. Don't duplicate
   install/auth/version details the linked repo already documents; those go
   stale here and don't there.

   Keep the body timeless: describe what the tool _is_ and _who it's for_, not
   an exhaustive, point-in-time claim about what it currently can or can't do.
   "Only manages X, not Y" or "doesn't support Z yet" reads like a permanent
   limitation but is really a snapshot of today's code — the tool evolves, the
   card doesn't get updated to match, and now it's actively misleading. If a
   limitation genuinely matters, phrase it as what the tool is _for_ ("this
   covers scheduling, not accounting") rather than what it _lacks_. Same goes
   for another party's plans or status (e.g. "X is evaluating this") — link to
   their own material if that context matters, don't restate it here as fact.

3. Run `pixi run generate` and commit the updated `README.md` and `llms.txt`
   alongside your datacard.
4. Run `pixi run check` before opening the PR. CI runs the same thing.

### Scoping an entry: `experiments` and `facilities`

Leave both fields off entirely when a tool is generic: usable by anyone,
regardless of experiment or facility. Add one or both when the tool, **as it
actually exists and is usable today**, requires being a member of that
experiment or having an account at that facility — not when the underlying code
merely _could_ be deployed elsewhere.

The test is: can someone outside that experiment/facility click the link and
have it running? If not, it's scoped. Two examples that came up designing this:

- **AF Filesystem MCP** is generic Helm config that any facility could deploy —
  but the only place it's actually running is UChicago, so it's tagged
  `experiments: [ATLAS]`, `facilities: [UChicago]`. If BNL stands up its own
  deployment, add `BNL` to its `facilities` list rather than creating a second
  entry.
- **Rucio MCP** is untagged. Rucio itself spans many experiments, and which
  instance you reach depends on how the MCP server is configured, not on the
  tool itself — configuration isn't the same thing as scope.

Both fields reference canonical names declared in
[`experiments.yml`](experiments.yml) and [`facilities.yml`](facilities.yml) —
`pixi run validate` rejects a name not declared there. Add a new name to the
relevant file in the same PR as the first entry that needs it, matching the
capitalization already used elsewhere (e.g. `UChicago`, not `uchicago`).

### Code vs. a live service: `hosted`

This is a second, independent axis from scope, and answers a different question:
is `url` something you'd have to build/deploy/run yourself, or can you connect
to it right now?

- **`hosted: false`** (the default): `url` is a source repository. The reader
  still has to install, deploy, or run this themselves — or their facility does,
  on their behalf.
- **`hosted: true`**: `url` is a live, already-running endpoint. Nothing to
  install; you point an MCP client at it and go.

The same underlying software can appear as both, in separate entries: **AF MCP
Platform** (`hosted: false`) is the deployable gateway code, generic and
untagged; **UChicago AF MCP Portal** (`hosted: true`, `experiments: [ATLAS]`,
`facilities: [UChicago]`) is UChicago's actual running instance of it. Don't
collapse these into one card — a reader deciding "can I use this right now?"
needs a different answer than a reader deciding "could I deploy this?", and a
single set of frontmatter can't honestly answer both.

A hosted entry's scope tags describe who the _running service_ is configured
for, which doesn't have to match the software's own generality: **Rucio MCP
(UChicago-hosted)** runs the same generic, untagged
[rucio-mcp](https://github.com/kratsg/rucio-mcp) code, but is tagged
`experiments: [ATLAS, CMS, DUNE, ESCAPE]` because that's what this particular
deployment is configured to serve — with no `facilities` tag, since (unlike the
AF-branded servers) reaching it doesn't require a UChicago account.

## Editing or removing an entry

Same process: edit the `entries/*.md` file, run `pixi run generate`, commit
both. If a tool is dead or has been superseded, open a PR removing its datacard
rather than filing an issue.

## Adding a new category

Categories are declared in [`categories.yml`](categories.yml) independently of
any entry, so a category can exist with zero entries. Propose a new one in the
same PR as the first entry that needs it, and explain in the PR description why
the existing categories don't fit.

## Recognizing contributions

This repo follows the [All Contributors](https://allcontributors.org)
specification. A contribution doesn't have to be a datacard — reviewing PRs,
fixing the generator, writing docs, and reporting issues all count. See the
[emoji key](https://allcontributors.org/en/reference/emoji-key/) for the full
list of contribution types.

Add yourself in the same PR as your contribution:

```bash
pixi run contributors-add <your-github-username> <comma-separated-contribution-types>
pixi run contributors-generate
```

Commit the resulting changes to `.all-contributorsrc` and `README.md` alongside
your other changes.
