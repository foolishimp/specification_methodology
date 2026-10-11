# T-01 Run A return: 20261011-A-claude-fresh-001

Case: urn:stdo-3:claude:case:T-01, Run A (per-step subject context cap
160,000 bytes). Constructor: fresh Claude context (model id
claude-fable-5-1), one bounded activation, no conversation history, no
design notes, no C1 realisation, no reviews. Wall clock: start
2026-10-11T11:15:32Z, end recorded in the last section.

Stop state: satisfied. Composite result for FOUNDATIONS §3 routes: satisfied
(22 of 22 routes satisfied; no known failure; no uncovered route). Residuals
are listed in the final section and do not alter any route result under the
decision contract declared below.

## 1. Intake (CALCULUS §1)

Outcome served. The T-01 shared task: for every
`stdo://releases/v2.5.1-rc.2/standards/<member>#<slug>` link in FOUNDATIONS
§3 Commitments, confirm the heading slug exists in the installed rc.2 member
and judge whether the tenant's characterisation of the clause is consistent
with the rc.2 text at that heading; return one core result per route and one
composite result for the section. This serves the conformance trial named in
CASE.md (CONFORMANCE §2 / thread T1) as an experiment; it is not promotion of
anything.

Affected relation set and invariants. The 22 route relations from FOUNDATIONS
§3 to rc.2 headings, plus the section-level conjunction over them. Governing
invariants: a clause's standing vocabulary (FOUNDATIONS §1: conserved means
the rc.2 clause governs unchanged and the route is given); the result algebra
and its no-coercion rule (CALCULUS §3); the fit test and the ban on silent
omission (CALCULUS §2); claim discipline (EVALUATION §1); separation of
semantic law, evidence, evaluator and disposition (EVALUATION §2). Nothing
this run produces disposes acceptance; the constructor's self-review is
construction output (EVALUATION §3).

Basis, by identity (sha256 computed by this actor at run time):

| Input | Bytes | sha256 |
|---|---|---|
| standards/FOUNDATIONS.md | 14,463 | 5f5e7ab3b820657ec5992aa3eb9c0bc7a6f937dbe9ec0f36eb75014429efed80 |
| standards/CALCULUS.md (§1–3 read, lines 1–108) | 13,470 (6,328 read) | 879fb9dd7c8f59c866f2e9564e685dd57611bbeabd2806dc40d9b0ea5fb582ad |
| standards/EVALUATION.md (§1–4 read, lines 1–80) | 8,042 (4,403 read) | fc063460e6834c190bcc5fe045d4a5a8f45a2ffd96a0ec2cad4fa82b677f246d |
| a_c/t1/projection-bounded-activation-materialized.json | 85,546 | 728973230d798e051290cee41eb183aaef6b7903beffcf4db573036fccdbb990 |
| qualification/cases/T-01/CASE.md | 6,800 | 53cd9f6fea7c633d7b4337b7e245c967b643ad9649a2aff73c7e9ef3e0b6082a |
| qualification/cases/T-01/fragment.py | 2,472 | 02c7128913df35b614ec9ef2b7fe1e68975f8aef9aed8b3fe22da18cc7d53eda |
| rc.2 AXIOMATIC_CALCULUS.md | 37,849 | cbe2edb928d3e75e23446f6d525baea664966e8d5920e6fa389cbaa4af8f1f8d |
| rc.2 REFERENCE_FRAME_METHOD.md | 55,118 | 6e9148d7c8eff847abf172315b0e282e4477f3d40866b28f7fef21c41cb067e7 |
| rc.2 SPEC_METHOD.md | 157,952 | 7f12d32ef4e5720d5d59ee5ace50de6c1a12cc56afa53dd67a8ee4c54f8fb8a4 |
| rc.2 DESIGN_MODULE_METHOD.md | 121,432 | 5cb69556bba1171ec347cac96811c50071f0648a367103aa215070239b93785e |
| rc.2 WORLD_MODEL_METHOD.md | 51,197 | 123ddcd05130aa95508c9fcfa194bf083caae3657baedaba0ce9214009453762 |

The rc.2 install is `/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2/standards/`
(read only). The projection's `resolved_sources` names the same sha256 for
FOUNDATIONS, CALCULUS, EVALUATION and rc.2 AXIOMATIC_CALCULUS.md, so the
standing basis this actor read is the basis the projection was materialised
from. The projection carries program_sha256 743e07fa…, map_sha256 8c48e04c…,
projection_sha256 34c63a10…. CASE.md states the subject commit as `cc1d29d`
and the expectations input commit as `80b46944f1c1`; this actor was told not
to read git history and did not verify either commit.

Grant. Operations permitted: read the named standing basis; read the case
directory; measure and read rc.2 fragments by heading through fragment.py
(`--size` before `--text`) or `wc -c` for whole files; run `date -u`; create
the run directory and write exactly one file, this RETURN.md. Territory that
may change: `qualification/runs/T-01/20261011-A-claude-fresh-001/` only.
Reserved to others: assessment (EVALUATION §3–4), disposition of any finding
or residual, any edit outside the run directory, any read of other files
under `stdo_3/build_tenants/claude/` or elsewhere in the repository, any git
state change.

Re-entry conditions. A route whose slug does not resolve, or whose pair
cannot fit the cap, re-enters at FOUNDATIONS §3 (the owning relation of the
route) or at CASE.md (the cap); a conflict between the tenant's standing
vocabulary and its own use of it re-enters at FOUNDATIONS §1/§6; a change in
the rc.2 install identity invalidates every route result.

Allowance and measurement. Per-step subject context cap 160,000 bytes,
counting the tenant paragraph plus the rc.2 fragment transferred in one step,
measured before reading with `fragment.py --size` (or `wc -c` for a whole
file). The method documents, the projection, CASE.md and fragment.py are the
standing basis: reported once, not charged. The actor's own output is not
counted. Total-work budget: one activation, 60 minutes wall.

Decision contract for "consistent" (declared before judging; P1 requires a
semantic decision to run under an exact contract). A tenant characterisation
of a clause is consistent with the rc.2 text at the cited heading when both
hold: (a) the subject matter of the rc.2 section is the subject matter the
tenant attributes to it by placing it under that commitment with the
standing "conserves"; and (b) nothing the tenant states in the commitment
paragraph contradicts the rc.2 section. Where the paragraph restates clause
content, the restatement must not invert or narrow the rc.2 meaning in a way
that would change a consuming decision. Omissions in a restatement that are
covered by conservation-by-reference are recorded as findings, not as
falsifiers. A route is satisfied only when the slug resolves and (a) and (b)
hold; falsified when a contradiction is shown; indeterminate when the texts
cannot decide (a) or (b); out_of_frame when the pair cannot fit the cap or
the judgment needs an undeclared relation; invalid_basis when the member or
slug cannot be resolved as a subject.

## 2. Closure and projection boundary (CALCULUS §2)

Order of operations, as performed: cap declared (160,000) → closure computed
→ every member and fragment measured → fit tested per step → reads
performed. No read was performed before its measurement; no step's reads
approached the cap.

Seed set Z: FOUNDATIONS §3 and the task predicate. Relation family R: the
`stdo://` links in §3 (route relations) and the heading-slug relation of
fragment.py (Axiom Indexer slug rule at the pinned subject). Material closure:
the §3 section (5,443 bytes by fragment.py `--slug 3-commitments --size`)
plus the 22 cited rc.2 sections. The closure is finite and unique: the links
were extracted mechanically by regular expression over §3 (lines 71–148 of
FOUNDATIONS.md) and the slugs resolved one-to-one.

Boundary seams recorded:

- excluded: six clause labels named in §3 without an `stdo://` link in §3
  (UP-013, AC-002, AC-014, AC-009, UP-001, UP-004; their links are in §1/§2).
  Outside the task's literal route rule; not checked.
- external: the rc.2 install is an external immutable subject; the five
  members cited by §3 total 423,548 bytes; all top-level rc.2 members total
  848,544 bytes.
- unresolved: none at the route level.
- translated: fragment.py's slug rule is the translation from heading text to
  slug; the slug in each link was resolved by that rule only.
- invalidation-sensitive: every route result binds the member sha256 above;
  a changed member invalidates its routes.

Route list and measured coupled pairs (tenant paragraph bytes + rc.2 section
bytes, measured before reading):

| Route | Commitment | Para bytes | Member | Slug | Fragment bytes | Pair bytes | Fit (≤160,000) |
|---|---|---|---|---|---|---|---|
| R01 | P1 | 867 | AXIOMATIC_CALCULUS.md | ac-017-interpretation-fidelity | 378 | 1,245 | fits |
| R02 | P1 | 867 | AXIOMATIC_CALCULUS.md | ac-018-structural-and-semantic-separation | 325 | 1,192 | fits |
| R03 | P1 | 867 | AXIOMATIC_CALCULUS.md | ac-019-valid-model | 801 | 1,668 | fits |
| R04 | P1 | 867 | REFERENCE_FRAME_METHOD.md | rf-008-overlap-without-identity-collapse | 290 | 1,157 | fits |
| R05 | P2 | 482 | SPEC_METHOD.md | proportional-method-and-delivery-stdo-up-014 | 4,219 | 4,701 | fits |
| R06 | P2 | 482 | DESIGN_MODULE_METHOD.md | boundary-and-governance-cost-stdo-up-005 | 653 | 1,135 | fits |
| R07 | P3 | 564 | SPEC_METHOD.md | recursive-product-taxonomy | 2,925 | 3,489 | fits |
| R08 | P3 | 564 | WORLD_MODEL_METHOD.md | entity-cut-construction-law | 3,486 | 4,050 | fits |
| R09 | P4a | 464 | AXIOMATIC_CALCULUS.md | ac-016-typed-composition | 557 | 1,021 | fits |
| R10 | P4a | 464 | REFERENCE_FRAME_METHOD.md | rf-010-composition-on-demand | 430 | 894 | fits |
| R11 | P4b | 936 | AXIOMATIC_CALCULUS.md | ac-013-transformation | 6,411 | 7,347 | fits |
| R12 | P4b | 936 | AXIOMATIC_CALCULUS.md | ac-005-authority-conservation | 324 | 1,260 | fits |
| R13 | P4b | 936 | DESIGN_MODULE_METHOD.md | bounded-frame-conservation-stdo-up-017 | 2,942 | 3,878 | fits |
| R14 | P4b | 936 | SPEC_METHOD.md | complete-enclosing-relation-admission-stdo-up-021 | 5,914 | 6,850 | fits |
| R15 | P5 | 690 | REFERENCE_FRAME_METHOD.md | rf-012-closed-results | 624 | 1,314 | fits |
| R16 | P5 | 690 | REFERENCE_FRAME_METHOD.md | rf-014-capability-fit | 318 | 1,008 | fits |
| R17 | P5 | 690 | AXIOMATIC_CALCULUS.md | ac-007-constraint-and-refusal | 275 | 965 | fits |
| R18 | P5 | 690 | DESIGN_MODULE_METHOD.md | 8-totality-rule | 660 | 1,350 | fits |
| R19 | P6 | 847 | SPEC_METHOD.md | semantic-evidence-and-projection-separation-stdo-up-008 | 728 | 1,575 | fits |
| R20 | P6 | 847 | SPEC_METHOD.md | assurance-boundary-congruence-and-method-qualification-stdo-up-022 | 5,343 | 6,190 | fits |
| R21 | P6 | 847 | REFERENCE_FRAME_METHOD.md | rf-006-authority-conservation | 297 | 1,144 | fits |
| R22 | P6 | 847 | REFERENCE_FRAME_METHOD.md | rf-007-semantic-evidence-and-verdict-separation | 437 | 1,284 | fits |

P0 has no `stdo://` link in §3 and yields no route.

Fit result at section level: the §3 section plus all 22 cited fragments
measures 5,443 + 38,337 = 43,780 bytes, which fits the Run A cap in one
step. Whole-member reading would not fit: the five cited members total
423,548 bytes against a 160,000 cap, so the fit depends on projection by
heading.

Refinement chosen: the section-level contract was refined into 22 per-route
steps, one coupled pair each, with the composite computed as a declared
conjunction over independent closed results (FOUNDATIONS §4; RF-010). Reason:
the task deliverable is one core result per route with per-step byte
accounting, and each route's predicate is independent of the others. No
compression was applied; no material was omitted; no actor change or
sequencing beyond per-route steps was needed. CASE.md names this shape as
the expected one for Run A; see residual RS-5 on who authorises the
refinement.

## 3. Per-route results

Each route: slug found (fragment.py `--size` returned exit 0 at the cited
member and slug; `--text` then returned the section beginning at that
heading), the rc.2 heading as read, and the consistency judgment under the
declared contract. "Finding" marks something a later actor may act on that
does not falsify the route.

R01 — satisfied. Slug found. Heading read: "### AC-017 Interpretation
Fidelity" (378 bytes). rc.2: admitted model records map to exact subject
provenance or are declared model-local; every evaluated subject declaration
has a retained/omitted/residual/inapplicable/refused disposition;
interpretation cannot treat absence as immateriality without recorded basis
and authority. Tenant P1: subject, representation and interpretation are
distinct; meaning holds within a declared context through a declared
contract; structural success never establishes fidelity. (a) holds: AC-017
is an interpretation-fidelity clause. (b) holds: no contradiction. P1 does
not restate AC-017's disposition set; conserved by reference.

R02 — satisfied. Slug found. Heading: "### AC-018 Structural And Semantic
Separation" (325 bytes). rc.2: structural conformance decides closed syntax,
types, identities, references, bases and mechanically decidable predicates;
semantic fidelity decides meaning and materiality; structural success is
evidence for semantic review, not a substitute. Tenant P1: "algorithmic"
means explicit and structurally checkable; structural success never
establishes fidelity. Direct match.

R03 — satisfied. Slug found. Heading: "### AC-019 Valid Model" (801 bytes).
rc.2: six validity conditions for a model under a signature; a checker may
decide the structural subset; no generic checker may claim the semantic or
authority subset unless the model supplies an exact lawful decision
contract. Tenant P1: a semantic decision is lawful only under an exact
decision contract. Direct match on the cited point; the six validity
conditions are not restated and are conserved by reference.

R04 — satisfied. Slug found. Heading: "### RF-008 Overlap Without Identity
Collapse" (290 bytes). rc.2: shared material does not establish identical
meaning, basis, authority or result; every cross-frame equality or
translation is declared where needed. Tenant P1: two contracts give one
representation two meanings; meaning holds through a declared contract;
ontology row "equal representations do not establish equal meaning".
Consistent.

R05 — satisfied, with finding. Slug found. Heading: "## Proportional Method
And Delivery (`STDO-UP-014`)" (4,219 bytes). rc.2: proportionality is
ambiguity removed versus effective reasoning complexity introduced; each
constraint identifies the ambiguity it removes; the method does not
prescribe internal procedure where variation cannot affect a governed
property; delivery priority applies the same relation to the Product
outcome. Tenant P2: a selected outcome defines adequacy; interfaces inherit
material obligations from the transformation they serve; an obligation with
no route to the outcome is unjustified. (a) holds: UP-014 is a
purpose/proportionality clause. (b) holds: no contradiction. Finding: P2's
criterion ("route to the outcome") is stated at a different altitude from
UP-014's criterion ("contraction of the admissible interpretation space
justifies the reasoning complexity introduced"); P2 does not restate the
UP-014 relation. Smallest correction if an assessor wants the restatement
tighter: add "proportionally to the ambiguity it removes" to P2's obligation
sentence, or leave as conserved by reference.

R06 — satisfied, with the same finding as R05. Slug found. Heading: "###
Boundary And Governance Cost (`STDO-UP-005`)" (653 bytes). rc.2: review
cuts, realization units, runtime modules and work items are distinct
boundaries not forced one-to-one; contraction fails when it increases
authority centres, truth surfaces, acceptance boundaries, cycles, manual
reconciliation or review burden; evidence proportional to semantic change
and risk. Tenant P2 as above. UP-005 is a cost/proportionality clause under
Purpose; no contradiction; not restated.

R07 — satisfied. Slug found. Heading: "## Recursive Product Taxonomy" (2,925
bytes). rc.2: Substrate, Development Product, Source Project, Release Cut,
Product, Install, Artifact, Product Definition, each with a URN; rules
against collapsing the roles; the Development Product role "creates no new
Product identity and transfers no meaning or authority". Tenant P3: an
object's identity is declared (authority, kind, value) and survives
admissible change; current state, historical observation and representation
identity stay separate. (a) holds: the taxonomy is an identity-kind
discipline. (b) holds. P3 does not restate the taxonomy; conserved by
reference.

R08 — satisfied. Slug found. Heading: "## Entity Cut Construction Law"
(3,486 bytes, including its Admissibility, Discrimination and Publication
subsections). rc.2: entities are recovered not invented; a cut is admissible
when identity, boundary, authority, state, evidence, treatment, covariance
and ambiguity are explicit and discriminated from plausible alternatives at
proportional evidence altitude; boundary is interventional, a field-set
boundary is a weaker claim; "coat stripping" shows identity survives varied
context. Tenant P3: a boundary is a claim with a proof obligation; identity
survives admissible change. Direct match on both points.

R09 — satisfied, with finding. Slug found. Heading: "### AC-016 Typed
Composition" (557 bytes). rc.2: two traversals compose only when the first
result type and judgment satisfy the second's exact domain and
preconditions; composition retains both identities, intermediate results,
judgments, evidence, authority, provenance and stop states; it cannot
flatten probabilistic proposal, deterministic evaluation and human decision
into one operation; no universal F_P → F_D → F_H sequence. Tenant P4a
restates the composition condition and the retained list with "steps" for
"traversals". Finding: P4a's retained list omits "provenance" and does not
restate the no-flattening clause; CALCULUS §1 lists provenance among
step-produced facts and FOUNDATIONS §4 says the composite carries both
steps' step-produced facts, so the omission does not change a consuming
decision. Smallest correction: add "provenance" to the P4a list.

R10 — satisfied. Slug found. Heading: "### RF-010 Composition On Demand"
(430 bytes). rc.2: using several frames does not require composing their
manifolds; composition law is required only when the evaluation combines
internal variables, transports values across frames, or treats operations as
one execution relation; independent evaluations may return closed results to
one declared conjunction or decision rule. Tenant P4a cites it as conserved;
FOUNDATIONS §4 restates it faithfully. Consistent.

R11 — satisfied. Slug found. Heading: "### AC-013 Transformation" (6,411
bytes). rc.2: the transformation record (preserved, introduced, removed,
external_* deltas, external_resolution_witnesses, residuals, evidence,
provenance, stop_states, invalidation, re_entry), the closed local-record
delta equations, the external-resolution witness law, residual carry-over
unless an exact authorised disposition is in the evidence, and the
application signature returning successor, hold, gap or refusal. Tenant P4b:
judgments, residuals, observations and authority decisions the outer
contract needs are recorded by the producing step; typed instance
"transition"; FOUNDATIONS §4 conservation accounting names preserved,
introduced, removed, external resolution witnesses and residuals (AC-013).
(a) holds: AC-013 is a conservation record for transformations. (b) holds.
The delta equations and witness law are conserved by reference, not
restated. See residual RS-3 on the dual standing "conserves" plus
"reframed".

R12 — satisfied, with finding. Slug found. Heading: "### AC-005 Authority
Conservation" (324 bytes). rc.2: objects, relations, constraints, latitude,
residuals, traversals, transformations, projections and judgments retain
their declared authority; copying, interpreting, encoding, evaluating or
transporting a record does not transfer authority. Tenant P4b: typed
instance "authority" of the one conservation obligation; ontology row
"Authority: never minted from capability, label or reachability". (a) holds.
(b) holds. Finding: P4b's one-obligation wording ("recorded by the step that
produced them") is a recording obligation; AC-005's content is non-transfer
of authority under copying and transport, which the reframed wording does
not cover. The clause is also marked conserved, so its content governs
unchanged. See RS-3.

R13 — satisfied. Slug found. Heading: "### Bounded Frame Conservation
(`STDO-UP-017`)" (2,942 bytes). rc.2: each material design frame identifies
its governing frames, affected relation set, inherited invariants, seams and
subordinate frames; every seam includes its far side or states why it cannot
participate; a bounded local action conserves governing truth and re-enters
at a changed governing relation; plus the discovered-functionality
derivation order. Tenant P4b typed instance "frame"; CALCULUS §1 intake
names the affected relation set, its invariants and the re-entry conditions
at an owning relation. (a) holds. (b) holds. Observation: the section at
this heading also carries the Ontology derivation-order block, which is
design-profile material; FOUNDATIONS §6 says profile law stays in PROFILES.
No contradiction with the rc.2 text.

R14 — satisfied. Slug found. Heading: "## Complete Enclosing-Relation
Admission (`STDO-UP-021`)" (5,914 bytes, including Standing Structural
Qualification). rc.2: an admission owner derives the complete enclosing
relation; an owner may consume established facts when their exact subject,
basis, scope, provenance and validity remain applicable and their production
and invalidation are recoverable; a boundary alone requires no repeated
derivation; admission is one semantic commit. Tenant P4b: "sources a later
step can re-acquire are governed by sufficiency, not conservation". Direct
match on the consumption-of-established-facts point; typed instances
"transition" and "successor claim".

R15 — satisfied. Slug found. Heading: "### RF-012 Closed Results" (624
bytes). rc.2: the five-member baseline algebra with definitions identical in
substance to CALCULUS §3 (satisfied, falsified, indeterminate, out_of_frame,
invalid_basis); a compatible extension may refine it while preserving
explicit indeterminate, out-of-frame and invalid-basis pressure. Tenant P5:
the result algebra carries indeterminate, out_of_frame and invalid_basis as
first-class outcomes. Direct match. See RS-2: P5 says "conserves" while
CALCULUS §3 says it "supersedes" RF-012 and AC-007; that is a tenant-internal
standing conflict, not an inconsistency with the rc.2 text.

R16 — satisfied, with finding. Slug found. Heading: "### RF-014 Capability
Fit" (318 bytes). rc.2: when the material manifold exceeds an actor's
envelope, human authority may select another actor, refine the frame,
sequence activations, or provide a lawful compression; the actor may not
silently omit material relations to fit context. Tenant P5: a step cannot
report success on a condition outside its context; its control model names
the next move. (a) holds. (b) holds. Finding: RF-014 vests the choice among
the options in human authority; neither P5 nor CALCULUS §2 restates who
selects, and CALCULUS §2 adds "return out_of_frame" to the option list. The
projection's residual `lawful-compression-judge-is-unnamed` records the
adjacent gap. See RS-5 for the consequence for this run.

R17 — satisfied. Slug found. Heading: "### AC-007 Constraint And Refusal"
(275 bytes). rc.2: each constraint names its subject, predicate, judgment
kind, latitude and refusal; a failed, missing, indeterminate, out-of-scope
or invalid-basis result follows the declared result algebra rather than
being coerced to success. Tenant P5 and CALCULUS §3 "nothing is coerced to
success; a missing, failed or out-of-scope result returns its member".
Direct match. Observation: CALCULUS §3 says RF-012 and AC-007 "name the same
five outcomes"; AC-007 names five result conditions (failed, missing,
indeterminate, out-of-scope, invalid-basis) that are not literally the five
members. That sentence is outside FOUNDATIONS §3 and outside this task's
predicate.

R18 — satisfied, with observation. Slug found. Heading: "## 8. Totality
Rule" (660 bytes). rc.2: semantic functions should be total or near-total;
prefer closed outcome carriers, explicit validation stages, explicit
unsupported/rejected outcomes; avoid partial functions with hidden
preconditions, fallback chains, defaults reconstructing truth. Tenant P5:
the result algebra carries non-success as first-class outcomes. (a) holds:
totality of outcomes. (b) holds. Observation: the rc.2 rule is a
design-profile preference ("should", "prefer") while P5 is stated as law;
"conserves" is accurate for the rc.2 rule itself and P5 adds a stronger
derived commitment. FOUNDATIONS §6 says nothing from DESIGN_MODULE is
imported into tier 1, yet P5 (tier 1) cites this DESIGN_MODULE section; not
a contradiction with the rc.2 text.

R19 — satisfied. Slug found. Heading: "### Semantic, Evidence, And
Projection Separation (`STDO-UP-008`)" (728 bytes). rc.2: semantic basis,
evidence basis and state projection are distinct; evidence change may
invalidate a verdict without changing law; projection change may invalidate
a view; semantic change requires re-entry and invalidates downstream
acceptance. Tenant P6: distinct standings; evidence supports a claim on a
basis. EVALUATION §2 restates UP-008 faithfully. Consistent.

R20 — satisfied. Slug found. Heading: "### Assurance-Boundary Congruence And
Method Qualification (`STDO-UP-022`)" (5,343 bytes). rc.2: assurance binds
the exact claimed subject; mechanical enforcement needs a predicate and a
reachable witness; a claim's quantifier, population and scope cannot exceed
its evidence; later counterevidence invalidates dependent verdicts; method
qualification by fresh constructor and independently authorised evaluator;
post-exposure revision is an intervention. Tenant P6: evidence supports a
claim on a basis; authority permits or disposes; a bounded actor can still
take a green label as acceptance. EVALUATION §1 and §3 restate the cited
points. Consistent.

R21 — satisfied. Slug found. Heading: "### RF-006 Authority Conservation"
(297 bytes). rc.2: a frame carries and applies admitted authority; it does
not mint, widen, transfer or reconstruct authority from actor identity,
capability, evidence shape, reachability or frame selection. Tenant P6:
authority permits or disposes within scope; neither evidence nor authority
is minted by the other; ontology "never minted from capability, label or
reachability". Direct match.

R22 — satisfied. Slug found. Heading: "### RF-007 Semantic, Evidence, And
Verdict Separation" (437 bytes). rc.2: semantic law defines meaning;
evidence supplies observations; the evaluator applies the declared relation;
decision authority disposes; roles stay distinguishable even when one actor
performs several. Tenant P6 and EVALUATION §2 restate this. Direct match.

## 4. Composite result

Composite for FOUNDATIONS §3 rc.2 routes: satisfied.

Computation (FOUNDATIONS §4 conservation accounting; CASE.md E2): required
obligation set R = the 22 routes; admitted coverage C = the 22 route results
above, each produced on its own measured pair; uncovered coverage R minus C
= empty. Known failures = union over routes of falsified, indeterminate,
out_of_frame and invalid_basis results = empty. The composite takes the
weakest route result, which is satisfied, and may project success only
because no failure and no uncovered route survive the join. Findings on
R05, R06, R09, R12, R16 and the observations on R13, R17, R18 are recorded
as residuals below; under the declared contract none is a counterexample to
its route predicate, so none changes the composite. An assessor applying a
stricter contract (for example, requiring every restatement to be complete)
would need to re-judge R09 and R12 first.

## 5. Bytes transferred, standing basis, wall time

Standing basis, reported once, not charged to the per-step cap:
FOUNDATIONS.md 14,463 + CALCULUS.md 13,470 + EVALUATION.md 8,042 +
projection JSON 85,546 = 121,521 bytes by file size. Actually transferred
from those files: 14,463 + 6,328 (CALCULUS lines 1–108) + 4,403 (EVALUATION
lines 1–80) + 85,546 (projection, read in two passes: a 44,383-character
truncated read, then a pretty-printed dump of the remaining top-level keys)
= 110,740 bytes. Case inputs, also standing: CASE.md 6,800 + fragment.py
2,472 = 9,272 bytes.

Per-step subject bytes charged against the 160,000 cap:

| Step | Subject material | Bytes |
|---|---|---|
| S0 | rc.2 README.md, first 40 lines, read during orientation of the install (not a cited member; charged conservatively) | 2,330 |
| R01 | P1 paragraph + ac-017-interpretation-fidelity | 1,245 |
| R02 | P1 paragraph + ac-018-structural-and-semantic-separation | 1,192 |
| R03 | P1 paragraph + ac-019-valid-model | 1,668 |
| R04 | P1 paragraph + rf-008-overlap-without-identity-collapse | 1,157 |
| R05 | P2 paragraph + proportional-method-and-delivery-stdo-up-014 | 4,701 |
| R06 | P2 paragraph + boundary-and-governance-cost-stdo-up-005 | 1,135 |
| R07 | P3 paragraph + recursive-product-taxonomy | 3,489 |
| R08 | P3 paragraph + entity-cut-construction-law | 4,050 |
| R09 | P4a paragraph + ac-016-typed-composition | 1,021 |
| R10 | P4a paragraph + rf-010-composition-on-demand | 894 |
| R11 | P4b paragraph + ac-013-transformation | 7,347 |
| R12 | P4b paragraph + ac-005-authority-conservation | 1,260 |
| R13 | P4b paragraph + bounded-frame-conservation-stdo-up-017 | 3,878 |
| R14 | P4b paragraph + complete-enclosing-relation-admission-stdo-up-021 | 6,850 |
| R15 | P5 paragraph + rf-012-closed-results | 1,314 |
| R16 | P5 paragraph + rf-014-capability-fit | 1,008 |
| R17 | P5 paragraph + ac-007-constraint-and-refusal | 965 |
| R18 | P5 paragraph + 8-totality-rule | 1,350 |
| R19 | P6 paragraph + semantic-evidence-and-projection-separation-stdo-up-008 | 1,575 |
| R20 | P6 paragraph + assurance-boundary-congruence-and-method-qualification-stdo-up-022 | 6,190 |
| R21 | P6 paragraph + rf-006-authority-conservation | 1,144 |
| R22 | P6 paragraph + rf-007-semantic-evidence-and-verdict-separation | 1,284 |

Route steps total 54,717 bytes (rc.2 fragments 38,337 + tenant paragraphs
16,380, each paragraph charged once per route it anchors). Total transferred
and charged across all steps including S0: 57,047 bytes. Largest single
step: R11 at 7,347 bytes (4.6% of the cap). No step exceeded or approached
the cap; no read was refused for size. Measurement outputs (sizes, slug
resolution codes, sha256 values, directory listings) are metadata and were
not charged.

Delegated actors: none. All reads were performed by this one context, so the
count above is the complete transferred-context count for the run.

Wall time: start 2026-10-11T11:15:32Z; end 2026-10-11T11:24:55Z; elapsed
9 min 23 s (both by `date -u`; the end stamp precedes the final edit of
this file by under a minute). Budget 60 minutes.

## 6. Stop state, residuals, resumption

Stop state: satisfied (construction availability: candidate_ready; the
candidate is this file, a self-reviewed construction output awaiting
independent assessment).

Residuals, each a step-produced fact not re-acquirable from sources:

- RS-1 (observation, CASE.md). CASE.md states "The cited members together
  exceed 600,000 bytes". Measured: the five members cited by §3 total
  423,548 bytes; all sixteen top-level rc.2 members total 848,544 bytes.
  The discriminator's premise still holds for Run A (423,548 exceeds the
  160,000 cap), but the figure in the case does not match the §3 member
  set. Re-entry: CASE.md, owner of the case design.
- RS-2 (ambiguity, tenant-internal). FOUNDATIONS §3 P5 says it "conserves"
  RF-012 and AC-007; CALCULUS §3 says its single statement "supersedes" both;
  FOUNDATIONS §6 lists them as "conserved by reference" and "restated".
  FOUNDATIONS §1 gives a clause exactly one standing. Not an inconsistency
  with the rc.2 text; not resolved here. Re-entry: FOUNDATIONS §1/§6.
- RS-3 (ambiguity, tenant-internal). P4b marks AC-013, AC-005, UP-017,
  UP-021 (and the unlinked AC-009) as "conserves" and in the same sentence
  says the nine rc.2 conservation statements "are reframed as one
  obligation with typed instances". Conserved and reframed are distinct
  standings under §1. The reframed one-obligation wording is narrower than
  AC-005's content (R12 finding). Re-entry: FOUNDATIONS §3 P4b.
- RS-4 (omission, restatement). P4a's retained list omits "provenance"
  relative to AC-016 (R09 finding). Smallest correction: add the word.
- RS-5 (authority). RF-014 vests selection among refine/sequence/another
  actor/compression in human authority; CALCULUS §2 lets the step select.
  This run's refinement into per-route steps rests on CASE.md's declared
  expected shape for Run A and the activating instruction, not on this
  actor's own authority. If an assessor reads RF-014 as conserved unchanged,
  the authority for the refinement should be traced to the case owner, which
  this record does by citing CASE.md "Caps and measurement", row A.
- RS-6 (scope). Six clause labels appear in §3 without an `stdo://` link in
  §3 (UP-013, AC-002, AC-014, AC-009, UP-001, UP-004); their links are in §1
  and §2. Not checked under the task's literal route rule. A later actor
  extending the route list would need six more coupled pairs; AC-002,
  AC-014, AC-009 are in AXIOMATIC_CALCULUS.md, UP-013 and UP-001 in
  SPEC_METHOD.md, UP-004 in IDENTITY_METHOD.md (11,350 bytes).
- RS-7 (decision contract). The task's "consistent" had no exact decision
  contract in the method documents; this run declared one in §1 above and
  applied it uniformly. A different contract may change R09 and R12 first.
- RS-8 (altitude). P2's obligation criterion differs in altitude from UP-014
  and UP-005 (R05/R06 findings); no contradiction found.
- RS-9 (incidental read). S0 read the first 40 lines of the rc.2 README.md
  (2,330 bytes) while listing the install; it informed no route result and is
  charged above for completeness.
- RS-10 (unverified identities). Commits `cc1d29d` and `80b46944f1c1` named
  in CASE.md were not verified; the basis is bound by the sha256 values in
  §1 instead.

What a later actor needs to resume without this conversation: this file;
the sha256 table in §1 to confirm the same standing basis and rc.2 members;
fragment.py and the slug column in §2 to re-acquire every rc.2 section by
heading; the decision contract in §1 to re-judge any route; the residual
list above with its re-entry points. No private memory of this actor is
needed: every judgment, its evidence by heading and byte count, and every
residual are recorded here. The route results are invalidated by any change
to the five rc.2 member hashes or to FOUNDATIONS.md's hash.

Wall clock end: 2026-10-11T11:24:55Z (`date -u`). Elapsed from start:
9 min 23 s.
