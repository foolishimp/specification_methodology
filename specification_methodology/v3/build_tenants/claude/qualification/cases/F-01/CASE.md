# F-01 Frame usability: a fresh actor applies the REFERENCE_FRAME member from its projected frame

Identity: urn:stdo-3:claude:case:F-01. A fixture for the usability evidence
of the REFERENCE_FRAME member, designed under
[DOCUMENT_STRUCTURE](../../../design/DOCUMENT_STRUCTURE.md) "Activation
unit": a finite actor is activated on a projected reference frame, never on
the corpus. Status: designed; no run exists; the expectations are not
written here.

## Claim under test

A fresh actor given only the projected frame and the task applies the
member without private knowledge or author memory. Concretely: for each
task below, one fresh headless actor whose whole context is the instrument's
system line, the routing card, one projected frame of the set-2 program as
the only METHOD block, and the task as the TASK block, produces the output
the task asks for, and the governing relations it applies are those of
REFERENCE_FRAME, FOUNDATIONS §2 and ACTIVATION §1 to §3 and §7 as the
set-2 program encodes them. The actor has no tools, no memory and no
repository; the card carries no method content.

Two tasks, one frame each:

| Task | Frame (METHOD block) | What the actor must apply |
|---|---|---|
| A | `frame-declaration-and-activation` | the minimal frame declaration (REFERENCE_FRAME §13), activation on an exact subject and basis (ACTIVATION §1, §2), the minimal evaluation result with one member of the result algebra (REFERENCE_FRAME §13, ACTIVATION §3, §7) |
| B | `coverage-and-revision` | the coverage ledger fields and statuses (REFERENCE_FRAME §8), the diagnostic order on a missing-frame signal (§10), one revision action with the activations, results and coverage claims it reopens (§10) |

## Subject under test

The standards at commit `1a68fd5` on `tenant/claude/c3-v3`, whose digests
are in the set-2 record under
[a_c/set-2/](../../../a_c/set-2/README.md), encoded as program
`urn:stdo-3:claude:program:a-c-text:set-2` (canonical digest
`sha256:4cc36994c07d5ad637f380cb3b6b577b9b19b996f3b0e55b7335d7ee838aca01`),
and the two frame files projected from it, which are the bytes the actor
receives:

| Frame file | SHA-256 | Bytes |
|---|---|---|
| `a_c/set-2/projection-frame-declaration-and-activation-materialized.json` | `94bb707a8234a17f11647a690dffaa49a0814a16faae5dc7d04d7694fc959231` | 247,020 |
| `a_c/set-2/projection-coverage-and-revision-materialized.json` | `ae12446d197aea778aff725606562e69cfdb14624d1e27978c497c025facc08e` | 208,066 |

The frame files are introduced by the W3 commit that introduces this case;
a run names that commit in the runs table. The frames and this fixture were
authored by the same actor as the set-2 program.

## Fixture material

- [CARD.md](CARD.md) (`237ea8f9…47b23`, 455 bytes): the routing card every
  actor receives. It names the two blocks, tells the actor the METHOD block
  is its only method source, and tells it to return only what the task
  asks for and to say where it had no method source. It carries no method
  content; a card that did would contaminate the claim.
- [TASK-A.md](TASK-A.md) (`93b314b2…624d5`, 3,136 bytes): workspace
  `W-ledger-export`, a basis with two builds, a configuration revision and
  a read-replica move, three evidence items, named authorities, three
  evaluations E1 to E3 and an owner's claim K; the instruction to declare a
  frame for E1 per the minimal frame declaration, activate it, return a
  minimal evaluation result, say what the result does and does not say
  about K, and list what had no method source. The record is invented and is
  evidence about no product.
- [TASK-B.md](TASK-B.md) (`48b2ebd6…ef41e`, 3,985 bytes): workspace
  `W-notify`, a governed outcome, a basis whose configuration revision
  advanced, a declared frame set of three frames, an evaluation inventory
  of six evaluations (two closed, one whose basis changed, one with two
  conflicting activations on the same basis, two never activated, one of
  them with no decision owner recorded), named authorities and an observed
  signal from a release meeting; the instruction to produce the coverage
  ledger with statuses, apply the diagnostic order to the signal, name one
  revision action with what it reopens, and list what had no method source.
  Invented likewise.

## Instrument invocations

The instrument is
[bounded_step.py](../../instruments/bounded_step.py) at
`f92ca26b3e4fda953d8732f0665861d54a9121df67451ea90f981555c6ffe81d`, the
version repaired for R-01 run 002. Each task is one step. Run from the
tenant root `specification_methodology/v3/build_tenants/claude/`; the
instrument itself starts the actor in a fresh empty directory outside any
repository, so no CLAUDE.md enters the actor's context (the R-01 finding).

Task A:

```sh
python3 -I qualification/instruments/bounded_step.py --cap 400000 \
  --run-dir qualification/runs/<run-id> --step-id A-<n> \
  --card qualification/cases/F-01/CARD.md \
  --block "METHOD frame-declaration-and-activation=a_c/set-2/projection-frame-declaration-and-activation-materialized.json" \
  --block "TASK=qualification/cases/F-01/TASK-A.md" \
  --model sonnet
```

Task B:

```sh
python3 -I qualification/instruments/bounded_step.py --cap 400000 \
  --run-dir qualification/runs/<run-id> --step-id B-<n> \
  --card qualification/cases/F-01/CARD.md \
  --block "METHOD coverage-and-revision=a_c/set-2/projection-coverage-and-revision-materialized.json" \
  --block "TASK=qualification/cases/F-01/TASK-B.md" \
  --model sonnet
```

Cap: 400,000 bytes of whole context per step, as in R-01. Model: `sonnet`,
the model id as the instrument logs it. One calibration step per run
(`--calibrate`) records the headless CLI's framework overhead. Each task
runs twice per run (the trial is probabilistic); allowance per run: five
actor starts and 20 minutes wall.

Measured-context requirement: the instrument measures the whole context in
bytes, with every component's SHA-256, before any actor exists, logs the
`measured` event to `lifecycle.jsonl`, and refuses a context over the cap
without starting an actor. A run record is admissible only when its
`measured` events carry the frame file digests above; a different digest is
a different subject. The dry-run measurement at design time (no actor
started), from this fixture at these digests: task A 250,979 bytes (system
182, card 455, METHOD block 247,073, TASK block 3,154, header 115); task B
212,852 bytes (system 182, card 455, METHOD block 208,108, TASK block
4,003, header 104). Both fit the cap. Each run's `lifecycle.jsonl`, the
`steps/*.in.md`, `steps/*.out.md` and `steps/*.usage.json` files are kept
under the run directory; the operator judges nothing.

## Expectations

Written by an independent context before any run; see EXPECTATIONS.md.

## Assessment

An assessor other than the author, under a review Jim authorises, reads
the run directory at a named commit after the expectations exist, and
returns a review result per EVALUATION §4 over the expectations, judging
each record against the member's relations as the set-2 program encodes
them and the costs as logged. The assessor makes no repair. The author's
structural check of a record (the four parts present, a result word from
the algebra, a status word from the seven) is mechanical evidence under
EVALUATION §2, not assessment.

## Runs and assessments

| Run | Operator | Record | Assessment |
|---|---|---|---|
| none | | | |

## Subject revision 2 (2026-10-12)

Standards at commit `ac3ec5f` on `tenant/claude/c3-v3` (the three W2c
repairs: ACTIVATION §3 boundary, REFERENCE_FRAME §10 family-inclusion test
and reopen rule, RF-011 cross-reference), encoded as program
`urn:stdo-3:claude:program:a-c-text:set-3` under
[a_c/set-3/](../../../a_c/set-3/README.md) (canonical digest
`sha256:18f58f7e939b05bafa8d1957c12abc999b9733beb731c2f4f98438bfa13ea38f`),
and the two frame files projected from it, which are the bytes the actor
receives in runs against this revision. The set-3 files are introduced by
the W5 phase 1 commit; a run names that commit in the runs table.

| Frame file | SHA-256 | Bytes |
|---|---|---|
| `a_c/set-3/projection-frame-declaration-and-activation-materialized.json` | `545c293146a95b8fcace05180e59ca9d5b53bebc72de7a4e61297bbb7c21ecbc` | 271,966 |
| `a_c/set-3/projection-coverage-and-revision-materialized.json` | `c4ec41584efb48d8fa15de214b3f88d4bd3f3d2aa43b9116dbca1938cd778757` | 223,594 |

Invocations as in "Instrument invocations" above with `a_c/set-3/` in
place of `a_c/set-2/` in the METHOD block path and the step ids `A-003`,
`A-004`, `B-003`, `B-004` (five characters, so the header line is the
length the original dry run measured). Dry-run measurement at these
digests, no actor started: task A (`A-003`) 275,925 bytes (system 182,
card 455, METHOD block 272,019, TASK block 3,154, header 115); task B
(`B-003`) 228,380 bytes (system 182, card 455, METHOD block 223,636, TASK
block 4,003, header 104). Both fit the cap. CARD.md, TASK-A.md and
TASK-B.md are unchanged (`237ea8f9…`, `93b314b2…`, `48b2ebd6…`).

## Subject revision (2026-10-13)

The standards at commit `4425993` on `tenant/claude/c3-v3`, with two
members advanced during the W27 derivation on the Executive's
instruction: TRAVERSAL_OCCURRENCE to `188bc81` and ACTIVATION to
`9be9f57`; the other twenty-one members are byte-identical to `4425993`.
Their digests are recorded under [a_c/set-6/](../../../a_c/set-6/README.md).
They are encoded as program `urn:stdo-3:claude:program:a-c-text:set-6`,
canonical digest `sha256:d8a1d086508c96036641f13d21e6f1e923d2a65de56d1a8c3814983e5c1bbc83`, zero diagnostics against the pinned Axiom
Indexer, after the fidelity pass recorded in
[a_c/set-6/FIDELITY.md](../../../a_c/set-6/FIDELITY.md) corrected 106
set-5 clauses and removed two. The actor receives the bytes of these frame
files:

| Frame file | SHA-256 | Bytes |
|---|---|---|
| `a_c/set-6/projection-frame-declaration-and-activation-materialized.json` | `f4a8fb6bbf617dde7a1f7b3ec5794906124ebc90098e6644f4b577076e858a80` | 98,438 |
| `a_c/set-6/projection-coverage-and-revision-materialized.json` | `1ccc9c8663a51bc613fd22571808fc1bc791dc58f1475335fbc952198656d0bb` | 94,166 |

The F-01 frames are reselected under the 100,000-byte limit (set-6
README, "F-01 frames reselected"). They carry fewer relations than the
set-2 and set-3 frames, so a run against this revision tests a narrower
frame; the relations left out are listed there. The cap of 400,000 bytes
is unchanged.

Invocations as in "Instrument invocations" above with `a_c/set-6/` in
place of the earlier set directory in the METHOD block path and the step
ids `A-0R2`, `B-0R2` and so on (five characters, so the header line is the
length the earlier dry runs measured). CARD.md and the TASK files are
unchanged. The W27 commits introduce the set-6 files; a run names the
commit it used in the runs table.

Dry-run measurement at these digests with `--dry-run`, into a scratch run
directory outside the repository; no actor was started:

| Step | Total bytes | System | Card | METHOD block | TASK block | Header |
|---|---|---|---|---|---|---|
| A-0R2 | 102,397 | 182 | 455 | 98,491 | 3,154 | 115 |
| B-0R2 | 98,951 | 182 | 455 | 94,208 | 4,003 | 103 |

All 2 fit the cap; the total over 2 steps is 201,348 bytes. The
`measured` events carried the METHOD block digests `f4a8fb6bbf61…`, `1ccc9c8663a5…`
(the frame file digests above), the card digest `237ea8f915ca…` and
instrument SHA-256 `f92ca26b3e4f…`.
