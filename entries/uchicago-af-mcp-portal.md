---
name: UChicago AF MCP Portal
url: https://mcp-portal.af.uchicago.edu/
description: Live UChicago AF MCP portal - connect directly, nothing to deploy
categories: [mcp-servers]
experiments: [ATLAS]
facilities: [UChicago]
hosted: true
---

The running instance of
[AF MCP Platform](https://github.com/maniaclab/af-mcp-platform) at the UChicago
ATLAS Analysis Facility: a browser-facing portal with its own OIDC login that
fronts the same `/v1` and `/mcp` routes the platform's credential-brokered
gateway serves. Unlike the AF MCP Platform card, this one is `hosted: true` —
there's nothing to install; you log in and connect.

Useful when: you have a UChicago AF account and want to connect an MCP client to
Rucio/AMI/HTCondor/Jupyter/etc. right now, without deploying anything.

Not useful when: you're not at UChicago (there's nothing for you to log into),
or you want the deployable software itself — that's
[AF MCP Platform](https://github.com/maniaclab/af-mcp-platform).
