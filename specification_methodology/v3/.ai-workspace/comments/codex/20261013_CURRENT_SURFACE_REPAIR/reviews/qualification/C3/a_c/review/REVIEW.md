# Interpretation-fidelity review: subject b0ec615c9ebe8da80e9852df3968233155a432b7

I used only the bytes you supplied. I ran no tools, read no repository state, and did not consult a peer or advisor. I couldn't check `AXIOMATIC_CALCULUS.md` (including AC-017) or the real `SOURCE.md` file, so I took the finite source text and the two supplied owner scopes as the whole basis.

## Results

| Subject | Result |
|---|---|
| Program Alpha | **falsified** |
| Program Beta | **indeterminate** overall: no contradiction found, but one source relation is left out (details below) |
| Executable interpretation | **satisfied** for one-step token-state behaviour only; **indeterminate** as an interpretation of the whole selected source |

Alpha and Beta have the same program URI (`urn:codex-stdo3:c3:program:finite`) but different contents. FOUNDATIONS §Identity says equal content does not establish identity; the reverse also holds here. One name now points to two programs that mean different things. I judged each program separately, and any record citing that URI is ambiguous between them.

## Program Alpha: falsified

**Clause:** `urn:codex-stdo3:c3:clause:permission`
- The premise literal says: "A named current owner or display label supplies permission without an exact grant."
- The statement says: "Naming an owner or display label authorizes the assignment."

**Source it contradicts (§Token state):** "Permission is issued by that token's current owner for that exact token/destination/operation. A display label grants no permission. … Known current state plus missing permission returns refused without an effect."

**What spreads from it:** `clause:token-transfer` uses `clause:permission` as its premise, and frame index `index:tokens` refers to `token-transfer`. So the token frame rests on the false permission clause. The clause's own qualification ("known missing exact permission returns refused") contradicts its premise and statement, so the clause is also inconsistent with itself.

**Counterexample from the source:**
- State: t0 = A, t1 = A, observed.
- Operation: move t0 to B.
- Permissions: none. The display label "A" is present, and owner A is named.
- Source result: `refused`, and the state stays (A, A).
- Alpha's statement: the assignment is authorized, so t0 becomes B.

That is an unauthorized ownership change. The executable's `infer_permission=True` mutant has the same shape: it completes this case where the source refuses it.

Alpha's other clauses (finding-conservation, role-boundary, typed-join) are identical to Beta's. Beta's findings below apply to them too, but they don't change Alpha's result.

## Program Beta: indeterminate

### Token state: satisfied
- **`clause:permission`** has premises `symbol:permission` ("Exact current-owner permission") and `symbol:observed`. Its qualification is "unknown → unresolved, no effect; known missing exact permission → refused, no effect". Its statement is "A named owner or display label alone never authorizes". This matches §Token state.
- **`clause:token-transfer`**: only the selected token changes to the destination owner, and the token set and single ownership hold. "Resumption re-observes actual state" and "no universal idempotence is asserted" match the source's limits, and FOUNDATIONS §Finite capacity.

### Finding conservation: indeterminate
- **Matches the source:** the conclusion keeps A falsified, its original producer, the citation `source/A.md#permission-branch` and B uncovered, and stays non-green. The qualification treats a missing planned judgment as invalidating the complete planned-set claim and never invents one. Both match the source and TRANSFORMATION_LIBRARY §Conjoin.
- **Left out:** the source says the admitted set is "exactly slot A, **bound to source-v1** and one producer." Beta's premise says only "admitted/authenticated" and never binds slot A to source-v1.
- **Counterexample:** slot A is authenticated but its finding is bound to source-v2. Beta's premise still accepts it, and conservation goes ahead. Under the source and Conjoin ("Combine only compatible, authenticated results…"), a different basis is outside this domain and cannot support a wider claim.
- Because this is an omission and not a contradiction, the result is indeterminate rather than falsified.

### Authority and interpretation (`clause:role-boundary`): satisfied
- It covers "no action or acceptance grant" and that the decision owner acts "within its existing grant". This matches Evaluate/Dispose and FOUNDATIONS §Judgment and authority.
- Not encoded: "Unknown effects require observation/reconciliation or an unresolved stop before blind repetition." Token-transfer's re-observation wording only partly covers it.

### Typed join (`clause:typed-join`): content satisfied, structurally out_of_frame
- The content matches the source: LengthMetres → DurationSeconds is incompatible, milliseconds → seconds divides by 1000, and compatible types give no permission.
- But `#typed-join` is not in `frame_refs`, and no frame index refers to the clause. Only the residual names it. Under the program's own declared frames it sits outside any frame, so no frame-indexed claim covers it.

### Residuals
The residual leaves out source items:
- **Runtime capacity** is missing.
- **Release** and **practical adequacy** (distinct claims under §Authority) are missing.
- "Distributed exactly-once effect" becomes "distributed transport guarantee", which is close but not the same wording.
- `subject_refs` leaves out finding-conservation and role-boundary.

These are gaps in the residual claims, not contradictions.

## Executable interpretation

**What it models:** 4 ownership states × 2 tokens × 2 destinations × 16 permission subsets × observed/unobserved = 512 cases. `operation` returns:
- `unresolved` with no effect when the state is not observed;
- `refused` with no effect when there is no permission;
- otherwise it assigns the selected token only.

The assertions check the other token is unchanged, both owners are in {A, B}, the token count is 2, and the state is unchanged when the operation doesn't complete. The 128 mutant counterexamples are correct: 256 observed cases, half of which lack the relevant permission bit.

**Satisfied for:** one-step token-state behaviour, treating permission as an abstract "exact grant present" bit.

**Limits that keep it from covering the whole source:**
1. **Two of the four relations are not modelled.** Finding conservation and the typed join have no executable model. Authority is mentioned only in the `limits` text. The source selects "two bounded proof domains"; the executable covers one.
2. **The issuer is not modelled.** Permission is one bit per (token, destination). Nothing represents a grant from a non-owner, a display label or a named owner. "Issued by that token's current owner" and "a display label grants no permission" are assumed by construction, not tested. The comment "Permission must match the current owner" is not enforced.
3. **The expected-result check repeats the implementation.** `expected` uses the same conditions as `operation`, so the result check is close to a tautology. Only the invariant assertions and the mutant add independent force.
4. **The first reported counterexample is weak evidence.** With `product` ordering it is owners (A, A), t0 → A, mask 0, observed. That is a no-op: the mutant's state equals the expected state, and only the result label differs. An exhibit where the state actually changes would show the harm better.
5. **Later invocations are not tested.** "A later invocation re-observes actual state" and "no permission carried across a later state" are not checked over sequences of operations.
6. **It evaluates neither program.** Its result is the same for Alpha and Beta. A green run therefore says nothing about which program is faithful.
7. **The source hash is unchecked.** It hashes `root/SOURCE.md`, and I can't confirm from the supplied bytes that this is the source text above.

## What this review does not establish

- Even taken together, Beta's verdict and the executable's satisfied token-state result are only a scoped finite judgment. They do not show fidelity across all of STDO, whole-corpus qualification, practical adequacy, category equivalence, Markov properties, distributed exactly-once effects, runtime capacity or release.
- I could not check AC-017 interpretation-fidelity law, because the calculus was not supplied.
- I could not check that the `repo://codex-v3/...` URIs resolve to the supplied owner-scope bytes.
- I have no repair or acceptance authority. Possible fixes include:
  - correcting Alpha's permission clause;
  - binding source-v1 in Beta;
  - indexing typed-join in a frame;
  - completing the residual;
  - modelling finding conservation and the issuer;
  - giving the two programs distinct identities.

The decision owner chooses which, if any, to apply.
