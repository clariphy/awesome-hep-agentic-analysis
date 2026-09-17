---
name: AMI MCP
url: https://github.com/kratsg/ami-mcp
description: MCP server wrapping ATLAS AMI for dataset metadata lookups
categories: [mcp-servers]
experiments: [ATLAS]
---

Wraps ATLAS AMI (ATLAS Metadata Interface) as MCP tools, so an agent can query
dataset provenance, tags, and derivation metadata without hand-writing AMI
command invocations.

Useful when: you need to know what a dataset _is_ — its provenance, derivation
chain, or associated tags — before deciding whether to use it.

Not useful when: you already know the dataset identifiers and just need to find
or move files — that's [Rucio MCP](https://github.com/kratsg/rucio-mcp)'s job.
