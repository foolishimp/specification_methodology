# Claude Tenant C1: Principles Attempt

Status: C1 second successor candidate, Claude tenant, after independent
review. Predecessors
`329fe4228eb9d6e2a5f79bf597fa25a82d6a798a30146a93dd5773678c73d0bb` (initial)
and `454770386c4cbe7c8aa2269afeafa3084a26ed0960774fae25e577a407f900a2` (first
successor) are retained in the tenant return record. Not accepted STDO 3 law.
Not common WHAT.
Ticket: [T-001-CLAUDE](../../../.ai-workspace/tickets/backlog/T-001-CLAUDE-principles.md).
Builder basis: `stdo://releases/v2.5.1-rc.2/`, manifest SHA-256
`3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`.
Common inputs: snapshot `C1-inputs-20261011-02`, 16 members, verified before the
first write. Subject: the six
[working common principles](../../../specification/requirements/PRINCIPLES.md)
and their proposed formalisation. This document recovers, derives and critiques
them; it adopts nothing and reads no peer realisation.

## 1. Method and vocabulary

For each principle I read the cited rc.2 clauses in full, then the adjacent
clauses the citations omit, across `AXIOMATIC_CALCULUS`, `SPEC_METHOD`,
`REFERENCE_FRAME_METHOD`, `DESIGN_MODULE_METHOD`, `IDENTITY_METHOD`,
`RELEASE_METHOD`, `TICKET_METHOD`, `ODD_METHOD`, `WORLD_MODEL_METHOD` and
`STDO_REFERENCE_FRAME_BASELINE`. Every route below is
`stdo://releases/v2.5.1-rc.2/standards/<file>#<anchor>`; the file prefix is
abbreviated in tables as AC, SM, RF, DM, IM, RM, TM, OM, WM, BL.

Each recovered relation is classified as one of:

- preserved: the clause already states the commitment at the proposed scope;
- generalised: the clause states it for a narrower subject (an a_c model, a
  frame, a traversal, a Product outcome) and the principle widens the subject;
- derived: the commitment follows from other commitments under stated premises;
- independent: it does not follow from the other commitments;
- hypothesis: a claim no clause establishes and no argument here establishes;
- gap: no clause states it, or only a profile states it.

Independence is argued per
[conformance row one](../../../specification/conformance/README.md); nothing is
assumed independent or derived by its position in the list.

## 2. The generative statement and its premises

I state one commitment separately because four others depend on it. It is not
in the six and I propose adding it (section 6).

C: a finite actor realises a selected outer contract through bounded steps.
Each step has a selected context that must fit the actor's capability
envelope. The actor's internal path within a step is not determined by the
contract. C says nothing about what a step must carry forward; that is derived
below, not assumed.

C is recovered, not new. Its three parts are stated at
[RF-002](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-002-finite-attention)
(finite attention surface fitting a declared envelope),
[RF-003](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-003-material-sufficiency)
(every material relation appears in the frame),
[AC-010](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-010-material-closure)
(material closure as a finite least fixed point, else gap or refusal), the
[Probabilistic Work Boundary](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#probabilistic-work-boundary)
(declared contract, context, capability, evidence, stop states; internal HOW is
the worker's) and
[graph functions](stdo://releases/v2.5.1-rc.2/standards/ODD_METHOD.md#graph-functions)
(an outer vector refined into an inner workflow while the outer vector remains
the contract). RF's
[Engagement](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#engagement)
functions (establish basis, select and activate, evaluate, return a closed
result, reconfigure) are the generic operational form. What rc.2 lacks is the
composition of these into one generic statement; the refinement
A → B → … → X exists only in the ODD profile.

Premises C relies on, each separately recovered:

- Pr1, selected outcome: there is a selected outcome whose obligations the
  steps serve. Recovered at
  [UP-013](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#product-outcome-conservation-stdo-up-013).
  This is principle P2, so C depends on P2, not the reverse.
- Pr2, actor change: the actor of one step need not be the actor of the next.
  A step may re-acquire declared sources and evidence; it may not rely on the
  previous actor's private memory. Recovered at
  [RF-013](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-013-reconstructable-activation)
  and the intake rule of
  [UP-020](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#agentic-construction-execution-stdo-up-020).
- Pr2a, step-produced facts: a step's judgments, residuals, observations and
  authority decisions are not re-acquirable from sources; they exist only if
  the step records them. Recovered at
  [AC-014](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-014-judgment-separation)
  (a judgment is a record over an unchanged subject) and
  [Return A Closed Result](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#return-a-closed-result)
  (the result carries verdict, residual uncertainty and invalidation
  conditions; the working context need not be transferred).
- Pr3, open world: the method does not require proving that no undiscovered
  material relation exists. Recovered at RF-003 second paragraph and
  [RF-015](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-015-residual-uncertainty).
- Pr4, probabilistic construction: the step's output is a candidate whose
  claims need evaluation. Recovered at
  [UP-020](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#agentic-construction-execution-stdo-up-020)
  (constructor's report is not independent evidence) and the
  [Ambiguity Governance Rule](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#ambiguity-governance-rule)
  (lawful probabilistic processing).

## 3. Source-recovery table

### P1 Contextual interpretation

| Route | Clause commits to | Class |
|---|---|---|
| [AC Interpretation And Models](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#interpretation-and-models) | interpretation applies a calculus to an exact subject under a declared contract; the proposed model is not accepted by construction | preserved for a_c models; generalised to any representation |
| [AC-017](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-017-interpretation-fidelity) | every model record maps to subject provenance; every subject declaration has a disposition; absence is not immateriality | preserved |
| [AC-018](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-018-structural-and-semantic-separation) | structural success is evidence for semantic review, not a substitute | preserved |
| [AC-008](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-008-explicit-latitude) | two values differ lawfully only through declared latitude | preserved, uncited by P1 |
| [RF-008](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-008-overlap-without-identity-collapse) | shared material does not establish identical meaning | preserved; this is P1's falsifier stated as law, uncited |
| [UP-008](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#semantic-evidence-and-projection-separation-stdo-up-008) | semantic basis, evidence basis and state projection are distinct | preserved, uncited |

P1's clause "an algorithmic description can make interpretation operationally
explicit" is generalised from a_c's own position, with one correction: AC's
scope statement disclaims consistency, decidability and category-theoretic
status except where a model proves them, and
[AC-019](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-019-valid-model)
lets a checker decide only the structural subset. "Algorithmic" therefore means
explicit and structurally checkable; a semantic decision is lawful only under
an exact decision contract (AC-019), and structural success alone never
establishes fidelity. The claim that all meaning is algorithmically
representable is a hypothesis; AC itself refuses it.

P1 is independent. Non-entailment: hold purpose, identity, evidence and
authority fixed and vary only the interpretation contract. One representation
of a quantity under two contracts (units declared or not; an encoding read as
text or as a digest) yields two meanings while P2, P3, P6 and C are all
satisfied. Nothing in those commitments supplies the contract; RF-008 states
the same non-entailment as law (shared material does not establish identical
meaning). So interpretation is a premise the others consume, not a conclusion
they yield.

### P2 Purpose and adequacy

| Route | Clause commits to | Class |
|---|---|---|
| [UP-013](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#product-outcome-conservation-stdo-up-013) | one selected unresolved outcome governs progress; evidence surfaces cannot select, enlarge or replace it; admitted prerequisites and experiments are bounded | preserved; P2 is UP-013 widened from Product outcome to any selected outcome |
| [Reconstruction Litmus](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#reconstruction-litmus) | each layer must be derivable from the one above; sufficiency, not uniqueness | preserved |
| [Constitutional Chain](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#constitutional-chain) and [Ambiguity Governance](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#ambiguity-governance-rule) | the chain progressively narrows ambiguity from goals to realisation | preserved, uncited: purpose is what narrows |
| [UP-014](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#proportional-method-and-delivery-stdo-up-014) | an obligation is justified by the ambiguity it removes relative to the reasoning it costs | preserved, uncited; this is P2's "no obligation without a material outcome relation" |
| [11.5D loop](stdo://releases/v2.5.1-rc.2/standards/ODD_METHOD.md#115d-constructive-evaluation-and-yield-loop) | the selected outcome is external authority for the loop; `evaluate_next` cannot enlarge it | preserved, ODD projection of UP-013 |

P2 is independent. Nothing in C, P3 or P6 yields a selected outcome; UP-013
treats selection as a Goals decision and re-scoping as Product re-entry. The
clause "interfaces inherit obligations from the transformation they serve" is
derived: premise, an interface is a boundary inside a transformation that
serves an outcome (UP-013); premise, each obligation must be justified by
ambiguity removed for that outcome (UP-014); conclusion, an interface obligation
with no route to the outcome is unjustified. That matches
[UP-005](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#boundary-and-governance-cost-stdo-up-005).

### P3 Identity, state and representation

| Route | Clause commits to | Class |
|---|---|---|
| [IM Scoped Identity](stdo://releases/v2.5.1-rc.2/standards/IDENTITY_METHOD.md#1-scoped-identity) | identity = authority + kind + value, optionally scope, revision, version, time | preserved, uncited by P3 |
| [AC-002](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-002-scoped-identity) | equal spelling, payload, position or carrier does not establish identity | preserved |
| [AC-014](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-014-judgment-separation) | a judgment points to an unchanged subject; promotion is a relation, not a rewrite | preserved; identity survives judgment |
| [Recursive Product Taxonomy](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#recursive-product-taxonomy) | source project, release cut, Product, Install and Development Product are distinct roles of one lineage | preserved; identity across lifecycle roles |
| [UP-015](stdo://releases/v2.5.1-rc.2/standards/RELEASE_METHOD.md#successor-baseline-conservation-stdo-up-015) | a successor disposes every predecessor claim: conserved, superseded, removed, not applicable | preserved, uncited; identity of claims across versions |
| [RF-005](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-005-exact-basis-and-coordinates), [RF-011](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-011-topology-mutation-and-recharting) | apparent equality is not coordinate equality; topology mutation forces re-evaluation | preserved, uncited |
| [WM Markov Object](stdo://releases/v2.5.1-rc.2/standards/WORLD_MODEL_METHOD.md#markov-object) and [Epistemic Status](stdo://releases/v2.5.1-rc.2/standards/WORLD_MODEL_METHOD.md#epistemic-status-of-the-construct) | load-bearing working vocabulary; the conditional-independence promotion gate was run and not met | hypothesis, correctly labelled by P3 |
| [WM Entity Cut Construction Law](stdo://releases/v2.5.1-rc.2/standards/WORLD_MODEL_METHOD.md#entity-cut-construction-law) | entities are recovered, not invented; admissibility is explicit identity, boundary, authority, state, evidence, treatment, covariance and ambiguity | preserved; P3's "object O with declared boundary" is this, generalised |

P3 is independent. Identity is a declared relation (authority, kind, value);
no quantity of attention, purpose or evidence produces it. The clause "current
state, historical observations and representation identity remain separate" is
the taxonomy plus AC-014, generalised. The entity-cut law supplies what P3's
bounded formulation leaves implicit: a boundary is admissible only with
explicit evidence altitude, so objecthood is a claim with a proof obligation,
not a given.

### P4 Typed composition and conservation

| Route | Clause commits to | Class |
|---|---|---|
| [AC-016](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-016-typed-composition) | traversals compose only when result type and judgment satisfy the next domain and preconditions; composition retains identities, judgments, evidence, authority, stop states; no universal F_P → F_D → F_H | preserved |
| [AC-013](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-013-transformation) | a transformation records preserved, introduced, removed, external resolution witnesses and residuals | preserved, uncited; this is the conservation accounting |
| [AC-005](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-005-authority-conservation), [RF-006](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-006-authority-conservation), [UP-004](stdo://releases/v2.5.1-rc.2/standards/IDENTITY_METHOD.md#authority-identity-and-conservation-stdo-up-004) | copying, transporting, interpreting or encoding does not transfer or widen authority | preserved, three owners |
| [AC-009](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-009-residual-conservation), [AC-011](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-011-projection) | uncertainty stays until disposed; a projection cannot trim a required member for a carrier or capability budget | preserved |
| [UP-017](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#bounded-frame-conservation-stdo-up-017) | a bounded local action conserves governing truth; every crossing seam includes its far side or states why not | preserved |
| [UP-021](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#complete-enclosing-relation-admission-stdo-up-021) | admission is one semantic commit of the complete transition or none; reuse does not transfer responsibility | preserved |
| [UP-018](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#invariant-reconstruction-sufficiency-stdo-up-018) | an action preserves, changes, duplicates or violates each governing relation; a change accepted in the acting frame is a violation | preserved |
| [RF-010](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-010-composition-on-demand) | composition law is required only when internal variables combine; otherwise closed results go to a declared conjunction | preserved, uncited; limits P4's scope |
| [BL Work result](stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md#work-result) | a result references its evidence by owning carrier and does not reconstruct unchanged material per handoff | preserved; P4's "no copying every body" |
| [UP-019](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#computational-realization-projection-stdo-up-019), [UP-023](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#capability-and-foundation-selection-stdo-up-023) | computational similarity yields a commonisation candidate, never an adjudication; foundation selection precedes a new generic mechanism | preserved; P4's "shared machinery supplies instances without merging responsibility" |

P4 bundles two commitments with different standing. Typed composition
(compatibility of contracts) is independent: it is a typing relation that
needs P1 (what the types mean) and P3 (what is being joined) and nothing else.
Conservation is derived, and narrower than the predecessor candidate claimed:
premise Pr1 (a selected outer contract), premise C (the contract is realised
in steps, by possibly different actors) and premise Pr2a (step-produced facts
are not re-acquirable). Conclusion: a step's judgments, residuals, observations
and authority decisions that the outer contract needs are lost unless the
step's output records them. That obligation is conservation of step-produced
facts, which is what AC-009, AC-016's retention clause and the work-result
clause state. It does not extend to sources and evidence a later step can
re-acquire; those are governed by RF-003 sufficiency, not by conservation.
What counts as material is decided by P2 and P1. So conservation does not
follow from finite capacity alone and is not independent; it follows from C
with Pr1 and Pr2a.

### P5 Finite capacity and graceful total handling

| Route | Clause commits to | Class |
|---|---|---|
| [RF-002](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-002-finite-attention), [RF-003](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-003-material-sufficiency), [RF-004](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-004-irrelevance-exclusion), [RF-013](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-013-reconstructable-activation) | finite surface, material sufficiency, irrelevance exclusion, reconstruction by a fresh actor | preserved |
| [RF-014](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-014-capability-fit), [RF-017](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-017-proportional-compression) | when material exceeds the envelope: another actor, refine, sequence, or lawful compression; never silent omission | preserved; the cannot-fit menu |
| [AC-010](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-010-material-closure), [AC-011](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-011-projection) | material closure is finite or returns gap; projection records its boundary | preserved; the formal context object exists |
| [RF-012](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-012-closed-results), [AC-007](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal) | every evaluation returns one of satisfied, falsified, indeterminate, out_of_frame, invalid_basis; nothing is coerced to success | preserved; totality as result algebra |
| [DM Totality Rule](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#8-totality-rule) | semantic functions are total; invalid input rejected at the boundary; typed failure | preserved for code; generalised by P5 to control models |
| [Probabilistic Work Boundary](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#probabilistic-work-boundary), [OM Probabilistic Compute](stdo://releases/v2.5.1-rc.2/standards/ODD_METHOD.md#probabilistic-compute) | the bounded unit declares contract, context, capability, evidence, provenance and stop, hold, gap, continuation, completion states | preserved; P5's dispositions already enumerated |
| [UP-020](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#agentic-construction-execution-stdo-up-020) | intake without conversation history; smallest causal cone; accept, local_repair, re_enter, reject; preservation checkpoint; a restart must say why repair is insufficient and what survives | preserved; restart as iteration is already law |
| [BL Work result](stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md#work-result) | candidate_ready, refused, incomplete, re_entry_requested: total and exclusive | preserved |
| [Ambiguity Governance](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#ambiguity-governance-rule) | ambiguity is carried, decided, escalated or blocked under declared risk appetite; hard stops are not optional | preserved; the disposition policy |
| [UP-014](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#proportional-method-and-delivery-stdo-up-014) last paragraphs, [UP-019](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#computational-realization-projection-stdo-up-019) operational assumptions | proportionality applies to the method's own execution; material work declares supported dimensions, workload and limits before qualification; no universal quota | preserved; cost exposure exists at design boundaries |
| [RF Select And Activate](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#select-and-activate), [Evaluate](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#evaluate), [Return A Closed Result](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#return-a-closed-result), [Reconfigure When Necessary](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#reconfigure-when-necessary) | the method's generic operations: select a capable frame and bind it to subject and basis, loading declared relations rather than a workspace dump; refuse or return out_of_frame when no pairing can perform the evaluation; seven named moves after an out_of_frame, invalid-basis or repeated indeterminate result | preserved; uncited by P5 and missed by the predecessor candidate |
| [RF Method Self-Qualification](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#method-self-qualification) | a fresh constructor and an independent evaluator qualify each method function (declare, activate, evaluate, conjoin, translate, audit_coverage, revise, result consumption, material composition) with representative cases | preserved; the method's functions are self-qualified |

P5 has two halves. Finite capacity is C itself. Totality is derived in two
steps. From C and Pr3 (open world): a bounded step can meet a condition
outside its context, so such conditions occur and cannot be excluded by
design. From P6 (a claim needs justification on a basis): a step that met such
a condition cannot report success, so its result algebra must carry
indeterminate, out_of_frame and invalid_basis as first-class outcomes and its
control model must name what happens next. RF-012, RF-014 and Reconfigure
When Necessary are that conclusion. Without P6 the derivation yields only that
out-of-context conditions exist, not that they are handled truthfully. The
"unified graceful-recovery account" is generalised from the owners in the
table above, including the RF engagement functions.

### P6 Justified claims and separate authority

| Route | Clause commits to | Class |
|---|---|---|
| [UP-001](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#proof-target-identity-and-adequacy-stdo-up-001) | a proof names subject, property, basis, witness relation, nearest weaker excluded property and falsifier | preserved |
| [UP-008](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#semantic-evidence-and-projection-separation-stdo-up-008), [RF-007](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-007-semantic-evidence-and-verdict-separation), [AC-018](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-018-structural-and-semantic-separation) | semantic law, evidence, evaluator and decision authority are distinct roles even in one actor | preserved, three owners |
| [UP-022](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#assurance-boundary-congruence-and-method-qualification-stdo-up-022) | a claim's quantifier cannot exceed its evidence; fresh constructor and independent evaluator; freeze before reference exposure | preserved |
| [UP-007](stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md#execution-and-verification-authority-separation-stdo-up-007), [UP-004](stdo://releases/v2.5.1-rc.2/standards/IDENTITY_METHOD.md#authority-identity-and-conservation-stdo-up-004), [RF-006](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-006-authority-conservation) | authority is identity-bearing; not minted from capability, label or reachability; proxy grants are explicit | preserved |
| [AC-014](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-014-judgment-separation), [AC-005](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-005-authority-conservation) | judgment and subject are distinct; recording or transporting confers nothing | preserved |
| [TM Judgment Continuity](stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md#recorded-judgment-and-owner-ruling-continuity) | J is not O; reusing the author's judgment cannot satisfy independence; rulings are recorded in original wording | preserved, uncited |

P6 is independent and the most completely recovered. Non-entailment: a finite
actor with a selected outcome, scoped identities, a fixed interpretation
contract and faithful composition can still accept a green label as
acceptance, or treat available capability as permission. Nothing in C or
P1–P5 forbids either; UP-022 and RF-006 exist to forbid them, as separate
normative commitments. Codex's reviewer countermodels (evidence does not
imply authority; a declared purpose does not entail justified claims) are the
same non-entailment from P2 alone. So justification and authority are
premises, not consequences of the construction account. No clause of P6 is
generalised beyond its current scope; the "general epistemic account" adds
wording, not commitment.

## 4. Derivation graph

Independent: P1 interpretation, P2 purpose, P3 identity, P4a typed
composition, P6 justification and authority. C is recovered as a composite of
RF-002, RF-003, AC-010 and the work boundary, with premises Pr1 to Pr4.

Derived, with premises:

| Derived commitment | From | Premises | Where rc.2 states the conclusion |
|---|---|---|---|
| Bounded work: the outer contract is realised through steps that fit | C | none beyond C | RF-002, AC-010, graph functions (ODD only) |
| Conservation of step-produced facts (P4b) | C | Pr1, Pr2a | AC-009, AC-016, UP-017, UP-021, BL work result |
| Totality: closed result algebra and named next moves | C, P6 | Pr3 | RF-012, RF-014, AC-007, work result, RF Reconfigure When Necessary |
| Proportionality and cost exposure | C, P2 | attention is the scarce resource | UP-014, UP-019, UP-005 |
| Reconstructable representation of the method itself | C | Pr2 | RF-013, UP-018, UP-022, RF Method Self-Qualification for the method's functions; no clause benchmarks the recoverability of its published documents |
| Independent assessment | P6 | Pr4 | UP-007, UP-022, UP-020 |
| Shared machinery with distinct responsibilities | proportionality, P6 | a shared implementation is a candidate, not an owner | UP-019, UP-023 |
| Ambiguity governance (carry, decide, escalate, block) | P6, totality | risk appetite is Product-owned policy | Ambiguity Governance Rule |
| Lawful re-entry and change classes | P4b, P2 | a changed governing relation is accepted only at its owner | UP-018, UP-013, TM change class |

Hypotheses, none established by any rc.2 clause or by this attempt:

- H1, categorical structure: 𝒜, ℐ, 𝒞_H with S and R_H as functors.
  [Traversals And Functor Kinds](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#traversals-and-functor-kinds)
  states that a functor kind "does not by itself assert a category-theoretic
  functor" and that a model claiming one must define its categories and prove
  identity and composition preservation. Until someone writes the objects,
  arrows and laws and proves them, the diagram is notation.
- H2, universal algorithmic capture of meaning: refused by AC's own scope.
- H3, Markov boundary as statistical object: promotion gate not met.
- H4, runtime traversal composition laws (the "HoG monad"): no rc.2 clause
  mentions HoG; the term is ABG realisation vocabulary (section 5, correction
  5).
- H5, implicit in the formalisation: that "interpreted behaviour satisfies Σ"
  is decidable without an interpretation contract and an evaluator. UP-022
  makes conformance a semantic judgment against the governing basis, so S(a_j)
  ⊨ Σ is shorthand for a P1 contract plus a P6 judgment.

## 5. Contradictions, duplication and gaps

### Contradictions

1. P1's algorithmic clause reads as if a_c can decide meaning. AC-018
   confines mechanical decision to the structural subset and AC-019 permits a
   semantic decision only under an exact lawful decision contract.
   Resolution: qualify "algorithmic" (correction 6).
2. CAPABILITIES states that no universal budget is introduced, while UP-019
   already requires material algorithmic work to declare supported dimensions
   and limits before qualification. Not a contradiction in law. The recorded
   ABG failure (no cost term on day one) was a failure to select a claim, not
   an absence of law. Resolution: a selected-by-claim cost field (gap 4), not
   a principle.

The predecessor candidate listed two further contradictions and both are
withdrawn. One claimed that P5's standing denied derivation of composition;
the pinned `-02` text leaves derivation open, and the claim was made against
the retired `-01` wording. The other claimed an S(a_j) notation collision;
that notation is in the plan posts, not the common draft. The H overloading
(architecture subscript and HoG) is real and is handled by correction 7.

### Duplication

Each row is one obligation stated by several owners in different words. Under
UP-014 every extra statement is a reconciliation path a bounded actor must
hold. Count is of rc.2 clauses read in this attempt; unread files may add more.

| Obligation | Owners in rc.2 | Count |
|---|---|---|
| Conservation (authority, residual, judgment, frame, transition, successor claim, evidence by reference) | AC-005, AC-009, AC-016, RF-006, UP-004, UP-015, UP-017, UP-021, BL work result | 9 |
| Semantic, evidence and verdict separation | UP-008, RF-007, AC-018, AC-014, UP-022 | 5 |
| Reconstructability without private memory | RF-002, RF-013, UP-018, UP-020 intake, Reconstruction Litmus | 5 |
| Evaluation result algebra | RF-012, AC-007 | 2 near-identical algebras for one question; BL work result is a declared mapping of RF-012 |
| Probabilistic worker boundary | Probabilistic Work Boundary, OM Probabilistic Compute, UP-020, Ambiguity Governance lawful probabilistic processing | 4, specialisation declared only in ODD |
| Outcome conservation | UP-013, OM 11.5D TargetObligationBinding | 2 |

rc.2 also carries UP-020 dispositions, ODD's EdgeClosureDecision and the
Ambiguity Governance outcomes. They answer different questions (what to do
with a candidate, how an edge attempt closes, what happens to a declared
ambiguity) and are not duplicates of the evaluation algebra. Any 3.0
unification is limited to the RF-012 and AC-007 pair and must keep the other
three distinct; RF-012 already permits compatible refinement.

### Gaps

1. Context construction under an envelope. RF's
   [Select And Activate](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#select-and-activate)
   and
   [Reconfigure When Necessary](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#reconfigure-when-necessary)
   are generic operations: select a capable frame, bind it, load declared
   relations, refuse when nothing fits, then one of seven moves. AC-010
   defines material closure. What no clause states is the step between them:
   how a frame's material manifold is derived from a seed and relation family
   so that it fits a declared envelope (the AC-010 closure bound to RF-002),
   and what a lawful compression under RF-017 must preserve. This is an
   addition over existing operations, not absent governing law. ODD's
   `eval_gap` and `evaluate_next` are the only procedural account of that
   derivation, and they are profile law.
2. Recursive refinement of an outer contract into bounded inner steps is
   stated only in ODD graph functions and UP-020's causal cone. The generic
   core has no "A → X realised as A → B → … → X with conservation of the outer
   contract".
3. Selective acquisition. AC-011 forbids trimming required members. No clause
   permits authenticating a selected subset of a large immutable body without
   acquiring the whole. The Claude plan post in the tuple reports, from the
   2 October ABG handoff, a 504.8 MB manifest parsed to select 182 entries;
   that is an indirectly reported historical observation, not a tuple source.
   C2 input; the ABG primary sources are deferred and were not reacquired.
4. Cost of an activation. UP-014 applies proportionality to the method's own
   execution and states that no universal quota follows; UP-019 declares
   operational assumptions at design boundaries, by claim. RF-002's envelope
   is declared, never measured. The addition is selected, not universal: where
   capability fit under RF-002 or a cost claim under UP-019 is itself the
   governed question, the activation declares its allowance and reports spend
   with its measurement source. This ticket's allowance is one such
   selection; it does not establish a general requirement.
5. Generic work state. UP-020 has the preservation checkpoint and the restart
   rule, but "current persistent work state" is defined only in ODD's
   workspace, ledger and event triple. The core lacks the object the restart
   rule operates on.
6. Recoverability of the method's documents. RF-013 and UP-018 require a
   fresh actor to reconstruct from the basis; UP-022 and
   [Method Self-Qualification](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#method-self-qualification)
   qualify the method's functions through a fresh constructor and an
   independent evaluator. What no clause benchmarks is the published documents
   themselves: whether a fresh reader recovers the governing meaning from
   them, and at what reconstruction cost. That is what the matrix measures as
   F27 and F28 and scores 4/12 with F29 and F30. An addition over existing
   qualification law, not absent law.
7. Independence across actor families. UP-007, UP-022 and RF-007 require
   independence "for the assessed claim". No clause says whether two
   activations of one model family are independent for a semantic judgment.
   The C0 reviews were same-family; the C1 cross-review is not. The question
   needs an answer before C2 fixes acceptance criteria.

## 6. Candidate Spec Method mechanisms

Five questions per mechanism: requiring principle, transformation performed,
distinctions conserved, admissible alternative HOW, observable adequacy.

| Mechanism | Requiring principle | Transformation | Conserves | Alternative HOW | Adequacy |
|---|---|---|---|---|---|
| Constitutional chain with one WHAT and tenant HOWs | P2, P1 | ambiguity narrowed layer by layer | outcome; semantic versus realisation split | any decomposition passing the Reconstruction Litmus | two realisations satisfy one WHAT; litmus holds at each boundary |
| Bounded activation (intake, grant, territory, return) | C, P6 | basis → candidate, refusal, incomplete or re-entry | authority (RF-006), basis (AC-006), residuals (AC-009) | direct Writer entry or Executive coordination, both already lawful | a fresh actor reconstructs the activation from intake alone with history withheld |
| Closed result algebra | totality | evaluation → one of five results | indeterminate and out-of-frame pressure | compatible refinements (RF-012) | no coerced success; the cannot-fit case returns out_of_frame |
| Conservation accounting at step outputs | P4b | preserved, introduced, removed, residuals (AC-013) | failures, uncovered obligations, authority | reference versus copy | a detected failure A and an uncovered B survive a join |
| Independent assessment with freeze | P6, Pr4 | frozen subject → judgment | J ≠ O; subject unchanged | actor topology free (RF-016) | a planted defect is found with author material withheld (UP-022) |
| Ambiguity governance | P6, totality | ambiguity → carried, decided, escalated, blocked | hard stops | risk appetite per Product | no major ambiguity is silent |
| Change classes and smallest re-entry | P4b, P2 | observed gap → owning layer | upstream authority | sprint-local or ticket carrier | a changed governing relation is never accepted inside the acting frame |
| Proportionality review | C, P2 | obligation → justified or removed | ambiguity removed per reasoning added | none; it is the test, not a procedure | removing an obligation loses a detected ambiguity, or it did not |
| Outcome conservation (UP-013) | P2 | evidence → progress, prerequisite, preservation, regression | the selected outcome | Goals selection | evidence surfaces cannot enlarge the outcome |
| Successor disposition (UP-015) | P3, P6 | predecessor claim → one of four dispositions | claim identity across versions | consumer's record and proof mechanism | every rc.2 claim has a disposition before 3.0 qualifies; this applies to this project |
| Ticket-first intake | none as universal; triage derives from change classes | request → change intent, class, re-entry point | upstream authority | smallest existing carrier (TM) | the triage fields exist wherever substantive work starts; the ticket is one carrier |
| Steel-thread sequencing (BL) | proportionality, totality | increments ordered by consequential uncertainty | working composition | a HOW heuristic, not law | early integration evidence prunes incompatible choices |
| Design derivation chain (Ontology → Prime → IACS → views) | P1, proportionality | discovered functionality → derived operation identities | ownership, authority, singular admission | profile law (SOFTWARE_DESIGN), not core | the chain removes ambiguity proportional to its reasoning cost; this is the proportionality test case C2 should run first |
| Declared allowance and observed spend, where selected | C, proportionality; applicability by RF-002 fit or a UP-019 cost claim | activation → envelope and spend | the cost term | measurement source per host | spend is reported with its source, or marked unavailable; absent where no claim selects it |

Two mechanisms are precedent-only as universals: ticket-first (lawful as a
carrier choice, not a principle) and steel-thread sequencing (a heuristic).
One is missing as a selectable field: the declared allowance. One is the main
proportionality risk:
the design derivation chain, which the ABG lessons reported in the two plan
posts in the tuple identify as the overhead that displaced Product delivery;
the post-mortems themselves are deferred C2 sources.

## 7. Proposed corrections to the common principles

Returned to the common pen; not written by this tenant.

1. Add the generative statement C as a seventh commitment, or as P0, with its
   premises stated. Reduce P5 to totality. Without C in the common WHAT,
   four derived commitments have no stated origin and the 06 October Product
   statement is not represented in the principles that are meant to derive it.
2. Split P4 into typed composition (independent) and conservation of
   step-produced facts (derived from C, Pr1, Pr2a).
3. Add a commitment or a named gap for recoverable representation: the method's
   own published surfaces are subject to RF-013, with reconstruction cost as a
   measured quantity under UP-022. This is the matrix's strongest finding and
   has no principle.
4. Name the RF-012 and AC-007 evaluation-algebra unification as a C2
   capability, keeping construction dispositions, closure decisions and
   ambiguity outcomes as the distinct questions they are.
5. Replace "HoG monad laws" in the open claims with "runtime traversal
   composition laws". HoG appears in no rc.2 standard; keeping it in the
   common WHAT imports a realisation term into the foundations.
6. In P1's standing, state that "algorithmic" means explicit and structurally
   checkable (AC-018); structural success alone does not establish semantic
   fidelity, and a semantic decision needs an exact lawful decision contract
   (AC-019).
7. In the formalisation, rename either the functor S or the semantics S(a_j),
   and avoid H for both architecture and HoG.
8. Record gap 7 (independence across actor families) as an open question for
   C2 acceptance criteria.

## 8. Residuals

- Second successor relation: this candidate supersedes `45477038…00a2`
  after Codex's posted review
  (`stdo_3/build_tenants/codex/reviews/20261011T072147Z_REVIEW_claude_c1_principles.md`,
  SHA-256 `189aa622…90af`, which binds the initial predecessor). Two items
  were still open in the first successor and are closed here: the ABG
  handoff and post-mortems were described as tuple members and are now
  attributed to the plan posts that report them; P1 and P6 now carry
  non-entailment arguments instead of asserted independence.
- Successor relation: this candidate supersedes `329fe422…d0bb` after the
  independent review recorded in the ticket; the predecessor is retained.
  Changes: C restated without the carrying clause; conservation re-derived
  over step-produced facts with Pr2a; totality re-derived with P6 as a
  premise; two contradictions withdrawn as made against retired `-01` text or
  misattributed; correction 6 narrowed to AC-019; gaps 1 and 6 restated as
  additions over the existing RF engagement and self-qualification law; the
  cost field made selected-by-claim; the result-algebra duplication narrowed
  to the RF-012 and AC-007 pair; RF sections 575–660 and 1132–1200 added to
  the recovery.
- Not read in this attempt: IDENTITY_METHOD beyond the core law; UX_METHOD;
  RELEASE_METHOD beyond UP-015; TRAVERSAL_OCCURRENCE_PROFILE; GLOSSARY_GUIDE;
  the authority compressions; AC-013 beyond its record shape; AC-020;
  UP-002, UP-003, UP-006, UP-009, UP-010, UP-012; WORLD_MODEL beyond the cited
  sections; REFERENCE_FRAME_METHOD sections 480–575 and 662–1132; the
  baseline's specialist and testing frame sets. These may add duplication
  rows or further recovery for P3 and P6. Bounded by the allowance.
- The peer tenant's realisation was not read, per contract.
- ABG primary sources are deferred to C2; the lessons used here come only from
  the three plan posts and the matrix in the tuple.
- Provider token counters are not exposed to this host; the return reports
  wall time and marks counters unavailable.
- This attempt proposes no document organisation, reader route or a_c
  encoding; those are C3 and later.
