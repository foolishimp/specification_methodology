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
semantic, authority-bearing, installed or end-to-end claim because the
weaker property is easier to measure (P6; conserves
[UP-001](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#proof-target-identity-and-adequacy-stdo-up-001)).

A claim's quantifier, population and scope cannot exceed its evaluated
evidence. Generalising a local observation needs a declared inference
relation, the comparable population and explicit counterexample treatment.
Later counterevidence invalidates every dependent verdict until the
claim-evidence relation is requalified
([UP-022](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#assurance-boundary-congruence-and-method-qualification-stdo-up-022)).

## 2. Separation

Semantic law defines what an evaluation means; evidence supplies
observations; the evaluator applies the declared relation; decision
authority disposes. One actor may lawfully perform several; the record keeps
them distinguishable. Evidence change may invalidate a verdict without
changing law; projection change may invalidate a view without changing
truth; semantic change requires re-entry and invalidates dependent
acceptance (conserves
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
(ACTIVATION §7). Any post-exposure revision is a declared intervention and a
new subject (UP-022).

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
incumbent (conserves the
[Reconstruction Litmus](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#reconstruction-litmus)
and
[UP-022](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#assurance-boundary-congruence-and-method-qualification-stdo-up-022)'s
comparison rule, under which unique derivation, determinism and incumbent
equality are not generic comparison criteria). A weak Σ that admits materially different
behaviours either declares the latitude or is repaired before a
decision-complete design is claimed.

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

The method is qualified the way it qualifies anything else: a fresh
competent constructor, inside a declared envelope, using only the declared
ordinary method and authority surfaces and declared trial subjects, with
material reference outcomes, incumbent realisations, author memory and ad
hoc rescue withheld until freeze wherever earlier exposure would
compromise reconstructive independence; then an independent evaluator
compares the frozen result with the method's mandatory relation
population. This conserves
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
| UP-001, UP-022 | conserved; §1, §3, §6 |
| UP-008, RF-007, AC-018, AC-019 | conserved; §2 |
| UP-007 | conserved; §3 |
| RF-013, UP-022 qualification protocol | conserved; §7; the benchmark is new |
| RF frame qualification, method self-qualification | conserved; §7; rows in the table below |
| UP-013 acceptance interval, AC-014, UP-004 proxy grant, UP-020 proxy limits | conserved; §5 |
| Reconstruction Litmus | conserved; §6 |
| TICKET judgment continuity | conserved via ACTIVATION §7 |
| Baseline Reviewer and technical triage | conserved by reference; §4 states the result shape |

RF rows received by this member (anchors into rc.2
REFERENCE_FRAME_METHOD.md):

| Anchor | Disposition | Locus |
|---|---|---|
| #frame-qualification | conserved | §7 Frame qualification |
| #method-self-qualification | conserved | §7 Method self-qualification |
