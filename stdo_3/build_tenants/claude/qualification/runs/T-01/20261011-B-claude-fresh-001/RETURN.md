# T-01 Run B return: 20261011-B-claude-fresh-001

Case: urn:stdo-3:claude:case:T-01, Run B (per-step subject context cap 6,000
bytes). Constructor: fresh Claude context (model id claude-fable-5-1), one
bounded activation, direct entry as constructor (CALCULUS section 1: one
capable context with sufficient intake; no coordination needed).

Wall-clock start: Sun 11 Oct 2026 11:15:41 UTC.
Wall-clock end: Sun 11 Oct 2026 11:28:04 UTC.

Sections 1 and 2 were written and saved before any rc.2 fragment was read
(E1). Sections 3 to 9 were appended after the step reads.

Summary. Existence check: 22 of 22 slugs resolve in the installed rc.2
members. Consistency check: 19 routes satisfied, 3 routes (R11, R14, R20)
out_of_frame because their coupled pair exceeds the 6,000-byte cap; no read
was performed for them. Composite for FOUNDATIONS section 3: out_of_frame.
Stop state of this activation: out_of_frame (construction availability:
re_entry_requested). Subject bytes transferred: 26,091 over 8 reading steps;
largest step 5,355. Standing basis: 130,793 bytes, reported once.

## 1. Intake (CALCULUS section 1)

Outcome served. The T-01 shared task: for every
`stdo://releases/v2.5.1-rc.2/standards/<member>#<slug>` link in FOUNDATIONS
section 3 Commitments, (1) confirm the heading slug exists in the installed
rc.2 member and (2) judge whether the tenant's one-line characterisation of
that clause is consistent with the rc.2 text at that heading; return one core
result per route and one composite result for the section, with evidence.
This serves the conformance trial named in the case (the method's own
recoverability benchmark under a context cap); it is not product work.

Affected relation set. The 22 conservation routes from FOUNDATIONS section 3
to rc.2 headings (listed in section 2). Invariants that govern it: each
route's coupled pair (tenant paragraph plus rc.2 section) is the smallest
unit that must fit together in one step (CASE.md, "Shared task"); no required
member is trimmed to fit a carrier or budget (AC-011 as restated in
FOUNDATIONS section 4; projection clause
`urn:stdo-3:claude:a-c-text:clause:projection-cannot-trim-required-member`);
silent omission to fit is never an option (CALCULUS section 2 step 3);
nothing is coerced to satisfied (CALCULUS section 3); a read that would
exceed the cap is not performed (case measurement rule).

Basis by identity (sha256 computed in this run with `shasum -a 256`):

| Input | Role | Bytes | sha256 |
|---|---|---|---|
| qualification/cases/T-01/CASE.md | case | 6,800 | 53cd9f6fea7c633d7b4337b7e245c967b643ad9649a2aff73c7e9ef3e0b6082a |
| qualification/cases/T-01/fragment.py | measurement tool | 2,472 | 02c7128913df35b614ec9ef2b7fe1e68975f8aef9aed8b3fe22da18cc7d53eda |
| standards/FOUNDATIONS.md | subject (section 3) and standing basis | 14,463 | 5f5e7ab3b820657ec5992aa3eb9c0bc7a6f937dbe9ec0f36eb75014429efed80 |
| standards/CALCULUS.md | standing basis, sections 1 to 3 | 13,470 | 879fb9dd7c8f59c866f2e9564e685dd57611bbeabd2806dc40d9b0ea5fb582ad |
| standards/EVALUATION.md | standing basis, sections 1 to 4 | 8,042 | fc063460e6834c190bcc5fe045d4a5a8f45a2ffd96a0ec2cad4fa82b677f246d |
| a_c/t1/projection-bounded-activation-materialized.json | standing basis (frame index urn:stdo-3:claude:a-c-text:frame-index:bounded-activation; projection_sha256 34c63a10...) | 85,546 | 728973230d798e051290cee41eb183aaef6b7903beffcf4db573036fccdbb990 |
| rc.2 install `/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2/standards/` | subject (cited members), read only | section 2 | section 2.1 |

The projection's `resolved_sources` carries the same sha256 for FOUNDATIONS,
CALCULUS and EVALUATION as computed here, so the projection and the three
documents are one basis. The projection also declares
`sha256:cbe2edb928d3e75e23446f6d525baea664966e8d5920e6fa389cbaa4af8f1f8d`
for rc.2 AXIOMATIC_CALCULUS.md; the installed member matches (section 2.1).
No declared hash for the other four cited members was among this actor's
inputs (the case points to a_c/t1/README.md, which this actor may not read);
their identity is by path inside the read-only rc.2 release, and their
observed hashes are recorded in section 2.1 for a later actor.

Grant. Permitted: read the inputs above; run `fragment.py` with `python3 -I`
(`--size`, `--text`) against the rc.2 install; `wc -c`, `sed -n`, `grep -o`
and `shasum` for measurement, enumeration and identity; write exactly one
file, this RETURN.md, in this run directory (created by this run). Not
permitted: any other read under `stdo_3/build_tenants/claude/` or elsewhere
in the repository; any write outside this run directory; any git command
that changes state; reading git history. Reserved to others: acceptance and
disposition of this return (assessor under EVALUATION section 4; Jim);
selection of another actor for the three unread routes (RF-014 reserves this
to human authority, see residual R-3); rulings on the residuals in section 7.

Re-entry conditions. Re-enter at the owning relation if: a cited member is
absent from the install (invalid_basis for its routes); a slug is unresolved
(falsified on the existence check; the consistency check then has no
subject); the measured coupled pair exceeds the cap (out_of_frame for that
route, no read, escalation named); the rc.2 text at a heading is a
cross-reference whose consuming decision needs a further heading not in the
closure (out_of_frame or indeterminate, with the missing relation named).
Each condition was tested; only the third occurred (R11, R14, R20).

Allowance (CALCULUS section 1, last bullet). Cap: 6,000 bytes of subject
material per step. Measurement source: `fragment.py --size` for a heading
section (reads nothing into context), `wc -c` for whole files, `sed -n |
wc -c` for a tenant paragraph line range. Charged: the tenant paragraph and
each rc.2 fragment actually printed into context in a step. Not charged: the
standing basis (reported once), the actor's own output, measurement output
(sizes, hashes, directory listing, the 22-link enumeration). Total-work
budget: 60 minutes wall.

Standing basis size, reported once: 130,793 bytes (CASE.md 6,800 +
fragment.py 2,472 + FOUNDATIONS 14,463 + CALCULUS 13,470 + EVALUATION 8,042 +
projection 85,546). Disclosures: CALCULUS and EVALUATION were read whole, so
CALCULUS sections 4 to 8 and EVALUATION sections 5 to 8 entered context; they
are not used as basis in this return (residual R-5). The projection was
delivered in two pieces (the Read tool truncated at 44,383 characters; the
remaining top-level members were printed with a JSON dump), so the whole
file was received.

## 2. Closure and projection boundary (CALCULUS section 2)

Seed set Z: FOUNDATIONS section 3 (slug `3-commitments`, 5,443 bytes); the
22 `stdo://releases/v2.5.1-rc.2/standards/...#...` links it contains; the
two-part task predicate per route.

Relation family R: the conservation route from a tenant commitment paragraph
to one rc.2 heading section. The closure of Z under R is the 22 coupled
pairs. It is finite and unique on the exact basis: the links were enumerated
mechanically (`grep -o` over FOUNDATIONS lines 71 to 148; 22 matches, listed
in the route table) and each resolved to exactly one heading section under
the slug rule in fragment.py (`--size` exit 0 for all 22).

Boundary. Excluded: clauses section 3 names without a link in section 3
(UP-013 in P2; AC-002 and AC-014 in P3; AC-009 in P4b; UP-001 and UP-004 in
P6; their links are in FOUNDATIONS section 2, and the task scopes links in
section 3 only); P0, which has no rc.2 link. External: the slug rule
(fragment.py states it as "the Axiom Indexer rule at the pinned subject");
the rc.2 install's provenance. Unresolved: no declared hash for four of the
five cited members (section 1). Translated: none; the rc.2 text is read
verbatim. Invalidation-sensitive: a change to FOUNDATIONS section 3, to
fragment.py's slug rule, or to the rc.2 install invalidates every route
result.

Cited rc.2 members (`wc -c`):

| Member | Bytes |
|---|---|
| AXIOMATIC_CALCULUS.md | 37,849 |
| REFERENCE_FRAME_METHOD.md | 55,118 |
| SPEC_METHOD.md | 157,952 |
| DESIGN_MODULE_METHOD.md | 121,432 |
| WORLD_MODEL_METHOD.md | 51,197 |
| total | 423,548 |

The case says the cited members together exceed 600,000 bytes; the five
members cited from section 3 total 423,548 (residual R-6). Either way the
full basis exceeds the 6,000 cap, and the whole-section context (5,443 +
423,548) was never a candidate.

Tenant paragraph sizes (FOUNDATIONS line ranges, `sed -n | wc -c`):

| Commitment | Lines | Bytes |
|---|---|---|
| P0 | 73 to 80 | 559 (no rc.2 link in section 3; no route) |
| P1 | 82 to 91 | 868 |
| P2 | 93 to 98 | 483 |
| P3 | 100 to 106 | 565 |
| P4a | 108 to 113 | 465 |
| P4b | 115 to 126 | 937 |
| P5 | 128 to 136 | 691 |
| P6 | 138 to 147 | 848 |

Route list, coupled-pair measurement and fit (all sizes measured with
`fragment.py --size` before any read; every slug resolved, exit 0):

| Route | Commitment | Member#slug | Fragment bytes | Pair bytes | Fit (cap 6,000) |
|---|---|---|---|---|---|
| R01 | P1 | AXIOMATIC_CALCULUS.md#ac-017-interpretation-fidelity | 378 | 1,246 | fits |
| R02 | P1 | AXIOMATIC_CALCULUS.md#ac-018-structural-and-semantic-separation | 325 | 1,193 | fits |
| R03 | P1 | AXIOMATIC_CALCULUS.md#ac-019-valid-model | 801 | 1,669 | fits |
| R04 | P1 | REFERENCE_FRAME_METHOD.md#rf-008-overlap-without-identity-collapse | 290 | 1,158 | fits |
| R05 | P2 | SPEC_METHOD.md#proportional-method-and-delivery-stdo-up-014 | 4,219 | 4,702 | fits |
| R06 | P2 | DESIGN_MODULE_METHOD.md#boundary-and-governance-cost-stdo-up-005 | 653 | 1,136 | fits |
| R07 | P3 | SPEC_METHOD.md#recursive-product-taxonomy | 2,925 | 3,490 | fits |
| R08 | P3 | WORLD_MODEL_METHOD.md#entity-cut-construction-law | 3,486 | 4,051 | fits |
| R09 | P4a | AXIOMATIC_CALCULUS.md#ac-016-typed-composition | 557 | 1,022 | fits |
| R10 | P4a | REFERENCE_FRAME_METHOD.md#rf-010-composition-on-demand | 430 | 895 | fits |
| R11 | P4b | AXIOMATIC_CALCULUS.md#ac-013-transformation | 6,411 | 7,348 | does not fit (fragment alone exceeds cap) |
| R12 | P4b | AXIOMATIC_CALCULUS.md#ac-005-authority-conservation | 324 | 1,261 | fits |
| R13 | P4b | DESIGN_MODULE_METHOD.md#bounded-frame-conservation-stdo-up-017 | 2,942 | 3,879 | fits |
| R14 | P4b | SPEC_METHOD.md#complete-enclosing-relation-admission-stdo-up-021 | 5,914 | 6,851 | does not fit (pair exceeds cap by 851) |
| R15 | P5 | REFERENCE_FRAME_METHOD.md#rf-012-closed-results | 624 | 1,315 | fits |
| R16 | P5 | REFERENCE_FRAME_METHOD.md#rf-014-capability-fit | 318 | 1,009 | fits |
| R17 | P5 | AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal | 275 | 966 | fits |
| R18 | P5 | DESIGN_MODULE_METHOD.md#8-totality-rule | 660 | 1,351 | fits |
| R19 | P6 | SPEC_METHOD.md#semantic-evidence-and-projection-separation-stdo-up-008 | 728 | 1,576 | fits |
| R20 | P6 | SPEC_METHOD.md#assurance-boundary-congruence-and-method-qualification-stdo-up-022 | 5,343 | 6,191 | does not fit (pair exceeds cap by 191) |
| R21 | P6 | REFERENCE_FRAME_METHOD.md#rf-006-authority-conservation | 297 | 1,145 | fits |
| R22 | P6 | REFERENCE_FRAME_METHOD.md#rf-007-semantic-evidence-and-verdict-separation | 437 | 1,285 | fits |

Fit outcome, recorded before any read: 19 coupled pairs fit; 3 (R11, R14,
R20) do not. For the three, the CALCULUS section 2 step 3 options were
considered in order: refine (not possible: the coupled pair is already the
smallest unit); sequence activations (does not reduce the pair); select
another actor whose envelope fits (the Run A envelope of 160,000 bytes fits
all three; recorded as the escalation, for human authority to select);
lawful compression (declined: the consistency judgment needs the whole
clause text, and trimming a required member to fit is forbidden); return
out_of_frame (chosen for this run, with the escalation named). No read was
performed for R11, R14 or R20.

Refinement chosen (CALCULUS section 2 step 3, first option). The
section-level contract is refined into per-commitment reading steps, each
holding one tenant paragraph plus every fitting fragment it cites, with P3
split in two because its paragraph plus both fragments (6,976) exceeds the
cap; plus three no-read steps returning out_of_frame. Every reading step's
measured total is below 6,000 and was enforced by a guard in the step script
(appendix A) that measures first and refuses to print anything when the
total exceeds the cap.

| Step | Content | Measured bytes |
|---|---|---|
| S1 | P1 paragraph + R01, R02, R03, R04 | 868 + 378 + 325 + 801 + 290 = 2,662 |
| S2 | P2 paragraph + R05, R06 | 483 + 4,219 + 653 = 5,355 |
| S3 | P3 paragraph + R07 | 565 + 2,925 = 3,490 |
| S4 | P3 paragraph + R08 | 565 + 3,486 = 4,051 |
| S5 | P4a paragraph + R09, R10 | 465 + 557 + 430 = 1,452 |
| S6 | P4b paragraph + R12, R13 | 937 + 324 + 2,942 = 4,203 |
| S7 | P5 paragraph + R15, R16, R17, R18 | 691 + 624 + 318 + 275 + 660 = 2,568 |
| S8 | P6 paragraph + R19, R21, R22 | 848 + 728 + 297 + 437 = 2,310 |
| S9 | R11: no read | 0 transferred; pair measured 7,348 |
| S10 | R14: no read | 0 transferred; pair measured 6,851 |
| S11 | R20: no read | 0 transferred; pair measured 6,191 |

Planned and actual total transfer: 26,091 bytes. Steps S1 to S8 are
independent in data; they were activated one per turn, in order, so that
each turn's transfer is one step's transfer (residual R-10).

Composite rule, declared in advance (FOUNDATIONS section 4; CASE E2): the
section-level predicate is "every route exists and is consistent". The
composite is satisfied only when all 22 route results are satisfied.
Otherwise it unions the known failures (falsified routes) and the uncovered
obligations (routes returning indeterminate, out_of_frame or invalid_basis),
and its single stop state is the weakest route result under this order,
declared by this actor because the documents give none (residual R-2):
falsified < invalid_basis < out_of_frame < indeterminate < satisfied. Known
before any read: three routes are out_of_frame, so the composite cannot be
satisfied in this run.

Interpretation contract for "consistent" (P1: a semantic decision is lawful
only under an exact decision contract). A route's characterisation is the
commitment paragraph's statement together with its claim "Conserves <clause>"
(FOUNDATIONS section 1: conserved means the rc.2 clause governs unchanged).
It is consistent when (a) the rc.2 heading's subject falls within the
commitment's stated scope, and (b) no sentence of the paragraph contradicts
a sentence of the rc.2 section. It is falsified when a paragraph sentence
contradicts the rc.2 text or the heading's subject is foreign to the
commitment. It is indeterminate when the rc.2 section's consuming decision
depends on text outside the section. This contract does not require the
paragraph to restate the clause's obligations; where it restates none, the
evidence says so (residual R-9).

### 2.1 rc.2 member identity (`shasum -a 256`, read-only install)

| Member | sha256 |
|---|---|
| AXIOMATIC_CALCULUS.md | cbe2edb928d3e75e23446f6d525baea664966e8d5920e6fa389cbaa4af8f1f8d (matches the projection's declared hash) |
| REFERENCE_FRAME_METHOD.md | 6e9148d7c8eff847abf172315b0e282e4477f3d40866b28f7fef21c41cb067e7 |
| SPEC_METHOD.md | 7f12d32ef4e5720d5d59ee5ace50de6c1a12cc56afa53dd67a8ee4c54f8fb8a4 |
| DESIGN_MODULE_METHOD.md | 5cb69556bba1171ec347cac96811c50071f0648a367103aa215070239b93785e |
| WORLD_MODEL_METHOD.md | 123ddcd05130aa95508c9fcfa194bf083caae3657baedaba0ce9214009453762 |

## 3. Per-route results

Each route carries two sub-results (existence of the slug; consistency of
the characterisation) and one core result, the weaker of the two. "Heading
read" quotes the heading line as printed by `fragment.py --text`. Quoted rc.2
sentences are the evidence relied on; a later actor can re-acquire them by
member and slug.

### P1 Interpretation (step S1, 2,662 bytes)

R01 AXIOMATIC_CALCULUS.md#ac-017-interpretation-fidelity. Existence:
satisfied; heading read "### AC-017 Interpretation Fidelity", 378 bytes.
Consistency: rc.2 requires that admitted model records map to exact subject
provenance or are identified as model-local, that every evaluated subject
declaration has a disposition, and that "Interpretation cannot treat absence
as immateriality without a recorded basis and authority." P1 states that
meaning holds "within a declared context through a declared contract" and
that "structural success never establishes fidelity." Subject in scope
(interpretation fidelity); no contradiction. P1 restates none of AC-017's
three specific obligations; the route conserves them by reference only.
Result: satisfied.

R02 AXIOMATIC_CALCULUS.md#ac-018-structural-and-semantic-separation.
Existence: satisfied; "### AC-018 Structural And Semantic Separation", 325
bytes. Consistency: rc.2 "Structural success is evidence for semantic review,
not a substitute for it"; P1 "'Algorithmic' means explicit and structurally
checkable ... structural success never establishes fidelity." Direct
restatement. Result: satisfied.

R03 AXIOMATIC_CALCULUS.md#ac-019-valid-model. Existence: satisfied; "### AC-019
Valid Model", 801 bytes. Consistency: rc.2 "A checker may decide the
structural subset. No generic checker may claim the semantic or authority
subset unless the model supplies an exact lawful decision contract for it";
P1 "a semantic decision is lawful only under an exact decision contract."
Direct restatement of the clause's closing rule; the six validity conditions
are conserved by reference. Result: satisfied.

R04 REFERENCE_FRAME_METHOD.md#rf-008-overlap-without-identity-collapse.
Existence: satisfied; "### RF-008 Overlap Without Identity Collapse", 290
bytes. Consistency: rc.2 "Shared material does not establish identical
meaning, basis, authority, or result"; P1 "two contracts give one
representation two meanings" and "Subject, representation and interpretation
are distinct." Same distinction at a different grain (frames versus
representations); no contradiction. Result: satisfied.

### P2 Purpose (step S2, 5,355 bytes)

R05 SPEC_METHOD.md#proportional-method-and-delivery-stdo-up-014. Existence:
satisfied; "## Proportional Method And Delivery (`STDO-UP-014`)", 4,219
bytes. Consistency: rc.2 "Each constraint must identify the semantic
ambiguity it removes and must contract enough of the admissible
interpretation space to justify the reasoning complexity it introduces"; "A
method addition is disproportionate when it ... expands the bounded
reasoning surface without materially reducing ambiguity"; delivery priority
is applied "to the current Product outcome". P2 "an obligation with no route
to the outcome is unjustified." Consistent: both reject obligations without
a justifying route; UP-014's proportionality relation itself is not restated
in P2 (FOUNDATIONS section 6 routes it to CALCULUS section 6). Result:
satisfied.

R06 DESIGN_MODULE_METHOD.md#boundary-and-governance-cost-stdo-up-005.
Existence: satisfied; "### Boundary And Governance Cost (`STDO-UP-005`)", 653
bytes. Consistency: rc.2 "Review cuts, realization units, runtime modules,
and work items are distinct boundaries ... must not be forced into one-to-one
decomposition for administrative convenience"; "Evidence remains proportional
to semantic change and risk." P2 "interfaces inherit material obligations
from the transformation they serve." No contradiction; the shared principle
is that boundaries and their cost are justified by what they serve. This is
the thinnest route in the section: P2 restates nothing of UP-005. Result:
satisfied (under the declared contract; see residual R-9).

### P3 Identity (steps S3 and S4, 3,490 and 4,051 bytes)

R07 SPEC_METHOD.md#recursive-product-taxonomy. Existence: satisfied; "##
Recursive Product Taxonomy", 2,925 bytes. Consistency: rc.2 distinguishes
Substrate, Development Product ("The role creates no new Product identity
and transfers no meaning or authority"), Source Project, Release Cut,
Product, Install, Artifact and Product Definition, and rules "do not confuse
an immutable RC release cut or installed product with the mutable source
project". P3 "identity is declared (authority, kind, value) and survives
admissible change; current state, historical observation and representation
identity stay separate." Consistent: the taxonomy is an identity discipline
by kind in which roles mint no identity. Result: satisfied.

R08 WORLD_MODEL_METHOD.md#entity-cut-construction-law. Existence: satisfied;
"## Entity Cut Construction Law", 3,486 bytes. Consistency: rc.2 "The claim
carries its own discrimination; a stronger claim needs stronger
discrimination"; "Boundary is interventional in character, not structural";
a cut should state "the reinterpretations under which identity survives". P3
"a boundary is a claim with a proof obligation"; identity "survives
admissible change." Direct correspondence. Result: satisfied.

### P4a Typed composition (step S5, 1,452 bytes)

R09 AXIOMATIC_CALCULUS.md#ac-016-typed-composition. Existence: satisfied;
"### AC-016 Typed Composition", 557 bytes. Consistency: rc.2 "Two traversals
compose only when the first result type and judgment satisfy the second
traversal's exact domain and preconditions ... Composition retains both
traversal identities, intermediate results, judgments, evidence, authority,
provenance, and stop states." P4a restates this with "steps" for
"traversals" and the retained list minus "provenance". No contradiction; one
retained item dropped from the restatement (finding F3), and AC-016's
"cannot flatten probabilistic proposal, deterministic evaluation, and human
decision" is not restated. Result: satisfied.

R10 REFERENCE_FRAME_METHOD.md#rf-010-composition-on-demand. Existence:
satisfied; "### RF-010 Composition On Demand", 430 bytes. Consistency: rc.2
"Composition law is required only when the governing evaluation combines
their internal variables, transports evidence or values across them, or
treats their operations as one material execution relation"; independent
evaluations "may instead return closed results to one declared conjunction".
P4a states when two steps compose; RF-010 states when composition law is
needed at all. Compatible; FOUNDATIONS section 4 restates RF-010 (outside the
section 3 predicate). Result: satisfied.

### P4b Conservation of step-produced facts (step S6, 4,203 bytes; S9 and S10 not read)

R11 AXIOMATIC_CALCULUS.md#ac-013-transformation. Existence: satisfied by
measurement only (`--size` exit 0, 6,411 bytes; the heading line was not
read). Consistency: out_of_frame. The coupled pair measures 7,348 bytes
against a 6,000-byte cap; the fragment alone (6,411) exceeds the cap, so no
reading of this route under any pairing is possible for this actor. No read
was performed. Escalation: an actor whose envelope is at least 7,348 bytes
(Run A's 160,000 fits). Result: out_of_frame.

R12 AXIOMATIC_CALCULUS.md#ac-005-authority-conservation. Existence:
satisfied; "### AC-005 Authority Conservation", 324 bytes. Consistency: rc.2
objects, relations, judgments and the rest "retain their declared semantic,
operation, evaluation, and decision authority. Copying, interpreting,
encoding, evaluating, or transporting a record does not transfer authority."
P4b: authority decisions "are recorded by the step that produced them", and
AC-005 is the "authority" typed instance of the one conservation
obligation. Consistent. P4b calls the clause both "Conserves" and
"reframed"; FOUNDATIONS section 1 gives a clause one standing (residual
R-4; not a contradiction of the rc.2 text). Result: satisfied.

R13 DESIGN_MODULE_METHOD.md#bounded-frame-conservation-stdo-up-017.
Existence: satisfied; "### Bounded Frame Conservation (`STDO-UP-017`)", 2,942
bytes. Consistency: rc.2 "A bounded local action conserves governing truth;
it does not rewrite it"; "Every seam crossing the affected set must either
include its causally relevant far-side relation in that set, or state why".
P4b: the "frame" typed instance of conservation. Consistent; UP-017's seam
and derivation-order content is not restated in P4b (FOUNDATIONS section 6
routes UP-017 to P4b; the seam rule reappears in CALCULUS section 4, outside
this basis). Result: satisfied.

R14 SPEC_METHOD.md#complete-enclosing-relation-admission-stdo-up-021.
Existence: satisfied by measurement only (`--size` exit 0, 5,914 bytes;
heading line not read). Consistency: out_of_frame. The coupled pair measures
6,851 bytes against the 6,000 cap. The fragment alone would fit (5,914), but
the case names the coupled pair as the unit that must fit together, and the
tenant paragraph was charged in every step; reading the fragment without its
paragraph would be the silent omission CALCULUS section 2 forbids. No read
was performed. Escalation: an actor with envelope at least 6,851 bytes, or a
ruling on residual R-1. Result: out_of_frame.

### P5 Totality (step S7, 2,568 bytes)

R15 REFERENCE_FRAME_METHOD.md#rf-012-closed-results. Existence: satisfied;
"### RF-012 Closed Results", 624 bytes. Consistency: rc.2 lists exactly
satisfied, falsified, indeterminate, out_of_frame and invalid_basis with
meanings matching CALCULUS section 3 in name and nearly in wording, and
allows an extension that preserves "explicit indeterminate, out-of-frame, and
invalid-basis pressure". P5 "its result algebra carries indeterminate,
out_of_frame and invalid_basis as first-class outcomes." Direct
correspondence. P5 says "Conserves" while CALCULUS sections 3 and 8 say
RF-012 is "superseded" by the section 3 algebra (residual R-4). Result:
satisfied.

R16 REFERENCE_FRAME_METHOD.md#rf-014-capability-fit. Existence: satisfied;
"### RF-014 Capability Fit", 318 bytes. Consistency: rc.2 "When the material
manifold exceeds an actor's capability envelope, human authority may select
another actor, refine the frame, sequence activations, or provide a lawful
compression. The actor may not silently omit material relations to fit
context." P5 "A step can meet a condition outside its context; it cannot
report success on one." Consistent. Observation for this run: RF-014 places
the selection among the options with human authority; this return names the
escalation and does not select it (residual R-3). Result: satisfied.

R17 AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal. Existence:
satisfied; "### AC-007 Constraint And Refusal", 275 bytes. Consistency: rc.2
"A failed, missing, indeterminate, out-of-scope, or invalid-basis result
follows the declared result algebra rather than being coerced to success."
P5's first-class non-success outcomes and "cannot report success" agree.
Consistent. Incidental observation outside the predicate: AC-007 names result
conditions (failed, missing, out-of-scope), not the five member names, which
bears on CALCULUS section 3's wording "name the same five outcomes"
(residual R-7). Result: satisfied.

R18 DESIGN_MODULE_METHOD.md#8-totality-rule. Existence: satisfied; "## 8.
Totality Rule", 660 bytes. Consistency: rc.2 "Semantic functions should be
total"; "failure is returned in a typed and explicit form"; prefer "closed
outcome carriers" and "explicit 'unsupported' or 'rejected' outcomes"; avoid
"partial functions that assume hidden preconditions". P5 generalises typed
explicit failure from software functions to steps. No contradiction; the rc.2
rule is profile guidance ("should"). Result: satisfied.

### P6 Justification and authority (step S8, 2,310 bytes; S11 not read)

R19 SPEC_METHOD.md#semantic-evidence-and-projection-separation-stdo-up-008.
Existence: satisfied; "### Semantic, Evidence, And Projection Separation
(`STDO-UP-008`)", 728 bytes. Consistency: rc.2 distinguishes semantic basis,
evidence basis and state projection; "Evidence change may invalidate a
verdict without changing law. Projection change may invalidate a view without
changing semantic truth. Semantic change requires lawful re-entry." P6
"Definitions, assumptions, observations, candidate judgments and accepted
claims have distinct standing; evidence supports a claim on a basis."
Consistent (EVALUATION section 2 carries the three invalidation sentences
almost verbatim). Result: satisfied.

R20 SPEC_METHOD.md#assurance-boundary-congruence-and-method-qualification-stdo-up-022.
Existence: satisfied by measurement only (`--size` exit 0, 5,343 bytes;
heading line not read). Consistency: out_of_frame. The coupled pair measures
6,191 bytes against the 6,000 cap; the fragment alone would fit (5,343); the
same reasoning as R14 applies. No read was performed. Escalation: an actor
with envelope at least 6,191 bytes, or a ruling on residual R-1. Result:
out_of_frame.

R21 REFERENCE_FRAME_METHOD.md#rf-006-authority-conservation. Existence:
satisfied; "### RF-006 Authority Conservation", 297 bytes. Consistency: rc.2
a frame "does not mint, widen, transfer, or reconstruct semantic,
evaluation, operation, or decision authority from actor identity, available
capability, evidence shape, implementation reachability, or frame selection."
P6 "authority permits or disposes within scope; neither is minted by the
other"; ontology row "never minted from capability, label or reachability."
Direct correspondence. Result: satisfied.

R22 REFERENCE_FRAME_METHOD.md#rf-007-semantic-evidence-and-verdict-separation.
Existence: satisfied; "### RF-007 Semantic, Evidence, And Verdict
Separation", 437 bytes. Consistency: rc.2 "Semantic law defines what the
evaluation means. Evidence supplies observations. The evaluator applies the
declared relation ... Decision authority disposes the result"; roles stay
distinguishable "even when one actor lawfully performs several of them." P6's
distinct standings and "authority permits or disposes within scope" agree
(EVALUATION section 2 restates RF-007's four roles). Result: satisfied.

### Route result table

| Route | Existence | Consistency | Core result | Step | Bytes read |
|---|---|---|---|---|---|
| R01 | satisfied | satisfied | satisfied | S1 | 378 |
| R02 | satisfied | satisfied | satisfied | S1 | 325 |
| R03 | satisfied | satisfied | satisfied | S1 | 801 |
| R04 | satisfied | satisfied | satisfied | S1 | 290 |
| R05 | satisfied | satisfied | satisfied | S2 | 4,219 |
| R06 | satisfied | satisfied | satisfied | S2 | 653 |
| R07 | satisfied | satisfied | satisfied | S3 | 2,925 |
| R08 | satisfied | satisfied | satisfied | S4 | 3,486 |
| R09 | satisfied | satisfied | satisfied | S5 | 557 |
| R10 | satisfied | satisfied | satisfied | S5 | 430 |
| R11 | satisfied (by measurement) | out_of_frame | out_of_frame | S9 | 0 (pair 7,348) |
| R12 | satisfied | satisfied | satisfied | S6 | 324 |
| R13 | satisfied | satisfied | satisfied | S6 | 2,942 |
| R14 | satisfied (by measurement) | out_of_frame | out_of_frame | S10 | 0 (pair 6,851) |
| R15 | satisfied | satisfied | satisfied | S7 | 624 |
| R16 | satisfied | satisfied | satisfied | S7 | 318 |
| R17 | satisfied | satisfied | satisfied | S7 | 275 |
| R18 | satisfied | satisfied | satisfied | S7 | 660 |
| R19 | satisfied | satisfied | satisfied | S8 | 728 |
| R20 | satisfied (by measurement) | out_of_frame | out_of_frame | S11 | 0 (pair 6,191) |
| R21 | satisfied | satisfied | satisfied | S8 | 297 |
| R22 | satisfied | satisfied | satisfied | S8 | 437 |

No route is falsified, indeterminate or invalid_basis. No route was dropped.

## 4. Composite result for FOUNDATIONS section 3

Computed by the rule declared in section 2 before any read.

- Required obligation set R: 22 routes, each with existence and consistency.
- Admitted coverage C: existence 22 of 22; consistency 19 of 22.
- Known failures (falsified): none.
- Uncovered required obligations (R minus C): consistency of R11, R14, R20,
  each out_of_frame with its measured pair size and escalation.
- Weakest route result: out_of_frame.

Composite: out_of_frame. The section-level predicate is not satisfied and not
falsified; three routes need a capability (an envelope of at least 7,348
bytes, or a human ruling on residual R-1) that this actor does not have. The
19 satisfied routes and the 22 existence results are closed results a later
actor may reuse after the applicability check in CALCULUS section 7 (the
invalidators are listed in section 2, Boundary); the three uncovered
obligations survive every join until an actor with a fitting envelope
returns their results.

## 5. Bytes transferred

| Step | Subject bytes transferred | Under cap |
|---|---|---|
| S1 | 2,662 | yes |
| S2 | 5,355 | yes (largest step) |
| S3 | 3,490 | yes |
| S4 | 4,051 | yes |
| S5 | 1,452 | yes |
| S6 | 4,203 | yes |
| S7 | 2,568 | yes |
| S8 | 2,310 | yes |
| S9, S10, S11 | 0 | no read |
| total | 26,091 | |

Each reading step's first output line was the guard's measurement
("MEASURED ... -> fits"); no step printed subject text without it. Standing
basis: 130,793 bytes, reported once in section 1. Not charged: measurement
output (the 22-row size listing, member sizes, hashes, directory listing,
link enumeration). Delegated actors: none; all transfer was into this one
context. Wall time: see the header (start 11:15:41 UTC); the 60-minute
budget was not exceeded.

## 6. Stop state

Core result for this activation: out_of_frame. Construction-availability
refinement: re_entry_requested (maps to out_of_frame). The candidate (this
return) is complete for 19 routes and for all 22 existence checks; the outer
contract (one consistency result per route) needs a capability outside this
actor's declared envelope for three routes. Next move, named per P5: human
authority (RF-014) selects an actor whose envelope fits the three remaining
coupled pairs, or rules on residual R-1; that actor reads R11, R14 and R20
and recomputes the composite under the rule in section 2. Nothing here is a
disposition; acceptance is reserved (EVALUATION section 4, section 5).

## 7. Residuals

R-1. Paragraph residency. R14 (5,914) and R20 (5,343) fit the cap alone;
they fail it only when the tenant paragraph (937 and 848 bytes) is charged
with them. The paragraph was already resident as standing basis. This run
charged the paragraph in every step because the case names the coupled pair
as the unit that must fit together and the parent instruction forbids
trimming required material. Whether a resident paragraph may be treated as
transferred at zero cost in a step is a ruling for the case owner; under
that ruling R14 and R20 become readable and only R11 remains out_of_frame.

R-2. The documents give no order among non-satisfied members for a composite
stop state. FOUNDATIONS section 4 says failures union and uncovered
obligations survive joins; CASE E2 says "weakest". This run declared the
order falsified < invalid_basis < out_of_frame < indeterminate < satisfied.

R-3. RF-014 says "human authority may select another actor, refine the
frame, sequence activations, or provide a lawful compression"; CALCULUS
section 2 step 3 lists the same options as the step's own ("one of").
Refinement into fitting steps was performed by this actor as a step option;
selecting another actor is reported as an escalation, not performed.

R-4. Tenant-internal standing tension, outside the task predicate: P5
"Conserves RF-012, AC-007" while CALCULUS sections 3 and 8 say both are
"superseded" by the section 3 algebra; P4b both "Conserves" and says the
conservation clauses "are reframed as one obligation"; FOUNDATIONS section 1
gives a clause exactly one standing. No route was judged against this; it is
recorded for the owner.

R-5. Basis overreach in reading. CALCULUS sections 4 to 8 and EVALUATION
sections 5 to 8 entered context because the files were read whole. They were
not used as basis; the one rule this return needed from CALCULUS section 4
(coupled relations fit together in some step) is cited from CASE.md instead.
A later actor should confine reads to the named sections.

R-6. CASE.md says the cited members together exceed 600,000 bytes; the five
members cited from section 3 measure 423,548. The figure may include members
cited elsewhere in FOUNDATIONS. No result depends on it.

R-7. Incidental, outside the predicate: AC-007's text names "failed,
missing, indeterminate, out-of-scope, or invalid-basis" results; CALCULUS
section 3 says RF-012 and AC-007 "name the same five outcomes". RF-012 does;
AC-007 names conditions, not the member set. For the owner of CALCULUS
section 3.

R-8. P4a's retained list omits "provenance", which AC-016 retains; CALCULUS
section 1 lists provenance among step-produced facts, so the obligation is
carried elsewhere in the corpus but not in P4a (finding F3).

R-9. The declared contract for "consistent" (section 2) is non-contradiction
plus subject in scope. Under a stricter contract requiring the paragraph to
restate the clause's obligations, R01, R06, R07 and R13 would return
indeterminate rather than satisfied. The evidence for each says what is and
is not restated so an assessor can apply either contract.

R-10. The case does not say how a step maps onto an actor's tool calls or
turns. This run used one guarded call per turn per step; the actor's
physical context accumulates every step's transfer plus the standing basis,
so the cap was applied as the per-step transfer measure the case defines,
not as a physical context limit.

R-11. No declared hash for REFERENCE_FRAME_METHOD.md, SPEC_METHOD.md,
DESIGN_MODULE_METHOD.md or WORLD_MODEL_METHOD.md was among the inputs; the
hashes observed on the read-only install are in section 2.1 for comparison
against a_c/t1/README.md by an actor permitted to read it.

R-12. Existence for R11, R14 and R20 rests on `fragment.py --size` resolving
the slug (exit 0), a structural, mechanically decidable check (AC-018); the
heading text was not read. A later actor with a fitting envelope will see
the heading line.

## 8. Findings, ranked by consequence (constructor self-review; not assessment)

F1. Three coupled pairs exceed the Run B cap (R11 7,348; R14 6,851; R20
6,191). Consequence: the composite cannot be satisfied in this run. Smallest
correction: activate those three routes under an envelope of at least 7,348
bytes (Run A), or rule on R-1 and then only R11 needs the larger envelope.
Evidence: section 2 route table; `fragment.py --size` outputs.

F2. Standing tension inside the tenant corpus (R-4): the same clauses carry
"conserves" in FOUNDATIONS section 3 and "superseded" or "reframed" in
CALCULUS section 8 and P4b. Consequence: an undisposed standing is the
condition FOUNDATIONS section 1 says blocks qualification. Smallest
correction: one standing per clause, stated once. Evidence: P5 and P4b text
read in S6 and S7; CALCULUS section 3 and 8 text (standing basis).

F3. P4a drops "provenance" from AC-016's retained list (R-8). Consequence:
low; carried by CALCULUS section 1. Smallest correction: add "provenance" to
P4a. Evidence: S5 output.

F4. Four routes conserve by reference with no restatement (R-9). Consequence:
none under the declared contract; indeterminate under a stricter one.
Smallest correction: none if "conserved by reference" is the intended
standing; otherwise one characterising clause per route in section 3.

Invalidation conditions for every result above: a change to FOUNDATIONS
section 3 (hash 5f5e7ab3...), to fragment.py's slug rule (hash 02c71289...),
or to any cited rc.2 member (hashes in section 2.1).

## 9. Resumption without this run's conversation

A later actor needs only this file and the inputs in section 1. To finish
the outer contract: (1) obtain an envelope of at least 7,348 bytes or a
ruling on R-1; (2) for each of R11, R14, R20 run `fragment.py --size` again
to confirm the sizes in section 2, print the tenant paragraph (P4b lines 115
to 126; P6 lines 138 to 147 of FOUNDATIONS at hash 5f5e7ab3...) and the
fragment with `--text`, and judge under the contract in section 2;
(3) recompute the composite by the rule in section 2 (satisfied only if all
22 are satisfied; otherwise union failures and uncovered obligations and take
the weakest). The 19 satisfied route results and the 22 existence results
are reusable after checking the invalidators in section 8. No external
effects were produced; nothing needs reconciliation. The only file written
by this run is this RETURN.md.

## Appendix A. Step guard used for every reading step

Run as `step.sh STEP_ID PARA_START PARA_END member:slug [member:slug ...]`
from a scratch directory outside the repository; it measures first and
prints nothing when the total exceeds the cap.

```zsh
#!/bin/zsh
CAP=6000
F=.../qualification/cases/T-01/fragment.py
FD=.../standards/FOUNDATIONS.md
RC="/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2/standards"
id=$1; ps=$2; pe=$3; shift 3
para=$(sed -n "${ps},${pe}p" "$FD" | wc -c | tr -d ' ')
total=$para
typeset -a sizes
for pair in "$@"; do
  m=${pair%%:*}; s=${pair#*:}
  sz=$(python3 -I "$F" --file "$RC/$m" --slug "$s" --size) || { echo "REFUSED $id: unresolved $m#$s"; exit 2; }
  sizes+=("$m#$s=$sz")
  total=$((total+sz))
done
if (( total > CAP )); then
  echo "REFUSED $id: measured total $total > cap $CAP (para=$para ${sizes[*]})"
  exit 3
fi
echo "STEP $id MEASURED: para=$para ${sizes[*]} total=$total cap=$CAP -> fits"
sed -n "${ps},${pe}p" "$FD"
for pair in "$@"; do
  m=${pair%%:*}; s=${pair#*:}
  echo "===== RC.2 $m#$s ====="
  python3 -I "$F" --file "$RC/$m" --slug "$s" --text
done
```
