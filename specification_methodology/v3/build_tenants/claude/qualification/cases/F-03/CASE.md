# F-03 Member usability: fresh actors apply ten swept members from frames under 100 KB

Identity: `urn:stdo-3:claude:case:F-03`. This is a fixture for usability
evidence on the members set-4 did not encode or encoded only in part:
TICKETS carrier and retention with ACTIVATION §1 admission, RELEASE,
IDENTITY, DESIGN_MODULE, ODD, TRAVERSAL_OCCURRENCE, UX, WORLD_MODEL,
PRODUCT_DEFINITION and GLOSSARY. Each actor is activated on one projected
frame, never on the corpus, and each frame is at most 100,000 bytes
materialized. Status: designed. No run exists, and the expectations are
not written here.

## Claim under test

A fresh actor given only one projected frame and one task applies the
member without private knowledge or author memory. For each task below,
one fresh headless actor receives a whole context made of four parts: the
instrument's system line, the routing card, one projected frame of the
set-5 program as its only METHOD block, and the task as its TASK block. It
produces the output the task asks for, and the governing relations it
applies are the ones the set-5 program encodes for that frame. The actor
has no tools, no memory and no repository. The card carries no method
content.

There are nine tasks, one frame each:

| Task | Frame (METHOD block) | What the actor must apply |
|---|---|---|
| A | `carrier-retention` | the carrier-selection table, ticket-shaped versus ticket, ticket-state authority, the obligation-retention order when admission is absent or rejected, including where an obligation is kept without ticket-state authority, and the carrier side of admission (TICKETS §5); goals as orientation, not execution tracking (TICKETS §1); the step side of admission with its coordinates and durable result surface (ACTIVATION §1). This re-runs the gap F-02 task C's actor reported. |
| B | `release-and-successor` | the release identities and project-qualified refs, the three phases (mutable candidate, immutable RC publication, exact-cut qualification) and monotonic advancement, the selector versus consumer adoption (RELEASE §2 to §4); successor baseline conservation (§9, STDO-UP-015) |
| C | `identity-scoped` | scoped identity as authority, kind and value, uniqueness, type and stability (IDENTITY §2); engine-owned versus domain-owned identity (§5); authority identity and conservation (§6, STDO-UP-004) |
| D | `design-gate` | the decision-complete criterion, proportional design sequencing, native constructability (UP-002) and recursive Prime with root conservation (UP-003) (DESIGN_MODULE §5); the ontology and three-view design gate (§7) |
| E | `odd-closure` | the A8 closure decisions with their core mapping, yield versus failure (ODD 11.5D); real authority-path negative proof (11.7B, STDO-UP-010); the cumulative environment law (11.8) |
| F | `traversal-lineage` | causality and typed lineage, OP-001 to OP-007, the stop kinds and their mapping to the core (TRAVERSAL_OCCURRENCE) |
| G | `ux-replay` | the process model, the effect membrane, continuation and the Msg-replay proof, the scaffold and exemption law, the profile results mapped to the core (UX §4, §6, §8, §12, §15) |
| H | `world-model-cut` | entity cut admissibility, discrimination and publication (WORLD_MODEL §9), the attribute ledger law (§8) and saturation (§11), the profile results mapped to the core (§14) |
| I | `bind-and-resolve` | the required definition relations (PRODUCT_DEFINITION §2), bounded-context semantic resolution and its disambiguation binding (§5, §6, §10); the glossary index contract and locator law (GLOSSARY §1, §2) |

## Subject under test

The subject is the standards at commit `3824752` on `tenant/claude/c3-v3`,
whose digests are recorded under [a_c/set-5/](../../../a_c/set-5/README.md).
They are encoded as program `urn:stdo-3:claude:program:a-c-text:set-5`,
with canonical digest
`sha256:b12b31216456f375c2a2e24aefbd16c897d92c1a7b469b50c52ee89b450e4a42`
and zero diagnostics against the pinned Axiom Indexer. The actor receives
the bytes of the nine frame files projected from that program:

| Frame file | SHA-256 | Bytes |
|---|---|---|
| `a_c/set-5/projection-carrier-retention-materialized.json` | `16bc90d75e969e44e238f1dc13059c7b3aabbe5247ae3e442e8da0f00e78c4eb` | 55,905 |
| `a_c/set-5/projection-release-and-successor-materialized.json` | `42a33da6a01e9c8740fcc420cb75cda2875a4706ce304037ce97507cad9acbf4` | 62,813 |
| `a_c/set-5/projection-identity-scoped-materialized.json` | `2148de3efe8ab0f838faf8e53df05b25f43949078e47d3bec4a2552fa61077c1` | 37,612 |
| `a_c/set-5/projection-design-gate-materialized.json` | `82bbd09ca1b4922f543d4328c4c33fdeafc03dd0b643494c0c21d4317251c663` | 83,252 |
| `a_c/set-5/projection-odd-closure-materialized.json` | `ec44026052563a4ce951051048cec44ecf35af8908b13e0e999f07089e5e2ea2` | 47,936 |
| `a_c/set-5/projection-traversal-lineage-materialized.json` | `6c017de3956ed9ff2bd9ff1a82dfe872ebe656f3ceb9665ad9bd5345164d788a` | 62,598 |
| `a_c/set-5/projection-ux-replay-materialized.json` | `c923a607c7faea6bbfeb993270a7524988ef83d8e9abd8167c0d639b0730f69f` | 46,256 |
| `a_c/set-5/projection-world-model-cut-materialized.json` | `b85f70562d366be3eaed846d21b49ee30751f3c085497ba96e7a956df674d9e7` | 38,558 |
| `a_c/set-5/projection-bind-and-resolve-materialized.json` | `871c6d663f666cdf5ba2a6114ac815bbc4ac24b3ea985caf4203892aedc9ffda` | 53,088 |

The W22 commit `731c24e` introduced the frame files, and a run names that
commit in the runs table. The candidate `bootstrap` frame in the same
directory is not part of this fixture. The set-5 program is a partial
encoding: what each frame carries is recorded in the set-5 README. The
program increment, the frames and this fixture were authored by one Writer
activation and its forks.

## Fixture material

- [CARD.md](CARD.md) (`237ea8f9…47b23`, 455 bytes): a byte-identical copy
  of F-02's routing card, itself a copy of F-01's. It carries no method
  content.
- [TASK-A.md](TASK-A.md) (`c58fadb1dab3…`, 3,482 bytes): project
  `docs-site`, the F-02 task C subject with the goals carrier stated. Work 1 is an exact one-run instruction with a
  complete admission record; Work 2 is a goals-wave outcome needing state
  across three sessions, with a self-labelled `admitted` contract naming
  the conversation as its result surface, a board card and no admission.
  The agent holds no ticket-state authority. The actor names the carrier
  row, the contract state, whether execution may begin, and where an
  obligation that must survive is kept.
- [TASK-B.md](TASK-B.md) (`a7efdc7c91c5…`, 3,536 bytes): repository
  `acme-tools` moving from an unqualified ref profile to project
  namespaces. Two publication options for a fix (moving an RC tag; new
  qualified tags plus force-moving the old selector), a publication record,
  an accept-then-retag message, a consumer pinned to an older cut with a
  one-invocation adopt job, and four predecessor claims.
- [TASK-C.md](TASK-C.md) (`f14324746632…`, 3,093 bytes): product
  `field-notes` on engine `runloop`. Four identity uses (engine rewriting
  domain ids, one id in two scopes flattened, a family and a version used
  as identities, a retired id reused) and four authority events (a label
  rename, a wrapper exposing a proxy, a proxied acceptance recorded under
  the grantor, self-review claimed as independent).
- [TASK-D.md](TASK-D.md) (`dea2248562b3…`, 3,437 bytes): product
  `parcel-lockers`. An unchanged-semantics refactor of an accepted
  boundary, and a new boundary with an undecided owner, retained code, a
  substrate lacking a needed capability, duplicated lifecycle across two
  atoms, a second state truth and an incomplete three-view asset.
- [TASK-E.md](TASK-E.md) (`216eeebc3d16…`, 3,099 bytes): product
  `parcel-router`. Four evaluated edges, a three-function line whose last
  step needs the first step's output, and two negative proofs (a
  constructed event; the public path with a legacy endpoint unexercised).
- [TASK-F.md](TASK-F.md) (`c13f1d2f836d…`, 2,618 bytes): product
  `inventory-sync`. A cause recorded from timing, an in-place edit of an
  event, a lineage edge with a wrong source sort, a precedence coordinate
  used as a decision, and three stopped occurrences.
- [TASK-G.md](TASK-G.md) (`41cdc23dec1f…`, 3,204 bytes): product
  `tidewatch`. Three behaviours of one surface (through the membrane, in
  the view, in a component effect), one replay proof covering one of two
  interaction families, a debug pane with a partial exemption record, and
  a closure claim.
- [TASK-H.md](TASK-H.md) (`9bdffc03440e…`, 2,918 bytes): builder project
  `harbourworks`. A complete cut and a draft cut with empty, missing and
  unsourced surfaces, one attribute with a ledger entry and one without,
  and an in-place edit of a published cut.
- [TASK-I.md](TASK-I.md) (`ad14721ac74b…`, 3,695 bytes): product
  `clinic-booking`. A product definition with missing and defective
  relations, a term defined differently in two owned contexts, an
  incomplete disambiguation binding, a glossary whose row order a
  developer used to choose a meaning, and a row pointing at a missing
  file.

Every subject is invented for this fixture and is evidence about no
product. Each subject states facts, not the diagnosis the task asks for.

## Instrument invocations

The instrument is [bounded_step.py](../../instruments/bounded_step.py) at
`f92ca26b3e4fda953d8732f0665861d54a9121df67451ea90f981555c6ffe81d`, the
version F-01 and F-02 use. Each task is one step. Run from the tenant
root `specification_methodology/v3/build_tenants/claude/`. The instrument
starts the actor in a fresh empty directory outside any repository.

```sh
python3 -I qualification/instruments/bounded_step.py --cap 400000 \
  --run-dir qualification/runs/<run-id> --step-id A-001 \
  --card qualification/cases/F-03/CARD.md \
  --block "METHOD carrier-retention=a_c/set-5/projection-carrier-retention-materialized.json" \
  --block "TASK=qualification/cases/F-03/TASK-A.md" \
  --model sonnet

python3 -I qualification/instruments/bounded_step.py --cap 400000 \
  --run-dir qualification/runs/<run-id> --step-id B-001 \
  --card qualification/cases/F-03/CARD.md \
  --block "METHOD release-and-successor=a_c/set-5/projection-release-and-successor-materialized.json" \
  --block "TASK=qualification/cases/F-03/TASK-B.md" \
  --model sonnet

python3 -I qualification/instruments/bounded_step.py --cap 400000 \
  --run-dir qualification/runs/<run-id> --step-id C-001 \
  --card qualification/cases/F-03/CARD.md \
  --block "METHOD identity-scoped=a_c/set-5/projection-identity-scoped-materialized.json" \
  --block "TASK=qualification/cases/F-03/TASK-C.md" \
  --model sonnet

python3 -I qualification/instruments/bounded_step.py --cap 400000 \
  --run-dir qualification/runs/<run-id> --step-id D-001 \
  --card qualification/cases/F-03/CARD.md \
  --block "METHOD design-gate=a_c/set-5/projection-design-gate-materialized.json" \
  --block "TASK=qualification/cases/F-03/TASK-D.md" \
  --model sonnet

python3 -I qualification/instruments/bounded_step.py --cap 400000 \
  --run-dir qualification/runs/<run-id> --step-id E-001 \
  --card qualification/cases/F-03/CARD.md \
  --block "METHOD odd-closure=a_c/set-5/projection-odd-closure-materialized.json" \
  --block "TASK=qualification/cases/F-03/TASK-E.md" \
  --model sonnet

python3 -I qualification/instruments/bounded_step.py --cap 400000 \
  --run-dir qualification/runs/<run-id> --step-id F-001 \
  --card qualification/cases/F-03/CARD.md \
  --block "METHOD traversal-lineage=a_c/set-5/projection-traversal-lineage-materialized.json" \
  --block "TASK=qualification/cases/F-03/TASK-F.md" \
  --model sonnet

python3 -I qualification/instruments/bounded_step.py --cap 400000 \
  --run-dir qualification/runs/<run-id> --step-id G-001 \
  --card qualification/cases/F-03/CARD.md \
  --block "METHOD ux-replay=a_c/set-5/projection-ux-replay-materialized.json" \
  --block "TASK=qualification/cases/F-03/TASK-G.md" \
  --model sonnet

python3 -I qualification/instruments/bounded_step.py --cap 400000 \
  --run-dir qualification/runs/<run-id> --step-id H-001 \
  --card qualification/cases/F-03/CARD.md \
  --block "METHOD world-model-cut=a_c/set-5/projection-world-model-cut-materialized.json" \
  --block "TASK=qualification/cases/F-03/TASK-H.md" \
  --model sonnet

python3 -I qualification/instruments/bounded_step.py --cap 400000 \
  --run-dir qualification/runs/<run-id> --step-id I-001 \
  --card qualification/cases/F-03/CARD.md \
  --block "METHOD bind-and-resolve=a_c/set-5/projection-bind-and-resolve-materialized.json" \
  --block "TASK=qualification/cases/F-03/TASK-I.md" \
  --model sonnet
```

The cap is 400,000 bytes of whole context per step, and the model is
`sonnet`. A repeated trial uses the step ids A-002, B-002 and so on,
always five characters, so the header line stays the length the dry run
measured.

The instrument measures the whole context in bytes before any actor
exists, logs the `measured` event with every component's SHA-256, and
refuses a context over the cap without starting an actor. A run record is
admissible only when its `measured` events carry the frame file digests
above. A different digest is a different subject.

## Dry-run measurement

The dry runs were made at design time with `--dry-run`, from this fixture
at these digests, into a scratch run directory outside the repository. No
actor was started.

| Step | Total bytes | System | Card | METHOD block | TASK block | Header |
|---|---|---|---|---|---|---|
| A-001 | 60,179 | 182 | 455 | 55,943 | 3,500 | 99 |
| B-001 | 67,149 | 182 | 455 | 62,855 | 3,554 | 103 |
| C-001 | 41,493 | 182 | 455 | 37,648 | 3,111 | 97 |
| D-001 | 87,469 | 182 | 455 | 83,284 | 3,455 | 93 |
| E-001 | 51,815 | 182 | 455 | 47,968 | 3,117 | 93 |
| F-001 | 66,008 | 182 | 455 | 62,636 | 2,636 | 99 |
| G-001 | 50,236 | 182 | 455 | 46,286 | 3,222 | 91 |
| H-001 | 42,264 | 182 | 455 | 38,594 | 2,936 | 97 |
| I-001 | 57,573 | 182 | 455 | 53,125 | 3,713 | 98 |

All nine fit the cap; the total over nine steps is 524,186 bytes. The
`measured` events carried the frame digests `16bc90d75e96…`,
`42a33da6a01e…`, `2148de3efe8a…`, `82bbd09ca1b4…`, `ec4402605256…`,
`6c017de3956e…`, `c923a607c7fa…`, `b85f70562d36…` and `871c6d663f66…`, the
card digest `237ea8f915ca…`, and instrument SHA-256 `f92ca26b3e4f…`.

## Expectations

Expectations: written by an independent context before any run; see EXPECTATIONS.md.

## Assessment

Under a review Jim authorises, an assessor other than the author reads the
run directory at a named commit after the expectations exist. The assessor
returns a review result per EVALUATION §4 over the expectations, judging
each record against the member's relations as the set-5 program encodes
them and the costs as logged. The assessor makes no repair. The author's
structural check of a record is mechanical evidence, not assessment.

## Runs and assessments

| Run | Operator | Record | Assessment |
|---|---|---|---|
| none | | | |
