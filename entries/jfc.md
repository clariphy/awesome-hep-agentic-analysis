---
name: JFC (Just Furnish Context)
url: https://github.com/jfc-mit/jfc
description:
  Multi-agent framework that plans, executes, and documents a full HEP analysis
  from a physics prompt
categories: [agent-frameworks]
---

A proof-of-concept framework for autonomous HEP analysis. It integrates
autonomous analysis agents with literature-based knowledge retrieval and
multi-agent review, and is sufficient to plan, execute, and document a credible
HEP analysis starting from a short physics prompt. The specification splits into
a **methodology** (the analysis workflow phases, with tiered multi-agent review
at every stage), **general agent behavior** (strict input/output contracts per
subagent role and an experiment log for human oversight), and the orchestration
that ties them together.

Useful when: you want a reference architecture for orchestrating specialized
subagents (strategy, data exploration, statistics, writing) through a full
analysis, with human oversight gates between phases.

Not useful when: you need a single-purpose tool (a data-access server, a fitting
library) rather than an end-to-end orchestration framework.
