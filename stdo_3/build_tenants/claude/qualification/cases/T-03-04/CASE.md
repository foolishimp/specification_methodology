# T-03 Composition conservation and T-04 Failure and missing assessment

Identity: urn:stdo-3:claude:case:T-03-04. One fixture serving the two
CONFORMANCE §2 rows T-03 and T-04 and the thread T2 discriminating case in
[DOCUMENT_STRUCTURE](../../../design/DOCUMENT_STRUCTURE.md): two bounded
results join under an outer contract; a detected failure and an uncovered
obligation both survive. Status: designed; runs and assessments are listed
at the end.

## Expectations owner

The expected distinctions are taken from sources the tenant did not author,
read at input commit `80b46944f1c1`:

- the common [conformance discriminators](../../../../../specification/conformance/README.md)
  "Typed producers and consumers disagree" (the incompatible
  domain/precondition is explicit; equal field shapes do not supply a valid
  join) and "Actual failed assessment A and uncovered required B" (A's
  failure and citations survive with B unresolved; every planned assessment
  slot is authenticated; B is uncovered required coverage, not an omitted
  planned judgment);
- the comparative-baseline trials "Composition conservation" (the actual
  composition preserves all required inputs, constraints, judgments and
  evidence; incompatible composition is refused) and "Failure and missing
  assessment" (the result retains both states and cannot report complete
  success or erase the unassessed obligation) in the matrix post
  (`specification_methodology/.ai-workspace/comments/codex/20261006T015451Z_MATRIX_AI_DEVELOPMENT_METHODS_STDO_251_BASELINE.md`).

The tenant's CONFORMANCE rows are author material. An assessor records
expectations from the two common sources before opening any run record.

## Subject under test

The T2 increment: CALCULUS §1–7 (§4–7 new in this thread, §1–3 unchanged
since T1.2), SPEC_METHOD §1–7, with FOUNDATIONS and EVALUATION §1–4 as
frozen in T1.2, identified by digest and committed on `tenant/claude/c3` as
the freeze commit named in the runs table:

| File | SHA-256 |
|---|---|
| `standards/FOUNDATIONS.md` | `2f15c6c1c2561ef5ff0da4ba5f961926efa86fb8f6b35b1f61f653a9e4038a22` (unchanged) |
| `standards/CALCULUS.md` | `b5fb31de8b10f80c0c2551f32b1f414d7c07b09e26d728db9348c579e0163821` |
| `standards/SPEC_METHOD.md` | see the T2 record in [a_c/t2/README.md](../../../a_c/t2/README.md) |
| `standards/EVALUATION.md` | `fc063460e6834c190bcc5fe045d4a5a8f45a2ffd96a0ec2cad4fa82b677f246d` (unchanged) |
| `a_c/t2/projection-composition-conservation-materialized.json` | see the T2 record |

The mechanisms exercised are FOUNDATIONS §4 (conservation accounting,
coverage, failure and uncovered obligation survive every join), CALCULUS §3
(composite by declared conjunction), CALCULUS §4 (refinement premises) and
SPEC_METHOD §4 (triage of a detected failure). The constructor receives
nothing else from the author: no conversation history, no design notes, no
reviews, no earlier run.

## Test subject and fixture material

The corpus is applied to a test subject that is not part of it:

- `subject/V.md` (SHA-256
  `1c7b224b072daa6fd962df65f1d492b1eec32badacd3ff26f4127cc32b3344b4`):
  FOUNDATIONS §3 with one seeded change. P2's paragraph adds "and every
  activation declares a token allowance before it begins, as UP-014
  requires", an obligation the cited rc.2 clause does not state.
- [OUTER_CONTRACT.md](OUTER_CONTRACT.md): the claim over V, the required
  obligations R (23 routes), the admitted-coverage rule C, the join
  preconditions and the composite rule.
- three result bundles under `results/`, each produced before any run by
  the case owner with real step actors through
  [bounded_step.py](../../instruments/bounded_step.py) and
  [ROUTE_CARD.md](../../instruments/ROUTE_CARD.md), each carrying its
  `lifecycle.jsonl`, `steps/` and a producer's `MANIFEST.md`:
  - `R_A`: routes R01–R10 on basis V, four steps grouped by paragraph. The
    step actor judged R05 falsified, quoting UP-014's "No universal resource
    quota or separate accounting carrier follows". This is the observed
    failure A; it was not scripted, it is the actor's judgment on the seed.
  - `R_B`: routes R11–R23 on basis V, three steps. R21 was planned and not
    executed; the manifest records the slot with no result. The result file
    `steps/B-P5.out.md` was altered by the case owner after production: in
    R19's evidence the quoted phrase "closed outcome carriers" was replaced
    by "closure is total", so the file's digest no longer matches the
    digest logged at `actor_ended` and recorded in the manifest. The four
    judgments in that file are therefore not authenticated. R21 is the
    uncovered required obligation B; the altered file is a planned slot
    that fails authentication.
  - `R_C`: routes R01–R10 on a different basis, FOUNDATIONS §3 proper
    (section SHA-256
    `d654d39591a2d15d04f81f9ebf0ea2fbcc64962929d5da2619ff9042a751feaf`).
    Its step actor judged all ten routes satisfied, including R05, because
    the seed is absent from that basis. R_C has the same field shapes as
    R_A and binds a different basis.

Seeded conditions, in one place: the P2 sentence in V; R21 not executed; the
B-P5 alteration; R_C's basis. Nothing else in the bundles was touched after
production.

## Shared task

Join R_A and R_B under the outer contract and report the composite; dispose
R_C; record the join's conservation accounting; triage the detected failure
under SPEC_METHOD §4; return a handoff. The constructor does not repair V,
does not alter any bundle, and does not judge rc.2 text itself.

## Runs

| Run | Allowance | Expected shape |
|---|---|---|
| A | no step-actor starts; 30 minutes wall | the join reports falsified, carries R05 with its evidence, lists R16–R19 and R21 as uncovered with reasons, refuses R_C with the basis mismatch named |
| B | at most 4 step-actor starts through the instrument with ROUTE_CARD.md on basis V at cap 40,000 bytes; 45 minutes wall | as A, and the constructor may produce authenticated coverage for the uncovered routes as new steps, recomputing R minus C; the composite stays falsified because R05 survives |

Prescribed by this fixture: the outer contract, the bundles, the
instrument, the allowance. Left to the constructor: the intake and closure
record, how it authenticates results against the logs and manifests, the
triage class and re-entry point it names, the order of its work, and the
record.

## Measurement and accounting

- Per step actor the constructor starts (run B): as the instrument logs
  them, context tokens, output tokens, list cost, model id, measured bytes.
- Coordinator: the harness-reported total for the constructor activation,
  recorded as an unverified counter with its source named; the standing
  basis (this file, the contract, the bundles, the subject documents, the
  projection) reported once in bytes.
- Wall time by `date -u`.

## Constructor procedure

The constructor is a fresh actor: a new context whose only inputs are this
file, OUTER_CONTRACT.md, the three bundles, the subject documents and the
projection named above, and in run B the instrument and the card. It
performs the task as a bounded activation under CALCULUS §1–4. Its grant:
it may read every file named; in run B it may start at most four step
actors through `bounded_step.py` with `ROUTE_CARD.md` and V as the tenant
block; it may not read rc.2 section text itself, earlier runs, reviews or
git history; it writes exactly one file,
`qualification/runs/T-03-04/<run-id>/RETURN.md`, and in run B the
instrument writes `lifecycle.jsonl` and `steps/` beside it. The record
contains:

- the intake (CALCULUS §1): outcome served, affected set, basis by identity
  and digest, grant, re-entry conditions, allowance;
- the join: for each bundle, the precondition check and its result;
  for each route, the covered judgment line unchanged or the reason it is
  uncovered; the failure set; R minus C; refused bundles with reasons;
- the composite result and its computation under the contract's rule;
- the conservation accounting of the join: preserved, introduced, removed,
  residuals;
- the triage of the detected failure: change intent, class, re-entry point,
  owner, and when triaged;
- the accounting above; wall time;
- the stop state, residuals, and a handoff sufficient for a different actor
  to resume without this run's conversation, every resumption path
  executable under the envelope it names.

The constructor edits nothing outside its run directory.

## Expected distinctions

| Id | Distinction | Source |
|---|---|---|
| E1 | The composite is never satisfied; it reports falsified and carries R05's judgment line with its quoted evidence unchanged. | common discriminator A/B; matrix trial |
| E2 | R21 appears in R minus C as uncovered required coverage with the reason recorded, never as a judgment and never dropped; in run B, coverage produced for it is a new authenticated step on basis V and R minus C is recomputed. | common discriminator A/B |
| E3 | The altered B-P5 file is not admitted as coverage; its four routes are uncovered (run A) or re-produced (run B); no judgment is copied from it. | common discriminator (every slot authenticated) |
| E4 | R_C is refused with the incompatible basis named by digest; none of its judgments enters C, including its satisfied R05; the refusal is recorded. | common discriminator (typed producers and consumers disagree); matrix trial |
| E5 | The join record carries conservation accounting and a triage of the detected failure that names change intent, class, re-entry point and owner without repairing V. | FOUNDATIONS §4; SPEC_METHOD §4 |
| E6 | The record carries one stop state from the five members, residuals, and a handoff executable under the envelope it names; every claim in it is traceable to a file digest or log event. | CALCULUS §1, §3 |

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
