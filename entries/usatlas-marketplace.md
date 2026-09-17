---
name: USATLAS Marketplace
url: https://github.com/usatlas/marketplace
description:
  Claude Code plugin marketplace covering ATLAS analysis facilities and the full
  ATLAS software stack
categories: [marketplaces]
experiments: [ATLAS]
facilities: [BNL, UChicago]
---

A Claude Code plugin marketplace for ATLAS physics analysis, with four plugins:
`af-bnl` (BNL LOCALGROUPDISK storage migration), `af-uchicago` (HTCondor,
JupyterLab, XCache, Rucio, ServiceX, Coffea Casa, Triton, and the AF MCP
Platform), `atlas` (subagents for analysis
architecture/coding/data-exploration/statistics, plus ~40 skills spanning pyhf,
cabinetry, TRExFitter, coffea, awkward, uproot, and ATLAS software setup), and
`hep-python-tools` (generic HEP Python tooling).

The BNL/UChicago tags cover only `af-bnl`/`af-uchicago`: those two plugins are
useless without an account at that specific facility. `atlas` and
`hep-python-tools` work for any ATLAS member anywhere, install and all.

Useful when: you use Claude Code for ATLAS analysis and want skills/agents for a
specific US ATLAS analysis facility, or for the ATLAS statistics and
analysis-framework stack.

Not useful when: you're working on a non-ATLAS experiment — most of its plugins
are ATLAS-specific by design.
