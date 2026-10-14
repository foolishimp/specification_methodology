# REVIEW: Critical review of the frozen Codex v3 candidate

**Author**: Dimitar Popov
**Date**: 2026-10-13T23:57:54Z
**Addresses**: the Codex tenant candidate `build_tenants/codex/`, product source frozen at `9bc8962e44aff2cd1dc29a9bac95356cdccf7cdd`, qualification evidence at `3ad1fca31dc93ba0847bbbbf308312a554daa1f6`; the common specification at the same commit (identical to `main` at `a9adce2`)
**Status**: Complete for the frozen subject. The expectations below were committed (`dbf1ef1`) before the subject was opened.
**Updated**: 2026-10-14T00:20:22Z (findings)

## Authority and independence

The product owner asked for this review on 2026-10-14: "ok i want you to do a critical review of the v3/codex candidate", and named its subject: "frozen candidate as V3 iteration 3 work has commenced". The review reads the candidate at the frozen commits above, not the Codex worktree, where iteration 3 is in progress. It repairs nothing.

The reviewer is Claude, a different model family from the candidate's author, Codex. Two limits on that independence:

- Claude authored the competing candidate, which it finished building the night before this review.
- Any part of the Codex candidate ported from the Claude candidate is Claude's authorship. A finding on such a part is marked as not independent.

## Expectations, recorded before opening the subject

Sources: the common specification at the frozen commit, and the installed predecessor `stdo://releases/v2.5.1-rc.2/`. The detailed oracle is the expectations file written for the Claude line's rebuild: [EXPECTATIONS](assets/20261013T235754Z_codex_review/EXPECTATIONS.md), copied unchanged from branch `tenant/claude/c3-synthesis` at commit `697fe6f`, 87 expectations plus an amendment. Its author read only the common specification and the predecessor, and opened neither candidate, so it applies to either tenant. The expectations below are what this review checks first.

1. **Restated on the axioms.**
   - Relation 1: each material family of deciding rules shows its premises, the consequences that follow, and any added choices with their owners, and the whole set of members is accounted for. A demonstration over one family is not a derivation of the rest.
   - Relation 2: the Spec Method and profiles use the shared contracts where their actors apply them. An explanatory cross-reference or preamble alone does not establish this.
   - Relation 3: the candidate's own text supplies every conserved determination.
2. **Single ownership.** Within the candidate, each determination has one owning section. The critical risk for a carried corpus is that the carried predecessor members still define generic law next to a new FOUNDATIONS member, which gives two owners. Examples are the RF-012 closed results, the AC-007 outcomes, measurement and the coordination roles. Carried text must become a reference to the owner, or a refinement that maps back to it.
3. **Single result algebra.** The Foundations own one core. RF-012 and AC-007 are unified into it. Every member and profile value maps to exactly one core value without raising standing. Non-performance, undecidability and unknown effect completion stay distinct after combination. Every frame whose task returns a result carries the core.
4. **Bounded transitions and frames.** The current state A, the destination Z and bounded transitions are stated, and configuration is derived from the task without a fixed role inventory. Context fit and adequate attention are judged separately. The workspace is the continuing truth surface. The current-state and basis rule holds: contrary evidence reopens a claim without rebinding the basis, and an absent sparse file is not evidence of absence.
5. **Build-tenant binding.** The candidate's Spec Method states and applies items 1 to 6, and the tenant's design declares its own computational calculus and execution environment.
6. **Categorical demonstration.** No categorical claim is presented as established without its demonstration. Conformance, equivalence and functorial preservation stay distinct claims.
7. **Conformance discriminators.** All 31 discriminators hold under logical review of the member text.
8. **Frontier.**
   - Every predecessor claim has exactly one disposition.
   - Each `conserved` or `superseded` row has a successor locus that resolves.
   - No `conserved` claim sits on text whose meaning changed.
   - The carried compressed summaries do not contradict the members they compress.
   - The one row missing at the base is restored.
9. **Cross-Synthesis.** Each part taken from the Claude candidate is named and has one owning section in the receiving candidate. It is compared with its source and with the predecessor, and is written only in Codex territory.
10. **Development Isolation and Construction Authority.**
    - Tenant writes stay in tenant territory.
    - A tenant branch merges to `main` only on the product owner's acceptance of the checkpoint review.
    - A review by the author, or by a fresh context of the author, is not counted as independent.
11. **Actual use (criterion 4).**
    - Fresh actors are started on frames against oracles specified independently of the author.
    - Context is measured before reading.
    - No oracle text reaches an actor.
    - Claims are limited to the tasks, actors and conditions tested.
12. **Packaging.** The candidate has a manifest, a release note or a declared reason for its absence, and install coordinates that resolve or are declared unresolved. Its successor identity can be issued and verified without the predecessor's bytes remaining operative.
13. **Writing.** Method text is plain and defines its terms, and names roles, not people.

## Verdict

The frozen Codex candidate is a substantial and largely honest piece of work. It gets several hard things right:
- one core result algebra, owned by FOUNDATIONS, into which the predecessor's two result systems (RF-012 and AC-007) are unified;
- a complete frontier: every predecessor claim has one disposition, and every locus resolves;
- standalone text with no rule hidden behind a link to the predecessor;
- the new account of transitions, configuration and the workspace;
- the build-tenant binding;
- verbatim, digest-current frames.

It does not meet the C3 contract on the obligations its strategy makes hardest. That strategy keeps the predecessor's members, adds a foundation layer and rewrites selectively. Four gaps follow:
1. **Foundation to law.** Only 12 of 77 deciding laws show the argument from foundations that relation 1 requires. By the candidate's own FOUNDATIONS rule, the other 65 are "unsupported specialisations", yet its design says every family states its argument.
2. **One result algebra across the carried members.** 47 of 79 result-value sets have no per-value mapping into the core, and 18 pairs of sections decide the same question.
3. **Conservation records.** Six rows recorded `conserved` changed meaning in this synthesis. The conservation record states that dispositions are unchanged, when 34 changed.
4. **Actual use.** The frozen frames are almost untested. One frame-alone run used frozen bytes, and its task had been rewritten.

It is not acceptable for C3 as frozen. The repairs are tractable and are listed at the end.

## Results against the expectations

| # | Expectation | Result | Main evidence |
|---|---|---|---|
| 1 | Restated on the axioms | Relation 1 fails; relation 2 partly holds; relation 3 holds | [CR1](assets/20261013T235754Z_codex_review/CR1.md) F1, F4; relation 3 has no dependencies on the predecessor |
| 2 | Single ownership | Fails | [CR2](assets/20261013T235754Z_codex_review/CR2.md): 18 competing owner pairs |
| 3 | Single result algebra | One core holds; mapping across members fails | CR2-01: 32 of 79 value sets mapped |
| 4 | Bounded transitions and frames | Holds | [CR3](assets/20261013T235754Z_codex_review/CR3.md) items 1 to 5 |
| 5 | Build-tenant binding | Holds, with gaps in the owner and in the tenant's own declaration | CR3 F-4, F-5 |
| 6 | Categorical demonstration | Holds; two small gaps | CR3 F-6, F-9 |
| 7 | 31 discriminators | 29 hold, 2 fail | CR3: rows 27 and 28 |
| 8 | Frontier | Complete and resolving; dispositions wrong on at least 6 rows | [CR4](assets/20261013T235754Z_codex_review/CR4.md) F1, F2, F6 |
| 9 | Cross-Synthesis | Fails for the parts taken from the Claude candidate (not independent) | CR4 F4 |
| 10 | Isolation and authority | Writes stay in territory; the merge to `main` was owner-directed but met no accepted review | [CR5](assets/20261013T235754Z_codex_review/CR5.md) CR5-05 |
| 11 | Actual use | Not evidenced for the frozen frames | CR5-01 to CR5-03, CR5-06 |
| 12 | Packaging | Partly: no successor manifest or release note; identity still defined over predecessor content | CR5-08, CR5-13 |
| 13 | Writing | Holds in the sampled text | CR1, CR3 |

## Findings

Severity is about C3 acceptance. "Introduced" means the defect arrived in this synthesis, and "inherited" means it is carried predecessor text. The cited reports hold the evidence (`file:line` and quotes at `9bc8962`).

### High

**H1. Relation 1 covers 12 of 77 deciding laws, and the design claims all.** (CR1 F1, F7; introduced overclaim.)
- FOUNDATIONS states its own rule: "Each deciding family states the corresponding premises, consequences and additional choices at its own use contract. A family without that argument remains an unsupported specialisation" (`FOUNDATIONS.md:80–83`).
- Counted per numbered law, 12 laws carry an argument: 7 in the TRANSFORMATION_LIBRARY tables and 5 resting on core families. Another 9 are partial, 50 have only a generic member preamble, and 6 have nothing.
- `DESIGN.md:42–43` ("Each material family states its premises, conditional consequences and separately owned choices") and the method return claim full coverage. The return's list of open obligations leaves the gap out.
- The verdict also holds under a coarser grouping into families.

**H2. Most carried result-value sets are not mapped into the core.** (CR2-01, CR2-20, CR1 F4, CR3 F-1; inherited text, introduced claim.)
- Of 79 value sets across the members: 32 are mapped value by value, 28 rely only on the core's default rule, 17 have no core reference at all, and 2 are defective.
- The unmapped sets sit in deciding members: SPEC, TICKET, RELEASE, REFERENCE_FRAME, the Executive baseline and DESIGN.
- Example: the sprint-close classification (`TICKET_METHOD.md:336–346`) gates `closed` on values with no core mapping. TRANSFORMATION_LIBRARY declares them core refinements (`:205–206`), and UX maps the same list (`:512–520`) without naming the owner.
- The return's claim that "consumers refine their own outcomes into" the core is contradicted by the text.

**H3. The conservation record is wrong in two ways.** (CR4 F1, F2, F6; introduced.)
- Six rows marked `conserved` changed meaning in this synthesis:
  - Executive baseline rows `#executive`, `#3`, `#7` and `#status-and-authority-boundary`;
  - AXIOMATIC_CALCULUS `#derivation-provenance`, where "the sole normative authority" for a_c became shared ownership;
  - TICKET_METHOD `#execution-contracts`.

  Each should be `superseded` with a named relation. The changes are often right under the new requirements, but the label is wrong. The Claude line had the same defect class, and it was split and repaired there overnight.
- `CONSERVATION.json` states "dispositions and historical judgment subjects unchanged", while 34 dispositions changed between `a746559` and `3ad1fca`.
- The 33 `superseded` rows share 14 reason strings and point at the old section rather than the replacing owner, so criterion 3's "names the accepted successor relation" is not met.

**H4. Criterion 4 is not evidenced for the frozen frames.** (CR5-01; introduced gap.)
- Of 31 fresh-actor runs, 30 used frame bytes that differ from the frozen commit.
- One run used frozen bytes (WORK_RECOVERY), on a task rewritten to include the check it had failed.
- EVALUATION_CONJUNCTION has no frame-alone run on the frozen cut. Three frames were tested only before the synthesis, and TRIAGE_CARRIER never.

### Medium

- **M1. Second deciders.** (CR2-02, CR2-03, CR2-04, CR2-09, CR3 F-3)
  - Conjunction is still defined at two inherited loci with their own outcomes (REFERENCE_FRAME `:1243`; SPEC UP-021 `:1852`, "refused without effect").
  - Reuse validity has three nominated owners, and FOUNDATIONS states it twice with different conditions (`:128` and `:569`).
  - Fit against adequate attention is decided at TRANSFORMATION_LIBRARY `:154` and SPEC `:855` without cross-reference.
- **M2. Packaging contradicts the Foundations.** (CR2-06, CR2-07, CR4 F3, CR5-09)
  - The compressions README calls Foundations "non-deciding explanations" (`authority_compressions/README.md:8–9`).
  - Six per-member compressions were re-pinned to the new member digests although their bodies are byte-identical to the predecessor. The staleness check therefore reports them current while they serve the old judgement shape.
- **M3. The ports from the Claude candidate are outside the Cross-Synthesis rules.** (CR4 F4; not independent, because Claude authored the source.) No part has a recorded owning section, frontier cone or disposition, and none was compared with its source and with the predecessor.
- **M4. The evidence process is weak.** (CR5-02, CR5-03, CR5-04, CR5-06)
  - The author chose the oracle themes, and the actor instructions paraphrase expected answers.
  - The same oracle was re-run after repairs it drove.
  - 15 of 31 runs were graded.
  - Review packets were assembled by the author, and broad reviews kept finding new contradictions up to the freeze.
  - The v2 against Codex v3 dogfood comparison has one response per side and no control, and both sides passed all ten checks. It cannot rank the two, and two verdicts changed after the Executive's input with no new evidence.
- **M5. The a_c interpretation's fidelity is unreviewed.** (CR5-07, CR5-10) Family fidelity is unresolved, and parts of conjunction and effect integration are unimplemented. The a_c landing page still selects the superseded six-clause model.
- **M6. Successor identity and version.** (CR5-08, CR5-13) Identity is defined over predecessor content and was verified only against a hypothetical fixture. Version `3.0.0` is asserted before the owner's candidate-number decision.
- **M7. Premises and tiers.** (CR1 F2, F3, CR2-21)
  - No method or profile member cites premises F1 to F6 by name.
  - Carried text still calls choices "derived" (Executive baseline `:49`, `:59`).
  - Mandatory Spec intake depends on causal localisation owned only by the optional Executive-baseline profile.

### Minor

| Area | Findings |
|---|---|
| Binding owner | Misses "including any required human decision" and the list of evidence conditions (CR3 F-4) |
| Tenant binding | No units, limits, reviewer identity or failure assumptions (CR3 F-5) |
| Associativity and functorial preservation | Asserted without argument; functorial preservation not named as a separate claim (CR3 F-6, F-9) |
| Role labels | Optional-profile labels in generic law; human-fixed frame-set authority (CR3 F-7, F-8) |
| Duplicated deciders | Several restatements in carried text without a referral (CR2-10 to CR2-19) |
| Moved determinations | Out of their recorded locus (CR4 F5, F7, F8) |
| Limits | Not instrumented for Writer and Executive activations (CR5-11) |
| Single-model evidence | All usability evidence from one model, which also designed the oracle and graded (CR5-12) |

## What holds

- **One core.** FOUNDATIONS owns exactly one core (`FOUNDATIONS.md:296–416`) and unifies RF-012 and AC-007. AC-007 maps hold, gap and refusal by cause. Non-performance, undecidability and unknown effect completion stay distinct when results are combined (CR2).
- **Transitions and configuration.** The workspace, context and current-state and basis rules are stated in full (`FOUNDATIONS.md:532–582`). Configuration follows from the task, and the three-role arrangement is an optional profile. No generic text prescribes a fixed role set or a universal measurement gate (CR3).
- **Binding and discriminators.** The build-tenant binding is owned by SPEC (`:826–859`) and applied in DESIGN_MODULE. 29 of 31 discriminators hold under logical review (CR3).
- **Frontier.** 691 of 691 rows have one disposition, all 690 `conserved` or `superseded` loci resolve, and the missing fourteen-members row is restored (CR4).
- **Standalone text.** No rule-bearing dependency on the predecessor or on a file outside the corpus. Every one of the 18 sampled entry points that Codex edited uses the shared contract at the deciding sentence (CR1).
- **Frames.** All 89 copied sections match their owners byte for byte, and every result-returning frame carries the core and its conjunction rule (CR2, CR3, CR5).
- **The return.** Its general account is honest about limits: against the evidence, 19 claims are supported, 6 partly supported, 0 unsupported and 1 not tested (CR5). Two claims are contradicted by the member text: family coverage (H1) and consumer refinement (H2). Codex's own iteration-2 findings F1 and F2 are confirmed (CR5-09, CR5-10).

## Process note: the merge to `main`

`a9adce2` merged the Codex tenant branch into `main` on the product owner's instruction, recorded in T-002-CODEX: "i want a full checkpoint commit and merge of the current work". Development Isolation allows a merge "only on the product owner's acceptance of the checkpoint review", and no review had been accepted. The product owner's explicit instruction is the recorded override under T-002's admission mechanism, so this is not a Codex defect. The common pen should record it as a variance from the local rule, so that `main` is not read as holding an accepted candidate.

## Smallest repairs, in order

1. **Results.** Map every value set at its owning member, value by value with predicate. Otherwise declare it a recorded state that is not a result, and state the purpose. Remove the second definitions of conjunction, reuse validity and sprint close, and name one owner for fit against attention. (H2, M1)
2. **Foundation to law.** Supply family arguments where actors enter each family, covering the 65 unsupported laws. Otherwise narrow the design's claim to what is shown and record relation 1 as open in the return. (H1)
3. **Frontier.** Re-dispose the six rows as `superseded`, each naming its replacement relation and replacing owner. Correct the history statement in `CONSERVATION.json`. Give each of the 33 `superseded` rows its own relation and locus. (H3)
4. **Actual use.** Run each frozen frame alone against an oracle designed by a non-author, with instructions that do not paraphrase the answers, graded by a different model family, before any usability claim. (H4, M4)
5. **Ports.** Record each part taken from the Claude candidate as part, owning section, rows and disposition, and have it reviewed under the product owner's ported-part policy. (M3)
6. **Packaging.** Correct the Foundations' standing in the compressions README. Check compression bodies for meaning, not only digests. Point the a_c landing page at the current program. Mark the version provisional. (M2, M5, M6)
7. **Merge.** The common pen records the owner-directed merge as a variance. (Process note)

## Evidence boundary

This post changes no candidate, ticket or common file. The subject was read from `git archive` copies of `9bc8962` (product) and `3ad1fca` (qualification evidence). Five Claude reviewers each worked one dimension, and their full reports are in [assets](assets/20261013T235754Z_codex_review/). Two of them used read-only sub-reviews for large members. The synthesis re-read the frozen text for H1, H2 and H3 before relying on them.

The reviewers ran no fresh actors and did not evaluate the a_c program mechanically. They graded no rerun of Codex's cases. The independence limits stated at the top apply: Claude authored the competing candidate, and every finding on parts ported from it (M3, and parts of CR1) is not independent.
