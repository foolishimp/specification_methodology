# Purpose Context

Purpose Context constructs reusable indexes over selected governing source and
supplies the constraints needed for an actual purpose. Agents author the meaning;
one deterministic engine verifies bindings, selects rules and renders/checks the
context. An index is comparable to a database covering index: it serves a defined
family of queries while the original source remains authoritative.

Start with the [canonical skill](skills/stdo-context/SKILL.md) and its
[catalog](skills/stdo-context/indexes/CATALOG.json). Through STDO Skills, run the
installed adapter's `provider.py describe` and follow the returned physical skill
path. Direct consumers use `skills/stdo-context/scripts/context.py`. Both paths
use the same engine and independently selected public manifest pin.

The caller's ticket is the durable reference for its work state; the selected
governing sources own the rules and current workspace evidence establishes actual
results. Purpose Context derives the constraints needed for the next decision.
Its output is a derived view, not a replacement ticket or authority. An agent's
context is disposable once required facts and results are retained. Resume through
the current work record and its linked evidence.

| Actual purpose | Current index and source | Usage |
|---|---|---|
| Work and ticket continuity, bounded context, QA, causal triage/re-entry, repair, boundary decisions and evidence reuse | `stdo-3.1.0-rc.3-sdlc-workflow-v1`; 40 rules over 12 owners from the exact selected native cut | [SDLC workflow](skills/stdo-context/references/sdlc-workflow.md) |
| Pure/local Python 3.12 refactoring under adopted DESIGN_MODULE, including conditional ODD/UX law | `stdo-3.1.0-rc.3-python-pure-refactor-v2`; 113 rules over 16 owners from exact STDO 3.1.0-rc.3 | [Python refactoring](skills/stdo-context/references/python-pure-refactor.md) |

Bind the actual selected source, choose the matching purpose, supply observed
query facts, then select, consume and check the complete received context. Read
the deciding source whenever context is missing, uncertain or insufficient.
A development-source index requires explicit selection/adoption or an admitted
trial alongside the caller's complete operative constitution. Installation does
not make that choice. A different purpose follows the same generic prepare,
author, validate, build and check path when authoring is in scope.

`covered: true` needs an applicable external assessment for the exact index,
corpus and query, with no material unknowns. It concerns the declared governing
constraints; it does not admit work or prove a repair, code result or release.
An authorized trial can use an unassessed context with `covered: false`.
Unknown facts, unsupported purposes and changed sources remain explicit; a new
query receives no inherited verdict. Requirements for independent assessment
come from the governing work contract.

The [SDLC rebuilding guide](skills/stdo-context/references/sdlc-workflow.md#source-led-rebuilding)
connects Product requirements, source closure, authored rules and public bindings.
The [current authoring declaration](authoring/README.md) selects RC3's source-grounded corrections:
tracking and reconciliation remain required, runtime design is Product-owned,
and Product end state is distinct from current Goals epics. RC2's W35
successor-acceptance correction remains.
Affected source, purpose or requirement changes require impact review and
regeneration before reuse. Preserve evidence that still applies to its exact
claim; refresh consumer pins after final public bytes are stable.

[PUBLIC_MANIFEST.json](PUBLIC_MANIFEST.json) pins the portable public files.
The implementation uses Python 3.11+ and the standard library, with no model,
provider or representation runtime dependency. Release-target indexing follows the
[method-target policy](skills/stdo-context/references/method-targets.md). The selected
3.1.0-rc.3 target is bound to its actual native manifest before packaging. The
Product construction basis remains STDO 3.0.4. Public release and qualification
are recorded externally for the exact package; a catalog entry supplies neither.
See [release packaging and migration](RELEASE.md).

Historical consumers retain the exact four-owner, 68-rule
[3.0.4 P1 artifact](skills/stdo-context/indexes/stdo-3.0.4-python-pure-refactor-p1/PROVENANCE.json)
and sixteen-owner [3.0.4 successor](skills/stdo-context/indexes/stdo-3.0.4-python-pure-refactor-v2/COVERAGE-STANDING.json).
The separate [3.0.5-rc.1 coverage record](skills/stdo-context/indexes/stdo-3.0.5-rc.1-python-pure-refactor-v2/COVERAGE-STANDING.json)
binds its exact external judgment and evidence reuse limits. Failed predecessors
and original evidence remain intact. None transfers coverage to another query.

Ownership and commitments: [Product](specification/PRODUCT.md),
[requirements](specification/requirements/README.md), [design](design/DESIGN.md).
