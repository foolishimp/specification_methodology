# Installed-route task 02: exhaustion and separate result predicates

**Scope.** This is test use only: it is not acceptance or consumer adoption. I used only Read, Glob and Grep, all inside the installed root, and wrote nothing. I did not recompute the manifest, payload or installed-byte digests. I did no structural check of the subject, and I don't claim that v_copy or v_sorted qualify as deterministic (`F_D`) operations. I took the two task contracts as given.

## Sources I actually read
All paths are relative to the installed root.

- `standards/README.md`, the whole file. Its route table pointed me to ACTIVATION §3 and FOUNDATIONS §4 Results.
- `standards/AXIOMATIC_CALCULUS.md`:
  - lines 536–630: AC-007, constraint and operation outcomes.
  - lines 950–1093: §5 stop algebra, `F_D`, exhaustion and totality, AC-015.
- `standards/ACTIVATION.md`:
  - lines 73–76: family-table rows.
  - lines 166–197: §1 Transitions, Completion and Stops.
  - lines 298–349: Construction relation.
  - lines 938–1087: §3 Step results.
  - lines 1120–1199: end of Effects, and §4 Totality.
  - lines 1370–1391: start of §5.
  - lines 1627–1680: §6 Resource limits.
- `standards/FOUNDATIONS.md`:
  - lines 730–936: §4 Results, with the F3 family table.
  - lines 937–1055: Conjunction of results.
- I located these through Grep for `exhaust|fuel`, `AC-007|stop contract|stop_states` and the section headings.

**Not acquired.** `standards/examples/DETERMINISTIC_CONTRACTS.md#exhaustion` is cited by `ACTIVATION.md:1180-1181` and `AXIOMATIC_CALCULUS.md:1054-1055`. The task limited me to the README, AXIOMATIC_CALCULUS, ACTIVATION and FOUNDATIONS, so I didn't read it. README line 66 says it carries "no generic law or acceptance authority", so the decisions below rest only on the owning clauses.

## Clauses used in every case
- **`F_D` outcome.** The traversal produces exactly one outcome, "including a stop with its closed report where declared; that report and its stop are not two outcomes. An enclosing step's output availability remains a separate predicate" (`AXIOMATIC_CALCULUS.md:996-999`).
- **Exhaustion.** "Refusal and exhaustion retain their cause and evaluated predicate… an exhausted tag alone supplies no mapping. Construction availability and assessment retain their separate predicates and results, and an unperformed assessment has no result. A fuel-bounded operation is distinct from the potentially divergent operation it bounds" (`AXIOMATIC_CALCULUS.md:1002-1008`).
- **Stop declarations.** The signature's stop contract declares any further stop value and the one core value it maps to. No stop maps to `satisfied` (`AXIOMATIC_CALCULUS.md:961-979`).
- **Totality.** "Fuel exhaustion retains the evaluated predicate; candidate absence, an available indeterminate assessment report and an unperformed assessment take the different results of §3" (`ACTIVATION.md:1177-1181`).
- **Recording.** Every result records its core value, its predicate and its domain outcome (`FOUNDATIONS.md:751-756`). Availability, assessment and acceptance are three separate predicates (`FOUNDATIONS.md:817-825`; `ACTIVATION.md:956-962`).

## Case 1: `v_copy([0,1],1)` produces only the prefix `[0]`

| Item | Decision | Citation |
|---|---|---|
| Domain outcome | v_copy's declared stop `copy_exhausted`, cause "fuel ended before the required output". This is the one `F_D` outcome. The prefix `[0]` is partial material, not the required candidate. | `AXIOMATIC_CALCULUS.md:967-969, 994-999, 1002-1003` |
| Evaluated predicate and result | Predicate: "this fuel-1 application yields the required complete copy of `[0,1]`". Result: **`falsified`**, from the declared core value of `copy_exhausted`. Counterexample: fuel ran out after one element, so element `1` was never copied. | `AXIOMATIC_CALCULUS.md:967-979, 1002-1005`; `FOUNDATIONS.md:738, 760-761` |
| Availability of the work result | If an enclosing constructing step's declared output is the complete copy, its availability is **`incomplete`**, which maps to `falsified` for "a candidate is available". The cause is that bounded execution ended first. Handing over `[0]` as the candidate would substitute a different subject. | `ACTIVATION.md:1013, 1017-1021, 1026-1027`; `AXIOMATIC_CALCULUS.md:998-999` |
| Fitness or acceptance | No assessment and no disposition were performed, so there is no result. | `FOUNDATIONS.md:780-782`; `ACTIVATION.md:1051-1058` |
| Who owns the stop | v_copy owns `copy_exhausted`, through its signature's stop contract or its traversal `stop_states`. The enclosing step owns its own `incomplete`. These are two predicates, and two `falsified` values that should not be merged. | `AXIOMATIC_CALCULUS.md:967-972`; `ACTIVATION.md:174-176, 1002-1007` |

## Case 2: `v_sorted([0,1,0],1)` inspects only `(0,1)` and issues its declared closed report

| Item | Decision | Citation |
|---|---|---|
| Domain outcome | v_sorted's declared stop `assessment_exhausted` together with its closed report. Basis: input `[0,1,0]`, fuel 1. Evidence: pair `(0,1)`, no inversion. Residual: pair `(1,0)` was not inspected. The stop and the report are one outcome, not two. | `AXIOMATIC_CALCULUS.md:996-998` |
| Evaluated predicate and result | Predicate: "`[0,1,0]` is sorted". Result: **`indeterminate`**, because the admissible evidence cannot decide it. The residual names what would decide it: inspecting `(1,0)`. It is not `falsified`, because v_sorted observed no inversion. It is not `satisfied`. | `FOUNDATIONS.md:739, 761-764, 842-844`; `AXIOMATIC_CALCULUS.md:973-976` |
| Availability of the work result | The assessing step's output is its closed results (`ACTIVATION.md:1004-1006`), and the declared output is the complete report including its residual. So availability is **`candidate_ready`**, which maps to `satisfied` for availability only. This assumes the step's transition evidence exists, which the task doesn't state. If an enclosing step's declared output instead required a decided verdict, its availability would be `incomplete`. | `ACTIVATION.md:1011, 1013, 1023-1024, 1026-1029, 1178-1180` |
| Separation of predicates | The `satisfied` for availability never counts toward sortedness or acceptance. | `FOUNDATIONS.md:1009-1013` |
| Who owns the stop | v_sorted owns `assessment_exhausted`. The step does not stop, because `candidate_ready` is not a stop. | `AXIOMATIC_CALCULUS.md:967-969`; `ACTIVATION.md:174-176` |

From the stated input, I can see that `(1,0)` is an inversion. That observation is not v_sorted's result and does not change its `indeterminate`. An admitted evaluation that actually inspects `(1,0)` would be a separate performed evaluation with its own `falsified` result.

## Case 3: setup budget exhausted before v_sorted is invoked; no report exists

| Item | Decision | Citation |
|---|---|---|
| Domain outcome | None for v_sorted. "An operation that was not applied has no outcome." No `assessment_exhausted` is issued, and an exhausted tag on its own supplies no mapping. | `AXIOMATIC_CALCULUS.md:620, 1004-1006` |
| Evaluated predicate and result | Sortedness was **not performed, so there is no result**. It is never `indeterminate` and never `falsified`. In any conjunction it is a planned assessment without a closed result, which counts as a gap. | `FOUNDATIONS.md:773-776, 780-787, 953-956, 961-966`; `ACTIVATION.md:943, 1036-1038` |
| Availability of the work result | I read "assessing step" as a lawfully activated step. On that reading, availability is **`incomplete`**, which maps to `falsified` for "a candidate is available". The step must name the setup-budget limit. That `falsified` "concerns its own output, never the subject under assessment". The work state carries the unperformed assessment as a residual. | `ACTIVATION.md:1013, 1029-1032, 1037-1039, 1653-1659, 180-182` |
| Who owns the stop | The assessing step, under ACTIVATION §3 and §1 Stops. v_sorted owns no stop, because it was never applied. | `ACTIVATION.md:174-176, 1002-1021` |

**Alternative reading.** If the setup budget ran out before lawful admission or activation, no step exists. Then this is an admission or activation outcome, for example `out_of_frame` when no fit option fits the actor's envelope. It would not be a value of availability and would not be a work result (`ACTIVATION.md:988, 991-997, 1020-1021`).

**Omission rule.** Pressure on the budget never permits skipping the assessment and reporting anyway (`ACTIVATION.md:1653-1654`).

## Does an exhaustion report prove the missing domain property?
No.

- **Case 1.** `copy_exhausted` falsifies only its own bounded predicate. It does not show that `[0,1]` can't be copied, and it says nothing about the unbounded copy. "A fuel bound … proves nothing about the unbounded original" (`AXIOMATIC_CALCULUS.md:1007-1008, 1048-1050`).
- **Case 2.** The report establishes neither sortedness nor unsortedness (`FOUNDATIONS.md:761-764`).
- **Case 3.** There is no report and no result.
- **General rule.** "A resource limit can end an attempt with an unresolved outcome; it establishes neither achievement nor impossibility." "Exhaustion or an unresolved attempt proves neither completion nor impossibility" (`ACTIVATION.md:314-316, 329-330`, and the family row at line 76). Only `satisfied` establishes a predicate (`FOUNDATIONS.md:760`).

## A retained falsifying counterexample when later work exhausts
Suppose an earlier performed evaluation returned `falsified`, for example v_sorted with enough fuel to observe the inversion `(1,0)`. The rules for what follows:

- **The failure survives.** It is a known failure and survives every join. Agreement among contributors can't discard it, and a stop discards nothing (`FOUNDATIONS.md:997-1007`; `ACTIVATION.md:180-182`).
- **The later stop stays separate.** If later work exhausts, its `incomplete` answers only its own availability predicate. Its unperformed evaluations have no result and are gaps (`ACTIVATION.md:1026-1039`; `FOUNDATIONS.md:849-865`).
- **Nothing merges.** Neither the later stop nor its gap turns the counterexample into `indeterminate`, and the counterexample doesn't resolve the gaps (`FOUNDATIONS.md:1009-1013`).
- **The composite is never `satisfied`.** Which non-satisfied value it reports belongs to the conjunction's declared rule. No universal order applies, and the gaps stay recorded by kind (`FOUNDATIONS.md:1015-1033, 1040-1045`).
- **Reuse is bounded by basis.** The retained result supports its predicate only on the basis it binds. Reusing it requires re-checking its invalidators. If the list changed, it is stale (`FOUNDATIONS.md:968-991`; `ACTIVATION.md:1383-1384`).

## Gaps and assumptions
1. **Predicate wording.** The owners don't fix the wording of the predicate for a stop declared by a domain traversal. AC-007's operation predicate (`AXIOMATIC_CALCULUS.md:577-578`) covers only a_c operations. I took the predicates from the task contracts plus "retain … evaluated predicate" (`AXIOMATIC_CALCULUS.md:1002-1003`).
2. **Status of `copy_exhausted`.** "Parent core value `falsified`" might mean a further stop value with its own core value, which `AXIOMATIC_CALCULUS.md:967-968` allows. It might instead mean a child of `refusal(constraint)` (`AXIOMATIC_CALCULUS.md:976`, ground at line 585). The installed text doesn't decide between these. Either way the core value is `falsified`.
3. **The prefix `[0]`.** A state-dependent operation must declare what its returned next state means (`AXIOMATIC_CALCULUS.md:1001-1002`). The contract doesn't, so whether `[0]` stands as retained partial state is unsettled.
4. **Unstated facts.** Three things the task doesn't state, which I assumed:
   - that case 2's transition evidence exists;
   - that case 3's step was lawfully activated;
   - that the setup budget was a declared limit (`ACTIVATION.md:1634-1641`).
5. **Effects and disposition.** No external effect is involved and no decision owner acted, so the Effects and Disposition refinements give no result here.
