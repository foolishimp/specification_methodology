# STDO 3.2

STDO 3.2 is one release of two parts: the STDO standards, and STDO Builder, a
framework that builds a product to its specification under those standards.
Exact cut: **3.2.1**. Release 3.2.0 was reviewed in full and the verdict was no:
do not use it on real work.

Download `stdo-3.2.1.tar.gz` from the
[3.2.1 release](https://github.com/foolishimp/specification_methodology/releases/tag/stdo%2Fv3.2.1),
unpack it, run `sh stdo-3.2.1/install.sh <folder>` and put `<folder>/bin` on your
PATH. Then start with `builder/GETTING_STARTED.md` in the unpacked folder.

Builder's source is in [builder/](builder/README.md): its intent, product
definition, requirements, design, tests and code.

The standards in 3.2.1 are release 3.1.0-rc.3, the exact cut of the public 3.1.0
line. The rest of this page describes the 3.1 standards and their companion
Products. The [release note](releases/3.2.1/RELEASE.md) says what 3.2.1 repairs
and what it does not. [The history](history.html) says how STDO came to 3.2.0
and is not yet brought up to this release.

## The standards: STDO 3.1

STDO supplies rules for the software development lifecycle. Version 3.1 brings
Purpose Context, default QA and causal triage, and ticket-based context continuity
together in an explicit six-Product release. Exact cut: **3.1.0-rc.3**; public
version line: **3.1.0**.

Start with [Using STDO](specification_methodology/v3/build_tenants/common/plugins/spec/references/GETTING_STARTED.md)
for the method and published assets, then [Skills Getting Started](stdo_skills/GETTING_STARTED.md)
for Purpose Context and Codex/Claude bindings. The [release scope](releases/3.1.0-rc.3/RELEASE.md)
and [migration guide](releases/3.1.0-rc.3/MIGRATION.md) describe the changed Product
boundaries. The [exact release](https://github.com/foolishimp/specification_methodology/releases/tag/specification_methodology%2Fv3.1.0-rc.3)
provides the native manifest, manager, companion Products and cohort inventory.

| Product | Responsibility |
|---|---|
| [Specification Methodology](specification_methodology/v3/README.md) | SDLC rules, native workflows and default reference frames |
| [Purpose Context](purpose_context/README.md) | Reusable indexes over exact sources and purpose-specific context construction |
| [STDO Skills](stdo_skills/README.md) | Codex/Claude adapters that consume Purpose Context and preserve native workflow ownership |
| [Representation Tools](a_c/README.md) | Source-linked visual generation and exploration; stable namespace remains `a_c` |
| [STDO Representation](stdo_representation/README.md) | Visual documentation of selected STDO sources with declared coverage and residuals |
| [STDO Builder](builder/README.md) | New in 3.2: builds a product to its specification under the standards, by governed LLM agent sessions |
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
| Pure/local Python 3.12 refactoring | `stdo-3.1.0-rc.3-python-pure-refactor-v2` | Exact native 3.1.0-rc.3 |
| Work, QA, triage, repair verification, boundaries and evidence reuse | `stdo-3.1.0-rc.3-sdlc-workflow-v1` | Exact native 3.1.0-rc.3 |

Both indexes bind `stdo://releases/v3.1.0-rc.3/`, manifest
`2b3a7391dfb731219e64240199fe2e1b2736b9d5a44d030602fe7f07dd6c7a9a`.
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
