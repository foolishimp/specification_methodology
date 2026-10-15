# CB2: cross-family review of the Codex v3 iteration 3 candidate (result algebra, ownership, transitions, binding, categorical claims)

Status: commentary, not specification. A Claude reviewer assessed a Codex-authored subject and repaired nothing. Findings on parts ported from the Claude candidate are marked "not independent".

## Basis

- Subject: frozen `3aaa2f2`, at `subject/.../codex/successor/standards/` (18 members, 6 frames, compressions), with `design/DESIGN.md` and `qualification/`.
- The member and design bytes at `3aaa2f2` are identical to those at the return checkpoint `939ce0c`; `git diff 3aaa2f2 939ce0c` touches only `qualification/`.
- Return claims tested:
  - the return post on `main`, `.ai-workspace/comments/codex/20261014T134223Z_RETURN_CODEX_V3_I3_R2.md` (RP);
  - `qualification/C3/iteration-3/RETURN.md` at `939ce0c` (RET).
- Common specification at `355aa86`. Installed predecessor `v2.5.1-rc.2`.
- Iteration 2 comparison subject `9bc8962`. Its findings are CR2 (result algebra and ownership) and CR3 (transitions, binding, categorical claims).
- Expectations: part A (H2, M1) and the oracle part B, groups d, e, f and g. Both were read before the subject.

Path abbreviations: `F` = FOUNDATIONS.md, `TL` = TRANSFORMATION_LIBRARY.md, `RF` = REFERENCE_FRAME_METHOD.md, `AC` = AXIOMATIC_CALCULUS.md, `B` = STDO_REFERENCE_FRAME_BASELINE.md, `TOP` = TRAVERSAL_OCCURRENCE_PROFILE.md, `WM` = WORLD_MODEL_METHOD.md, `DES` = `design/DESIGN.md`. The other members are spelled out. Line numbers refer to the subject at `3aaa2f2`.

## Method

CR2's method is reused so the counts compare. Its inclusion rule, status classes and severity scale are unchanged. Three rules are added because iteration 3 introduces two-predicate maps and a general "other instances" rule.

- **Inclusion rule (unchanged).** A set is counted when it is the outcome of a constraint check, a judgement, a frame evaluation, a stop, a work step, an effect, or a decision or disposition. Lifecycle statuses, kinds, change classes, input bases and treatment menus are excluded with a reason.
- **Status classes (unchanged):**

| Class | Meaning |
|---|---|
| M | A per-value or per-(value, cause) map to exactly one core value, given at the set's owner. |
| S | Declared a recorded state, with its purpose, at the set's owner (new label; CR2 had none in use). |
| I | An open, instance-declared set. The member obliges each instance to bind an exactly-one map before use. |
| R | Rule-only. The set is covered only by a general rule, such as F:391-408, F:410-418, F:420-424 or TL:320-323, which cannot assign each value its core target. |
| U | No referral covers the set. |
| D | Competing or defective map. |
| X | Excluded, with a reason. |

- **Added rule 1, two-predicate maps.** Some sets are now named treatments or dispositions and bind a separate semantic predicate plus a decision predicate. Such a set counts as M only if the owner states all three of:
  - the named semantic predicate;
  - a cause-keyed table that gives each (value, cause) exactly one core value;
  - each value's decision relation.
  Otherwise it counts as R. The missing-reason case may rest on F:397-400, because that rule decides a unique value (`indeterminate`).
- **Added rule 2, general rules stay R.**
  - **Sets covered only by a general rule are R.** This applies to a set covered only by F:391-408, by an unbound reference to the stop rule at F:420-424, or by TL:320-323 ("Other instances retain their original domain classifications"). H2 forbids exactly that.
  - **Decision and stop sets are an exception.** They count as M when their owner explicitly binds them to a named predicate. For decision sets that predicate is the decision predicate of F:410-418, as CR2 counted rows 7, 27 and 50: "disposition D … was made under mandate M" fixes the core value case by case through the verdict meanings at F:315-321. For stop sets it is the stop rule F:420-423 on the exact task predicate and cause, which likewise decides by evidence case.
  - **The exception does not cover assessment claims.** A value that also asserts an assessment, such as `accepted` meaning "compliant" (CR3 F-1), stays R unless that assessment is mapped.
- **Added rule 3, a recorded state needs a declaration at its locus.** It counts as S only where the set's owner declares it a recorded state, with its purpose. TL:320-323 tells owners to distinguish recorded state; that instruction alone does not make any set S.
- **Unit rule (unchanged).** TOP rows 65-70 count as six sets. Totals are also given without the contestable rows 22, 25, 43 and 60.
- **Severity (unchanged), relative to C3 acceptance:**

| Severity | Meaning |
|---|---|
| High | A requirement item fails across members, or a stated qualification claim is materially contradicted by the text. |
| Medium | A requirement item fails at a specific locus in a way a consumer would act on: a competing owner with divergent content, an unmapped closed set in a deciding member, or packaging that misstates standing. |
| Low | Wording drift, consistent restatement without a referral at the locus, or an intra-member duplicate with consistent content. |

- **Origin labels:**
  - rc.2-inherited: byte-present in the installed predecessor;
  - I2-introduced: present at `9bc8962`, absent in rc.2;
  - I3-introduced: new at `3aaa2f2`.
- **Inherited or introduced** was decided with `grep -F` of a distinctive phrase against rc.2 and against `9bc8962`.
- **Reading.**
  - F, TL, TICKET (sprint close), RELEASE (UP-015), UX (sprint close) and DES were read directly.
  - The other members were inventoried by bounded read-only sub-evaluations. Each was anchored to its member's CR2 rows and swept the member for new sets. All used the schema above.
  - Every quote in the findings table was re-read by the parent at its cited range.
- **Frames.** CR2's script (`scratchpad/cb2tools/framecheck.py`, run with `python3 -I`) recomputes each owner's SHA-256, extracts the owner section, relocates links and byte-compares it with the frame's copy.

## Transitions, recovery and acquisition (oracle group e)

Port note: `FOUNDATIONS.md#workspace-and-context` receives ports I3-R2-P01 and P02 (`PORT_ACCOUNT.json`). Results resting on F:540-594 are therefore **not independent**.

| Item | Result | Owning text |
|---|---|---|
| E1 transition, destination change, stop | Holds | F:602-604 "A transition binds its preconditions, permitted effects, result predicate and outer obligations". F:626-627 "Changing Z follows its owner and cannot establish that the old destination was reached". F:420-423 a stop reports "the actual destination or task predicate … with its reason, observed effects and outstanding obligations". |
| E2 capacity never licenses omission | Holds | F:198-205 "If a coupled required relation does not fit, the actor reports the misfit … Never replace a difficult required relation with an easier claim". TL:272 "Capacity does not license omission." RF:489-494 (RF-014) "The actor may not silently omit material relations to fit context." RF-003 (RF:369-376) "An omitted material relation makes the activation insufficient." |
| E3 fit and adequacy judged separately | Holds in content; ownership fails (CB2-03) | TL:269-270 "Measure context where the execution binding selects it, and assess actual adequacy separately." SPEC:908-910 "Attention adequacy is evaluated through actual-use evidence; no universal attention unit or score is required." RF-002 (RF:362-367) decides fit only. |
| E4 configuration, no role inventory | Holds | F:632-640 "They do not uniquely derive a hierarchy or a fixed inventory of roles. An adequate configuration can use one actor, peers, a hierarchy or supported adaptive allocation." F:645-646 "Roles acquire authority from their grants, never from their names. Functional decomposition, communication, authority and evaluation dependency are distinct." F:648-650: the Executive arrangement is "optional". Inherited residue as in CR3 F-7 and F-8: SPEC:1844-1858 ("constructor or Writer", "Executive mutation restrictions remain applicable") and RF:209, RF:492 ("human authority"). These permit; they prescribe no inventory. |
| E5 recovery | Holds (not independent) | F:542-545 "The actor's context is a bounded account … It is fallible and disposable." F:559-561 "Absence from a partial projection, sparse checkout or empty local record is not evidence of absence". F:572-575 resumption "neither erases progress nor requires a transcript". F:587-594: an event log "is not universally the work state or a compulsory recovery algorithm". F:382 "An empty local log or discarded context does not establish no effect." |
| E6 reuse checks | Holds (not independent) | F:577-585 "Reuse requires supported applicability: the same claim scope, adequate current basis and evidence, valid dependencies and required independent authorship … A stored green label is not a validity argument … A role, conversation or resumption change alone is not an invalidator". |
| E7 acquisition quantities | Holds at the design | DES:84-86 "Supplied context, cumulative acquisition and actively retained context are separate quantities; unknown host or reasoning portions remain unknown." RP:84-85 "Reader emissions are not retained context or token usage; source I/O is separate." |
| E8 result binding | Holds | F:463-467 "First authenticate each contribution against its producer, subject, basis and required plan membership. An unauthenticated claim cannot discharge an obligation." |

## Build-tenant binding (oracle group f)

Port note: `SPEC_METHOD.md#what-how-and-work-carriers` receives port I3-R2-P04. Findings on SPEC:877-935 are **not independent**. That section is byte-identical to `9bc8962`, checked by `diff` of the extracted section.

| Item | Result | Owning text |
|---|---|---|
| F1 chain from requirements calculus to computational calculus to environment | Holds | SPEC:887-895 "The common `WHAT` is the requirements calculus … A tenant's design supplies its computational calculus and concrete binding … The binding may use software, hardware, people, organisations or a mixture." |
| F2 author, actor and operation kind distinct; human decisions stay human | Holds in use, incomplete at the owner (CB2-09) | SPEC:898-901 "Author identity, actor identity and operation kind remain distinct … A person performing a procedure is not thereby making a human adjudication." The owner still omits "including any required human decision". It is carried only at SPEC:1840 ("does not weaken direct-human acceptance where …"). This is CR3 F-4, unchanged. |
| F3 operations, laws, effects, measures with units and boundaries | Holds at the owner | SPEC:906-908 "Context, time, memory, communication, human effort and spend state their units and are measured at the boundary declared by that binding where they are material." |
| F4 calculus reuse; a_c selects no executor | Holds | SPEC:896-902 "A computational calculus may be reused across tenants and execution environments … An a_c representation neither selects the executor nor proves realisation conformance by passing structural validation." |
| F5 tenant applies the binding to its own process | Improved, still incomplete (CB2-10) | DES:5-15 and DES:58-88 add an operations table and separate the supplied, cumulative and retained quantities. Still absent: units for time and spend; the "declared process boundary" (DES:14) is never declared; the review actors and their family; the per-call and aggregate limits; failure assumptions. These are CR3 F-5 residue. DES:162-174 keeps the candidate's rule for future consumers. RET:189-190 "The installed builder and common input above govern this evaluation; the candidate has not become its own authority." |

## Categorical demonstration (oracle group g)

| Item | Result | Owning text |
|---|---|---|
| G1 standard carried as law | Holds, with two loci (CB2-08) | F:251-274 carries items 1-5. TL:360-362 restates a subset: "declare the objects, arrows, equality, identities and composition and discharge the laws at that domain". AC:883-884 refers to the library, not to F: "Categorical claims additionally meet the library's demonstration conditions." |
| G2 objects, arrows, functor laws | Holds | F:251-253 "To assert a category, specify its domain, objects, typed arrows, arrow equality, identities and associative composition. To assert a functor, define its action on objects and arrows and show identity and composition preservation." AC:846-849: `Functor Kind` "does not by itself assert a category-theoretic functor". |
| G3 per-layer preservation, end-to-end bound | Holds | F:263-265 "approximation declares its adequacy relation and an end-to-end bound, since local tolerances alone do not compose". |
| G4 licensing laws | Holds | F:265-267 "without additional laws only universally valid steps are licensed". |
| G5 evidence class; distinct claims | Partly holds (CB2-11) | F:270-271 names the four evidence classes. F:257-259 distinguishes conformance, semantic equivalence and computational equivalence, but does not name functorial preservation as a distinct claim (CR3 F-9, unchanged). F:518-520 asserts two associativity laws with no argument and no evidence class (CR3 F-6, unchanged). |
| G6 capability unselected; worked join reserved | Holds | F:273-274 "an unproved categorical account remains a hypothesis". DES:141 "the unselected categorical work item". RET:156 "I3-15 categorical worked join: Reserved and not selected". No member presents the five layers, a sheaf account or a grade algebra as law (grep). B:670's "steel thread" is the Executive delivery term, not the categorical one. |

## Frames and acquisition views

- **Exact copies.** CR2's script reproduced all 98 `Source:` excerpts in the six frames, byte for byte after the declared link relocation. All 11 owner SHA-256 pins equal the frozen members. There were 0 `sha_ok=False` and 0 `DIFF` lines (`scratchpad/cb2tools/frames.out`).
  - The per-frame counts are CONSTITUTIONAL_DERIVATION 23, DOMAIN_BINDING 18, TRIAGE_CARRIER 19, WORK_RECOVERY 15, RELEASE_ADOPTION 12 and EVALUATION_CONJUNCTION 11. This supports RET:56-57 "Six task views contain 98 exact source excerpts".
- **Core carried.** Every frame carries both `FOUNDATIONS.md#Result algebra` and `#Result conjunction`, so oracle D11 and R item 7 hold for the core.
  - WORK_RECOVERY:491 and TRIAGE_CARRIER:922 also carry the UP-020 disposition map.
  - RELEASE_ADOPTION carries the UP-015 section with its new map.
  - No frame carries the sprint-close map (TICKET:343-395). No frame's stated task is sprint close, so this is not a defect.
- **Acquisition routes.** The ordinary work entry (`plugins/spec/skills/stdo-work/SKILL.md:28-35`) routes by task to the work/recovery, triage/carrier and constitutional-derivation views, and otherwise to the "deciding owners". It states that "The view alone makes no universal sufficiency claim" (SKILL.md:46-47).
- **Compressions.**
  - All 25 front-matter pins in `stdo_bootstrap.md` and `stdo_compressed.md` and all 7 per-member `source_digest` pins match.
  - The per-member bodies are no longer rc.2 bytes. Against `9bc8962` they differ by 7-29 changed lines each.
  - The AC compression now carries the successor judgement shape. AC compression:157-158 says a judgement "carries the predicate, core verdict, actual evaluation performance and observed effects".
  - CR2-07's defect is therefore repaired in the sampled case. Its packaging README wording (CR2-06) is also repaired: `authority_compressions/README.md:8-9` "Foundations and the library own shared deciding contracts".

## Result algebra inventory (H2; oracle group d)

### Counts

CR2's 79 sets were re-located in iteration 3. Rows 65-70 count as six sets; row 20 stays excluded.

| Status | Iteration 2 (`9bc8962`) | Iteration 3 (`3aaa2f2`) |
|---|---:|---:|
| M (mapped at owner) | 30 | 59 |
| I (instance-declared map) | 2 | 4 |
| S (declared recorded state with purpose) | 0 | 2 |
| R (rule-only) | 28 | 9 |
| U (unmapped) | 17 | 0 |
| D (competing or defective) | 2 | 1 |
| Merged into another owner's set, or dissolved | - | 4 |
| **Total** | **79** | **79** |
| Mapped (M+I+S) against unmapped (R+U+D) | 32 against 47 | 65 against 10 |

**Without the contestable rows 22, 25, 43 and 60:** M 58, I 4, S 1, R 7, D 1, for 71 sets, 63 mapped against 8.

**Parent overrides.** The parent graded thirteen rows M where a sub-evaluation applied a stricter reading and gave R: rows 7, 10, 16, 23, 26, 27, 44, 45, 50, 58, 74, 77 and 80. Under that stricter reading the comparable count is M 46, R 22.

The overrides follow the decision-and-stop rule in Method. Each overridden set either:
- binds its decision predicate explicitly (7, 16, 27, 50, 77);
- binds its stop to the stop rule on a named predicate and cause (23, 44, 58);
- maps its semantic leg by cause through a linked owner (10);
- refers to a core rule that itself decides the value (45 and 74, via the effect law F:365-389; 80, via conjunction);
- keeps its I2 per-(value, cause) table, whose explicit totality sentence was replaced by a referral (26; see CB2-02).

**Merged or dissolved sets:**
- Row 4: the RF conjoin oracle no longer returns its own outcome set. RF:1285 reads "Conflict, veto and refusal remain predicate-bound evidence or decision annotations, never replacement verdicts".
- Row 18: the DESIGN UP-021 consumer map is deleted. SPEC:2002 says "This section owns its reason-sensitive map; consumers refer here."
- Row 40: the TICKET second debt vocabulary is deleted. `grep -F ticketed` finds 0 hits in I3, against I2 lines 240 and 257. TICKET:260 and 277 refer to Sprint Close Review.
- Row 64: the UX sprint-close list and its map are deleted. UX:509-511 refers to TICKET as "which owns the six treatment classes and their reason-sensitive assessment/decision bindings".

**Additional sets.** The full read of each member found 47 further sets that CR2's inventory did not list. Inclusion is contestable for many of them.
- Every one is inherited from rc.2 and was already present at `9bc8962`. They are therefore not an iteration 3 regression, but H2 covers them.
- Sub-evaluation grading: 2 M, 43 R, 2 U.
- The R sets reach the core only through a family preamble, a Contract-application referral or the general stop rule. The parent re-read five of them:
  - TICKET:1218-1224, "Allowed inherited-implementation classifications are:" (`carry_across` / `redundant` / `rewrite`) followed by "Unclassified inherited implementation blocks closure." Only the member preamble covers it.
  - DESIGN:910-916, "Every row must be one of:" (derived atomic / derived composition / deferred / excluded / unresolved gap). Covered only by the DESIGN:14-22 preamble.
  - DESIGN:672-696: candidate eliminated / dominated / undominated / selected / rejected / design gap. No core map.
  - SPEC:1735, "A method addition is disproportionate when it duplicates truth" (UP-014). No result referral: U.
  - RF:657-667, applicability true / false / unresolved. Bound into conjunction ("including unresolved applicability"). This one is arguably M through F:479, so it is a contestable R.
- The other 42 come from the sub-evaluation reports and were checked by quote only.
  - SPEC: 13 R and 2 U.
  - DESIGN and B: 9 R.
  - TICKET and ODD: 8 R.
  - UX, TOP and WM: 7 R.
  - RF, AC and RELEASE: 6 R, including the RELEASE residual fail-closed loci RELEASE:166-169, 231-233 and 365-367 that sit outside the named gates of RELEASE:243-254.

### The four sets H2 names

- **Sprint close: M, single owner.**
  - TICKET:365-366 "These six values classify treatment. The assessment separately evaluates" the compliance predicate.
  - TICKET:370-376 gives a five-row cause table, with "insufficient proof, unresolved requirement/applicability or missing reason | `indeterminate`".
  - TICKET:385-390 gives the decision relation for "each of the six D values".
  - TICKET:390-392: "A raw `accepted` label cannot supply its missing compliance assessment". This repairs CR3 F-1 / CR2-04.
  - UX:509-520 refines with its own item-compliance predicate and no map of its own. UX:35 says "Ticket owns sprint-close classification and eligibility".
  - Map I3-introduced; set rc.2-inherited.
- **UP-015 dispositions: M.**
  - RELEASE:630 "These are row dispositions, not interchangeable verdicts on retention."
  - RELEASE:634-639 gives a per-value semantic predicate and decision relation.
  - RELEASE:641-645 maps fulfilment / counterexample / "insufficient evidence or a missing reason" / basis / scope to the five core values.
  - RELEASE:651-656 gives the decision predicate per row.
  - `conserved` (a semantic judgement) and `intentionally removed` (an owner decision) are now separate predicates. This repairs CR2-05 / CR3 F-2.
  - Map I3-introduced.
- **Coverage statuses: S, with the predicate mapped.**
  - RF:903 "recorded coverage state used by the coverage predicate below".
  - RF:906-907 "they do not report whether the row's underlying evaluation predicate is true".
  - RF:972-985 maps the Operational Full Coverage predicate to all five core values, including "Missing causes or unsupported state labels use the core missing-reason rule".
  - CR2 row 3 was U. Repaired; I3-introduced.
- **Conjunction defined once: holds.**
  - F:426-538 is the only conjunction.
  - The RF qualification oracle now exercises it (RF:1285, quoted above). Iteration 2 had "basis mismatch … return conflict, indeterminate, or refusal"; `grep -F "basis mismatch"` finds 0 hits in I3 RF.
  - SPEC UP-021 maps mixed bases into the core. SPEC:2011 reads "mixed owner bases with no interpretable admitted composite | `invalid_basis`; retain the mixed-basis refusal diagnosis". `grep -F "cannot combine"` finds 0 hits.
  - TL:302 (Conjoin), AC:875-876 (AC-016) and WM:1091-1093 refer to F.
  - CR2-02 is closed.

### Iteration 2 rows by status in iteration 3

| CR2 rows | I3 status | I3 loci (selection) | Origin of I3 map |
|---|---|---|---|
| 1, 5, 6, 11-14, 19, 26, 41, 45, 52, 63, 65-70, 72, 73, 74, 76, 80 | M, map from I2 (unchanged, reworded or extended) | RF:456-474; AC:443-461, 477-491; IDENTITY:49-60, 398-406; GLOSSARY:32-42; DESIGN:1476-1486; B:536-544 (row 19, **not independent**: port P05 lists B#work-result); SPEC:1868-1875 (row 26, CB2-02); TICKET:798-817; RELEASE:235-254; ODD:1195-1229; UX:321-336; TOP:765-828; TOP:1143-1159 (row 74, **not independent**: port P05 lists TOP#mutable-subject-effect-relation); WM:812-822, 1072-1100 | I2 (reworded or extended in I3) |
| 7, 27, 50, 16 | M, decision predicate bound at owner | AC:468-474; SPEC:1890-1895; RELEASE:594-597; DESIGN:1532-1548 | I2 / I3 |
| 2, 10, 15, 17, 23, 25, 28-31, 34-38, 39, 42, 44, 46-49, 51, 53, 54, 58, 61, 77-79 | M, newly mapped in I3 | RF:765-776; AC:937-949; DESIGN:1373-1388, 1985-1991; B:338-340 (stop on "the exact interrupted predicate and cause"); B:840-845; SPEC:715-722, 1260-1270, 1523-1535, 1607-1616, 1946-1955, 2006-2015, 560-578, 637-658, 2658-2666; TICKET:365-394, 772-777, 944-953; RELEASE:243-254, 281-298, 467-482, 621-660; ODD:941-951, 1158-1174, 879-887, 1222-1229; WM:40-49, 1217-1223, 1264-1273 | I3 |
| 24 | M, owner moved to SPEC | SPEC:1421-1464; B:1183 "Apply [Spec's Counterexample Localization]" | I3. Repairs CR2-21 (tier defect). |
| 8, 9, 32, 62 | I | AC:817-827, 753-756; SPEC:138-144 "These are instance-declared control states. Before use, the work contract binds"; UX:199-208, 238-245 | I2 / I3 |
| 3, 60 | S | RF:903-923; ODD:1604-1623 "`open` is a lifecycle state" | I3 |
| 21 | R (was M) | B:399-423. The I2 per-failure map (I2 B:413-417) is deleted. Its "A stale or substituted basis is `invalid_basis`" conflicted with RF-012, where an established admission failure is `falsified`, so the deletion removed a conflict. Activation-side failures now refer to RF-012's map. Disposition-side failures get only "exact predicate and core mapping" (B:401-403). | I3 |
| 22 | R | B:501-517. `requires narrowing` has no decision relation | I3 partial map |
| 55 | R | ODD:254 "lawful stop, hold, gap, continuation, or completion states". No link to the ODD:879-887 stop map | rc.2 |
| 33 | R | SPEC:1272-1287. Hard stops "can falsify admissibility" (permissive), with the task predicate and an admissibility predicate mixed | I3 partial map |
| 43 | R | TICKET:864-881. No satisfied condition; relevance labels unmapped | I3 referral |
| 56, 57, 59 | R (partial) | ODD:306-321 (F_D mapped and F_H bound to the decision predicate; F_P has no failure case); ODD:479-497 (`incorporation` predicate unbound); ODD:1524-1540 (`agent error` has no core target) | I3 partial maps |
| 75 | R | TOP:574-608 `refuse_*` tags, though TOP:1015-1016 still uses `refuse_duplicate` as an outcome | rc.2 |
| 71 | D (narrowed) | TOP:771, 788, 828. CR2-19 is repaired at TOP:789-796: an explicit `falsified` line, and `partial` keyed by `unfulfilled` / `unknown` / missing reason. A new defect is CB2-06. | I3 map; defect from rc.2 |

**Distinctions under combination (oracle D8): hold.** Not independent: F#result-algebra receives ports P03 and P05.
- F:406-407 "No refinement turns failure, undecidability, non-performance or unknown effect completion into greater standing".
- F:351-354: an absent slot is distinct from a performed-undecidable evaluation and from unconfirmed execution.
- F:455 "any unknown gives unknown".
- No sub-evaluation found a standing raise.
- Guards at the owners include:
  - TICKET:390-392;
  - RELEASE:647-648 ("Satisfaction of removal or non-applicability is not a claim that predecessor meaning was retained");
  - DESIGN:1538-1539 (non-acceptance "does not itself mean falsified");
  - B:538 and 547-548 (`candidate_ready` establishes availability only);
  - TOP:779-781;
  - WM:1223-1225.

**Availability, assessment and acceptance (D9): hold, not independent at F** at F:410-416 and SPEC:1887-1888. AC:851-852 reads "satisfying `an exact candidate is available` does not satisfy `the candidate conforms` or `the candidate is accepted`".

**Status labels that decide (D10): hold where mapped.**
- The ticket status, sprint status and coverage states are declared states that feed a mapped predicate: TICKET:1434 ("not a second result algebra"), TICKET:207-209 and RF:919-923.
- Gap: TICKET:1218-1224, where a missing classification "blocks closure" with no map (see the additional sets).

### Oracle group d, item by item

| Item | Result | Where |
|---|---|---|
| D1 one owning locus per determination | Partly holds | 16 of CR2's 18 pairs closed. 6 pairs remain (M1 section). No precedence rule remains. |
| D2 placement by responsibility | Holds | The packaging README now names F and TL as owners (`authority_compressions/README.md:8-9`). No profile owns generic law found. |
| D3 generic law without an optional profile | Holds | Causal localization moved from the optional Baseline to SPEC:1421-1464 (CR2-21 closed). Transition and recovery law is at F:540-628. |
| D4 frame copies match owners | Holds | 98 of 98 excerpts are exact, and all pins match. |
| D5 a ported part takes one owning locus | Fails once (not independent) | SPEC:906-910 sits in SPEC:877-935, which receives port P04. It coexists with the rival TL:269-270 (CB2-03). Reuse (P02) has one owner. |
| D6 one core algebra; conjunction once | Holds for core and conjunction (not independent) | F:304-538. Parallel outcome sets remain rule-only (CB2-01). |
| D7 each refined value maps to one core value at its owner | Partly holds | 65 of 75 comparable sets meet it. Exceptions: CB2-01 and CB2-02. |
| D8 standing never rises | Holds (not independent) | Above. |
| D9 availability, assessment and acceptance separate | Holds | Above. |
| D10 deciding labels return through the core | Holds where mapped | Gap at TICKET:1218-1224. |
| D11 result-returning frames carry the core | Holds | All six frames carry `F#Result algebra` and `F#Result conjunction`. |

## Single ownership (M1; oracle group d)

### CR2's 18 competing-owner pairs

| CR2 finding (pairs) | I3 status | Evidence |
|---|---|---|
| CR2-02 conjunction (2) | Closed | RF:1285; SPEC:1997-1998, 2011 (quoted above). |
| CR2-03 reuse validity (3) | Closed | F:133-134 "Reuse follows the applicability rule owned by [Workspace and context]". SPEC:1581-1583 "`TICKET_METHOD.md` owns ticket-state recording and the carrier binding for reuse; [workspace and context] owns applicability of the resulting exact claim". DESIGN:1628-1631 applies the reuse relation "owned by [workspace and context]". TICKET:1020 "Reuse applies Contract application's Currentness condition", which leads to TL:130. **Not independent:** the owner F:577-585 receives port I3-R2-P02. |
| CR2-04 sprint close (1) | Closed | TICKET:365-394 owns; UX:509-520 refines. |
| CR2-06 packaging standing (1) | Closed | `authority_compressions/README.md:8-9` "Foundations and the library own shared deciding contracts; domain methods bind them". |
| CR2-07 re-pinned rc.2 bodies (1) | Closed for the sampled case | The 7 per-member bodies differ from I2 and rc.2 (body digests). AC compression:157-158 carries predicate, core verdict, performance and effects. |
| CR2-08 Baseline "disjointly" (1) | Closed | B:1711-1715 "each qualified `(Worker work-result variant, cause)` maps to exactly one core verdict"; `grep -F disjointly` finds 0. |
| CR2-09 UP-021 map in consumer (1) | Closed | SPEC:2002; DESIGN:868-895 refers. |
| CR2-10 "work state" (1) | Closed | TICKET:1474 "Work-carrier state has one authority chain" against F:130 "Work state is the current subject under construction". |
| CR2-11 "verdict" for decisions (1) | Narrowed, open | RELEASE:188 now reads "acceptance remains a decision over the exact immutable RC". RELEASE:274 still has "owner verdicts" (CB2-05). |
| CR2-12 F disposition list (1) | **Open** | F:239-240 "disposition to repair, re-enter, reject or accept" is unchanged, has no link, and differs from SPEC:1868-1875 (`local_repair`, `re_enter`) (CB2-04). |
| CR2-13 bare-label checklist (1) | Closed | The I2 DESIGN:2468-2470 question is gone. DESIGN:1503-1504 stands. |
| CR2-14 totality (1) | Closed | DESIGN:1974-1977 "permitted repair, re-entry, refusal, yielding or termination" links F#bounded-construction (F:614-619). |
| CR2-15 effect drift (2) | Closed | TOP:1153-1154 "Classify its actual observations using the single [core effect observation law]". UX:241-245 "The command binding relates each qualified message to that observation boundary". **Not independent:** the TOP effect section receives port I3-R2-P05. |
| CR2-18 TICKET debt vocabularies (1) | Closed | Row 40 merged (see above). |

**Result:** 16 of 18 pairs closed, 1 narrowed (CR2-11) and 1 open (CR2-12).

Other CR2 items:
- The precedence clause (CR2-17) is gone. B:127-129 now reads "A profile statement that contradicts its cited owner is a defective application and requires revision". A grep for `controls|prevails|wins|overrides|takes precedence|outranks` finds no rule of precedence between loci.
- The tier defect (CR2-21) is closed (row 24).
- The consistent duplicates of CR2-18 are mostly reduced to referrals:
  - TICKET:840-844 (UP-007) now links F#configuration: "Fresh context alone changes no authorship relation."
  - DESIGN:1620-1622 now says "orthogonal accounts" and links F's three.

### M1's four named questions

| Question | Owner in I3 | Result |
|---|---|---|
| Conjunction | F#result-conjunction (F:426-538) | One owner. Closed. |
| Reuse validity | F#workspace-and-context (F:577-585) | One owner with refinements. Closed (not independent: port P02). |
| Sprint close | TICKET §Sprint Close Review (TICKET:343-410) | One owner. Closed. SPEC:1173-1181 still uses its own vocabulary ("accept, paydown, escalate"; "split") without a map, but names TICKET as owner at 1183 (CB2-13). |
| Fit against adequate attention | None | **Open.** TL:269-270 and SPEC:908-910 both decide "assess actual adequacy separately" / "Attention adequacy is evaluated through actual-use evidence". Neither refers to the other. F names "Finite context and attention" only as a constraint (F:637). RF-002 (RF:362-367) decides fit only. Both texts are unchanged from I2 (TL:155, SPEC:855). This is CR3 F-3, not repaired (CB2-03). SPEC:908-910 lies in the port-P04 section, so this result is partly **not independent**. |

### Competing pairs found in I3

| Pair | Loci | Origin |
|---|---|---|
| Categorical demonstration standard | F:251-274 (full standard) against TL:360-362 (subset, no link to F). AC:883-884 sends a consumer to the subset: "Categorical claims additionally meet the library's demonstration conditions." | I3-introduced (both TL and AC lines are absent at `9bc8962`) |
| Consumer adoption ownership | RELEASE:27 "It does not own Product meaning or consumer adoption." README:61 "[Spec Method] owns Product-definition routing and consumer adoption". RELEASE:336-337 "This family chooses separate presentation and mutation, digest-bound plans and same-line downgrade refusal." SPEC:2379-2380 refers back to RELEASE#selector-and-consumer-adoption. | RELEASE:27 rc.2; README:61 I2; RELEASE:336-337 I3-introduced |
| UP-017 against UP-018 on `duplicates` | DESIGN:571-572 "A locally valid action that violates, duplicates or silently reinterprets an affected governing invariant fails this obligation." DESIGN:1367 and 1380-1381: a `duplicates` "with its required explicit disposition" satisfies lawfulness. No cross-reference. | rc.2 (RC2 DESIGN:547) |
| UP-020 cases reached only by referral | TL:296-298 "The [Spec disposition consumer] owns its mapping and conditions … the library supplies no second table." SPEC:1883-1885 "Apply [Contract application] to the assessment and its supporting results; its Result condition supplies the core verdict and conjunction". The chain terminates at TL:136-140 and F. This is not a rival decider. Explicitness at the owner is reduced (CB2-02). | I3-introduced |

**Pair count in I3:** 6, under CR2's definition (divergent content or a misnamed owner, with no referral), against 18 in iteration 2:
- from iteration 2: CB2-03 (fit/attention), CB2-04 (CR2-12) and CB2-05 (CR2-11 residue);
- introduced in I3: CB2-07 (adoption, partly) and CB2-08 (categorical standard);
- inherited from rc.2 and newly noticed: CB2-12 (UP-017/UP-018).

The SPEC sprint vocabulary (CB2-13) names its owner, so it is drift, not a pair.

## Findings

Severity is relative to C3 acceptance, on the scale in Method. "Not independent" marks findings on loci that receive a port from the Claude candidate (`PORT_ACCOUNT.json`).

| ID | Sev | Claim | Evidence (`file:line`, short quote) | Inh./Intr. | Smallest repair |
|---|---|---|---|---|---|
| CB2-01 | High (narrowed from I2) | **Single Result Algebra items 1-2 are still unmet across members.** On CR2's 79 sets, 65 are now mapped or declared, against 32 in iteration 2. The severity rests on the comparable residue alone: 9 R sets and 1 D set (rows 21, 22, 33, 43, 55, 56, 57, 59, 75 and 71), spanning B, SPEC, TICKET, ODD and TOP. It holds without the 45 contestable additional sets. Those reach the core only through a family preamble, a Contract-application referral or an unbound stop reference; all are inherited from rc.2. The requirement says a referral is insufficient where the core needs a domain map. | R item 2: "A referral to the core is insufficient when the core requires the domain to supply that mapping." F:393-394 "supplies a total, reason-sensitive map into this record". Comparable residue: B:401-403 "consumed results use their exact predicate and core mapping"; SPEC:1283 "can falsify admissibility"; ODD:254 "lawful stop, hold, gap, continuation, or completion states"; ODD:317-319: F_P has only the satisfied case; TOP:574-608 `refuse_*`; TOP:771 and 828 (CB2-06). Additional: TICKET:1218-1224 "Unclassified inherited implementation blocks closure."; DESIGN:910-916 "Every row must be one of:"; SPEC:1735 "A method addition is disproportionate when". | Sets inherited (rc.2). The maps were never supplied. | Apply the TICKET:365-394 or RELEASE:630-656 pattern at each listed owner. For a set that is not a result, declare it a recorded state with its purpose (as at RF:903-923). |
| CB2-02 | Low | **Contraction moved owner-level map sentences into referrals. Content survives, but explicitness at the owner is reduced.** Three places changed:<br>• UP-020: I2 SPEC:1702-1710 read "Insufficient evidence returns `indeterminate`, a missing material evaluation capability returns `out_of_frame` … Preserve missing causes under the core rule … a known failure survives alongside missing coverage". I3 replaces it with a referral to Contract application. TL:136-140 (item 6) retains "known failures, absent required coverage, scope/basis diagnoses"; F:329-333 and F:397-400 decide the cases; the remedy sentence survives at SPEC:1885-1887. The table and SPEC:1865 are unchanged from I2. A reader of SPEC:1868-1875 alone now finds no `out_of_frame` row and needs two hops to find it.<br>• B drift locks: the I2 map is deleted (I2 B:413-417). This removes a conflict with RF-012 but leaves disposition-side failures rule-only (row 21).<br>• RELEASE: I2:227 and I2:540-542 are deleted. F:368-370 and F:323-333 decide both cases. | SPEC:1883-1885 "Apply [Contract application] … its Result condition supplies the core verdict and conjunction". TL:136-138 "Apply the [core result and conjunction law] on the actual predicates. Retain known failures, absent required coverage, scope/basis diagnoses". B:401-403. | Introduced (I3) | Restore one sentence at SPEC:1883 naming the `out_of_frame`, `invalid_basis` and undecided cases. Give B's disposition-side lock failures a cause map, or refer them to one. |
| CB2-03 | Low (M1 open; partly not independent) | **Fit against adequate attention has two unlinked deciders and no Foundations owner.** CR3 F-3 is unchanged. SPEC:908-910 lies in the port-P04 section, so this is also oracle D5's falsifier: a ported clause coexists with a rival. | TL:269-270 "Measure context where the execution binding selects it, and assess actual adequacy separately." SPEC:908-910 "Attention adequacy is evaluated through actual-use evidence; no universal attention unit or score is required." RF:364-365 (RF-002) decides only "fits the selected actor's declared capability envelope". F:637 names attention as a constraint only. | I2-introduced, persists | Put one owning sentence in F (Workspace and context or Configuration). TL and SPEC refer to it. |
| CB2-04 | Low | **The Foundations still enumerate the UP-020 dispositions in their own spelling, with no link.** This is CR2-12, unchanged. | F:239-240 "disposition to repair, re-enter, reject or accept" against SPEC:1868-1875 `local_repair`, `re_enter`. | I2-introduced, persists | Link SPEC#proportional-disposition, or drop the list. |
| CB2-05 | Low | **"Verdict" is still used for an owner decision in RELEASE** (CR2-11 residue). | RELEASE:274 "evidence subjects, owner verdicts, and unresolved gaps". RELEASE:302 "the verdict remains attached to the old" RC. Fixed: RELEASE:188 "acceptance remains a decision". | Inherited (rc.2) | Say "owner decisions", or "the review result". |
| CB2-06 | Low | **TOP `transition_evaluation` maps an incomplete subject onto the intended-outcome predicate.** The `refused` decision comes from the precondition constraint `transition_subject_complete`. Through the constraint table it counts as falsified on a judgement whose predicate is the intended outcome. The Foundations forbid substituting a different admission predicate. | TOP:771 "refused yields `refusal`". TOP:788 "For `transition_evaluation`, bind the exact intended-outcome predicate". TOP:828 `transition_subject_complete` → "`refused` plus `refusal`". F:358-359 "a different admission predicate is not silently substituted for P". | Inherited (rc.2); not flagged in I2 | Map `refused` to `invalid_basis` or `indeterminate` on the intended outcome, or bind it to its own completeness predicate. |
| CB2-07 | Low-Med | **Consumer adoption has no clear owner.** RELEASE disclaims adoption, the README assigns it to Spec, Spec refers back to RELEASE, and an I3 sentence makes RELEASE choose adoption policy. | RELEASE:27 "It does not own Product meaning or consumer adoption." README:61 "[Spec Method] owns Product-definition routing and consumer adoption". SPEC:2379-2380 "[Selector and consumer adoption](RELEASE_METHOD.md#selector-and-consumer-adoption)". RELEASE:336-337 "This family chooses separate presentation and mutation, digest-bound plans and same-line downgrade refusal." | RELEASE:336 introduced (I3); the others are inherited | Name one owning section and make the other loci refer to it. |
| CB2-08 | Low | **The categorical demonstration standard has two loci, and AC routes consumers to the weaker one.** TL:360-362 omits per-layer preservation, licensing laws and evidence classes (F:263-272), and does not link F. | F:251-274. TL:360-362 "declare the objects, arrows, equality, identities and composition and discharge the laws at that domain". AC:883-884 "Categorical claims additionally meet the library's demonstration conditions." | Introduced (I3) | Reduce TL:360-362 to a link to F#orthogonal-descriptions, and point AC:883 at F. |
| CB2-09 | Low (not independent) | **The build-tenant binding owner is still incomplete** (CR3 F-4). It omits R item 2's "including any required human decision" and item 4's authority, independence, failure and recovery conditions, and has no link to the categorical standard. | SPEC:877-935 is byte-identical to `9bc8962`. SPEC:898-901 covers author, actor and kind. Human decisions appear only at SPEC:1840 "does not weaken direct-human acceptance". | I2-introduced (port P04) | Add one sentence at SPEC:903-911 naming those conditions and linking F#orthogonal-descriptions. |
| CB2-10 | Low | **The tenant's own binding still lacks** units for time and spend, a declared process boundary, the reviewer actors and their family, per-call and aggregate limits, and failure assumptions (CR3 F-5 residue). | DES:13-15 "wall time and CLI spend measure the declared process boundary" (the boundary is never declared). DES:82-87 adds the quantity separation but no units. | I2-introduced, persists | Add units (s, USD, bytes), the boundary, the actors and limits, and known failure modes at DES §Binding. |
| CB2-11 | Low (associativity part not independent: F#result-conjunction lies in port P03's scope) | **Two categorical-evidence gaps remain.** The associativity claims carry no argument or evidence class (CR3 F-6), and functorial preservation is not named as a third distinct claim (CR3 F-9). | F:518-520 "the conjunction precedence is associative, and the effect join over normalized disjoint parts is associative". F:270-271 requires an evidence class. F:257-259 lists conformance and two equivalences only; R §Categorical item 4 also lists "functorial preservation". | Introduced in I2, persists | Add the two-line argument labelled "mathematically argued", and add "functorial preservation" to F:258. |
| CB2-12 | Low | **UP-017 says an action that "duplicates" an invariant fails; UP-018 says a disposed `duplicates` is lawful.** Neither refers to the other. | DESIGN:571-572 "A locally valid action that violates, duplicates or silently reinterprets an affected governing invariant fails this obligation." DESIGN:1367 and 1380-1381: `duplicates` "with its required explicit disposition" satisfies lawfulness. | Inherited (rc.2 DESIGN:547) | Qualify DESIGN:571 as "an undisposed duplicate", or refer it to UP-018. |
| CB2-13 | Low | **A consumer uses its own sprint-close vocabulary without a map.** It names TICKET as owner. | SPEC:1180 "The work must be split, escalated," with accept / paydown / escalate at 1173-1181. SPEC:1183 "`TICKET_METHOD.md` defines the sprint and ticket mechanics." TICKET:356-363 has six values and no `split`. | Inherited (rc.2) | Use TICKET's six values, or map them at SPEC:1173. |
| CB2-14 | Low | **Return claims overstate single ownership (see the claims table).** The integration check's "unique/disjoint ownership" concerns authored account contributions, not determinations in member text. | `RULE_ACCOUNT.md:142-143` "verifies source pins, unique/disjoint ownership". `SEMANTIC_INTEGRATION_CHECK.json` has `"independent_fidelity": "unassessed"`. RET:30-33 "Shared contracts own recurring binding, composition, projection and constraint-surface decisions". | n/a (evidence claim) | State the scope of the check. Cite CB2-03, CB2-07 and CB2-08 as open owner pairs. |

## Closure of H2 and M1

**H2 (one result algebra across members): not closed; substantially narrowed.**

| Part-A condition | Result |
|---|---|
| Every result-value set maps value by value, or is declared a recorded state with purpose | Not met. 65 of 75 comparable sets meet it; 10 do not. Further rule-only sets exist outside CR2's inventory (CB2-01). |
| No set relies only on a general rule | Not met. 9 comparable sets, plus most of the additional sets (CB2-01). |
| Sprint close and UP-015 covered | Met (TICKET:365-394; RELEASE:621-660). |
| No two sections decide the same question | Met for result values in the comparable set: the competing sprint, UP-021, RF conjoin and Baseline maps are gone. Two sets remain pairs: CB2-05 (wording) and CB2-12 (UP-017/UP-018 on `duplicates`). UP-020's uncovered cases are now reached only by referral (CB2-02). |

**M1 (second deciders): not closed.**

| Question | Result |
|---|---|
| Conjunction | One owner (F:426-538). |
| Reuse validity | One owner (F:577-585, port P02, not independent). |
| Sprint close | One owner (TICKET:343-410). |
| Fit against adequate attention | Still two unlinked deciders, TL:269-270 and SPEC:908-910, and no Foundations owner (CB2-03). Partly not independent: SPEC:908-910 lies in the port-P04 section. |

Six pairs remain in all (M1 section). Two were introduced in I3: the categorical standard (CB2-08) and adoption (CB2-07).

## Return claims tested

| Claim | Verdict | Evidence |
|---|---|---|
| RP:38 and RET:56-57 "Six current task views contain 98 exact excerpts" | Holds | 98 of 98 excerpts are byte-exact after relocation, and 11 of 11 owner pins match (`cb2tools/frames.out`). |
| RP:39 "32 compression pins" | Holds | 25 front-matter pins plus 7 `source_digest` pins match. The bodies are regenerated: CR2-07 is closed for the sampled AC case. |
| RET:30-33 "Shared contracts own recurring binding, composition, projection and constraint-surface decisions. Domain owners retain their particular predicates, exceptions and authority." | Holds in the main; falsified in part | Contract application is consumed by 13 members and Faithful projection by 12 (`grep -c`). Two deciders remain for fit/attention (CB2-03) and for the categorical standard (CB2-08), and adoption ownership is circular (CB2-07). |
| RET:34-36 "Executive, Worker and Reviewer remain applicable configurations rather than universal actor requirements" | Holds | F:632-640 and F:648-650. |
| RET:143 "I3-02 … complete independent duplicate-owner and practical-reduction assessment remains open" | Holds as a limit | This review finds 6 remaining pairs (M1 section). |
| RET:144 "I3-03 domain results: Source-specific predicates/data and shared-result bindings represented" | Holds for most sets, not all | 65 of 75 comparable sets hold; the exceptions are CB2-01. The stated hedge ("bounded checks do not prove all possible domain instances") is accurate. |
| `RULE_ACCOUNT.md:142-143` "verifies … unique/disjoint ownership" | Holds only for the account | It checks disjoint authored contributions over 697 units (`integrate_semantics.py:1` "Integrate disjoint authored semantic contributions"). It does not test owner uniqueness in the member text (CB2-14). |
| DES:99-101 "removes a duplicate deciding body only after every unique condition has a successor owner" | Not contradicted; explicitness reduced | Every deleted UP-020 clause has a successor at TL:136-140 or F, though only by referral (CB2-02). |
| RET:156 "I3-15 categorical worked join: Reserved and not selected" | Holds | F:273-274; no member asserts a worked join. |

## What holds

- **One core, unchanged in shape** (not independent: ports P03 and P05):
  - five verdicts, three performance values and six effect values, with legal pairs (F:304-424);
  - one conjunction, effect join and declared-operator rule (F:426-538);
  - TL refers to it throughout and supplies no second algebra (TL:93-94, 136-140, 285-290, 302-308).
- **Large owner-level mapping work.** Roughly 30 sets gained maps in I3, including:
  - sprint close, UP-015 and the coverage predicate;
  - UP-021, now with a single owner and a missing-reason row (SPEC:2006-2015);
  - SPEC triage, delta, ambiguity, progress and fixture sets;
  - RELEASE gates and cohort;
  - TICKET admission and obligation dispositions;
  - ODD gap, next-action and closure-projection sets;
  - WM null-peer and assurance sets.
- **The decision rule is used to separate assessment from authority.** TICKET:381-394, RELEASE:651-656 and DESIGN:1536-1539 each keep the assessment and the decision as separate predicates.
- **16 of CR2's 18 owner pairs are closed.**
  - The precedence rule is gone.
  - Causal localization now has a generic owner (SPEC:1421-1464), which repairs the tier defect.
  - UP-007 refers to F#configuration.
- **Groups e, f and g hold in content** (sections above). The build-tenant owner and the tenant's own binding still have the gaps in CB2-09 and CB2-10. The categorical evidence gaps are CB2-08 and CB2-11.
- **Frames are exact projections carrying the core.** The ordinary work entry routes by task to them.

## Limits

- **Delegated reading.** Five bounded read-only sub-evaluations read every member except F and TL in full, each with the schema and rules above.
  - The parent re-read every locus cited in the findings, the four named H2 sets and five of the 47 additional sets.
  - Other inventory loci were checked by quote with `grep -F`, not re-read in context.
- **Inclusion and grading are contestable.**
  - The thirteen parent overrides are listed in Counts. Under the sub-evaluations' stricter reading the comparable count is M 46, R 22.
  - Many of the 47 additional sets could be read as triage, kinds or treatments. CR2 excluded some similar ones, and CR2's own sweep was less complete, so the "additional" figure is not an iteration 3 regression.
- **Independence.**
  - The reviewer and the oracle author are both Claude-family activations.
  - Results on F#workspace-and-context, F#result-algebra (ports P01, P02, P03, P05), SPEC#what-how-and-work-carriers (P04), the B work-result map and the TOP effect relation are marked not independent where cited.
  - The Claude candidate was not read.
- **Not assessed:**
  - conservation dispositions (H3);
  - actual use (H4);
  - the a_c interpretation (M5);
  - identity (M6);
  - the 89-member package beyond frames and compressions;
  - templates, schemas and plugin skills (beyond the stdo-work acquisition route).
- **Tools.** The frame check is the reviewer's tool, kept outside the subject (`scratchpad/cb2tools/framecheck.py`).
- **Subject note.** At `3aaa2f2`, `qualification/C3/iteration-3/RETURN.md` still describes the earlier repair checkpoint ("Construction remains incomplete"). RP:3-8 places the return and qualification record at `939ce0c`, so return claims were tested there. This is a recording-order note, not a finding.
