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

## Reusable formal verification gate

[T-012](../../.ai-workspace/tickets/active/T-012-reusable-formal-gate.md) selects
the reusable verification capability below. FR-001–FR-007 retain their bounded
formal meaning. A gate applies that declared fragment to the actual invocation;
it does not acquire wider semantic or authority powers by becoming reusable.

| ID | Required behavior | Deciding discriminator |
|---|---|---|
| FR-008 | Accept previously unseen subject/model/signature instances within an explicit versioned adapter contract. Check its permitted parameters and fixed record, reference-domain, governing-dependency and refusal rules against the selected implementation. Unsupported contracts remain explicit. A subject cannot mint a trusted adapter, weaken those rules or admit its own interpretation. | A new supported subject runs without adding its identity to a fixture allowlist. A self-declared compatible profile, altered fixed schema/domain/governing rule, or unknown adapter cannot obtain verification merely by refreshing its digest. |
| FR-009 | Bind each request to the exact raw and canonical model/carrier identities supplied, exact ordered seeds, declared budget unit/value and requested claim. If a supplied projection is the subject, check its actual bytes, parent/selection, complete retained records and boundary against the checked formal result. A model-only check makes no supplied-projection claim. | Changing the actual view's content, authority/basis, residuals, parent, selection or budget invalidates the corresponding result. Rebuilding a correct view while ignoring the submitted view cannot produce verification of that submitted view. |
| FR-010 | Produce portable exact-subject evidence with an explicit `verified`, `refused`, `unsupported` or `incomplete` status, requested/checked claims, input/output identities, deciding proof/implementation identities, observations and limits. Provide a reproducible check using closed artifact contents or exact resolvable dependencies, without relying on the author's mutable workspace or a success label. | A compatible independent consumer can identify and recheck the actual subject and result. Missing members, mismatched identities, forged success or unresolved proof evidence cannot be reported as verified. A non-verified result retains its reason and performed work. |
| FR-011 | Bind verification to exact adapter, bridge/generator, theorem-contract/proof, dependency, compiler/kernel and runtime/serialization identities. Check current concrete obligations and the actual output correspondence under that basis. Reuse may conserve exact established proof support only after its origin, complete relevant identity bindings and currentness are checked; stale or unbound cached evidence cannot satisfy a current request. | Changes to source/carrier/view/selection/budget or deciding implementation/proof/toolchain dependencies invalidate affected evidence. A cache hit, old compiled object or copied report without current exact-subject support does not verify. Interrupted or unavailable required checking remains incomplete. |
| FR-012 | Support an optional caller-selected **required gate** in ordinary generation and context construction. When selected, bind verification to the actual generated model/carrier/view and actual selected context content, and require current matching verified evidence before the gated output is treated as usable. Preserve accurate source and interpreter provenance. Without selection, preserve the existing operation contract and make no gate-verification claim. | A normal generation/context invocation exercises the selected gate. Missing, refused, unsupported, incomplete or stale required evidence blocks the affected use; it is not silently downgraded to optional. Controlled/replayed generation inputs retain that identity and are not described as fresh F_P authoring. |
| FR-013 | Carry the selected gate condition and exact evidence bindings through preflight and dispatch to the actual bytes delivered to the Worker. Honor existing operation/effect boundaries. Revalidate affected bindings before use and preserve the observed result or refusal through the actual return path. Gate verification supplies no work grant, disclosure permission, semantic admission, context-sufficiency decision or replacement method result algebra. | A changed projection/context, selection, gate requirement or evidence between construction, preflight and dispatch cannot reuse stale verification. Actual Worker handoff observes the verified subject binding. Existing independent authority/precondition failures still prevent dispatch even when proof checking succeeds. |
| FR-014 | Qualify the reusable gate and integrated actual path with new supported subjects, meaningful counterexamples, independent assessment and measured execution costs. Include proof/data currentness, supplied-view conservation, all four statuses, required/optional behavior and observed generation/context/preflight/dispatch. Retain failed/partial attempts and distinguish construction, proof, actual use and semantic qualification. | An unseen-subject runnable gate is demonstrated before integration claims. Independent actual-path controls detect omitted dependencies/residuals, forged/stale evidence and substituted delivered content. Record subject size, proof work, elapsed/resource costs and reuse state; no efficiency or semantic-quality claim is inferred from passing correctness checks. |

`verified` means every required check for the exact declared claim completed
successfully on its bound subject. `refused` identifies an observed violation or
invalid/stale required binding. `unsupported` identifies a contract or operation
outside the declared fragment. `incomplete` identifies required checking that
did not finish or could not establish its evidence. These are gate evidence
statuses, with a declared mapping to any consumer method's result contract;
they do not redefine that method. A required gate permits the affected use only
with current matching `verified` evidence and all other independently required
conditions.

Context construction may produce an explicitly pending/draft artifact before
effectful verification. A separate declared effect may verify its immutable
subject before required preflight/admission and dispatch. The requirement is
enforcement before checked use, not kernel execution inside a pure constructor.
The pure/effect distinction, proof origin and exact delivered-byte bindings
remain explicit throughout that staged path.

The adapter and formal core may keep source predicates opaque. A new subject,
portable receipt or ordinary Worker use does not establish F_P interpretation
fidelity, semantically sufficient dependency selection, authority legitimacy,
arbitrary predicate/transformation execution, whole-calculus validity or
semantic/carrier admission. No paid LLM campaign is required to test generation
mechanics; the provenance and limits of the chosen construction path remain
visible. The first three T-012 increments deliver the runnable unseen-subject
gate and portable evidence; the fourth and fifth deliver ordinary-path
integration and independent qualification. Concrete interfaces, effect plans,
adapter schemas, transport, artifacts and cache mechanisms remain tenant HOW.
