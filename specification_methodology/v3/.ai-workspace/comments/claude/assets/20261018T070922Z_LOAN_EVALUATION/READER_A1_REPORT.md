## Causes

### I3-R2-R003 — AC-014 judgment signature (home row 02)

**What it changes.** rc.2 AC-014 (`rc2/standards/AXIOMATIC_CALCULUS.md` 639-665, quoted in `rows/02.md` 10-35) obliges a 14-field `Judgment` record pointing to an unchanged subject, with promotion an explicit relation. Line A's AC-014 (`A/standards/AXIOMATIC_CALCULUS.md` 739-760) adds `predicate`, `verdict`, `performance`, `effects`, `residuals`, and states "Each field is required by this semantic contract" (771) and "`decision` retains the original calculus or interpreted-domain outcome; it is not another verdict enum" (767-768). The record contract is widened and `decision` is newly constrained.

**Meaning test.** Changes element 1 (obligation: five more required fields; `decision` may no longer carry the verdict). The unchanged-subject and promotion sentences (762-764) are verbatim. Not a relocation.

**Does each line make it?** A: yes, at AC-014 728-788 and the core record it binds, `A/standards/FOUNDATIONS.md` 367-372 ("Its core record contains the predicate, exact subject and basis, verdict, performance, original qualified domain outcome…"). B: no. `B/standards/AXIOMATIC_CALCULUS.md` 892-920 restates the 14 fields and both sentences verbatim; B's Judgment object (`B/standards/FOUNDATIONS.md` 67) has "evaluator, decision, evidence, scope and revising observation". B realises the core-value/predicate pairing at the result level instead (`B/standards/FOUNDATIONS.md` 811-816, Recording).

**Common input.** The distinctions are required: results of judgements stated in the core (`common/README.md` 162), "The core value travels with the evaluated predicate and the original domain outcome" (169), not-performed and unknown-effect kept distinct (167-168). The record fields are a tenant realisation, permitted not prescribed. Whether B's 14-field Judgment, which carries no predicate or core-value field, meets README 169 is a conformance question for B, not a meaning question for this row.

### I3-R2-R012 — RF-012 closed results (home row 27)

**What it changes.** rc.2 RF-012 (`rc2/standards/REFERENCE_FRAME_METHOD.md` 409-423, `rows/27.md` 10-23): every evaluation returns a member of its declared algebra; the five-value baseline family with meanings; "An externally owned compatible extension may refine this algebra while preserving explicit indeterminate, out-of-frame, and invalid-basis pressure." A's RF-012 (`A/standards/REFERENCE_FRAME_METHOD.md` 485-521) binds every result to "its exact frame, activation, subject, basis and predicate" (487-488), adds performance (`performed`/`not_performed`/`unconfirmed`, 512-516) and effect state to every result (513), adds admission-result rules (495-510), and replaces the extension permission with one explicit mapping plus a no-erasure list (489-493, 518-520).

**Meaning test.** A: elements 1 (binding, performance, effect-state and admission obligations) and 4/1 (refinement permission conditioned on one mapping and non-erasure; "externally owned" dropped). B (`B/standards/REFERENCE_FRAME.md` 396-411): "Every performed evaluation of a frame returns one closed result" (398) — the obligation's scope now excludes unperformed evaluations, which "has no result" (407-408; `B/standards/FOUNDATIONS.md` 840-847: never mapped to `indeterminate`); refinement must map "each of its values to exactly one core value" and "raises no result's standing" (B/AC-007 546-547; FOUNDATIONS 862-876). Element 4 and element 1 (tightened permission), narrower than A's. Relocating the five values to Foundations (B FOUNDATIONS 795-801 restates them verbatim; A FOUNDATIONS 385-391 rewords) is a move and preserves meaning.

**Does each line make it?** A: yes (RF-012 485-521; FOUNDATIONS 383-434 verdict/performance, 435-459 effects, 461-478 refinements). B: yes, narrowly (RF-012 396-411; FOUNDATIONS 790-801, 828-860, 862-883).

**Common input.** Required: one core owned by Foundations (`common/PRODUCT.md` 129; `common/README.md` 162), each refined value maps "to exactly one core value" (163), not-performed distinct from undecidable (167), unknown effect distinct (168). Moving the determination to a shared owner is conservation (README 67). A's performance/effects fields and admission rules are a permitted realisation; B's "no closed result" is another. No conflict found.

### I3-R2-R015 — Result conjunction (home row 25)

**What it changes.** rc.2 (`rc2/standards/REFERENCE_FRAME_METHOD.md` 674-691, `rows/25.md` 10-26): a declared rule states five things (mandatory results; "how conflict and indeterminacy are handled"; basis agreement; decision authority; veto/defer); agreement cannot discard a single-contributor counterexample; "Missing, wrong-subject, conflicted or indeterminate mandatory results remain unresolved under the declared rule". A's RF text (`A/standards/REFERENCE_FRAME_METHOD.md` 797-801) replaces bullet 2 with "how conflicting or indeterminate contributions are routed for re-evaluation", and A's core (`A/standards/FOUNDATIONS.md` 549-561) fixes the verdict precedence: "Any authenticated, applicable falsification of a required predicate or material join makes the conjunction `falsified`. Missing or undecidable other coverage remains explicit alongside it" (551-553), then invalid_basis, out_of_frame, indeterminate.

**Meaning test.** A: element 1/4. The declared rule loses its latitude over how conflict is handled and which non-satisfied value is reported; a composite with a falsification and a missing mandatory slot is `falsified` where rc.2 left it "unresolved under the declared rule". B (`B/standards/FOUNDATIONS.md` 1086-1109): keeps the declared rule's latitude ("reports a non-satisfied value chosen by its declared rule… no universal order", 1091-1095) but fixes `invalid_basis` for basis disagreement (1095-1098) and `indeterminate` for gap-only cases (1098-1103), makes a single-contributor counterexample falsify the conjunction (1105-1108), and adds a sixth required item to the declared rule, "how results that are not mandatory count" (1115). Element 1, narrow. If "remain unresolved" is read as `indeterminate`, B's gap rule is a restatement; its basis-disagreement and sixth-item determinations are not.

**Does each line make it?** A: RF 791-807 and FOUNDATIONS 496-623 (authentication 541-547; precedence 549-561; declared operator 575-591). B: RF 625-633 delegates wholesale; FOUNDATIONS 1008-1130 (three inputs 1020-1030; survival 1068-1078; reported value 1086-1109; declared rule 1111-1118).

**Common input.** Required: "Conjunction and composition of results are defined once, over the core" (`common/README.md` 171), both comply; failure visible beside missing coverage (README 101; `common/PRODUCT.md` 222 "a known failure is not erased because another obligation is unresolved"), both comply. A's fixed precedence and falsified-with-gaps verdict go beyond "visible" and are permitted; B's declared-rule latitude is permitted. No conflict.

## Rows

**Row 01 — `AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal`**
- Claim: each constraint names subject, predicate, judgment kind, latitude, refusal; a failed/missing/indeterminate/out-of-scope/invalid-basis result follows the declared algebra, never coerced to success.
- A: changed (1, 4). `A/standards/AXIOMATIC_CALCULUS.md` 458-459 adds `basis`; 460-461 core owns the algebra; 490-493 "`hold`, `gap`, `refusal` and `refuse` always carry a declared cause"; 502-504 implementations bind mappings before execution and retain performance and effects.
- B: changed (1, 4). `B/standards/AXIOMATIC_CALCULUS.md` 544-547 algebra narrowed to core or one-to-one refinement; 569-572 a missing result "has no closed result, is never `indeterminate`" (rc.2: a missing result follows the algebra); 592-604 cause is part of a refusal's value and `refusal(constraint)` takes precedence over any basis condition.
- Same change? partly (core algebra; missing distinct from indeterminate; cause-carrying refusals).
- Only in A: `basis` binding, performance/effects retention (503-504). Only in B: constraint-over-basis precedence (595-604), `gap` limited to open resolution and dangling references refuse (588).
- Common input: core mapping and not-performed distinction required (`common/README.md` 157-163, 167); the additions are permitted.
- Records: A accurate. B inaccurate: `conserved` over a tightened algebra and a changed missing-result determination that B's own note calls "tightened" and "new" (`rows/01.md` 35).
- Note: Both lines keep the no-coercion rule; they differ on refusal precedence and on where performance lives.

**Row 02 — `AXIOMATIC_CALCULUS.md#ac-014-judgment-separation`**
- Claim: a 14-field judgment points to an unchanged subject; issuing it does not alter the subject; promotion is an explicit relation.
- A: changed (1). `A/standards/AXIOMATIC_CALCULUS.md` 739-760 (19 fields), 766-773.
- B: unchanged. `B/standards/AXIOMATIC_CALCULUS.md` 898-919 verbatim fields and sentences.
- Same change? n/a.
- Only in A: required `predicate`, `verdict`, `performance`, `effects`, `residuals`; `decision` "not another verdict enum" (767-768). Only in B: none.
- Common input: distinctions required (`common/README.md` 162, 167-169); field layout permitted.
- Records: A accurate. B accurate.
- Note: see cause R003.

**Row 03 — `AXIOMATIC_CALCULUS.md#ac-016-typed-composition`**
- Claim: traversals compose only when the first result type and judgment satisfy the second's domain; composition retains identities, results, judgments, evidence, authority, provenance, stops; no universal F_P→F_D→F_H sequence.
- A: changed (1). `A/standards/AXIOMATIC_CALCULUS.md` 886-891: the composite's result "uses the core conjunction or declared-operator rule… its effect boundary includes the traversals' material effects"; 896-898 categorical demonstration standard.
- B: unchanged. `B/standards/AXIOMATIC_CALCULUS.md` 1025-1038 verbatim.
- Only in A: composite result and effect-boundary obligations. Only in B: none.
- Common input: composition of results defined once over the core (`common/README.md` 171) requires some owner to decide the composite result; A binds it here, permitted.
- Records: A accurate. B accurate.
- Note: A adds determinations rc.2 left silent rather than altering the retained ones.

**Row 04 — `AXIOMATIC_CALCULUS.md#ac-017-interpretation-fidelity`**
- Claim: admitted model records map to subject provenance or are marked model-local; each evaluated declaration has one of five dispositions; absence is not immateriality without recorded basis and authority.
- A: changed (1). `A/standards/AXIOMATIC_CALCULUS.md` 951-963 per-treatment preservation predicate with core mapping; 985-991 "Fidelity evidence compares source and model on independently specified permissible, prohibited and unresolved decisions"; latitude retained unless admitted loss is recorded.
- B: unchanged. `B/standards/AXIOMATIC_CALCULUS.md` 1077-1082 verbatim.
- Only in A: fidelity-evidence and per-treatment evaluation obligations; O/E/C/L/X role statement (965-972). Only in B: none.
- Common input: fidelity evidence on independently specified cases is required somewhere (`common/README.md` 85-86); A places it here.
- Records: A accurate. B accurate.
- Note: A's record itself calls the added proof obligation a proposed replacement.

**Row 05 — `AXIOMATIC_CALCULUS.md#derivation-provenance`**
- Claim: the listed STDO clauses are provenance; the definitions below are "the sole normative authority for the meaning of `a_c`"; F_D/F_P/F_H are introduced here, derived from those clauses; issued bases record the absolute addresses; derivation is one-way.
- A: changed (5). `A/standards/AXIOMATIC_CALCULUS.md` 103-105: the laws "own the `a_c` specialization… and explicitly consume its common result and composition owners" replaces the sole-authority claim; 113-115 the three kinds are "a calculus policy, not a theorem forced by those predecessor clauses" (descriptive, not one of the five); 120-121 `principle_refs` field correction.
- B: unchanged. `B/standards/AXIOMATIC_CALCULUS.md` 104-106 keeps "sole normative authority for the meaning of `a_c`"; 115-116 keeps "from which the generic definitions are derived"; 121-122 same field correction; the clause list is re-pointed to B's members with rc.2 derivations beside each (72-102).
- Only in A: shared-owner consumption statement. Only in B: none beyond relocation.
- Common input: Foundations must own the result algebra (`common/PRODUCT.md` 129; `common/README.md` 162), so A's drop of "sole" follows the common requirement; B's retained sentence sits in tension with B's own import of the core (`B/standards/AXIOMATIC_CALCULUS.md` 550-553), a conformance point, not a conservation defect.
- Records: A accurate. B accurate.
- Note: the `release_uri`→`principle_refs` correction is made identically in both lines and matches the record shape (`B/standards/AXIOMATIC_CALCULUS.md` 1182-1186).

**Row 06 — `AXIOMATIC_CALCULUS.md#position`**
- Claim: a_c's identities; it defines sorts…validity laws independent of carrier/runtime; no claim of completeness etc. without proof; principles are provenance; calculus, interpreted model and carrier are distinct layers.
- A: unchanged. `A/standards/AXIOMATIC_CALCULUS.md` 26-48 retains every claim; 9-24 adds F1–F6 premises and that AC-007/014/016 consume shared owners (additive); 38 "specialization of" for "derived from" and 57 "provenance" arrow are descriptive.
- B: unchanged. `B/standards/AXIOMATIC_CALCULUS.md` 22-61; adds the formal-fragment pointer (42-44).
- Only in A: consumption statements (19-22). Only in B: none.
- Common input: not material.
- Records: A inaccurate: `superseded` over a section whose own determinations are unchanged (the ownership change it describes lives in rows 01, 02, 05, 27). B accurate.
- Note: the inventory's granularity rule confines this row to the position text.

**Row 09 — `DESIGN_MODULE_METHOD.md#9-effect-edge-rule`**
- Claim: effects should be explicit and isolated; kernels should not decide law and perform effects; preferred four-step sequence; a function doing both is suspect.
- A: changed (1). `A/standards/DESIGN_MODULE_METHOD.md` 2048-2053 "Bind the actual write, publication, invocation or other effect boundary to the core effect record" and Workspace and context decides unknown-effect reconciliation.
- B: unchanged. `B/standards/DESIGN_MODULE.md` 1830-1839 restates all four parts at `should` force.
- Only in A: core effect record binding. Only in B: none.
- Common input: effects in the core are required somewhere (`common/README.md` 162, 168); A binds them here, permitted.
- Records: A accurate. B accurate.
- Note: A keeps the rc.2 preferences at `should`; the added binding is imperative.

**Row 11 — `DESIGN_MODULE_METHOD.md#cross-view-axiom-evaluation`**
- Claim: the pack must evaluate every applicable axiom with pass/fail/not_applicable-with-reason; ten minimum columns; eleven proofs; graph-native visibility; blocking constructor.
- A: changed (1, 4). `A/standards/DESIGN_MODULE_METHOD.md` 1496-1509 labels map to five verdicts, a supported `not_applicable` falsifies the applicability predicate, performance required; 1518 fourteen columns.
- B: changed (narrow; 1, 4). `B/standards/DESIGN_MODULE.md` 1481-1483 keeps the three-verdict sentence and ten columns (1486), but 1521-1522 `not_applicable` "rests on a false applicability premise, an unresolved premise supports no `not_applicable`", and 1533-1541 an evaluated axiom reaching none of the three verdicts "records in the Verdict column the core value its cause selects" — a fourth outcome class in a closed set.
- Same change? partly (both map pass/fail; both tighten not_applicable); they differ on its value (A: falsified applicability; B: satisfied on a declared disjunction, 1513-1515).
- Only in A: performance column and `unconfirmed`; exclusion not conjoined as a failed axiom (1511-1514). Only in B: the disjunctive predicate and ACTIVATION §1 applicability binding (1517-1524).
- Common input: core mapping required (`common/README.md` 162-163); both permitted realisations.
- Records: A accurate. B inaccurate: its note concedes "tightening the predecessor implies and does not state" (`rows/11.md` 69).
- Note: B's widened Verdict column is the clearer meaning change; its not_applicable tightening is arguably derivable from applicability law.

**Row 12 — `ODD_METHOD.md#115d-constructive-evaluation-and-yield-loop`**
- Claim: one constructive loop with four named functions, external outcome authority, terminal conditions, the authority shape, A0–A16, the constitutional equation.
- A: changed (1). `A/standards/ODD_METHOD.md` 883-891 terminal conditions become control reasons returned through "the core stop contract"; 1030-1040 "L cannot overrule contrary current observations of W" with an admission duty; 1150-1158 `evaluate_action` evaluates obligations through core conjunction; 1197-1221 closure decisions bind a decision predicate with per-obligation verdict rules and `performance`.
- B: changed (narrow; 1). `B/standards/ODD.md` 792-796 the loop "is this profile's binding of ACTIVATION §1 Feedback and diagnosis… its diagnoses distinguish the four causes named there"; the closure-decision mapping (1122-1179) and typed no-action results (1019-1044) are additive and keep "The seven decisions of A8 stay the closed vocabulary" (1143).
- Same change? partly (both map closure decisions into the core).
- Only in A: stop contract; L/W currentness admission; A6 conjunction; A8 decision predicate and `not_performed`/`unconfirmed` rules. Only in B: four-cause diagnosis duty; cause-split decisions `retry(defeated)`, `repair(proof)`, `re-enter(basis)`…; closure decision ≠ ACTIVATION disposition (1181-1198).
- Common input: four-cause diagnosis is required (`common/README.md` 110); core mapping required (162); both realisations permitted.
- Records: A accurate. B inaccurate on the narrow added diagnosis duty; the mapping B labels "new" is additive.
- Note: both lines carry the equation and A0–A16 text; I sampled A 860-905, 970-990, 1025-1045, 1120-1160, 1190-1222 and B 785-830, 1015-1050, 1115-1210, not the full 600-line sections.

**Row 17 — `REFERENCE_FRAME_METHOD.md#evidence-or-coordinate-translation`**
- Claim: a translation declares source/target coordinates, preserved meaning, accepted loss, provenance, equality law, refusal conditions.
- A: changed (1). `A/standards/REFERENCE_FRAME_METHOD.md` 816-827 adds an evaluated translation predicate with core mapping and "All cases preserve actual performance and effects".
- B: unchanged. `B/standards/REFERENCE_FRAME.md` 636-639 verbatim; 639-647 points preserved-meaning content to ACTIVATION §4 and AC-013 (derivation by reference).
- Only in A: translation result mapping. Only in B: none.
- Common input: core mapping required (`common/README.md` 162); permitted here.
- Records: A accurate. B accurate.
- Note: A's record calls the mapping "explicitly proposed".

**Row 19 — `REFERENCE_FRAME_METHOD.md#method-functions`**
- Claim: seven relation signatures an application may implement in any conforming form; `conjoin -> decision | conflict | indeterminate`; no callable interface required.
- A: changed (1). `A/standards/REFERENCE_FRAME_METHOD.md` 659-660 `conjoin -> core_result + retained_conflicts + residuals`; 673-680 outcomes are domain outputs evaluated through RF-012.
- B: changed (narrow; 1). `B/standards/REFERENCE_FRAME.md` 532-553 signatures verbatim; 580-583 `conflict` becomes a `falsified` case ("mandatory results for the same claim disagree"); 576-579, 584-588 activation and translation refusals split by cause with fixed core values.
- Same change? partly (conflict ceases to be an unresolved aggregate outcome in both).
- Only in A: changed signature; Dispose consumption (675-678). Only in B: cause-split `activation_refusal(capability|authority|basis)` with `out_of_frame`/`invalid_basis` values; gaps are "no outcome of `conjoin`" (600-604).
- Common input: refinement mapping required (`common/README.md` 163); permitted.
- Records: A accurate. B inaccurate (narrow): the mapping its note calls "new" fixes what `conflict` establishes.
- Note: B's `activation_refusal(capability)`→`out_of_frame` and A's admission failure→`falsified` on the admission predicate are different realisations of the same case.

**Row 20 — `REFERENCE_FRAME_METHOD.md#method-self-qualification`**
- Claim: qualification uses external protocols; fresh constructor in a declared envelope; independent evaluator compares frozen results with the nine-row relation population; staged verdicts state what was evaluated; exemplars optional.
- A: changed (1). `A/standards/REFERENCE_FRAME_METHOD.md` 1355 `conjoin` row now exercises core conjunction: "authenticated applicable failure retained beside missing coverage… Conflict, veto and refusal remain… annotations, never replacement verdicts".
- B: changed (1). `B/standards/EVALUATION.md` 639 `conjoin` row: basis mismatch returns `invalid_basis`, veto returns the RF §5 outcome (rc.2: conflict, indeterminate or refusal); 613-617 withholding of expected outcomes until freeze; 670-687 falsity conditions; 689-702 "Recoverability benchmark (new…)".
- Same change? partly (both drop `refusal` as a conjoin return).
- Only in A: core-precedence observation. Only in B: withholding rule, falsity list, recoverability benchmark.
- Common input: not material beyond README 171; B's withholding rule relocates UP-022 (B 624-626), permitted.
- Records: A accurate. B inaccurate: `conserved` with a changed required observation and an added benchmark.
- Note: all other rows of the population table are verbatim in both lines.

**Row 21 — `REFERENCE_FRAME_METHOD.md#minimal-frame-activation-binding`**
- Claim: the listed carrier-neutral fields suffice to bind one frame for one evaluation; fields resolve through stable identities.
- A: changed (1). `A/standards/REFERENCE_FRAME_METHOD.md` 1161 field "exact evaluation and applicable core-result predicate or declared refinement" replaces "closed result algebra".
- B: unchanged. `B/standards/REFERENCE_FRAME.md` 1004 verbatim field.
- Only in A: predicate/refinement field. Only in B: none.
- Common input: follows R012; permitted.
- Records: A accurate. B accurate.
- Note: narrow template change following the result-algebra move.

**Row 22 — `REFERENCE_FRAME_METHOD.md#minimal-frame-declaration`**
- Claim: the twelve-section frame declaration template.
- A: changed (1). `A/standards/REFERENCE_FRAME_METHOD.md` 1415 "applicable core-result refinement" for "closed result algebra".
- B: unchanged. `B/standards/REFERENCE_FRAME.md` 1086 verbatim.
- Only in A: the field change. Only in B: none.
- Common input: permitted.
- Records: A accurate. B accurate.
- Note: as row 21.

**Row 23 — `REFERENCE_FRAME_METHOD.md#position`**
- Claim: the method's scope (finite actors, all work kinds), engagement meta-method boundary, ownership of its bounded context and "only its … result … concepts", substrate neutrality.
- A: unchanged. `A/standards/REFERENCE_FRAME_METHOD.md` 51-54, 75-92 retain every claim including 84-85; 56-73 add premises and consumption statements (additive).
- B: unchanged. `B/standards/REFERENCE_FRAME.md` 58-80 retains the claims; 82-118 adds an import table naming FOUNDATIONS as owner of the core results (103).
- Only in A: "they do not create another core result family" (70-71). Only in B: import table (96-108).
- Common input: not material; relocation of the core is conservation (`common/README.md` 67).
- Records: A inaccurate: `superseded` over retained determinations. B accurate.
- Note: both keep the "owns only its … result … concepts" sentence while importing the core; the substantive change is row 27's.

**Row 24 — `REFERENCE_FRAME_METHOD.md#reference-frame`**
- Claim: a frame is the 12-tuple ⟨Q…D⟩, a relation not a schema; a representation is a projection; bound when every coordinate resolves.
- A: unchanged. `A/standards/REFERENCE_FRAME_METHOD.md` 268-304; 288 describes R as "the shared core result algebra with the frame's declared refinements".
- B: unchanged. `B/standards/FOUNDATIONS.md` 208-226; 213-214 R "the closed result algebra (§4 Results, or a refinement mapped into it)".
- Only in A / Only in B: none material.
- Common input: not material.
- Records: A inaccurate (`superseded` over an unchanged tuple whose R follows RF-012 either way). B accurate.
- Note: both lines' R parentheticals point at the owner judged in row 27.

**Row 25 — `REFERENCE_FRAME_METHOD.md#result-conjunction`**
- Claim: see cause R015.
- A: changed (1, 4). `A/standards/REFERENCE_FRAME_METHOD.md` 797-801; `A/standards/FOUNDATIONS.md` 549-561.
- B: changed (narrow; 1). `B/standards/REFERENCE_FRAME.md` 627-632 delegates; `B/standards/FOUNDATIONS.md` 1095-1109, 1115.
- Same change? partly.
- Only in A: fixed precedence; "routed for re-evaluation"; declared-operator well-formedness rule (575-591). Only in B: three-input structure (1020-1030), stale-results rule (1039-1066), sixth declared-rule item.
- Common input: README 171 required; precedence choices permitted; README 101 satisfied by both.
- Records: A accurate. B inaccurate (narrow).
- Note: B keeps every rc.2 sentence of the declared rule and the survival paragraph (1068-1078) nearly verbatim.

**Row 27 — `REFERENCE_FRAME_METHOD.md#rf-012-closed-results`**
- Claim: see cause R012.
- A: changed (1, 4). `A/standards/REFERENCE_FRAME_METHOD.md` 487-493, 512-520.
- B: changed (narrow; 4, 1). `B/standards/REFERENCE_FRAME.md` 398-408; `B/standards/FOUNDATIONS.md` 840-847, 862-876.
- Same change? partly (core owned by Foundations; one-to-one refinement; not-performed distinct).
- Only in A: performance states, effect state per result, admission-predicate rules. Only in B: "no closed result" realisation of non-performance; three-way out_of_frame boundary (895-939).
- Common input: required (`common/README.md` 162-168).
- Records: A accurate. B inaccurate (narrow): the `performed` scope restriction and tightened refinement conditions change the rc.2 determinations.
- Note: B's note treats the extension clause as a refinement whose owner is named; the one-to-one condition is still new.

**Row 28 — `REFERENCE_FRAME_METHOD.md#select-and-activate`**
- Claim: select one frame/configuration; activation binds declaration to exact subject and basis and loads declared material; with no lawful pairing, activation "returns a refusal or `out_of_frame` pressure"; no implied context.
- A: changed (1, 4). `A/standards/REFERENCE_FRAME_METHOD.md` 729-733: activation returns an RF-012 refusal; `out_of_frame` on the work predicate "is not fabricated from the activation refusal"; 715-727 contract application.
- B: unchanged. `B/standards/ACTIVATION.md` 834-845 keeps both rc.2 options and assigns each to its case (out_of_frame when no pairing declares a needed relation or capability, otherwise the causal refusal), derivable from RF-012's out_of_frame meaning.
- Only in A: admission/work predicate split. Only in B: case assignment.
- Common input: not material.
- Records: A accurate. B accurate.
- Note: B's case split is borderline; I read it as a derivation, not a new determination.

**Row 29 — `RELEASE_METHOD.md#exact-cut-qualification`**
- Claim: qualification binds the six listed coordinates; evidence matches the claim; RC accepted only on complete review and human acceptance; byte changes move to a higher RC.
- A: changed (1). `A/standards/RELEASE_METHOD.md` 306-322 per-item contract application and label mapping (`passed`→`satisfied` only with established performance; `skipped`/`cached green`→`indeterminate`); 299 "owner verdicts" split into "assessment results, owner decisions".
- B: unchanged. `B/standards/RELEASE.md` 338-359 verbatim.
- Only in A: item-level core evaluation. Only in B: none.
- Common input: core mapping required somewhere (`common/README.md` 162); permitted here.
- Records: A accurate. B accurate.
- Note: A's "review result" for "verdict" (326) is wording.

**Row 36 — `SPEC_METHOD.md#proportional-disposition`**
- Claim: assessment returns one of accept/local_repair/re_enter/reject with the stated conditions; global correctness definition; repeated-rejection reassessment; no count threshold.
- A: changed (5, 1). `A/standards/SPEC_METHOD.md` 1935-1940 assessment returns evidence and a proposed disposition, Dispose applies the decision; 1942-1950 cause-split verdict table incl. missing-reason row.
- B: changed (5). `B/standards/ACTIVATION.md` 1058-1062 "The decision owner disposes… An assessor may recommend one; the recommendation is evidence… never a disposition"; 1068-1073 conditions verbatim with core values; 1085-1093 remaining rules verbatim.
- Same change? partly (both move the disposition from assessment to the decision owner).
- Only in A: cause-split verdicts (`local_repair` → falsified or indeterminate). Only in B: fixed single mapping (`local_repair`→falsified, `re_enter`→invalid_basis).
- Common input: availability/assessment/acceptance separate (`common/README.md` 170) — both comply; mapping required (162).
- Records: A accurate. B accurate with the disclosed carve-out ("save the returning party split to the child row below", `rows/36.md` 48); the child row is outside this packet.
- Note: cannot verify the child row's disposition.

**Row 40 — `SPEC_METHOD.md#universal-intake-triage`**
- Claim: one front door; triage must determine six things; no bypass; triangulation across frames; smallest configuration; six change classes with re-entry; below-Goals assertion; missing class is drift.
- A: changed (1, 4). `A/standards/SPEC_METHOD.md` 1422-1431 diagnosis must distinguish four causes; 1450-1458 contract application; 1473 `realization_refactor` widened to "implementation, procedure, configuration, or attribute change".
- B: changed (1). `B/standards/SPEC_METHOD.md` 846-854 four-cause diagnosis; 865-869 frame results combine under the one conjunction; 896-897 "Triage records the change intent, the class, the re-entry point and when triage occurred".
- Same change? partly (four-cause diagnosis in both).
- Only in A: procedure scope; computed-treatment routing. Only in B: recording duty; classes "map to no core value" (900-909).
- Common input: four-cause diagnosis required (`common/README.md` 110; `common/PRODUCT.md` 76).
- Records: A accurate. B inaccurate (narrow): an added required determination recorded as conserved.
- Note: the six determinations and six classes are carried in both.

**Row 42 — `STDO_REFERENCE_FRAME_BASELINE.md#3-worker-returns-to-executive`**
- Claim: every coordinated Worker activation ends in one closed WorkerResult sent to Executive; the four variants map one-to-one from RF results after lawful activation; Worker stops and does not activate Reviewer.
- A: changed (3, 4). `A/standards/STDO_REFERENCE_FRAME_BASELINE.md` 1515-1521 "Every completed… activation"; "Interruption or actor loss remains unreturned work"; mapping replaced by the cause-qualified Work result refinement.
- B: changed (1). `B/standards/EXECUTIVE_BASELINE.md` 1175-1181 each value maps to one core value under ACTIVATION §3, where `incomplete` is `falsified` (`B/standards/ACTIVATION.md` 1020) against rc.2's `indeterminate -> incomplete`.
- Same change? partly (cause-qualified, many-to-one mapping in both).
- Only in A: interruption rule. Only in B: WorkerResult notation retained (1167-1173).
- Common input: refinement mapping required (`common/README.md` 163); the value chosen for `incomplete` is a tenant choice.
- Records: A accurate. B accurate with disclosed carve-out ("save the mapping sentence split to the child row below", `rows/42.md` 49).
- Note: A removes the notation block from this section.

**Row 46 — `STDO_REFERENCE_FRAME_BASELINE.md#canonical-compression`**
- Claim: three overlapping frames mapped onto existing owners; the engagement flow; twelve specialist and four testing families with their topology; adoption by the existing project authority; a local axioms file is no new owner.
- A: unchanged. `A/standards/STDO_REFERENCE_FRAME_BASELINE.md` 11-23, 41-85 retain the flow, frames, families, topology and adoption clause; 25-39 add configuration premises and consumption; "selects" for "derives" (49, 59) is descriptive.
- B: changed (5). `B/standards/EXECUTIVE_BASELINE.md` 106-107 "Adopting the profile is the Product authority's act (PRODUCT_DEFINITION §7)" for rc.2's "existing project authority that owns the affected decision"; testing topology relocated to `B/standards/ASSURANCE.md` 380-398 (relocation).
- Only in A: configuration/consumption statements. Only in B: "not the method's default" (104-105).
- Common input: not material.
- Records: A inaccurate: `superseded` over retained determinations. B accurate with disclosed carve-out (`rows/46.md` 96).
- Note: A's record's stated change ("selected optional configuration") was already rc.2's text ("optional", "not mandatory actors").

**Row 47 — `STDO_REFERENCE_FRAME_BASELINE.md#closure`**
- Claim: evaluate only applicable obligations; every applicable obligation satisfied with valid evidence and J/O; indeterminate/review event do not satisfy; the 24 closure conditions; project-defined configuration need not claim conformance.
- A: changed (1). `A/standards/STDO_REFERENCE_FRAME_BASELINE.md` 2085-2116 replaces the 24 conditions with an obligation-group table resolved through core conjunction; A's record states conditions 4 and 7 change (cause-qualified mapping; bounded delivery view) and the rest are carried at the cited owners.
- B: changed (1). `B/standards/EXECUTIVE_BASELINE.md` 1812-1815 condition 4 "one work-result value selected by its cause, maps to exactly one core value" for rc.2's "maps exclusively from one closed Reference Frame Method result"; 1823-1827 condition 7 keeps "complete Product view"; 1792-1803 preamble and 1876-1878 closing sentence verbatim.
- Same change? partly (condition 4).
- Only in A: condition 7 change; table form. Only in B: the 24-item list in place.
- Common input: condition 4's mapping follows `common/README.md` 163; permitted.
- Records: A accurate. B accurate with disclosed carve-out (`rows/47.md` 147).
- Note: A's "complete 24-condition carrying matrix" is not in the packet locus; I did not verify it.

**Row 55 — `STDO_REFERENCE_FRAME_BASELINE.md#executive-attention-evaluation-and-action`**
- Claim: three duties; Executive holds no complete workspace or operation authority; no mutation while Executive; the attention cycle incl. "invalidate affected results when the subject or basis changes" and retaining the frontier and closed-result ledger; severity vs decisions; explicit D relation.
- A: changed (1, 3). `A/standards/STDO_REFERENCE_FRAME_BASELINE.md` 356 "reassess affected result reliance under the shared currentness law"; 361 third stop condition; 376-382 "acquires the portion of the durable frontier and closed results material to its current decision".
- B: unchanged. `B/standards/EXECUTIVE_BASELINE.md` 555-566, 576-589, 594-610 (605 "invalidate affected results"), 615-617, 619-629.
- Only in A: reassessment-not-invalidation; bounded frontier view; stop clause. Only in B: none.
- Common input: evidence reuse by applicability (`common/ASSURANCE.md` 115) supports A's change; B's automatic invalidation is permitted but stricter.
- Records: A accurate. B accurate.
- Note: B states the no-mutation rule as its own owned prohibition (584-589).

**Row 56 — `STDO_REFERENCE_FRAME_BASELINE.md#profile-qualification`**
- Claim: qualification applies Frame Qualification and UP-022; mechanical checks protect shape only; the 26 trial obligations; claim limited to what was evaluated.
- A: changed (1). `A/standards/STDO_REFERENCE_FRAME_BASELINE.md` 1850-1854 item 5 many-to-one by cause; 1863-1865 item 9 reassessment under change impact; 1905-1906 item 25 "sufficient bounded delivery view".
- B: changed (1). `B/standards/EXECUTIVE_BASELINE.md` 1570-1572 item 5 "selected by its cause, maps to exactly one core value"; 1581 item 9 and 1624-1627 item 25 verbatim.
- Same change? partly (item 5).
- Only in A: items 9 and 25. Only in B: none.
- Common input: permitted.
- Records: A accurate. B accurate with disclosed carve-out (`rows/56.md` 117).
- Note: items 1-4, 6-8, 10-24, 26 verbatim in both.

**Row 57 — `STDO_REFERENCE_FRAME_BASELINE.md#status-and-authority-boundary`**
- Claim: optional profile with no independent ownership; three ownership layers; owner table; every requirement is an application of a cited owner or an adoption condition; no second amendment path; availability is not adoption.
- A: unchanged. `A/standards/STDO_REFERENCE_FRAME_BASELINE.md` 96-120 re-routes result/conjunction to Foundations (107-108) and independence to Independent assessment plus UP-007 (111), a relocation; 141-154 verbatim rules; 130-139 family table additive.
- B: unchanged. `B/standards/EXECUTIVE_BASELINE.md` 116-121, 125-139 re-routed table incl. "core result algebra and conjunction of results | FOUNDATIONS §4" (126); 141-151 verbatim rules.
- Only in A: "'Derived'… not a uniquely forced role inventory" (91-93). Only in B: new rows for configuration (127) and proxy grant (138).
- Common input: moving a determination to a shared owner is conservation (`common/README.md` 67).
- Records: A inaccurate (`superseded` over relocation and additive argument). B accurate.
- Note: both tables name the same successor owners for the result algebra.

**Row 59 — `STDO_REFERENCE_FRAME_BASELINE.md#work-result`**
- Claim: a work result exists only after activation; activation_refusal is not a work result; the four variants are carriers disjoint by their RF result (`incomplete` accompanies `indeterminate`); total and exclusive mapping; consumers choose representation; UP-020 owns the execution relation; C/J/O reuse.
- A: changed (1). `A/standards/STDO_REFERENCE_FRAME_BASELINE.md` 565-582 cause-qualified table (`incomplete, undecided`→indeterminate; `incomplete, postcondition_defeated`→falsified), "The bounds include a delivery time only where the grant requires it" (569-570), performance and effect state in every result.
- B: changed (1). `B/standards/EXECUTIVE_BASELINE.md` 483-512: values are ACTIVATION §3's construction availability, where `incomplete` is `falsified` (`B/standards/ACTIVATION.md` 1020, 1033-1034) and `re_entry_requested` is split by cause; 514-525 verbatim remainder.
- Same change? partly (cause-qualification), different for `incomplete`.
- Only in A: delivery-bound predicate; `unconfirmed` performance. Only in B: `incomplete` always falsified with evaluations keeping their own results (1033-1041).
- Common input: availability never maps to fitness (`common/README.md` 170) — both comply; mapping required (163).
- Records: A accurate. B accurate with disclosed carve-out (`rows/59.md` 63).
- Note: the two lines disagree on the core value of `incomplete`; the common spec does not decide it.

**Row 60 — `TICKET_METHOD.md#execution-contract-admission`**
- Claim: treat the carrier as an admission candidate; four minimum states; an admitted contract should be logged in runtime/event truth, available to prompt assembly and closure checking; no silent self-certification; admission does not admit the growth basis.
- A: changed (1, 4). `A/standards/TICKET_METHOD.md` 821-823 "recorded in the selected work carrier, including an event log when that is its declared realisation" and "frame or prompt assembly"; 826-845 core mapping; 850-855 override decision result.
- B: unchanged. `B/standards/TICKETS.md` 688-695 (logging and availability verbatim), states and self-certification at `B/standards/ACTIVATION.md` 412-422, basis admission at `B/standards/SPEC_METHOD.md` 734-742.
- Only in A: carrier latitude (A's record ties it to pending I3-R2-R025); admission verdict mapping. Only in B: none.
- Common input: build-tenant binding permits human or mixed carriers (`common/README.md` 125: "Code, an event stream… is required only when… obligations… require it"), supporting A's latitude; B's retention permitted.
- Records: A accurate. B accurate.
- Note: ACTIVATION 434-438 adds a durable-surface admission condition that is B's own law, not a change to this claim.

**Row 62 — `TICKET_METHOD.md#recorded-judgment-and-owner-ruling-continuity`**
- Claim: residual judgments recorded once with the listed coordinates; later runs check applicability; changed evidence/basis/revising observation causes reassessment preserving originals; independence not satisfied by the author's J; owner rulings recorded in original wording; no registry; repricing gives retained/superseded/deferred/withdrawn dispositions.
- A: changed (1). `A/standards/TICKET_METHOD.md` 970-981 the four dispositions become decision results with a predicate and satisfied/falsified/indeterminate mapping; 939-944 reuse via Contract application's Currentness; the role/conversation non-invalidator moves to `A/standards/FOUNDATIONS.md` 885-886.
- B: unchanged. `B/standards/TICKETS.md` 1109-1157 verbatim content with reuse routed to ACTIVATION §7 (1119-1131); 1159-1176 declares the dispositions "recorded states… not results and map to no core value" (additive).
- Only in A: decision-result mapping. Only in B: states-not-results declaration.
- Common input: `common/README.md` 174 "Calling an output a state does not exempt a determination that decides compliance, admission, closure or disposition" — possible conflict for B's declaration; A's realisation follows 174.
- Records: A accurate. B accurate on meaning; the README 174 question is a conformance matter.
- Note: B's "A general instruction to continue does not accept…" and A's are both carried.

**Row 64 — `TRAVERSAL_OCCURRENCE_PROFILE.md#candidate-judgment-event-and-relation-separation`**
- Claim: the admission relation; only three admitted decisions admit the cut; distinct identities; judgments are inherited records with the listed fields; missing/non-admitted/wrong-subject/cross-basis judgment refuses the cut; identity and frontier equalities; exactly three edges; re-admission and `refuse_duplicate`.
- A: changed (1). `A/standards/TRAVERSAL_OCCURRENCE_PROFILE.md` 956-961 fields extended (predicate, verdict, performance, effects, residuals) and "leaves the semantic cut unadmitted; these conditions do not all establish the same verdict" for rc.2's "refuses"; 925-931, 970-979 conjunction before mapping `j_a`.
- B: unchanged. `B/standards/TRAVERSAL_OCCURRENCE.md` 1138-1232 verbatim (1175-1179 "refuses the semantic cut").
- Only in A: distinct verdicts for missing vs failed support. Only in B: none.
- Common input: not-performed distinct from falsified (`common/README.md` 167) supports A; B's "refuses" for a missing judgment is a profile policy, permitted.
- Records: A accurate. B accurate.
- Note: A's change here underlies row 68.

**Row 65 — `TRAVERSAL_OCCURRENCE_PROFILE.md#closed-constraint-judgment-residual-and-stop-kinds`**
- Claim: the four kind populations; every constraint predicate returns one of four values; satisfied/invalid_basis mappings; the judgment, constraint and residual tables; functor kinds unchanged.
- A: changed (1, 4). `A/standards/TRAVERSAL_OCCURRENCE_PROFILE.md` 754-759 "All five core verdicts are available" (rc.2: four); 774-775 claim_admission and semantic_cut_admission rows altered (staleness falsifies; conjoin judgments); 828-834 constraint rows altered; 853, 856 residual re-entry rows altered.
- B: unchanged. `B/standards/TRAVERSAL_OCCURRENCE.md` 777-778 four values retained; 795-840 three tables verbatim; 842-1079 adds mappings to the core (hold→indeterminate, refusal(constraint)→falsified, refusal(basis)→invalid_basis, partial split by cause read from evidence, 983-1000) without altering the tables.
- Only in A: out_of_frame availability; staleness-falsifies rule; prerequisite-check diagnosis (836-844). Only in B: structural-refusal classification (1025-1066); cause-split mapping.
- Common input: core mapping required (`common/README.md` 162-163); both permitted.
- Records: A accurate. B accurate.
- Note: B's note is very long; its substance is a mapping layer over unchanged tables.

**Row 66 — `TRAVERSAL_OCCURRENCE_PROFILE.md#finite-reference-domain-table`**
- Claim: the complete `RefDomain` specialisation: basis codes, every row, the external-resolution expansion, `ResolutionRefDomain`, closed non-reference content, refusal of model validation on defects.
- A: changed (1). `A/standards/TRAVERSAL_OCCURRENCE_PROFILE.md` 360-361 new rows `J:*.predicate`, `J:*.residuals`; 365-376 new value-contract table for `verdict`, `decision`, `performance`, `effects` closing "all nineteen Judgment fields" (366).
- B: unchanged. `B/standards/TRAVERSAL_OCCURRENCE.md` 407-412 J rows identical to rc.2; 511-519 closing sentences verbatim.
- Only in A: extended signature. Only in B: none.
- Common input: follows A's R003 realisation; permitted.
- Records: A accurate (its note states existing records cannot satisfy the extended signature). B accurate.
- Note: I compared the J rows and closing text, not every table row.

**Row 67 — `TRAVERSAL_OCCURRENCE_PROFILE.md#mutable-subject-effect-relation`**
- Claim: the observe/judge/dispatch relation; coordinates distinct; no operation without a matching grant; exact bindings; containment only by declared relation; the closed disposition law (`refused_effect` with "evidence that no authorized mutation began"); `invokes_effect` iff dispatched; readiness judged immediately before dispatch.
- A: changed (1). `A/standards/TRAVERSAL_OCCURRENCE_PROFILE.md` 1151-1152 `refused_effect` needs "evidence that no mutation began" (authorised or not); 1159-1184 evidence conditions for `not_requested`/`not_started`, unknown remainder, "An unauthorized mutation is still an actual effect".
- B: unchanged. `B/standards/TRAVERSAL_OCCURRENCE.md` 1339-1355 law verbatim incl. "no authorised mutation began" (1349); 1357-1374 adds an additive mapping to ACTIVATION §3 Effects.
- Only in A: unintended-effect observation duty. Only in B: `no_effect`→`not_effected`/falsified for an occurrence that intends an effect (1374).
- Common input: unknown effect never maps to no effect (`common/README.md` 168) — A's rule enforces it; B's mapping keeps `refused_effect` on authorised mutation only, permitted.
- Records: A accurate. B accurate.
- Note: A's `no_effect` clause (1143-1145) adds the stopped-before-dispatch case.

**Row 68 — `TRAVERSAL_OCCURRENCE_PROFILE.md#op-002-atomic-semantic-admission`**
- Claim: one admitted cut contains the seven members; frontier identity; successor = source + event; "Missing, conflicting, or inconsistent members refuse the cut"; semantic atomicity, no storage mechanism.
- A: changed (1). `A/standards/TRAVERSAL_OCCURRENCE_PROFILE.md` 1043-1045 "admits that whole unit or none… Missing or inconsistent members and missing judgment support keep their distinct core results" — a missing member no longer refuses; "conflicting" dropped here.
- B: unchanged. `B/standards/TRAVERSAL_OCCURRENCE.md` 1236-1244 verbatim.
- Only in A: distinct results at the gate. Only in B: none.
- Common input: as row 64.
- Records: A accurate. B accurate.
- Note: A's record argues conflict still refuses at the referenced owner (1026-1032 "Missing, extra, reversed, duplicate… refuse the cut").

**Row 69 — `UX_METHOD.md#5-state-transition-law`**
- Claim: typed messages through a pure reducer; five declarations; six Cmd fields incl. success and failure Msg; pure reducer; view-local ephemera at `may`; product state through the reducer; unmount test.
- A: changed (1). `A/standards/UX_METHOD.md` 207-211 "the typed outcome `Msg` family… including every observed or unresolved effect case" and "the reason and observation carried by each case" replace the success/failure pair.
- B: unchanged. `B/standards/UX.md` 347-354 success Msg, failure Msg retained; 336-368 remainder verbatim.
- Only in A: outcome family. Only in B: none.
- Common input: unknown effects distinct (`common/README.md` 168) motivates A; permitted.
- Records: A accurate (its record calls it a proposed replacement). B accurate.
- Note: all other parts carried in both.

**Row 70 — `UX_METHOD.md#6-effect-membrane-rule`**
- Claim: effects isolated to a membrane; allowed inside/forbidden outside lists; one job; logic in the reducer; named handlers; violation and repair.
- A: changed (1). `A/standards/UX_METHOD.md` 241-253 typed effect-state Msg cases, failed response may mean `unknown`, recovery command observes owning state before a dependent repeat.
- B: unchanged. `B/standards/UX.md` 372-390 verbatim, "refines DESIGN_MODULE §10 Effect edge".
- Only in A: effect-state return and recovery duties. Only in B: none.
- Common input: as row 69.
- Records: A accurate. B accurate.
- Note: none.

**Row 71 — `UX_METHOD.md#8a-msg-replay-proof-requirement`**
- Claim: at least one executable replay proof per interaction family before closure; six contents incl. success/failure Msg values; four failure dependencies; no-effect proof at `may`.
- A: changed (1). `A/standards/UX_METHOD.md` 309-310 "typed outcome `Msg` values… including unresolved effects"; 324-339 result record, `not_performed`, conjunction.
- B: unchanged. `B/standards/UX.md` 457-486 verbatim (472 success and failure Msg); `B/standards/UX.md` 768, 777-778 add an additive `replay_passes`/`replay_fails` mapping.
- Only in A: replay-fidelity ≠ effect completion statement. Only in B: §15 refinement table.
- Common input: core mapping required (`common/README.md` 162); both permitted.
- Records: A accurate. B accurate.
- Note: B's §15 (749-820) is new law beside the conserved claim.

**Row 72 — `WORLD_MODEL_METHOD.md#4-assure`**
- Claim: qualify traced observations into claims; assurance should make five things explicit.
- A: changed (1). `A/standards/WORLD_MODEL_METHOD.md` 808-813 mandatory binding of Assertions and observations, predictive adequacy distinguished from outcome; 823-833 result record with mapping; five items retained at `should` (815-821).
- B: unchanged. `B/standards/WORLD_MODEL.md` 669-673 five items verbatim.
- Only in A: assertion binding and mapping. Only in B: none.
- Common input: assertion/observation contracts required at evaluation (`common/ASSURANCE.md` 25-56; `common/README.md` 118); A binds them here, permitted.
- Records: A accurate (its record says "Adds a mandatory… binding"). B accurate.
- Note: none.

**Row 74 — `AXIOMATIC_CALCULUS.md#fundamental-laws`**
- Claim: heading only (`rows/74.md` 10).
- A: unchanged (heading retained; 390-411 adds a family-argument table, new text). B: unchanged (heading retained, `B/standards/AXIOMATIC_CALCULUS.md` 471-476 add three lines).
- Same change? n/a. Only in A: argument table. Only in B: scope sentence.
- Common input: not material.
- Records: A `conserved` defensible (heading kept, nothing to lose). B `not applicable` accurate: a heading with no text has no effect on the successor.
- Note: the INDEX tags this empty row with all three causes; nothing in it can be changed by them.

**Row 75 — `IDENTITY_METHOD.md#authority-split`** — Claim: heading only. A: unchanged (`A/standards/IDENTITY_METHOD.md` 256). B: unchanged (`B/standards/IDENTITY.md` 207). Only in A/B: none. Common: not material. Records: A defensible; B accurate (no claim). Note: children disposed individually per both records.

**Row 76 — `IDENTITY_METHOD.md#core-law`** — Claim: heading only. A: unchanged (124). B: unchanged (101). Records: A defensible; B accurate. Note: as row 75.

**Row 77 — `IDENTITY_METHOD.md#default-formats-and-overrides`** — Claim: heading only. A: unchanged (331). B: unchanged (263). Records: A defensible; B accurate.

**Row 78 — `IDENTITY_METHOD.md#examples`** — Claim: heading only. A: unchanged (478). B: unchanged (373). Records: A defensible; B accurate.

**Row 79 — `REFERENCE_FRAME_METHOD.md#definitions`** — Claim: heading only. A: unchanged (`A/standards/REFERENCE_FRAME_METHOD.md` 119). B: absent (no locus; definitions moved to `B/standards/FOUNDATIONS.md` 101-125 per row 24). Only in A/B: none. Common: not material. Records: A defensible; B accurate (empty claim). Note: the empty "Successor loci" field is expected for a not-applicable row.

**Row 80 — `REFERENCE_FRAME_METHOD.md#discovery-and-revision`** — Claim: heading only. A: unchanged (1078). B: absent. Records: A defensible; B accurate.

**Row 81 — `REFERENCE_FRAME_METHOD.md#engagement`** — Claim: heading only. A: unchanged (684). B: absent. Records: A defensible; B accurate.

**Row 82 — `REFERENCE_FRAME_METHOD.md#reference-frame-laws`** — Claim: heading only. A: unchanged (heading 351; 353-371 new argument table). B: absent. Only in A: the table. Records: A defensible; B accurate. Note: A's note "result ownership remains the explicit pending core replacement" describes row 27, not this empty row.

**Row 83 — `REFERENCE_FRAME_METHOD.md#workspace-coverage`** — Claim: heading only. A: unchanged (868; 870-885 new argument). B: absent. Records: A defensible; B accurate.

**Row 84 — `SPEC_METHOD.md#evidence-rules`**
- Claim: one non-normative sentence, "The following rules govern how constitutional claims are proved in practice."
- A: unchanged (`A/standards/SPEC_METHOD.md` 2478 verbatim; 2480-2491 argument added). B: unchanged in substance (`B/standards/SPEC_METHOD.md` 1711-1718 restates the sentence as a pointer to tier-1 owners).
- Only in A: argument. Only in B: closure-evidence sentence 1720-1727 (B marks it as from a compression).
- Common input: not material.
- Records: A accurate. B `not applicable` accurate: the sentence carries no determination.
- Note: none.

**Row 85 — `STDO_REFERENCE_FRAME_BASELINE.md#product-owned-adoption-or-project-defined-configuration`** — Claim: heading only. A: unchanged (1724). B: absent (adoption law at `B/standards/EXECUTIVE_BASELINE.md` 103-110 and §16, per B). Records: A defensible; B accurate.

**Row 86 — `STDO_REFERENCE_FRAME_BASELINE.md#profile-terms`** — Claim: heading only. A: unchanged (228). B: absent. Records: A defensible; B accurate.

**Row 87 — `TICKET_METHOD.md#core-model`** — Claim: heading only. A: unchanged (35; 37-45 new argument). B: unchanged (`B/standards/TICKETS.md` 30 "## 1. Work carriers"). Records: A defensible; B accurate.

**Row 88 — `TICKET_METHOD.md#sprint-rules`** — Claim: heading only. A: unchanged (220; 222-228 new argument incl. "Sprint status is recorded lifecycle state"). B: unchanged (184). Records: A defensible; B accurate.

**Row 89 — `TICKET_METHOD.md#ticket-rules`** — Claim: heading only. A: unchanged (433). B: unchanged (334). Records: A defensible; B accurate.

**Row 90 — `WORLD_MODEL_METHOD.md#core-claims`** — Claim: heading only. A: unchanged (487). B: unchanged (535). Records: A defensible; B accurate.

**Row 91 — `WORLD_MODEL_METHOD.md#method-units`** — Claim: heading only. A: unchanged (624). B: unchanged (597). Records: A defensible; B accurate.

**Row 92 — `REFERENCE_FRAME_METHOD.md#worked-binding-product-chain-drift-evaluation`**
- Claim: a self-declared "non-normative example" of a complete prose binding; defines no profile; consumers replace URIs.
- A: changed in illustration only, no obligation. `A/standards/REFERENCE_FRAME_METHOD.md` 1280-1291 replaces "invalid_basis on stale or substituted basis" with "invalid_basis when the governing basis cannot interpret the bound predicate" and `indeterminate` for stale supporting evidence; "invalidation" becomes "affected reliance".
- B: absent. No locus; B's reason: the binding shape is conserved at `B/standards/REFERENCE_FRAME.md` 992-1035 and the example's subject is tier-2 matter.
- Only in A: the example. Only in B: none.
- Common input: not material.
- Records: A `superseded` accurate as to the text (A ties it to the pending RF-005 replacement) though the example carries no determination; B `not applicable` accurate and bounded.
- Note: the normative change A illustrates is RF-005's (row 26, other reader).

**Row 93 — `DESIGN_MODULE_METHOD.md#15-adoption-guidance`**
- Claim: "Projects may adopt this method by" four means; consistent application across six boundaries; `should` for evaluators; Ontology/IACS/derivation/unit-lane obligations before completion; partial adoption rules.
- A: unchanged. `A/standards/DESIGN_MODULE_METHOD.md` 2436-2483 verbatim.
- B: changed (5). `B/standards/DESIGN_MODULE.md` 2405-2408 "only Product authority adopts it. This profile adds no adopter"; the four means become how "The adopting Product's authority may record its adoption" (2408-2413); 2416-2444 remainder carried in indicative force.
- Only in A: none. Only in B: adopter restriction via `B/standards/PRODUCT_DEFINITION.md` 689-693.
- Common input: not material; who adopts a profile is a tenant policy.
- Records: A accurate. B accurate (`superseded`, proposed and pending).
- Note: none.

**Row 94 — `TRAVERSAL_OCCURRENCE_PROFILE.md#closed-profile-signature-fourteen-members`**
- Claim (sentence-level): "For the calculus edition bound by this profile publication candidate, that population has fourteen members", with missing/extra refs refusing.
- A: unchanged. `A/standards/TRAVERSAL_OCCURRENCE_PROFILE.md` 1360-1362 sentence retained; A's derivation list (`A/standards/AXIOMATIC_CALCULUS.md` 73-101) still has fourteen clauses.
- B: changed (1, 4). The sentence is gone from `B/standards/TRAVERSAL_OCCURRENCE.md` (only its disposition entry at 1709 mentions it); `B/standards/AXIOMATIC_CALCULUS.md` 1206-1210 "retained without a hard-coded member count. The set is recomputed when the derivation account changes."
- Only in A: the count check. Only in B: recomputation rule.
- Common input: identity and packaging decisions are open owner decisions (`common/PRODUCT.md` 435); not material to conservation.
- Records: A accurate. B accurate (`superseded`, proposed and pending).
- Note: the row's anchor is synthetic, as both the row file and B's table state.

**Row 95 — `UX_METHOD.md#13-adoption-guidance`**
- Claim: "A project adopts `UX_METHOD.md` by" nine steps; per-project adoption at `may` with recorded scope.
- A: unchanged. `A/standards/UX_METHOD.md` 422-438 verbatim.
- B: changed (5). `B/standards/UX.md` 559-560 "Product authority adopts this profile for a project… and the adoption is recorded by" the nine steps; 577-579 per-project `may` retained; step 3 pointed to DESIGN_MODULE §6-§7.
- Only in A: none. Only in B: adopter restriction.
- Common input: not material.
- Records: A accurate. B accurate (`superseded`, proposed).
- Note: none.

**Row 96 — `UX_METHOD.md#1a-constitutional-authority-rule`**
- Claim: when a product, ticket, design module or review adopts the method, it is the sole UX authority; ADRs choose the stack but may not weaken the model; seven evidence-only kinds; fail closed with three exits.
- A: unchanged. `A/standards/UX_METHOD.md` 67-79 verbatim.
- B: changed (5). `B/standards/UX.md` 74-78 "When Product authority adopts this profile… recording the adoption in a product definition, ticket, design module or review"; 82-93 the three exits mapped to ACTIVATION §3 ambiguity outcomes (additive).
- Only in A: none. Only in B: adopter restriction; outcome mapping; "§15 states the result".
- Common input: not material.
- Records: A accurate. B accurate (`superseded`, proposed).
- Note: the UX profile's conflicting compliance tests are an open owner decision (`common/PRODUCT.md` 433); B's §15 (774) applies the stricter one pending that ruling.

**Row 97 — `WRITING_GUIDE.md#current-surface-writing`**
- Claim: active specification "should" be present tense; delete/supersede/move dead law; prefer six terms; version labels only for release facts, selector bindings or history.
- A: unchanged. `A/standards/WRITING_GUIDE.md` 125-146 verbatim; 127-128 adds "act within the owning authority and any required recorded UP-015 disposition", a cross-reference to existing law.
- B: changed (2). `B/standards/WRITING_GUIDE.md` 114-120 defers the rule, "with its force", to `B/standards/SPEC_METHOD.md` 435-444 (indicative mandatory) and keeps only the preferred terms (120-122).
- Only in A: UP-015 cross-reference. Only in B: none beyond the force transfer.
- Common input: README 34 "a preference must remain a preference"; but rc.2 SPEC_METHOD already bound the same surfaces at `shall` (`rc2/standards/SPEC_METHOD.md` 2701, 2703), so B contracts a duplicate preference into its mandatory owner (`common/README.md` 17, 63), permitted; the method-level obligation is unchanged.
- Records: A accurate. B accurate (`superseded`, proposed).
- Note: B's claim that the predecessor's SPEC_METHOD was already mandatory is verified.

## Tallies

Scope: 64 rows (40 tagged rows 01–72 and rows 74–97).

- A: unchanged 28 (06, 23, 24, 46, 57, 74–91, 93, 94, 95, 96, 97); changed 36 (01, 02, 03, 04, 05, 09, 11, 12, 17, 19, 20, 21, 22, 25, 27, 28, 29, 36, 40, 42, 47, 55, 56, 59, 60, 62, 64, 65, 66, 67, 68, 69, 70, 71, 72, 92); absent 0; cannot decide 0.
- B: unchanged 37 (02, 03, 04, 05, 06, 09, 17, 21, 22, 23, 24, 28, 29, 55, 57, 60, 62, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 75, 76, 77, 78, 84, 87, 88, 89, 90, 91); changed 19 (01, 11, 12, 19, 20, 25, 27, 36, 40, 42, 46, 47, 56, 59, 93, 94, 95, 96, 97); absent 8 (79, 80, 81, 82, 83, 85, 86, 92); cannot decide 0.
- Both changed: 14 rows; same change "partly" in all 14, "yes" in none, "no" in none.
- "Only in A" non-empty: 41 rows (01, 02, 03, 04, 05, 06, 09, 11, 12, 17, 19, 20, 21, 22, 23, 25, 27, 28, 29, 36, 40, 42, 46, 47, 55, 56, 57, 59, 60, 62, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 82, 83, 84, 87, 88, 92, 94, 97 counted as 48 including heading-row argument additions; 41 excluding rows 74, 82, 83, 84, 87, 88 and 97's cross-reference).
- "Only in B" non-empty: 24 rows (01, 06, 11, 12, 19, 20, 23, 25, 27, 28, 36, 40, 42, 46, 47, 57, 59, 62, 65, 67, 71, 74, 84, 93, 94, 95, 96 counted as 27 including rows 06, 74, 84 pointers; 24 excluding them).
- Inaccurate records, A: 5 (`superseded` over unchanged meaning at 06, 23, 24, 46, 57).
- Inaccurate records, B: 8 (`conserved` over a meaning change at 01, 11, 12, 19, 20, 25, 27, 40; 11, 12, 19, 25, 27 and 40 are narrow).
- B records accurate only with a disclosed carve-out to a child row outside the packet: 5 (36, 42, 46, 47, 56) plus 59.
- Heading-only rows 74–91 (17 rows) and row 84: neither line's record counted as inaccurate; B's `not applicable` is the more precise label.

## Limits

- Tool calls used: 107 of 220.
- Rows not read: none. Rows read by sampling rather than in full: 12 (A ODD 860-1465 and B ODD 785-1413 read at 860-905, 970-990, 1025-1045, 1120-1160, 1190-1222 and 785-830, 1015-1050, 1115-1210 plus keyword greps); 65 (B TO 722-1084 read at 722-870 and 975-1084); 66 (only the J rows and closing text compared in both lines); 47 (A's "24-condition carrying matrix" named in its record is not inside the packet locus and was not verified); 20 (B EVALUATION read in full, A RF in full).
- Departures: two Bash outputs (`common/*` and `rows/12.md`) exceeded the inline limit and were persisted to a file outside the packet; I did not open those copies and re-read the packet files with Read instead. No file was written or modified; no git, network or non-packet directory was used.
- Malformed or odd in the packet: CAUSES.md says R003 is tagged at AC-014 (row 02), yet INDEX row 02 carries only R012 and R015; likewise row 27 (RF-012) lacks R012 and row 25 (Result Conjunction) lacks R015 — each cause's home row omits its own tag. Rows 74, 82, 83 (heading-only) carry all three cause tags though they have no claim text. Rows 79–83, 85, 86 and 92 have empty "Successor loci" for B, consistent with `not applicable`. B's notes on rows 36, 42, 46, 47, 56, 59 refer to "the child row below"; no such child rows are in this packet, so the dispositions of the carved-out clauses could not be checked. Row 94 is a synthetic sentence-level anchor, as the row file states. The B note on row 65 (`rows/65.md` 140) is a single sentence of roughly 500 words.
- Judgment conventions applied throughout: relocation of a determination to another owner (including the five result values moving to Foundations) was treated as preserving meaning under the test's "moving a rule" clause and `common/README.md` 67; element 5 was applied only where a claim's own text names who holds an authority (rows 05, 36, 46, 93, 95, 96). Descriptive changes of standing ("derived" to "selected"/"specialization") were not counted as meaning changes. Additive core mappings that leave the predecessor's conditions and values intact were not counted as changes; mappings that fix a determination the predecessor left to a declared rule, or that alter a value's standing (`conflict`, `incomplete`, a missing result), were.