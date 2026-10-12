# EVALUATION

Tier 1. Owns how claims are justified and accepted: claims, evidence,
independent assessment, review results, acceptance, conformance of
realisations, and the qualification of frames and of the method itself.
Consumes
[FOUNDATIONS](FOUNDATIONS.md) and the result algebra in
[ACTIVATION §3](ACTIVATION.md).

## 1. Claims

A load-bearing claim names its exact subject, the property claimed, the
governing basis, the relation between witness and claim, the nearest weaker
property it excludes, and its falsifier, before a witness is selected.
Without these it is evidence discovery, not proof. Packaging, syntax,
compilation, presence, invocation or local behaviour never substitutes for a
semantic, authority-bearing, installed, release or end-to-end claim because
the weaker property is easier to measure (P6; conserves
[UP-001](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#proof-target-identity-and-adequacy-stdo-up-001)).

Boundary congruence. A checker, validator, harness, reviewer or other
assurance surface supporting promotion or closure binds the exact claimed
subject and its authoritative composition relation. Evidence over one file
or carrier proves only that boundary; it cannot establish a multi-file or
carrier-set claim. Cross-carrier satisfaction and conflict are decided at
the declared composite boundary (P3, P6). A claim of mechanical enforcement
names an executable or reproducible predicate and a witness reachable
through the declared ordinary assurance path; a planned or
specification-only harness is planned evidence, not observed verification,
and until both the predicate and such a witness are observed the claim
remains open or is explicitly downgraded to the planned property (P6;
conserves
[UP-022](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#assurance-boundary-congruence-and-method-qualification-stdo-up-022),
first two paragraphs).

A claim's quantifier, population and scope cannot exceed its evaluated
evidence. Generalising a local defect or observation needs a declared
inference relation, the relevant comparable population, explicit
counterexample treatment and governing evidence. Later counterevidence
invalidates every dependent verdict until the claim-evidence relation is
superseded, withdrawn or requalified (UP-022). The quantifier rule and the
boundary rule are false if assurance observes a weaker or different
subject, if per-carrier evidence closes an unevaluated composite claim, if
mechanical enforcement lacks its predicate or a reachable witness, if
planned evidence is reported as observed verification, if a verdict outruns
its evaluated population or declared inference relation, or if dependent
verdicts survive material counterevidence without requalification.

## 2. Separation

Three bases stay distinct (P6, P1): the semantic basis, the constitutional
and accepted-design relations that define what a claim means; the evidence
basis, the exact artifacts, events, logs, tests and observations used to
evaluate it; and the state projection, a current view derived from admitted
semantic and evidence bases. Semantic law defines what an evaluation means;
evidence supplies observations; the evaluator applies the declared
relation; decision authority disposes. One actor may lawfully perform
several; the record keeps them distinguishable. Evidence change may
invalidate a verdict without changing law; projection change may invalidate
a view without changing semantic truth; semantic change requires lawful
re-entry and invalidates affected downstream acceptance. A broad digest may
conservatively invalidate a review; it does not prove that every semantic
relation changed (conserves
[UP-008](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#semantic-evidence-and-projection-separation-stdo-up-008),
[RF-007](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-007-semantic-evidence-and-verdict-separation)).

Structural conformance decides closed syntax, types, identities, references,
bases and mechanically decidable predicates. Semantic fidelity decides
meaning and materiality. A checker decides the structural subset; it claims a
semantic or authority subset only under an exact lawful decision contract
supplied by the model
([AC-018](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-018-structural-and-semantic-separation),
[AC-019](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-019-valid-model)).
A valid parse, a valid map, a green test and a historical judgment each
establish exactly their own claim.

## 3. Independent assessment

A constructor's self-review is construction output, not assessment. Where
promotion needs independent assessment, the assessor evaluates the exact
live subject, authority paths, proof and installed state, not the
constructor's summary (P6 with the probabilistic-construction premise;
conserves
[UP-007](stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md#execution-and-verification-authority-separation-stdo-up-007)).

Protocol: the subject is frozen by identity before material reference
exposure; the assessor records its expectations from the governing source
before opening the candidate; it reads the subject at a named immutable
identity, never a working tree; it makes no repair; it does not assess its
own authorship. Reusing the constructor's judgment does not satisfy
independence; shared mechanical evidence may be reused, judgment may not
(ACTIVATION §7). Any post-exposure revision is a declared intervention: it
is either a method constituent with its own qualification boundary or a new
qualification subject, and it cannot retroactively make the original
frozen construction pass. This law prescribes no actor type or count,
review-round count, engine, prompt or orchestration (UP-022).

Independence across actor families is declared, not assumed. Whether two
activations of one model family are independent for a semantic judgment is a
policy the governing basis states for the claim; the default where it is not
stated is that they are not independent.

## 4. Review results

A review returns one core result (ACTIVATION §3) for each declared predicate it
evaluated, with: the exact subject and basis, the evidence consulted, the
findings ranked by consequence, each finding's evidence and the smallest
bounded correction, the residual uncertainty, and the invalidation
conditions. It recommends a disposition; it does not apply one. A finding
without evidence a consumer can chase is commentary.

### Result and triage projection

Where a review returns findings with technical triage, the triage is the
assessor's evidence-bound assessment of each finding against the exact
evaluated claim and basis. Severity, the assessor's grade of consequence,
is evaluation evidence. Priority, the effect on the current promotion
boundary and the disposition are the decision owner's (ACTIVATION §1,
Roles and delegation) and stay distinct values even where a
Product-defined policy maps one to another. The recommended disposition
above is evidence for the decision owner: it is not a disposition, a
priority or a boundary effect, and it is never adopted mechanically (P6,
RF-007). The fields of a triage are declared by the profile that adopts it, and
the scales it uses are bound by the adopting Product (P2, P6; provenance
[reviewer result and triage projection](stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md#reviewer-result-and-triage-projection)).

The projection of the finding-level triage payload is total over the result
algebra of ACTIVATION §3. The payload classes `complete`, `indeterminate`
and `not_applicable` classify the triage only; they are not new results,
dispositions, priorities or lifecycle states (P5, P1).

| Core result | Finding and triage payload | Decision-owner consumption constraint |
|---|---|---|
| satisfied | an explicit no-finding state; triage `not_applicable`; evidence, residuals and invalidation stay present | priority and boundary effect are `not_applicable` to this result unless another exact consumed result supplies a finding |
| falsified | one or more exact findings; triage `complete` where supported, keeping `indeterminate` fields where evidence cannot close them | apply the Product-owned priority and boundary policy without mapping severity mechanically to a disposition |
| indeterminate | a partial finding or observation state; triage `indeterminate`; the exact evidence gaps and residual uncertainty | keep the uncertainty or reactivate a capable evaluation; do not consume it as satisfaction or as a closed finding |
| out_of_frame | the evaluated claim needs an undeclared material relation or evaluator capability; triage `indeterminate`; the missing relation or capability and the exact reconfiguration pressure are named | refine or reconfigure a capable activation and keep the claim unresolved; do not consume the result as satisfaction or falsification |
| invalid_basis | a basis failure; triage `not_applicable`; invalidation evidence and basis-repair pressure | refuse to consume the result and return through the declared basis re-entry relation |

An adjacent observation outside the evaluated claim does not replace the
claim-relative result. The assessor returns it separately, with triage
`not_applicable` to that claim and the exact repricing or re-entry
pressure; the decision owner returns it to its declared owner without
creating a claim-relative block, or another review round, from its
severity alone (P6, P2).

The assessor returns to the decision owner, not to the constructor. It does
not edit the candidate, direct the repair or authorise continuation (P6,
§3).

## 5. Acceptance

Acceptance is the decision owner's disposition over an unchanged subject;
recording it cannot widen it, and it exhausts only the instance and interval
it names (P6, P2; conserves
[UP-013](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#product-outcome-conservation-stdo-up-013),
[AC-014](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-014-judgment-separation)).
A work item closes by the condition it stated, not by a reviewer's approval;
a reviewer result is an input to closure, never the closure. Green labels,
document counts, review counts and historical outcomes are not acceptance.
A human decision may be exercised directly or through an explicitly admitted
bounded proxy whose grant names its scope and exclusions
([UP-004](stdo://releases/v2.5.1-rc.2/standards/IDENTITY_METHOD.md#authority-identity-and-conservation-stdo-up-004));
a proxy cannot change Product meaning, requirements, governing authority
or accepted design, and such a change re-enters at its owning relation
([UP-020](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#agentic-construction-execution-stdo-up-020)).

## 6. Conformance of realisations

A realisation aⱼ conforms to a specification Σ when its interpreted behaviour
satisfies Σ under a declared interpretation contract (P1) and an independent
judgment (P6). Conformance establishes neither identical behaviour outside Σ
nor equal cost; semantic equivalence and computational equivalence are
separate claims with separate evidence. Several realisations may conform to
one Σ; sufficiency does not require unique derivation or equality with an
incumbent. A weak Σ that admits materially different behaviours either
declares the latitude or is repaired before a decision-complete design is
claimed.

Layered sufficiency. A specification arranged in layers is sufficient when
a competent actor can derive a conformant next layer from each layer; the
derivation need not be unique, since different realisations may satisfy the
same upper layer, and the test is sufficiency, not determinism. A failure
to derive at any boundary is a defect of the upper layer: unclear,
contradictory, underspecified, not concrete or decomposable enough, or
polluted with accidental lower-layer detail. A boundary that can be crossed
only by hiding a major unresolved ambiguity is not yet sufficient even if
some downstream artifact can be produced. For an already accepted relation,
reconstruction may reuse its exact current basis and sufficient evidence
after checking applicability and invalidation (ACTIVATION §7);
reconstructability requires a correct reconstruction route, not its
execution at every use, grants no restart authority and does not excuse
stale success. The claim determines the reconstruction span; a local
selected function does not require recreating the whole subject. New
material counterexamples still challenge the affected relation (P2, P1,
P0; conserves the
[Reconstruction Litmus](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#reconstruction-litmus),
whose application to the method's own chain, with the diagnosis per layer,
is SPEC_METHOD §2).

Comparison. After freeze the evaluator compares the frozen result against
the mandatory governing semantic basis for semantic conformance or
equivalence. A separately held expected or reference outcome, if one exists
and is applicable, is optional evidence and explicitly non-authoritative;
semantic equivalence to it is required only where the governing basis
requires it. A lawful alternative construction permitted by the basis
passes. Subjective similarity to the basis or the reference is insufficient
to establish conformance or equivalence. Byte or structural identity,
unique derivation, determinism and incumbent equality are not generic
comparison criteria. A construction outside the declared competence or
configuration envelope cannot indict generic method sufficiency (P6, P1;
conserves
[UP-022](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#assurance-boundary-congruence-and-method-qualification-stdo-up-022)'s
comparison rule).

## 7. Qualification of frames and of the method

### Frame qualification

A candidate frame ([REFERENCE_FRAME](REFERENCE_FRAME.md)) is qualified in
proportion to its claims (P6, P2; provenance
`stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#frame-qualification`).
The minimum evaluation asks:

1. Decision test: can a competent actor produce a result in the declared
   algebra for representative in-domain evaluations?
2. Reconstruction test: can a fresh competent actor activate the frame
   from the declared packet without hidden history (RF-013)?
3. Sensitivity test: do changes to declared material relations affect the
   result where expected?
4. Irrelevance test: do excluded unrelated changes leave the result stable
   where expected?
5. Basis test: does stale, mismatched or ambiguous basis information
   invalidate or refuse the evaluation?
6. Authority test: does frame selection preserve semantic and decision
   authority and the exact inherited operation authority for every
   material construction, transformation, admission, publication or
   mutation?
7. Counterexample test: does the frame detect the representative
   historical or constructed violations it claims to cover?
8. Capability test: can the declared actor class hold and operate the
   frame within its envelope?
9. Result-consumption test: can a declared consumer use the closed result
   without importing hidden frame context?

Qualification binds the exact frame revision, actor envelope, evaluation
family, basis class and evidence conditions evaluated. It does not
generalise to an unevaluated population by naming the frame generically
(§1, the quantifier rule).

### Method self-qualification

The method is qualified the way it qualifies anything else. Qualification
of generic method sufficiency consumes the work boundary (FOUNDATIONS §2),
the construction and assessment relation of ACTIVATION §1 and the layered
sufficiency of §6; it creates no second process. A fresh competent
constructor operates inside a declared capability, context and
configuration envelope, using only the declared ordinary method and
authority surfaces and declared trial subjects. An independently
authorised evaluator has a declared governing basis and comparison
predicate. Material expected or reference outcomes, source exemplars or
incumbent realisations, author memory and ad hoc rescue are withheld from
the constructor until its construction result is frozen wherever earlier
exposure would compromise reconstructive independence; then the evaluator
compares the frozen result with the method's mandatory relation population
under the comparison rule of §6. This conserves
[Method Self-Qualification](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#method-self-qualification),
which leaves the constructor, freeze and assessor protocols to the
governing authority, and
[RF-013](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-013-reconstructable-activation)
for the reconstructability of the activation; the surfaces rule and the
conditional withholding conserve
[UP-022](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#assurance-boundary-congruence-and-method-qualification-stdo-up-022)'s
qualification protocol. The constructor, freeze, assessor, acceptance and
release protocols are supplied by the governing authority; this member
defines none of them.

The qualification population is every function and failure relation the
method claims (REFERENCE_FRAME §5), each with its required representative
observations (P6):

| Relation under qualification | Required representative observations |
|---|---|
| `declare` | a frame set derived from a governed workspace, outcome, practices, capability envelopes, evaluation inventory, authority and residual boundary; missing authority or evaluation basis refuses |
| `activate` | activation with an exact subject and basis and a capable actor succeeds; stale, ambiguous, topology-mismatched, unauthorised and capability-incompatible activations refuse or return the applicable closed pressure |
| `evaluate` | representative `satisfied`, `falsified`, `indeterminate`, `out_of_frame` and `invalid_basis` results; sensitivity to material changes and stability under established irrelevance |
| `conjoin` | compatible closed results decide under the declared rule; result conflict, basis mismatch, mandatory indeterminacy and a declared veto return conflict, indeterminate or refusal without flattening frame meaning |
| `translate` | preserved coordinates and provenance reach the target; declared loss stays explicit; identity, basis, authority or equality mismatch refuses |
| `audit_coverage` | evaluation, interaction, semantic, operation and decision authority, failure, capability and required independently activated or assurance-independent coverage map to capable frames or explicit residuals; artifact or actor count cannot close coverage |
| `revise` | historical failure, topology mutation, evidence change and capability change produce the declared frame-set delta and identify every prior activation, result, conjunction and coverage claim requiring reevaluation |
| result consumption | a declared consumer uses one closed result without importing hidden frame context or authority; insufficient output produces a reconstructability failure |
| material composition | a case requiring cross-frame execution declares composition, order where material, closure, failure and the conservation of semantic, operation and decision authority; a case not requiring composition stays uncomposed |

One valid frame-set declaration and coverage result establishes only the
`declare` and evaluated `audit_coverage` population; it proves activation,
evaluation, conjunction, translation, revision, result consumption and
material composition by no implication. Each relation is exercised through
representative positive, boundary and falsifying cases. Qualification may
be staged, and every verdict states the exact functions, frame revisions,
actor envelopes, basis classes, result branches and evidence populations
evaluated; an unevaluated function or branch stays open rather than
inheriting a whole-method verdict (P6; §1). Prior exemplar frame sets or
outcomes may serve as optional comparison evidence after freeze; they are
not mandatory target answers unless the governing basis explicitly requires
equivalence (§6).

Derived guidance. Changed derived guidance, a compression, a frame packet,
a skill or any other projection of the method, is qualified against
source-derived expected behaviour, including the affected permissions,
exclusions and invalidators. For a native use claim, an ordinary actor
applies that guidance through its declared entry and available context.
Digest integrity and index generation establish identity and structure,
not semantic fidelity or usability. Mechanical and operational claims
require their own executable observations, including the applicable
workload and operational assumptions of ACTIVATION §6; semantic agreement
cannot substitute for those observations (P6, P1; UP-022).

The qualification law is false if constructor competence or its
capability, context or configuration envelope, or evaluator authority,
governing basis or comparison predicate, is undeclared, or an
out-of-envelope construction is used to indict the method; if the
constructor uses supplemental method or authority input that is not
declared; if a material expected or reference outcome, source exemplar or
incumbent realisation, author memory or ad hoc rescue is exposed to the
constructor before freeze where that exposure compromises reconstructive
independence; if comparison omits the mandatory governing semantic basis,
proceeds under constructor authority instead of independently authorised
evaluator authority, or is self-adjusted after seeing the result; if a
reference outcome is used as authority, reference equivalence is required
where the governing basis does not require it, basis-required reference
equivalence is omitted, subjective similarity is used as proof, or
identity, unique derivation, determinism or incumbent equality substitutes
for semantic conformance or equivalence; or if a post-exposure revision is
unclassified or is used to make the original frozen construction pass
retroactively (§3).

Recoverability benchmark (new; derived from P0 with the actor-change
premise). For a selected activation, measure whether a fresh actor given
only the published documents recovers the governing relations with fidelity
judged independently, and at what reconstruction cost (context transferred,
time, and spend where measurable), against the rc.2 corpus as baseline. A
document set that requires private validator knowledge, whole-corpus loading
or a prior actor's memory fails the benchmark regardless of its content.
This is the observable for the matrix criteria F27 and F28; F29 and F30 are
the same observation reported with the task completed, the material errors
detected and the cost.

## 8. Source dispositions

| rc.2 clause | Disposition |
|---|---|
| UP-001 | conserved; §1; row in the table below |
| UP-022 | conserved in full; boundary congruence, mechanical enforcement and the quantifier rule in §1, freeze and post-exposure revision in §3, the comparison rule in §6, the qualification protocol, derived guidance and the falsifiers in §7; row in the table below |
| UP-008, RF-007, AC-018, AC-019 | conserved; §2; UP-008's row in the table below |
| UP-007 | conserved; §3 |
| RF-013 | conserved; §7; the benchmark is new |
| RF frame qualification, method self-qualification | conserved; §7; rows in the table below |
| UP-013 acceptance interval, AC-014, UP-004 proxy grant, UP-020 proxy limits | conserved; §5; UP-013 is restated in SPEC_METHOD §3 and UP-020's delegation in ACTIVATION §1 |
| Reconstruction Litmus | conserved; the generic layered-sufficiency law in §6, its application to the chain in SPEC_METHOD §2; row in the table below |
| TICKET judgment continuity | conserved via ACTIVATION §7 |
| Baseline reviewer result and triage projection | conserved; restated in §4 Result and triage projection with assessor and decision owner in place of the profile's Reviewer and Executive; the profile's triage fields and its steps are EXECUTIVE_BASELINE §5 and §12; row in the table below |

RF rows received by this member (anchors into rc.2
REFERENCE_FRAME_METHOD.md):

| Anchor | Disposition | Locus |
|---|---|---|
| #frame-qualification | conserved | §7 Frame qualification |
| #method-self-qualification | conserved | §7 Method self-qualification |

SM rows received by this member (anchors into rc.2 SPEC_METHOD.md):

| Anchor | Disposition | Locus |
|---|---|---|
| #proof-target-identity-and-adequacy-stdo-up-001 | conserved; the six named relations and the weaker-property rule including release proof | §1 |
| #semantic-evidence-and-projection-separation-stdo-up-008 | conserved; the three bases, the three invalidation cases and the digest rule | §2 |
| #assurance-boundary-congruence-and-method-qualification-stdo-up-022 | conserved in full; the nine falsifiers are split between §1 (boundary, enforcement, quantifier) and §7 (qualification) | §1, §3, §6, §7 |
| #reconstruction-litmus | conserved; the generic law here, the five layer derivations and the per-layer diagnoses in SPEC_METHOD §2; the design-view coverage gate stays with the design profile | §6 Layered sufficiency; SPEC_METHOD §2 Reconstruction litmus |

Baseline rows received by this member (anchors into rc.2
STDO_REFERENCE_FRAME_BASELINE.md):

| Anchor | Disposition | Locus |
|---|---|---|
| #reviewer-result-and-triage-projection | conserved; all five result rows and the adjacent-observation rule; "Reviewer" written as assessor and "Executive" as decision owner; the sentence on the recommended disposition reconciles §4's "recommends a disposition" with the predecessor's "no priority or disposition" | §4 Result and triage projection |
