---
name: IRIS-HEP Marketplace
url: https://github.com/iris-hep/marketplace
description:
  Claude Code plugin marketplace with skills for awkward, hist, ServiceX, and
  building HEP analyses
categories: [marketplaces]
experiments: [ATLAS]
---

A Claude Code plugin marketplace hosted by IRIS-HEP. Its `iris-hep` plugin ships
agents for ATLAS analysis planning and plotting, a command for scaffolding a HEP
analysis plan, and skills covering `awkward`, `hist`, `servicex`, a
standalone-script template, and building a structured analysis specification.
Tagged ATLAS because the headline agents are ATLAS-branded today; the
`awkward`/`hist`/`servicex`/`vector-awkward` skills underneath are themselves
generic and not tied to any one experiment.

Useful when: you use Claude Code and want ready-made skills for the Scikit-HEP
array stack (awkward, hist, vector) and ServiceX, or a starting point for an
analysis spec.

Not useful when: you're not using Claude Code (or a marketplace-compatible
client) — this is a plugin distribution mechanism, not a standalone tool.
