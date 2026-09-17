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

Not tagged to any experiment or facility — HTCondor itself is generic batch
scheduling. It's aimed at whoever runs the pool, though, not a typical end user:
standing it up means deploying `htcondor-mcp` against your own schedd, which is
a sysadmin task.

Useful when: you're a facility operator who wants an agent to submit, monitor,
or manage HTCondor batch jobs against your own pool.

Not useful when: you're an end user hoping to point this at someone else's
HTCondor pool without help — there's nothing to connect to until a sysadmin
deploys it. Also not useful if you need the Python HTCondor bindings — this is
an independent Go implementation, not a wrapper around them.
