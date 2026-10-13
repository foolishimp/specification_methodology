# Integration review: candidate 9982ab8 against own preimage 875a56e

## Coverage

- **What I read:** the Common requirements, the supplied Foundations excerpt (Result algebra through Core contract derivations), and the diff hunks, each with about 15 lines of context.
- **What I did not see:**
  - PRINCIPLES, CAPABILITIES, A_C_DEPENDENCY and PREDECESSOR_CLAIMS;
  - `SPEC_METHOD.md#what-how-and-work-carriers`;
  - `FOUNDATIONS.md#orthogonal-descriptions`;
  - the Identity "relation above" and "owning transition relation above";
  - ODD §11.5D and any definition of `TargetObligationBinding`;
  - the rest of each member's body.
- **Where line numbers come from:** I computed them from the hunk headers.
- **Status:** this is a source check of these joins only. It is not acceptance of any member, and it does not approve the source-port review policy.

## Findings

### 1. ODD A8: the closure map overrides core precedence for invalid_basis and out_of_frame
**Where:** `ODD_METHOD.md:1202-1206`, A8 (closure decision vocabulary).

**Problem:**
- The new bullet says that, with no authenticated falsification, "an undecided closure predicate is `indeterminate` … otherwise core conjunction preserves the falsification." It defers to core only for falsification.
- Core conjunction rule 2 gives `invalid_basis`, and then `out_of_frame`, precedence over `indeterminate` (rule 3).

**Counterexample:** A productive `yield` has one obligation whose required basis is unusable and no falsified obligation.
- Bullet 3 yields `indeterminate`.
- Bullet 4 and core yield `invalid_basis`.

**Smallest repair:** "with no authenticated falsified obligation, invalid basis or out-of-frame judgment, an undecided closure predicate is `indeterminate` …; otherwise core conjunction precedence applies."

### 2. ODD A8: evaluation performance is still keyed to the worker
**Where:** `ODD_METHOD.md:1207` (bullet, context) and `:1209-1211` (changed sentence).

**Problem:**
- Core: performance belongs to "the named predicate's declared evaluation … separately from dispatch, admission or the work being assessed."
- The changed sentence retains `unconfirmed` "rather than asserting the worker did or did not run." This keeps the bullet's conflation of the worker with the evaluation.

**Counterexample:** The worker crashed before starting, and `evaluate_action` then assessed obligation O and found no evidence.
- Core: `performed` with `indeterminate`, or `falsified` if O's artifact is demonstrably absent from the complete authoritative set. The worker's non-start is evidence plus an effect observation of `not_started`.
- ODD: `not_performed`.

**Smallest repair:**
- In the sentence: "If the evaluation's performance cannot be established, retain `unconfirmed`."
- In the bullet: "an unperformed evaluation retains `not_performed`; a worker that did not run is evidence and its effect observation."

### 3. UX §13: the exemption is put into plain conjunction
**Where:** `UX_METHOD.md:525-526`, §13 (finding classification, before `## 14. Failure Pattern`).

**Problem:**
- Method closure "conjoins its applicable proof, accessibility and exemption results through core conjunction."
- The governing predicate (`:535-536`) is "§8A proof and §11 accessibility unless an explicit exemption is recorded." Per obligation, that is "exempt or proved", which is not a conjunct relationship. Core states: "Negation or disjunction evaluates a different predicate."

**Counterexamples:**
- **Exempt surface without a replay proof:** the proof result is `not_performed` or `indeterminate`, so the conjunction is `indeterminate`. The intended result is satisfiable.
- **Non-exempt surface:** the exemption slot is absent, so coverage is missing and the conjunction is `indeterminate` permanently.

**Smallest repair:** "the latter conjoins its applicable proof and accessibility results through core conjunction; an authorised recorded exemption is the supported applicability judgment that removes the exempted obligation."

### 4. World Model admission: non-applicability loses its support requirement
**Where:** `WORLD_MODEL_METHOD.md:1097-1099`, the admission paragraph before `### Discrimination`.

**Problem:**
- Preimage: "A *supported* stated absence or non-applicability can satisfy the explicitness obligation."
- New text drops "supported" and restores support only for "the absence claim."
- Core: "A not-applicable classification needs a supported applicability judgment."

**Counterexample:** A cut states "adjacent-domain treatment: not applicable" with a reason but no applicability support.
- Under the new text, explicitness is satisfied.
- Nothing visible requires the non-applicability claim to be supported as an admission conjunct.

**Smallest repair:** "the absence or non-applicability claim itself needs its support." Also confirm that this support remains a required admission conjunct, as the preimage made it. Otherwise this is a lost own-preimage obligation.

### 5. ODD A1: closure can proceed while a contrary observation awaits admission
**Where:** `ODD_METHOD.md:1020-1022` (A1, before **A1b**), together with the A12 conflict paragraph.

**Problem:**
- Invalidation now occurs only "once admitted."
- A12 says the ledger chain "governs admitted closure and next-action selection."
- Core reuse requires "adequate current basis"; a stale read cannot be assumed current.

**Counterexample:**
1. A worker observes W contradicting admitted claim C.
2. The observation is queued for admission.
3. `evaluate_action` folds C as current and issues `close`.
4. The contrary observation is admitted later.

**Smallest repair:** "Pending that admission decision, the affected claim is not reused as current support for closure or next-action selection."

This keeps admission authority with F_D/ABG/product admission and blocks only in the safe direction.

### 6. World Model composition: the categorical obligation is delegated to an unseen locus
**Where:** `WORLD_MODEL_METHOD.md:1338-1340`, the section before `## Projection Law`.

**Problem:**
- The preimage stated the operative requirement: "requires its stated objects, maps and laws."
- The new text says the claim "follows [Orthogonal descriptions]". That anchor is not in the supplied core, and its name does not indicate that it carries the Categorical Demonstration Standard (items 1–5, and "without the demonstration … is a hypothesis").

**Repair:**
- If the anchor owns that standard, no change is needed.
- Otherwise, point to the actual owner, or restore: "requires the demonstration at [owner]; without it the claim is a hypothesis."

### 7. Minor
- **`UX_METHOD.md` §8A replay (new text, around `:324`):** "A demonstrated … mismatch, or a dependency on any source excluded" can be read as making a merely suspected dependency `falsified`. Core requires an undemonstrated one to be `indeterminate`. **Repair:** "or a demonstrated dependency."
- **`IDENTITY_METHOD.md:56-60`:** The refusal map does not declare the missing-reason case that core requires of a refinement. It also maps "missing authentic basis binding," while the cause list at `:53` says "unbound." **Repair:** "unbound material (missing authentic basis binding) is invalid_basis; a refusal without a recorded cause leaves the predicate indeterminate."

## Checked, no finding within coverage

**Identity**
- "Concrete scoping hierarchy."
- The coordinate-continuity rewrite. It is consistent with the scoped minimum of authority, kind and value. It does change the preimage default for a rename. If a PREDECESSOR_CLAIMS row cites the old wording, that row should be rechecked.

**ODD**
- "Runtime API."
- The F_P availability correction, which now matches core item 5.
- A6 consumes the admitted, pre-fixed target binding. `TargetObligationBinding` is undefined in visible text.
- The A8 admission requirement for the decision predicate.
- The `unconfirmed` legal-pairs sentence.
- A9 yield wording.

**UX**
- Effect `Msg` states. The context line about failed responses after dispatch covers `unknown`.

**ODD and World Model**
- The tenant-binding references to Spec Method. They hold only if that anchor owns Common Build-Tenant items 1–4, and the adjacent sentences still apply the binding at the point of use.
