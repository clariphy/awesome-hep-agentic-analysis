---
name: Rucio MCP (UChicago-hosted)
url: https://rucio-mcp.af.uchicago.edu/
description: Live hosted Rucio MCP endpoint for ATLAS, CMS, DUNE, and ESCAPE
categories: [mcp-servers]
experiments: [ATLAS, CMS, DUNE, ESCAPE]
hosted: true
---

A running Rucio MCP endpoint hosted at UChicago, serving the same
[rucio-mcp](https://github.com/kratsg/rucio-mcp) code as a connect-directly
service rather than something you deploy yourself. Untagged for facility
(despite the `af.uchicago.edu` hostname): unlike the AF-branded MCP servers in
this list, you don't need a UChicago AF account to use it — it's configured
for Rucio users of ATLAS, CMS, DUNE, and ESCAPE specifically, wherever they are.

Useful when: you have Rucio credentials for one of ATLAS, CMS, DUNE, or ESCAPE
and want to connect an MCP client directly, with nothing to deploy.

Not useful when: your experiment isn't one of the four this instance is
configured for — deploy [rucio-mcp](https://github.com/kratsg/rucio-mcp)
yourself against your own Rucio instance instead.
