---
name: AF JupyterLab MCP
url: https://github.com/maniaclab/af-jupyterlab-mcp
description:
  MCP server for managing per-user JupyterLab servers and notebooks on an
  analysis facility
categories: [mcp-servers]
experiments: [ATLAS]
facilities: [UChicago]
---

Lets an agent manage a user's own per-user JupyterLab server on the UChicago
ATLAS Analysis Facility Kubernetes cluster — the same notebooks af-portal
deploys, exposed as MCP tools instead of a web UI. Only reachable if you have a
UChicago AF account.

Useful when: you have a UChicago AF account and an agent needs to work with
JupyterLab sessions on the AF, from spinning one up through running code in it.

Not useful when: you're not at UChicago.
