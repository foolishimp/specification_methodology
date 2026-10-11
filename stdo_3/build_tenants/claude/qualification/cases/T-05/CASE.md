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
| A, `20261012-A-claude-fresh-001` | fresh Claude context (claude-fable-5-1); subject at `c539daa`; step actors claude-sonnet-5-5 through the instrument; order its own | [RETURN.md](../../runs/T-05/20261012-A-claude-fresh-001/RETURN.md), SHA-256 `d8d14bf9642f398786ef2e3872fdcc66c4ee9b0dcf0ed4055b1b7edcf6359e26`; `work_state/lifecycle.jsonl` 36 events, the fixture's 19 first and unchanged; constructor's own composite: out_of_frame over 23 of 23 covered (21 satisfied, R09 out_of_frame, R10 indeterminate as P4a's actor judged); five completed steps reused after a recorded applicability check, none re-run, eight dry-run re-measurements; three draft claims disposed; P4b-2 closed as interrupted with its effect unknown before any repetition, R14 and R15 covered by a new step; 3 actor starts (P4b-2-resume, P5, P6), 37,154 context tokens, USD 0.171; stop state out_of_frame; 7 min 41 s | not assessed; awaiting an authorised assessor |
| B, `20261012-B-claude-fresh-001` | as above; order prescribed (P6, P5, then the interrupted routes) | [RETURN.md](../../runs/T-05/20261012-B-claude-fresh-001/RETURN.md), SHA-256 `0642f7dc556194d69dc1acf89a3c9fab6be945241309cdf5ad48bd763b1fba17`; `work_state/lifecycle.jsonl` 28 events, the fixture's 19 first and unchanged; constructor's own composite: out_of_frame over 23 of 23 covered (21 satisfied, R09, R10 as judged); five steps reused after a recorded check, none re-run; three draft claims disposed; P4b-2 closed as interrupted with its effect unknown, then R14 and R15 covered by a new step last, as prescribed; 3 actor starts in the order P6, P5, P4b-2b, USD 0.102; stop state candidate_ready with the contract's predicate out_of_frame; 9 min 57 s | not assessed; awaiting an authorised assessor |

The run records are the constructors' construction output and self-review;
nothing in them is assessment, and the author has not repaired, re-run or
annotated them. The author ran the structural check over both lifecycle
logs (chronology, caps, sizes, echoes, file digests): no problems; the
fixture directory is byte identical to its committed state after both
runs. Mechanical evidence only.

Corrections to this design recorded after the runs, without altering the
text the constructors read: the draft carries a third unsupported claim
the case owner did not declare. Its step table marks P4a "done, 2
satisfied" while `steps/P4a.out.md` records R09 out_of_frame and R10
indeterminate; the owner wrote the row from the plan, not from the file.
Both constructors detected it alongside the two declared claims. The
seeded-conditions list above should read three claims, not two.

Observations the constructors recorded, carried here without repair: the
instrument's own digest is not logged by the instrument, so its identity
at production rests on the current file (both runs); the rc.2 sections of
the reused steps were authenticated against the logged block digests by
re-measurement, since the install may not be opened (both); the P4a
judgments stand as a candidate finding against FOUNDATIONS P4a's
attribution of RF-010, and any repair of P4a changes the section digest
and re-opens all 23 routes under the contract (both handoffs); the
possible charge of the killed call is bounded at about USD 0.06 and
unknowable from the workspace (both).
