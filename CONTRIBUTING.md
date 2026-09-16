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

3. Run `pixi run generate` and commit the updated `README.md` and `llms.txt`
   alongside your datacard.
4. Run `pixi run check` before opening the PR. CI runs the same thing.

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
