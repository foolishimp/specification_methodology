# Purpose Context design

## One preserved engine

`skills/stdo-context/scripts/context_core.py` is copied byte-for-byte from the
closed direct-source portable candidate. It owns source identity, typed
three-valued guards, index validation, closure selection, rendering and content
checking. The authoring contract and JSON schema are preserved. No generated
representation or provider runtime participates.

`context.py` retains the existing CLI. Both `prepare` and catalog `bind` call
the same preparation function; both `build` and catalog `consume` call the same
compiler and delivery function. `context_catalog.py` adds public pin checking,
portable artifact lookup, actual installed-source binding and family selection.
It does not interpret governing source or implement another rule selector.

## Public identity and reuse

`PUBLIC_MANIFEST.json` contains Product identity, entrypoint, canonical skill,
catalog, Product Definition and complete public member hashes/byte counts.
The consumer selects its digest independently. `indexes`, `bind`, `select` and
`consume` verify that pin and the actual files before use. The manifest does not
hash itself. Skills pins this external dependency and forwards operations.

Catalog entries bind the exact index/purpose/source/provenance assets, source
member order and hashes, method, corpus/view identities and family guard.
`bind --source-root` means the actual installed method root containing
`manifest.json` and `standards/`. It hashes the actual manifest, checks release
identity and member declarations, then hashes every selected document. It does
not claim whole-install qualification. The local bundle retains actual paths;
distributable assets contain only relative paths and stable corpus identity.

`select` reacquires all source bytes and the method manifest and compares the
bundle to the catalog. It evaluates the declared family guard using the same
three-valued predicate evaluator as the core. False refuses, unknown returns
incomplete, and true selects the exact existing index. Query facts are caller
observations, not defaults copied from the catalog. Multiple queries may vary
target Product/task/grant without reauthoring or changing corpus identity.

`consume` writes the unchanged core's context result and Markdown plus a
separate selection receipt. Content checks use independently supplied inputs
and compare actual context/Markdown bytes. Actual native receipt remains a
separate evidence obligation for consumers that rely on it.

## Initial artifact and limits

`scripts/port_ci02_index.py` verifies exact historical inputs and ports selected
successor P1 by identity/profile rebinding only. All 68 rule objects, source
processing ledger and unresolved entries remain structurally equal; per-rule
and population digests record that proof. The common frozen workload facts
become the catalog family guard. This supplies an actual reusable index without
expanding its original purpose or transferring a historical assessment.

The initial index's examples use the original 262144-byte complete-result
bound. Every caller still selects its own explicit bound; overflow refuses.
No model is invoked by construction, selection or tests in this extraction.

## Source-closure successor

The `python-pure-refactor/2` index uses the same unchanged core, CLI, catalog
schema and exact-binding checks. It is a new authored index and corpus, not a
rewrite of P1. The source closure adds the twelve referenced owners needed to
represent activation, authority, reuse, result, ticket, identity, qualification
and conditional profile obligations. The 68 original rule lineages remain
traceable and 45 rules add those imported meanings. Every original gap has an
individual authored source disposition; independent assessment remains separate.

The purpose makes the deciding predicate explicit: retention of preconstruction
method constraints. Concrete Product parameters and unperformed task evidence
are required by complete conditional obligations, not asserted as future facts.
The request's permission to change semantics/effects/authority is distinct from
the future preservation result. Unknown deciding source or permission facts
remain unknown under the existing three-valued evaluator.

ODD and UX scope guards select their conditional law without narrowing the
catalog family. Actual mutation/failure-carrier/typing permissions use explicit
request-and-evidence guards. Other source qualifications remain complete
conditional instructions, never empty-guard exception objects asserting a
permission is already applicable. This representation grants no task authority.

The 262144-byte comparison bound is retained. The controlled base query's
unassessed canonical result measured 209425 bytes; all 113 rules under the
combined ODD/UX branch control measured 250844 bytes. These are exact subject
measurements, not promises for arbitrary caller coordinates or assessment
metadata. Actual overflow still refuses the complete body.

The retained first coverage candidate was independently falsified for omitted
source meaning. The source-repaired successor preserves that result and adds
rewrite licensing, mandatory-gate conservation, completion/repricing/outcome
distinctions and the missing review obligations. Its source comparison records
all 56 review questions, 43 functional checklist items and the diagnostic
paragraph; that authored mapping is evidence for review, not its verdict.

Current assessment standing and the preserved negative subject are bound by
[the coverage record](../skills/stdo-context/indexes/stdo-3.0.4-python-pure-refactor-v2/COVERAGE-STANDING.json).

## Latest method source rebinding

The release-target successor uses the existing catalog and unchanged runtime.
Its exact native method identity, corpus subject/member hashes, numbered-source
view, purpose digest and index digest are all rebound. The same purpose ID and
fact meanings remain valid; the description identifies the new selected
release. C13 and C15 retain exactly equal cited RELEASE text at their new
coordinates. No release-construction duty is added to the local refactor family.
The reproducible transform and complete per-rule/source delta are retained in
the new work record and index provenance.

Catalog selection already checks the actual installed manifest and selected
source bytes. Keeping both older and later entries therefore preserves older
consumer bindings without a latest-version fallback. The exact assessment
check also rejects predecessor support for the new corpus/index, independently
of whether query bytes change. Candidate and final publication remain separate;
the [method-target policy](../skills/stdo-context/references/method-targets.md)
defines the final-cut reconciliation without adding another engine.

## SDLC source-to-index pipeline

`authoring/sdlc-workflow/` holds the declared source closure, purpose/fact
meanings, source-grounded rule recipe and scenario inputs.
`scripts/rebuild_sdlc_index.py` resolves exact source sections, freezes selected
bytes under the new catalog entry, emits a development-source manifest and
calls the existing core for corpus/view identity and index validation. It
updates only the separately named SDLC entry and regenerates the complete
public manifest after all public files exist. `--check` builds in a disposable
directory and compares expected generated bytes; source or authoring drift
requires deliberate regeneration and impact review.

The catalog adapter adds one explicit `development-method-root` branch.
It checks a candidate manifest with a non-release URI, developmental standing,
exact predecessor and unique ordered members, then hashes every selected
member using the existing safe path resolver. Installed-method behavior and
`context_core.py` remain unchanged. The candidate snapshot is portable;
consumer roots may be disposable copies, but the exact selected manifest and
member bytes are required again at every select/consume.

Family applicability requires actual SDLC workflow scope and adopted selected
defaults. Conditions distinguish repair, recurring failure, evidence reuse and
named boundary work. Unknown deciding predicates remain unknown. Rich causal,
permission, review and policy premises stay complete conditional obligations;
query flags do not purport to prove future work or grant exception permission.
A template omits unknown facts until observed, rather than giving false values.

Rebuilding verifies the source recipe's exact section text hashes before using
its semantic rules. A changed governing section requires author re-entry and a
new ground hash; changing metadata alone cannot silently conserve meaning.
Changes outside a cited span still alter the corpus, view and candidate
manifest and invalidate exact assessments. Source-delta records distinguish
that identity change from a claim that every meaning changed.

Ticket/context continuity adds source-grounded obligations to the same
`sdlc-workflow/1` index, conserving its purpose, fact meanings, family guard
and existing rule meanings. The conditions for a durable ticket, qualified
reference, declared context capacity and restart remain in the rule text;
new fact flags cannot switch off those duties. The engine still selects and
renders governing constraints only. The authorized native workflow records
results and reconciles actual workspace/effect state through its selected
carrier; Purpose Context adds no task-state runtime or second truth store.

## Native release-target construction

`scripts/rebuild_release_indexes.py` constructs the two native 3.1 entries from
an actual caller-selected installed manifest and its selected sources. It uses
the existing catalog installed-source validator, deterministic core and source
section resolver. The old development generator and its generated bytes remain
unchanged. No selected-owner directory is presented as a complete native install.

The explicit release authoring record retains source-role adjustments and the
Python TICKETS carrier clarification. Every previous Python source is checked
against its retained hash; source grounds are located by unique exact text before
the declared amended ground is applied. SDLC grounds retain their section hashes.
The constructor emits per-source and per-rule changes, validates both indexes,
and updates the public inventory after final public files. Assessment and actual
use stay outside that inventory. A changed source ground refuses for author
re-entry; the constructor never creates a supported judgment.

The release exporter `scripts/package_release.py` selects the two current entries
from the verified source catalog and emits a separate portable public manifest.
All selected source bytes are preserved except that catalog projection. The
source relation identifies every selected member and excluded historical asset.
Source history and its full catalog remain available for old callers. Skills
release packaging explicitly selects the portable Product; it records the single
dependency-pin transformation in its package inventory.

The RC2 authoring record declares the W35 guard amendment with its expected
preimage, replacement and deciding EVALUATION/RELEASE section hashes. The shared
release generator applies that declaration after the preserved base recipe;
it owns no hard-coded W35 interpretation. This preserves reproducibility of the
historical development/RC1 indexes while current release authoring selects the
corrected acceptance branch. The deterministic runtime is unchanged.
