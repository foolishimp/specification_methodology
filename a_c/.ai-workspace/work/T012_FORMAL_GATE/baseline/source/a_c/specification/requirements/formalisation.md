# Formalisation requirements

These requirements apply to a tenant declaring formalisation capability. They
supplement AC-R-001..015 without selecting a proof language or redefining the
calculus. The owning basis is the exact `AXIOMATIC_CALCULUS.md` named in the
[common requirements](README.md). Tenant HOW owns the logic, data grammar,
algorithms, proof assistant, libraries and commands.

| ID | Required behavior | Deciding discriminator |
|---|---|---|
| FR-001 | Declare the formal fragment, its mathematical interpretation, exact calculus clauses and source-to-formal mapping. Distinguish formal propositions from opaque source content and unformalised predicates. Name every premise, trusted component and unsupported claim. | A reviewer can trace each theorem to the defined operation and source clause, and determine which source assertions the theorem does not interpret. A theorem is not evidence for an unstated stronger claim. |
| FR-002 | Represent all eight core record-family tags distinctly, including empty populations. Preserve exact model, signature and basis identities, each retained record's identity and complete content, and its context, owner, scope, basis and declared authority. Preserve residuals as records. | Exact retained-record equality detects changed content or coordinates. Empty traversal/transformation/judgment populations remain explicit; tagging them does not implement their operations. |
| FR-003 | Construct closure for finite declared local records, exact seeds and an exact directed required-dependency relation. Prove seed inclusion, dependency closure, and leastness among seed-containing closed sets; connect membership to finite reachability. | Generic checked proofs cover cycles and self-dependencies. A missing reachable record or an unrelated extra record violates the selected closure. The execution path discharges the proved construction or a sound finite-certificate check, rather than assuming the expected closure. |
| FR-004 | Construct a projection containing exactly that closure, with an exact parent/selection identity and explicit included, excluded, external and unresolved boundaries. Prove that every retained record equals its parent record, conserving content, family, identity, authority, basis and residual data. | Changed retained coordinates fail equality; omission of a required residual fails closure. Excluded residuals remain named boundaries rather than becoming resolved uncertainty. A projection cannot present itself as the complete parent or a new owner. |
| FR-005 | Define the exact budget unit and checked success/refusal relation. When the complete required closure exceeds the budget, return explicit refusal; otherwise return that complete closure. Refuse unsupported or unresolved input conditions rather than weakening the theorem premises silently. | Checked refusal and success properties and executed boundary cases distinguish sufficient budget from one below the required amount. No successful result is a truncated closure. |
| FR-006 | Bind imported subject bytes and every source-to-formal record/dependency mapping to immutable identities. Check the selected importer fragment and retain exact external-resolution, grounding and unresolved coordinates. Identify parser, importer, generated code, compiler, runtime and kernel/library trust separately. | Reproduction checks the exact source digests and generated formal data; unsupported, malformed, stale or identity-conflicting inputs refuse within the declared importer fragment. A passing kernel proof over generated values does not certify the parser, dependency selection or source prose. |
| FR-007 | Deliver runnable checked proofs, an executable subject example and meaningful positive/negative controls with pinned tool and library identities. Report theorem statements, checked premises, proof axioms/dependencies and actual results. Keep F_P construction, deterministic proof checking, independent assessment and authority decisions distinct. | No unfinished proof placeholder, added axiom, circular premise or unchecked native result discharges the selected obligations. Tests exercise both useful success and refusal. Re-running the documented path verifies the same bounded propositions without assuming the expected conclusion. |

For FR-003, a required edge from `a` to `b` means that retaining `a` requires
retaining `b` under the exact declared relation. The formal theorem is conditional
on that supplied relation. Semantic completeness of its selection from subject
prose remains an F_P judgment. Finite closure is least under that relation;
neither minimum token cost nor sufficient human/agent understanding follows.

For FR-002/004, full record content may remain opaque under a declared exact
equality. Such conservation proves data preservation, not truth of an embedded
predicate, legitimacy of an authority declaration or fidelity of a prose model.
Signature completeness, external reference typing and other AC laws are claimed
only to the extent separately defined and checked. No proof of whole-calculus
validity, soundness, consistency or logical completeness follows from this
fragment. F_P interpretation and the exact external semantic acceptance required
for an accepted carrier remain separate from formal construction and checking.

## Selected first delivery

[T-011](../../.ai-workspace/tickets/active/T-011-lean-formalisation.md) selects
Lean with Mathlib as a new independent tenant. The delivery includes the formal
definitions and generic proofs above, reproducible build/run commands and a
source-linked execution on the exact published STDO 3.0.2 composition supplement
`MODEL.json`. That fixture has 32 records and all eight population keys; three
populations are empty. It is a represented subject, with its raw and canonical
identities fixed by T-011, and does not replace the installed v2.5.1-rc.2 builder.

Graph carrier import is an explicit adapter. The common obligations and formal
core require no Graphify execution, mutable v3 source, Axiom Indexer or STDO
Representation service. The first fragment does not execute AC-013
transformations, decide arbitrary source predicates, select semantically
sufficient dependencies or issue semantic acceptance. Independent review and
owner disposition remain separate from successful construction.
