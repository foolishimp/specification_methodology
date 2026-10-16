# Trial design, iteration 5 delta

This file amends the iteration 4 trial design,
[`../../C3-ITER4/trial/DESIGN.md`](../../C3-ITER4/trial/DESIGN.md), for a
run on the iteration 5 candidate. Where this file is silent the iteration 4
design stands. The run itself is not selected here: the shared protocol,
the resources and the decision to run belong to the product owner under
the Product's Candidate Comparison. Nothing in this file is evidence of
fit, use or acceptance.

Terms. An expectation item is one checkable statement about an actor's
return, written by a nonauthor writer before any run; its `decides` field
quotes the owning section and sentence that make it checkable. An
expectation set is the hashed list of items for one task. An item's
assertion provenance is the account of where its expected answer comes
from: the owning obligation, its interpretation, its assumptions, its
derivation and the dependencies it shares with the thing it checks. Its
execution provenance is the record of the run that produced the return it
is graded on. Both are owned by FOUNDATIONS §4 Parallel derivation and
mutual assurance; this delta applies them to the trial. Two records of
this iteration are cited below: the end-to-end delivery-and-correction
return ([`../returns/E2E-01.md`](../returns/E2E-01.md)), which reassessed
the expectation sets after the frames changed at I5-01, and the I5-02
return ([`../returns/I5-02.md`](../returns/I5-02.md)), which did so after
the consumers paragraphs were written. Four other names: TO1 is the
declared tradeoff of REDUCTION §4.3, that frames carry family-table rows,
which raises M4a, the byte size of a frame; R-I5-01b is the successor
readback of the owner texts of I5-01 ([`../reviews/R-I5-01b.md`](../reviews/R-I5-01b.md));
I5-07 (reduction) and I5-09 (integrated review) are rows of the common
work map T-002; the tasks TT-01 to TT-12 and the arms A0, A1, A3 and A5
are those of the iteration 4 design §2 and §3.

## 1. Subject, frames and what reaches the actor

The subject is the iteration 5 candidate at its freeze. Its twelve frames
are regenerated from the current members; each carries a `Binds:` list
that names, by owner section, member digest and section digest (for the
assurance relations, the digest of the family span from the owner
paragraph through Formal representation), the
construction relation of ACTIVATION §1 and, where the task applies them,
the assurance relations of FOUNDATIONS §4 (every task that returns an
evaluation or a result value at any level of its return: all but TT-10),
Change impact and evidence reuse (TT-02, TT-05, TT-06 and TT-09, the
tasks that decide a reuse or what a revision reopens) and the return
distinction of EVALUATION §6 Return of a reconstruction (TT-12, the
reconstruction task). The rule
is item 4 of the `limits` list in `standards/frames/FRAME_INPUTS.json`;
the requirement it applies is the frame-binding paragraph of
REFERENCE_FRAME_BASIS. A `Binds:` item copies no section and owns no
determination.

What carries a bound section to the actor differs by arm:

- A0 receives no method text; no bound section reaches it.
- A1 receives the frame's bytes and no tools. A bound section reaches the
  actor only where a route of the frame excerpts it; otherwise the actor
  has the `Binds:` item alone, which is a paraphrase and a derived view
  under the constraint-surface fidelity requirement, and the frame's own
  header says so. At I5-06d no route of any frame excerpts a bound
  section, so in A1 every bound obligation reaches the actor as the
  paraphrase. Excerpting the construction relation (9,387 bytes) and the
  assurance relations family (27,998 bytes, owner paragraph through Formal
  representation) in every frame is a tradeoff not taken at this iteration
  and is declared under TO1 (REDUCTION §4.3): the `configuration` frame at
  144,806 bytes leaves 15,194 bytes under the declared capacity, so
  the excerpts would not fit it without a further capacity increase. An `M` item on a bound obligation in A1 therefore
  measures the paraphrase; whether the paraphrase suffices or an excerpt
  is needed is decided by the run and by the frame-entry traces of I5-07.
- A3 receives the frame and the isolated `standards/` copy and follows
  the frame's `Source:` lines and links; each `Binds:` item renders its
  destination as a link, which that instruction admits, so every bound
  section is acquirable.
- A5 receives the isolated copy entered at its `README.md`; bound
  sections are reachable by ordinary discovery, and nothing names them.

The grader does not know the arm; the Executive's attribution reads the
arm from the run record.

## 2. Reuse of the iteration 4 expectation sets

Frame bytes differ from the iteration 4 frames. Seven of the eight sets
written at iteration 4 (TT-01 to TT-07) are reused under the validity
conditions of FOUNDATIONS §4 Change impact and evidence reuse; TT-08's
is rewritten, as stated below. A set's expected answers
depend on four things: the owning sections its items name in their
`decides` fields; the task sentence, which is the item's subject; the
fixture the writer wrote; and the list of sections the frame routed when
the writer was activated, which the writer packet records verbatim as the
writer's basis Γ and which fixes what the set can cover. The task
sentences are unchanged since the preceding candidate (no `task` field of
`FRAME_INPUTS.json` differs from `c66ed4e`); the fixtures are unchanged
since their sets were hashed (`qualification/C3-ITER4/trial/expectations`
last changed at `6f2bce0`). The routed content changed in TT-01, TT-02,
TT-05 and TT-07 at I5-01 (ACTIVATION §7 grew) and in every frame at I5-02
(the Results route uses row selection; the consumers paragraphs are
omitted); a set written over the earlier content covers less of the
current frame where material was added, and the uncovered material is
reported in §3 under the obligations no set covers, never as satisfied.
The judgment that no deciding section changed in meaning is recorded in
E2E-01 §4 and the I5-02 return §3; for ACTIVATION §7 it rests on the
nonauthor readback R-I5-01b, and for every other deciding section it is
the author's claim, labelled as such here and reserved for the I5-09
integrated readback and for the comparison protocol's own conditions.
Until a nonauthor performs that check, the reuse applicability of the
seven sets is unresolved, and a run on them is reported as such.
TT-08's set is rewritten before the run, as the iteration 4 handoff
requires, because its frame carries the constitutional chain section of
SPEC_METHOD §2, repaired at iteration 4 after Codex's finding R1. TT-09
to TT-12 have no set yet.

A set is never edited after its hash is recorded. The `W` and `A`
additions of §4 to TT-01 to TT-07 make a new set with a new hash: the
iteration 4 items enter it unchanged, checked by diff against the hashed
original, and the iteration 4 hash is recorded as superseded, not edited.
A set whose deciding sections change in meaning before the run is
rewritten as a new set.

## 3. Assertion provenance and the result account

Each item's `decides` field is its assertion provenance: the owning
obligation (section and quoted sentence), the interpretation (the item's
statement), the assumptions (the fixture's facts and the basis Γ the
writer read), the derivation (the writer derived the item from the owning
sections of the frame's routes), and the shared dependencies (writer and
actor both read the owning sections; the writer never sees a frame; the
grader sees neither frame nor sections). An item tagged `F` decides on the
fixture's own facts; it stays an assessed criterion-4 item, and only its
attribution differs: it is evidence about reading the fixture, and the
benefit attribution of the iteration 4 design §7 excludes it from any
claim about the method.

Predicate kind. Every item is a necessary condition of correct use of the
frame for its task: a return that satisfies every item of a set is not
thereby established to have used the frame correctly in every respect,
and the set's conjunction is not claimed sufficient (FOUNDATIONS §4
Assertions and observation, the three directions).

Result account. A run's criterion-4 account lists, per item, `satisfied`,
`falsified` or `indeterminate` with the grader's quoted evidence or
reason, and separately the obligations no set covers. A run meets the set
only when every `M`, `F` and `W` item is `satisfied`; a `falsified` item is a
failed condition the account keeps with its standing; an `indeterminate`
`M` or `F` item is reported with its reason (the return neither meets nor
contradicts the item, or is silent) and remains an unestablished
condition, never counted as met.
An `A` item's `indeterminate` is the demonstration the item exists for,
not an unassessed task outcome, and is reported in its own line (§4).
Meeting the set is a necessary condition of correct use, not a sufficient
one; criterion 4 stays unresolved, as work, until the shared protocol's
run.

## 4. Weak-assertion and ambiguous-observation cases

Duty I5-A4 requires the trial to demonstrate weak-assertion and
ambiguous-observation cases through affected ordinary entry. The writer
adds two items to each set under the iteration 5 addendum to its
instructions ([`WRITER-INSTRUCTIONS-I5.md`](WRITER-INSTRUCTIONS-I5.md)):

- one item tagged `W`, a deliberately weak assertion: a necessary
  condition of the task's required outcome that a return making the wrong
  decision can still satisfy (for example, that the return names the
  basis it read). Its purpose is to show that a pass establishes only the
  condition it checks. The grader grades it like any other item; the
  Executive's attribution excludes `W` items from any benefit claim and
  reports them as the weak-assertion demonstration.
- one item tagged `A`, an ambiguous observation: an item that observes
  one point of the return at which two admissible returns, one correct
  under the method and one not, read the same, so that the observation
  does not separate them. The item records the point and both returns in
  an `admissible` field, each return in at most 40 words, marking which
  is correct; the field is part of the hashed set. The grader reads the
  whole return, first checks that the two recorded returns do read the
  same at the recorded point and lists the item as "pair separable" for
  diagnosis (§5) when they do not, then grades the item at that point
  under the addendum to its instructions
  ([`GRADER-INSTRUCTIONS-I5.md`](GRADER-INSTRUCTIONS-I5.md)): where the
  return reads as either recorded return at that point, `indeterminate`
  with the reason "the observation does not separate the admissible
  answers"; where the return is silent at the point, `indeterminate` with
  the reason "silent"; where it reads as neither, `indeterminate` with the
  reason "outside the described ambiguity", and the item is listed for
  diagnosis (§5), because the writer may have constructed an item whose
  observation does separate the answers, which is an expectation defect,
  or the return may have taken a third course. `satisfied` and `falsified`
  are never returned on an `A` item: at the recorded point the observation
  supports neither. The purpose is to exhibit the observation-sufficiency
  condition (FOUNDATIONS §4 Assertions and observation, Observation
  sufficiency) in the trial's own instrument by a case that fails it; the
  demonstration is the recorded pair of returns and the grade at that
  point, not the tag.

Both items are written before the set is hashed and are part of the set.
Their presence is disclosed to no task actor; the grader is told the tags
and the rules above, and nothing about which arm produced a return.

## 5. Shared error, disagreement and diagnosis

Writer, actor and grader are one model family under the declared
exception of the iteration 4 design §4. Writer and actor share the owning
sections; agreement between an actor's return and the writer's expected
answer is compatible with a shared misreading and is not counted as
independent evidence of correctness (FOUNDATIONS §4 Parallel derivation
and mutual assurance). The grader is a probabilistic checker: it may admit
different conclusions on the same return, so a grade is one admitted
conclusion, recorded with the quoted evidence against which a second
grading can be compared; no claim is made that a grading is the only
admissible one.

Ports. No bound section, frame, fixture, expectation item or instruction
of this trial is ported from the Codex line; the iteration 4 grading rule
was corrected after Codex's finding R3, which is a review and not a port.
Material received under I5-04 enters the shared-cause account by name
with its donor and the dependencies it shares with the donor's own
evidence, because porting retains authorship and common dependencies
(FOUNDATIONS §4 Parallel derivation and mutual assurance).

Diagnosis. A disagreement, an `M` or `W` item graded `falsified`, an `A`
item graded "outside the described ambiguity" or an `A` item listed as
"pair separable", is diagnosed after grading
by triangulation among the four causes of ACTIVATION §1 Feedback and
diagnosis, mapped to the trial as follows: the realisation (the frame's
content, its routing and the task wording, and the actor's application of
them); the governing text and its interpretation (the owning section, or
the writer's reading of it in the item, which is where a wrong expectation
item belongs); the predictive model (this design's prediction of how an
arm's inputs change the actor's return, for example that a paraphrase or
a route suffices to carry a bound obligation); and the observation (the
grader's reading of the return). The iteration 4 design's attribution of a
failure to frame content, owner text, task wording or actor application
is kept: frame content, task wording and actor application are the
realisation, owner text is the governing text; the third and fourth
causes are added. A "pair separable" item is an expectation defect by
construction and is recorded as one. An item found wrong by this diagnosis keeps its original
grade in the record and is listed as an expectation defect; it is not
re-tagged or removed (iteration 4 design §7, as corrected after Codex's
finding R3).

## 6. Evidence reuse

No earlier run is reused (iteration 4 design §7). Expectation sets are
reused only under §2 of this file; the record of each run names the set
hash and the frame digest it used, and for A3 and A5 the acquired bytes.
Control-arm (A0) outcomes are attribution evidence only; every applicable
item stays a criterion-4 item (iteration 4 design §3 and §7). The A0 arm
row of the iteration 4 design was corrected in place at E2E-01 because
T-002 row I5-06 asks for exactly that alignment of the stale description;
the capacity amendment, which no common row asks for, is carried in §7 of
this delta instead.

## 7. Limits and costs

Frame capacity 160,000 bytes and whole-input cap 300,000 bytes
(CONSTRUCTION_BINDING, FRAME_INPUTS). This delta amends the iteration 4
design §5 and §6, which declare 150,000 bytes for a frame: the capacity
is 160,000 from E2E-01, raised because the `configuration` frame would
otherwise have been refused at 150,061 bytes (REDUCTION §4.3, TO1); the
whole-input cap is unchanged. The iteration 4 design keeps its iteration 4
figures. The largest frame is 144,806 bytes at I5-06d; all twelve
1,177,665. The disclosure of the harness's instruction files (iteration 4
design §5) is remeasured at the run. While the harness does not disclose
its prompt size, a run's fit judgment is `indeterminate` (iteration 4
design §5), so the proof item "correct use with supported active-context
fit" of T-002 row I5-06 is not reachable by this design alone; it depends
on the disclosure the product owner's protocol selection supplies. Before the arms run: five writer
activations (TT-08 rewritten, TT-09 to TT-12 new) and seven augmenting
writer activations (TT-01 to TT-07) that receive the existing set and its
owning sections and return the new set of §2; all twelve hashes recorded
in the ledger; then 44 actor runs and 12 gradings as the iteration 4
design counts them. Costs are reported where measured; the product owner
selects the resources.

## 8. Not decided here

The run; the shared head-to-head protocol, which the common pen records
under Candidate Comparison after both candidate freezes; cross-family
assessment; any acceptance.
