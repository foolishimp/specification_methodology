# Integration review: candidate 875a56e3 against own preimage 5b4aebb

## Coverage

- **What I read:** COMMON in full, then the four CORE sections (Result algebra, Result conjunction, Workspace and context, Bounded construction). Configuration and the derivation table I read only as far as they bear on these consumers. Then the four consumer diffs.
- **What I could not see:** only the changed hunks with about 15 lines of context. I did not see:
  - the rest of each member;
  - the candidate's Spec Method, Transformation Library, the FOUNDATIONS identity section, and PREDECESSOR_CLAIMS;
  - ODD §11.5D and A5/A11, UX §8A and §11 in full, and the World Model eight-surface list.
- **Consequences:**
  - Where a finding depends on an unseen body, I say so.
  - "Lost predecessor claim" means lost relative to the preimage hunk. I could not check whether a PREDECESSOR_CLAIMS row dispositions it.
  - Section headings named "§n" or "An" are inferred from neighbouring headings where the heading itself is outside the context.

This is a working source check. It is not acceptance.

---

## ODD_METHOD.md

### 1. Lost precedence of the admitted chain (paragraph after the non-authoritative artifact list, hunk @-1297, after A13a). Severity: high

- **Change:** the preimage said that when the listed artifacts conflict, "the ledger, decision, and projection chain **wins**". The candidate says the chain "owns the account of what was admitted".
- **Counterexample:** a run summary or CLI output reports the edge closed, while the admitted EdgeFulfillmentLedger shows it not converged.
  - Under the preimage, the chain wins and the edge is not closed.
  - Under the candidate, the run summary makes no claim about what was admitted, so nothing resolves the conflict for closure or selection.
  - The "if that chain is absent" sentence still covers absence, but not a chain that is present and contradicted.
- **Repair:** restore "the ledger, decision, and projection chain wins for closure and next-action selection", then keep the new sentence on contrary observation.

### 2. A contrary observation invalidates claims before admission (A1 consistency rule, before A1b). Severity: high

- **Problem:** "Such an observation re-enters evidence admission **and invalidates** affected current claims" can be read as invalidation happening at observation time. That conflicts with the unchanged lines "Closure can only use W through L" and "Eval only affects traversal after its own L/E admission". It also conflicts with the CORE rule that contrary evidence "does not … confer authority".
- **Counterexample:** unadmitted worker prose says "file changed". Under this reading it invalidates an admitted closure, which is a rival control path that bypasses F_D/ABG admission.
- **Repair:** "Such an observation enters evidence admission; **once admitted**, it invalidates affected current claims under their re-entry rules." The A13 sentence ("triggers … evidence admission under A1") then stays consistent.

### 3. evaluate_action becomes a second owner of the target obligations (A6. Evidence Before Closure). Severity: high

- **Problem:** "`evaluate_action` binds the exact target-obligation predicates and required evidence set". But TargetObligationBinding is produced by `bind(U, G0.pressures, …)` before the action, according to:
  - the Bind row;
  - A13a's causal chain;
  - the constitutional equation (`B0`).
- **Counterexample:** an action runs under B0 = {o1, o2, o3}. evaluate_action, holding the binding role after the action, binds {o1, o2}. The sentence's own ban on "a smaller target selected after the action" is then enforced by a locus that also owns the choice.
- **Repair:** "`evaluate_action` **consumes the admitted TargetObligationBinding** and its required evidence set, fixed before the action, and folds them with …"

### 4. Wrong verdict for a closure predicate with a known failure (A8, closure decision vocabulary). Severity: high

- **Problem:** the third bullet says "an unproved closure predicate is `indeterminate`". "Unproved" includes the case where one obligation is falsified.
- **Counterexample:** o1 is falsified, o2 is unassessed, and the disposition is `repair`.
  - Bullet 2 says o1 is falsified.
  - Bullet 3 says the closure predicate is indeterminate.
  - The A6 fold uses result conjunction, and rule 1 of conjunction makes the closure predicate falsified.
- **Repair:** "with no authenticated falsified obligation, an unproved closure predicate is `indeterminate` …; otherwise it is `falsified` under result conjunction."

### 5. `unconfirmed` is forced to indeterminate (A8, same block). Severity: medium-high

- **Problem:** "retain `unconfirmed` with an indeterminate predicate". CORE permits falsified, invalid_basis or out_of_frame under `unconfirmed` when deciding evidence exists independently. The text also contradicts the A8 bullet "a demonstrated obligation violation is `falsified`".
- **Counterexample:** the worker's response is lost, but a fresh eval_gap observation authentically shows that a required file was deleted. CORE gives falsified with performance unconfirmed. ODD gives indeterminate, and the known failure is lost.
- **Repair:** "retain `unconfirmed`; the predicate is indeterminate unless independently authenticated counterevidence or a basis/scope diagnosis decides it under the core legal pairs."

### 6. Yield and the retained falsified assessments (A8 addition against A9. Yield Is Lawful Iterate). Severity: medium

- **Problem:**
  - A9, which is unchanged, says yield "returns control **without failure classification**".
  - The new A8 text says the decision's "complete return preserves … the ledger's assessment records". It also allows `yield` alongside a falsified obligation.
  - It then claims "This mapping preserves A9".
- **Counterexample:** a yield is returned while o1 is falsified. Under A9 the return carries no failure classification. Under A8 it carries o1 = falsified.
- **Repair:** qualify A9's line as "the yield disposition itself adds no failure classification; retained assessment verdicts remain."

### 7. F_P availability expires (paragraph immediately before `### Graph Functions`). Severity: medium-high

- **Problem:** "an `F_P` candidate establishes availability **only until** its fitness is assessed". This implies that the fitness result overwrites or ends the availability result. CORE says "A new result over a different predicate does not overwrite the earlier result" and treats availability and fitness as separate predicates.
- **Counterexample:** a candidate is available and then assessed as falsified. Under ODD, availability is no longer established, so the repair path cannot rely on the candidate existing. Read the other way, pre-assessment availability stands in for provisional fitness.
- **Repair:** "an `F_P` candidate establishes only availability; fitness and acceptance are separate results."

### 8. The decision predicate can be satisfied before admission (A8). Severity: medium

- **Problem:** the EdgeClosureDecision result binds "this disposition was lawfully issued … under mandate". But per A1, evaluate_action's output is F_P work, and the Dispose row puts authority at F_D/ABG/product admission. Nothing stops the evaluator's own unadmitted `close` from carrying a satisfied decision result. CORE says "Recording the decision is not its authority."
- **Repair:** add "satisfied only once F_D/ABG/product admission has admitted that decision".

### 9. Undispositioned guard removal (Governing Relations). Severity: low-medium

- **Problem:** the preimage said "They add no six-stage workflow, **runtime API** or categorical-equivalence claim." The candidate drops "runtime API" and weakens the workflow clause to "no **compulsory** six-stage workflow". Identity Method keeps "runtime API" in its equivalent sentence.
- **Repair:** "The operations add no six-stage workflow, runtime API or categorical-equivalence claim."

---

## IDENTITY_METHOD.md

### 10. "Hierarchy" contradicts Position (Governing Relations against `## Position`). Severity: medium

- **Problem:**
  - Governing Relations says the choice of "names, encoding, **hierarchy** and optional coordinates remains with the adopting owner".
  - Position says "Identity is made unique by hierarchy and type" and "is not a flat global string convention".
- **Counterexample:** an owner adopts flat global names. Governing Relations allows it; Position forbids it.
- **Repair:** replace "hierarchy" with "the concrete form of the scoping hierarchy".

### 11. "Refuses" has no reason-sensitive map, and sparse absence is conflated (Derivation Verification Material). Severity: medium

- **Problem:** the unchanged rule says "Missing, duplicate, altered, incomplete or unbound material **refuses**". The new paragraph adopts the shared record but gives no map from the refusal cause. CORE: "a consumer cannot guess from a word such as `refused`", and "an absent sparse file is not evidence of absence".
- **Counterexample:** a fragment is absent from the local checkout. Treating that as falsified on membership is wrong; it is indeterminate until the authoritative source is acquired.
- **Repair:** add one sentence:
  - an altered, duplicate or incomplete fragment, or a fragment shown missing from the authoritative manifest, gives `falsified` on that check;
  - unbound material (no authentic manifest binding) gives `invalid_basis`;
  - material that has not been acquired gives `indeterminate`.

### 12. The rename sentence has two readings (paragraph before `## Release Version Boundary`). Severity: low-medium

- **Problem:** "Renaming a coordinate does not by itself replace the subject" can be read as:
  - same subject, so no transition is needed; or
  - the rename cannot escape history.

  Given the minimum (authority, kind, value), these give opposite answers on whether REQ-12 → REQ-12a without a supersession relation keeps continuity.
- **Repair:** "A changed coordinate neither establishes nor ends continuity; continuity across it requires the owning transition relation above."

---

## UX_METHOD.md

### 13. The effect `Msg` map is not total (§6 effect membrane, before §7). Severity: medium

- **Problem:** "observed completion, partial execution and uncertainty as distinct typed `Msg` cases" covers three of the six core effect states. It omits `not_started`, which requires an authenticated rejection before mutation, and `reverted`. §8A still requires only "success and failure `Msg` values".
- **Counterexample:** a server rejects a request on validation before any write. It has no Msg case, so it is either forced to `unknown` or left as an untyped failure that "records the corresponding shared effect state" cannot express.
- **Repair:** "Effect returns distinguish, under the command's contract, each shared effect state the command can produce; §8A's success/failure `Msg` values carry that state."

### 14. §8A "proof fails" conditions are unmapped (§8A, before §9). Severity: medium

- **Problem:** the new map covers only expected-state or command mismatch, missing trace, a bad fixture and out-of-domain cases. A demonstrated dependency on DOM, refs, timers or bypassing I/O is not mapped, even though §8A says the proof then fails.
- **Counterexample:** the final State matches only because a module variable persisted. No listed falsifier applies.
- **Repair:** "a demonstrated dependency on any §8A excluded source is `falsified` on the replay predicate."

### 15. "Conjoined by the shared owner" (§13 sprint close, before §14). Severity: low-medium

- **Problem:** two predicates are declared separate and then "conjoined by the shared owner". That owner is unnamed, and the composite predicate is undeclared.
- **Repair:** "Method closure conjoins its own required results (§8A, §11, recorded exemptions) under result conjunction; the sprint-close result is not a conjunct."

---

## WORLD_MODEL_METHOD.md

### 16. A weaker restatement of the categorical demonstration standard (`## Composition Law`). Severity: medium

- **Problem:** "requires its stated objects, maps and laws" omits several items of the standard:
  - arrow equality and identities;
  - shown functor laws;
  - the distinction between conformance and equivalence;
  - the evidence class.

  It also names no owner, which creates a second locus.
- **Counterexample:** an adjunction claim with stated functors and unit/counit, but with no functor laws shown and no evidence class, passes here and fails COMMON items 4 and 5.
- **Repair:** replace it with a reference to the candidate's owning locus for the categorical demonstration standard.

### 17. Partial restatement of the build-tenant binding without its owner (`## Control Plane And Data Plane`). Severity: low-medium

- **Problem:** the profile lists "operations … composition, effect sites, authority and resource dimensions". It omits operational assumptions (COMMON binding item 3) and does not name the Spec Method locus. ODD's sentence "human, machine or mixed implementation" has the same unowned framing.
- **Repair:** in both profiles, "as bound under [Spec Method build-tenant binding]", and drop the inline list.

### 18. Standing of a stated absence (entity-cut admission paragraph, before `### Discrimination`). Severity: low-medium

- **Problem:** "A **supported** stated absence … does not establish an absent property". A supported absence claim does establish its claim, so the sentence contradicts itself.
- **Repair:** "Stated absence or non-applicability satisfies explicitness; the absence claim itself is satisfied only by its support, and an unexamined property is unresolved, not absent."

---

## Checked and consistent within the visible context

- Links to `FOUNDATIONS.md#result-algebra`, `#result-conjunction`, `#workspace-and-context` and `#bounded-construction` match the CORE headings.
- UX keeps `accepted` separate from authorised acceptance.
- World Model keeps the provenance labels for Assure separate from verdicts.
- ODD keeps the no-action selection separate from product completion.
- ODD A13 and UX §6 both state that a lost response or failed response is not evidence of `not_started`.

**Unverified risk:** three profiles renamed the `Foundation And Transformation Binding` heading to `Governing Relations`. I could not check whether any inbound anchors to the old heading exist.
