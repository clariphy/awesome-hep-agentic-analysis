---
name: Rucio MCP (UChicago-hosted)
url: https://rucio-mcp.af.uchicago.edu/
description:
  Live hosted Rucio MCP endpoint - connect directly, nothing to deploy
categories: [mcp-servers]
experiments: [ATLAS, CMS, DUNE, ESCAPE]
hosted: true
---

A running Rucio MCP endpoint hosted at UChicago, serving the same
[rucio-mcp](https://github.com/kratsg/rucio-mcp) code as a connect-directly
service rather than something you deploy yourself. Untagged for facility
(despite the `af.uchicago.edu` hostname): unlike the AF-branded MCP servers in
this list, you don't need a UChicago AF account to use it — just Rucio
credentials for one of the experiments tagged above.

Useful when: you have Rucio credentials for a supported experiment and want to
connect directly, with nothing to deploy.

Not useful when: your experiment isn't one of the ones tagged above — deploy
[rucio-mcp](https://github.com/kratsg/rucio-mcp) yourself against your own Rucio
instance instead.
