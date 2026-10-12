# F-02 Member usability: fresh actors apply four new members from frames under 100 KB

Identity: `urn:stdo-3:claude:case:F-02`. This is a fixture for usability
evidence on the members added since set-3: AXIOMATIC_CALCULUS, SPEC_METHOD
(restated), TICKETS and EXECUTIVE_BASELINE with ASSURANCE. Each actor is
activated on one projected frame, never on the corpus, and each frame is at
most 100,000 bytes materialized. Status: designed. No run exists, and the
expectations are not written here.

## Claim under test

A fresh actor given only one projected frame and one task applies the
member without private knowledge or author memory. For each task below,
one fresh headless actor receives a whole context made of four parts: the
instrument's system line, the routing card, one projected frame of the set-4
program as its only METHOD block, and the task as its TASK block. It
produces the output the task asks for, and the governing relations it
applies are the ones the set-4 program encodes for that frame. The actor
has no tools, no memory and no repository. The card carries no method
content.

There are four tasks, one frame each:

| Task | Frame (METHOD block) | What the actor must apply |
|---|---|---|
| A | `transformation-and-judgment` | the AC-013 transformation record with its closed local and external deltas, preservation, residual conservation and application outcome; the AC-014 judgment record and the promotion relation (AXIOMATIC_CALCULUS §3, §4) |
| B | `triage-and-reentry` | the six determinations of universal intake triage with C, J and O annotations, the computed classification, the change classes (SPEC_METHOD §4); the upward propagation walk to the first missing layer and the triage metadata (TICKETS §4) |
| C | `carrier-and-admission` | the carrier selection table, ticket-state authority and the carrier side of admission (TICKETS §1, §5); the step side of admission and its coordinates (ACTIVATION §1) |
| D | `executive-disposition` | steps 4 to 7 of the complete engagement transition, the five drift locks and their failure results, severity versus priority versus frame result versus boundary effect, the promotion constraint projection (EXECUTIVE_BASELINE §5, §6, §12); testing evidence composition as it bears on step 4 (ASSURANCE §7, §10) |

## Subject under test

The subject is the standards at commit `978d324` on
`tenant/claude/c3-v3-evA`, whose digests are recorded under
[a_c/set-4/](../../../a_c/set-4/README.md). They are encoded as program
`urn:stdo-3:claude:program:a-c-text:set-4`, with canonical digest
`sha256:16f840cb501b0df497d7a7747142e756108d031e6c0db2fbd8d3f69003325025`
and zero diagnostics against the pinned Axiom Indexer. The actor receives
the bytes of the four frame files projected from that program:

| Frame file | SHA-256 | Bytes |
|---|---|---|
| `a_c/set-4/projection-transformation-and-judgment-materialized.json` | `839dff0bba028508132270a61e8fad73f18e7824b01294fe85fdd3b945455ea6` | 56,993 |
| `a_c/set-4/projection-triage-and-reentry-materialized.json` | `90336a8f9e269dc70bb128e41605b51141d6d438cf45b740f433d10c06685ac1` | 68,182 |
| `a_c/set-4/projection-carrier-and-admission-materialized.json` | `5ee0fb61ab65aa130d5950bdb974cfbff37f852f53de322e3bf9227c16fec163` | 67,504 |
| `a_c/set-4/projection-executive-disposition-materialized.json` | `b9b2f361b40ecbff80e59ac43755a9647acc0b4646759e8dfa5e3ddd6c562c75` | 93,412 |

The W13 commit introduced the frame files, and a run names that commit in
the runs table. The set-4 program is a partial encoding: what each frame
carries, and what the size limit kept out, is recorded in the set-4
README. The same actor authored the program increment, the frames and this
fixture.

## Fixture material

- [CARD.md](CARD.md) (`237ea8f9…47b23`, 455 bytes): a byte-identical copy
  of F-01's routing card. It names the two blocks, tells the actor that the
  METHOD block is its only method source, and tells it to return only what
  the task asks for and to say where it had no method source. It carries no
  method content.
- [TASK-A.md](TASK-A.md) (`8a41765c…0ad`, 4,262 bytes): workspace
  `W-invoice-rounding`. The input model holds a requirement sentence with
  its owner, a latitude record and a residual, plus one pinned external
  reference. The proposed successor adds a derived design clause and
  carries the residual with one changed field. The task also gives the
  traversal record and grant of the step, and an independent reviewer's
  evaluation of the successor. The actor writes the transformation
  record, the application outcome, the judgment record and what promotion
  would require.
- [TASK-B.md](TASK-B.md) (`dadfeff5…ca04`, 2,922 bytes): product
  `meter-reports` and an incoming bug report filed as ticket `T-901`. The
  task gives the product definition's time zones, the complete requirement
  set R-20 to R-22, accepted design D-20, the realisation and test
  evidence, and the current release scope. The actor writes the six
  determinations marked C, J or O, the upward walk, the class with its
  re-entry point and flow, and the triage metadata.
- [TASK-C.md](TASK-C.md) (`fe860848…2f70`, 2,948 bytes): project
  `docs-site` and two pieces of work. Work 1 is an exact product-authorised
  one-run instruction with a drafted contract and a complete admission
  record. Work 2 is a goals-wave outcome needing state across three
  sessions, with a self-labelled `admitted` contract, a board card and no
  admission record. The acting agent holds no ticket-state authority. The
  actor names the matching carrier row, the contract state with the
  coordinates present or missing, and whether execution may begin.
- [TASK-D.md](TASK-D.md) (`ae864060…804f`, 3,949 bytes): product
  `shopfront`. The task gives the release mandate, the Product-owned
  severity scale, priority scale, cutoff and hard stop, the Executive's
  grant, a `candidate_ready` Worker result whose commit changes the
  payment step and the address step, and an independent Reviewer result. The Reviewer result is `falsified`, with one severity-high
  finding on a path outside the mandate. A configuration revision changed
  after the review, and that revision falls within the Reviewer result's
  stated invalidation conditions. Acting as Executive, the actor checks the
  five drift locks, evaluates the work result at step 4, gives the four
  values of the finding, and applies one disposition or says why none
  applies.

Every subject is invented for this fixture and is evidence about no
product. Each subject states facts, not the diagnosis the task asks for.

## Instrument invocations

The instrument is [bounded_step.py](../../instruments/bounded_step.py) at
`f92ca26b3e4fda953d8732f0665861d54a9121df67451ea90f981555c6ffe81d`, the
same version F-01 uses. Each task is one step. Run from the tenant root
`specification_methodology/v3/build_tenants/claude/`. The instrument
starts the actor in a fresh empty directory outside any repository.

```sh
python3 -I qualification/instruments/bounded_step.py --cap 400000 \
  --run-dir qualification/runs/<run-id> --step-id A-001 \
  --card qualification/cases/F-02/CARD.md \
  --block "METHOD transformation-and-judgment=a_c/set-4/projection-transformation-and-judgment-materialized.json" \
  --block "TASK=qualification/cases/F-02/TASK-A.md" \
  --model sonnet

python3 -I qualification/instruments/bounded_step.py --cap 400000 \
  --run-dir qualification/runs/<run-id> --step-id B-001 \
  --card qualification/cases/F-02/CARD.md \
  --block "METHOD triage-and-reentry=a_c/set-4/projection-triage-and-reentry-materialized.json" \
  --block "TASK=qualification/cases/F-02/TASK-B.md" \
  --model sonnet

python3 -I qualification/instruments/bounded_step.py --cap 400000 \
  --run-dir qualification/runs/<run-id> --step-id C-001 \
  --card qualification/cases/F-02/CARD.md \
  --block "METHOD carrier-and-admission=a_c/set-4/projection-carrier-and-admission-materialized.json" \
  --block "TASK=qualification/cases/F-02/TASK-C.md" \
  --model sonnet

python3 -I qualification/instruments/bounded_step.py --cap 400000 \
  --run-dir qualification/runs/<run-id> --step-id D-001 \
  --card qualification/cases/F-02/CARD.md \
  --block "METHOD executive-disposition=a_c/set-4/projection-executive-disposition-materialized.json" \
  --block "TASK=qualification/cases/F-02/TASK-D.md" \
  --model sonnet
```

The cap is 400,000 bytes of whole context per step, and the model is
`sonnet`. A repeated trial uses the step ids A-002, B-002 and so on, always
five characters, so the header line stays the length the dry run measured.

The measured-context requirement is the same as F-01's. The instrument
measures the whole context in bytes before any actor exists, logs the
`measured` event with every component's SHA-256, and refuses a context over
the cap without starting an actor. A run record is admissible only when its
`measured` events carry the frame file digests above. A different digest is
a different subject.

## Dry-run measurement

The dry runs were made at design time with `--dry-run`, from this fixture
at these digests, into a scratch run directory outside the repository. No
actor was started.

| Step | Total bytes | System | Card | METHOD block | TASK block | Header |
|---|---|---|---|---|---|---|
| A-001 | 62,067 | 182 | 455 | 57,041 | 4,280 | 109 |
| B-001 | 71,898 | 182 | 455 | 68,221 | 2,940 | 100 |
| C-001 | 71,252 | 182 | 455 | 67,546 | 2,966 | 103 |
| D-001 | 98,161 | 182 | 455 | 93,454 | 3,967 | 103 |

All four fit the cap. The `measured` events carried the frame digests
`839dff0bba02…`, `90336a8f9e26…`, `5ee0fb61ab65…` and `b9b2f361b40e…`, the
card digest `237ea8f915ca…`, and instrument SHA-256 `f92ca26b3e4f…`.

## Expectations

Written by an independent context before any run; see EXPECTATIONS.md.

## Assessment

Under a review Jim authorises, an assessor other than the author reads the
run directory at a named commit after the expectations exist. The assessor
returns a review result per EVALUATION §4 over the expectations, judging
each record against the member's relations as the set-4 program encodes
them and the costs as logged. The assessor makes no repair. The author's
structural check of a record is mechanical evidence, not assessment.

## Runs and assessments

| Run | Operator | Record | Assessment |
|---|---|---|---|
| none | | | |
