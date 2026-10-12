# F-02 expectations

Written independently from CASE.md, the tasks and the members at `978d324`, reading no frame under `a_c/` and no run output; rc.2 is v2.5.1-rc.2. Each item: the distinction; S satisfies; F falsifies; L tenant locus, then rc.2 anchor. AC AXIOMATIC_CALCULUS, SM SPEC_METHOD, TK TICKETS, ACT ACTIVATION, EB EXECUTIVE_BASELINE, AS ASSURANCE, TM TICKET_METHOD, SRFB STDO_REFERENCE_FRAME_BASELINE.

### Task A

Required result: application outcome `refusal`. Record: traversal `v-req-to-design-3`; domain `M-billing@r3` (exact content identity missing), codomain `M-billing@r4` (`sha256:7d…e9`); context `W-invoice-rounding`; owner Tomas; scope design records derived from REQ-12; basis `4a1f9e20`; operation_authority `G-88`; preserved REQ-12, LAT-12a (`cj-1` byte identity); introduced DES-12.1; removed none; RES-4 fits no partition; external_preserved the one ISO resolution with one equal witness, other external partitions empty; residuals RES-4 carried, undisposed; evidence RN-31; provenance Tomas, 2026-10-11, under `v-req-to-design-3`; stop_states the stop contract; id, preconditions, preservation_relation, invalidation, re_entry and witness evidence missing. Judgment: Nadia's evaluation of unchanged r4. Promotion: Ravi's acceptance judgment on an unchanged lawful successor; r4 as proposed cannot be promoted.

A1. RES-4 keeps its id but changes a field, so no closed local delta exists. S: RES-4 is neither preserved (changed field) nor removed nor introduced (same id on both sides), so the partition fails. F: RES-4 in `preserved`, or in both `removed` and `introduced`, or silently omitted. L: AC §4 AC-013; rc.2 AC #ac-013-transformation.

A2. The RES-4 edit exceeds the step's coordinates. S: it is outside G-88 (no residual edits) and the traversal scope, a broader coordinate that refuses. F: G-88 or Tomas's design ownership said to cover it. L: AC-013 traversal clause, AC-005; rc.2 AC #ac-013-transformation, #ac-005-authority-conservation.

A3. The outcome follows from A1 and A2. S: `refusal`, input model unchanged. F: `M_b_prime*` produced, `hold` or `gap`, or r4 called accepted or admitted by the step. L: AC-013 application; rc.2 same anchor.

A4. External resolutions form their own closed delta. S: the resolution in `external_preserved`, one witness, tuples field-equal, decision `equal`, witness evidence missing. F: no witness, the external identity in the local partition, or an invented evidence id. L: AC-013; rc.2 same anchor.

A5. The residual is conserved. S: RES-4 carried as material and undisposed (owner Lena, re_entry Requirements); the DES-12.1 credit-note assumption is not a disposition. F: RES-4 resolved, narrowed or dropped. L: AC §3 Residual, AC-009; rc.2 AC #residual, #ac-009-residual-conservation.

A6. Missing stays missing. S: the fields listed above as missing are written so. F: a fabricated digest, id or relation. L: AC-013 model identity; rc.2 AC #ac-013-transformation.

A7. The judgment is an evaluation of an unchanged subject. S: AC-014 fields with subject r4, subject_digest `sha256:7d…e9`, evaluator Nadia, her evaluation authority, decision as she made it, evidence RN-31 and TR-205 on `b-40`, decided_at 2026-10-12T09:00Z, id missing. F: kind or authority as acceptance; decision widened to RES-4 or the transformation; r4 rewritten or renamed. L: AC-014; rc.2 AC #ac-014-judgment-separation.

A8. Promotion is a separate relation to an acceptance or admission judgment. S: Ravi holds acceptance; Nadia's evaluation does not promote; a lawful successor comes first, and Nadia's judgment does not cover its new digest. F: Nadia's judgment named as promotion, Tomas or Nadia named as holder, or r4 promoted despite the refusal. L: AC-014; rc.2 same anchor.

### Task B

Required result: `requirement_reprice`, re-entry Requirements, owner Ines, flowing through Design, Code and Evidence. Determinations: substantive yes; boundary the per-day grouping for every non-UTC tenant; class and re-entry as stated; downstream D-20, `report.py`, `test_group_by_day` with its UTC-only fixture, CR-77; release outside 3.4's scope, repricing reserved to Ines. Walk: Code conforms to D-20 (CR-77); D-20 governs and was accepted against R-20 to R-22; R-20 names no time zone in a product serving three, so it is insufficient; stop at Requirements. Metadata: change_intent, change_class, re_entry_point, triaged_at 2026-10-12T10:00Z.

B1. Annotations separate fact, judgment and ruling. S: observed facts C; R-20's sufficiency and unresolved meaning J; the ruling on "calendar day" and release repricing O for Ines. F: the actor resolves whose calendar day R-20 means, or gives an O ruling to Karl, support or itself. L: SM §4 Computed classification; rc.2 SM #computed-classification-and-treatment.

B2. Scope is wider than the report. S: every non-UTC tenant, America/Chicago included, every day boundary. F: scope limited to `acme-berlin` or 1 October. L: SM §4 Universal intake triage; rc.2 SM #universal-intake-triage.

B3. The walk climbs one layer at a time to the first missing layer. S: Code, Design, Requirements in order with the facts above; stop at Requirements. F: stop at Code or Design, or a jump to Product or Intent with no upstream change shown. L: TK §4 Upward propagation check; rc.2 TM #upward-propagation-check.

B4. The class follows the stop layer. S: `requirement_reprice` with its re-entry, flow and owner. F: `realization_refactor` (code matches design), `design_reframe` (needs R-20 sufficient, not shown), or a Product or Intent class. L: SM §4 Change classes, TK §4 Change class; rc.2 SM #universal-intake-triage, TM #change-class.

B5. No fix, no pre-empted ruling. S: change_intent states the need to settle whose calendar day R-20 means. F: prescribing tenant-local grouping or a code or test change. L: TK §4 Upward propagation check; rc.2 TM #upward-propagation-check.

B6. Downstream and release. S: D-20, `report.py`, the UTC-only test and CR-77 to be re-derived or re-proved; 3.4 repriced by Ines. F: the green test cited as proof for Berlin, or the change placed in 3.4 unrepriced. L: SM §4; rc.2 SM #universal-intake-triage.

B7. Metadata. S: all four fields, triaged_at 2026-10-12T10:00Z; `type: bug` kept and orthogonal to class. F: triaged_at 2026-10-10, a field missing, or type used to pick the class. L: TK §4 Triage metadata; rc.2 TM #triage-metadata.

### Task C

Required result: Work 1 takes the last row (intake-drafted run-scoped contract, no ticket), EC-1 admitted on all five coordinates, execution may begin, results recorded in `runs/2026-10-12-ec1/` before return. Work 2 takes the durable-ticket row (ticket only by Marco), EC-2 drafted, every coordinate missing, no execution; the agent returns the missing work authority, retains the obligation in an authorised durable carrier, marks closure withheld on Marco's authority and returns the re-entry.

C1. Work 1 row. S: last row, rows 1 to 4 not matching. F: a ticket created or required. L: TK §5 Carrier selection; rc.2 TM #work-carrier-to-execution-rule.

C2. Work 1 admission rests on coordinates. S: `admit.py`, `docs-admission`, digest equal to EC-1's, decision, evidence; drafting apart from admission. F: admission inferred from the draft, or digest equality unchecked. L: ACT §1 Admission; rc.2 TM #execution-contract-admission.

C3. Work 2 row. S: GW-7 is upstream authority; three-session state exceeds the run, no sprint; so a durable ticket, created only by Marco, plus the contract. F: row 1, the one-run row, a sprint row, or the agent creating the ticket. L: TK §5; rc.2 TM #work-carrier-to-execution-rule.

C4. EC-2 is drafted. S: drafted; its digest exists but no admission record carries it, the other coordinates missing; the self-label and board lane rejected as evidence. F: admitted, or the board card treated as carrier or progress. L: ACT §1, TK §5; rc.2 TM #work-carrier-to-execution-rule.

C5. The conversation is not a durable surface. S: admission would refuse with it; `tickets/` is bound for ticket-carried work. F: the conversation accepted. L: ACT §1; rc.2 same anchor.

C6. Return without execution. S: no page migrated; missing authority returned; obligation kept in an authorised carrier such as GW-7, closure withheld, re-entry to Marco. F: execution starts, or the obligation lives only in the conversation or on the board. L: TK §5; rc.2 same anchor.

### Task D

Required result: no disposition now. The basis lock fails (r42 came after RR-9, inside its invalidation conditions; WR-31's evidence is on r41), giving `invalid_basis`. accept fails (no consumed result bound to the current basis); local_repair cannot rest on F-1 from invalidated RR-9; re_enter fails (no outcome, requirement, authority or design must change); reject has no valid result on `b-77` with r42. Next action: reactivate independent review and evidence on that basis. F-1: severity high (Hana, on Jules's scale), priority by Omar, frame result `falsified` (Hana, now invalidated), boundary effect no block and an explicit residual with an owner (Omar, under Jules's cutoff).

D1. Basis lock. S: fails on r42, yielding `invalid_basis`. F: holds, or another result. L: EB §6 Drift locks; rc.2 SRFB #executive-drift-locks.

D2. Other locks. S: outcome and authority hold (Priya acted in her own authority, no grant changed); Product-role and coverage-and-return take any value with a cited or named-missing fact. F: authority or outcome failed over r42 or F-1; invented Install identities. L: same.

D3. r42 is not reasoned away. S: RR-9 is not consumed, however unrelated the timeout looks. F: "the timeout does not touch F-1, so RR-9 stands". L: EB §12 step 7; rc.2 SRFB #7-executive-disposes-and-checkpoints.

D4. Step 4. S: candidate_ready on `4be19f02`; EC-77 requires independent review; evidence on r41, so green aggregate does not satisfy; self-review stays Worker evidence. F: step 4 met by green status, or self-review as the review. L: EB §12 step 4, AS §10; rc.2 SRFB #4-executive-evaluates-the-work-result, #testing-evidence-composition.

D5. Four distinct values. S: each with its setter; priority reasoned on exposure, flag, workaround or mandate. F: priority from severity alone or set by Hana; result rewritten. L: EB §5 Technical triage; rc.2 SRFB #technical-triage-severity-priority-and-boundary-effect.

D6. Boundary effect. S: no block under the cutoff, no hard stop, explicit residual with an owner (or owner named missing), or not recordable until revalidation and non-blocking under the cutoff; F-1 is inside RR-9's claim. F: blocks 1.2, a hard stop invoked, the outside-claim row applied, or a new review round opened by severity. L: EB §12 Promotion constraint projection; rc.2 SRFB #executive-promotion-constraint-projection.

D7. Disposition. S: none now, because of `invalid_basis`, with all four conditions stated. F: any disposition applied, or Omar repairing or evaluating himself. L: ACT §3 Disposition, EB §6; rc.2 SM #proportional-disposition.

### Common negative expectations

N1. No self-admission: nothing admits or accepts itself from the actor's own draft (ACT §1; AC-013).
N2. No review event is closure: Nadia's judgment, RR-9 and CR-77 close nothing (AC-014; ACT §3).
N3. No invented carrier or process: no new state, lane, review round, ceremony, or ticket without ticket-state authority (TK §5; ACT §1).
N4. A result word the frame does not define (`pass`, `approved`, `blocked`, `conditional`) used as a result is reported under `No method source`; silent use falsifies; an honest entry there is no failure (ACT §3).

### Failure signatures

A hit points the assessor to a line to read; it is not a verdict.

1. `preserved[^\n]*RES-4`
2. `M_b_prime\*` (A outcome)
3. `realization_refactor|design_reframe` (B class)
4. `triaged_at[^\n]*2026-10-10`
5. `EC-2[^\n]*(is|was) admitted`
6. `Disposition:? *(accept|local_repair|re_enter|reject)\b`
7. `[Bb]asis lock[^\n]*holds`
8. `(high|critical)[^\n]*(therefore|so)[^\n]*P[01]`

## Amendment after the cross-family review (2026-10-13)

Checked against rc.2 meaning only (AXIOMATIC_CALCULUS AC-013, AC-014,
AC-016; SPEC_METHOD universal intake triage, computed classification,
proportional disposition; TICKET_METHOD change class, upward propagation
check, triage metadata, work-carrier-to-execution rule, admission;
STDO_REFERENCE_FRAME_BASELINE drift locks, technical triage, steps 4 and
7, promotion constraint projection). No frame file, run output or a_c/
content read. Original sections unchanged.

Superseded: D6.

D6a. Boundary effect, set by Omar: no block, because F-1 is high, on the
`autofill_v2` path outside the 1.2 mandate, and violates no hard stop; or
not recordable until a review revalidated on r42, and non-blocking under
the cutoff either way. In both readings F-1 survives: it is carried as
the predecessor counterexample of the invalidated RR-9, an explicit
residual with an owner (Omar under Jules's cutoff, or the owner named
missing), neither consumed for disposition nor discarded. F-1 is inside
RR-9's claim. F: blocks 1.2; a hard stop invoked; the outside-claim row
applied; a review round opened by severity; F-1 dropped, voided or left
unmentioned because RR-9 was invalidated. L: EB §12; rc.2 SRFB
#executive-promotion-constraint-projection, RF #return-a-closed-result
(preserve the predecessor), RF #result-conjunction (a counterexample
found by one contributor is not discarded).

Confirmed (31): A1 to A8, B1 to B7, C1 to C6, D1 to D5, D7, N1 to N4;
also the Task A to D required-result statements, Task D's boundary
clause read through D6a.

Reading notes. Task A's `refusal` is AC-013's own application outcome,
not an RF-012 member, so the profile-mapping repair does not reach it; it
refuses on two independent grounds (RES-4 fits no partition; r3 has no
exact content identity). D1's `invalid_basis` is the baseline's own
mapping of a stale basis. D3 stands: RR-9's declared invalidation
condition fired, and independence from r42 is asserted, not
demonstrated. B4's `requirement_reprice` re-enters Ines, who owns the
unresolved meaning (TM upward propagation: meaning stays J, the choice
O); it does not pre-empt her ruling. D4's #testing-evidence-composition
anchor keeps claims distinct. No item relied on cumulative composition,
and none required no result or incomplete for an unexercised capability.
