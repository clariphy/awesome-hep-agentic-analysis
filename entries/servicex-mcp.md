---
name: ServiceX MCP
url: https://github.com/maniaclab/servicex-mcp
description:
  MCP server wrapping the ServiceX client for on-demand ATLAS/CMS data delivery
categories: [mcp-servers]
---

Wraps the `servicex` Python client as MCP tools for
[ServiceX](https://github.com/ssl-hep/ServiceX), the IRIS-HEP on-demand
data-delivery service for ATLAS/CMS, so an agent can submit and monitor ServiceX
transforms without writing the client calls by hand.

Useful when: an agent needs to skim or slim a dataset via ServiceX as an
analysis step.

Not useful when: you already have flat ntuples or arrays on disk — ServiceX is
for producing them from larger datasets, not for reading files you already have.
