# STDO 3.1

STDO supplies rules for the software development lifecycle. Version 3.1 brings
Purpose Context, default QA and causal triage, and ticket-based context continuity
together in an explicit six-Product release. Exact cut: **3.1.0-rc.2**; public
version line: **3.1.0**.

Start with [Using STDO](specification_methodology/v3/build_tenants/common/plugins/spec/references/GETTING_STARTED.md)
for the method and published assets, then [Skills Getting Started](stdo_skills/GETTING_STARTED.md)
for Purpose Context and Codex/Claude bindings. The [release scope](releases/3.1.0-rc.2/RELEASE.md)
and [migration guide](releases/3.1.0-rc.2/MIGRATION.md) describe the changed Product
boundaries. The [exact release](https://github.com/foolishimp/specification_methodology/releases/tag/specification_methodology%2Fv3.1.0-rc.2)
provides the native manifest, manager, companion Products and cohort inventory.

| Product | Responsibility |
|---|---|
| [Specification Methodology](specification_methodology/v3/README.md) | SDLC rules, native workflows and default reference frames |
| [Purpose Context](purpose_context/README.md) | Reusable indexes over exact sources and purpose-specific context construction |
| [STDO Skills](stdo_skills/README.md) | Codex/Claude adapters that consume Purpose Context and preserve native workflow ownership |
| [Representation Tools](a_c/README.md) | Source-linked visual generation and exploration; stable namespace remains `a_c` |
| [STDO Representation](stdo_representation/README.md) | Visual documentation of selected STDO sources with declared coverage and residuals |
| [Axiom Indexer](axiom_indexer/README.md) | Retained conversion, validation and visual projection |

The [SDLC default](specification_methodology/v3/build_tenants/common/standards/SDLC_DEFAULTS.md)
connects work → QA → causal triage → appropriate owner re-entry → verification →
continue or close. Incremental QA and a named acceptance/release boundary have
different claims and exit conditions. Recurring bugs can require requirements,
design, model or observation repair rather than another implementation patch.

The ticket is the durable reference for its unit of work. Construct task context
from that current record and its linked governing sources and evidence; record
results and the next authorized step there. [TICKETS](specification_methodology/v3/build_tenants/common/standards/TICKETS.md#5-from-carrier-to-execution)
owns application through the work carrier; [ACTIVATION](specification_methodology/v3/build_tenants/common/standards/ACTIVATION.md#2-context-construction-under-an-envelope)
owns context construction and restart. Default frames project those owners,
Skills apply them, and guides explain their use.

| Purpose | Current release index | Native source |
|---|---|---|
| Pure/local Python 3.12 refactoring | `stdo-3.1.0-rc.2-python-pure-refactor-v2` | Exact native 3.1.0-rc.2 |
| Work, QA, triage, repair verification, boundaries and evidence reuse | `stdo-3.1.0-rc.2-sdlc-workflow-v1` | Exact native 3.1.0-rc.2 |

Both indexes bind `stdo://releases/v3.1.0-rc.2/`, manifest
`ddbd3910981a63f41c17879551f93ef58f369848bae81cc9726d77df55dc7faa`.
Assessment applies to exact sources, purpose and caller facts. Unknown facts
remain unknown. Context coverage does not establish successful code, repair,
automatic host pickup or release acceptance. The complete installed constitution
and the current ticket remain governing references.

The companion bundle exposes Purpose Context and Skills as separate Products.
Visual documentation is optional for context use. Lean and the retired
registry/formal/context routes are outside the current delivery. Historical
indexes and releases remain exact historical subjects; they are not relabelled.
Existing Product construction bases and consumer installations are unchanged by
publication. The 3.0.4 construction basis does not select the indexed corpus.

For source work, read [DEVELOPMENT.md](DEVELOPMENT.md), select a Product Definition
and follow its local AGENTS.md. The repository root coordinates six independently
owned Products; it owns no seventh Product. The [historical five-Product descriptor](stack_release.json)
remains preserved and is not the 3.1 distribution contract.
