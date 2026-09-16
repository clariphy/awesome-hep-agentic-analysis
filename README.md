# awesome-hep-agentic-analysis [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

A curated collection of agentic analysis toolings for the HEP community, compatible with
Claude Code, Codex, Gemini CLI, Cursor, and more.

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

## Background

This list grew out of the **Analysis Agentic Workflows** breakout session at the
[CLARIPHY AI Collaboration Meeting](https://indico.global/event/18639/) (Pyle Center,
UW-Madison, September 14-16, 2026). That session reviewed a scattered set of tools —
[JFC](https://github.com/jfc-mit/jfc), the
[IRIS-HEP](https://github.com/iris-hep/marketplace) and
[USATLAS](https://github.com/usatlas/marketplace) plugin marketplaces, HTCondor MCP,
Rucio MCP — and CLARIPHY itself exists to follow up on
[the community-vision whitepaper](https://arxiv.org/abs/2602.17582), "Building an
AI-native Research Ecosystem for Experimental Particle Physics." A single discoverable
index of that tooling was one of the concrete outcomes. See the
[Community, Papers & Talks](#community-papers--talks) section below for both.

## What belongs here

An entry must be:

- **HEP-specific.** Built for, or specifically adapted to, particle/nuclear/astroparticle
  physics analysis. Generic ML libraries, agent frameworks, or MCP tooling with no HEP
  angle belong in a general-purpose awesome list, not this one.
- **First-hand.** Every entry is here because the person who added it uses it or
  maintains it. See [CONTRIBUTING.md](CONTRIBUTING.md).
- **Actually usable today**, not a proposal or a roadmap item — with the deliberate
  exception of the [Community, Papers & Talks](#community-papers--talks) section, which
  exists to record the context this list came from.

## Using this list with an agent

Each entry below is a one-line summary. The full detail — what a tool is actually good
for, and where it doesn't apply — lives in its datacard under
[`entries/`](entries/), not in this table. [`llms.txt`](llms.txt) is a flat,
agent-readable index of every entry with a link straight to its datacard.
[AGENTS.md](AGENTS.md) spells out the retrieval protocol: shortlist from the table
below, then confirm the match by reading the datacard before recommending anything.

<!-- UPDATE:START -->
- [Agent Frameworks & Orchestration](#agent-frameworks--orchestration)
- [Plugin Marketplaces](#plugin-marketplaces)
- [MCP Servers](#mcp-servers)
- [Standalone Skills & Plugins](#standalone-skills--plugins)
- [Knowledge Assistants & RAG](#knowledge-assistants--rag)
- [Foundation Models for HEP](#foundation-models-for-hep)
- [Benchmarks & Evaluations](#benchmarks--evaluations)
- [Datasets & Open Data for AI](#datasets--open-data-for-ai)
- [Community, Papers & Talks](#community-papers--talks)

### Agent Frameworks & Orchestration

Frameworks that coordinate one or more LLM agents through a HEP analysis workflow, end to end or in part.

- [JFC (Just Furnish Context)](https://github.com/jfc-mit/jfc) - Multi-agent framework that plans, executes, and documents a full HEP analysis from a physics prompt

### Plugin Marketplaces

Collections of Claude Code (or equivalent) plugins, skills, and agents, published as an installable marketplace.

- [IRIS-HEP Marketplace](https://github.com/iris-hep/marketplace) - Claude Code plugin marketplace with skills for awkward, hist, ServiceX, and building HEP analyses
- [USATLAS Marketplace](https://github.com/usatlas/marketplace) - Claude Code plugin marketplace covering ATLAS analysis facilities and the full ATLAS software stack

### MCP Servers

Model Context Protocol servers that expose HEP data, compute, or software infrastructure to any MCP-compatible agent.

- [AF Filesystem MCP](https://github.com/maniaclab/af-filesystem-mcp) - MCP server giving browse and read access to a user's own analysis-facility home and data directories
- [AF JupyterLab MCP](https://github.com/maniaclab/af-jupyterlab-mcp) - MCP server for creating, inspecting, and deleting per-user JupyterLab servers on an analysis facility
- [AF MCP Platform](https://github.com/maniaclab/af-mcp-platform) - Credential-brokered MCP gateway aggregating Rucio, PanDA, AMI, GitLab, Jupyter, and HTCondor behind one URL
- [AMI MCP](https://github.com/kratsg/ami-mcp) - MCP server wrapping ATLAS AMI for dataset metadata lookups
- [ATLAS OpenSearch MCP](https://gitlab.cern.ch/atlas-search/mcp) - MCP server for querying the ATLAS collaboration's OpenSearch-backed search index
- [Bamboo MCP](https://github.com/BNLNPPS/bamboo-mcp) - Plugin-based MCP runtime for AI-assisted PanDA/ATLAS, ePIC/EIC, and CGSim workflows
- [HTCondor MCP](https://github.com/bbockelm/golang-htcondor) - Go HTCondor client library with a bundled MCP server for submitting and querying batch jobs
- [Rucio MCP](https://github.com/kratsg/rucio-mcp) - MCP server wrapping the Rucio client for dataset discovery and replica management
- [ServiceX MCP](https://github.com/maniaclab/servicex-mcp) - MCP server wrapping the ServiceX client for on-demand ATLAS/CMS data delivery

### Standalone Skills & Plugins

Individual agent skills or plugins not bundled into one of the marketplaces above.

_No entries yet. [Contributions welcome!](CONTRIBUTING.md)_

### Knowledge Assistants & RAG

Retrieval-augmented systems and knowledge assistants built for HEP documentation, software, or support workflows.

- [archi](https://github.com/archi-physics/archi) - Retrieval-augmented chat, ticketing, and course-support assistant framework for research teams

### Foundation Models for HEP

Pretrained models built specifically for particle, nuclear, or astroparticle physics data.

_No entries yet. [Contributions welcome!](CONTRIBUTING.md)_

### Benchmarks & Evaluations

Benchmarks and evaluation suites for measuring agent or model performance on HEP tasks.

_No entries yet. [Contributions welcome!](CONTRIBUTING.md)_

### Datasets & Open Data for AI

Datasets and open-data releases curated or packaged for AI/agentic use in HEP.

_No entries yet. [Contributions welcome!](CONTRIBUTING.md)_

### Community, Papers & Talks

Workshops, whitepapers, and community efforts that shaped or motivated this list.

- [Building an AI-native Research Ecosystem for Experimental Particle Physics](https://arxiv.org/abs/2602.17582) - 459-author community whitepaper laying out grand challenges and infrastructure for AI-native particle physics
- [CLARIPHY AI Collaboration Meeting](https://indico.global/event/18639/) - Workshop that formed the working group producing this list, including the Agentic Workflows session
<!-- UPDATE:END -->

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Short version: one entry per PR, add a datacard
under `entries/`, run `pixi run generate`, and only submit a tool you personally use or
maintain.

## Contributors

Recognized per the [All Contributors](https://allcontributors.org) specification —
every kind of contribution counts, not just entries. See
[CONTRIBUTING.md](CONTRIBUTING.md#recognizing-contributions) for how to add yourself.

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://giordonstark.com/"><img src="https://avatars.githubusercontent.com/u/761483?v=4?s=100" width="100px;" alt="Giordon Stark"/><br /><sub><b>Giordon Stark</b></sub></a><br /><a href="https://github.com/clariphy/awesome-hep-agentic-analysis/commits?author=kratsg" title="Code">💻</a> <a href="https://github.com/clariphy/awesome-hep-agentic-analysis/commits?author=kratsg" title="Documentation">📖</a> <a href="#ideas-kratsg" title="Ideas, Planning, & Feedback">🤔</a> <a href="#projectManagement-kratsg" title="Project Management">📆</a></td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td align="center" size="13px" colspan="7">
        <img src="https://raw.githubusercontent.com/all-contributors/all-contributors-cli/1b8533af435da9854653492b1327a23a4dbd0a10/assets/logo-small.svg">
          <a href="https://all-contributors.js.org/docs/en/bot/usage">Add your contributions</a>
        </img>
      </td>
    </tr>
  </tfoot>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

## License

[CC BY 4.0](LICENSE).
