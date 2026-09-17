---
name: AF JupyterLab MCP
url: https://github.com/maniaclab/af-jupyterlab-mcp
description:
  MCP server for creating, inspecting, and deleting per-user JupyterLab servers
  on an analysis facility
categories: [mcp-servers]
experiments: [ATLAS]
facilities: [UChicago]
---

Lets an agent create, inspect, and delete a user's own per-user JupyterLab
server on the UChicago ATLAS Analysis Facility Kubernetes cluster — the same
notebooks af-portal deploys today, exposed as MCP tools instead of a web UI.
Only reachable if you have a UChicago AF account.

Useful when: you have a UChicago AF account and an agent needs to spin up or
tear down a JupyterLab session as part of a larger workflow on the AF.

Not useful when: you need to run code _inside_ an already-running notebook —
this only manages the server's lifecycle, not its contents — or you're not at
UChicago.
