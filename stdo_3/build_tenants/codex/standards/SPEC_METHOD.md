# Spec Method

Standing: Codex candidate documentary implementation for review. Construction
basis: `stdo://releases/v2.5.1-rc.2/`, manifest SHA256
`3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`.
This document makes no acceptance, release or adoption decision. Common WHAT
was recovered at
`00be6b8e674d61d96ed31e744e1d85adcd456df4`; the accepted Codex C1
[principles](../design/PRINCIPLES.md) and [build plan](../design/BUILD_PLAN.md)
were recovered at `a485c220155ccae735406860b87dbc2f7d45e0c1`.

Spec Method is one particular methodology over the
[Foundations](FOUNDATIONS.md). It owns specification and realization relations.
[Work](WORK_METHOD.md) owns binding, acquisition, execution, recovery and next
action; [Evidence](EVIDENCE_METHOD.md) owns judgment and conjunction. Those
definitions apply here by import.

## S-01 Select Purpose And Product

Intent states purpose and direction. Product states the outcome, boundary,
material terms and owned choices that the specification makes concrete. A work
wave selects current concerns within those relations; it cannot silently change
the Product. Identify the actual outcome owner and reserved decisions before
treating an observed result as adequate.

Distinguish Product meaning, mutable source state, a frozen release and an
installed instance. A constituent needing its own material boundary can have its
own Intent/Product/specification/realization account. Directory nesting, shared
actors or code do not supply that account or establish composition.

Recovery: [RC2 constitutional chain](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#constitutional-chain)
and [recursive Product taxonomy](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#recursive-product-taxonomy).

## S-02 One Common WHAT, Independent HOWs

The specification states what every admitted realization must make true. Design
chooses a HOW that satisfies those obligations; implementation realizes that
design. Design and implementation remain derivative unless their governing
owner accepts a change to WHAT. A prescribed structure or path is an obligation
only where the governing specification actually selects it.

Resolve a material term through its type, context, semantic owner, scope and
basis under [F-01](FOUNDATIONS.md#f-01-purpose-interpretation-and-object). Define
the interpretation by which a representation makes an obligation inspectable.
Equal labels, bytes or field shapes do not establish equal meaning. A changed
encoding must preserve the distinctions required by its consumers.

Several HOWs can conform to one WHAT. Different algorithms, document layouts or
implementations may satisfy the same obligations while differing in unselected
behavior or cost. Conformance, semantic equivalence and computational equivalence
are separate claims. Judge each against its own declared predicate and basis.

Recovery: [RC2 semantic resolution](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#bounded-context-semantic-resolution)
and [reconstruction litmus](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#reconstruction-litmus).

## S-03 State Obligations At Their Owner

Requirements state capabilities, invariants, constraints, governance or evidence
conditions that the Product must satisfy. An obligation needs sufficient meaning
to identify its applicable subject, condition and adequate outcome. Preserve
material uncertainty and non-applicability with their reasons; absence of a
loaded clause cannot prove that its obligation is absent.

Keep the common obligation separate from a tenant's chosen topology, carrier or
strategy. If realization exposes a missing material decision, return that
question to the owning specification or design relation. Tests can discriminate
the governing obligation; a convenient fixture cannot author it.

Trace a consequential design choice to the obligations and sources it serves.
Stable identities and sufficient source routes let a consumer recover the
relation without a second competing rule body. [F-04](FOUNDATIONS.md#f-04-conservation-through-change)
owns reference sufficiency; Evidence owns the resulting support claim.

## S-04 Derive Interfaces From Outer Outcomes

An interface serves a governed transformation. Derive its material input/output
types, interpretation, preconditions, identity/basis, effects, failure routes and
authority from that transformation's outer outcome and constraints. Name the
owner of each supplied fact and of any consequential admission. A use-case verb
or transport shape alone does not establish a semantic boundary.

Before composing producer and consumer, establish compatibility under
[F-03](FOUNDATIONS.md#f-03-typed-composition). Account for the material seams and
coupled invariants through a sufficient local or joining evaluation. A wrapper,
adapter or projection translates or exposes its owner's truth; it cannot invent
missing identity, admission or closure semantics.

Shared machinery may realize several instances while their bindings and owners
remain distinct. Commonization needs a supported equivalence of the relevant
contract, effect and authority relations. Similar code is a candidate for that
evaluation, not its conclusion.

Recovery: [RC2 typed composition](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-016-typed-composition)
and [bounded frame conservation](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#bounded-frame-conservation-stdo-up-017).

## S-05 Make Reconstruction Sufficient

For the selected construction span, a capable consumer must recover the material
contract and derive an allowed realization without hidden major decisions. The
test is sufficiency under the declared context and actor envelope. It requires
neither a unique realization nor equality to an incumbent.

An adequate design makes its consequential decisions and admitted latitude
recoverable. Expose contradictions and materially unresolved alternatives before
dependent promotion. Reuse unchanged accepted relations under their validity
conditions; reconstructability does not require repeating their construction.
Required independent evaluation still supplies its own judgment under Evidence.

Algorithmic description, informational interpretation and computational
realization are orthogonal accounts under [F-07](FOUNDATIONS.md#f-07-orthogonal-accounts-and-proof-limits).
They can constrain the same subject simultaneously. They are not consecutive
development stages, and the supported deterministic fragment establishes no
universal categorical equivalence or hardware-cost model.

Recovery: [RC2 reconstruction litmus](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#reconstruction-litmus)
and [invariant reconstruction sufficiency](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#invariant-reconstruction-sufficiency-stdo-up-018).

## S-06 Bound Construction And Checkpoints

Select a coherent affected set capable of delivering the chosen behavior while
preserving every material governing relation. Include causally relevant far-side
relations, or justify their exclusion. A function, file or ticket boundary need
not coincide with that set. Unrelated incompleteness remains bounded input to its
owner rather than an invented condition on the local claim.

Apply [W-01](WORK_METHOD.md#w-01-bind-the-selected-work) through
[W-04](WORK_METHOD.md#w-04-transform-and-observe) to the selected action. A
checkpoint identifies the exact retained subject, included territory,
predecessor, concurrent effects and evidence. Preserve unaccepted work with its
actual standing. Acceptance, preservation and publication are distinct decisions.

The next action uses current work and still-live authority under
[W-05](WORK_METHOD.md#w-05-select-the-next-authorized-action). Resume retained
work through [W-06](WORK_METHOD.md#w-06-re-enter-current-persistent-work).
Reconstruction from scratch requires its own supported reason and grant; a
restart does not discard valid progress or resolve uncertain external effects.

Recovery: [RC2 construction relation](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#agentic-construction-execution-stdo-up-020)
and [checkpoint/continuation](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#checkpoint-continuation-progress-and-churn).

## S-07 Diagnose Before Repair

An observed mismatch challenges the relation it actually defeats. Determine
whether its supported cause lies in Product meaning, specification, accepted
design, implementation, producer/consumer binding, evidence, effect observation
or authority. The frame that exposes a mismatch need not own its repair. Causes
may be plural or unresolved; retain that uncertainty before selecting action.

Use [W-07](WORK_METHOD.md#w-07-progress-churn-and-conclusion) and Evidence's exact
subject judgment to choose the smallest supported repair at its actual owner.
Changing governing meaning or accepted design requires re-entry there. A local
patch cannot silently alter the upstream obligation to fit its output. Preserve
the failed subject and fixed expectation; assess the affected successor claim.

Real-use observations can motivate a new purpose or changed obligation. Return
that proposal through the owning Intent/Product/specification relation before
implementing it as accepted behavior. Repeating an unchanged rejected relation
supplies no reason to expect a different result.

Recovery: [RC2 proportional disposition](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#proportional-disposition)
and [renewal path](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#renewal-path).

## S-08 Preserve Outcome, Scope And Authority

Progress and completion concern one selected outcome instance and interval under
[W-07](WORK_METHOD.md#w-07-progress-churn-and-conclusion). Prerequisite readiness,
preservation, observed activity and churn retain their actual standing. Document,
test, receipt or commit counts alone do not establish Product progress.

Evidence judges the exact candidate; its owner accepts only within the declared
authority. A bounded success cannot widen the outcome, select a canonical
realization, renew exhausted growth authority or imply release/adoption. A new
outcome or changed acceptance condition requires its owning decision. Consume an
unchanged owner ruling under [E-05](EVIDENCE_METHOD.md#e-05-evidence-does-not-grant-authority)
without re-minting or enlarging it.

Recovery: [RC2 outcome conservation](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#product-outcome-conservation-stdo-up-013).

## S-09 Select Domain Meaning Explicitly

[Profiles](profiles/README.md) add domain obligations only when the governing
Product/design selects their scope and basis. Their owners retain software,
graph, work-record or world-model meaning; they import the core method relations.
An application example, deployment fixture or external runtime remains a
separately owned subject. Its incidental particulars do not become method law.

The physical library, work carrier, actor population and resource limits are
selected HOW or owned operational constraints. This method requires no universal
document or ticket count, serialized control pack, actor-family default, runtime
or fixed budget. Added structure must remove a material ambiguity or satisfy an
actual obligation under [RC2 proportionality](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#proportional-method-and-delivery-stdo-up-014).
