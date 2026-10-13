# Independent fidelity assessment: rebuilt core finite interpretation

**Basis and limits.** I read only the supplied source excerpt (Foundations: Result algebra, Result conjunction, Workspace and context, Bounded construction, Configuration, Core contract derivations) and then the artifacts. I used no tools:

- I did not execute `finite_check.py`.
- I did not see `SOURCE_INVENTORY.json` or `program.json`.
- I cannot confirm that the excerpt matches the pinned digests.

Statements about runtime behaviour below come from reading the code. By reading, I found no fixture the check would fail. I make no whole-corpus, native-agent, transport or release claim.

**Same-Writer separation versus this judgment.** The set-based `oracle()` and `model.conjoin` encode the same interpretation of the input tokens. One example is `I` meaning an authenticated `invalid_basis` judgment. Their agreement on 1620 cases therefore shows the code is consistent. It does not show the code is faithful to the source. The findings below are my own reading of the source against the artifacts.

## Overall judgment

The fixtures preserve the source in several areas:

- Conjunction precedence
- Effect join
- Temporal normalisation
- Operator well-formedness
- The recovery table

Three material defects and several overclaims prevent a clean fidelity acceptance:

| # | Severity | Area |
|---|---|---|
| 1 | **High** | The legal-coordinate guard and `evaluation()` contradict each other, and the guard is not total |
| 2 | **High** | Domain refinement has no reason domain, no missing-reason case, and is not total |
| 3 | **Medium** | `negate_result` can turn a failed required join into `satisfied` |
| 4 | **Medium** | Four "actual faulty-function" counterexamples are vacuous or literal |
| 5 | **Medium** | Recovery, Construction and Configuration have no meaningful executable interpretation |
| 6–10 | Low–Medium | Gaps in coverage, retention and naming (below) |

## Preserved semantics (positive findings)

- **Conjunction precedence** (Result conjunction, steps 1–4 and the uninterpretable-composite paragraph). `conjoin` gives:
  - an uninterpretable outer basis → `invalid_basis`, with failures and citations kept (oracle row `outer-basis-invalid`);
  - otherwise falsification first, then `invalid_basis`, then `out_of_frame`, then `indeterminate`;
  - `satisfied` only when every slot is S and coverage is established.
  
  A false required join is treated as counterevidence, not as a missing basis, which matches "names that declared role…". Unauthenticated `X` cannot discharge an obligation. `H` (aborted without return) is kept as a missing slot with performance `performed` and extent `partial_aborted`, which matches "An interruption does not erase evaluation already undertaken". I agree with these readings independently.
- **Thirteen legal pairs** (Result algebra, legal-pairs table). The count of 5+4+4 is correct, and `satisfied` requires `performed` plus completion.
- **Evaluation fixtures.** These match the source's own examples: the inadequate load test is `performed`/`indeterminate`, the aborted suite is `performed`/`falsified`, and independent counterevidence or a basis diagnosis on a not-run or unconfirmed evaluation is admitted without inventing execution.
- **Effect join** (Result conjunction, "Over the resulting disjoint part observations…"). `_fold_states` is exactly the source table. The 216-case check uses a separately derived unit-level formula and tests associativity over disjoint grouped boundaries.
- **Temporal normalisation.** Fixtures cover:
  - completed deployment then rollback → `reverted`; reapplication → `completed`;
  - a timestamp alone never supersedes;
  - unsupported supersession → `unknown`;
  - reversal without evidence the part began → `unknown`;
  - an irreversible message survives local rollback → `partial`;
  - an unrequested part observed not begun → `not_requested`, with its observation kept;
  - a requested part observed not begun → `not_started`;
  - no request alone → `unknown`.
  
  All of these match the source.
- **Operators.** Truth and falsity must be disjoint and exhaustive. A required join of 0 must be falsified. Unestablished well-formedness → `indeterminate`. An overlapping table, a gap, or an ignored join → `invalid_basis`.
- **Recovery table.** Retry with `unknown` effect requires both a grant and established idempotence; otherwise the model observes or returns unresolved.

## Findings

### 1. High: the coordinate guard contradicts `evaluation()` and admits no verdict for valid fixtures

**Source:** Result algebra. "Without deciding support it is indeterminate." A missing completion condition also blocks satisfaction.

**What the code does:** `legal_coordinates` treats any `deciding` value as admissible deciding support. For `indeterminate` it requires `deciding is None`. But `evaluation()` passes *claimed* support in `deciding` and filters admissibility itself. Three fixed fixtures therefore yield results that the model's own guard rejects:

| Fixture | `evaluation()` result | Guard accepts any verdict? |
|---|---|---|
| `claimed-success-without-undertaking` | (`unconfirmed`, `indeterminate`) | No |
| `counterevidence-no-independent-support` | (`not_performed`, `indeterminate`) | No |
| `undertaken-but-completion-obligation-missing` | (`performed`, `indeterminate`) | No |

For each of these evidence states, **every** verdict is illegal under the guard. That breaks F5 total handling for this domain.

**Why the check misses it:** the 180-case probe only ever pairs `indeterminate` with `deciding=None`, and decided verdicts with `deciding == verdict`. It never probes a mismatched or inadmissible `deciding`. It also never runs `evaluation()` outputs through `legal_coordinates`.

**Fix:**
- Compute admissibility inside the guard, or split the field into `claimed_support` and `admissible_support`.
- Add a check that every `evaluation()` output passes `legal_coordinates`.
- Extend the probe so `deciding` ranges over `None` and all five verdicts.

### 2. High: domain refinement lacks the reason domain and the missing-reason rule

**Source:** Result algebra, refinement paragraph. A refined value is the pair (original outcome, cause) with an explicit missing-reason case. The map must be total and reason-sensitive. "A consumer cannot guess from a word such as `refused`, `ready` or `accepted`." A missing reason leads to `indeterminate`, inadmissible support, and the raw outcome kept.

**What the code does:** `refine(domain, predicate)` has no cause input. It maps bare outcome words such as `out_of_scope` and `candidate_ready` directly to verdicts. It raises on any pair it does not list. As a result:

- The `refused_predicate_substitutions` cases pass because *any* unlisted pair raises. The test cannot tell a principled refusal apart from an unmodelled case.
- The missing-reason case is absent.
- "Unconfirmed performance stays unconfirmed" is absent; performance is hard-coded to `performed`.

The scope claims "domain refinements" under Results. Either add a reason coordinate with a total map that includes a missing-reason fixture, or narrow the scope statement.

### 3. Medium: `negate_result` flips a bare verdict

**Source:** Result conjunction. "Negation… evaluates a different predicate; it cannot erase a failed leaf." Any declared operator must also be falsified when its required join fails.

**What the code does:** `negate_result(apply_operator(and_table, True, True, False))` gives `falsified` → `satisfied`. A failed required join is promoted to satisfaction. The negated table would fail the model's own `operator_wellformed`. The output also carries no predicate binding, so it can be mistaken for the original predicate's result, contrary to "does not overwrite the earlier result".

Only the `indeterminate` and `invalid_basis` paths are tested. The fix is to express negation as its own declared table, checked by `operator_wellformed`, rather than as a verdict flip.

### 4. Medium: several "actual faulty-function" counterexamples are vacuous

**Claim:** the scope says actual faulty functions cover twelve defects.

**What the code does:** four entries do not execute a faulty rule against the oracle:

- **`candidate-means-fit`** compares a dict to the string `'refused predicate substitution'`. They are always unequal, so detection is vacuous.
- **`later-timestamp-is-supersession`** uses a literal state from the fixture as `actual`; no function runs.
- **`arbitrary-operator-is-associative`** compares two hand-computed Python booleans. It is a valid counterexample to associativity, but no mutant claiming associativity is run.
- **`reset-erases-workspace`** uses a literal dict.

The other eight are genuine one-rule mutants:

- erased failure
- invented performance
- inconclusive run called unperformed
- unknown effect called not started
- out-of-scope word relabelled out of frame
- unknown remainder called partial
- raw labels folded together
- blind retry

### 5. Medium: Recovery, Construction and Configuration are essentially uninterpreted

**Source:** Workspace and context requires that recovery:
- reacquires current state and authority,
- invalidates affected claims when support changes,
- keeps unchanged independent work,
- applies freshness and concurrency conditions.

**What the code does:**
- The context-reset trace runs `context.clear(); context.update(workspace)`. It is equal to the workspace by construction, so it proves nothing about reacquisition. The `r0→r1` basis change is never used to invalidate a claim.
- `recover()` takes `grant` as an input. Nothing models reacquiring authority, or the rule that "context loss… creates no authority".
- A `not_started` observation leads to `permitted_initial_dispatch` with no freshness check.
- Bounded construction (total control responses, preserving outer obligations) and Configuration have no executable at all.

The scope's "This interpretation covers… bounded construction and configuration laws" should say that these are covered by textual reading only. The finite artifacts supply no evidence for them.

### 6. Medium: the conjunction result has no effect coordinate

**Source:** Result conjunction. The aggregate keeps uncertain effects. "Effect uncertainty prevents satisfaction where the predicate requires a known effect state." Parts owned by an absent slot must also be normalised.

**What the code does:** `conjoin` returns no effect value. Effect composition is tested only in isolation, so no fixture links an `unknown` effect to blocked satisfaction, or an absent slot to its affected part.

### 7. Low–Medium: the associativity check tests verdicts only

**Source:** "Retained component sets combine by union."

**What the code does:** the 125-case AND check re-encodes inner verdicts as single tokens. That discards failures, citations and missing slots, and outer `failures` would name the wrong component. Union of retained components is never checked. The verdict associativity itself is correct.

### 8. Low: `observe_effect` defaults unknown tokens to `not_started`

An unexpected unit value such as `'x'` falls through to `not_started`. That is the same "unknown promoted to nonstart" defect that one of the mutants targets. `_fold_states` validates its domain; `observe_effect` should too.

### 9. Low: naming ambiguities

- **`I` labelled "invalid contribution".** In the source's authentication paragraph, "An invalid contribution does not erase an independently authenticated finding" means a contribution that *failed authentication*. That would leave the slot uncovered → `indeterminate`. The fixture uses `I` for an authenticated `invalid_basis` judgment instead. The expectation is right under that meaning; rename it, e.g. `invalid-basis-judgment`.
- **`missing-planned-evaluation` uses `M`, which is always `not_performed`.** The source warns that an absent return does not establish non-performance. The domain does keep `N` for the unconfirmed case, so this is a naming issue, not a semantic one; rename it to `known-unperformed-planned-evaluation`. Also, `N` is excluded from `missing_evaluations` although it is an absent slot.
- **`fallback-satisfied-earlier-failure-retained`** checks only the verdict string. Retention of the failed leaf is not checked.

### 10. Low: declared but unstated domain limits

These source rules are outside the finite domain and should be listed in the limits:

- Applicability and not-applicable judgments (step 3, and "A not-applicable classification needs…").
- Conjunction slots that are `not_performed` or `unconfirmed` but carry independent counterevidence. `conjoin` hard-codes `F`, `I` and `O` as performed.
- Unauthenticated or missing joins (joins are drawn only from `SFUOI`).
- Non-Boolean operator leaves and "only dependencies needed to decide" ordering.
- Ordering of temporal observations, which comes from list position. That is an implicit ordering stipulation that should be declared.

## Scope limits of this assessment

- **Not established by this review:**
  - source fidelity for the material families
  - the traversal semantic-cut dependency
  - domain policy
  - predecessor dispositions
  - installation, transport or exactly-once behaviour
- **Supported, with Findings 1–3 fixed:** a finite-interpretation claim limited to:
  - AND precedence
  - the effect join and temporal fixtures as stipulated
  - Boolean operator well-formedness
  - the recovery decision table
- **Should be withdrawn or narrowed until fixed:** the claims about the evidence guard, refinement, negation, the twelve faulty functions, and Recovery/Construction/Configuration coverage.
