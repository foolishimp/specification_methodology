# Actual-use trial design, iteration 4 (criterion 4, D5 option A)

The product owner's instruction of 2026-10-15 ("we shouldnt hold back",
after "go max") is read by this line as funding D5 option A: isolated
Fable actors use this candidate's frames, with no external spend. This
file fixes the design before any actor runs. It adapts the iteration 3
design ([C3-ITER3 PLAN §5](../../C3-ITER3/PLAN.md#5-trial-design)) and
the five elements selected from the Codex protocol (port C2,
[ports.md](../ports.md)). It is this line's own criterion-4 evidence; the
head-to-head comparison uses the pen's shared protocol, which this trial
neither anticipates nor replaces.

## 1. What is tested

Criterion 4 of the C3 contract: each selected task of a member has a
frame that fits the declared limits, supplies sufficient relevant
material and excludes irrelevant material; a fresh actor uses that frame,
its subject and declared acquisition routes and tools correctly; its work
is judged against expectations specified independently of the author;
fit is supported, not asserted. The ratified text adds: curated-frame use
and ordinary discovery are reported separately; a desk trace or an
unmeasured success does not complete the criterion; a subagent is a
possible mechanism, not proof of freshness or fit by its label.

## 2. Tasks

One task per frame, twelve in all: the `task` sentence recorded for the
frame in `standards/frames/FRAME_INPUTS.json`, applied to one concrete
fixture. The fixture (the situation's facts, the subject, the grant the
actor holds, and what it is asked to return) is written by the
expectation writer of §4, not by the candidate's author.

| Task | Frame | Kind |
|---|---|---|
| TT-01 | `rf-task-a` | declare and activate one frame; minimal result |
| TT-02 | `rf-task-b` | coverage ledger |
| TT-03 | `ac-task-a` | transformation record |
| TT-04 | `traversal-task-f` | causal, correction, lineage and proof claims |
| TT-05 | `eb-task-d` | Executive revalidation in the coordinated branch |
| TT-06 | `dm-task-d` | refactor inside and across a boundary |
| TT-07 | `configuration` | propose a configuration |
| TT-08 | `binding` | build-tenant binding |
| TT-09 | `stale-summary` | resume from a stale summary |
| TT-10 | `bootstrap` | enter the method for an unspecified task |
| TT-11 | `acceptance-release` | accept or release |
| TT-12 | `member-build-assess` | build or assess one member |

## 3. Arms

| Arm | The actor receives | Purpose | Runs |
|---|---|---|---|
| A0 control | the neutral card, the task and the fixture; no method text | calibrates the `M` items: an item any control run passes is decided by the fixture, not the method | 12 × 1 |
| A1 frame | the neutral card, the frame's bytes, the task and the fixture; no tools | criterion-4 evidence for curated-frame use | 12 × 2 |
| A3 routes | as A1, plus read-only access to an isolated copy of the frozen `standards/` directory, with the instruction to follow only the frame's `Source:` lines and the links in it | the declared acquisition routes in use; supplied, cumulative and active bytes | 4 × 1 (TT-01, TT-05, TT-09, TT-11) |
| A5 discovery | the neutral card, the task, the fixture, and read-only access to the same isolated copy entered only at its `README.md` | ordinary discovery, reported separately from curated use, never standing in for it | 4 × 1 (the same four) |

The neutral card states the role (an actor asked to do one task), the
return form, the limits, and nothing about the method.

## 4. Roles and independence

- **Expectation writer.** One fresh Fable activation per task. It
  receives the task sentence and the owning sections of the frame's
  routes (the sections, not the frame), writes the fixture and the
  expectation items, and tags each item `M` (the method decides it) or
  `F` (the fixture states it). It never sees a frame or an actor's work.
  Its output is hashed and the hash recorded in the ledger before any
  actor runs.
- **Actor.** One fresh Fable activation per run, `general-purpose`,
  never a fork. It receives only what its arm lists.
- **Grader.** One fresh Fable activation per task. It receives the
  expectations and the returns of every run of that task with the arm
  labels removed and the order shuffled, and returns one closed value per
  item per run: `satisfied`, `falsified` or `indeterminate`, with the
  evidence quoted.
- The candidate's author (the Executive of this line) writes none of the
  fixtures, expectations or grades. All three roles are Claude-family;
  the evidence is same-family working evidence under the exception of
  CONSTRUCTION_BINDING §1, and not the cross-family evidence the C3
  contract requires for acceptance.

## 5. Freshness and fit: what is established and what is disclosed

A subagent of this harness starts with no private context of this
session and no conversation history (established by construction of the
mechanism: a `general-purpose` agent receives only its prompt). It may
receive the harness's own system prompt and the repository instruction
files of its working directory, which the actor does not select. These
are disclosed, not denied:

- the repository instruction files reachable from the working directory
  of this session total 15,345 bytes (`/Users/jim/src/apps/CLAUDE.md`
  7,062; `specification_methodology/CLAUDE.md` 2,216; the worktree's
  `CLAUDE.md` 1,991; `v3/CLAUDE.md` 4,076); none names a frame, a task or
  an expectation;
- each actor is asked, as the first item of its return, to state whether
  it received any instruction beyond the card, and to quote the first
  line of each such instruction; this is the actor's disclosure and is
  recorded as such, not as proof.

Fit is supported, never asserted, by a recorded upper bound per run:
supplied bytes (card, frame, task, fixture, measured) plus the 15,345
bytes above plus the actor's reported acquisition (A3, A5), under the
declared context capacity of 150,000 bytes for a frame and 300,000 bytes
of whole input. The harness system prompt is an unmeasured component; a
run's fit judgment is therefore `indeterminate` in the strict sense of
ACTIVATION §2 step 3 unless the actor reports a measured excess
(`falsified`) or the harness discloses its prompt size. This limit is
stated in the results.

## 6. Limits per run

Context: at most 300,000 bytes of whole input, 150,000 for the frame; a
run whose supplied bytes exceed the cap is refused before it starts,
never truncated. Wall time: 20 minutes. Spend: tokens of this session's
allowance; no external spend. Each run records its supplied bytes and,
for A3 and A5, cumulative acquired bytes and the largest active set.

## 7. Grading and attribution

Criterion 4 is judged on `M` items only. An `M` item that any A0 run
passes is re-tagged `F`, excluded from attribution and reported. A
failed `M` item in A1 is attributed by triangulation to frame content,
owner text, task wording or actor application, by the Executive after
grading, and the attribution is a finding, not a grade. A1 is the
curated-frame measure; A5 is the ordinary-discovery measure; they are
reported side by side and neither stands in for the other. No earlier
run of any iteration is reused.

## 8. Records

`trial/expectations/TT-nn.md` (writer output, hashed before runs),
`trial/runs/TT-nn/<arm>-<k>.md` (the exact card, the supplied bytes,
the actor's full return), `trial/grades/TT-nn.json`, `trial/RESULTS.md`.
