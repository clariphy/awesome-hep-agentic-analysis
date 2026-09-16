---
name: AF MCP Platform
url: https://github.com/maniaclab/af-mcp-platform
description:
  Credential-brokered MCP gateway aggregating Rucio, PanDA, AMI, GitLab,
  Jupyter, and HTCondor behind one URL
categories: [mcp-servers]
---

A Model Context Protocol gateway that any ATLAS analysis facility can deploy. It
authenticates callers against the facility's Keycloak, brokers per-user
credentials to downstream systems, and aggregates every registered MCP backend
behind one endpoint, so an LLM client never holds raw x509/IAM credentials
directly. The reference deployment is the UChicago ATLAS Analysis Facility
(`mcp.af.uchicago.edu`).

Useful when: you are standing up MCP access for an analysis facility and want
one credential-brokered front door instead of wiring auth into every backend
server separately.

Not useful when: you just need a single tool (e.g. only Rucio) — reach for that
tool's own MCP server directly instead.
