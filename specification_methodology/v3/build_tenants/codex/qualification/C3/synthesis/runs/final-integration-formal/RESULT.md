# Integration review: candidate 875a56e3 (preimage 5b4aebb)

## Coverage

I read COMMON first, then the CORE sections (`Result algebra`, `Result conjunction`, `Workspace and context`, `Bounded construction`, `Configuration`, `Core contract derivations`), then the three consumer diffs. Each hunk came with about 15 lines of context, so the following were not visible:

- The rest of FOUNDATIONS, including the F1–F6 statements.
- SPEC_METHOD (UP-016, UP-017, UP-021 and the tenant-binding locus).
- TRANSFORMATION_LIBRARY and AC-014.
- The profile's generic signature rows and its external-kind list.
- PREDECESSOR_CLAIMS and A_C_DEPENDENCY.

Where a finding depends on unseen text, I say so. This is a working source check, not acceptance.

## Findings, ranked

### 1. A held or invalid component judgment becomes a falsified cut
**Location:** TRAVERSAL_OCCURRENCE_PROFILE `## Candidate, Judgment, Event, And Relation Separation`

- **The join:** The new paragraph conjoins the claim, event and cut predicates "through result conjunction". The context sentence below it still says "A missing cut judgment, non-`admitted` decision, … refuses the semantic cut". The profile's new mapping text fixes `refused` as `falsified`.
- **Counterexample 1:** `j_c.decision = hold` with `stale_frontier`, which is `indeterminate`. The profile says the cut is refused, so `falsified`. Core conjunction rule 3 gives `indeterminate`.
- **Counterexample 2:** `j_e.decision = invalid_basis`. The profile gives `refused`. Core rule 2 gives `invalid_basis`, and the profile itself says `invalid_basis` maps only to `invalid_basis`.
- **Counterexample 3:** `j_a` is absent. The profile gives `refused`. Core says a missing judgment is an absent slot and does not fabricate a result.
- **Further contradiction:** The `semantic_cut_admission` row says a stale source frontier "retains `hold`", and the profile's own re-entry rule differs between hold and refusal.
- **Smallest repair:** Replace "refuses the semantic cut" with: "leaves the semantic cut unadmitted; the cut result follows result conjunction (an inconsistent or refused component is `refused`/`falsified`, a held or absent judgment is `hold`/`indeterminate`, an invalid component basis is `invalid_basis`)."

### 2. The profile's effect-disposition map is not total
**Location:** TRAVERSAL_OCCURRENCE_PROFILE, the disposition-law paragraphs just before `### OP-005 Mutable Reality Conservation`

- **Gap (a):** `no_effect` is mapped only "with no requested operation". Take a stale `effect_readiness` result followed by a stop: an operation was requested, nothing was dispatched, and the disposition is `no_effect`. No core value is assigned. Core requires `not_started` when there is evidence, otherwise `unknown`, and never a default to `not_requested`.
- **Gap (b):** `partial_effect` maps to `partial` only for a "completed part and an unexecuted remainder". Core `partial` also covers a *reverted* remainder, and core `reverted` covers "every begun part reversed". Take an invocation whose begun part is rolled back within the boundary. It cannot be `refused_effect` (mutation began), and the map gives no value.
- **Smallest repair:**
  - Add: "`no_effect` for a requested operation is `not_started` with authenticated non-dispatch evidence, otherwise `unknown`."
  - Restate the `partial_effect` map using core's `partial`/`reverted`/`unknown` definitions, including the reverted remainder.

### 3. The design-method effect return drops `reverted`
**Location:** DESIGN_MODULE_METHOD §9, the effect-edge section between `## 8. Totality Rule` and `## 10.`

- **The defect:** The list "`not_requested`, `not_started`, `completed`, `partial` or `unknown`" omits the core value `reverted`.
- **Counterexample:** A database write begins and its transaction rollback is observed complete. The effect has no lawful value, so it will be forced into `partial` or `unknown`.
- **Smallest repair:** Add `reverted` to the list.

### 4. An "established prohibition" falsifies the constraint predicate
**Location:** AXIOMATIC_CALCULUS `### AC-007 Constraint And Refusal`

- **The defect:** AC-007 maps on "that same subject, basis and predicate", and then sends "an established prohibition or counterexample to `falsified`".
- **Counterexample:** `Interpret` refuses because the interpreter lacks its grant. AC-007 then reports the model or constraint predicate as `falsified`, but no counterexample to that predicate exists. Core requires admissible evidence defeating *that* predicate, and keeps decision and authority predicates separate.
- **Smallest repair:** "a prohibition is `falsified` only on the permission or admission predicate it defeats; on the evaluated predicate a missing grant or capability is `out_of_frame` (or `indeterminate`)."

### 5. `not_applicable` maps to the wrong core verdict
**Location:** DESIGN_MODULE_METHOD `### Cross-view axiom evaluation`

- **The defect:** `not_applicable` is mapped to `out_of_frame` on the axiom predicate, while applicability is declared "a separate predicate".
- **Effect when the exclusion is supported:** The axiom leaves the required set, so the `out_of_frame` value describes nothing.
- **Effect when the exclusion is unsupported:** The gate conjunction applies rule 2 and returns `out_of_frame`, a scope or capability claim. Core rule 3 requires `indeterminate` for unresolved applicability.
- **Counterexample:** The Python-typing axiom is marked `not_applicable` with a weak reason. The gate reports `out_of_frame` instead of `indeterminate`.
- **Smallest repair:**
  - `not_applicable` is a result on the applicability predicate: `falsified` ("axiom applies") when supported, `indeterminate` otherwise.
  - Reserve `out_of_frame` for an applicable axiom that lies outside the pack's scope or capability.

### 6. The cross-view table cannot carry the required coordinates
**Location:** DESIGN_MODULE_METHOD `### Cross-view axiom evaluation` (minimum columns), consumed by `### Gate and retrospective work`

- **The defect:** The new text requires `indeterminate`, `invalid_basis` and `not_performed`. The only result columns are `Verdict` and `Gap owner`, and the domain labels are just {pass, fail, not_applicable}.
- **Counterexample:** An aborted check that witnessed a failure must be `falsified` with `not_performed`. The table cannot record performance, and the gate conjunction needs it.
- **Smallest repair:**
  - Define `Verdict` as the core verdict, with the domain label retained.
  - Add a `Performance` column.

### 7. The new Judgment fields have no closed signature rows
**Location:** TRAVERSAL_OCCURRENCE_PROFILE, closed signature table (`J:*` rows)

- **The defect:** Rows were added for `predicate` and `residuals` only. The profile claims to fix "every … cardinality, closed enum", yet `verdict`, `performance` and `effects` have no rows.
- **Counterexample:** An `effects` value that is absent or empty can be read as `not_requested`, which core forbids for requested effects.
- **Coverage caveat:** This finding stands unless a wildcard row outside the excerpt covers these fields.
- **Smallest repair:** Add rows:
  - `J:*.verdict`: 1, core verdict enum
  - `J:*.performance`: 1, core performance enum
  - `J:*.effects`: 1..*, core effect enum, one per declared part

### 8. Non-conjunctive sequential composition has no owner
**Location:** AXIOMATIC_CALCULUS `### AC-016 Typed Composition`, and the Position/provenance paragraph

- **The join:** Core delegates sequential composition "within a_c" to AC-016 and applies the declared-operator rule to the outer predicate. AC-016 invokes only conjunction ("when the composition claims that several constraints hold"). Meanwhile AC's provenance text says it "consume[s] its common … composition owners". Each side points to the other, and neither owns the rest.
- **Counterexample:** A fallback `F_D[w] compose F_P[v]` with outer predicate "a candidate from v or its fallback". v refuses and w succeeds. No AC rule decides the result, and conjunction would wrongly defeat it.
- **Smallest repair:** In AC-016, add: "Otherwise the composition declares its outer predicate and applies the core declared-operator rule ([result conjunction](FOUNDATIONS.md#result-conjunction))."

### 9. A stale admission basis may be reclassified as `invalid_basis`
**Location:** DESIGN_MODULE_METHOD `#### Admission contract use`

- **The tension:** "A stale … admission basis is `invalid_basis`". The next paragraph treats predecessor continuity as a required relation of the admission predicate. Core forbids "reclassifying a known failed join as a missing basis" unless the role is declared.
- **Counterexample:** A candidate is built on P1, and P2 is established as the current predecessor. DMM gives `invalid_basis`; if continuity is a join, core gives `falsified`.
- **Smallest repair:** Declare predecessor currency an admission condition of this evaluation, or map established discontinuity to `falsified` and keep `invalid_basis` for a contradictory or uninterpretable basis.
- **Coverage caveat:** UP-021's standing test is not visible.

### 10. Possible second owner for the tenant binding
**Location:** DESIGN_MODULE_METHOD, the new paragraph after **The projection.**

- **The tension:** "The build tenant owns this binding…" restates the binding obligations without naming an owner. COMMON *Build-Tenant Binding* places the statement in the Spec Method.
- **Divergence from COMMON:** The DMM list adds authority and omits COMMON item 3's units and boundaries.
- **Smallest repair:** Name the Spec Method locus as owner and frame this paragraph as its design-surface application.
- **Coverage caveat:** The Spec Method locus is not visible.

## Possible predecessor losses (unverified)

The DMM preamble rewrite removed two sentences:

- "Theoretical analogies supply no additional prerequisite."
- "Cross-member references preserve each relation's declared semantic scope and owner."

If either is a row in PREDECESSOR_CLAIMS, it needs a UP-015 disposition; I could not check this.

## Checked joins with no defect found

- The AC-007 verdict table against the core verdicts.
- The separation of availability, fitness and acceptance in AC (traversal note, `accepted`/`admitted`) and in the profile (`valid`/`admitted`/`ready`).
- `refused_effect` tightened to "no mutation began", and the unauthorized-mutation clause.
- Lost-acknowledgment handling after dispatch.
- DMM `## 8. Totality Rule`.
- The pinned-checker disclaimer. Whether it fits A_C_DEPENDENCY is not visible.
- The profile's in-domain exclusion of `out_of_frame`, which is a lawful refinement.
- The `out_of_scope` → `falsified` explanation.
