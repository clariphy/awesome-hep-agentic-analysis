# AGENTS.md

This file has two audiences. Read the section that matches what you're doing.

## If you're using this list to answer "what should I use for X?"

Follow this protocol rather than answering from the README table alone:

1. Read [`README.md`](README.md) (or [`llms.txt`](llms.txt) for a flat,
   single-fetch index) to shortlist candidates by category and one-line
   description.
2. **Do not recommend from the one-liner alone.** Open every shortlisted card
   under [`entries/`](entries/) (the path is in `llms.txt`) and read its
   frontmatter and body. The body says when the tool applies and, just as
   importantly, when it doesn't.
3. **Check the entry's scope before recommending it.** A `(ATLAS · UChicago)`
   suffix in the README, or a non-"generic" `scope` field in `llms.txt`, means
   the tool is only actually usable by someone in that experiment and/or at that
   facility — not merely "related to" it. No suffix means generic: usable by
   anyone, tied to nothing specific. If you don't know the person's
   experiment/facility and an entry is scoped, ask, or say so explicitly rather
   than recommending it and letting them discover the mismatch themselves.
4. **Check whether it's code or a live service.** A `hosted` tag (the leading
   word inside the parenthetical, or the leading word of the `scope` field in
   `llms.txt`) means `url` is a running endpoint you connect to directly —
   nothing to deploy. No `hosted` tag means `url` is source code the person (or
   their facility) has to build/deploy/run themselves. Someone asking "what can
   I use right now" wants a `hosted` entry; someone asking "what should our
   facility stand up" wants the unhosted code, even when both exist for the same
   tool (e.g. AF MCP Platform vs. UChicago AF MCP Portal). Don't hand someone a
   repo when they wanted something they could connect to today, or vice versa.
5. Recommend only where the card's body confirms the match. If nothing confirms
   a good match, say this list doesn't have one — don't stretch the closest
   entry to fit.
6. Link the entry's `url` so the person can verify for themselves. This list
   deliberately does not track auth, install steps, or version numbers — the
   linked repo owns that, and it goes stale here faster than there.

## If you're editing this repo

- Never invent an entry. Every datacard here represents someone's first-hand
  claim that they use or maintain the tool (see
  [CONTRIBUTING.md](CONTRIBUTING.md)) — you cannot satisfy that on a human's
  behalf. If asked to add one you have no such claim for, say so and ask the
  human to confirm they use it, rather than adding it anyway.
- Never hand-edit the content between `<!-- UPDATE:START -->` and
  `<!-- UPDATE:END -->` in `README.md`, or `llms.txt` directly. Both are
  generated from `entries/` and `categories.yml` by `pixi run generate` — edit
  the source, then regenerate.
- Run `pixi run check` (validates entries, confirms generated files are current,
  lints, tests) before committing.
- Escalate to the human rather than guessing when a task requires first-hand
  knowledge of a tool you can't verify (e.g. writing a datacard's "useful when /
  not useful when" guidance for something neither of you has used).
