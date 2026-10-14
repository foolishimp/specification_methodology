# CR2: cross-family review of the frozen Codex v3 candidate (single ownership and result algebra)

Status: commentary, not specification. A Claude reviewer assessed a Codex-authored subject. It repaired nothing. The reviewer did not read the Claude candidate's members.

Basis:
- Subject: `9bc8962` at `subject/.../codex/successor/standards/`. 18 members, 6 frames and the compressions.
- Evidence: `3ad1fca`.
- Common requirements: R §Single Ownership Requirement and §Single Result Algebra Requirement; C, the conformance rows on two loci, member result values and frame results.
- Installed predecessor rc.2: RF-012 and AC-007.
- Oracle: EXPECTATIONS items 4 and 5.

Path abbreviations: `F` = FOUNDATIONS.md, `TL` = TRANSFORMATION_LIBRARY.md, `RF` = REFERENCE_FRAME_METHOD.md, `AC` = AXIOMATIC_CALCULUS.md, `B` = STDO_REFERENCE_FRAME_BASELINE.md, `TOP` = TRAVERSAL_OCCURRENCE_PROFILE.md, `WM` = WORLD_MODEL_METHOD.md. The others are spelled out. Line numbers refer to the subject.

## Method

- **Owner-section quotes.** The FOUNDATIONS, TL, RF, AC, IDENTITY, guides, README, frames and compressions loci were read directly.
- **Large members (SPEC, DESIGN, B, ODD, UX, TICKET, RELEASE, WM, TOP).** These were read in full by six bounded read-only sub-evaluations. Each one used the same inclusion rule and row schema. The parent re-read every locus cited in the findings table below, and spot-checked a further 24 inventory loci.
- **Inherited or introduced.** This was decided with `grep -F` of a distinctive phrase against the rc.2 member. rc.2 has no FOUNDATIONS or TL. When the deciding text of a pair is byte-present in rc.2 and the owner is new, the pair is labelled "inherited text beside introduced owner".
- **Frames.** Checked by a script kept outside the subject (`scratchpad/cr2tools/framecheck.py`, run with `python3 -I`). For each `Source:` line it:
  - recomputes the owner's SHA-256;
  - extracts the owner section by heading (code fences excluded);
  - relocates relative links as each frame preface declares;
  - byte-compares the result with the frame's copy.
- **Inclusion rule for value sets.** A set is counted when it is the outcome of one of these: a constraint check, a judgement, a frame evaluation, a stop, a work step, an effect, or a decision or disposition. Decisions are included under oracle A3. Lifecycle statuses, kinds, change classes, input bases and treatment menus are excluded, with a reason (see "Excluded sets").
- **Status classes:**

| Class | Meaning |
|---|---|
| M | A per-value or per-(value, cause) map to exactly one core value, given in the member. |
| I | An open, instance-declared set. The member obliges each instance to bind an exactly-one map before use. |
| R | Rule-only. Closed values are declared as refinements by a member referral, a preamble referral or TL:205-207, but no per-value map is given. Only the default rule at F:383-397 covers them. That rule cannot raise standing, but it also cannot assign a value its core target. |
| U | No referral covers the set. |
| D | Competing or defective map. |

Severity scale:

| Severity | Meaning |
|---|---|
| High | A requirement item fails across members, or a stated qualification claim is materially contradicted by the text. |
| Medium | A requirement item fails at a specific locus in a way a consumer would act on: a competing owner with divergent content, an unmapped closed set in a deciding member, or packaging that misstates standing. |
| Low | Wording drift, consistent restatement without a referral at the locus, or an intra-member duplicate with consistent content. |

## Findings

| ID | Sev | Claim | Evidence (`file:line`, short quote) | Inh./Intr. | Smallest repair |
|---|---|---|---|---|---|
| CR2-01 | High | Single Result Algebra items 1–2 are not met. Of 79 in-scope refinement sets, 32 are mapped (M+I), 28 are rule-only, 17 are unmapped and 2 are competing or defective; 47 lack a per-value map. The R/U boundary is a reviewer judgement; the requirement-relevant split is 32 against 47. Unmapped sets sit in deciding members (SPEC, TICKET, RELEASE, RF, B, DESIGN). The core's own rule asks each refinement for "a total, reason-sensitive map into this record". | F:384-386 "supplies a total, reason-sensitive map into this record". R item 2: "Every refined value maps to exactly one core value". Examples: RF:880-888 coverage statuses `covered` … `excluded_by_authority`; SPEC:1157-1158 "resolved, carried forward, escalated, or blocked"; DESIGN:1401-1406 `preserves`/`changes`/`duplicates`/`violates`; B:1128 "The localization result represents exactly one of:"; RELEASE:290 "Advancement is refused when…". | Inherited sets, not unified. | At each owner, add a (value, cause) → core table. Or declare the set a non-result classification, with its reason. See the inventory. |
| CR2-02 | Medium | Conjunction is not defined once. Two inherited loci keep their own combination outcome. First, RF's qualification oracle for `conjoin` expects a non-core outcome set and routes basis mismatch to `refusal`. Second, UP-021 says mixed-basis owner judgments "cannot combine" and are "refused without effect". The core routes an invalid required basis, or an uninterpretable composite basis, to `invalid_basis`. RF's own Result Conjunction section makes conflict an annotation. DESIGN reconciles UP-021 only at the consumer. | RF:1243 "result conflict, basis mismatch, mandatory indeterminacy, and declared veto return conflict, indeterminate, or refusal". SPEC:1813 "independently valid mixed-basis judgments cannot combine". SPEC:1852 "cannot combine and are refused without effect". F:468-470 "an invalid required basis prevents satisfaction and yields `invalid_basis`". F:482-484 "If the composite subject or governing basis itself cannot be interpreted, the aggregate is `invalid_basis`". RF:748 "The verdict is the core conjunction result; conflict annotates retained…". DESIGN:897 "An uninterpretable or contradictory governing basis is `invalid_basis`". | Inherited text (rc.2:1179; SPEC UP-021 rows) beside introduced owner. | Restate both loci as core verdicts, keeping conflict, veto and refusal-without-effect as retained domain outcomes, and cite F#result-conjunction. |
| CR2-03 | Medium | Reuse validity has three nominated owners and two divergent statements inside F. Neither F locus refers to the other, and F does not refer to UP-021 or Ticket. | F:128-129 "Reuse requires supported applicability, including identity, basis, freshness and the predicate actually assessed." F:569-571 "Reuse requires supported applicability: the same claim scope, adequate current basis and evidence, valid dependencies and required independent authorship." SPEC:1421 "`TICKET_METHOD.md` owns work-state recording and reuse." DESIGN:1659-1660 "the validity and reuse relation owned by `SPEC_METHOD.md` `STDO-UP-021`". Against these, TICKET:825-826 and TL:107 refer reuse to F#workspace-and-context. | F loci introduced. SPEC:1421 and DESIGN:1659 inherited. | Make F:569 the owner. Reduce F:128-129 to a referral. Make SPEC:1421, DESIGN:1659 and SPEC:1798-1806 refinements that name F#workspace-and-context. |
| CR2-04 | Medium | The sprint-close classification has two loci with different definitions of `accepted`. The named owner has no core map, and the copy that maps does not name the owner. TICKET:338 also fuses the compliance assessment with an acceptance label (R item 5). | TL:205-206 "[Ticket Method] owns sprint/paydown … classifications". TICKET:338 "`accepted`: compliant under the sprint authority" (no map at 336-346). UX:506 "`accepted`: compliant with this method and the cited design". UX:515 "`accepted` maps to … `satisfied` only for that compliance predicate". | Both lists inherited. UX map introduced. | Move the (value, cause) map to TICKET:336-343. Make UX:504-521 a refinement that names TICKET and maps its UX predicate. |
| CR2-05 | Medium | UP-015 dispositions, the set C3 itself is built on, are declared core refinements elsewhere but have no map. One set mixes a semantic judgement (`conserved`) with an owner decision (`intentionally removed`). | TL:206-207 "[Release Method] owns conserved/superseded/intentionally removed/not applicable" as "core refinements" (TL:205). RELEASE:561-565 lists the four, with no predicate or core value. | Set inherited. Refinement claim introduced. | Bind two predicates at RELEASE:557ff, a conservation judgement and an authorised disposition decision, and map each value. |
| CR2-06 | Medium | Packaging contradicts the Foundations' owning standing. | authority_compressions/README.md:8-9 "Foundations and the library are non-deciding explanations; the detailed owners retain deciding law". authority_compressions/README.md:58-60 has the same wording ("Foundations and the library organise explanations; detailed deciding law remains at its named owner"). Against this: the standards README (`standards/README.md:16-17`) "It owns the [single result algebra]"; F:55 "the owning locus of F1–F6"; RF:436-437 "The five verdicts and their conjunction have that single owner". | Introduced. | Change the compression README to name F as the owner of the result algebra, conjunction, workspace/context and configuration. Packaging states a standing it may not determine (R §Single Ownership 2, "packaging owns no method determination"). |
| CR2-07 | Medium | Six of the seven per-member compressions were re-pinned to successor digests, but their bodies are byte-identical to rc.2. Under its "current" pin, the AC compression serves the predecessor judgement shape: no predicate, verdict, performance or effects, and `decision` as the outcome. | AC compression:154-155 "binds kind, digest, basis, evaluator, authority, decision, evidence, provenance, and time". AC:725-728 "`predicate`, `verdict`, `performance`, `effects`… `decision` … is not another verdict enum". Body diff against rc.2 is 0 lines for the axiomatic, design, odd, spec, ticket and ux compressions; only `source_digest` changed. The refresh tool re-pins mechanically: ARTIFACT_CHECK.json:77, 82 "Compression pins and 6 excerpt views refreshed; no semantic verdict inferred." Scope: PRODUCT's tier table lets packaging stay unresolved until a release-candidate cut, so this blocks release-candidate readiness, not member acceptance. | Introduced re-pin over inherited body. | Regenerate the per-member compressions from the successor members, or mark them stale. Do not re-pin unchanged bodies. |
| CR2-08 | Medium | The Baseline qualification item contradicts the Baseline's own introduced map. Two variants map to `falsified`, and `incomplete` maps to two verdicts by cause, so the map is not disjoint "from" the RF result. | B:1708-1709 "every Worker work-result variant is disjointly mapped from its Reference Frame Method result". B:513-521: the `refused` row is `falsified`; the `incomplete`, `postcondition_defeated` row is `falsified`; the `incomplete`, `undecided` row is `indeterminate`. Closure item B:1939-1941 was updated; item 5 was not. | Introduced inconsistency (item text from rc.2). | Copy the closure wording, "maps to one core verdict on its exact predicate", into B:1708. |
| CR2-09 | Low-Med | The UP-021 admission outcomes have no core map at their owner. The map lives in a consumer. | SPEC:1849-1852 "refused without effect"; "causes effect-free re-entry". There is no F reference in SPEC:1787-1866. DESIGN:887 "UP-021 owns the admission decision". DESIGN:889-905 maps the admission assessment to core. | Set inherited. Consumer map introduced. | Put the (case, cause) → core map at SPEC UP-021. DESIGN refers to it. |
| CR2-10 | Low | The term "work state" has two referents and no disambiguation. | F:125 "Work state is the current subject under construction". TICKET:1381 "Work state has one authority chain: Goals own the bounded work wave, the ticket owns ticket state". SPEC:1421. | Inherited beside introduced. | Qualify one term (e.g. "ticket state authority") or add a context declaration. |
| CR2-11 | Low | "Verdict" is used for decision predicates, against the core's reserved term. | RELEASE:177 "acceptance remains a verdict over the exact immutable RC". DESIGN:1576, 1580 call `accepted`/non-accepted a "verdict". F:305 gives the verdict exactly five values. F:405-408 treats acceptance as a decision predicate. | Inherited. | Replace with "decision" and cite F:405-408. |
| CR2-12 | Low | Foundations restates the UP-020 disposition set with a different spelling and no link to its owner. | F:233-234 "disposition to repair, re-enter, reject or accept". The owner is SPEC:1687-1694 (`local_repair`, `re_enter`). | Introduced. | Link SPEC#proportional-disposition, or drop the enumeration. |
| CR2-13 | Low | A review checklist asks for the bare labels that the owner declares an incomplete handoff. | DESIGN:2468-2470 "with `pass`, `fail`, or reasoned `not_applicable`?" DESIGN:1539 "a bare `pass`, `fail` or `not_applicable` is not a complete handoff". | Inherited. | Ask for the core verdict with the original label. |
| CR2-14 | Low | Design totality refines F's total control contract without naming it, and its response list differs. | DESIGN:2005-2011 links only #result-algebra: "recovery, re-entry, yield or termination". F:201-203 "Bounded construction owns total control handling. The design totality rule refines that contract". F:605-606 "repair, re-entry, refusal, yielding or termination". | Introduced. | Name F#bounded-construction at DESIGN:2005 and align the list. |
| CR2-15 | Low | The effect owner has drifting copies, and two notes from Codex's own effect-owner review are not applied. | TOP:1155-1156 "a completed part with a known unexecuted or reverted remainder is `partial`" against F:369-370 "an observed unexecuted or reverted remainder". UX:209-210 binary success/failure `Msg` beside UX:241-245 (six states). runs/effect-owner-final/RESULT.md notes 1–2: "unexecuted" is still at F:370, and single-effect aggregation is split between F:363-372 and F:447-452. | TOP/UX restatements introduced. UX:209 inherited. | Make TOP:1153-1162 refer to F:357-381. Reword F:370. State completed + not_requested at the owner, or refer to the join. |
| CR2-16 | Low | Core spellings are reused as local values in unmapped sets. | B:1135 "`indeterminate` when the evidence cannot support a bounded frontier" (localization). B:791-792 "`out_of_frame` residual" (coverage disposition). RF:886 `unknown` coverage status. B:1449 `invalid_basis` → triage `not_applicable`, against F:409-410 "never a synonym for a missing evaluation". | Inherited. | Map each set (CR2-01) or rename. |
| CR2-17 | Low | A precedence rule stands where single ownership requires an owner. It is mitigated because owners are named per relation at B:103-118. | B:125-127 "If the profile conflicts with an owning STDO clause, the owning clause controls and the profile requires revision." R item 7. | Inherited. | Keep the revision duty and remove the precedence clause. |
| CR2-18 | Low | There are consistent restatements without a locus referral (duplicate deciders). | SPEC:1419-1423 against F:463-475 (closure conjunction). B:415-416 and B:806-813 against F:463-475. SPEC:1440-1442 and SPEC:1768-1775 (progress, mutually unreferenced) against F:611-613. SPEC:1726-1727 against F:615-616. TICKET:767-774 and 835-837 against F:631-632 (independence). SPEC:1566-1567 / F:187-189 / TL:264-270 ("no universal" budget). DESIGN:1652-1653 has four accounts against F:238-243 "three accounts". TICKET:240-241 and TICKET:336-343 give two debt-disposition vocabularies. | Mostly inherited beside introduced owner. DESIGN:1652 introduced. | Add a referral at each locus, or reduce it to a referral. |
| CR2-19 | Low | TOP `transition_evaluation` maps `partial` by evidence without a declared cause case. Decision `falsified` reuses the core spelling, and the member gives no explicit map line for it. | TOP:781 domain includes `satisfied`, `falsified`, `partial`, `indeterminate`. TOP:798-800 "determine `falsified` if non-fulfilment is established, or `indeterminate`". | Introduced. | Add `partial`/`unfulfilled` and `partial`/`unknown` causes, plus a `falsified` row. |
| CR2-20 | Medium | The RETURN's claim that "consumers refine their own outcomes into it" is not supported by the text. RETURN:123-124 attributes residual vocabulary problems to actor fidelity, but the method text itself leaves 45 sets without a per-value map. | RETURN:31-32 "One core result owner … Consumers refine their own outcomes into it." See CR2-01 and the inventory. | n/a (evidence claim) | Narrow the claim, or complete the maps. |
| CR2-21 | Medium | Tier defect (oracle E-4-2). Mandatory Spec intake depends on an optional profile's clause. Causal localization is generic assurance law, but its only owner is the optional Baseline, and Spec intake links to it without making that conditional on adoption. Its result set (inventory row 24, unmapped) is therefore reachable from mandatory work. | SPEC:1308-1311 "Use the smallest sufficient applicable frame configuration … with [causal localization](STDO_REFERENCE_FRAME_BASELINE.md#counterexample-localization) where required." B:91 "This document is an optional derived role and evaluation profile." B:1121-1135 owns the localization rule and its four-way result. Contrast F:218 and F:636 and TL:163, which reference the Baseline only under consumer adoption. | Inherited (rc.2 SPEC:1231). | Move counterexample localization, with a core map, to the Spec Method's assurance law. The Baseline refers to it. |

Counts:

- **Competing owner pairs: 18.** These are divergent content or a misnamed owner, with no referral:
  - CR2-02: 2 pairs (RF:1243 against F; SPEC UP-021 against F).
  - CR2-03: 3 pairs (F:128 against F:569; F against UP-021; F against Ticket).
  - CR2-04, -06, -07, -08, -09, -10, -11, -12, -13 and -14: 1 pair each.
  - CR2-15: 2 pairs (TOP; UX intra-member).
  - CR2-18: 1 pair (the TICKET debt vocabularies).
  - Of the 18, 9 fall under Medium findings. CR2-21 is a tier defect, not a pair.
- **Precedence rules between loci (oracle E-4-6, N-11).** A grep of all 18 members for `controls|prevails|wins|overrides|takes precedence|governs where|outranks` finds one: B:125-127 (CR2-17). B:1670 "`STDO-UP-007` controls" names an owner. ODD:208, TICKET:1315, IDENTITY:352/372 and WM:53 concern releases, fixtures, identity overrides or amendment authority, not loci.
- **Consistent duplicate deciders without a locus referral: at least 12.** These are CR2-18 plus ODD:737-741, ODD:1019-1029, ODD:1291-1296, B:1222-1227 and TOP:1163-1167.

## Value-set inventory

The core sets are owned once, at F. They are not counted as refinements:
- verdict: F:305-313;
- performance: F:315-325;
- effect: F:357-381;
- the decision-predicate rule F:402-410 and the stop rule F:412-416.

There are no second cores. Restatements of the five verdicts carry the same values at RF:20, RF:1107 (example), B:1171, B:1561 and TOP:758-763. RF:20 has no link at the locus, but RF:64-68 names the owner.

Order of the rows below: RF, AC, IDENTITY, GLOSSARY, DESIGN, B, SPEC, TICKET, RELEASE, ODD, UX, TOP, WM. TL, POSTING, WRITING and README define no result set; they refer.

| # | Locus | Values (short) | Kind | Status | Mapping locus / note | Origin of set |
|---|---|---|---|---|---|---|
| 1 | RF:597-598 | activated_frame / activation_refusal | frame | M | RF:443-453 (admission predicate) | inh. |
| 2 | RF:606-607 | translated_value / declared_loss / refusal | frame | R | RF:616-625 "The frame binds any finer case mapping" | inh. |
| 3 | RF:880-888 | covered … excluded_by_authority (7) | judgement | U | none | inh. |
| 4 | RF:1243 | conflict / indeterminate / refusal | combination | D | competes with F:463-475 (CR2-02) | inh. |
| 5 | AC:427-439 | constraint outcome (5 rows) | constraint | M | AC-007 table | intr. map |
| 6 | AC:457-461 (+505, 686, 870, 495) | hold / gap / refusal / refuse + cause | stop | M | by cause → 4 core values | intr. map |
| 7 | AC:452-455, 947-950 | accepted / admitted / refuse | decision | M | decision predicate | intr. map |
| 8 | AC:784-791 (151, 549, 769) | `Omega_v`, `stop_states`, `StopKind` | stop | I | "binds each outcome … to one core verdict" | intr. |
| 9 | AC:725-729 | Judgment.decision | judgement | I | "declares its map before the judgment is used" | intr. |
| 10 | AC:899-901 | retained / omitted / residual / inapplicable / refused | judgement | R | only AC:449-451 blanket | inh. |
| 11 | IDENTITY:49-59 | verification refusal + cause | constraint | M | in place | intr. map |
| 12 | IDENTITY:398-406 | identity reader admission | constraint | M | in place | intr. map |
| 13 | GLOSSARY:32-42 | route resolution | judgement | M | in place | intr. |
| 14 | DESIGN:1505-1524 | pass / fail / not_applicable | judgement | M | in place, by predicate | inh. set, intr. map |
| 15 | DESIGN:1401-1406 | preserves / changes / duplicates / violates | judgement | U | none; no undecided value | inh. |
| 16 | DESIGN:1573-1580 | accepted / non-accepted | decision | R | DESIGN:1573 generic | inh. |
| 17 | DESIGN:2005-2023 | unsupported / rejected; four causes | work / stop | R | DESIGN:2005-2006 generic | mixed |
| 18 | DESIGN:889-905 | admission assessment | judgement | M | in place | intr. |
| 19 | B:513-521 | candidate_ready / refused / incomplete / re_entry_requested + cause | work | M | in place | intr. map |
| 20 | B:1443-1449 | triage complete / indeterminate / not_applicable | judgement payload | X | excluded: B:1439-1441 "they are not new evaluation results". Read as a refinement it fails exactly-one: triage `not_applicable` sits under `satisfied` and `invalid_basis`, and `indeterminate` under `indeterminate` and `out_of_frame` (see CR2-16) | inh. rows |
| 21 | B:413-416 | drift-lock failures | judgement | M | in place | inh. |
| 22 | B:489-491 | blocks / requires narrowing / residual | decision | R | B:34-36 | inh. |
| 23 | B:331-333 | Executive stop conditions | stop | R | consistent with F:412-416, no link | mixed |
| 24 | B:1128-1135 | locus / joint set / frontiers / `indeterminate` | judgement | U | none | inh. |
| 25 | B:784-792 | instantiated / non-material / residual | judgement | U | none | inh. |
| 26 | SPEC:1687-1694 | accept / local_repair / re_enter / reject + cause | judgement | M | "Core verdict" column | intr. map |
| 27 | SPEC:1712-1717 | applied disposition | decision | M | F:405-408 | intr. |
| 28 | SPEC:1361-1367 | covered / missing / stale / ambiguous / outside-scope | judgement | R | SPEC:1305-1306 | inh. |
| 29 | SPEC:1352-1364 | changed / unchanged / unknown delta | judgement | R | SPEC:1305-1306 | inh. |
| 30 | SPEC:1157-1158 | resolved / carried forward / escalated / blocked | decision | U | none | inh. |
| 31 | SPEC:655-667 | exactly one admits; zero unresolved; many ambiguous | constraint | U | none at owner | inh. |
| 32 | SPEC:127 | stop / hold / gap / continuation / completion | stop | U | none | inh. |
| 33 | SPEC:1185-1191 | hard-stop classes | stop | U | none | inh. |
| 34 | SPEC:1440-1442 | advance / readiness / preservation / regression | judgement | U | none | inh. |
| 35 | SPEC:1768-1775 | progress / prerequisite / preservation / churn | judgement | U | none; second locus of 34 | inh. |
| 36 | SPEC:1847-1852 | admitted / refused without effect / effect-free re-entry / not_applicable | decision | U | consumer map only, DESIGN:889-905 (CR2-09) | inh. |
| 37 | SPEC:526-614 (534-538) | fail closed / refusal / restore / recovery | work / effect | U | none; effect prose not in core vocabulary | inh. |
| 38 | SPEC:2422-2423 | governed diagnostic / semantic failure | constraint | U | none | inh. |
| 39 | TICKET:336-343 | accepted … remove (6) | judgement + decision | R | TL:205-206; TICKET:10-12 preamble | inh. |
| 40 | TICKET:240-241, 257-258 | accepted / ticketed / repriced / removed | decision | R | TL:205-206 | inh. |
| 41 | TICKET:728-742 | admitted / rejected + cause | judgement | M | in place | intr. map |
| 42 | TICKET:851-863 | retained / superseded / deferred / withdrawn | decision | R | TICKET:859-861 decision predicate, no table | intr. binding |
| 43 | TICKET:785-794 | blocks promotion / repricing input | decision | U | none | inh. |
| 44 | TICKET:658, 696-703 | stop / re-enter; returns missing authority | stop | R | TICKET:10-12 | inh. |
| 45 | RELEASE:224-231 | publication core result; `unknown` effect | effect / work | M | in place | intr. |
| 46 | RELEASE:250-263 | passed / skipped / cached green | judgement | R | guarded; "cannot raise its standing" | intr. |
| 47 | RELEASE:290-292 | advance / refused | constraint | U | none | inh. |
| 48 | RELEASE:220-222, 316-326, 454-481 | fails closed / refuses / stops | stop | U | none | inh. |
| 49 | RELEASE:417-424 | cohort complete / incomplete | constraint | U | none | inh. |
| 50 | RELEASE:538-543 | owner accepted | decision | M | decision predicate | intr. |
| 51 | RELEASE:561-565 | conserved / superseded / intentionally removed / not applicable | judgement + decision | R | TL:205-207 only (CR2-05) | inh. |
| 52 | ODD:921, 1194-1225 | EdgeClosureDecision (7) | decision | M | in place, by predicate | intr. map |
| 53 | ODD:1089-1101 | evaluate_next outputs incl. typed no-action | decision | R | ODD:45; partial at 1223-1224 | inh. |
| 54 | ODD:913 | GapPressureRow (5) | judgement | R | ODD:45 | inh. |
| 55 | ODD:265 | stop / hold / gap / continuation / completion | stop | R | ODD:317-323 | inh. |
| 56 | ODD:317-322 | F_D / F_P / F_H returns | work | R | per-predicate prose | intr. |
| 57 | ODD:483-487 | compliant / non-compliant / incorporate | judgement | R | ODD:45; no undecided value | inh. |
| 58 | ODD:874-879 | loop stop conditions | stop | R | ODD:45 | inh. |
| 59 | ODD:1515-1519 | method defect / agent error | judgement | R | ODD:45 | inh. |
| 60 | ODD:1587-1593 | carrier open / closed | judgement | R | ODD:45; "explicitly deferred" closes without applicability judgement | inh. |
| 61 | ODD:1171 | edge_converged | judgement | R | ODD:45 | inh. |
| 62 | UX:209-210, 241-245 | success / failure `Msg` | effect | R | no per-state map | mixed |
| 63 | UX:320-331 | replay assessment | judgement | M | in place | intr. |
| 64 | UX:506-521 | sprint-close six classes | decision | M | in place, but competes (CR2-04) | inh. set, intr. map |
| 65–70 | TOP:775-780 | model_validation … effect_readiness decisions | judgement | M | TOP:789-797, 804-811, 820-828 | intr. map |
| 71 | TOP:781 | transition_evaluation (6) | judgement | D | CR2-19 | intr. |
| 72 | TOP:782 | frontier_projection | judgement | M | TOP:789-794 | intr. map |
| 73 | TOP:747-755 | stop hold … partial_effect | stop | M | as cause, TOP:804-813 | intr. map |
| 74 | TOP:1127-1170 | no_effect / completed / partial / refused effect | effect | M | TOP:1144-1170 (unknown kept) | intr. map |
| 75 | TOP:596-597 | refuse_* / not_applicable | constraint | R | AC:457 generic only | inh. |
| 76 | WM:816-823 | assurance outcome by condition | judgement | M | in place; no positive `satisfied` condition | intr. |
| 77 | WM:46 | publish / supersede / retain unresolved | decision | R | WM:55-57 | inh. |
| 78 | WM:1201-1215 | accepted overlay / candidate | judgement | R | WM:55-57 | inh. |
| 79 | WM:1241-1253 | null-peer tests pass / fail | judgement | R | WM:55-57 | inh. |
| 80 | WM:1079-1101 | eight-surface admission | judgement | M | refers F#result-conjunction | intr. |

Totals, counted by script over this table (rows 65–70 are six sets; row 20 is excluded): M 30, I 2, R 28, U 17, D 2, for 79 sets. Mapped (M+I) is 32; without a per-value map is 47. All 17 U sets are inherited text that was not unified onto the core.

Distinctions through combination:
- The three distinctions survive in F's conjunction:
  - non-performance: the absent-slot rule, F:457-458, and component retention, F:421-425;
  - undecidability: F:471-472;
  - unknown effects: "any unknown gives unknown", F:447.
- The aggregate itself records `performance = performed` (F:427-428) even when every component is `not_performed`. Under oracle A2(b) this passes, because the component results are mandatory and "Its summary never replaces them" (F:425).
- In the M sets the distinctions are kept in place: B:526-527, DESIGN:1522-1524, TICKET:739-741, RELEASE:258-260, ODD:1212-1216, TOP:1149-1150, 1163-1164.
- In the R, U and D sets they are not addressed per value.
- No set maps a failure, undecided, unperformed or unknown-effect value upward. RELEASE:256-257, TOP:789-790 and WM:821-822 explicitly forbid it.
- WM:821-822 says "never `satisfied` by default". That is weaker wording at the point of use than F:324, but it is not a raise.

Excluded sets, by reason:
- **Carrier lifecycle:** TICKET:245-262 sprint status; TICKET:716-719, 742 contract states; TICKET:1336-1352 ticket status ("not a second result algebra", 1346-1347); SPEC:3062 ADR status; SPEC:1487 basis termination.
- **Kinds and change classes:**
  - SPEC:1318-1323 change classes;
  - TICKET:507-527 types and categories;
  - TOP:705-744 constraint, judgment and residual kinds;
  - AC:776-778 functor kinds;
  - B:49-51, 763-776 and 834-844 families and frames.
- **Design or treatment choices:**
  - SPEC:2005-2008 treatments;
  - SPEC:2703-2718 and TICKET:1130-1136 migration classification;
  - DESIGN:1699-1702 realization dispositions;
  - DESIGN:928-934 derivation-row dispositions;
  - RF:704-716 reconfiguration and RF:1001-1013 revision menus.
- **Input bases and provenance:** ODD:916 NextActionBasis; WM:822-823 provenance classes; WM:410-433 construct status; TOP:193-197 observation and scope kinds.
- **Completeness markers:** DESIGN:757-758, 646-648 and 1956-1961 (`Gap:`/`Unanswered:`/`not_applicable`). These are borderline: `not_applicable` there has no applicability-predicate tie.
- **Single witness constant:** AC:662 `decision: equal`.
- **Product-owned scales:** B:483-485 severity and priority.

## Records requested by the oracle

- **Oracle A3 (dispositions).** The candidate reads dispositions as decision-predicate refinements inside the core: TL:205-207 ("Other instances retain their original domain classifications as core refinements"), with F:405-408 binding the predicate "disposition D on subject S at basis B was made under mandate M". The reading is coherent where a map is given: SPEC:1712-1717, TICKET:859-861, RELEASE:538-543, ODD:1194-1225. It is not discharged for UP-015 (CR2-05), the sprint-close set (CR2-04) or the debt dispositions (TICKET:240-241).
- **Identity (scope item 1).** DESIGN:2307, "Exact hashes establish subject identity", was examined against F:120-122, "Content equality does not establish identity … A digest binds bytes". DESIGN uses hash identity for a frozen review subject; F speaks of scoped object identity across state changes. F:124 names IDENTITY_METHOD as owner of governed names, and IDENTITY:72-78 and 398-406 refine with core maps. Conclusion: no competing owner. There is a wording tension only, which is not counted as a pair.
- **Oracle A2 (distinct outcomes).** The candidate uses reading (b): distinctions travel in the performance and effect coordinates and the retained components (F:315-355, F:421-425), not in extra verdict values.

## Frames

- **Digests and bytes.** All 89 `Source:` excerpts in the 6 frames reproduce their owner section byte for byte after the declared link relocation. All 11 owner SHA-256 pins match the frozen members.
- **Core algebra.** Every frame carries both `F#result-algebra` and `F#result-conjunction`. Every result-returning frame therefore carries the core (R item 7).
- **Profile mappings.**
  - DOMAIN_BINDING does not include ODD's closure-decision map (ODD:1194-1225). Its stated scope (DOMAIN_BINDING:3) does not require it.
  - TRIAGE_CARRIER carries SPEC:1330-1403, which includes rule-only sets 28 and 29.
- **Compressions** are packaging, not frames. Their digest pins match, but see CR2-06 and CR2-07.

## RETURN claims tested

| Claim | Verdict | Evidence |
|---|---|---|
| RETURN:30-33, one core result owner with predicate, raw outcome, cause, performance, extent, verdict, evidence and effects | holds for the core | F:296-416 is the only core. RF-012 (RF:433-469) and AC-007 (AC:427-471) refer to it and map into it. 6 of 6 frames copy it exactly. |
| RETURN:32, "Consumers refine their own outcomes into it" | falsified as a text-wide claim | 45 sets have no per-value map (28 R, 17 U), and 2 are D (CR2-01, CR2-20). |
| RETURN:34-37, composition binds predicate and joins; current-observation effect reconciliation | holds in F | F:427-453, F:489-518, AC:829-863. Conjunction-once fails narrowly at RF:1243 (CR2-02). |
| RETURN:53, `9bc8962` removes the competing classification from conjunction | holds within F | F:436-437 "The composite supplies no different classification". It is not a one-effect-owner result across members: TOP:1155-1156, UX:209-210, SPEC:534-538, and RESULT.md notes 1–2 remain (CR2-15). |
| RETURN:74, 89 exact sections and 32 compression pins | holds for frames | The frame script reproduces 89/89. Pins match, but six re-pinned compression bodies are rc.2 bytes (CR2-07). |

## What holds

- **One core in the Foundations.** It has five verdicts, three performance values, six effect values, legal pairs, a reason-sensitive refinement rule, and a separate decision predicate (F:296-416). Conjunction, effect join and declared operators are given once (F:418-530).
- **RF-012 and AC-007 are unified into the core.**
  - RF:435-437 says "The five verdicts and their conjunction have that single owner".
  - The AC-007 constraint-outcome table maps each outcome to one core verdict (AC:433-439).
  - Hold, gap and refusal are mapped by cause (AC:457-461).
  - Neither predecessor algebra survives as a parallel set.
- **Strong refinement maps:**
  - B:513-521, keyed by cause, with a missing-reason row;
  - SPEC:1687-1694;
  - DESIGN:1505-1524, which separates applicability from conformance;
  - DESIGN:889-905;
  - TICKET:728-742;
  - RELEASE:250-263, guarded against raising standing;
  - IDENTITY:49-59 and IDENTITY:398-406;
  - GLOSSARY:32-42;
  - ODD:1194-1225;
  - UX:320-331;
  - TOP:765-830, apart from row 71;
  - WM:816-823.
- **Availability, assessment and acceptance stay separate:** F:402-410, B:524, AC:449-455, SPEC:1708-1710, TOP:789-790.
- **Owner referrals that refine correctly:**
  - TICKET:825-833 refers to F#workspace-and-context;
  - RF:740-753 refers to core conjunction;
  - TL refers throughout (TL:92, 170-183, 187-193, 212-214);
  - B:721-725 refers to UP-020 without a second table.
- **Frames:** exact copies with named owners and matching digests.

## Coverage limits

- **Delegated reading.** SPEC, DESIGN, B, ODD, UX, TICKET, RELEASE, WM and TOP were read in full by bounded sub-evaluations. The ODD evaluation read lines 140-249, 339-459, 502-722 and 1720-1818 by keyword only. The TOP reference-domain tables (210-500, 533-700) were spot-read.
- **Quote verification.** The parent re-read every locus in the findings table. Inventory rows outside the findings were spot-checked (24 loci) rather than all re-read.
- **Inherited/introduced labels** rest on one `grep -F` phrase per locus.
- **Inclusion judgements are contestable.** Rows 22, 25, 43 and 60 could be read as triage or coverage classifications rather than results. Excluding all four changes the totals to M 30, I 2, R 26, U 15, D 2 (75 sets; 32 mapped against 43).
- **Packaging.** Templates, schemas and plugin assets were not reviewed. Compressions were checked for pins, body identity with rc.2 and the cited standing statements only.
- **Not assessed.** Semantic conservation of predecessor claims and the a_c interpretation evidence.
