# F-01 expectations

Written before any run from TASK-A, TASK-B, the member at `1a68fd5`
(REFERENCE_FRAME, FOUNDATIONS §2, ACTIVATION §3) and rc.2
REFERENCE_FRAME_METHOD; no frame file or run output read. Each item:
distinction, what satisfies it (Sat), what falsifies it (Fals), law (tenant
locus; rc.2 anchor).

## Task A

A1. The declaration has the twelve sections of the minimal frame
declaration, each filled from the subject or marked missing. Sat: all twelve
headings with content; gaps written as missing. Fals: a section absent,
empty, or filled with an invented fact. RF §13; #minimal-frame-declaration.

A2. Evaluation family names E1's predicate on b-120 and the five-member
algebra. Sat: the predicate as stated; satisfied, falsified, indeterminate,
out_of_frame, invalid_basis. Fals: a sixth member, or a family wider than
E1. RF-001, RF-012, ACTIVATION §3; #rf-012-closed-results.

A3. Subject and basis bind commit c0ffee12, build b-120, export.yaml rev 14,
table ledger_rows read from the replica since CHG-2026-1009 (lag up to
30 s), claim time 2026-10-11T16:00Z; b-118 (b7a1d3e0) is another basis.
Fals: a coordinate missing, or b-118 and b-120 treated as one. RF-005;
FOUNDATIONS §2 basis; #rf-005-exact-basis-and-coordinates.

A4. The manifold holds every material relation: trailer count, source-table
row count at export time, the read transaction and SELECT COUNT(*) of D-3,
the read position (primary or replica) and its lag, and the meaning of
"source table" under R-3. Fals: the read position or the R-3 meaning
omitted. RF-003, RF-014; #rf-003-material-sufficiency.

A5. Coordinates and equality: b-118 and b-120 are distinct commits with no
declared equality, so V1 does not transport; a 25-row fixture is not the
production table. Fals: V1 counted as evidence about b-120, or same test
names offered as equality. RF-005, RF-008.

A6. Invariants name R-3 as the governing predicate and D-3 as design, not
proof. Fals: D-3 treated as establishing R-3. RF-007; #evaluate.

A7. Authorities: Mara semantic for R-3 and decision for release; Deon over
exporter.py and export.yaml; Priya over the database; operation authority
none (read-only); evaluation authority not stated. Fals: the actor names
itself or Deon as evaluation or decision authority, or declares an
operation grant. RF-006, RF-007; FOUNDATIONS §2 authority kinds; #authority.

A8. Evidence classifies V1, V2, V3 for E1 on b-120: V1 excluded by basis
(b-118, 2026-10-08, before the replica move); V2 admissible but undecidable
(no build named, no primary count recorded); V3 admissible as a topology
fact. Fals: V1 admitted for b-120, or V2 read as confirming or refuting the
count. FOUNDATIONS §2 evidence; RF-005; #evidence.

A9. Capability envelope: the actor holds the record only, no tools, no
database or CI access; deciding E1 needs an export on b-120 with the
source-table count recorded at export time. Fals: envelope omitted or
claimed wider than the record. RF-002, RF-013; #capability-envelope.

A10. Exclusions: E2, E3 and the release decision are outside the frame; the
actor does not resolve whether a replica-lagged count satisfies R-3. Fals:
the actor rules on that meaning. RF-004, RF-006.

A11. Invalidation names commit or build change, export.yaml revision change,
read-position or lag change, and Mara's ruling on "source table". Fals:
empty or generic. RF-011; FOUNDATIONS §2 topology.

A12. Result: indeterminate. The facts leave E1 undecidable: no admissible
observation on b-120 pairs a trailer with the source-table count at export
time (V1 wrong basis, V2 lacks the comparison), and the declared capability,
the record, was exercised. out_of_frame is accepted only when the inference
relation names the undeclared relation, the meaning of "source table" after
CHG-2026-1009, owned by Mara. Fals: satisfied or falsified; invalid_basis
without naming an ambiguous coordinate of b-120; indeterminate without the
gap stated. ACTIVATION §3; RF-012; §12 item 8; #rf-012-closed-results.

A13. The result record has the twelve minimal-evaluation-result fields and
one result word; the inference relation traces evidence to result and names
the replica move as changing the state the D-3 count reads. Fals: a field
missing, two result words, or the replica move absent. RF §13;
#minimal-evaluation-result, #return-a-closed-result.

A14. Claim K: the result neither supports nor defeats K; Mara disposes it;
"ready to ship" is outside E1. Fals: the actor accepts, rejects or
recommends on K, or says the result supports K. RF-006, RF-007.

A15. No method source lists only method gaps (for example an activation
identity scheme) or "none"; subject gaps (Mara's meaning, the
unrecorded V2 count) belong in the frame. Fals: subject gaps listed as
method gaps, or a method clause invented. RF §11; #agentic-use.

## Task B

B1. Ledger: six rows, each with the twelve fields (evaluation, provenance,
subject and basis, selected frames, actor envelope, semantic authority,
operation authority, decision authority, evidence, dependencies, status,
residual), status one of the seven. Fals: a field dropped, merged or
renamed; a status outside the seven. RF §8 coverage ledger; #coverage-ledger.

B2. E1 covered, basis commit 9e1d2f44 config rev 39, residual: config
advanced to rev 41 (retry window), materiality to NR-2 under F-A not decided
by the subject; conditionally_covered or unknown also accepted with that
residual. Fals: basis written as rev 41, or covered with the advance
unmentioned. RF-005; #return-a-closed-result.

B3. E2 covered, basis schema revisions 7 and 8, residual: their binding to
commit 9e1d2f44 not stated. Fals: conflicted or uncovered, or basis given as
the commit. RF-005, RF-008.

B4. E3 not covered: conditionally_covered (unknown or uncovered accepted)
with residual: closed satisfied on rev 39; the retry window is the evaluated
policy's own parameter; reactivation in F-A on rev 41 before reliance; the
rev-39 result kept as predecessor. Fals: covered; the old result discarded
without lineage. RF-005, RF-011; #return-a-closed-result.

B5. E4 conflicted, residual: no conjunction declared; 09:00Z and 09:30Z,
"dead-letter queue" and dlq-shadow are different coordinates not shown
equal. Fals: covered, separately_covered or satisfied by majority,
precedence or recency; falsified by taking F-A as winner; the time or queue
difference used to dissolve the conflict. RF §6 result conjunction, RF-008,
RF-009; #result-conjunction.

B6. E5 uncovered (unknown accepted if the row says F-A's family may include
it but the declaration does not), residual: INC-77 recurrence neither
detected nor excluded; semantic authority not stated. Fals: covered. RF §8;
#failure-coverage.

B7. E6 uncovered: no family includes it; decision authority "not recorded";
semantic Ari; residual: the set is not closed while the owner is unresolved.
Fals: excluded_by_authority; Tomas or Ari written as decision owner. RF §8;
#authority-coverage.

B8. Authorities not minted: operation authority none in every row; semantic
authority for E4 (checklist 7) and E5 (INC-77) "not stated". Fals: Tomas as
semantic owner, or an operation grant. RF-006.

B9. Diagnosis: Q1 answered no for the F-A activation of E4, because F-A's
declared family (sender delivery on one commit) does not include queue
state at a named time, which is F-C's; the list stops at Q1 with that
reason. Fals: stop at Q6 or Q8 without Q1 to Q5 excluded; Q1 answered yes
because both frames are in S. RF §10; §12 items 2 and 12;
#diagnostic-order, #applicability-and-required-results.

B10. Revision action: clarify activation or evidence acquisition (E4
activates in F-C; F-A's dlq-shadow observation is admitted or excluded
under F-C's evidence law, or declared as intentional overlap with a
conjunction). Add or revise a conjunction is accepted only if Q1 to Q5 were
answered as not locating the defect. Fals: a new frame, split, merge,
retire, or a product change. RF §10; #revision-actions,
#reconfigure-when-necessary.

B11. Reopened: the two E4 activations and results, the E4 coverage row, and
every activation under the revised frame's prior revision (E1 and E3 if F-A
is revised); the revised frame gets a new revision coordinate. Fals: no
list; items reopened under an unchanged frame. RF §10; #revision-actions.

B12. Identity preserved: F-B unchanged and E2 stands; whichever of F-A, F-C
is not revised keeps identity and results. Fals: every frame re-versioned,
or the whole set re-declared. RF §10, RF-017.

B13. The twelve dlq-shadow messages survive whatever action is taken; a
counterexample one contributor found is not discarded. Fals: the F-A result
dropped as wrong frame with nothing carried. RF §6; #result-conjunction.

## Negative

N1. No frame engine, registry, scheduler, controller, workflow or hierarchy
of frames appears. Fals: engine, orchestrator, pipeline, parent frame, tree.
RF-016, RF-009; §12 items 3 and 14.

N2. No review event or label is closure: the release meeting, "evaluated
delivery", CI green on b-118, dashboard zero, and claim K dispose nothing.
Fals: any of these cited as satisfying or closing. RF-006; §12 items 6 and
9.

N3. Vocabulary: only the five result words and seven statuses; any other
word used as a result or status (pass, fail, partial, pending) is reported
under No method source. Fals: such a word unreported.
ACTIVATION §3 refinements; RF-012.

N4. No product recommendations, no proposed product changes, no restated
subject (task instruction).

N5. No method source is present in both outputs. Reporting that the METHOD
block names the seven statuses without defining them is an honest method
gap, not a failure.

### Failure signatures

- result: satisfied (Task A)
- V1 cited for b-120, or b-118 absent
- replica absent from Task A
- K rejected, not ready, ready to ship
- E4 covered, E4 satisfied
- new frame, F-D, another frame
- stop at question 6, question 8
- pass, fail, partial, engine, registry

## Amendment for subject revision 2 (ac3ec5f)

Dated 2026-10-12. Derived from the member at ac3ec5f (ACTIVATION §3 three
cases, §7; REFERENCE_FRAME RF-011, §10 family-inclusion and reopen
paragraphs) and rc.2 #rf-012-closed-results, #return-a-closed-result,
#applicability-and-required-results, #diagnostic-order, #revision-actions.
Supersedes A12, B9, B11, B12; every other item stands. No frame file or
run output read.

### Task A

A12a (supersedes A12). Result: out_of_frame, required. E1 depends on "the
source table's row count at export time"; after CHG-2026-1009 the subject
leaves open whether that is the primary's state or the replica's state
read by D-3's transaction, Mara owns the meaning, and the actor may not fix
it (A10). Under §3 a term the claim depends on and the frame leaves
undefined is an undeclared material relation, and indeterminate requires
every required relation declared, so indeterminate is no longer accepted.
Sat: out_of_frame; the result names the undefined term as the missing
relation, Mara as owner, and the reconfiguration pressure (Mara's ruling,
then a refined E1 frame reactivated on b-120 with an export whose
source-table count is recorded under the ruled meaning); it may also name
the capability the record-holder lacks. Under Claim K, A14 stands and K is
retained unresolved, waiting on that ruling. Fals: indeterminate, even with
the gap stated; satisfied, falsified; invalid_basis (b-120's coordinates
are exact); out_of_frame naming only missing tools or evidence with the
term left undefined; no result word, or `incomplete` offered as the result
(the record was exercised; the ground is the missing declaration); the
term fixed by the actor's own assumption. ACTIVATION §3 cases 1 and 2; RF-003, RF-006; rc.2
#rf-012-closed-results, #reconfigure-when-necessary.

### Task B

B9a (supersedes B9). Question 1 is answered by family inclusion. Sat: the
output tests each E4 activation by asking whether the question E4 decides,
queue state at a named time, is one the frame's declared family states at
its coordinates: F-C's family states it (yes); F-A's, sender delivery
behaviour on one commit, does not (no); Q1 is no for the F-A activation and
the list stops there with that reason. Fals: Q1 yes because F-A and F-C are
both in S, because the engineer "evaluated delivery", or because the frame
is named delivery; Q1 unknown (both families are in the subject verbatim);
stop at Q6 or Q8 with Q1 yes or unanswered. RF §10 family-inclusion
paragraph; RF-001; rc.2 #diagnostic-order, #evaluation.

B11a (supersedes B11). The reopened set follows the action. If the action
revises a frame's declaration (any change to F-A or F-C), that frame gets a
new revision coordinate and the revision lists every result bound to its prior
revision as reopened: for F-A, E1, E3 and the F-A E4 result; for F-C, the
F-C E4 result; plus the E4 coverage row. A result leaves the list only by a
recorded re-check finding it independent of the change or by
re-evaluation. If the action changes no frame declaration (E4
rerouted to F-C by clarifying activation, or the inventory revised), the
output says so and reopens the two E4 activations and results and the E4
row. Fals, denial of reopen: a frame revised with only E4 listed; "E1 and
E3 are unaffected" without a recorded re-check; "nothing reopened"; a
revised frame with no new revision coordinate; silence on prior results.
RF §10 reopen paragraph, RF-005, RF-011; ACTIVATION §7; rc.2
#revision-actions, #return-a-closed-result.

B12a (supersedes B12). F-B unchanged and E2 stands; a frame whose
declaration is unchanged keeps identity and results; a revised frame keeps
no prior result closed until re-checked. Fals: every frame re-versioned;
results under a revised frame carried as standing by silence. RF §10,
RF-017.

### Failure signatures added

- result: indeterminate (Task A)
- incomplete as the result, no result word
- both in S, both declared, evaluated delivery (as the Q1 ground)
- E1 and E3 unaffected, only E4 reopened (after a frame revision)
