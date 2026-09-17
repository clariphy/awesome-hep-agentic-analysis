---
name: AF Filesystem MCP
url: https://github.com/maniaclab/af-filesystem-mcp
description:
  MCP server giving browse and read access to a user's own analysis-facility
  home and data directories
categories: [mcp-servers]
experiments: [ATLAS]
facilities: [UChicago]
---

Gives an Analysis Facility user browse/read access to their own files on the
AF's shared NFS home and Ceph data area — nothing more. Designed to sit behind
[AF MCP Platform](https://github.com/maniaclab/af-mcp-platform)'s credential
broker so an LLM session can look at a user's own analysis outputs, condor logs,
and scratch files without a human copying paths around.

The helm configuration is generic — BNL is evaluating it for SDCC — but the only
place it's actually deployed and reachable today is UChicago, hence the tags
above. If you're not at an AF that runs it, this isn't installable by you
directly; you'd need your facility's sysadmins to deploy it.

Useful when: you have a UChicago AF account and an agent needs to read or list
your own analysis-facility files as part of debugging a job or inspecting
output.

Not useful when: you need write access, access to another user's files, or
you're not at a facility that runs this — this is scoped strictly to the
caller's own home and data area on facilities that deploy it.
