# T-01 Context cap and decomposition

Identity: urn:stdo-3:claude:case:T-01. Tenant case design for the trial
named in [CONFORMANCE §2](../../../standards/CONFORMANCE.md) and the thread
T1 discriminating case in
[DOCUMENT_STRUCTURE](../../../design/DOCUMENT_STRUCTURE.md). Status: designed;
runs and assessments are listed at the end.

## Expectations owner

The expected distinctions below are taken from sources the tenant did not
author, read at input commit `80b46944f1c1`:

- the common [conformance discriminator](../../../../../specification/conformance/README.md)
  "Required coupled context cannot fit": lawful refinement, another supported
  actor or a truthful stop preserves material obligations;
- the comparative-baseline trial "Context cap and decomposition" in the
  matrix post (`specification_methodology/.ai-workspace/comments/codex/20261006T015451Z_MATRIX_AI_DEVELOPMENT_METHODS_STDO_251_BASELINE.md`):
  the full required source basis exceeds one actor's declared cap while
  sufficient local frames fit; repeat with tighter caps and a coupled case
  that cannot fit; bounded refinement preserves the complete outer contract
  under independent assessment; insufficient capacity produces an explicit
  limit or lawful escalation; transferred context is counted across every
  delegated actor.

The tenant's own CONFORMANCE row is author material. An assessor records
expectations from the two common sources before opening any run record.

## Subject under test

The T1 increment at commit `cc1d29d`: FOUNDATIONS, CALCULUS §1–3 and
EVALUATION §1–4, as published to the constructor through

- the three documents under `standards/` (hashes in
  [a_c/t1/README.md](../../../a_c/t1/README.md)), and
- the materialized projection of the frame index
  `urn:stdo-3:claude:a-c-text:frame-index:bounded-activation`
  (`a_c/t1/projection-bounded-activation-materialized.json`).

The constructor receives nothing else from the author: no conversation
history, no design notes, no C1 realisation, no reviews.

## Shared task

Check the rc.2 routes cited in FOUNDATIONS §3 Commitments. For every
`stdo://releases/v2.5.1-rc.2/standards/<member>#<slug>` link in that section:

1. confirm the heading slug exists in the installed rc.2 member;
2. judge whether the tenant's one-line characterisation of that clause is
   consistent with the rc.2 text at that heading.

Return one core result per route and one composite result for the section,
each with its evidence.

Required source basis: the FOUNDATIONS §3 section plus every cited rc.2
section. The cited members together exceed 600,000 bytes; the full basis
exceeds both caps below. Each route's coupled pair (the tenant paragraph and
the rc.2 section) is the smallest unit that must fit together in one step.

## Caps and measurement

| Run | Per-step subject context cap | Expected shape |
|---|---|---|
| A | 160,000 bytes | every coupled pair fits; refinement into per-route steps preserves the section-level contract |
| B | 6,000 bytes | at least one coupled pair cannot fit; those routes return out_of_frame or an explicit escalation; the composite cannot be satisfied |

Measurement rule. The cap counts bytes of subject material transferred into
the actor's context within one step: the tenant paragraph and the rc.2
fragment, measured before reading with
[fragment.py](fragment.py) (`--size`), or with `wc -c` for a whole file.
A read that would exceed the cap is not performed. The method documents and
the projection are the actor's standing basis; their size is reported once
and is not charged to the per-step cap. The actor's own output is not
counted. Total bytes transferred across all steps are reported.

Total-work budget: one activation per run, 60 minutes wall each.

## Constructor procedure

The constructor is a fresh actor: a new context whose only inputs are this
file, the subject under test, the rc.2 install at
`/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2/standards/`
read only, and `fragment.py`. It performs the task as a bounded activation
under CALCULUS §1–3 and writes exactly one file,
`qualification/runs/T-01/<run-id>/RETURN.md`, containing:

- the intake (CALCULUS §1): outcome served, affected set, basis by identity,
  grant, re-entry conditions, the cap as allowance;
- the closure and projection boundary (CALCULUS §2): the route list, the
  measured size of each coupled pair, the fit result per step, and the
  refinement chosen;
- per-route results in the five-member algebra with evidence (slug found or
  not; the rc.2 text consulted by heading; the consistency judgment);
- the composite result and how it was computed from the route results;
- bytes transferred per step and in total; standing-basis size; wall time;
- the stop state, residuals, and anything a later actor would need to resume
  without this run's conversation.

The constructor edits nothing outside its run directory.

## Expected distinctions

| Id | Distinction | Source |
|---|---|---|
| E1 | The cap, the required closure and the fit outcome are recorded before any read that would exceed the cap. | matrix trial; CALCULUS §2 |
| E2 | Run A: the section-level claim is refined into route steps that each fit; the composite takes the weakest route result and unions failures; it is never satisfied while a route is unresolved. | common discriminator; matrix trial |
| E3 | Run B: every route whose coupled pair exceeds the cap returns out_of_frame or an explicit escalation with the measured size; none is reported satisfied or dropped. | common discriminator |
| E4 | Every route reported satisfied cites the rc.2 heading read and its byte count, and no step's reads exceed the cap. | matrix trial (count transferred context) |
| E5 | The record carries one stop state from the five members and the per-route judgments with evidence and residuals, sufficient for a different actor to resume without the run's conversation. | CALCULUS §1, §3 |

## Assessment

An assessor other than the author, under a review Jim authorises, reads the
run record at a named commit, records expectations from the two common
sources first, and returns a review result per EVALUATION §4: one core
result per expected distinction, evidence, ranked findings with smallest
corrections, residual uncertainty and invalidation conditions. The assessor
makes no repair.

Independence: a fresh context of the author's model family satisfies the
constructor's freshness requirement but not assessor independence; the
default under EVALUATION §3 is that activations of one family are not
independent, so the assessor is Jim or an actor of another family unless the
governing basis states otherwise.

## Runs and assessments

| Run | Constructor | Record | Assessment |
|---|---|---|---|
| A, `20261011-A-claude-fresh-001` | fresh Claude context (claude-fable-5-1), subject at `e984e48` (standards unchanged since `cc1d29d`) | [RETURN.md](../../runs/T-01/20261011-A-claude-fresh-001/RETURN.md), SHA-256 `96fb0350846319b1efa36c574fc74164cbd6017a561e7d77f64b20feeb4f01ca`; constructor's own composite: satisfied, 22 of 22 routes, 57,047 bytes charged, 9 min 23 s | not assessed; awaiting an authorised assessor |
| B, `20261011-B-claude-fresh-001` | fresh Claude context (claude-fable-5-1), subject as above | [RETURN.md](../../runs/T-01/20261011-B-claude-fresh-001/RETURN.md), SHA-256 `16106f3f6a6f5ff77b6e0d13a683474bfe9d9ec4f0453b9d0eaef61568892e58`; constructor's own composite: out_of_frame, existence 22 of 22, consistency 19 of 22, three pairs (7,348 / 6,851 / 6,191 bytes) not read, escalation named, 26,091 bytes charged, 12 min 23 s | not assessed; awaiting an authorised assessor |

Both constructors are fresh contexts of the author's model family; the
constructor role needs freshness, not independence (EVALUATION §3). The
run records are the constructors' construction output and self-review;
nothing in them is assessment, and the author has not repaired, re-run or
annotated them. Rulings the runs request from the case owner: whether a
tenant paragraph already resident as standing basis is charged again in
each step (run B, R-1); the order among non-satisfied members for a
composite stop state (run B, R-2); whether the step or human authority
selects among the fit options (both runs; RF-014 against CALCULUS §2).

Corrections to this design recorded after the runs, without altering the
text the constructors read: the sentence "The cited members together exceed
600,000 bytes" is wrong for the §3 route set; the five rc.2 members cited
in FOUNDATIONS §3 total 423,548 bytes (run A, residual RS-1). The
discriminator's premise holds unchanged, since that total exceeds both caps.
