# Proposed replacement relations of the Claude line, by question (I4-04 input to the pen)

Input to the common pen's consolidated decision list under T-002 I4-04.
It lists every `superseded` row and every unresolved compression in the
Claude line's frontier at the I4 rebind (`d0b0024` on
`tenant/claude/c3-synthesis`; the rows are unchanged since the I3 freeze
`2beed8d`), grouped by the question the product owner has to decide. Each
row names the exact predecessor claim at the installed `v2.5.1-rc.2`, the
replacement determination with its owning successor locus, and the member
acceptances that depend on the decision. Nothing here is accepted; each
relation stays proposed until the product owner decides it, and an
undecided relation blocks the dependent member acceptance and this
candidate's eligibility.

## Q1. Work-result values and the single result algebra (7 rows)

Decision asked: that a work step's `incomplete` maps to `falsified` for the
predicate "a candidate is available", never to `indeterminate`; that
`refused` and `incomplete` therefore share the core value `falsified`, with
the cause of the stop selecting the work-result value; that an evaluation
the step planned and did not perform has no result and is carried as a
residual, distinct from one whose evidence cannot decide; and that a result
already held when a basis lock fails is a gap in the disposition's
conjunction, not `invalid_basis`. Owner of the replacement: ACTIVATION §3
`Construction availability`, applying item 3 of the common single result
algebra requirement; FOUNDATIONS §4 `Conjunction of results` for the gap
and stale-result cases. Dependent acceptances: EXECUTIVE_BASELINE,
ACTIVATION, FOUNDATIONS.

| Predecessor claim (`STDO_REFERENCE_FRAME_BASELINE.md`) | Replacement |
|---|---|
| `#work-result-disjointness-and-incomplete-pairing`: variants disjoint by their accompanying result; `incomplete` accompanies `indeterminate` | ACTIVATION §3 Construction availability |
| `#derived-worker-frame-result`: one core result plus exactly one variant, `indeterminate` for `incomplete` | ACTIVATION §3 Construction availability |
| `#3-worker-returns-to-executive-mapping`: `satisfied -> candidate_ready`, `falsified -> refused`, `indeterminate -> incomplete`, `out_of_frame \| invalid_basis -> re_entry_requested` | ACTIVATION §3 Construction availability |
| `#profile-qualification-obligation-5`: every variant disjointly mapped from its core result | ACTIVATION §3 Construction availability |
| `#closure-condition-4-mapping`: every Worker result maps exclusively from one closed core result | ACTIVATION §3 Construction availability |
| `#derived-generic-specialist-frame-set-seam-result`: a seam result | FOUNDATIONS §4 Conjunction of results, Gaps |
| `#executive-drift-locks-stale-held-result`: a held result relabelled `invalid_basis` when the lock fails | FOUNDATIONS §4 Conjunction of results, Stale results |

## Q2. Who adopts a profile (3 rows)

Decision asked: that only Product authority adopts an available profile,
the adoption being recorded in a product definition, ticket, design
module or review; the predecessor's "may" means (DESIGN_MODULE_METHOD
#15) and nine adoption steps (UX_METHOD #13) become the means by which
that authority records its adoption. Owner: PRODUCT_DEFINITION §7
`Collective reference frame basis`. Dependent acceptances: DESIGN_MODULE,
UX, PRODUCT_DEFINITION.

| Predecessor claim | Replacement |
|---|---|
| `DESIGN_MODULE_METHOD.md#15-adoption-guidance` | PRODUCT_DEFINITION §7; DESIGN_MODULE §12 keeps the four means |
| `UX_METHOD.md#1a-constitutional-authority-rule` (adoption part only; the rest conserved at UX §1 and §15) | PRODUCT_DEFINITION §7 |
| `UX_METHOD.md#13-adoption-guidance` | PRODUCT_DEFINITION §7; UX §12 keeps the nine steps |

## Q3. Diagnostic order of the Executive (1 row)

Decision asked: that the Executive asks all eight diagnostic questions in
order, verifying the specialist-frame inputs before question 5, in place
of the predecessor's missing-frame and re-entry application order. Owner:
REFERENCE_FRAME §10 `Diagnostic order`. Dependent: EXECUTIVE_BASELINE,
REFERENCE_FRAME. Row:
`STDO_REFERENCE_FRAME_BASELINE.md#missing-frame-and-re-entry-application-order`.

## Q4. Who disposes an assessed candidate (1 row)

Decision asked: that the decision owner disposes an assessed candidate and
an assessor's recommendation is evidence for that disposition, in place of
"Assessment returns one of these semantic dispositions". Owner: ACTIVATION
§3 `Disposition`. Dependent: SPEC_METHOD, ACTIVATION. Row:
`SPEC_METHOD.md#proportional-disposition-returning-party` (new at I3 step
7, FR-09).

## Q5. The release selector (1 row)

Decision asked: that the "latest-accepted" selector is replaced by the
release law: the highest-ordinal published cut, never moved by acceptance.
Owner: RELEASE §1 selector paragraph, §3 `Exact-cut qualification`, §8
`Acceptance criteria`; IDENTITY §9 restates the rest unchanged. Dependent:
IDENTITY, RELEASE. Row: `IDENTITY_METHOD.md#release-version-boundary`.

## Q6. The profile population count (1 row)

Decision asked: that the hard-coded "fourteen members" is replaced by the
size that the bound calculus member's derivation account yields,
recomputed when that account changes; the population law itself is
conserved. Owner: AXIOMATIC_CALCULUS §8 `Calculus identity`. Dependent:
TRAVERSAL_OCCURRENCE, AXIOMATIC_CALCULUS. Row:
`TRAVERSAL_OCCURRENCE_PROFILE.md#closed-profile-signature-fourteen-members`.

## Q7. The current-surface writing rule (1 row)

Decision asked: that the writing guide's current-surface rule is replaced
by SPEC_METHOD §2 `Specification surface rule` at mandatory force, which
names superseded material among the label uses; the guide keeps its six
preferred terms. Owner: SPEC_METHOD §2. Dependent: WRITING_GUIDE,
SPEC_METHOD. Row: `WRITING_GUIDE.md#current-surface-writing`.

## Q8. The ten authority compressions (10 auxiliary members)

Decision asked: that each `authority_compressions/*` member of rc.2 is
superseded by projection from the a_c set program (RELEASE §7,
PRODUCT_DEFINITION §11), with the projection obligation outstanding: today
no projection of the whole successor corpus exists, and the claims these
members state that no rc.2 body states are carried at the loci the
frontier names (rows 806 to 815 of the Claude frontier). The alternatives
are to carry the compressions as members, or to reject the relation.
Codex's I4 classification treats the compressions as a permitted packaging
alternative plus this reserved replacement decision. Dependent: RELEASE,
PRODUCT_DEFINITION, and the interpretation coverage under I4-05.

| Member | Today |
|---|---|
| `README.md` | the set-3 program and seven frames exist; neither is regenerated from the whole corpus |
| `axiomatic_calculus.compressed.md` | AXIOMATIC_CALCULUS carries the theory in full; not projected |
| `design_module_method.compressed.md` | DESIGN_MODULE with ASSURANCE §14 to §16; not projected |
| `odd_method.compressed.md` | ODD with its canonical compression §20; not projected |
| `spec_method.compressed.md` | SPEC_METHOD with ACTIVATION, PRODUCT_DEFINITION, TICKETS, ASSURANCE; an earlier SPEC_METHOD encoded in seven frames |
| `stdo_bootstrap.md` | PRODUCT_DEFINITION §4, §9, §12 and the templates; `frames/bootstrap.md` is a verbatim frame, not a projection |
| `stdo_compressed.md` | no projection of the whole corpus exists |
| `ticket_method.compressed.md` | TICKETS; not projected |
| `traversal_occurrence_profile.compressed.md` | TRAVERSAL_OCCURRENCE with AXIOMATIC_CALCULUS §8; not projected |
| `ux_method.compressed.md` | UX; not projected |

## Rows this line will add during I4

The conservation reading of I4-04 (140 rows: every `conserved` row whose
predecessor "must" or "shall" is written in the indicative, and every row
the I3 working check judged only from a delta) may yield further proposed
relations. They will be posted as a supplement to this list at the I4
freeze, in the same form.
