# Iteration 3 Plan, Claude Line

Written by Writer activation I3-1 under execution contract
`EC-CLAUDE-I3-01`. It proposes the order of work; the Executive selects
each activation and disposes each return, and the ledger records both
([ledger, Iteration 3](../C3-SYNTHESIS/LEDGER.md#iteration-3)). Nothing in
this plan is acceptance.

## 1. Basis

| Coordinate | Value |
|---|---|
| Authority | `EC-CLAUDE-I3-01`, admitted in T-002-CLAUDE at `651581c`, SHA-256 `3c928885…0b859`; confirmed by the product owner at 2026-10-14T16:01Z |
| Common input | `C3-I3-R2-01`: common specification at `355aa8655cca9c6ba6cf5c414f9bea3032ae89fd`, merged inward at `22991db` |
| Builder | installed `stdo://releases/v2.5.1-rc.2/`, manifest `3d860ff4…2782` |
| Candidate preimage and second comparison subject | `5ab44d5c51bf5956d12b120d83159f6c28eee3a9` (tenant tree `b75d6aa6…`). The working tree differs from it only in `qualification/C3-ITER3/ORACLE.md` and the ledger; every comparison cites the commit, not the working tree |
| First comparison subject | the installed predecessor above |
| Oracle | [ORACLE](ORACLE.md), 98 expectations, a declared same-family exception for this candidate ([CONSTRUCTION_BINDING §1](../../design/CONSTRUCTION_BINDING.md#1-three-coordinates-kept-apart)) |
| Paid-trial allowance | USD 15 for iteration 3 trials, balance USD 15.00, recorded in the ledger at 2026-10-14T16:01Z |
| Known gaps carried | the product owner's sign-off on the common specification; the changes to accepted conditions; the pillar list; the replacement relations awaiting acceptance |

## 2. Starting state

- Codex findings: F1, F2, F4 and F5 are repaired in source, with
  same-family working evidence; cross-family confirmation is open. F3,
  the current a_c interpretation, is open
  ([F1-F5](F1-F5.md)).
- Pillar account and reduction inventory: [REDUCTION](../../design/REDUCTION.md)
  sections 2 and 3.
- Interpretation: none current; design in
  [INTERPRETATION](../../design/INTERPRETATION.md).
- Frontier: the tenant copy holds every row of the common inventory at
  `355aa86` (726 rows) plus 5 tenant child rows; its header still names
  the earlier common commit `b83ed1c`.
- Conformance: the candidate's CONFORMANCE maps the 31 discriminators of
  the earlier input; the common input now has 52 member-conformance rows
  and 3 construction and closure rows.
- Frames: 10 published frames under `standards/frames/`. No frame covers
  the tasks "decide acceptance or release" or "build or assess a member"
  as such.

## 3. Conventions for every activation

- **Intake.** The Executive's intake gives the UP-020 fields: the exact
  outcome and checkpoint, the rows in scope, the governing invariants,
  the grant and write territory, the evidence required, exclusions, stop
  and re-entry conditions, the context, wall-time and spend limits, and
  the exact bounded action.
- **Limits.** Defaults from
  [CONSTRUCTION_BINDING](../../design/CONSTRUCTION_BINDING.md#limits-for-each-activation-kind):
  300,000 bytes of declared material, 45 minutes, spend `unavailable`
  for subagents. Each return reports supplied bytes, cumulative acquired
  bytes with repeats, and the active retained bound separately, with
  start and end times by `date -u`.
- **Returns and deltas.** A Writer writes its return to
  `qualification/C3-ITER3/returns/<ID>.md` and the frontier rows it
  changes to `qualification/C3-ITER3/deltas/<ID>.md` (row, disposition,
  locus, before and after quotes, the claim's meaning, its judgement).
  Only the integration activations change `frontier/PREDECESSOR_CLAIMS.md`,
  `standards/GLOSSARY.md` and `standards/README.md`.
- **Changed conserved rows.** Every `conserved` or `superseded` row whose
  locus text an activation changes is re-assessed in that activation's
  delta against the predecessor claim, including scope, modal force,
  triggers and exceptions. A changed meaning becomes a proposed
  `superseded` row with its replacement relation, pending the product
  owner's acceptance. The working check re-reads each such row.
- **Working checks.** Each Writer return is followed by a same-family
  working check that records its expectations from ORACLE before opening
  the subject. It has no territory, counts toward the concurrency limit,
  and supports `local_repair`, `re_enter` or `reject`, never `accept`.
- **Concurrency.** At most four activations at once, with disjoint
  territories
  ([composition law 2](../../design/CONSTRUCTION_BINDING.md#composition-laws)).
- **Purpose.** No activation adds an obligation or process step without
  naming its purpose and material relation (conformance row 41).
- **Escalation.** A defect in the common specification goes to the
  common pen through the Executive. A change of predecessor meaning goes
  to the product owner as a proposed replacement relation.
- **Same text, same owner.** An activation that finds a second locus
  deciding a question its territory owns makes the other locus a
  reference or a refinement only inside its own territory; otherwise it
  reports the locus for the activation that owns it.
- **Fixed interfaces.** Concurrent activations link to sections another
  activation creates, so these headings are fixed in advance:
  - ACTIVATION §2 `### Staleness of derived surfaces` (R23);
  - EVALUATION §5 `### When a finding blocks promotion` (R25);
  - FOUNDATIONS §2 Authority kinds keeps its anchor and owns the list of
    what creates no authority and the proxy limit (R12);
  - FOUNDATIONS §3 family-index and family-table format gain a `Pillar`
    column (REDUCTION §2);
  - AXIOMATIC_CALCULUS §9 `### Constraint surfaces` (pillar 10);
  - all other owner anchors named in REDUCTION §3 stay as they are.

## 4. Activations

The sequence follows the contract: reconcile design and shared owners;
repair consumer bindings; complete claim dispositions and named port
accounting; regenerate interpretation and views; freeze; assess; triage
and repair.

Steps 1 to 3 settle the member text. The source settles at the commit
I3-4d returns, and every encoding and frame starts from that commit.

Every Writer is followed by a working check. A check runs as soon as its
subject is committed and takes one of the four concurrent places. Where a
step lists more than four activations, the Executive runs them in the
order given, keeping at most four running and every territory disjoint.

### Step 1: reconcile design and shared owners

The four activations of this step run together. Their territories are
disjoint, and each applies only the REDUCTION §3 actions inside its own
members.

| ID | Territory | Work | Inputs | Exit proof |
|---|---|---|---|---|
| I3-2a | `standards/FOUNDATIONS.md`, `standards/ACTIVATION.md` | owner side of R2, R10, R12, R16, R18, R23, R26 and design discrepancy b; pillar column in the family-table format and index; ACTIVATION §2 binds the successor RF sections instead of rc.2 links (pillars 6 and 7); resource-limit law in ACTIVATION §6; owner text for RF §10 and ACTIVATION §7 trigger terms (R8) | REDUCTION §2 and §3; F1-F5 (F1, F2 owners); the common requirements | each named owner states its determination once; no rc.2 link stands in for a successor rule at ACTIVATION §2; delta with every changed row re-assessed |
| I3-2b | `standards/EVALUATION.md`, `standards/REFERENCE_FRAME.md`, `standards/AXIOMATIC_CALCULUS.md`, `standards/IDENTITY.md` | rival side of R1 (EVALUATION:352), R6, R8, R11 (author identity), R12, R19, R20, R22, R29 in these members; EVALUATION §5 owns R25; AXIOMATIC_CALCULUS §9 states the constraint-surface use (pillar 10); EVALUATION:101 takes the owner's force | as I3-2a | each listed rival refers or refines with a map; delta. If the work exceeds 45 minutes the Executive splits off REFERENCE_FRAME and AXIOMATIC_CALCULUS |
| I3-2c | `standards/SPEC_METHOD.md`, `standards/TICKETS.md`, `standards/RELEASE.md`, `standards/ASSURANCE.md`, `standards/PRODUCT_DEFINITION.md` | R7 (SPEC_METHOD:902–905, :932; TICKETS:1065–1070, :1142), R10 lifecycle owner, R11 triggers in TICKETS, R13 (SPEC_METHOD:494–500, :1466; ASSURANCE:1096), R14 closure-condition owner and close classifications, R17 (TICKETS:481), R23 (PRODUCT_DEFINITION §11 refines ACTIVATION §2), R26, R29 (SPEC_METHOD:1757–1764), SPEC_METHOD §11 binds ACTIVATION §6 limits; rename the S/T/D/O sense of "pillar" | as I3-2a | as I3-2b |
| I3-2e | `design/DOCUMENT_STRUCTURE.md`, `design/REDUCTION.md` | record the REDUCTION owner decisions beside D1 to D8 (correcting D1's wording and D2/D4/D7 per discrepancies a and b); update the member map, activation unit and per-member proof for the 52 + 3 conformance rows; complete the inventory: sweep POSTING_GUIDE, WRITING_GUIDE, schemas, templates and wording-variant rivals, adding clusters and paths under REDUCTION §4's rule | REDUCTION; the three sweeps' scratch outputs | every new cluster has an owner, an action with an activation and, if material, a path; nothing in §4 is removed or redefined |

### Step 2: consumer bindings

Relation 1 arguments must be real, meaning premise to consequence, with a
named policy where a choice is made, the pillar contribution bound, and
the declared instance premises cited. A hollow row, which files a whole
rule as a policy, does not pass. Result mappings: every value set
that decides maps each value to exactly one core value with its
predicate. Rivals become references or refinements.

| ID | Territory | Work | Exit proof |
|---|---|---|---|
| I3-3a | `standards/EXECUTIVE_BASELINE.md` | R2 (`:991`), R3 (`:439`, `:442`), R5 (`:393–396`, `:619`), R8 (`:1273–1281`), R11 (`:885`, `:1103`), R14 (`:402`, `:1651`), R16 (`:165–178`, `:656`, `:1290`), R21 (`:1288`), R25 (`:1183`); F16 table real, with pillars | the table check below; each listed locus refers or refines |
| I3-3b | `standards/DESIGN_MODULE.md` | R7 (`:1897–1902`), R10, R12 (`:769`), R21 (`:2272`), R25 (`:1876`); F17 table real, with pillars | as I3-3a |
| I3-3c | `standards/ODD.md` | R3 and R14 homonyms (`:1049`, `:1071`); R23 duplicate (`:1644`); F18 table real; trace ODD §2, §3, §10, §11.2–11.3, §16 to §20 | as I3-3a |
| I3-3g | `standards/TRAVERSAL_OCCURRENCE.md` | R1 and R5 (`:760`, `:964`, `AXIOMATIC_CALCULUS.md:524` alignment), R21 (`:1426`); MT-7 example (F1-F5, F2); F19 table real | as I3-3a |
| I3-3d | `standards/UX.md`, `standards/WORLD_MODEL.md`, `standards/PROFILES.md`, `plugins/`, `standards/templates/` | R4 and R16 plugin and template texts; R5 template; R9 UX replay need; R10 skill; R14 UX conflict (ruling request) and `:713`; R18 UX exits; R20 and R29 WORLD_MODEL:529; R21 UX adoption; R23 UX:392; pillar 2 refinement; R13 PROFILES:136–142; F20 and F21 tables real | as I3-3a |
| I3-3f | `standards/SPEC_METHOD.md`, `standards/TICKETS.md` | F10, F11, F13 tables real, with pillars; trace TICKETS §6 (`:763–926`); TICKETS:570 hollow row | as I3-3a |
| I3-3h | `standards/PRODUCT_DEFINITION.md`, `standards/RELEASE.md`, `standards/ASSURANCE.md` | F12, F14, F15 tables real; R4 (`PRODUCT_DEFINITION.md:416–418`, the suspected F2 recurrence), R19 (`:484`), R21 (`:571`) | as I3-3a |
| I3-3j | `standards/REFERENCE_FRAME.md`, `standards/ACTIVATION.md` tables only, `standards/EVALUATION.md`, `standards/IDENTITY.md`, `standards/AXIOMATIC_CALCULUS.md` tables only | F1, F2, F4, F5, F6 to F9 tables real, with pillars; the hollow rows EVALUATION:69, :78 and IDENTITY:70; instance premises of F3, F8, F9 cited | as I3-3a |
| I3-3k | `standards/CONFORMANCE.md` | map the 52 member-conformance discriminators and the 3 closure checks to a case or a logical-review check; R1 (`:24`); R6 (`:70`); F2 wording at `:96` | every row mapped; no row maps to a stale locus |
| I3-3i | `qualification/instruments/finite_oracle/` | F4 evidence: re-review P0 and P4 against the changed single result algebra requirement (item 2 and the lifecycle paragraph), re-declare the section digest at `check.py:32`, regenerate `FINITE_RESULT.json`, keep the four value-only mutants | `--check` exits 0 at the new commit; every declared mutant falsified |
| I3-3e | `frontier/PREDECESSOR_CLAIMS.md`, `standards/GLOSSARY.md`, `standards/README.md` | integration 1: apply the step 1 and step 2 deltas; rebind the frontier header to the common inventory at `355aa86` (726 rows plus 5 tenant child rows, checked by script); GLOSSARY senses for R27; README route | every delta applied and nothing else (diff); every locus resolves (script) |

Order:
- I3-3a, I3-3c, I3-3g and I3-3i together; I3-3b, I3-3d, I3-3f and I3-3k
  next; then I3-3h and I3-3j; then I3-3e.
- I3-3f follows I3-2c, and I3-3j follows I3-2a and I3-2b, because they
  share members.

**Table check.** The working check of each step 2 activation samples at
least 30% of the member's family-table rows, and all rows that were
hollow or weak. For each sampled row it confirms that the cited premises
force the consequence or that a named policy carries the choice. It also
confirms that every deciding section of the member is in the table or
excluded with a reason.

### Step 3: claim dispositions and named port accounting

| ID | Territory | Work | Exit proof |
|---|---|---|---|
| I3-4a | `qualification/C3-ITER3/reassess/tier12.md` | re-assess every `conserved` or `superseded` row whose locus text changed in steps 1 and 2, or in revision 2b (the 9 exact and 16 possible rows in [F1-F5](F1-F5.md#frontier-rows-touched-by-revision-2b)), for tier 1 and Spec Method members; check scope, modal force, triggers and exceptions; propose `superseded` with a replacement relation where meaning changed. Also row 364's cell | one judgement per row, citing predecessor and candidate text; the actor wrote none of the changed text |
| I3-4b | `qualification/C3-ITER3/reassess/profiles.md` | the same for profiles, guides and packaging | as I3-4a |
| I3-4c | `qualification/C3-ITER3/ports.md` | named port accounting for the six ports of [CROSS_SYNTHESIS](../../design/CROSS_SYNTHESIS.md): exact source at `31f28f90…` as recorded, receiving owner, cone, disposition; reconcile the port records with the frontier. No new peer inspection is selected under the contract, so comparison with the peer source waits for the product owner's ported-part review policy | each port has one owner and one cone; conflicts between records listed |
| I3-4d | `frontier/PREDECESSOR_CLAIMS.md`, `standards/GLOSSARY.md`, `standards/README.md` | integration 2: apply I3-4a and I3-4b; account for the 36 non-body and 19 auxiliary rows (each `unresolved` row names its owner decision); write the `standards/README.md` route text for the interpretation, which points to `a_c/i3/README.md` for the current subject and limits, so README does not change after settlement (INTERPRETATION §7); record the source-settlement commit | frontier complete at PC granularity; the settlement commit named in the return; no member file changes after it except through step 7 |

### Step 4: interpretation and views

Each activation here starts from the source-settlement commit and follows
[INTERPRETATION](../../design/INTERPRETATION.md).

| ID | Territory | Work | Exit proof |
|---|---|---|---|
| I3-5s | `a_c/i3/SIGNATURE.md`, `a_c/i3/tools/` | signature, standing symbols, shared premises P0 to P6 and C, core result values; `assemble.py` and its test. May start after step 1 | the tool's tests pass, including a fragment with a hollow policy, a refinement mapping to two core values and a residual-dependent clause without `blocked-by`, each rejected |
| I3-5e01 to I3-5e13 | `a_c/i3/fragments/G<n>.json`, `a_c/i3/dispositions/<member>.md` for its group | one fragment per group G1 to G13 of INTERPRETATION §8, in four waves of four or fewer; G1 to G4 (shared owners) first | every heading section of the group's members has one disposition; the fragment passes `assemble.py` alone |
| I3-5m | `a_c/i3/axiomatic-program.json`, `bindings.json`, `README.md` | assemble; the tenant pre-check over the whole program; coverage totals; known gaps with scope; the three coordinates | pre-check passes; README states subject, basis, signature, coverage and evidence boundary |
| I3-5k | `a_c/i3/validation-report.json`, `logical-constraint-map.json`, `projections/` | only on the product owner's selected evaluation: acquire, verify and run the checker (INTERPRETATION §5), twice | seven members and aggregate verified; validation and projections reproduced byte for byte |
| I3-5v | `qualification/instruments/generate_frames.py` and tests, `standards/frames/`, `a_c/README.md`, `a_c/*/README.md` first lines. No member file | frames carry the family-table rows and result maps their sections need (TO1); new frames for "decide acceptance or release" and "build or assess a member"; `kind` label (F5 residual); entry relabel (INTERPRETATION §7); regenerate | `--check` exits 0; links resolve; every frame within 100,000 bytes or split by task, never truncated; no route reaches a historical set as current |

### Step 5: freeze

| ID | Actor | Work |
|---|---|---|
| I3-6 | the Executive in a recorded Writer role | commit; record the freeze commit and the digests of members, frames, `a_c/i3/` and instruments in the ledger. That commit is subject S2 for every assessment |

### Step 6: independent source review and actual-use assessment

| ID | Territory | Work | When |
|---|---|---|---|
| I3-7a | `qualification/instruments/bounded_step.py` and its card | harden fresh-actor isolation and prove it with a canary: show that user-level instruction files, memory and skill listings do not reach the actor. Without that proof a run is not counted as fresh. Add a read-only-tool mode confined to an isolated copy of the frozen standards, recording each acquisition and its bytes. Add a neutral card with no method hint for all arms | any time; before any run |
| I3-7b | `qualification/C3-ITER3/trials/TT-*/` task, fixture and expectations | trial tasks and expectations (§5), written before frames are opened by an actor that wrote no member text or frame; hashes recorded; the cross-family set requested through the product owner | after I3-4d, before I3-7r |
| I3-7c | `a_c/i3/fidelity/cases/` | interpretation fidelity cases from the prose, before the model is opened (INTERPRETATION §6) | after I3-4d |
| I3-7d1 to I3-7d4 | `qualification/C3-ITER3/paths/S0-S1-<group>.md` | trace DP-01 to DP-40 on S0 and S1 under REDUCTION §4.5, from route entry and, where a frame exists, frame entry; four activations of ten paths each | any time after this plan is disposed |
| I3-7d5 to I3-7d8 | `qualification/C3-ITER3/paths/S2-<group>.md` | trace the same paths on S2 and compare against both baselines under the outcome rule, route-entry verdicts kept apart from the frame-entry measure | after I3-6 |
| I3-7r | `qualification/C3-ITER3/runs/` | paid runs (§5, §6) | after I3-6, I3-7a, I3-7b |
| I3-7g | `qualification/C3-ITER3/grading/` | blind grading: arm labels removed, outputs shuffled, by an actor that wrote neither frames nor expectations | after I3-7r |
| I3-7v | `a_c/i3/fidelity/review.md` | source-first fidelity review on the cases; coverage and standing checks | after I3-5m (I3-5k if selected) and I3-7c |
| I3-7w1 to I3-7w4 | `qualification/C3-ITER3/reviews/W<n>.md` | working source reviews per member group (tier 1; Spec Method; profiles; guides and packaging): criteria 1 to 6 and the applicable discriminators over each cone, expectations from ORACLE recorded first | after I3-6 |
| I3-7x | `qualification/C3-ITER3/reviews/INTEGRATED.md` | integrated working assessment: cross-member reduction from REDUCTION §3 and the path results, interpretation coverage, frame-use evidence; closure checks J53 to J55 | after all of the above |

Cross-family acceptance reviews are not tenant activations. The Executive
requests them through the product owner, with the frozen commit.

### Step 7: triage, repair and retry

| ID | Work |
|---|---|
| I3-8t | the Executive triages the findings of step 6 with bounded evaluations: each finding goes to its owning locus, or to the common pen when the common specification causes it |
| I3-8r | repair Writers, by territory as in steps 1 to 4; each changed row is re-assessed as in step 3. A repair that changes member text also re-encodes the affected fragments and their dispositions, regenerates the affected frames, and reruns the affected fidelity cases, so the interpretation's stated subject stays true |
| I3-8f | re-freeze (as I3-6); every changed frame or task is a new subject |
| I3-8q | retry runs only for frames or tasks whose subject changed, under the retry reserve; a corrected run is reported as evidence for the correction's subject, not as an unchanged independent test of it |

### Return

| ID | Work |
|---|---|
| I3-9 | the closed return under the installed baseline: `candidate_ready` with the exact frozen commit, or `incomplete` with committed progress. It covers the four Outcome bullets, the remaining gaps with source links, measured activations and spend, and a handoff for the product owner |

If limits bind before the whole plan runs, the smallest coherent return
is:
- steps 1 to 3;
- the shared-owner fragments G1 to G4 with the refinement maps, declared
  as partial coverage;
- the freeze;
- I3-7d1 to I3-7d8;
- trials on the four frames whose paths carry the most clusters: rf-task-b,
  eb-task-d, traversal-task-f and stale-summary.

## 5. Trial design

Each trial is a fresh actor started on one input bundle, against tasks
whose expectations were fixed before the run. The design separates
the effect of frame content from what the fixture text already decides.

- **Tasks.** One per selected task kind and path situation:
  - TT-01 review (DP-01);
  - TT-02 decide (DP-03);
  - TT-03 profile, traversal (DP-04);
  - TT-04 work, capacity (DP-06);
  - TT-05 resume (DP-07);
  - TT-06 review, revision (DP-08);
  - TT-07 decide, proxy (DP-11);
  - TT-08 member, dispositions (DP-12);
  - TT-09 work, direct entry (DP-16);
  - TT-10 work, ambiguity (DP-17);
  - TT-11 decide, release (DP-21);
  - TT-12 entry (DP-23);
  - TT-13 the interpretation route (DP-27).
  Together they cover the six task kinds and REDUCTION §5's successful,
  refused, unresolved, composition, failure and recovery kinds.
- **Not decided by fixture text.** Every expectation item is tagged `M`
  if the method decides it, or `F` if the fixture text states it. The
  no-method control calibrates the tags. An `M` item that any control run
  passes is re-tagged `F`, excluded from attribution and reported.
  Criterion 4 is judged on `M` items only.
- **Arms.**

  | Arm | Input | Purpose | Runs |
  |---|---|---|---|
  | A0 control | neutral card, task, fixture; no method | calibrate `M` items | 12 tasks × 1 |
  | A1 frame alone | neutral card, the S2 frame for the task, task, fixture | criterion 4 evidence for the frame | 12 tasks × 2 |
  | A2 predecessor | neutral card, the rc.2 sections the S0 route of the task's path reaches, verbatim, task, fixture | comparison only; not standalone evidence | 4 tasks × 1 (TT-01, TT-02, TT-05, TT-11) |
  | A3 routes | neutral card, frame, task, fixture, with read-only tools confined to an isolated copy of the frozen standards | declared acquisition routes in use; supplied, cumulative and active retained bytes from the transcript | 2 tasks × 1 (TT-05, TT-08) |
  | A4 projection | neutral card, the a_c projection for the task, task, fixture | actual use of the interpretation; only if I3-5k ran | TT-13 × 2 |

- **Fresh contexts.** One task per process. There are no tools except in
  A3. The working directory is empty and outside any repository, and the
  I3-7a canary proof is required. Supplied instructions and all acquired
  material are recorded.
- **Declared limits.** Each run's card states:
  - its context cap: at most 120,000 bytes of whole input; for A3 also
    150,000 bytes active retained;
  - 10 minutes of wall time;
  - USD 2 of spend.
  A run over its cap is refused before it starts, never truncated.
- **Expectations.** Written in I3-7b before the frames are opened, with
  hashes recorded in the ledger before the first run. The writer is the
  cross-family set when the product owner supplies it, otherwise a
  declared same-family exception.
- **Grading.** Blind to arm. One closed result per expectation item. A
  failed `M` item in A1 is attributed by triangulation: frame content,
  owner text, task wording or actor application.
- **Reuse.** No earlier run (C3S, F-xx, T-xx) is reused for a changed
  frame or task. `qualification/cases/F-03/EXPECTATIONS.md:176` is not
  used as a current expectation ([F1-F5](F1-F5.md#f2)).

## 6. Paid-trial budget

The allowance is USD 15 for iteration 3 trials, with a balance of USD
15.00 recorded in the ledger at 2026-10-14T16:01Z. Revision 2 and 2b
spend keeps its own record. Per-run estimates scale from measured
history:
- the archived suite's 18 runs: USD 3.22, about USD 0.18 per run at
  65–94 KB of input;
- C6b: USD 0.84 for 4 runs, about USD 0.21 per run.
They are estimates, not prices.

| Item | Runs | Estimate per run (USD) | Subtotal (USD) |
|---|---|---|---|
| canary probes (I3-7a) | 3 | 0.03 | 0.09 |
| A0 control | 12 | 0.06 | 0.72 |
| A1 frame alone | 24 | 0.25 | 6.00 |
| A2 predecessor | 4 | 0.25 | 1.00 |
| A3 routes (multi-turn; unmeasured) | 2 | 0.60 | 1.20 |
| A4 projection | 2 | 0.25 | 0.50 |
| planned total | 47 | | 9.51 |
| retry reserve after repair (I3-8q) | about 12 | 0.25 | 3.00 |
| unallocated | | | 2.49 |
| allowance | | | 15.00 |

Rules:
- the first batch is the canaries and four A1 runs. If its mean cost
  exceeds the estimate by more than 30%, the Executive cuts A1
  repetitions or A2 tasks before continuing;
- no batch starts whose estimate exceeds the balance minus the retry
  reserve;
- the first A3 run is measured before the second starts;
- `total_cost_usd` is recorded per run, and the ledger balance after each
  batch;
- an increase needs the product owner's decision. A new contract does not
  reset this allowance.

## 7. Points for the product owner or the common pen

Each point blocks only the work that depends on it.

1. **Select the mechanical evaluation** of the frozen iteration 3 a_c
   program under A_C_DEPENDENCY: validation, then projection of the frame
   indexes. Without it I3-5k, the projections, A4 and DP-27 do not run.
   Requested now so encoding can plan for it.
2. **Rulings:**
   - MT-9 and MT-2 (F1 residuals);
   - AS3 B21 attribution (a) and (b);
   - the UX compliance conflict (`UX.md:737`);
   - the compression carrier's disposition;
   - the occ-24 fixture reading (OF-5).
3. **Replacement relations.** Accept or reject the pending ones (rows
   516, 522, 543, 560, 565 children) and those iteration 3 proposes. Each
   dependent `superseded` row cites the ticket record before member
   acceptance.
4. **Cross-family evidence:** a non-Claude expectation set (I3-7b),
   fidelity cases (I3-7c) and acceptance reviews; the acceptance-review
   assignment; the ported-part review policy.
5. **Sign-off** of the common specification and its pillar list. This
   plan and REDUCTION §2 bind the current list.
6. **Common pen:** transcribe the ledger's iteration 3 entries into
   T-002-CLAUDE (variance V1).

## 8. Risks

- **Size.** About 55 Writer activations plus their working checks. At
  four concurrent and 45 minutes each, that is on the order of 20 rounds.
  The fallback return in §4 keeps a truncated run coherent.
- **Independence.** Every check and trial expectation inside the tenant
  is same-family working evidence. No criterion reaches acceptance
  without cross-family review.
- **Owner gates.** The checker selection and the rulings in §7 block the
  work that depends on them.
- **Encoding scale.** An estimated 1,800 to 2,600 clauses. Complete
  fidelity review over all of them is larger than this plan's sampled
  review and is required before C3 closure.
- **Frame size.** Carrying family tables and maps (TO1) may push frames
  past the 100,000-byte declared capacity; the fallback is task splitting,
  not truncation.
- **Budget.** The allowance is tight for the arms planned, and the A3
  cost is unmeasured. The stop rules in §6 apply.
- **Moving basis.** The common specification is not signed off. A
  change on `main` reopens the affected conclusions under the
  re-entry rules.
- **Inventory incompleteness.** The inventory is a lower bound; late
  clusters add paths and work.
- **Concurrency.** Four concurrent activations raise the backlog of
  returns to dispose. The Executive reduces concurrency if returns wait
  undisposed.
