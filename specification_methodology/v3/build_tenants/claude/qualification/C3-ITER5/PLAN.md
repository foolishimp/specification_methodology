# Iteration 5 Plan, Claude Line

Activation plan for the Claude line's iteration 5 (I5) under the ratified
common input C3-I5-06 and the contract EC-CLAUDE-I5-01. It is written by
the Executive in the main session. It claims nothing accepted. Terms are
defined in the [I3 plan](../C3-ITER3/PLAN.md); the I3 conventions (its
section 3) and the I4 conventions ([I4 plan](../C3-ITER4/PLAN.md),
section 3) apply unchanged unless a line below says otherwise.

## 1. Basis

| Coordinate | Value |
|---|---|
| Common input | C3-I5-06: common specification at `4c340f7adec9f3c893e3e267b23e4cadeb357854` on `main`, 47 members recorded at `3ff9dfd`, merged inward at `0a05106`. Every requirement, conformance, Product, Intent and frame-basis byte equals `4c340f7`; the seven work-state records differ only by the pen's later recordings and this line's posts |
| Ratification | the product owner, 2026-10-16T15:11:14Z: "ocntinue" to the pen's request to ratify `4c340f7`, recorded in T-001 "Iteration 5 ratification" (main `2ec695f`); "continue" to this session |
| Contract | EC-CLAUDE-I5-01, posted at main `4f6307f`: 4,529 UTF-8 bytes, SHA-256 `d1e07305c372142e03b3d8dc4a44ade6d31ab30508c4d656db1cdb0a81338b92`; admitted in the [ledger](../C3-SYNTHESIS/LEDGER.md), section "Iteration 5" |
| Preceding candidate | `c66ed4e` on `tenant/claude/c3-synthesis`, tenant tree `9e08290ab4ad6e297942d949145f089dd6741d46`, handoff `1092f9a` ([I4 handoff](../C3-ITER4/HANDOFF.md)) |
| Donor | the frozen Codex iteration 4 candidate: return `9a93c5a`, package `903f119`, read only through `git show` at those commits |
| Comparison subjects for reduction | the installed `v2.5.1-rc.2` (manifest `3d860ff4…2782`) and the preceding candidate `c66ed4e` |
| Work list | T-002 "Iteration 5 consolidated work": I5-01 to I5-09 and the assurance duties I5-A1 to I5-A7 |
| Recheck before admission | main `4f6307f`, `comments/claude/20261016T151236Z_PREADMISSION_CLAUDE_I5_RECHECK_C66ED4E.md`: eight digests reproduce; Codex's R1 to R4 repaired; three residuals (SPEC_METHOD §2 provenance clause, trial A0 arm row, stale readback sentence in RESULTS.md) |
| Checker | the pinned Axiom Indexer `v2.5.1-rc.2`, structural validation only (owner decision, I3) |

## 2. Work items

The order follows the contract. "Owner" means the candidate section that
states a rule; "consumers" are the sections that apply it. The common
owner of each item is named in T-002.

| # | Item | This line's work | Return |
|---|---|---|---|
| 1 | I5-01 rebind, with I5-A1 and I5-A6 | `REBIND.md`: every common decision changed in `3c4c503..4c340f7`, its effect on this candidate and its task. Then the construction relation (A, Z, strategy, composition, feedback, and the distinction of preservation, progress and completion) at its owner in FOUNDATIONS, with the formal preservation obligations (A1) and validity dependencies distinct from justification links (A6), and the consumer bindings in SPEC_METHOD, TICKETS, EXECUTIVE_BASELINE, EVALUATION, ACTIVATION and RELEASE | `REBIND.md`; owner and consumer text; `returns/I5-01.md` |
| 2 | End-to-end delivery-and-correction path | One feature carried through the candidate's own law: intake, construction, discrepancy, diagnosis, correction, reassessment and closure, with an interruption, an uncertain effect and a valid reuse. The subject is a real item of this line selected at the end of I5-01. It is the first integrated case | `returns/E2E-01.md` |
| 3 | I5-02 deciding laws and generic bindings, with I5-A2 | The I5 dependents of the chain repair; generic procedures and the permitted human and mixed bindings at ACTIVATION, TICKETS and RELEASE; family tables name actual consumers or a supported absence; one owner for assertion versus execution provenance and for necessary versus sufficient conditions; evidence wording aligned to the demonstration standard | `returns/I5-02.md` |
| 4 | I5-08 entry and package standing | The chain provenance clause moved out of SPEC_METHOD §2 into design history; the tenant README at I5; the package entry separates target version from released status | `returns/I5-08.md` |
| 5 | I5-06 frame use and grading, with I5-A4 | The A0 arm row aligned with §7; every frame binds the construction requirement; assurance and reassessment bindings as task-specific fields of existing frames; expectation sets carry assertion provenance; weak-assertion and ambiguous-observation cases designed through ordinary entry. The run waits for the product owner | `returns/I5-06.md`; `trial/` |
| 6 | I5-05 interpretation and acquisition, with I5-A3 | Offered-entry acquisition reproduced from a clean checkout with adverse controls; `a_c/i3` represents the construction and assurance obligations with the five standings (stated formula, discharged argument, checked structure, external predicate, execution evidence); positive, negative and unresolved fidelity cases; uncovered scope stated | `returns/I5-05.md`; `a_c/i3/` |
| 7 | I5-04 received contributions | The frozen Codex I4 candidate evaluated as donor; adaptation or reasoned exclusion per part; receiving-line nonauthor assessment of selected ports | `ports.md`; `returns/I5-04.md` |
| 8 | I5-03 conservation and owner decisions | The remaining `conserved` rows read in fresh contexts, or their unread scope stated exactly; the owner's replacement decisions carried when made; one consolidated decision list | `reassess/`; `returns/I5-03.md` |
| 9 | I5-07 reduction and costs, with I5-A5 | Paths traced against rc.2 and `c66ed4e`; the README tradeoff declared or removed; the two residual rivals; the selected assurance assessed against obligations, consequences, uncertainty and total cost | `paths/`; `returns/I5-07.md` |
| 10 | I5-09 integrated review and comparison, with I5-A7 | Discriminator mapping on the three tables and the four new integrated rows; results table corrected; nonauthor readbacks of changed material and its dependents; freeze; handoff | `RESULTS.md`; `HANDOFF.md` |

## 3. Conventions changed for I5

- Reviewer model: Fable at maximum effort in a fresh context, never a fork; one subagent at a time; exact file scope; findings withheld from the reviewer's prompt. Each review gets one triage, one repair round and one successor readback.
- Evidence reuse from I4: each reused result states its validity conditions on the new subject under the assurance requirement's change-impact rule (I5-A6). Unchanged bytes alone do not carry a judgment forward. The 140 conservation readings, the seven desk traces, the port readbacks and the checker controls are reused only on that account.
- Vocabulary: "categorical join" for a map between categories; "composition boundary" for the join between successive construction steps; `indeterminate` for the judgment whose admissible evidence cannot decide the predicate; `unresolved` for work or coverage.
- Common defects go to the pen as posts on `main`. No common file is edited from this line.
- Ledger timestamps are UTC from `date -u` at the time of writing.

## 4. Budget

Native Fable session for construction; reviewer subagents as above; no paid external calls. Token and context figures are reported where the harness reports them and otherwise stay uninstrumented; no fit claim rests on them. The product owner's I4 instruction that readings run on Fable at max, lifting the token constraint of D8, is read as carrying into I5 until the owner says otherwise.

## 5. Open owner decisions carried

1. The replacement relations: 17 rows in 9 questions plus 10 compressions (main `708dfb9` and [the supplement](../C3-ITER4/reassess/REPLACEMENTS-SUPPLEMENT.md)).
2. The UX compliance-test replacement.
3. Identity and packaging of the released interpretation.
4. The actual-use trial: shared protocol, resources and the decision to run. Criterion 4 stays `unresolved` until then.
5. Acceptance-review assignments and the cross-family review of this line's candidate.
