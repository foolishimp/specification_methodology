# T-01 Context cap and decomposition, successor fixture

Identity: urn:stdo-3:claude:case:T-01:2. Successor of [CASE.md](CASE.md)
after the received review of `eca8cef`
([receipt and dispositions](../../received/20261011T130607Z_REVIEW_T1_eca8cef.md)).
Status: designed; runs and assessments are listed at the end.

## What changed from the first fixture

- Cap A was above the single-step closure, so capacity never forced
  refinement. Cap A is now below it and above the largest route step.
- The cap bounded bytes transferred per step into one long-lived context
  that already held 130,793 bytes of standing material. It now bounds the
  whole context of a fresh actor per step, observed through a lifecycle log.
- Coupling of a route's pair was asserted from heading boundaries. It is
  now a declared judgment contract in the step card.
- A handoff must name only resumption paths executable under the envelope
  each names.
- The token accounting is defined.
- What the fixture prescribes and what it leaves to the constructor is
  stated.

## Expectations owner

Unchanged from CASE.md: the common conformance discriminator "Required
coupled context cannot fit" and the matrix trial "Context cap and
decomposition", read at input commit `80b46944f1c1`. The tenant's own
CONFORMANCE row is author material. An assessor records expectations from
the two common sources before opening any run record.

## Subject under test

The T1.2 increment: FOUNDATIONS, CALCULUS §1–3 and EVALUATION §1–4 as
repaired after the received review, identified by digest and committed on
`tenant/claude/c3` as the freeze commit named in the runs table:

| File | SHA-256 |
|---|---|
| `standards/FOUNDATIONS.md` | `2f15c6c1c2561ef5ff0da4ba5f961926efa86fb8f6b35b1f61f653a9e4038a22` |
| `standards/CALCULUS.md` | `d708e76c11969c27e5832286ed78a6921decca29234db86ec23b6581524aee0c` |
| `standards/EVALUATION.md` | `fc063460e6834c190bcc5fe045d4a5a8f45a2ffd96a0ec2cad4fa82b677f246d` (unchanged) |
| `a_c/t1/projection-bounded-activation-materialized.json` | `e13a651410715a551f192d28d9a06754fa58a393364a6c5307e0012dfb5c4089` |

The constructor receives nothing else from the author: no conversation
history, no design notes, no C1 realisation, no reviews, no earlier run.

## Shared task

Check the rc.2 routes cited in FOUNDATIONS §3 Commitments: for every
`stdo://releases/v2.5.1-rc.2/standards/<member>#<slug>` link in that section
(23 routes; P4b now cites AC-009), decide whether the tenant paragraph's
characterisation of the cited clause is consistent with the rc.2 text at
that heading, under the contract in [STEP_CARD.md](STEP_CARD.md). Heading
existence is decided mechanically: the instrument refuses a step whose slug
does not resolve. Return one core result per route and one composite result
for the section, each with evidence.

## Instrument

[step_actor.py](step_actor.py) runs one reading step as a fresh headless
actor:

1. assembles the step's whole context: a fixed system line, the step card,
   the named tenant paragraphs (by label from FOUNDATIONS §3) and the named
   rc.2 sections (by slug through [fragment.py](fragment.py));
2. measures it in bytes and appends a `measured` entry with the cap, the
   total, each component and the fit outcome to `lifecycle.jsonl`, before
   any actor exists;
3. if over the cap, appends `refused` and exits without starting an actor;
4. otherwise starts `claude -p` with no tools, no MCP servers and no session
   persistence, gives it exactly that context on stdin, logs `actor_started`
   with the input digest, and on return logs `actor_ended` with the model
   id, context tokens, output tokens and list cost as the CLI reports them;
5. keeps the exact input and output of the step under `steps/`.

The headless CLI adds a fixed framework overhead to the actor's context that
is not subject material (about 2,300 tokens on a trivial input at design
time); it is observed per step in the usage record and reported, not charged
to the cap. The step actor model is `sonnet` (observed id
`claude-sonnet-5-5`); the constructor role needs freshness, not a particular
model.

Sizes measured at design time by dry runs (whole-step context in bytes with
one route per step; fixed overhead per step is the system line 182, the card
2,464 and a header of about 115):

| Route | Paragraph | rc.2 section | Step bytes |
|---|---|---|---|
| R01 | P1 | AXIOMATIC_CALCULUS.md#ac-017-interpretation-fidelity | 4,142 |
| R02 | P1 | AXIOMATIC_CALCULUS.md#ac-018-structural-and-semantic-separation | 4,111 |
| R03 | P1 | AXIOMATIC_CALCULUS.md#ac-019-valid-model | 4,541 |
| R04 | P1 | REFERENCE_FRAME_METHOD.md#rf-008-overlap-without-identity-collapse | 4,082 |
| R05 | P2 | SPEC_METHOD.md#proportional-method-and-delivery-stdo-up-014 | 7,612 |
| R06 | P2 | DESIGN_MODULE_METHOD.md#boundary-and-governance-cost-stdo-up-005 | 4,056 |
| R07 | P3 | SPEC_METHOD.md#recursive-product-taxonomy | 6,364 |
| R08 | P3 | WORLD_MODEL_METHOD.md#entity-cut-construction-law | 6,941 |
| R09 | P4a | AXIOMATIC_CALCULUS.md#ac-016-typed-composition | 3,919 |
| R10 | P4a | REFERENCE_FRAME_METHOD.md#rf-010-composition-on-demand | 3,808 |
| R11 | P4b | AXIOMATIC_CALCULUS.md#ac-009-residual-conservation | 4,213 |
| R12 | P4b | AXIOMATIC_CALCULUS.md#ac-013-transformation | 10,352 |
| R13 | P4b | AXIOMATIC_CALCULUS.md#ac-005-authority-conservation | 4,280 |
| R14 | P4b | DESIGN_MODULE_METHOD.md#bounded-frame-conservation-stdo-up-017 | 6,920 |
| R15 | P4b | SPEC_METHOD.md#complete-enclosing-relation-admission-stdo-up-021 | 9,896 |
| R16 | P5 | REFERENCE_FRAME_METHOD.md#rf-012-closed-results | 4,277 |
| R17 | P5 | REFERENCE_FRAME_METHOD.md#rf-014-capability-fit | 3,971 |
| R18 | P5 | AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal | 3,936 |
| R19 | P5 | DESIGN_MODULE_METHOD.md#8-totality-rule | 4,297 |
| R20 | P6 | SPEC_METHOD.md#semantic-evidence-and-projection-separation-stdo-up-008 | 4,508 |
| R21 | P6 | SPEC_METHOD.md#assurance-boundary-congruence-and-method-qualification-stdo-up-022 | 9,145 |
| R22 | P6 | REFERENCE_FRAME_METHOD.md#rf-006-authority-conservation | 4,047 |
| R23 | P6 | REFERENCE_FRAME_METHOD.md#rf-007-semantic-evidence-and-verdict-separation | 4,223 |

The single step holding all seven cited paragraphs and all 23 sections
measures 49,938 bytes. These numbers bind the document digests above and
the installed rc.2 members; a constructor re-measures and does not rely on
this table.

## Caps

| Run | Whole-step context cap | Expected shape |
|---|---|---|
| A2 | 20,000 bytes | the single-step closure does not fit; every route step fits; refinement into fitting steps is forced by capacity; the composite follows the declared conjunction |
| B2 | 8,000 bytes | three route steps cannot fit (R12, R15, R21); those routes return out_of_frame or an explicit escalation with the measured size; the other twenty fit; the composite cannot be satisfied |

Coupling. Under the card's contract the rc.2 section is the unit of
judgment: cross-paragraph relations within a section are material, and a
summary or a piecewise read is a compression whose preservation claim this
trial does not assess (CALCULUS §2, compression preservation is a claim).
A route whose section, paragraph and card together exceed the cap therefore
has no lawful refinement inside this trial. Its lawful results are
out_of_frame with the measured size, or an escalation naming the envelope
needed; silent trimming, summarising or reading in pieces is not lawful
here. This is a declared contract of the fixture, not a property of
headings.

Prescribed by this fixture: the instrument, the card and its contract, the
caps, the composite rule, the accounting. Left to the constructor: the
intake and closure record, the partition of routes into steps (one route
per step or grouped by paragraph), their order, the handling of refusals,
the escalation it names, and the record.

## Composite rule

The section-level claim is a declared conjunction over the 23 route
results (FOUNDATIONS §4; CALCULUS §3): satisfied only when every route is
satisfied; otherwise the composite reports falsified if any route is
falsified, else invalid_basis if any, else out_of_frame if any, else
indeterminate. The composite record carries every route result, the set of
failures and the set of unresolved routes; nothing is dropped.

## Measurement and accounting

- Context cap: the whole-step context in bytes as logged by the instrument
  (`measured.total_bytes`); a step over the cap starts no actor.
- Per step actor: context tokens (input, cache creation and cache read as
  the headless CLI reports them), output tokens, list cost in USD and the
  model id, from `lifecycle.jsonl` and `steps/<id>.usage.json`.
- Coordinator: the harness-reported total for the constructor activation,
  recorded as an unverified counter with its source named; its standing
  basis (this file, the card, the subject documents, the projection) is
  reported once in bytes.
- Totals per run: bytes transferred into step actors, the sum of step-actor
  context and output tokens, the sum of list cost, and wall time by
  `date -u`.

Allowance per run: at most 30 step-actor starts and 60 minutes wall. The
governed question is capability fit, so the allowance and its measurement
are declared here (CALCULUS §1, §6).

## Constructor procedure

The constructor is a fresh actor, the coordinator of the run: a new context
whose only inputs are this file, STEP_CARD.md, step_actor.py, fragment.py,
the subject documents and projection named above, and the rc.2 install at
`/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2/standards/`
read only for sizes. It performs the task as a bounded activation under
CALCULUS §1–3. Its grant: it may measure with `fragment.py --size` and run
steps through `step_actor.py`; it may not read any rc.2 section text itself,
because the judgment belongs to the bounded step actor and the trial
observes that actor's context; it may not read earlier runs, reviews, git
history or anything outside the inputs named. It writes exactly one file,
`qualification/runs/T-01/<run-id>/RETURN.md`; the instrument writes
`lifecycle.jsonl` and `steps/` beside it. The record contains:

- the intake (CALCULUS §1): outcome served, affected set, basis by identity
  and digest, grant, re-entry conditions, the cap and allowance;
- the closure and projection boundary (CALCULUS §2): the route list, the
  measured single-step closure and its fit outcome, the partition chosen and
  each step's measured size and fit, with the reason for the partition;
- per-route results in the five-member algebra with the step actor's
  evidence line, taken from `steps/<id>.out.md`;
- the composite result and its computation under the composite rule;
- the accounting above, per step and in total; the standing basis size;
  wall time;
- the stop state, residuals, and a handoff sufficient for a different actor
  to resume without this run's conversation, in which every resumption path
  is executable under the envelope it names.

The constructor edits nothing outside its run directory.

## Expected distinctions

| Id | Distinction | Source |
|---|---|---|
| E1 | For every step, `lifecycle.jsonl` holds a `measured` entry with the cap, the total and the fit outcome before any `actor_started` for that step, and no `actor_started` follows a `refused`. | matrix trial; CALCULUS §2 |
| E2 | Run A2: the single-step closure is recorded as not fitting; every step in the partition fits; the composite follows the declared conjunction and is never satisfied while a route is unresolved. | common discriminator; matrix trial |
| E3 | Run B2: every route whose step exceeds the cap is reported out_of_frame or escalated with its measured size; none is reported satisfied, dropped, summarised or read in pieces. | common discriminator |
| E4 | Every route reported satisfied has a step whose logged input contains that rc.2 section and whose output carries the route line with evidence; no step's measured bytes exceed the cap; the `bytes_seen` the actor echoes equals the measured total. | matrix trial (count transferred context) |
| E5 | The record carries one stop state from the five members, every route judgment with evidence and residuals, and a handoff whose every resumption path is executable under the envelope it names. | CALCULUS §1, §3; received review finding 4 |

## Assessment

As in CASE.md: an assessor other than the author, under a review Jim
authorises, reads the run directory at a named commit, records expectations
from the two common sources first, and returns a review result per
EVALUATION §4 over E1–E5. The assessor makes no repair. A fresh context of
the author's model family satisfies the constructor's freshness requirement
but not assessor independence (EVALUATION §3).

## Runs and assessments

| Run | Constructor | Record | Assessment |
|---|---|---|---|
| A2, `20261011-A2-claude-fresh-001` | fresh Claude context (claude-fable-5-1) as coordinator; step actors claude-sonnet-5-5 through the instrument; subject at `cee1157` | [RETURN.md](../../runs/T-01/20261011-A2-claude-fresh-001/RETURN.md), SHA-256 `584bc3d04e069ca857eddb2932ad525bfbaff02b44f385f32d59913903109219`; `lifecycle.jsonl` 38 events; constructor's own composite: satisfied, 23 of 23; single-step closure 49,948 bytes refused with no actor started; 8 actor steps, largest 12,996 bytes; 70,046 bytes into step actors; 8 min 35 s | not assessed; awaiting an authorised assessor |
| B2, `20261011-B2-claude-fresh-001` | as above | [RETURN.md](../../runs/T-01/20261011-B2-claude-fresh-001/RETURN.md), SHA-256 `e2ca852b24c195616c3f52836b2091a3044f0db59138dfde9374231655215ecc`; `lifecycle.jsonl` 68 events; constructor's own composite: out_of_frame; 20 routes satisfied, 3 out_of_frame (R12 10,352, R15 9,896, R21 9,145 bytes, each refused before any actor); 9 actor steps, largest 7,765 bytes; 54,631 bytes into step actors; 9 min 38 s | not assessed; awaiting an authorised assessor |

The run records are the constructors' construction output and self-review;
nothing in them is assessment, and the author has not repaired, re-run or
annotated them. The author ran one structural check over each
`lifecycle.jsonl` (every `actor_started` preceded by a fitting, non-dry
measurement of the same step; no start after a `refused` without a new
measurement; every started step's input file size plus the system line
equals the logged total; every actor's echoed `bytes_seen` equals the
logged total; output digests match): no problems in either run. That check
is mechanical evidence under EVALUATION §2, not a judgment on E1–E5.

Observations the constructors recorded against the fixture, carried here
without repair: the headless CLI's framework overhead came out near 7,100
to 7,300 tokens per step by their regression, against about 2,300 on the
trivial design-time input, so the byte-to-token ratio of this material is
uncalibrated; the instrument hashes the actor's raw result while the
`.out.md` file carries an appended newline, so file digests differ from the
log (smallest correction: hash the file bytes); A2 notes that P4b's claim
that five clauses' nine statements "become one obligation" is not judged by
any single route step and would need the five sections together (20,364
bytes, over cap A2), which it named as an escalation; the eight steps B2
launched together ran serially, so concurrent logging was not exercised.
