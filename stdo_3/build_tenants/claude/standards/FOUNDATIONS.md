# FOUNDATIONS

Tier 1. Owns the ontology, the commitments as law, the algebra of composition
and conservation, and the list of hypotheses. Every later document consumes
these definitions by reference and adds none of its own.

## 1. Vocabulary of standing

A clause in this corpus has one standing relative to the rc.2 builder:

- conserved: the rc.2 clause governs unchanged; the route is given;
- reframed: the obligation is kept and restated at a different scope or
  owner; the rc.2 clause continues to govern its own scope; the route and
  the change are given;
- superseded: an accepted successor relation replaces it; the route and the
  successor are given;
- new: no rc.2 clause states it; the requiring principle is given.

A commitment has one standing relative to the others: recovered, derived
(with named premises), independent (argued by non-entailment) or hypothesis.
This is
[UP-015](stdo://releases/v2.5.1-rc.2/standards/RELEASE_METHOD.md#successor-baseline-conservation-stdo-up-015)
applied to the corpus itself: an undisposed rc.2 obligation blocks
qualification.

## 2. Ontology

| Term | Definition | Requires |
|---|---|---|
| Subject | the thing a claim, representation or transformation is about; exact, with inventory and bytes or semantic addresses | P3 |
| Representation | bytes, text, a model or a program standing for a subject; equal representations do not establish equal meaning | P1 |
| Interpretation | a declared contract from representation to meaning within a context; says which distinctions a consumer may rely on and which are residual | P1 |
| Context | the declared scope under which an interpretation holds: subject, definitions, basis, admissible observations | P1 |
| Outcome U | a selected, owner-defined, directly verifiable state with an acceptance interval; adequacy of a transformation is judged against it | P2 |
| Object O | a subject with scoped identity (authority, kind, value), a boundary, current state and declared material relations; identity survives admissible state and encoding change | P3 |
| Actor | whoever performs a step within a declared capability envelope (context, attention, time, capability); roles (constructor, reviewer, executive) are relations an actor occupies, not kinds of actor | P0, P6 |
| Step | one bounded unit of work: intake, selected context, grant, execution, output | P0 |
| Step-produced fact | a judgment, residual, observation or authority decision produced by a step that cannot be re-acquired from declared sources; an observation reproducible from declared sources is re-acquirable and is not one | P0, P4b |
| Claim | an assertion with subject, property, basis, witness relation and falsifier | P6 |
| Evidence | artifacts, events, observations used to evaluate a claim on a basis | P6 |
| Judgment | a recorded evaluation over an unchanged subject, with evaluator, decision, evidence, scope and revising observation | P6 |
| Authority | an identity-bearing permission to operate or to dispose acceptance within a scope; never minted from capability, label or reachability | P6 |
| Residual | a material uncertainty, omission, loss or unproven relation that remains until an authorised disposition | P4b |
| Basis | the exact immutable set of definitions a step, claim or result binds; mixed bases need an explicit composite relation | P6 |
| Material | of a relation, uncertainty or closure: its change can alter a result, the validity of a basis, the sufficiency of evidence or an authority; the relation family of CALCULUS §2 is the material relations of a step | P2, P6 |

Dispositions: subject, representation and interpretation conserve
[AC Interpretation And Models](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#interpretation-and-models)
and
[bounded-context semantic resolution](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#bounded-context-semantic-resolution);
identity conserves
[IDENTITY_METHOD](stdo://releases/v2.5.1-rc.2/standards/IDENTITY_METHOD.md#1-scoped-identity)
and
[AC-002](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-002-scoped-identity);
outcome conserves
[UP-013](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#product-outcome-conservation-stdo-up-013);
actor and envelope conserve
[RF-002](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-002-finite-attention);
claim, judgment and authority conserve
[UP-001](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#proof-target-identity-and-adequacy-stdo-up-001),
[AC-014](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-014-judgment-separation),
[UP-004](stdo://releases/v2.5.1-rc.2/standards/IDENTITY_METHOD.md#authority-identity-and-conservation-stdo-up-004);
residual and basis conserve
[AC-009](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-009-residual-conservation)
and
[AC-006](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-006-basis-coherence).
Step and step-produced fact are reframed from the
[Probabilistic Work Boundary](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#probabilistic-work-boundary)
and
[Return A Closed Result](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#return-a-closed-result)
to the generic unit.

## 3. Commitments

P0 Bounded construction. A finite actor realises a selected outer contract
through steps. Each step's selected context fits the actor's envelope. The
actor's internal path within a step is its own. Recovered as a composite;
the generic statement is reframed from the ODD profile's graph functions.
Premises: a selected outcome (P2); the actor of one step need not be the
actor of the next and may re-acquire declared sources but not private
memory; step-produced facts are not re-acquirable; the world is open; a
step's output is a candidate until evaluated.

P1 Interpretation. Subject, representation and interpretation are distinct;
meaning holds within a declared context through a declared contract.
Independent: with purpose, identity, evidence and authority fixed, two
contracts give one representation two meanings. "Algorithmic" means explicit
and structurally checkable; a semantic decision is lawful only under an exact
decision contract; structural success never establishes fidelity. Conserves
[AC-017](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-017-interpretation-fidelity),
[AC-018](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-018-structural-and-semantic-separation),
[AC-019](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-019-valid-model),
[RF-008](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-008-overlap-without-identity-collapse).

P2 Purpose. A selected outcome defines adequacy; interfaces inherit material
obligations from the transformation they serve; an obligation with no route
to the outcome is unjustified. Independent: identical capacity serves
opposite purposes. Conserves UP-013,
[UP-014](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#proportional-method-and-delivery-stdo-up-014),
[UP-005](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#boundary-and-governance-cost-stdo-up-005).

P3 Identity. An object's identity is declared (authority, kind, value) and
survives admissible change; current state, historical observation and
representation identity stay separate; a boundary is a claim with a proof
obligation. Independent: equal capacity admits identity by persistence or by
digest. Conserves AC-002, AC-014, the
[recursive Product taxonomy](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#recursive-product-taxonomy),
[Entity Cut Construction Law](stdo://releases/v2.5.1-rc.2/standards/WORLD_MODEL_METHOD.md#entity-cut-construction-law).

P4a Typed composition. Two steps compose only when the first's result type
and judgment satisfy the second's domain and preconditions; composition
retains both identities, intermediate results, judgments, evidence,
authority, provenance and stop states. Independent. Conserves
[AC-016](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-016-typed-composition),
[RF-010](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-010-composition-on-demand).

P4b Conservation of step-produced facts. Judgments, residuals, observations
and authority decisions the outer contract needs are recorded by the step
that produced them; sources a later step can re-acquire are governed by
sufficiency, not conservation. Derived from P0 with P2 and the
step-produced-facts premise. Reframed from
[AC-009](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-009-residual-conservation),
[AC-013](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-013-transformation),
[AC-005](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-005-authority-conservation),
[UP-017](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#bounded-frame-conservation-stdo-up-017),
[UP-021](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#complete-enclosing-relation-admission-stdo-up-021),
whose nine statements of conservation become one obligation with typed
instances (authority, residual, judgment, frame, transition, successor
claim, evidence by reference); each continues to govern its own scope.

P5 Totality. A step can meet a condition outside its context; it cannot
report success on one; so its result algebra carries indeterminate,
out_of_frame and invalid_basis as first-class outcomes and its control model
names the next move. Derived from P0 with the open-world premise and P6.
Conserves
[RF-012](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-012-closed-results),
[RF-014](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-014-capability-fit),
[AC-007](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal),
[Totality Rule](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#8-totality-rule);
RF-012 and AC-007 are restated once in CALCULUS §3 and continue to govern.

P6 Justification and authority. Definitions, assumptions, observations,
candidate judgments and accepted claims have distinct standing; evidence
supports a claim on a basis; authority permits or disposes within scope;
neither is minted by the other. Independent: a bounded actor satisfying all
else can still take a green label as acceptance. Conserves UP-001,
[UP-008](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#semantic-evidence-and-projection-separation-stdo-up-008),
[UP-022](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#assurance-boundary-congruence-and-method-qualification-stdo-up-022),
UP-004,
[RF-006](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-006-authority-conservation),
[RF-007](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-007-semantic-evidence-and-verdict-separation).

## 4. Algebra

Composition. For steps s₁: X → Y and s₂: Y → Z, s₂ ∘ s₁ exists only under P4a.
The composite's output carries both steps' step-produced facts. Composition
law is required only where the governing evaluation combines internal
variables or transports values across steps; independent closed results may
instead go to one declared conjunction (RF-010).

Conservation accounting. Every transformation records what it preserved,
introduced and removed, its external resolution witnesses and its residuals
(AC-013). For a required obligation set R and admitted coverage C, uncovered
coverage is R minus C; combining results takes the union of known failures
and recomputes uncovered coverage; a composite with a known failure or an
uncovered required obligation cannot project success. A known failure A and
an uncovered obligation B survive every join.

Reference versus body. A reference conserves a relation when its owner,
exact selector, authenticity, availability and completeness support the same
consuming decision. An inaccessible or insufficient reference is a residual,
not success. A projection cannot trim a required member to fit a carrier or
budget
([AC-011](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-011-projection)).

Latitude. Two values differ lawfully only through a declared latitude or
transformation relation; preference, probabilistic choice and human presence
are not implicit latitude
([AC-008](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-008-explicit-latitude)).

Shared machinery. Computational similarity yields a commonisation candidate,
never an adjudication of identity or authority; one implementation may serve
many instances while each instance keeps its responsibility and binding
([UP-019](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#computational-realization-projection-stdo-up-019),
[UP-023](stdo://releases/v2.5.1-rc.2/standards/DESIGN_MODULE_METHOD.md#capability-and-foundation-selection-stdo-up-023)).

Formal fragment (new in this corpus; P1). Where 𝒜 is the free category on
typed primitives, ℐ the selected carrier sets with total functions and 𝒞_H
pairs of functions with additive costs, S: 𝒜 → ℐ and R_H: 𝒜 → 𝒞_H are
functors and S is not faithful; that S is not an equivalence. Any further
categorical claim defines its objects, arrows, identities and composition and
proves preservation (conserves
[functor kinds](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#traversals-and-functor-kinds),
which states that obligation and asserts no categorical functor itself).
H names an architecture, never a runtime.

## 5. Hypotheses

Not law; carried for falsification: categorical equivalence of 𝒜 and ℐ under
some reformulation; universal algorithmic capture of meaning; the statistical
Markov boundary (candidate status under
[WORLD_MODEL_METHOD](stdo://releases/v2.5.1-rc.2/standards/WORLD_MODEL_METHOD.md#epistemic-status-of-the-construct));
traversal composition laws of any runtime.

## 6. Source dispositions

| rc.2 clause family | Disposition in this corpus |
|---|---|
| AC-001 to AC-012, AC-014 to AC-019 | conserved by reference; AC-007 is restated in CALCULUS §3 as the one result algebra |
| AC-013 transformation record | conserved; its fields are the conservation accounting above |
| AC-020 layer and release separation | conserved by reference; applied in SPEC_METHOD §6 |
| RF-001 to RF-017 | conserved by reference; RF-012 restated in CALCULUS §3; RF-002/003/014/017 consumed by CALCULUS §2 |
| UP-001, UP-004, UP-008, UP-022 | conserved; consumed by EVALUATION |
| UP-013, UP-014, UP-005 | conserved; consumed by SPEC_METHOD §3 and CALCULUS §6 |
| UP-015 | conserved; applied to this corpus in §1 |
| UP-016, UP-018, UP-019, UP-023 | conserved; UP-018 consumed by CALCULUS §1, UP-019/023 by §4 above; UP-016 stays in the software-design profile |
| UP-017, UP-021 | conserved; reframed with AC-005, AC-009 and AC-013 into P4b's one obligation |
| UP-020 | conserved; consumed by CALCULUS §1, §3, §5 |
| Probabilistic Work Boundary, Ambiguity Governance | conserved; consumed by CALCULUS §1 and §3 |
| ODD, DESIGN_MODULE, UX, WORLD_MODEL profile law | conserved by reference in PROFILES; nothing imported into tier 1 |
