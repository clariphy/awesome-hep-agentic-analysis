---
name: AF Filesystem MCP
url: https://github.com/maniaclab/af-filesystem-mcp
description:
  MCP server giving browse and read access to a user's own analysis-facility
  home and data directories
categories: [mcp-servers]
---

Gives an Analysis Facility user browse/read access to their own files on the
AF's shared NFS home and Ceph data area — nothing more. Designed to sit behind
[AF MCP Platform](https://github.com/maniaclab/af-mcp-platform)'s credential
broker so an LLM session can look at a user's own analysis outputs, condor logs,
and scratch files without a human copying paths around.

Useful when: an agent needs to read or list a user's own analysis-facility files
as part of debugging a job or inspecting output.

Not useful when: you need write access, or access to another user's files — this
is scoped strictly to the caller's own home and data area.
