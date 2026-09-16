---
name: HTCondor MCP
url: https://github.com/bbockelm/golang-htcondor
description:
  Go HTCondor client library with a bundled MCP server for submitting and
  querying batch jobs
categories: [mcp-servers]
---

A pure-Go HTCondor client library (collector queries, schedd submission and
management, file transfer, sandbox handling, pool metrics) that also ships
`htcondor-mcp`, a Model Context Protocol server exposing the same engine to LLM
agents over stdio. The same repo also ships a standalone REST API server
(`htcondor-api`) for non-MCP clients.

Useful when: an agent needs to submit, monitor, or manage HTCondor batch jobs
directly.

Not useful when: you need the Python HTCondor bindings — this is an independent
Go implementation, not a wrapper around them.
