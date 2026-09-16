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
shelling out to `rucio` by hand.

Useful when: you are locating ATLAS (or any Rucio-managed) datasets, checking
replication, or inspecting rules before launching a job.

Not useful when: you need Rucio _administration_ (creating rules, managing
accounts) — this covers client-side, read-mostly operations.
