---
name: Rucio MCP
url: https://github.com/kratsg/rucio-mcp
description:
  MCP server wrapping the Rucio client for dataset discovery and replica
  management
categories: [mcp-servers]
---

Wraps the Rucio Python client as MCP tools, so an agent can list datasets,
resolve replicas, and inspect rules from a conversational session instead of
shelling out to `rucio` by hand. Not tagged to any experiment or facility here:
Rucio itself is used well beyond ATLAS (it originated there but is now
experiment-agnostic), and which Rucio instance you actually reach is a matter of
how this MCP server is configured, not something the tool itself fixes.

Useful when: you are locating datasets on whichever Rucio instance this is
configured against, checking replication, or inspecting rules before launching a
job.

Not useful when: you need Rucio _administration_ (creating rules, managing
accounts) — this covers client-side, read-mostly operations. Also not useful if
you just want to _connect_ to a running instance rather than deploy your own —
see [Rucio MCP (UChicago-hosted)](https://rucio-mcp.af.uchicago.edu/) for one
that already exists.
