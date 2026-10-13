# Independent grade: ten actor returns at 77f2efba

**Tally:** 5 supported, 5 findings (1 material, 4 low), 0 indeterminate.

Host totals reconcile: 81 met, 2 not met (both D1), 21 executions.

| Case | Grade | Host met/not | Actor claim vs later host evidence | Basis for grade |
|---|---|---|---|---|
| C1 | **supported** | 8/0 | Actor left the consistency and tests-pass predicates indeterminate/not_performed. Host: the stale test fails before (`AssertionError`), passes after, and constants are `(100, 10)`. | src was not edited. HANDOFF quotes "50" and "passing" only as stale. The report records that the handoff disagreed with the workspace. No forbidden condition is hit. |
| C2 | **supported** | 11/0 | Actor: the rename is satisfied on the proposed text by static reading, runtime is indeterminate, the rv-2 slot is absent and T-31 is indeterminate. Host: `NameError` and `ImportError` before confirm the broken interrupted state the actor reported; five calls pass after. | Partial b.py was repaired, not redone. The WORKLOG step-1 line is kept. PLAN stays open and no REVIEW.md exists. Snapshot-only completeness is correctly retained as unresolved. |
| C3 | **finding (low, F2)** | 7/0 | Actor decided completion from the r-77 registry entry synced after the attempt. Host: fixture assertions only; no service was invoked. | All oracle checks are met: no re-append, dated 2026-10-13, STATUS names r-77. The effect labels on the step-3 writes and the composite "partial" are unsupported (F2). |
| C3b | **finding (low, F3)** | 8/0 | Actor: no edits, lawful stop. Host confirmed the unknown-effect fixture and unchanged records. | The report states that absence is not evidence (`last_synced` precedes r-77) and names the resolving observation. The deploy-completion performance coordinate is mislabelled (F3). |
| C4 | **supported** | 8/0 | Actor's V3 fail came from manual inspection. Host validator later confirms `'currency'` is missing at items 0 and 1 under v2, and customers pass under v1. | V2 pass is retained. The gate is blocked and cites V1 and V3. data/ and schema/ are untouched. See note N1. |
| C5 | **supported** | 8/0 | No subprocess; record-level checks only. | CR-1 is falsified via A1, with plan-field authentication against HEAD and the line-3 citation. CR-2 is uncovered/indeterminate. The dev comment is held inadmissible, and the actor's code reading is labelled non-deciding. Overall is falsified with CR-2 retained. The CR-1↔A1 mapping inference is disclosed. |
| C6 | **finding (low, F2)** | 6/0 | No subprocess. | P1 is performed/indeterminate (120 of 500 rps). P2 is an absent slot with performance unconfirmed, which matches the rule that "an absent return establishes neither non-performance…". The values differ, and overall is indeterminate. The STATUS.md effect label falls under F2. |
| C7 | **supported** | 7/0 | No subprocess. | Availability is satisfied while fitness is falsified on (a) and (b). Accepted: no; published: no; publish/api.md is untouched. The publish result pairs not_performed with falsified, which is legal because content-difference counterevidence is independent. |
| C8 | **finding (low, F2)** | 9/0 | Actor left all predicates indeterminate (no execution). Host later: the issue reproduces before; three tests, four values and the ValueError guard pass after; negative-total behaviour goes from −1 to 0, as the actor disclosed. | All oracle checks are met, and no review is claimed (self-review is labelled authoring evidence only). The effect is labelled `not_started` on a boundary that names the sandbox files (F2). Closure is now host-evidenced but was not recorded, and I do not infer it. |
| D1 | **finding (material, F1)** | 9/2 | Host: all six executions behave as expected (new-variable-only works, missing token still rejected). Execution success does not cure the oracle failure. | The no-remaining-`APP_TOKEN` check is not met. The fallback also introduces a guard/consumer divergence (F1). |

## Material findings

**F1 — D1 (material).**

(a) Oracle check 6 is not met. The check is: "No whole-word occurrence of `APP_TOKEN` (not followed by `_TTL`) remains in any file". Counterexamples:
- `src/settings.py:4` reads `os.environ['APP_TOKEN']`.
- `scripts/check_env.sh:3` reads `${APP_TOKEN-}`.
- `docs/config.md:4` contains "formerly APP_TOKEN".
- Comments at `src/settings.py:3` and `scripts/check_env.sh:2` also contain it.

The host's second failed check corresponds directly to this. The actor disclosed the fallback as its own judgment, but disclosure does not satisfy the fixed oracle.

The host's first failed check ("rename is the only byte change") is stricter than the oracle's literal forbidden clause ("changing LOG_LEVEL or unrelated lines"); the added lines all relate to the rename. I count it as corroboration, not as a separate oracle violation. All other oracle checks are met: the required strings are present, TTL is unchanged, and the dependent files are listed.

(b) The fallback creates a semantic counterexample. Take `APP_API_TOKEN=""` and `APP_TOKEN="x"`:
- `check_env.sh`: `:=` fills from `APP_TOKEN` because the value is empty, `:?` passes, and it prints `ok`.
- `settings.py`: the membership test succeeds, so `TOKEN == ""`.

The guard therefore reports `ok` while the application gets an empty token. Before the change, both consumers read one variable and the guard rejected empty values. The report describes each rule separately but not this divergence. The host executions (new-only, missing) do not cover this input. Actor result 2 ("every consumer reads `APP_API_TOKEN`") is literally true but omits the retained old-name read.

**F2 — Effect labels on returned proposals (C3, C6, C8, D1; low).** These actors label their own file writes `not_started` (C6 says "not_started until host applies").

Source basis:
- `not_started` "needs evidence that the selected effect did not begin".
- "Transport dispatch alone proves neither effect completion nor absence".
- The boundary includes "each material part the operation may have affected under its supported operating model".

Returning replacements for the host to apply is that dispatch. After handoff, the actor's evidence supports only `unknown`, which is how C1, C4 and C7 label it.

Counterexample: the host confirms the after-state equals the original plus the full replacements. So C8's named boundary files (`utils/paging.py`, `tests/test_paging.py`) were changed, and likewise C3's CHANGELOG and STATUS, C6's STATUS and D1's four files.

C3's composite "partial" needs an *observed* unexecuted remainder. After dispatch the remainder's completion is unknown, so the composite should be `unknown`, with the completed rollout retained as evidence. C6's time qualifier mitigates the problem but does not change the post-handoff value.

No verdict or oracle check is affected. The host checks cannot see this defect.

**F3 — C3b performance coordinate (low; one reading only).** For the predicate "deploy r-77 has completed", the actor declares its basis as the registry, RUNBOOK and session log. Its outcome then records reading the registry and concluding that the snapshot predates the request.

That is an evaluation actually undertaken that reached an undecidable conclusion. The source's load-test example classes this as performed/indeterminate, not as "evidence establishes the evaluation was not undertaken". C3's actor labelled the identical procedure `performed`.

`not_performed` would be defensible only if the declared evaluation were a fresh owning-interface observation, and that is not the basis the actor declared. The verdict, the lawful stop and the next action are unaffected.

## Non-finding notes

- **N1 (C4).** V1's result cell still begins with the literal `pass (stale: … replaced by V3)`, and the re-evaluation is a new record V3 rather than V1 rebased to v2. This meets the oracle's "explicitly invalidated" alternative in substance, and the host counted it met. A reader that takes the result column literally would still see "pass" for V1. The gate stays blocked through V3 either way.
- **C8.** The negative-total behaviour change is unspecified by the oracle, disclosed by the actor and observed by the host. It is left as owner input, not graded.
- **C1.** The applied HANDOFF still says "edit proposed" and "pass/fail unconfirmed". That was accurate at handoff; the host test run supersedes it as evidence but does not rewrite the record.

## Scope limits

- **Selected excerpts only.** I graded against the supplied excerpts. Actor citations to RF-005/006/012/015, UP-020, STDO-UP-007, TRANSFORMATION_LIBRARY and the Condition-Based Closure rule point to text not supplied here. I did not verify them and did not count them for or against any actor.
- **Edits and results only for C4–C7.** Narrative reports for C4, C5, C6 and C7 were omitted, so those cases are graded on edits and structured results alone.
- **Host evidence taken as supplied.** I did not inspect ASSERTIONS.json commands or traces, or re-run anything. Each host check's mapping to an oracle condition is inferred from its name; the D1 first-check mapping is noted above.
- **Application and test success are not semantic correctness.** The 10/10 applications and the passing executions establish that the edits applied and the listed behaviours hold. They do not validate effect or performance labels (F2, F3), and D1 passes every execution while failing an oracle check.
- **No acceptance inferred.** I infer no release acceptance or closure:
  - C3's completion rests on a fixture registry with no service invoked.
  - C5's falsified gate is an evaluation record, not a disposition.
  - C8 and T-31 closure are not recorded.
- **Oracle unchanged.** I did not alter the oracle, and I neither invented nor credited any review.
