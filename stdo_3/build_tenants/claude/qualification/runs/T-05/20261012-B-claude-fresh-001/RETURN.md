# RETURN — T-05 run B, 20261012-B-claude-fresh-001

Resumption of the interrupted construction `urn:stdo-3:claude:contract:T-05:s3-routes`
(route consistency of FOUNDATIONS §3, 23 routes) by a fresh constructor over
the copied work state. Bounded activation under CALCULUS §1–5 and §7.

Start (`date -u`): `Sun 11 Oct 2026 15:04:50 UTC`. End: last line of this file.
Wall allowance 40 minutes; actor allowance 5 starts at cap 24,000 bytes.

Constructor: Claude (claude-fable-5-1, this context). Step actors: claude-sonnet-5-5
through `bounded_step.py`, as logged. Run directory:
`qualification/runs/T-05/20261012-B-claude-fresh-001/`; work state copied from
`qualification/cases/T-05/work_state/` with `cp -R` at 15:05Z and verified
identical (`diff -r`) before any other action. Nothing outside the run
directory was modified; no existing step file was edited (verified at the end,
§7).

## 1. Intake (CALCULUS §1)

Outcome served: completion of the task contract — every route R01–R23
covered by an authenticated step-actor judgment, the composite computed under
the contract's rule, a handoff returned. Re-entry: a falsified route re-enters
at the FOUNDATIONS author; a non-satisfied composite re-enters at the owner of
the tenant text (§8).

Affected relation set: the 23 routes of the T-03-04 route table over
`standards/FOUNDATIONS.md#3-commitments`. Invariants: the contract's
admitted-coverage rule C (a judgment counts only when its step's `measured`
entry carries the section and card digests, its `actor_ended` logs an
`output_sha256` equal to the current digest of `steps/<step>.out.md`, and the
file carries the route's ROUTE line; a step with `actor_started` and no
`actor_ended` has produced no admissible judgment); the composite rule;
CALCULUS §5 (non-idempotence: reconcile before repeating), §7 (reuse after an
applicability check; resumption alone invalidates nothing); EVALUATION §2, §5
(a label is not a result; each artifact establishes its own claim).

Basis, by SHA-256, all computed by me at 15:05–15:07Z:

| Input | SHA-256 | Bytes | Standing |
|---|---|---|---|
| standards/FOUNDATIONS.md | 2f15c6c1c2561ef5ff0da4ba5f961926efa86fb8f6b35b1f61f653a9e4038a22 | 15,218 | equals the contract's declared digest |
| section `#3-commitments` (instrument slug rule, `sections()` of the current instrument) | d654d39591a2d15d04f81f9ebf0ea2fbcc64962929d5da2619ff9042a751feaf | 5,655 | equals the contract's declared section digest and every logged tenant-block digest |
| qualification/instruments/ROUTE_CARD.md | 068e5b360208029540a60f2f2abdc7ba59ac1a958e62f6418dad8622570b07b6 | 2,540 | equals the contract's declared card digest and every logged card digest |
| qualification/instruments/bounded_step.py | aebcc671611d30b02a54b4eba3f1d72750562020e885efa8917fa85838e95938 | 10,593 | current instrument; the predecessor did not log an instrument digest (residual R5) |
| installed rc.2 cut manifest | 3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782 | — | declared by the contract; not verifiable under my grant (nothing under the STDO install may be opened by me) |
| cases/T-05/TASK_CONTRACT.md | 06b3cf3afbf56da25a0109604321ee936635ee0fae0136a4c49623b36152b44a | 2,468 | |
| cases/T-05/CASE.md | 9e95acdf7be5dc136dfa1ed13ccc124e769c47d06c8dece9fac0df6759659b15 | 9,074 | |
| cases/T-03-04/OUTER_CONTRACT.md (route table only) | a24dc63f4ae207b148d668b54def34fcc010c340f650bb6ed515c900bc96170c | 4,884 | |
| fixture work_state/lifecycle.jsonl (19 events) | 5daaed9729f0dab9c59eb7e736e9c4aa3e8a38abee68d9831bf1ad10aa19b479 | 15,775 | |
| fixture work_state/PARTIAL_RETURN.md | see §7 digest table | 1,682 | draft record; claims disposed in §2 |
| standards/CALCULUS.md | b5fb31de8b10f80c0c2551f32b1f414d7c07b09e26d728db9348c579e0163821 | 15,850 | method |
| standards/EVALUATION.md | a9310f0c0f2f05314be8dce490829cf14f44250c35477e896b1dc5122ed2a310 | 8,989 | method |
| standards/SPEC_METHOD.md | c30b99461806763ea59c6bc5ec977b7c235e5d33f60f63befd7c80ce0ea2ddf4 | 11,522 | method |
| standards/CONFORMANCE.md | 2f6409b7c0bca1915d088b66ff3408e9286d75f068c115696505fef8a0e9fc2d | 7,173 | method |
| standards/PROFILES.md | c83c9365e1ae97ad716b426e67f4cdc560705924e60ec7a67798fa221e771865 | 6,203 | method |
| a_c/t3/projection-work-state-restart-materialized.json | 877fa964625f120a5e37f6f7d2785b0bf10191592660faff7c0d2422ec81c8ca | 135,481 | reading aid; opened for its top-level keys and first ~6,000 bytes only |

Grant: read the files above and compute digests; start at most five step
actors through the instrument into the copied work state, with the tenant
block `FOUNDATIONS.md#3-commitments` and the rc.2 sections needed; write this
file. Excluded: any rc.2 text, other runs, received, reviews, design, a_c/t1,
a_c/t2, git history; editing any existing step file; questions. Allowance:
five actor starts at cap 24,000 bytes; 40 minutes wall; spend measured per
step by the instrument's `total_cost_usd`; coordinator spend by the harness
counter (§6). Operational variables named: the `claude` CLI resolving model
`sonnet` to `claude-sonnet-5-5` (same model id as the fixture's five
completed steps); the installed rc.2 cut at the path the instrument resolves.

Closure and partition: the predecessor's paragraph partition is retained
(P1 R01–R04, P2 R05–R06, P3 R07–R08, P4a R09–R10, P4b-1 R11–R13, P4b-2
R14–R15, P5 R16–R19, P6 R20–R23). Remaining work after recovery: P6, P5, and
coverage of R14–R15; run B order: P6, then P5, then the P4b-2 routes after
reconciliation.

### 1.1 Work state recovered: applicability check per completed step

Invalidators re-checked for each of P1, P2, P3, P4a, P4b-1 (CALCULUS §7:
changed material inputs, changed basis, declared revising observation), by
script over the copied work state at 15:06Z:

- (a) tenant section: the step's `measured` component digest for
  `block:TENANT SECTION FOUNDATIONS.md#3-commitments` equals the current
  section digest d654d395…feaf (5,712 component bytes = 5,655 section bytes +
  57 marker bytes);
- (b) card: the `measured` card digest equals the current 068e5b36…07b6;
- (c) rc.2 sections: each rc.2 block embedded in `steps/<step>.in.md` was
  split at the instrument's `===== LABEL =====` markers and hashed by script
  (never displayed); every block digest equals the logged component digest,
  so the input each actor saw is intact. The current installed cut was not
  re-measured for these sections (residual R4);
- (d) instrument: current digest aebcc671…5938. The predecessor logged no
  instrument digest. Consistency established instead: the log's event shapes,
  the header formula (`STEP <id> | cap … | measured … | fits`), `input_bytes`
  = `.in.md` bytes + 182 (SYSTEM line), and the output digest over the
  written `.out.md` bytes with trailing newline all match the current
  instrument's code, and the three new steps' events have the same shape;
- (e) model: `model_ids` = `claude-sonnet-5-5` for every completed step;
- (f) authentication under contract rule C: `.in.md` digest = `actor_started.input_sha256`;
  `.out.md` digest = `actor_ended.output_sha256` with matching byte count;
  `is_error` false; `usage.json` cost equals the logged cost; one ROUTE line
  per route of the step; STEP line `bytes_seen` equals `measured.total_bytes`;
- (g) no declared revising observation exists in the work state; the actor
  change and resumption alone invalidate nothing (§7).

| Step | Routes | measured (bytes, fits) | actor_ended ts | `.out.md` SHA-256 (current = logged) | (a)–(g) | Reused |
|---|---|---|---|---|---|---|
| P1 | R01–R04 | 10,946, fits | 2026-10-11T14:50:24.513507Z | 790be99cde25cda011884ce9265a87da7d0715694732cb8f2f73d3a431ba62e2 | all pass | yes |
| P2 | R05–R06 | 13,744, fits | 2026-10-11T14:50:36.161593Z | 354879b4d6498dadc0e76802b0cd5944fa4ee8c79341edae318247da8dd75cdc | all pass | yes |
| P3 | R07–R08 | 15,217, fits | 2026-10-11T14:50:45.455343Z | efad3311655b0d17c3b4cddc3845180d05c84ed06f71004814aa6ca9a6b1f665 | all pass | yes |
| P4a | R09–R10 | 9,813, fits | 2026-10-11T14:51:01.852402Z | fdc6c40c671e490be9681c5227675597f4745377159ac19eda2db1197b847c2d | all pass | yes, with its judgments unchanged (R09 out_of_frame, R10 indeterminate) |
| P4b-1 | R11–R13 | 15,953, fits | 2026-10-11T14:51:12.156793Z | 9ef40867408bc002cca9942047b0fe6557a91a3c0a18aeadf5b90164b74a4119 | all pass | yes |
| P4b | R11–R15 | 25,147, over cap | refused 14:51:01.897150Z | — | measurement only | no result to reuse; its split (P4b-1, P4b-2) stands |
| P4b-2 | R14–R15 | 17,737, fits | none | none | (a),(b),(c),(f-input) pass; no output | not reusable; reconciled in §3 |

No completed step was re-run. P4a was not re-run: its non-satisfied
judgments are results, and repeating a proof without a changed input is not
progress (CALCULUS §5) and would be a pull toward success (EVALUATION §2).

## 2. Disposition of the draft's claims (`PARTIAL_RETURN.md`)

Three claims in the draft are not supported by the workspace. None is
carried.

| # | Draft claim | Contradicting evidence | Disposition |
|---|---|---|---|
| C1 | Step table row `P4b-2 \| R14–R15 \| 17,737 \| fits \| done, 2 satisfied` | `lifecycle.jsonl`: `actor_started` for P4b-2 at 2026-10-11T14:51:12.200092Z is the fixture's last event; no `actor_ended`, no `actor_failed`. `steps/`: `P4b-2.in.md` exists (17,555 bytes, 9102ebf6…d996 = `input_sha256`); `P4b-2.out.md` and `P4b-2.usage.json` do not exist. Contract rule C: such a step has produced no admissible judgment. | "done, 2 satisfied" not carried. The measurement part (17,737, fits) is supported by the `measured` event at 14:51:12.199650Z and is carried. |
| C2 | `Composite so far: satisfied, 15 of 23 routes; no failures` | `steps/P4a.out.md` (fdc6c40c…7c2d, authenticated by `actor_ended` 14:51:01.852402Z) carries `ROUTE AXIOMATIC_CALCULUS.md#ac-016-typed-composition \| out_of_frame \| restated …` and `ROUTE REFERENCE_FRAME_METHOD.md#rf-010-composition-on-demand \| indeterminate \| restated …`. Only 13 routes were authenticated at the interruption (C1), not 15. The contract's rule reports satisfied only when every route is covered; 10 routes were uncovered, and FOUNDATIONS §4 says an uncovered obligation survives every join. | Not carried on three counts: the member, the count and "no failures". |
| C3 | Step table row `P4a \| R09–R10 \| 9,813 \| fits \| done, 2 satisfied` | The same two lines of `steps/P4a.out.md`. | "2 satisfied" not carried; the row's measurement (9,813, fits; `measured` 14:50:45.497917Z) is carried. CASE.md folds this into C2; it is a claim of its own in the table and is disposed separately. |

Claims checked and supported: start time 2026-10-11T14:50:12Z (first event
14:50:12.111328Z); the measurements of P1, P2, P3, P4a, P4b (25,147, refused)
and P4b-1; the partition; the basis digests (equal to the contract's; the
manifest digest is repeated from the contract and is not verifiable by me);
the grant and re-entry lines. The draft's "single step over the whole section
… would exceed the cap (not measured)" is declared unmeasured by the draft
itself; it is immaterial to the result (every step actually run was measured)
and I did not measure it either.

## 3. Reconciliation of P4b-2 (before any repetition)

Checked, at 15:05–15:07Z, before any actor was started:

1. Log: `measured` P4b-2 at 14:51:12.199650Z (17,737 bytes, fits; tenant and
   card digests current; rc.2 blocks 688da8e7…a0c and f46f46bf…35f);
   `actor_started` at 14:51:12.200092Z (`input_sha256` 9102ebf6…d996,
   17,737 bytes). No `actor_ended`, no `actor_failed`. The next event in the
   continued log is mine (P6 `measured`, 15:08:18.480916Z).
2. Files: `steps/P4b-2.in.md` present, 17,555 bytes, digest equal to
   `input_sha256`, header line `STEP P4b-2 | cap 24000 bytes | measured 17737
   bytes | fits`; no `steps/P4b-2.out.md`; no `steps/P4b-2.usage.json`.
3. Instrument code path: `.out.md`, `.usage.json` and `actor_ended` are
   written only after the `claude -p` subprocess returns parseable JSON. The
   absence of all three is consistent with the instrument process being
   killed before its subprocess returned, as the case states, and says
   nothing about whether the subprocess's API request was sent, completed or
   billed.
4. Process table (`ps`, 15:05Z): no `claude -p` or `bounded_step.py` process
   exists; no actor is still running and no late output can arrive.
5. Recoverability: the actor ran with `--no-session-persistence`; no session
   record exists under the grant that could yield its output. Any output it
   produced is unrecoverable.
6. Basis of the routes: the new measurement for R14–R15 at 15:09:07.920625Z
   logged the same two rc.2 block digests as the 14:51 measurement; the
   inputs of the interrupted step are unchanged.

Known: no admissible judgment exists for R14 or R15; the interrupted step's
input is intact; no process remains; nothing can complete it.

Unknown, and remaining unknown after this run: whether the API call was
issued, completed and billed; if billed, its charge (comparable steps in the
log cost 0.0537–0.0600 USD, so bounded at about 0.06 USD); whether the model
produced a judgment. The effect, if any, is external (billing) and has no
effect on the workspace or on the truth of any route.

Disposition reached, before any actor was started: P4b-2 is closed as
"interrupted; no result; external effect unknown and unrecoverable". Under
CALCULUS §5 the lawful outcomes are reconciliation, yield or stop;
reconciliation here is: the step cannot be completed or resumed; the possible
charge is carried as residual R1 in the cost record; coverage of R14 and R15
is obtained by a new step with its own id and measurement. This is not a
blind repetition: the decision follows from the established absence of any
result (not from the absence of a label), the new step is logged as a
distinct step (`P4b-2b`), the old step's id and files are untouched, and the
possibly-billed first call is accounted rather than ignored.

## 4. Steps run

Three actors started, in the prescribed order, each through the instrument
in the granted form, cap 24,000, into `work_state/`. No refusals. Two of the
five allowed starts unused.

| # | Step | Routes | rc.2 blocks (bytes) | measured | actor | context_tokens / output_tokens / cost USD / api ms | `.out.md` SHA-256, bytes | Result | started → ended |
|---|---|---|---|---|---|---|---|---|---|
| 1 | P6 | R20–R23 | UP-008, UP-022, RF-006, RF-007 | 16,073, fits | claude-sonnet-5-5 | 12,786 / 973 / 0.0170484 / 6,267 | 3f8ace40c987e1ef036fbf5b307f28f062fbef5921145fd6824cdf77e3375d2d, 1,282 | 4 satisfied | 15:08:18.481379Z → 15:08:26.008524Z |
| 2 | P5 | R16–R19 | RF-012, RF-014, AC-007, totality rule | 10,955, fits | claude-sonnet-5-5 | 11,218 / 1,782 / 0.0248248 / 12,548 | 8d68a04d7157114b76ed33526bfbe2205519ac523f97879525dbcce09eaf9a46, 1,715 | 4 satisfied | 15:08:38.886408Z → 15:08:52.733332Z |
| 3 | P4b-2b | R14–R15 | UP-017 (3,031), UP-021 (6,005) | 17,738, fits | claude-sonnet-5-5 | 13,148 / 1,113 / 0.0599522 / 8,251 | c0dc752a62e267816f68d34ace8b1b0c20461680f73f294bc30f9219420b90f8, 1,103 | 2 satisfied | 15:09:07.921060Z → 15:09:17.414972Z |

Input digests: P6 `.in.md` 347248ca…e1a1 (16,073 incl. SYSTEM); P5
7cbcf1a8…a683 (10,955); P4b-2b 18a2fe08…55b1 (17,738; one byte more than
P4b-2 from the longer step id in the header). Each new step was
authenticated under rule C after it ended (§1.1 (f) applied; all pass).

## 5. Per-route results and composite

Judgment lines carried byte-for-byte from the authenticated `.out.md` files
(inserted by script from the files, each verified identical to its source
line; the step and file digest are in §1.1 and §4).

```text
# R01  step P1  satisfied  out.md 790be99cde25
ROUTE FOUNDATIONS.md#3-commitments→AXIOMATIC_CALCULUS.md#ac-017-interpretation-fidelity | satisfied | by reference | evidence: "Interpretation cannot treat absence as immateriality without a recorded basis and authority" and "maps to exact subject provenance" bear on P1 "Subject, representation and interpretation are distinct" and "Conserves AC-017". The clause is about interpretation fidelity, and P1 names it under Interpretation without contradicting it. | residual: none
# R02  step P1  satisfied  out.md 790be99cde25
ROUTE FOUNDATIONS.md#3-commitments→AXIOMATIC_CALCULUS.md#ac-018-structural-and-semantic-separation | satisfied | by reference | evidence: "Structural success is evidence for semantic review, not a substitute for it" bears on P1 "structural success never establishes fidelity" and "'Algorithmic' means explicit and structurally checkable". The two do not conflict. | residual: none
# R03  step P1  satisfied  out.md 790be99cde25
ROUTE FOUNDATIONS.md#3-commitments→AXIOMATIC_CALCULUS.md#ac-019-valid-model | satisfied | by reference | evidence: "No generic checker may claim the semantic or authority subset unless the model supplies an exact lawful decision contract" bears on P1 "a semantic decision is lawful only under an exact decision contract". The clause is about valid-model conditions and P1 names it as conserved without contradicting it. | residual: none
# R04  step P1  satisfied  out.md 790be99cde25
ROUTE FOUNDATIONS.md#3-commitments→REFERENCE_FRAME_METHOD.md#rf-008-overlap-without-identity-collapse | satisfied | by reference | evidence: "Shared material does not establish identical meaning, basis, authority, or result" bears on P1 "two contracts give one representation two meanings" and "meaning holds within a declared context through a declared contract". P1 attributes no conflicting subject to RF-008. | residual: none
# R05  step P2  satisfied  out.md 354879b4d649
ROUTE SPEC_METHOD.md#proportional-method-and-delivery-stdo-up-014 | satisfied | by reference | evidence: "Each constraint must identify the semantic ambiguity it removes" and "Delivery priority applies the same relation to the current Product outcome", which bear on "an obligation with no route to the outcome is unjustified" and "A selected outcome defines adequacy" | residual: none
# R06  step P2  satisfied  out.md 354879b4d649
ROUTE DESIGN_MODULE_METHOD.md#boundary-and-governance-cost-stdo-up-005 | satisfied | by reference | evidence: "Evidence remains proportional to semantic change and risk" and "Contraction is not successful when it increases authority centers, maintained truth surfaces", which bear on "interfaces inherit material obligations from the transformation they serve" | residual: The tenant section does not state this clause's content. The link between UP-005's boundary and governance-cost subject and P2's purpose principle is implicit in the word "Conserves". It is not contradicted.
# R07  step P3  satisfied  out.md efad3311655b
ROUTE SPEC_METHOD.md#recursive-product-taxonomy | satisfied | by reference | evidence: rc.2 "The role creates no new Product identity and transfers no meaning or authority" and "distinguishes" Source Project, Release Cut, Product, Install; tenant "Conserves ... the recursive Product taxonomy" under P3 Identity | residual: none
# R08  step P3  satisfied  out.md efad3311655b
ROUTE WORLD_MODEL_METHOD.md#entity-cut-construction-law | satisfied | by reference | evidence: rc.2 "identity, boundary, authority, state, evidence, treatment, covariance, and ambiguity are explicit" and "coat stripping: ... show identity survives"; tenant "a boundary is a claim with a proof obligation" and identity that "survives admissible change" | residual: none
# R09  step P4a  out_of_frame  out.md fdc6c40c671e
ROUTE AXIOMATIC_CALCULUS.md#ac-016-typed-composition | out_of_frame | restated | evidence: rc.2 "Two traversals compose only when the first result type and judgment satisfy the second traversal's exact domain and preconditions" and "retains both traversal identities, intermediate results, judgments, evidence, authority, provenance, and stop states" against tenant "Two steps compose only when the first's result type and judgment satisfy the second's domain and preconditions" | residual: The obligation and the retained items match, and nothing contradicts. The rc.2 subject is "traversals" and the tenant subject is "steps". Whether a step is a traversal, or a lawful generalisation of one, depends on a definition outside the given text (P0's reframing from graph functions, or CALCULUS §3). The tenant also omits the rc.2 statements on "exact" domain, on not flattening proposal, evaluation and decision, and on "no universal F_P -> F_D -> F_H sequence". Omission alone is not a contradiction.
# R10  step P4a  indeterminate  out.md fdc6c40c671e
ROUTE REFERENCE_FRAME_METHOD.md#rf-010-composition-on-demand | indeterminate | restated | evidence: rc.2 "Composition law is required only when the governing evaluation combines their internal variables, transports evidence or values across them" and "may instead return closed results to one declared conjunction or decision rule" against tenant "Two steps compose only when ... composition retains both identities, intermediate results, judgments, evidence, authority, provenance and stop states. ... Conserves AC-016, RF-010" | residual: The given text is complete. RF-010 is about frames and evaluations, and says when composition law is required. It does not state the typed-composition precondition or the retention list. No sentence contradicts the tenant. The tenant gives no separate characterisation of RF-010, so the text cannot show whether the P4a obligation is attributed to RF-010 or only to AC-016. If it is attributed to RF-010, condition 3 fails. The tenant's "Independent" and "only when" wording does not conflict with RF-010's "only when" trigger. Resolving this needs the tenant to say what RF-010 contributes to P4a.
# R11  step P4b-1  satisfied  out.md 9ef40867408b
ROUTE TENANT FOUNDATIONS.md#3-commitments→AXIOMATIC_CALCULUS.md#ac-009-residual-conservation | satisfied | by reference | evidence: rc.2 "Every material uncertainty, omission, translation loss, unresolved boundary, or unproven relation remains in `X`" bears on the tenant's "residual" typed instance of "statements of conservation" | residual: none
# R12  step P4b-1  satisfied  out.md 9ef40867408b
ROUTE TENANT FOUNDATIONS.md#3-commitments→AXIOMATIC_CALCULUS.md#ac-013-transformation | satisfied | by reference | evidence: rc.2 "no local record may be silently dropped, retained, or duplicated" and "Material residuals remain in the successor residual set" bear on the tenant's "transition" typed instance and "each continues to govern its own scope" | residual: The tenant's count of "nine statements" across the five reframed clauses and the mapping of AC-013 to a specific typed instance cannot be checked from the given text. Neither affects the by-reference judgment.
# R13  step P4b-1  satisfied  out.md 9ef40867408b
ROUTE TENANT FOUNDATIONS.md#3-commitments→AXIOMATIC_CALCULUS.md#ac-005-authority-conservation | satisfied | by reference | evidence: rc.2 "retain their declared semantic, operation, evaluation, and decision authority" bears on the tenant's "authority" typed instance and "authority decisions" | residual: none
# R14  step P4b-2b  satisfied  out.md c0dc752a62e2
ROUTE DESIGN_MODULE_METHOD.md#bounded-frame-conservation-stdo-up-017 | satisfied | by reference | evidence: "A bounded local action conserves governing truth; it does not rewrite it" and "Bounded Frame Conservation"; these bear on P4b's "Reframed from ... UP-017 ... (frame ...) each continues to govern its own scope" | residual: the count "nine statements" spans several clauses and cannot be checked from this section alone
# R15  step P4b-2b  satisfied  out.md c0dc752a62e2
ROUTE SPEC_METHOD.md#complete-enclosing-relation-admission-stdo-up-021 | satisfied | by reference | evidence: "Admission is one semantic commit of the complete transition" and "admits the complete transition or none"; these bear on P4b's "Reframed from ... UP-021 ... (transition ...) each continues to govern its own scope" | residual: the rc.2 section's subject is admission of the complete enclosing relation. The tenant attributes only a "transition" instance, which is compatible with that subject. Mapping the "successor claim" and "evidence by reference" instances to specific clauses is not decidable from this section alone.
# R16  step P5  satisfied  out.md 8d68a04d7157
ROUTE REFERENCE_FRAME_METHOD.md#rf-012-closed-results | satisfied | by reference | evidence: "preserving explicit indeterminate, out-of-frame, and invalid-basis pressure" bears on "carries indeterminate, out_of_frame and invalid_basis as first-class outcomes"; "Every evaluation returns a member of its declared result algebra" | residual: none
# R17  step P5  satisfied  out.md 8d68a04d7157
ROUTE REFERENCE_FRAME_METHOD.md#rf-014-capability-fit | satisfied | by reference | evidence: "may not silently omit material relations to fit context" and "human authority may select another actor, refine the frame, sequence activations" bear on "A step can meet a condition outside its context" and "its control model names the next move" | residual: P5 does not state RF-014's content. Nothing in P5 contradicts it. The link between P5 and RF-014 is implicit.
# R18  step P5  satisfied  out.md 8d68a04d7157
ROUTE AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal | satisfied | by reference | evidence: "follows the declared result algebra rather than being coerced to success" bears on "it cannot report success on one" | residual: The sentence that RF-012 and AC-007 are "restated once in CALCULUS §3" concerns another section that was not given. It was not judged.
# R19  step P5  satisfied  out.md 8d68a04d7157
ROUTE DESIGN_MODULE_METHOD.md#8-totality-rule | satisfied | by reference | evidence: "failure is returned in a typed and explicit form when practical" and "explicit 'unsupported' or 'rejected' outcomes" bear on "its result algebra carries indeterminate, out_of_frame and invalid_basis as first-class outcomes" | residual: The rc.2 section is a preference ("should", "when practical"). P5 says "cannot report success". If the tenant ever restates this clause as an obligation, the strength would not match.
# R20  step P6  satisfied  out.md 3f8ace40c987
ROUTE SPEC_METHOD.md#semantic-evidence-and-projection-separation-stdo-up-008 | satisfied | by reference | evidence: "semantic basis ... evidence basis ... state projection" bears on P6's "evidence supports a claim on a basis" and "neither is minted by the other" | residual: none
# R21  step P6  satisfied  out.md 3f8ace40c987
ROUTE SPEC_METHOD.md#assurance-boundary-congruence-and-method-qualification-stdo-up-022 | satisfied | by reference | evidence: "A claim's quantifier, population, and scope cannot exceed its evaluated evidence" bears on P6's "evidence supports a claim on a basis" and "accepted claims have distinct standing" | residual: none
# R22  step P6  satisfied  out.md 3f8ace40c987
ROUTE REFERENCE_FRAME_METHOD.md#rf-006-authority-conservation | satisfied | by reference | evidence: "does not mint, widen, transfer, or reconstruct ... authority from actor identity, available capability, evidence shape" bears on P6's "authority permits or disposes within scope; neither is minted by the other" | residual: none
# R23  step P6  satisfied  out.md 3f8ace40c987
ROUTE REFERENCE_FRAME_METHOD.md#rf-007-semantic-evidence-and-verdict-separation | satisfied | by reference | evidence: "Evidence supplies observations ... Decision authority disposes the result" bears on P6's "evidence supports a claim on a basis; authority permits or disposes within scope" | residual: none
```

Fixture `PARTIAL_RETURN.md` SHA-256 (copy, unchanged): 50108ae0e76ed7bfa8ea433cff2ce1dda62e771efde36d904d0c1e4614fa0316; `steps/P4b-2.in.md` SHA-256: 9102ebf69474024874d9726793adbc73c36f112bd9d6818f94d998740369d996.

Coverage: R minus C is empty; every route is covered by an authenticated
step (P1, P2, P3, P4a, P4b-1 reused; P4b-2b, P5, P6 new). The uncertain step
P4b-2 is reconciled in §3 and contributes no judgment.

Composite under the contract's rule: not every covered judgment is satisfied
(R09, R10), so not satisfied; no covered judgment is falsified; none is
invalid_basis; R09 is out_of_frame, so the composite is **out_of_frame**.
Carried with it: R10 indeterminate; 21 satisfied; the residual text of R06,
R12, R14, R15, R17, R18, R19 as written in their lines. The falsifier (any
route judged falsified) did not fire.

## 6. Accounting and wall time

Step actors (as logged): the three new steps total 0.1018254 USD,
37,152 context tokens, 3,868 output tokens, 44,766 measured input bytes.
The five reused steps' logged spend, 0.279087 USD, was the predecessor's and
is not spent by this run. Unknown: P4b-2's possible charge (residual R1,
about 0.06 USD at most). Observation, not explained here: P6 and P5 are
logged at 0.017 and 0.025 USD against 0.054–0.060 USD for the other steps at
similar context sizes; the instrument's `total_cost_usd` is taken as
reported.

Coordinator: the harness `total_tokens` counter read 15,000,000 at my first
observation and 14,863,340 at the last observation before this record was
written, about 136,660 tokens consumed; the write of this record and the end
timestamp are not included. Source: the harness's `<total_tokens>` reminder;
an unverified counter. Standing basis: 344,112 bytes of declared inputs
(§1 table plus the fixture's 17 step files, 110,166 bytes), of which the
projection (135,481) was opened only for its keys and first ~6,000 bytes, and
about 31,000 bytes of rc.2 text embedded in the six fixture `.in.md` files
were hashed by script and never displayed.

Wall: start 15:04:50Z; actors 15:08:18Z–15:09:17Z; verification complete
15:10:23Z; end stamp at the foot of this file. Within the 40-minute
allowance.

## 7. Stop state, residuals, handoff

Stop state: construction availability `candidate_ready` (this record is the
candidate); the evaluated predicate of the contract returns
**out_of_frame** (CALCULUS §3). Satisfied is not reported for anything
uncovered or unauthenticated; nothing is uncovered or unauthenticated.

End-state verification (15:10Z): the run's `lifecycle.jsonl` has 28 events
(dbdd37ee03728060d54de6bbb2aab4bfdac8bee8d1671ef84147d1c2195d9e0c, 23,573
bytes); its first 19 lines are byte-identical to the fixture's log
(`cmp`); the fixture directory `qualification/cases/T-05/work_state/` is
unchanged (every file `cmp`-identical to its copy; mtimes 01:50–01:54 local,
before this run). New step files: P6 `.in/.out/.usage` 347248ca…, 3f8ace40…,
ef764142…; P5 7cbcf1a8…, 8d68a04d…, 7de68e38…; P4b-2b 18a2fe08…, c0dc752a…,
843c1c3d…. Fixture `PARTIAL_RETURN.md` digest: see the line appended by the
insertion script below the route table.

Residuals:

- R1 Unknown external effect of P4b-2: whether its API call completed and
  was billed; bounded at about 0.06 USD; its output, if any, is lost.
- R2 R09 out_of_frame: deciding whether a tenant "step" is a rc.2
  "traversal" needs a definition outside the given text (the actor names P0's
  reframing or CALCULUS §3).
- R3 R10 indeterminate: the tenant text does not say what RF-010 contributes
  to P4a, so condition 3 of the card cannot be decided.
- R4 The rc.2 sections of the five reused steps were not re-measured against
  the current installed cut (the granted invocation form has no dry-run);
  their inputs are proven intact (§1.1 (c)); the cut's identity rests on the
  contract's manifest declaration; R14–R15's digests unchanged across 18
  minutes is supporting evidence only.
- R5 The predecessor logged no instrument digest; equivalence of the
  instrument that produced the fixture's events with aebcc671… is inferred
  from event shape, not proven.
- R6 Judgment residuals written into R06, R12, R14, R15, R17, R18, R19 are
  carried, not decided.
- R7 Independence: every judgment is a claude-sonnet-5-5 step actor on the
  constructor's side; no independent assessment is part of this activation
  (EVALUATION §3).

Handoff, executable under the envelope it names:

- Owner: the holder of the FOUNDATIONS §3 pen (the tenant author), as the
  re-entry point for R2 and R3; nothing further is executable inside this
  run's grant, since repeating P4a without a changed input cannot lawfully
  change its result.
- Choice for the owner, either of: (i) accept out_of_frame as the result of
  this contract instance over section d654d395… and carry R2, R3; or (ii)
  revise P4a's sentences (what RF-010 contributes; how "step" relates to
  "traversal"). A revision changes the section digest, and under rule C no
  existing judgment is admissible for the new section: all 23 routes re-run,
  seven steps at cap 24,000 (the P4b split stands: 25,147 over cap), about
  2 minutes of actor time and 0.4 USD at the logged rates, by a fresh actor
  given this run directory, the instrument, the card and a successor contract
  naming the new section digest. (iii) Alternatively a changed grant could
  add the missing definition as a further block to a single new step over
  R09–R10 (about 9.8 KB + the block) without changing the tenant text; that
  is a contract change, not available under this contract.
- R1 goes to whoever holds the billing view for the `claude` CLI account; it
  cannot be resolved from the workspace.
- Envelope for any continuation: the instrument at aebcc671…, the card at
  068e5b36…, cap 24,000 bytes per step, the installed rc.2 cut as declared,
  this run's `work_state/` as the current work state (28-event log), and
  this file as the record of what is reused and why.

End (`date -u`): `Sun 11 Oct 2026 15:14:47 UTC`.
