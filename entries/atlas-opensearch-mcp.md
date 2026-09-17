---
name: ATLAS OpenSearch MCP
url: https://gitlab.cern.ch/atlas-search/mcp
description:
  MCP server for federated search across ATLAS's collaboration documentation
categories: [mcp-servers]
experiments: [ATLAS]
---

The MCP endpoint for ATLAS Search, a federated search index (OpenSearch-backed)
over ATLAS's documentation and collaboration tools — Twiki, GitLab repos and
pages, Indico, JIRA, ATLAS Talk, Confluence, CDS, public results, Glance,
WordPress, Zensical/MkDocs docs sites, arXiv, INSPIRE-HEP, and Mattermost team
metadata — in one query instead of searching each source separately. It
integrates with [AF MCP Platform](https://github.com/maniaclab/af-mcp-platform).
Gated by CERN SSO and ATLAS collaboration membership, so its contents aren't
independently verifiable from outside — this card records what the tool is, not
a review of it. Reachability of the link is excluded from this repo's automated
link check for the same reason (see `lychee.toml`).

Useful when: you are an ATLAS collaborator and want to search across the
collaboration's documentation and tools in one place instead of several.

Not useful when: you are outside the collaboration — you will hit a CERN SSO
login wall.
