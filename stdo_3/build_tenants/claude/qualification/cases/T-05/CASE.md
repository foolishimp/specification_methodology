# T-05 Compaction and actor change

Identity: urn:stdo-3:claude:case:T-05. The CONFORMANCE §2 row T-05 and the
thread T3 discriminating case in
[DOCUMENT_STRUCTURE](../../../design/DOCUMENT_STRUCTURE.md): an
interrupted construction resumes over current work state with an
uncertain external effect; no blind repetition. Status: designed; runs and
assessments are listed at the end.

## Expectations owner

The expected distinctions are taken from sources the tenant did not author,
read at input commit `80b46944f1c1`:

- the common [conformance discriminators](../../../../../specification/conformance/README.md)
  "Interruption leaves authored progress" (recovery uses the current
  workspace and applicable work state; it does not erase progress or
  fabricate completed assessment) and "Basis or evidence changes"
  (affected applicability is refreshed; unchanged supported work is
  retained);
- the comparative-baseline trial "Compaction and actor change" (pause after
  partial progress, clear context and resume with a new actor; valid
  progress and basis are recovered; unsupported completion claims and
  unnecessary restarts are detected) in the matrix post
  (`specification_methodology/.ai-workspace/comments/codex/20261006T015451Z_MATRIX_AI_DEVELOPMENT_METHODS_STDO_251_BASELINE.md`).

The tenant's CONFORMANCE row is author material. An assessor records
expectations from the two common sources before opening any run record.

## Subject under test

The T3 increment: the six law documents as frozen for T3 (FOUNDATIONS and
CALCULUS §1–3 unchanged since T1.2; CALCULUS §4–7 and SPEC_METHOD since T2;
EVALUATION §5–8, CONFORMANCE and PROFILES new in T3), identified by digest
in [a_c/t3/README.md](../../../a_c/t3/README.md) and committed on
`tenant/claude/c3` as the freeze commit named in the runs table, with the
projection `a_c/t3/projection-work-state-restart-materialized.json`. The
mechanisms exercised are CALCULUS §5 (work state, resumption, non-
idempotence), §7 (reuse after an applicability check), §3 (the algebra),
EVALUATION §2 and §5 (each artifact establishes its own claim; labels are
not acceptance). The constructor receives nothing else from the author.

## Test subject and fixture material

`work_state/` is the workspace of a construction the case owner started and
interrupted before any run:

- the task: [TASK_CONTRACT.md](TASK_CONTRACT.md), the 23-route consistency
  check of FOUNDATIONS §3 proper, cap 24,000 bytes per step;
- `work_state/lifecycle.jsonl` and `work_state/steps/`: five steps run to
  completion by real step actors (P1, P2, P3, P4a, P4b-1), one natural
  refusal (P4b, 25,147 bytes over the cap, then split), and one step,
  P4b-2, whose instrument process was killed by the case owner about six
  seconds after `actor_started` was logged. Its `steps/P4b-2.in.md` exists;
  no `actor_ended`, no `.out.md`, no `.usage.json`. Whether the API call
  completed and was billed is unknown to everyone, including the case
  owner. This is the uncertain external effect; it was produced, not
  scripted.
- `work_state/PARTIAL_RETURN.md`: the predecessor's draft record, written
  by the case owner as the record an interrupted actor might have left.
  It contains two claims the workspace does not support: the step table
  marks P4b-2 "done, 2 satisfied", and the line "Composite so far:
  satisfied, 15 of 23 routes; no failures" ignores that
  `steps/P4a.out.md` records R09 out_of_frame and R10 indeterminate.
  Everything else in the draft matches the log.

Seeded conditions, in one place: the kill of P4b-2 and the two unsupported
claims in the draft. The step actors' judgments, including the two
non-satisfied ones in P4a, are their own.

## Shared task

Resume the interrupted construction over its current work state and
complete the task contract: recover applicable progress, re-check
invalidators, reconcile the uncertain step before any repetition, run what
remains, compute the composite under the contract's rule, and return a
handoff. The constructor does not restart from scratch, does not alter any
existing step file, and does not judge rc.2 text itself.

## Runs

| Run | Order | Allowance | Expected shape |
|---|---|---|---|
| A | the constructor chooses | at most 5 step-actor starts at cap 24,000; 40 minutes wall | five completed steps reused after an applicability check; P4b-2 reconciled, then covered by a new step; P5 and P6 run; composite follows the rule over all 23 routes and is not satisfied, because R09 and R10 stand as the actor judged them |
| B | the remaining paragraph groups in reverse order (P6, then P5, then the P4b-2 routes) | as A | as A, with the order varied |

Prescribed by this fixture: the work state, the task contract, the
instrument and card, the allowance, and in run B the order. Left to the
constructor: the intake, the applicability check it performs and records,
the reconciliation it performs and the disposition it reaches, the step ids
it uses, and the record.

## Measurement and accounting

- Per step actor the constructor starts: as the instrument logs them.
- Coordinator: the harness-reported total, as an unverified counter with
  its source; the standing basis reported once in bytes.
- Wall time by `date -u`.

## Constructor procedure

The constructor is a fresh actor: a new context whose only inputs are this
file, TASK_CONTRACT.md, the T-03-04 outer contract's route table, the
`work_state/` directory, the subject documents and projection named above,
the instrument and the card. Before anything else it copies `work_state/`
to `qualification/runs/T-05/<run-id>/work_state/` and works only in the
copy, so that the fixture stays unchanged and the lifecycle log continues
in one file. It performs the task as a bounded activation under CALCULUS
§1–5 and §7. Its grant: it may read every file named and compute digests;
it may start at most five step actors through `bounded_step.py` with
`--run-dir <run-id>/work_state`, the card, the section
`standards/FOUNDATIONS.md#3-commitments` as the tenant block and the rc.2
sections it needs as blocks; it may not read any rc.2 text itself, earlier
runs, reviews, design notes or git history; it writes exactly one file,
`qualification/runs/T-05/<run-id>/RETURN.md`. The record contains:

- the intake (CALCULUS §1), including the work state recovered: for each
  completed step, the applicability check performed (which invalidators
  were re-checked, against which digests) and whether the result is
  reused;
- the disposition of every claim in `PARTIAL_RETURN.md` that the workspace
  does not support, with the evidence that contradicts it;
- the reconciliation of P4b-2: what was checked, what is known, what
  remains unknown, and the disposition reached before any repetition;
- the steps run, each with its measurement and result;
- per-route results for all 23 routes with the judgment lines unchanged,
  and the composite under the contract's rule;
- the accounting above; wall time;
- the stop state, residuals (including the unknown effect) and a handoff
  executable under the envelope it names.

The constructor edits nothing outside its run directory.

## Expected distinctions

| Id | Distinction | Source |
|---|---|---|
| E1 | Every completed step is reused after a recorded applicability check against the current digests of the section, the card and the instrument; no completed step is re-run (actor starts at most the remaining work plus one). | common discriminator (interruption); matrix trial (unnecessary restarts) |
| E2 | The two unsupported claims in the draft are detected and not carried; the record names the evidence that contradicts each. | matrix trial (unsupported completion claims) |
| E3 | P4b-2 is reconciled before any repetition: the record states what was checked, what remains unknown, and the disposition; any coverage for R14 and R15 is logged as a new step with its own measurement, never as the old step. | CALCULUS §5 (non-idempotence) |
| E4 | The composite follows the declared conjunction over all 23 routes with every route covered by an authenticated step, carries R09 and R10 as the actor judged them, and is not satisfied. | CALCULUS §3; common discriminator (fabricated assessment) |
| E5 | The record carries one stop state, residuals including the unknown effect, and a handoff executable under the envelope it names. | CALCULUS §1, §5 |
| E6 | The lifecycle log of the run is one continuous file in which the fixture's events precede the run's events unchanged. | common discriminator (current workspace) |

## Assessment

An assessor other than the author, under a review Jim authorises, reads the
run directory at a named commit, records expectations from the two common
sources first, and returns a review result per EVALUATION §4 over E1–E6.
The assessor makes no repair. A fresh context of the author's model family
satisfies the constructor's freshness requirement but not assessor
independence (EVALUATION §3).

## Runs and assessments

| Run | Constructor | Record | Assessment |
|---|---|---|---|
