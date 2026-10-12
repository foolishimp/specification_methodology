# Interpretation-fidelity review: subject `427a0deb39b7cd8e298b3b2ebc126c052f056d8a`

**Basis:** I used only the supplied text: SOURCE, Program Alpha, Program Beta, the finite token script, AC-017, FOUNDATIONS and TRANSFORMATION_LIBRARY. I didn't use any tools or run the script. I checked the script's counts by deriving them by hand. I can't confirm that the supplied text matches the bytes at that commit, or that the script's `source_sha256` matches this SOURCE.

Alpha and Beta are identical except for `clause:permission`. Their other clauses, symbols, residual and frame indexes match exactly, so I assessed those shared parts once and applied the result to both programs.

## Program Alpha (`urn:codex-stdo3:c3:program:permission-mutant`)

| Selected relation | RF result |
|---|---|
| Token state | **falsified** |
| Typed join | satisfied (shared with Beta) |
| Finding conservation | satisfied (shared with Beta) |
| Authority/recovery | satisfied at clause level (shared with Beta; see the shared observations below) |

**Evidence for the token-state result:**
- **SOURCE:** "Permission is issued by that token's current owner for that exact token/destination/operation." "A display label grants no permission." "Known current state plus missing permission returns refused without an effect."
- **Alpha's `clause:permission`:**
  - premise: "A named current owner or display label supplies permission without an exact grant."
  - statement: "Naming an owner or display label authorizes the assignment."
  - The premise that should refer to `symbol:permission` ("Exact current-owner permission") has been replaced by this literal. The symbol is still declared, but no clause refers to it, so it is orphaned.
- **The clause contradicts itself.** Its own qualification says "known missing exact permission returns refused with no effect," while its premise and statement grant permission without an exact grant.
- **The error spreads.** `clause:token-transfer` takes `clause:permission` as its premise. Its consequence, "with … exact permission," now depends on a premise that says no exact permission is needed.
- **The residual doesn't cover this.** `residual:scope` lists `clause:permission` only under generic scope limits. It doesn't disclose that the clause departs from the source. The URI name `permission-mutant` is not a recorded disposition under AC-017.

**Counterexamples** (known state, assign operation):
1. State (A, A), token t0, destination B, grant `label:A`.
   - SOURCE: refused; state stays (A, A).
   - Alpha: the label authorizes it; state becomes (B, A).
2. State (A, A), t0, B, no grant, current owner A is named.
   - SOURCE: refused.
   - Alpha: authorized.

## Program Beta (`urn:codex-stdo3:c3:program:source-v1`)

| Selected relation | RF result |
|---|---|
| Token state | **satisfied** |
| Typed join | **satisfied** |
| Finding conservation | **satisfied** |
| Authority/recovery | **satisfied** (clause content; see the observations below) |

**Token state**
- `clause:permission` has premises `symbol:permission` ("Exact current-owner permission") and `symbol:observed`.
- Its qualification says unknown observation gives unresolved with no effect, and known missing exact permission gives refused with no effect.
- Its statement: "A named owner or display label alone never authorizes."
- `clause:token-transfer`:
  - only the selected token receives the destination owner;
  - the token set and single-valued ownership survive;
  - resumption re-observes actual state;
  - no universal idempotence is claimed.
- **Weakness:** Beta never spells out the four exact grant coordinates (issuer, token, destination, operation) or the assign/inspect distinction. A reader recovers them only by following the source reference from the symbol to `#token-state`. AC-017 provenance is met, but the exact grant tuple is not stated in the model itself.

**Typed join**
- LengthMetres → DurationSeconds is incompatible.
- DurationMilliseconds → DurationSeconds requires dividing by 1000.
- "Compatible types confer no operation permission."
- The phrase "despite equal float representations" is carried by the statement "Field-shape equality cannot supply semantic compatibility."

**Finding conservation**
- Exactly slot A is admitted, bound to source-v1 and one original producer.
- The conjunction retains A falsified, its producer, the citation `source/A.md#permission-branch`, and B uncovered.
- The result stays non-green.
- A missing A invalidates the complete planned-set claim, and no judgment is invented.
- B being "not an omitted planned slot" follows from "exactly planned slot A." This agrees with the Conjoin rule that absence must not be read as a generic falsification.

**Authority/recovery**
- `clause:role-boundary`: a predicate result supplies no action or acceptance grant, and the decision owner acts only within its existing grant.
- `clause:effect-recovery`: after an unknown effect, observe and reconcile, or stop unresolved, before any blind retry.

## Observations on both programs (shared indexing and residual)

- **Authority/recovery has no frame.** SOURCE selects three qualitative relations, including authority/recovery. Neither program has a frame reference for `#authority-and-interpretation`. Its clauses are placed under other indexes instead: role-boundary under `index:findings`, effect-recovery under `index:tokens`.
- **Missing direct index entries.** `index:findings` doesn't list `clause:finding-conservation`, and its `residual_refs` is empty, even though `residual:scope` covers that clause. `index:tokens` doesn't list `clause:permission`. Both clauses can be reached only indirectly, as premises of other clauses.
- **Placement under the token index.** Because effect-recovery sits under `index:tokens`, a reader could take it to be executed by the token enumeration. The residual sentence "models token states only" offsets that only partly.
- **Role-boundary is scoped too narrowly.** It takes only finding-conservation as its premise. SOURCE applies the no-authority rule to every predicate result, including the finite model result and typed-join results.
- **Distinct claims are listed only as "not proved."** SOURCE says finite model success, source fidelity, adequacy, category equivalence, corpus qualification and release are distinct claims. The residual lists them as not proved instead. "Finite model success is not source fidelity" is not stated explicitly.
- **Residual coverage is complete.** The residual contains every item in SOURCE's residual list, plus practical adequacy and release.
- **Not assessed:** whether citing the v2.5.1-rc.2 `calculus_ref` alongside codex-v3 successor references is a valid binding.

## Finite token executable (checked against SOURCE `#token-state` only)

**RF result: satisfied** on its declared finite domain.

**What it gets right:**
- **Order of checks:** if the state is not observed, it returns unresolved with the state unchanged. This happens before any grant is read, as SOURCE requires.
- **Exact grant check:** it requires the grant to be a dict whose issuer equals `owners[token]`, with `token`, `destination` and `operation == 'assign'` all matching.
  - Labels are strings, so they are refused.
  - A wrong issuer, wrong token, wrong destination or `inspect` operation is refused.
- **Completion:** only `output[token]` changes, and the assertion `output[1-token] == owners[1-token]` checks the other token.

**Domain counts (my hand derivation agrees):**
- Grant variants: 3 non-typed (no grant and two labels) + 16 typed = 19.
- Cases: 4 states × 2 tokens × 2 destinations × 19 grants × 2 observation values = 608.
- Unresolved: 304 (all unobserved cases).
- Completed: 16 (one exact grant per state/token/destination).
- Refused: 288 (16 × 18 non-matching grants).

**Assertions are complete over the domain when combined with the pinned counts:**
- "Completed implies an exact grant" plus completed = 16 gives "an exact observed grant implies completed."
- Unresolved = 304 rules out any observed case returning unresolved.
- The mutant, which infers permission, differs in exactly the 288 refused cases.

**Resumption after a state or owner change:**
1. (A, A): A's exact grant moves t0 to B. Completed, giving (B, A).
2. Unknown observation: unresolved, no change.
3. The same grant from A, now stale: refused, because the issuer is no longer the current owner.
4. A grant from the new owner B: completed, giving (A, A).

Token identity (index 0) is kept throughout.

**Limits and concrete issues:**
1. **Report integrity under `-O`.** If you run it with `python -O` or `PYTHONOPTIMIZE` set, every `assert` is removed. The script then still writes `invariants_valid: True` and the pinned outcome counts without having checked anything. That flag proves nothing unless you know how the script was run.
2. **Single-valued ownership can't fail by construction.** It is guaranteed by the 2-tuple representation, so it is not a property that could actually be falsified.
3. **"Re-observes actual state" is supplied by the test harness.** It passes `changed` as the actual state. A stale-but-known observation is not modeled; SOURCE only distinguishes known from unknown.
4. **It runs neither program.** A green run is equally compatible with Alpha and Beta. It cannot detect Alpha's falsified permission clause or confirm that Beta is faithful.

## Out of scope

- None of these results establishes:
  - all-STDO meaning;
  - a distributed exactly-once guarantee;
  - categorical or Markov properties;
  - whole-corpus fidelity;
  - acceptance;
  - release.
- Neither a valid structure, nor the program URI, nor the green enumeration, nor the supplied hashes establishes those claims.
- As requested, this review gives no repair, next-action or acceptance direction.
