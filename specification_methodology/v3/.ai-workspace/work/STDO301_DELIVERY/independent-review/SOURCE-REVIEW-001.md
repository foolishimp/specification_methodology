# Cross-family source review 1

Received final response from Claude Opus 5.5. The Executive independently reverified all 83 native members and all 48 source effect hashes after the review; source identity remained unchanged. Reviewer wording and its stated limits follow without alteration. Its R1/R2/R3 labels differ from the requested feedback labels; the substantive authority, totality and exhaustion findings are retained.

**Overall result: `falsified`** for the bounded 3.0.1 amendment and its `candidate_ready` claim. That claim says P301-01–06 are realised in the owners and affected consumers with no additional normative change.

- **What holds:** the core P301-01 owner text in AXIOMATIC_CALCULUS §5 matches the proposal's meaning (the total-deterministic `F_D` contract, the evaluation-operation profile, the stop/exhaustion rules, no automatic `F_P`). P301-02–05 also match. There are no S0 or S1 findings.
- **What falsifies it:** one consumer changed meaning in a way the proposal never declared (F1), and the derivation and consumer-trace tables were not updated for the new kind (F4, F5).
- **What stays undecided:** F2, F3, F8 and F10 leave further parts `indeterminate`.

This is a working semantic assessment, not an acceptance decision. The inherited `not_ready` standing, the missing covering acceptance and actual-use evidence, and the pending supersessions are untouched and not discharged.

**Severity scale:** S0 = the subject or basis is invalid. S1 = falsifies a core P301 claim. S2 = material defect in the changed area; needs a correction or an explicit owner decision before the amendment's meaning can be accepted. S3 = local, trace or evidence defect that blocks stronger claims. S4 = clarity only.

**Subject:** commit `3204b84d`. The native root has 83 files, matching the inventory count. I could not compute any SHA-256 (no hashing tool), so byte identity is unverified by me. Unless stated otherwise, paths are under `specification_methodology/v3/build_tenants/common/standards/`. "Predecessor" means installed `v3.0.0-rc.1`.

## S2 findings

**F1. DESIGN_MODULE §2 governance scope silently narrowed** — `specification_methodology/v3/build_tenants/common/standards/DESIGN_MODULE.md:282-287`
- **Trigger:** the predecessor (lines 282-285) listed five governed classes; only the first was "`F_D` evaluators and proofs". The new sentence puts "common `F_D` operations qualified under §5" first and turns carrier constructors and admissions, deterministic transforms, effect shells and projections into "including" examples.
- **Consequence:**
  - A new deterministic transform without a totality proof, or an effect shell publishing to an external store, falls outside §2's stated scope. Yet item 3 (`:280`) and the predecessor both covered it.
  - The sentence implies effect shells are qualified `F_D`, which `:295` denies.
  - Only "existing helpers" keep their old scope (`:297-299`).
  - The source dispositions record this as "Conserved". `:2465` also says the contract is "imported in §2", but §2 only refers to it.
- **Correction:** restore the list structure so it is independent of any `F_D` claim, or record the narrowing as an owner-ratified change.

**F2. The stronger `F_D` contract has no failure outcome, and non-total deterministic work has no kind** — `specification_methodology/v3/build_tenants/common/standards/AXIOMATIC_CALCULUS.md:979-986`
- **Related lines:** `:1021-1026`; AC-015 at `:1036-1046`; AC-019 at `:1123-1141`; `TRAVERSAL_OCCURRENCE.md:280,285` (exactly one kind per occurrence) and `:1082-1088`; `RELEASE.md:727-732`.
- **Trigger:** under 3.0.0, every deterministic evaluation or proof was `F_D`. Now `F_D` requires totality and `F_P` is never automatic, but AC-015 still requires exactly one kind per application. The migration relation covers only existing uses.
- **Consequence:**
  - An application that claims `F_D` without a termination argument, or with an undeclared dependency, is not invalid under AC-019's conditions. No refusal, stop or core value is assigned to it.
  - A new non-total deterministic check (for example an unbounded proof search) can bind no lawful kind, and the outcome is not stated. Bounding it with fuel is implied at `:994-995` but never stated as the lawful route.
- **Correction (owner decision):** state in AC §5, AC-015 and AC-019 how an unestablished `F_D` claim is judged, and what successors do with non-total deterministic processing.

**F3. ODD A5's replacement for the old `F_D` authority is ambiguous and clashes with A1a** — `specification_methodology/v3/build_tenants/common/standards/ODD.md:1082-1092`
- **Trigger:** the predecessor (lines 1063-1066) said "F_D, ABG and product admission own durable evidence and closure truth". The new text says "the declared evaluation, ABG and Product admission and closure operations". But ODD defines evaluator work as `F_P` (`ODD.md:947`), and its results must be admitted before they count (`ODD.md:961-964`).
- **Consequence:**
  - Read literally, `F_P` evaluator work now helps establish durable evidence and closure truth. A5's own `F_P` prohibitions and A1a block the worst reading.
  - The predecessor's rule that this evidence comes from deterministic evaluation is dropped without a recorded decision.
  - The amendment requires "explicit authority owners" (`specification_methodology/v3/specification/requirements/STDO_3_0_1.md:37-38`).
  - The A5 text is verbatim from the selected proposal, so this is a proposal-level problem that construction did not reconcile.
- **Correction:** name the owners exactly (admission gates, ABG's closure fold, Product admission) and say that evaluator output establishes nothing until admitted. Otherwise record the change as an owner decision.

## S3 findings

**F4. The derivation table doesn't support the broader kind** — `specification_methodology/v3/build_tenants/common/standards/AXIOMATIC_CALCULUS.md:174`
- **Trigger:** row 13 now derives "total deterministic processing … distinct kinds" from premise (iii) (`:157-158`), which is only about deciding predicates. Construction is neither derived nor listed as an added choice.
- The derivation statement still says "evaluation … principles" (`:107-114`).
- `:997` cites ACTIVATION §3 as grounding, but ACTIVATION §3 is absent from the provenance list (`:61-96`), which the calculus identity record must bind completely (`:1237-1243`).
- **Consequence:** an added choice is presented as derived (FOUNDATIONS.md:624-632). The next calculus identity record's derivation basis may be incomplete.
- **Correction:** add a premise or list the construction scope as a §5 choice, and fix the provenance list.

**F5. Consumer and family traces not updated**
- AC row 13's consumer list (`AXIOMATIC_CALCULUS.md:198`) omits the new consumers: EVALUATION §2 (`:130-135`), SPEC_METHOD §11 (`:1800-1805`), DESIGN_MODULE §2, RELEASE §9 migration (`:715-753`), ACTIVATION §4 (`:1175-1181`), ODD A5 and §11.7A, and CONFORMANCE D301.
- FOUNDATIONS F22 row 4 (`FOUNDATIONS.md:1081`, consumers at `:1093`) omits AC-011, AC-016, ACTIVATION §2 and ACTIVATION §7.
- RELEASE's §9 row (`RELEASE.md:125`) doesn't trace the migration rules.
- **Correction:** extend the rows and consumer lists (discriminator 2, `CONFORMANCE.md:142`).

**F6. The release note drops the inherited standing** — `specification_methodology/v3/build_tenants/common/release/release-note.md:31-35`
- The predecessor note stated `not_ready`, owner acceptance `not_given`, covering review `unassigned`, and actual use unperformed. The new note only says those gates are "retained", and doesn't mention the pending supersessions.
- This weakens the requirement that release assets describe the cut accurately (`RELEASE.md:619`).
- **Correction:** state the current standing and pending supersessions explicitly before publication.

**F7. Some executable checks can't fail**
- The authority check compares two literal sets (`examples/deterministic_contracts.py:109-111`).
- The setup-exhaustion case is a literal dict checked against itself (`:144-146`).
- `:151` is a string tautology; the witness log has no grant check (`:89-91`); "resolution" is a JSON round-trip of a direct lookup (`:171-173`).
- Yet `CONFORMANCE.md:216-218` promises "executable model checks", and `DETERMINISTIC_CONTRACTS.md:45-46` overstates what the code checks.
- The checks with real discriminating power are the sortedness evaluator, copy and assessment exhaustion, the store table, the U/S/F/I state equivalence and the finite category laws.
- **Correction:** label D301-01, D301-04 case 3 and the D301-06 positive case as logical-review only, or model checks that can fail.

**F8. Qualified references: access and currentness are never exercised**
- Invalidators are carried but unused, and access is assumed (`DETERMINISTIC_CONTRACTS.md:114-127`; `deterministic_contracts.py:167-177`).
- So D301-06 (`CONFORMANCE.md:229`) tests only the S/I standing collapse, not the check in `ACTIVATION.md:699-701` or the rule that an inaccessible reference is a residual.
- **Correction:** add stale-target and inaccessible-target negative cases, or narrow D301-06.

**F9. The new `standards/examples/` payload isn't listed** in the README's cut-content list (`README.md:100-129`), the documents table (`:40-65`), or FOUNDATIONS' accounting of members without a family table (`FOUNDATIONS.md:603-622`). This matters because CONFORMANCE makes those files the home of the D301 contracts and oracles.

**F10. Migration row 2 is under-specified** — `RELEASE.md:725-732`
- Row 2 ("pending") never says whether the legacy meaning stays usable meanwhile. `:731-732` lets identical evidence take row 2 or row 3, so the disposition isn't determined by evidence, as `STDO_3_0_1.md:39-43` requires.
- The source dispositions also defer every in-corpus use to future owners, so no use has actually been assigned a row.
- **Correction:** state row 2's interim standing and the criterion that separates rows 2 and 3.

## S4 findings (clarity only)

- `AXIOMATIC_CALCULUS.md:1059-1060`: AC-016's "probabilistic proposal, deterministic evaluation" became "construction, evaluation". The guarantee survives through `:1057-1058`, but the change is undeclared.
- `RELEASE.md:719-720`: the preserved profile omits invalidation and permitted writes from the seven parts listed at `AXIOMATIC_CALCULUS.md:1012-1014`.
- `SPEC_METHOD.md:1802-1803`: the sentence can be parsed two ways.
- `ACTIVATION.md:708-709`: the hash-matching sentence reads as a rule for all digest matching; it should be scoped to sufficiency claims.
- Undefined symbols: `f_B`, `D_B` and `Outcome_B` aren't tied to `X_v`, `Y_v` and `Omega_v` (`AXIOMATIC_CALCULUS.md:980` vs `:951`), and `delta`, `alpha`, `T`, `T_hat` and `u` are undefined in `FOUNDATIONS.md:1237-1240`.
- Example wording:
  - Denial is called "refusal" in the table and code but "permission_denied" in the prose (`DETERMINISTIC_CONTRACTS.md:30-36`).
  - The assessment-exhaustion row should say the report is the stop's closed result, to keep "exactly one outcome" (`:57-64`).
  - "Six finite operations" (`:162`) are never enumerated.
  - The setup row (`:65`) drops "the enclosing step retains its own stop".
- `CONFORMANCE.md:222-231`: the D301 rows lack the check column the other rows have (`:131-132`), and D301-05 omits the human-handover binding the proposal places in conformance.
- `DETERMINISTIC_CONTRACTS.md:146-158`: the categorical example lacks the a_c representation that `FOUNDATIONS.md:677-684` requires; it should be classed as a finite mathematical argument.
- `release-note.md`: "is prepared" (`:37`) reads as completed, and the version assessment (`:24-29`) doesn't disclose that ODD's kind-level `F_D` authority is superseded.
- `specification_methodology/v3/build_tenants/README.md:9-13`: the "Current Task" section names only T-003.
- AC §5 states that the kind grants no authority only implicitly (`:1006-1010`, `:1017-1018`), while four consumers restate it in their own words (ODD:1089-1090, DESIGN_MODULE:294-295, EVALUATION:132, RELEASE:733-734).

## Per-item disposition

| Item | Result | Basis |
|---|---|---|
| P301-01 | Owner text satisfied; reconciliation falsified; parts indeterminate | AC §5 matches the proposal; ODD A5 replacement is verbatim; edition clause present; F1–F4, F10 |
| P301-02 | Satisfied | FOUNDATIONS:1227-1255; AC-011, AC-016 and ACTIVATION §7 refer to the owner; the U/I counterexample is sound (F5 trace gap) |
| P301-03 | Text satisfied; discriminator partial | ACTIVATION:695-714; no mandatory carrier; F8 |
| P301-04 | Satisfied | FOUNDATIONS:703-711; the 10-arrow chain category and terminal map are correct; constant projection can't factor; H1 stays open |
| P301-05 | Satisfied | EVALUATION:453-469 is optional and imposes no trial count or new review cycle |
| P301-06 | Partially falsified | D301-01–08 have applicability; compatibility statements are honest; frames checked as source-coherent; F1, F5–F7, F9 |

## The three targeted repairs

The corpus doesn't name them. I took them to be (R1) the three-way migration with no automatic `F_P`, (R2) predicate-specific exhaustion, and (R3) the four-state witness limited to sufficiency.

- **R1 holds, with gaps.** I ran six cases through the migration table:
  - A closed finite evaluator, and an infinite domain with structural termination, both take row 1.
  - An undeclared file dependency takes row 2 or row 3 (see F10).
  - A semi-decidable proof search gets a bounded successor plus a retained legacy original.
  - An ODD gate keeps authority only through its own contract.
  - A legacy occurrence stays on its old calculus edition.

  The remaining gaps are F10, and F2 for new uses.
- **R2 is satisfied.**
  - Copy exhaustion: the work result is `incomplete`, so candidate availability is falsified.
  - Assessment exhaustion: the property is `indeterminate`, while report availability is satisfied.
  - Setup exhaustion: there is no assessment result; the step itself is `incomplete`.

  None maps to satisfied, consistent with ACTIVATION:1009-1039 and FOUNDATIONS Results.
- **R3 is satisfied** (FOUNDATIONS:1248-1255; DETERMINISTIC_CONTRACTS:107-110).

The separate Definition design-binding repair is present outside the payload (`specification_methodology/v3/stdo_3.json:149-158`), and the builder basis is unchanged (`:19-22`).

## What I checked and what remains unqualified

**Checked:**
- The old vs new `F_D` meaning, and whether its guarantees survive across AC, RELEASE, EVALUATION and ODD.
- That the kind grants no authority, across all consumers.
- The exhaustion chain from AC §5 through ACTIVATION §3 and FOUNDATIONS Results to the examples and the code.
- The migration cases above, and edition/URN immutability.
- Continuation sufficiency under a fixed policy and horizon.
- Qualified references, and functor laws vs consumer adequacy.
- That the comparison guidance stays optional.
- The ac-task-a §5 frame excerpt, which is verbatim; frame owner digest prefixes, which match the inventory; no old wording left in frames.
- The derivation and trace tables.
- That nothing from the Claude cached-expertise note was adopted.

**Unqualified (not done or not possible):**
- No hashes computed; full byte diffs of the 13 changed members not done (deltas were located by searches and side-by-side reads).
- FRAME_INPUTS section digests not verified; the Python was not run.
- Not assessed: the supplemental Graphify representation, the native-release tooling, and the publication-layout mapping (the manifest schema fixes the standards source root to `specification/standards` and release-note paths to `releases/v*.md`).
- Unchanged members were only searched, not read.
- Inherited whole-method obligations and actual use were not assessed.
- The builder was consulted only for its result-conjunction rule.

**Limits:** spend was about US$11 by the session meter. Wall time wasn't instrumented, so I can't confirm the 30-minute budget was kept.

## Independence and access

- **Author vs reviewer:** I'm Claude Opus 5.5, and I authored none of the subject. The proposal and the delta are by Codex, so this review is cross-family for the delta.
- **Same-family relations:** the cached-expertise input is by Claude Fable 5.1 (same family as me, but not adopted). The 3.0.0 baseline came from a frozen Claude-tenant candidate, so the inherited text I relied on for F1 and F3 has same-family ancestry.
- **Access:** I used Read, Glob and Grep on the worktree and both installed releases, with no shell and no writes; the Executive should still confirm byte identity.
- **Records used:** I read the consumer dispositions and the cached-expertise triage only after deriving my own obligations. I searched `RETURN.md` once, only to identify the repairs, and did not open `CHECKS.json`, `PACKAGE_CHECK.json` or the private run logs.
