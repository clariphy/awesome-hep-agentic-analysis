---
name: ATLAS OpenSearch MCP
url: https://gitlab.cern.ch/atlas-search/mcp
description:
  MCP server for querying the ATLAS collaboration's OpenSearch-backed search
  index
categories: [mcp-servers]
experiments: [ATLAS]
---

An MCP server, hosted on CERN GitLab, that exposes ATLAS's internal
OpenSearch-backed search index to agents. It sits behind CERN SSO, so its
contents aren't independently verifiable from outside the collaboration — this
card records what the tool is, not a review of it. Reachability of the link is
excluded from this repo's automated link check for the same reason (see
`lychee.toml`).

Useful when: you are an ATLAS collaborator with CERN credentials searching
internal documentation or records.

Not useful when: you are outside the collaboration — you will hit a CERN SSO
login wall.
