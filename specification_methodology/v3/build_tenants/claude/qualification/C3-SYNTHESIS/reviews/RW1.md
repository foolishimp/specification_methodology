# RW1: Review Of The Claude Tenant Design At f7851aa

Status: same-family working check, not acceptance. Reviewer: a fresh Claude context (activation RW1) that did not write the subject. Author of the subject: activation W1 (Claude) with the Executive's D1 `local_repair` edits. Same-family exception: ledger default 2 ("every review in this rebuild is a same-family working check ... none counts towards acceptance"). Acceptance review stays cross-family and open. No repair made.

Subject: `git show f7851aa:specification_methodology/v3/build_tenants/claude/design/{CONSTRUCTION_BINDING,CROSS_SYNTHESIS,DOCUMENT_STRUCTURE,README}.md`.

Sources, read before the subject, all at `f7851aa`: `specification/PRODUCT.md` (P), `specification/requirements/README.md` (R), `qualification/C3-SYNTHESIS/EXPECTATIONS.md` (the oracle, E-*, PT-*), `qualification/C3-SYNTHESIS/LEDGER.md`. Port sources: `build_tenants/codex/` at `31f28f9` in the main checkout.

## Expectations (recorded before opening the subject)

Q1, CONSTRUCTION_BINDING (R §Build-Tenant Binding 1–6; P §Build-Tenant Binding; E-3-1..E-3-6):

- X1.1 It declares a computational calculus as executable operations, their composition and permitted transformations, with effects and resource behaviour (P §Build-Tenant Binding ¶2), and binds it to a concrete execution environment (stack, human process or mix) inside the existing design surface, not a new carrier (R 1; E-3-2).
- X1.2 It names operations, composition laws, effects, resource measures and operational assumptions material to conformance; each resource measure has a unit and a measurement boundary (R 3; E-3-4). Expected measures, from P §C3 Limits: context in bytes measured before reading, wall time, spend; human effort and communication where an obligation needs them.
- X1.3 Author identity, actor identity and operation kind are three separate coordinates. Authorship (Claude) does not select the environment; a person doing an operation does not make it human adjudication; owner decisions stay the product owner's (R 2; P ¶3; P §Source Project Construction "Author identity alone selects no execution environment"; E-3-3).
- X1.4 Conformance evidence covers meaning, constraints, authority, independence, failure and recovery; nothing is weakened for convenience (R 4; E-3-5). Any categorical claim is marked a hypothesis or carries the demonstration standard.
- X1.5 It does not claim a calculus per language or team; a_c structural validation is not cited as execution conformance; a_c does not select the executor (R 5–6; E-3-6).
- X1.6 Falsifiers: a resource figure without unit or boundary; byte fit cited as adequacy (E-2-3); a role name given as the source of a grant (E-2-6); the builder's (2.5.1-rc.2) operations presented as the successor method's law.

Q2, configuration (R §Bounded Transitions 4; P §Construction And Context Management ¶3–4; RF-009; E-2-4..E-2-7; N-3):

- X2.1 Allocation is derived from the operations, their dependencies, actor capabilities and assurance needs, and explains resource limits and failure assumptions.
- X2.2 Executive/Writer/Reviewer are presented as one configuration under the installed builder (P §Construction Authority), not as generic method; alternatives (one frame, peer, adaptive) are not excluded.
- X2.3 Decomposition, communication, authority and evaluation dependency stay distinct; frame names grant nothing; independence rests on authorship and evidence conditions, not on a fresh context (E-2-5..E-2-7).
- X2.4 Falsifiers: the role set stated as required for all work; "optimal" with no objectives or comparison scope (E-7-15); a fresh same-author context counted as independent.

Q3, CROSS_SYNTHESIS (P §Cross-Synthesis; P §Development Isolation "Porting reads"; P §C3 Independence; P §Open Owner Decisions bullet 2; PT-1..PT-10):

- X3.1 Each port names a source path and line range in `build_tenants/codex/` at `31f28f90c4a9b15243d84630fc4799024a9cd7ac`, read by `git show`, not a working tree; the range matches the named content at that commit (PT-1).
- X3.2 Each port names one receiving member and section in this line and the disposition it supports; it sits in one member's frontier cone (PT-2, PT-3).
- X3.3 The review plan compares each port with its peer source and with the previous release; peer fidelity is not counted as conservation (P §Cross-Synthesis ¶3; PT-5).
- X3.4 Independence: the Reviewer is never the author of the subject; default is a different model family; a same-family Reviewer is a declared exception with reason and marking (P §C3 Independence). For ports, the peer family is the source author, so cross-family review of a port collides with "no assessment of its own authorship"; the design must leave this to the product owner and not accept a port-bearing cone before that ruling (P §Open Owner Decisions bullet 2; PT-9; N-10).
- X3.5 No link to `build_tenants/codex/` remains in ported text; terms resolve in this line (PT-7); ported result values map into this line's core (PT-6).
- X3.6 Expected falsifiers: a wrong or shifted line range; a port with two receiving sections; the open owner decision on port review settled by the design.

Q4, DOCUMENT_STRUCTURE D1–D8 (R §Single Ownership 1–7; R §Single Result Algebra 1–7; E-4-*, E-5-*; ledger D1 ruling):

- X4.1 Each decision names exactly one owning locus (one section of one member) per question; other loci refer to it or refine it with a value map (R 1, 3, 7).
- X4.2 Tier placement: Foundations own what holds for any method (result algebra, frames, bounded activation, work state, evidence, authority); Spec Method owns build-tenant binding, work carriers, triage, change classes, release mechanics; profiles own only their bindings (frame catalogues, Executive law); guides own conventions only; packaging owns no determination (R 2; P tier table).
- X4.3 No precedence rule substitutes for an owner (R 7; N-11).
- X4.4 D1 as revised: five core values (RF-012's), owned in Foundations; one conjunction over the core; non-performance kept distinct without a sixth value, by keeping "planned assessments with no closed result" and "uncovered coverage" as separate inputs to conjunction; work-step `incomplete` maps to `falsified` only for the predicate "a candidate is available"; candidate availability never maps to fitness or acceptance; unknown effects never map to no-effect or completed; predicate and domain outcome travel with the core value (R §Single Result Algebra 1–7; E-5-1..E-5-9).
- X4.5 Points to probe in D1: whether "not performed has no closed result" is consistent with R 1 ("results of ... work ... are stated in it or as refinements of it") and R 3 bullet 3 (not performed distinct from undecidable); whether AC-007 refusal outcomes and UP-015/coordinator dispositions (ambiguity A3) are mapped or explicitly placed outside; whether stops and effects (P §Result Algebra list) are each mapped; whether `incomplete` → `falsified` risks merging non-performance with failure under conjunction (E-5-7).
- X4.6 Expected falsifiers: a sixth value surviving anywhere in the design after the ruling; two loci defining conjunction; an effect-unknown value mapped to `satisfied`.

Q5, writing (installed WRITING_GUIDE; workspace rules; owner preference recorded in auto-memory):

- X5.1 Every abbreviation or term is introduced with plain context on first use.
- X5.2 Present-tense design statements; no narration of how the design came about ("W1 proposed", "earlier", "now") in design text; history belongs in the ledger.
- X5.3 No promotional or floral language.
- X5.4 The person is named by role, "the product owner", not by name.

## Results

Citations: `CB` CONSTRUCTION_BINDING.md, `CS` CROSS_SYNTHESIS.md, `DS` DOCUMENT_STRUCTURE.md, `RM` design/README.md, all at `f7851aa`. `P` and `R` lines are at `f7851aa`. Codex lines are at `31f28f9` under `build_tenants/codex/`. Candidate member lines (`FOUNDATIONS.md`, `ACTIVATION.md` and others) are at `f7851aa` under `build_tenants/claude/standards/`; the working-tree edit to FOUNDATIONS.md was not read.

| Q | Result | Evidence | Findings |
|---|---|---|---|
| 1. CONSTRUCTION_BINDING: calculus, environment, coordinates (R §Build-Tenant Binding 1–6) | falsified (material) | R 1: CB:49–65 bind the requirements calculus; CB:67–167 the calculus; CB:169–181 the environment. R 2: CB:31–47 and CB:181 cover the environment and the human process. R 3: CB:71–82 operations, CB:89–117 laws, CB:119–146 resources with units and boundaries, CB:148–167 assumptions. R 4: CB:183–194. R 5–6: CB:196–204 and CB:163–164. The a_c pin at CB:178 matches A_C_DEPENDENCY.md:46–52. | F1, F2, F3 material; F4–F8 minor |
| 2. Configuration derived, no generic role inventory (R §Bounded Transitions 4) | falsified (minor) | CB:206–229 derive the allocation from operations, dependencies, actor capabilities and assurance. The figures check out: the members total 1,172,611 B and DESIGN_MODULE is 140,848 B. CB:231–241 give the allocation with reasons; CB:248–256 keep the four relations distinct, and the names confer no authority. CB:258–262 call a peer configuration lawful in general and attribute the Executive arrangement to the C3 contract. No fixed role inventory is presented as generic method. F9 (a chosen limit presented as derived) and F10 (an omitted item from R 4) are minor counterexamples. | F9–F11 minor |
| 3. CROSS_SYNTHESIS: sources, receiving owners, review plan, independence | falsified (material) | Every Codex range checks out at `31f28f9`: TL:93–112 (93/95–98/100–106/108–112), TL:27–57, FOUNDATIONS:48–51, :55–65, :128–162 (130–132, 155–156), :249–258, WORK_RECOVERY:1–21/25/27 and :10–17, refresh_views.py:1–18, :15–18, :44–66, :54–55, SKILL.md:18–39 (28–32), finite_check.py:1–95 with sub-ranges 12–13, 34–56, 50–55, 57–61, 61–63, 76–80, 86–93. The six parts are nominated items 2–6 of the cross-assessment §8. Candidate references check out: EVALUATION.md:184–188, FOUNDATIONS.md:299–322 and :379–382, PRODUCT_DEFINITION.md:412–443, bounded_step.py:21–24 and :58–61. Each part names a receiving owner (CS:31–36). The slug claim (CS:89–93) holds for every in-scope heading; the only 3 differences are level-1 headings inside fences. The review plan (CS:106–116) and independence fail as stated in F12–F14. | F12, F13, F14 material; F15–F18, F29 minor |
| 4. DOCUMENT_STRUCTURE D1–D8: one owner per question, tiers; D1 against the Single Result Algebra Requirement 1–7 | falsified (minor) | Each D names one owning section, in the tier R §Single Ownership 2 assigns: D1 F, D2 F, D3 F with the concrete configuration in Pf, D4 SM, D5 F format with family tables at their owners, D6 SM, D7 F refined by SM, D8 F. Packaging and GLOSSARY own nothing (DS:77–82). D1 against the requirement: item 1 DS:91–98; item 2 DS:124–126; item 3 DS:107–108, :116–123; item 5 DS:127–130; item 6 DS:91–94, :109–113; item 7 DS:262–264. AC-007 already refers to the core (AXIOMATIC_CALCULUS.md:450–464) and stops are in the core (ACTIVATION.md:284). No sixth value remains anywhere in the subject; D1 matches the ledger ruling (LEDGER.md:97–99). D1 contradicts none of items 1–7, but it leaves parts unspecified (F19–F21). The minor counterexamples are F22 (E-4-1, E-4-6), F24 (E-4-3), F25 (E-4-1) and F19 (E-5-3, a value with no stated core mapping). | F19–F26 minor |
| 5. Writing | falsified (minor) | No floral language. No personal name: the only "jim" is in filesystem paths (CS:20, CB:176). History narration, contrast framing and undefined shorthand appear as stated in F27–F28. | F27, F28 minor |

## Findings

### Q1

- **F1 (material). Author identity is bound to the tenant and its model family.** CB:35 makes the tenant the author. CB:44–47 then make every same-family context "a different actor with the same author". P:367 separates "never the author of the subject" from the same-family exception, and ledger default 2 (LEDGER.md:49) reads authorship at the level of the Writer activation. By the design's definition, its own allocation at CB:238 ("one Reviewer per subject, same family") assesses its own authorship, which the Reviewer frame forbids (P:164). Repair: define a subject's author as the Writer activations that produced it, plus the source author of any port. State that this tenant treats same-family reviews as working checks by its own choice.
- **F2 (material). The authority evidence omits that the ledger stands in for the pen's ticket record.** The Record operation (CB:81), composition law 1 (CB:91–94), the Executive's role changes (CB:173) and the ledger Writer (CB:240) let the next activation start once the tenant ledger records a decision. P:212–222 says the pen records each disposition before the next activation, and that no disposition exists until it does. P:354 has the pen record the decision before the next activation starts. P:356 has the pen record a role change before the effect. P:375 has the product owner name the Executive and Reviewer actors. CB:190 claims Authority without stating this variance or its basis, the owner's instruction at LEDGER.md:7–11. Repair: add to CB §5 Authority that ledger entries are interim records under that instruction, that a disposition or role change has no effect under P until the pen records it, and that no `accept` is made before then.
- **F3 (material). A spend limit is required only for headless runs.** CB:141–142 require one only "for headless runs", "as the C3 Limits paragraph requires". P:369 says "Every activation declares its limits: context in bytes, wall time and spend". The host's inability to report spend does not remove the obligation to declare a limit (R 4). Repair: declare a spend limit for every activation, the Executive included, and record "unavailable" where spend is not measured; or route the gap to the product owner as a named variance.
- **F4 (minor). Member acceptance is given to the product owner.** CB:181 and CB:192 give the product owner "member and checkpoint acceptance". P:172–179 grant member `accept` to the named Executive and reserve the checkpoint to the product owner. Repair: state that member `accept` is the named Executive's disposition and that none is made until the product owner names the Executive (P:375).
- **F5 (minor). Operations with effects outside the territory are missing.** The operations table (CB:71–82) omits setup (branch, worktree, sparse checkout) and merging `main` inward. Both change files outside `build_tenants/claude/`, against CB:190 "every effect lies in a declared territory", and the ledger records both (LEDGER.md:62, :74). Repair: add a Setup/Merge-inward operation with its effect and precondition, under P:196–198.
- **F6 (minor). A result value has no stated owner.** CB:84–87 say the installed release owns the meaning of the values the ledger Writer returns. Record returns `recorded` (CB:81), which is not an installed value. Repair: have Record return the installed work-result values, or drop the claim for Record.
- **F7 (minor). A resource measure has no unit.** "Human decisions: count and elapsed time" (CB:127) gives no unit for elapsed time. Repair: state the unit, for example minutes from the ledger's UTC timestamps.
- **F8 (minor). The evidence table has no row for meaning.** CB:188–194 have no row for "required meaning and constraints", the first clause of R 4. Repair: add a row naming the Review results against criteria 1–6 and the 31 discriminators, and the Run records for criterion 4.

Observation (no finding, ambiguity A1). The binding covers this construction and the fresh-actor use under test (Run). It declares no execution environment for the method the candidate expresses when a project adopts it. Under A1 that absence fails only on a product owner ruling.

### Q2

- **F9 (minor). The concurrency limit is presented as derived.** CB:150–154 and CB:261–262 say the observation at six to eight activations "excludes" more than three. It does not exclude four or five; three is a chosen limit. Repair: label three as a choice, with its reason.
- **F10 (minor). The reconfiguration rule omits two required items.** CB:266–267 omit "material dependencies" (R 4) and effects of uncertain completion (E-2-5); "uncommitted effects" is narrower than both. Repair: add both.
- **F11 (minor). The port count is inconsistent.** CB:211–212 say "five named parts"; CS:31–36 list six (item 4 of the nomination is split into parts 3 and 4). Repair: say six parts from five nominated items.

### Q3

- **F12 (material). The Reviewer is not assigned to compare adapted parts with their source.** P:259 requires the Reviewer to compare each part with its source and with the previous release. P:361 (criterion 2) requires that comparison to be independent of the author. CS:108–111 give a byte-for-byte check, with no named actor, for verbatim text only. CS:64–66 cover parts 2 and 3 by the receiving Writer's own diff, which is evidence supplied by the author (E-8-7). Parts 1 and 4, part 5's generator and acquisition rule, and part 6 have no stated source comparison. Repair: the Reviewer of each receiving cone compares every part, verbatim or adapted, with its source by `git show` at `31f28f9` and with the predecessor, and records both comparisons.
- **F13 (material). The port-review plan does not mark the product owner's decision as open.** CS:108–113 assign the port to a Claude Reviewer and the surrounding text to Codex, citing ledger default 3. P:376 leaves the review of a ported part to the product owner, decided before the first cone that contains a port is accepted (PT-9, N-10). Adapted sentences are written partly by both families, and under CB:44–47 no planned reviewer is independent of them. Repair: add one sentence. The plan yields working checks only, and acceptance of any cone with a ported part waits for the product owner's ruling on how ported parts, adapted sentences included, are reviewed.
- **F14 (material). The ported generator's section boundary ignores code fences.** Part 5 adapts the generator from `refresh_views.py:44–66`. Its rule (lines 52 and 57) ends a section at the next `#`–`######` heading of equal or higher level, including headings inside fenced blocks. CS:89–93 check only that slugs agree, and the adaptation does not mention fences. No generator exists at `f7851aa`: `qualification/instruments/` holds only `ROUTE_CARD.md` and `bounded_step.py`. The finding is therefore against the adaptation the design states. Applying the Codex rule to the members at `f7851aa` would cut nine sections short without notice:
  - REFERENCE_FRAME.md:667 §11, ending at fenced line 704;
  - REFERENCE_FRAME.md:773 §13, ending at line 787;
  - REFERENCE_FRAME.md:694, :780 and :824;
  - POSTING_GUIDE.md:91, ending at line 104;
  - TICKETS.md:627, :629 and :1111.

  The section digest would be computed on the shortened text, so regeneration would not detect the loss. DS:261–262 ("a copy never drifts from its owner") would then be false (R §Single Ownership 4; E-7-7). Repair: the generator ignores fenced code when it finds headings and section ends, and the adaptation states this.
- **F15 (minor). Some coordinates are imprecise.**
  - Part 4: lines 251–254 hold the 𝒜/ℐ/𝒞_H naming sentence, and line 254 starts mid-sentence, so the split into 249–253 and 254–258 does not fall on a sentence boundary.
  - Part 5 claims "whole file … schema verbatim" but lists 5 of the manifest's 7 top-level keys. It omits `source_linked_summaries`, `view_subject_binding`, `initial_derivation_commit` and `initial_derivation_commit_standing`.
  - Part 6 omits `program.json` and `program-mutant.json`, which `finite_check.py:78–79` reads.
  - Part 3's second instance (TL:27–57) has no receiving locus.
  - CS:87–88 ("names the owning section and its digest") disagree with DS:258–259 ("that member's digest"). The Codex `Source:` lines carry the member digest.

  Repair: correct each item.
- **F29 (minor). CS:89–93 describe a tool that does not exist as though it does.** CS:89–93 say in the present tense that "the generator uses one rule and refuses an absent or duplicated heading". `qualification/instruments/generate_frames.py` is absent at `f7851aa`. Repair: state these as requirements on the generator to be written.
- **F16 (minor). The design does not name each part's member cone.** P:259 lets a part enter "only as a named contribution inside one member's frontier cone". CS:31–36 give no cone per part. Part 5's generator and manifest and part 6 are tooling, not member text, and CS:115 anticipates parts with no predecessor row. Repair: name the member restatement whose cone each part enters, or state that the tooling parts are not candidate law.
- **F17 (minor). The rule against peer links is missing.** No sentence says that ported text keeps no link to `build_tenants/codex/` and that every term resolves in this line (PT-7). Repair: add that sentence to CS §Review of ported text.
- **F18 (minor). A rule is attributed to a requirement that does not state it.** CS:72–73 and DS:189–190 attribute "a tier-1 member must not depend on a tier-2 owner" to Single Ownership item 2. Item 2 assigns owners by tier; it does not state that rule. Repair: cite the tier order in P §Method Structure (P:51–55), or state the rule as this tenant's reading.

### Q4

- **F19 (minor). D1 does not name the core value of a conjunction with a gap.** It says such a conjunction is "never `satisfied`" and that the record names the gap (DS:111–113). It gives no core value, so item 6 ("defined once over the core") is incomplete, and how the gap kind survives combination depends on that missing value (A2). Repair: name the core value a conjunction returns for each gap kind, and carry the gap kind as the domain outcome under item 4.
- **F20 (minor). D1 leaves out item 4's general rule and some mappings.** What FOUNDATIONS §4 "Results" owns (DS:91–94) does not include item 4's general rule: the original domain outcome travels with every core value, and a mapping never owns domain meaning. The constraints map `candidate_ready` and `incomplete` but not `refused`, `re_entry_requested` or the coordinator dispositions. Repair: add item 4 to the owned list and name the mapping for the remaining work-result values and dispositions.
- **F21 (minor). D1's evidence is misdescribed.** DS:101 says `FOUNDATIONS.md:3–5` claims the result algebra. Those lines claim "the algebra of composition and conservation" and say later documents add no definitions. The result algebra is claimed at `ACTIVATION.md:3–5` and contradicted at `:6–8`. ACTIVATION is already tier 1 (DS:46), so item 1 does not itself require the move. Repair: correct the citation and state the move as a choice.
- **F22 (minor). D3 names no owner between two loci.** RF-009 (`REFERENCE_FRAME.md:195–203`) and the new ACTIVATION §1 configuration law (DS:145–149) both decide that decomposition, authority, configuration and evaluation dependency are distinct. D3 names no owner between them (R §Single Ownership 7). Repair: make one the owner and have the other refer to it.
- **F23 (minor). The disposition record names two owners and the wrong governing law.** DS:233–236 say the values are owned by RELEASE §9 "and, for this product, by the common successor requirements". RELEASE §9 is a candidate member, and CB:63–65 say candidate members do not govern the construction. Repair: name the installed UP-015 and the common Successor Disposition Requirement as governing this construction's records, and RELEASE §9 as the candidate's restatement.
- **F24 (minor). D7's refinement cannot map back to its owner.** D7 gives FOUNDATIONS §2 only the import rule (DS:186–190), yet requires PRODUCT_DEFINITION §5 to "map its four relation kinds back to the owner" (DS:190–192). Translation, equivalence and disambiguation have no counterpart there, and `PRODUCT_DEFINITION.md:436` reads "with Semantic Import defined here" (E-4-3). Repair: either FOUNDATIONS §2 owns the four-kind relation law, or PRODUCT_DEFINITION §5 owns three kinds and refers to FOUNDATIONS §2 for import.
- **F25 (minor). D8 gives item 4's distinction two owners and leaves item 6 unplaced.** DS:194–196 give FOUNDATIONS §4 item 4, including "conformance, equivalence and functorial preservation are distinct claims". DS:197 gives EVALUATION §6 the ladder that draws the same distinction, and CS:34 says FOUNDATIONS §4 refers to it. Item 6 has no locus. That is lawful while the capability is unselected (P:107), but D8 does not say so. Repair: assign the distinction to one locus, and note that item 6 waits for the product owner's selection.
- **F26 (minor). D2 fixes the owner but not the rule.** D2 fixes the locus but leaves the direction as a "recommended reading" (DS:140–143). Repair: state the rule, or name the activation that fixes it.

### Q5

- **F27 (minor). Design text narrates history and uses contrast framing.**
  - CB:150–154: "In the first pass, six to eight open activations …";
  - CB:130: "stated rather than hidden";
  - CS:25 and CS:92: dated verification events;
  - DS:114: "without a sixth core value";
  - DS:125: "maps today";
  - RM:19–23: "now settled", "now governed".

  Repair: state the current claim, move events to the ledger, and cite it.
- **F28 (minor). Shorthand is used without definition.** UP-004 (DS:48); UP-012 and UP-013 (DS:55); STDO-SURFACE-001 (DS:56); Prime (DS:72); H1 (DS:197); 6A to 6C (DS:209); RC (DS:228); 𝒜, ℐ and 𝒞_H (CS:34); MCP (CB:175). Repair: add a short gloss at first use.

Outside the subject (note only): candidate `FOUNDATIONS.md:23` reads "Jim's decision as Product authority". D6 relocates that text, and the receiving Writer should write "the product owner's decision".

## Closure

Every result uses one rule: a question is `falsified` if any finding is a counterexample to it, and the result records the highest severity. Closed result: Q1 `falsified` (material), Q2 `falsified` (minor), Q3 `falsified` (material), Q4 `falsified` (minor), Q5 `falsified` (minor). Material: F1, F2, F3, F12, F13, F14. Minor: 23.

Blocking is judged against the next activations that depend on this design. Wave A is editing members under D1–D8, and no finding makes that text impossible to repair later, so none is blocking. Gates:

- F14 must be repaired before any frame is generated.
- F1 and F13 must be repaired before any acceptance review is planned or any cone containing a port is accepted.
- F2 and F3 must be repaired, or put to the product owner as variances, before the binding is cited as conformance evidence.

This is a same-family working check, not acceptance. No repair was made and no git state was changed.
