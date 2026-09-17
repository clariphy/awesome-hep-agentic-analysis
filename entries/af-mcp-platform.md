---
name: AF MCP Platform
url: https://github.com/maniaclab/af-mcp-platform
description:
  Credential-brokered MCP aggregator/gateway for any MCP server to hook into
categories: [mcp-servers]
---

The source code for a Model Context Protocol gateway that any ATLAS analysis
facility can deploy. It authenticates callers against the facility's Keycloak,
brokers per-user credentials to downstream systems, and aggregates _any_
registered MCP backend behind one endpoint, so an LLM client never holds raw
x509/IAM credentials directly. Rucio, PanDA, AMI, GitLab, Jupyter, and HTCondor
are what UChicago's deployment currently registers — not a fixed list the
platform itself is limited to; any MCP server can be hooked in. Untagged
(generic) because this card is about the deployable software, not a specific
running instance — see
[UChicago AF MCP Portal](https://mcp-portal.af.uchicago.edu/) for the one live
deployment today (BNL is evaluating a second, for SDCC).

Useful when: you or your facility want to stand up your own credential-brokered
MCP gateway.

Not useful when: you just want to _use_ a gateway someone else already runs —
that's a `hosted: true` entry (like UChicago AF MCP Portal), not this one. Or
you just need a single tool — reach for that tool's own MCP server directly
instead.
