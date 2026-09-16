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
3. Recommend only where the card's body confirms the match. If nothing confirms
   a good match, say this list doesn't have one — don't stretch the closest
   entry to fit.
4. Link the entry's `url` so the person can verify for themselves. This list
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
