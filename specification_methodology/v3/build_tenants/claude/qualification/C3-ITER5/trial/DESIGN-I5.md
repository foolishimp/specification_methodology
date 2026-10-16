# Trial design, iteration 5 delta

This file amends the iteration 4 trial design,
[`../../C3-ITER4/trial/DESIGN.md`](../../C3-ITER4/trial/DESIGN.md), for a
run on the iteration 5 candidate. Where this file is silent the iteration 4
design stands. The run itself is not selected here: the shared protocol,
the resources and the decision to run belong to the product owner under
the Product's Candidate Comparison. Nothing in this file is evidence of
fit, use or acceptance.

Terms. An expectation item is one checkable statement about an actor's
return, written by a nonauthor writer before any run. Its assertion
provenance is the account of where the item's expected answer comes from:
the owning obligation, its interpretation, its derivation and the
dependencies it shares with the thing it checks. Its execution provenance
is the record of the run that produced the return it is graded on. Both
are owned by FOUNDATIONS §4 Parallel derivation and mutual assurance; this
delta applies them to the trial.

## 1. Subject and frames

The subject is the iteration 5 candidate at its freeze. Its twelve frames
are regenerated from the current members; each carries a `Binds:` list
that names the construction relation of ACTIVATION §1 by owner section
and digest, and, for the tasks that return an evaluation (TT-01, TT-02,
TT-04, TT-11, TT-12) or decide a reuse (TT-05, TT-06, TT-09), the
applicable assurance relations of FOUNDATIONS §4 (frame-binding
requirement of the ratified input; E2E-01). A frame's `Binds:` item copies
no section; the actor acquires a bound section through the frame's routes
or, in arms A3 and A5, through the isolated `standards/` copy.

Frame bytes differ from the iteration 4 frames. The eight expectation sets
written at iteration 4 (TT-01 to TT-08) remain applicable on the ground
recorded in E2E-01 §4 and the I5-02 return §3: an item's expected answer
depends on the owning sections it names in its `decides` field, and none
of those sections changed in meaning. TT-08's set is rewritten before the
run, as the iteration 4 handoff requires, because its frame carries the
chain section repaired at iteration 4. TT-09 to TT-12 have no set yet. A
set whose deciding sections change before the run is rewritten; a set is
never edited after its hash is recorded.

## 2. Assertion provenance of the expectation items

Each item's `decides` field is its assertion provenance: the owning
obligation (section and quoted sentence), the interpretation (the item's
statement), the derivation (the writer derived it from the owning sections
of the frame's routes, which the writer packet records verbatim and which
are the item's basis Γ), and the shared dependencies (the writer and the
actor both read the owning sections; the writer never sees a frame; the
grader sees neither frame nor sections). An item tagged `F` decides on the
fixture's own facts and is a control on reading, not evidence about the
method.

Predicate kind. Every item is a necessary condition of correct use of the
frame for its task: a return that satisfies every item of a set is not
thereby established to have used the frame correctly in every respect,
and the set's conjunction is not claimed sufficient (FOUNDATIONS §4
Assertions and observation, the three directions). A run's criterion-4
result is therefore the conjunction of necessary conditions it meets and
fails, reported with the items it fails and the items no set covers.

## 3. Weak-assertion and ambiguous-observation cases

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
- one item tagged `A`, an ambiguous observation: an item for which two
  admissible returns, one correct and one not, read the same at the point
  the item observes, so that the observation does not separate them. The
  grader must return `indeterminate` on every run for an `A` item with the
  reason "the observation does not separate the admissible answers"; a
  `satisfied` or `falsified` on an `A` item is a grading defect recorded
  against the grader, not evidence about the run. Its purpose is to show
  observation sufficiency (FOUNDATIONS §4 Assertions and observation,
  Observation sufficiency) in the trial's own instrument.

Both items are written before the set is hashed and are part of the set.
Their presence is disclosed to no actor.

## 4. Shared error and disagreement

Writer, actor and grader are one model family under the declared
exception of the iteration 4 design §4. Writer and actor share the owning
sections; agreement between an actor's return and the writer's expected
answer is compatible with a shared misreading and is not counted as
independent evidence of correctness (FOUNDATIONS §4 Parallel derivation
and mutual assurance). A disagreement, an `M` item graded `falsified`, is
diagnosed after grading by triangulation among the four causes of
ACTIVATION §1 Feedback and diagnosis: the realisation (the frame's content
or routing), the governing text (the owning section), the model (the
expectation item itself may be wrong), and the observation (the grader's
reading of the return). The iteration 4 design's attribution of a failure
to frame content, owner text, task wording or actor application is kept
and read as the first three causes with actor application; the fourth
cause, the grader's observation, is added. An item found wrong by this
diagnosis keeps its original grade in the record and is listed as an
expectation defect; it is not re-tagged or removed (iteration 4 design
§7, as corrected after Codex's finding R3).

## 5. Evidence reuse

No earlier run is reused (iteration 4 design §7). Expectation sets are
reused only under the validity conditions of FOUNDATIONS §4 Change impact
and evidence reuse, as stated in §1 of this file; the record of each run
names the set hash and the frame digest it used. Control-arm (A0)
outcomes are attribution evidence only; every applicable item stays a
criterion-4 item (iteration 4 design §3 and §7, aligned at E2E-01).

## 6. Limits and costs

Frame capacity 160,000 bytes and whole-input cap 300,000 bytes
(CONSTRUCTION_BINDING, FRAME_INPUTS, iteration 4 design §5 and §6 as
amended at E2E-01). The largest frame is 143,930 bytes at the I5-02
rebuild. The disclosure of the harness's instruction files (iteration 4
design §5) is remeasured at the run. Before the arms run: five writer
activations (TT-08 rewritten, TT-09 to TT-12 new) and the `W` and `A`
additions to TT-01 to TT-07 as separate writer activations that receive
the existing set and its owning sections; all twelve hashes recorded in
the ledger; then 44 actor runs and 12 gradings as the iteration 4 design
counts them. Costs are reported where measured; the product owner selects
the resources.

## 7. Not decided here

The run; the shared head-to-head protocol, which the common pen records
under Candidate Comparison after both candidate freezes; cross-family
assessment; any acceptance.
