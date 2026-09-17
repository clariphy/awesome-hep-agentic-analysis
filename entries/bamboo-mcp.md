---
name: Bamboo MCP
url: https://github.com/BNLNPPS/bamboo-mcp
description:
  Plugin-based MCP runtime for AI-assisted PanDA/ATLAS, ePIC/EIC, and CGSim
  workflows
categories: [mcp-servers]
experiments: [ATLAS, EIC]
---

A lightweight MCP-based runtime with a plugin architecture for AI-assisted
scientific tools, targeting PanDA/ATLAS workflows, ePIC/EIC experiment
operations, and CGSim distributed-computing simulation. LLMs are used for
summarization and explanation, not as a source of truth — structured evidence is
always returned alongside any natural-language answer.

Useful when: you want structured evidence plus an LLM summary for an operations
question, rather than raw logs alone.

Not useful when: you need a general-purpose MCP framework — Bamboo's plugins are
built for these specific operational domains.
