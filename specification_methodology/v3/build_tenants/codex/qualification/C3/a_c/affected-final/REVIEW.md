# a_c Interpretation Review: source 0ff2ed70, finite C3 token model

**Method.** You said no tools, so I ran nothing. I did not run `ac.py` or the executable. Every finite-behaviour result below comes from tracing the code by hand against the material you supplied. I did not resolve any references outside that material (`successor/standards/*`, the calculus).

## 1. Three separate verdicts

| Axis | Alpha (`permission-mutant`) | Beta (`source-v1-refined`) | Basis |
|---|---|---|---|
| Structural / project / join validity | **Not verified** | **Not verified** | `ac.py` was not run. The structural concerns in §4 are open, not confirmed. |
| Finite behaviour (executable on its declared domain) | n/a: the executable reads neither program | n/a | Hand trace: every assertion holds (§3) |
| Source fidelity | **FAIL** (permission) | **PASS with findings** (§2) | Source comparison |

A passing finite run does not support either program, because the executable hashes only `SOURCE.md` and itself, not Alpha or Beta. A passing `ac.py` check would not establish fidelity either.

## 2. Source-fidelity results by relation

**Token model and permission**
- **Alpha: FAIL.** Its `clause:permission` premise says *"A named current owner or display label supplies permission without an exact grant"* and its statement says *"Naming an owner or display label authorizes the assignment."* That directly contradicts the source: "A display label grants no permission", and permission is the exact issuer/token/destination/operation grant.
  - Alpha also drops the `symbol:permission` premise, leaving that symbol declared but unused.
  - It omits "assign only" and the inspect exclusion.
  - It contradicts itself: its own qualification says missing exact permission is refused.
  - The error spreads, because `clause:token-transfer` takes `clause:permission` as a premise.
- **Beta: PASS.**
  - **Exact grant tuple:** issuer must be the selected token's current owner, with the exact token, the destination, and operation `assign`. A label or an inspect grant supplies nothing. Unknown observation → unresolved, no effect. Known state with missing permission → refused, no effect. The token set and single-valued ownership are conserved.
  - **Resumption:** "re-observes actual state; no universal idempotence" is kept.
  - **Scope:** owners A/B and tokens t0/t1 are not named in any clause; they appear only in the symbol label. That is acceptable as implicit, but AC-017 would prefer a stated disposition.

**Typed joins: PASS (qualitative only, both programs)**
- Length→Duration is incompatible.
- ms→s requires ÷1000, and that direction is correct.
- "Compatible types confer no operation permission" matches "no source grant".
- "despite equal float representations" survives only in the statement ("Field-shape equality…"), which is acceptable.
- Nothing executes this relation.

**Finding conservation: content PASS, with three findings (both programs)**
- The premise and consequence keep: exactly slot A, source-v1, the one original producer, A falsified, the citation `source/A.md#permission-branch`, B uncovered, and non-green.
- **F1 (indexing).** `clause:finding-conservation` appears in no frame index. `index:findings` lists only `clause:role-boundary`, has empty `residual_refs`, and states a scope ("Conserve A falsified and B uncovered") that its own clause never backs. `clause:permission` is also unindexed.
- **F2 (weakened).** The source says "If A is not *supplied/authenticated*". The qualification covers only a "missing planned judgment". A slot that is supplied but unauthenticated fails the premise, but nothing says that invalidates the complete planned-set claim.
- **F3 (implicit).** The source says B is "not an omitted planned slot". The program only implies this through "Exactly planned slot A".

**Global selected-predicate authority and recovery: PASS (qualitative)**
- `role-boundary` takes finding-conservation, token-transfer (and through it, permission) and typed-join as premises. It qualifies them with "no action or acceptance grant; the decision owner acts only within its existing grant".
- `effect-recovery` carries its own "no operation authority follows".
- So every selected predicate is covered by a no-authority statement.
- The six distinct claims (finite model success, source fidelity, practical adequacy, category equivalence, corpus qualification, release) appear only in the residual detail, not as a clause. That is a weak placement, but they are present.
- **Recovery:** "observe/reconcile or stop unresolved before a potentially duplicating retry" matches the source.

## 3. Executable token model: hand-traced finite behaviour

**Domain and counts**
- The domain is 4 owner states × 2 tokens × 2 destinations × 19 grants × 2 observation flags = **608** cases. The 19 grants are none, 2 labels, and 16 typed grants.
- Unresolved: **304** (every unobserved case).
- Completed: **16**. Each of the 16 known (state, token, destination) combinations has exactly one matching typed grant.
- Refused: **288** (16 × 18 non-matching grants).
- Labels are strings, so `isinstance(grant, dict)` is false and they are never admitted.
- All counting assertions hold.

**Exact grant tuple**
- The guard checks issuer = `owners[token]`, then token, destination and `assign`.
- The inverse postcondition is `grant == {...}`, a full dict equality. Every typed grant in the domain has exactly those four keys, so this is an exact tuple match.
- The unselected token is preserved and the output stays in {A,B}² in every case.

**Permission-breaking variant**
- `infer_permission=True` does not model Alpha's mutation. It completes **every** known request, including no grant, wrong-issuer grants and inspect grants, not just a named owner or label.
- It yields **288** counterexamples, one for every refused case.
- The reported `state_changing_counterexample` is the first in iteration order: owners `[A,A]`, token 0, destination B, **grant `None`**, observed. The correct result is refused; the mutant completes with state `(B,A)`. That is a no-grant witness, not a label witness.
- The "kill" is a comparison against the reference implementation, not a spec assertion firing on the mutant. If you swapped the mutant in, the inverse-postcondition assertion would fail on this case. I inferred that; it is not executed.

**Resumption**
- `(A,A)` → completed `(B,A)`; then unknown observation → unresolved, unchanged; then the stale A-issued grant → refused; then a current B-issued grant → completed `(A,A)`. All four assertions hold.
- Limits:
  - "Re-observes actual state" is true by construction: `owners` *is* actual state, so a stale observation is never modelled.
  - An *unknown effect*, meaning an operation whose outcome is unknown, is not modelled. `observed=False` is checked before any effect.
  - Grants are never consumed. After the trace returns to `(A,A)`, `first_grant` would complete again. That is within scope ("no universal idempotence") but should be stated.
  - Only single steps are covered exhaustively. Multi-step behaviour is one hand-picked trace.

**Refusal of disabled assertions: PASS**
- `if not __debug__: raise SystemExit(...)` runs before any assertion, so it covers both `-O` and `PYTHONOPTIMIZE`.
- Residual: under refusal, an existing `FINITE_RESULT.json` is not removed and could be mistaken for current.
- `invariants_valid: True` is a hard-coded value. It is only trustworthy because the refusal guard forces the assertions to have run first.

## 4. Structural concerns for `ac.py` to settle (unverified)
- `clause:finding-conservation` and `clause:permission` are in no frame index (both programs).
- In Alpha, `symbol:permission` is declared but unused.
- References outside the source (`TRANSFORMATION_LIBRARY.md#transform|conjoin|bind|dispose`, `FOUNDATIONS.md#…`, `calculus_ref`) could not be checked from what was supplied.
- All `SOURCE.md` anchors cited by both programs match headings in the supplied source.

## 5. AC-017 disposition
- Model-local content is acknowledged only in general terms ("hand-authored… requires separate fidelity review"), not item by item. That content is: the label strings, the integer token indices, and the mutant flag.
- Source declarations without a full disposition:
  - Alpha: the exact grant, "assign is the tested operation", the inspect exclusion.
  - Both: the unauthenticated-A case (F2), the omitted-slot distinction (F3), and the owner/token identities.

## 6. Out of scope
I make no claim about complete-STDO validity, real or distributed transport, exactly-once delivery, category equivalence, practical adequacy, whole-corpus qualification or release.

**Next steps**
1. Fix F1 (index finding-conservation and permission) and F2 in Beta.
2. Bind the program hash in the finite report.
3. Either add a label-specific mutant matching Alpha or rename the existing mutant to describe what it actually does.
4. Run `ac.py` and the executable to replace these hand-traced results with real runs.
