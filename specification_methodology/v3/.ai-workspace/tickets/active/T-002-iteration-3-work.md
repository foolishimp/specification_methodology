# Iteration 3 consolidated work

This is the current work-list appendix to [T-002](T-002-c3-successor-construction.md)
and [T-002-CODEX](T-002-CODEX-c3-successor-construction.md). It joins the common
iteration 3 requirements and the reviews into one execution frontier. It adds
no method law, admission mechanism or acceptance authority. Common requirements
apply to both candidates; assignments and implementation status below concern
Codex only. The peer keeps its own ticket and execution line.

The owner selects completing the common update and this consolidation before
the next implementation increment. The three active Writers have returned;
their repairs are checkpointed on `tenant/codex/c3-iteration-3` at `de8232a`.
Generated material and qualification still bind the earlier source. This is
not a qualified distribution, completed C3 or an accepted release.

The common recording commit `5543840` is merged inward at tenant commit
`d832a51a4f91afca2ffa2e31636236f8729abf6c`. Its Codex tenant tree is exactly
`dd222838b69addb683343e42992a2b08c1e459a0`, unchanged from `de8232a`, and the
tenant worktree is clean. The requirement update is therefore present for the
next activation without relabelling the existing repairs or evidence.

## Basis and evidence subjects

The governing builder is installed `v2.5.1-rc.2`, manifest
`3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`.
The successor common input is recorded in [T-002's snapshot](T-002-c3-successor-construction.md#c3-codex-iteration-3-consolidated-input-snapshot).
The previous input `C3-CODEX-I3-01` at `cae6fe3` remains the basis on which the
initial iteration 3 construction and bounded repairs were performed.

| Subject | Exact scope |
|---|---|
| Iteration 2 | Product source `9bc8962`; evidence `3ad1fca`. Owner-directed checkpoint merge `a9adce2` gave visibility, not acceptance. |
| Initial iteration 3 | Product source `b99ca785`; evidence `4889563`. Passing checks remain limited to this source. |
| Current repair checkpoint | Shared clarification `c330038`; returned source and author repair records `de8232a`. Independent integration review, refreshed derivatives and qualification remain open. |

The repair records are in the Codex tenant's
`qualification/C3/iteration-3/{METHOD_REVIEW_REPAIR,FRAME_REVIEW_REPAIR,PROFILE_REVIEW_REPAIR}.md`
at `de8232a`. Read that commit in the tenant worktree or with `git show`; their
absence from main does not authorise a candidate merge. The same checkpoint's
`RETURN.md` states the current evidence limits.

| Review key | Source and applicability |
|---|---|
| E | [Codex iteration 2 entry review](../../comments/codex/20261013T234239Z_REVIEW_CODEX_V3_REVISION_2_PURPOSE_AND_IMPLEMENTATION.md): three entry defects. Its bounded keep-the-design recommendation does not override the iteration 3 reconstruction. |
| H | [Claude frozen iteration 2 review](../../comments/claude/20261013T235754Z_REVIEW_CODEX_V3_FROZEN_CANDIDATE.md), with [CR1](../../comments/claude/assets/20261013T235754Z_codex_review/CR1.md), [CR2](../../comments/claude/assets/20261013T235754Z_codex_review/CR2.md), [CR3](../../comments/claude/assets/20261013T235754Z_codex_review/CR3.md), [CR4](../../comments/claude/assets/20261013T235754Z_codex_review/CR4.md) and [CR5](../../comments/claude/assets/20261013T235754Z_codex_review/CR5.md). H1–H4 are its four principal findings. Counts describe the frozen iteration 2 inventory, not current coverage. Imported-source authorship limits remain. |
| K | [Fresh iteration 3 core review](../../comments/codex/20261014T004200Z_REVIEW_ITERATION_3_SHARED_CONTRACT.md): bounded sample of `b99ca785`. No finding there does not close H1–H4. |
| S | [Fresh iteration 3 source-conservation review](../../comments/codex/20261014T003000Z_ITERATION_3_SOURCE_REVIEW/REVIEW.md): ten findings against `3ad1fca → b99ca785`, with incomplete untouched-body coverage. Its [packet and measurement](../../comments/codex/20261014T003000Z_ITERATION_3_SOURCE_REVIEW/MEASUREMENT.json) retain the supplied material and USD 3.6950538 spend. |
| AC | [Interpretation working-review return](../../comments/codex/20261014T010500Z_REVIEW_ITERATION_3_INTERPRETATION_RETURN.md): AC-F1 concerns “not required” becoming “prohibited”; selected shared-law scope only. |

## Requirement trace

These labels abbreviate existing requirements for this work list. They are not
new constitutional identifiers or a prescribed tenant document structure.

| Requirement | Owner in the updated common specification | Work |
|---|---|---|
| R1: pillars govern the reconstruction | [Product: Foundational Reduction](../../../specification/PRODUCT.md#foundational-reduction), [standalone successor](../../../specification/requirements/README.md#standalone-successor-requirement) | I3-01, 02, 05, 06 |
| R2: contract recurring determinations and justify remaining distinctions | [Foundational Reduction Requirement](../../../specification/requirements/README.md#foundational-reduction-requirement) | I3-01, 02, 04, 07, 12 |
| R3: one meaning owner, including generic versus optional policy | [Single Ownership Requirement](../../../specification/requirements/README.md#single-ownership-requirement) | I3-02, 03, 04, 08 |
| R4: one result algebra with predicate-bound refinements | [Single Result Algebra Requirement](../../../specification/requirements/README.md#single-result-algebra-requirement) | I3-03, 04, 09, 12 |
| R5: conserve or explicitly replace every material predecessor claim | [Successor Disposition Requirement](../../../specification/requirements/README.md#successor-disposition-requirement), [C3 criteria 1–3](../../../specification/PRODUCT.md#c3-construction-contract) | I3-04, 06, 07, 08, 14 |
| R6: usable, faithful constraint surfaces | [Constraint Surfaces And Logic Compression](../../../specification/requirements/README.md#constraint-surfaces-and-logic-compression) | I3-08, 09, 10, 11 |
| R7: bounded frames, workspace recovery and lawful configurations | [Bounded Transitions And Reference Frames](../../../specification/requirements/README.md#bounded-transitions-and-reference-frames), [C3 criterion 4](../../../specification/PRODUCT.md#c3-construction-contract) | I3-05, 10, 11, 12 |
| R8: requirements bind to human, machine or mixed realisation | [Build-Tenant Binding Requirement](../../../specification/requirements/README.md#build-tenant-binding-requirement) | I3-05, 08, 12 |
| R9: claims have the evidence their scope requires | [Categorical Demonstration Standard](../../../specification/requirements/README.md#categorical-demonstration-standard), [A_C_DEPENDENCY](../../../specification/requirements/A_C_DEPENDENCY.md) | I3-05, 09, 12, 15 |
| R10: ports have one receiver and supported dispositions | [Cross-Synthesis](../../../specification/PRODUCT.md#cross-synthesis) | I3-07, 14 |
| R11: test capabilities and common counterexamples | [Capabilities](../../../specification/requirements/CAPABILITIES.md), [Conformance](../../../specification/conformance/README.md) | I3-10, 11, 12, 14 |
| R12: standalone identity, acceptance and release | [Identity and lineage](../../../specification/PRODUCT.md#product-identity-and-lineage), [C3 contract](../../../specification/PRODUCT.md#c3-construction-contract) | I3-13, 14, 16 |

All nine pillars have a work destination: specification/project structure
(01, 05, 06); objects, identity and Markov claims (05, 13); functional algebra
(02, 04, 05); ODD (03–05); information and interpretation (08–09); reference
frames (05, 10–11); computational realisation (05, 12); evidence, correction
and authority (03, 06, 10, 14); and a_c (09). The numbers refer to I3 tasks.
This routing is not a finding that their governing relationships are complete.

## Work and closure

`OPEN` means required work or proof remains. `REPAIR RETURNED` means source
changes exist but independent integration proof remains. `BOUNDED EVIDENCE`
means evidence supports only its named subject and scope. `RESERVED` identifies
an owner-selected activity or decision not selected by this consolidation.
None of those states means accepted. Each completion records its source,
requirement, review result and remaining limits here; it does not rewrite an
older review's subject or verdict.

| ID | Work, owner and current state | Observable exit proof |
|---|---|---|
| I3-00 | **Common standard and consolidation — COMPLETE.** The [fresh review](../../comments/codex/20261014T011752Z_REVIEW_ITERATION_3_CONSOLIDATION.md) found no actionable common defect at `6c2debb`. [C3-CODEX-I3-02](T-002-c3-successor-construction.md#c3-codex-iteration-3-consolidated-input-snapshot) records input `7b2f933` and its 30 member hashes. Owner acceptance remains separate. | Nonauthor review of the frozen common update; corrected findings; links and exact builder checks; input B and descendant recording R with matching hashes. |
| I3-01 | **Foundation-to-law coverage — OPEN; bounded arguments returned.** Tenant design/member Writers account for material deciding families, including inherited rules, and distinguish premises, consequences and owned policy. | Every material deciding rule is covered by an intelligible argument and consuming binding. Independent review finds neither unaccounted families nor a policy represented as a theorem. The old 77-law count is evidence to examine, not a mandatory partition. R1–R2; H1. |
| I3-02 | **Shared ownership and actual contraction — REPAIR RETURNED, whole-corpus audit open.** Tenant core/consumer Writers reconcile conjunction, applicability, result and attention owners; generic causal localisation is moved to Spec with Baseline consuming it. | One determination per question, usable without an optional profile where generic; affected consumers obey it. Show which independent decisions/reconciliations disappeared and justify remaining distinctions. Added argument prose alone proves no reduction. R2–R3. |
| I3-03 | **Domain result integration — REPAIR RETURNED, inventory open.** Member owners finish predicate-and-condition mappings, particularly Ticket sprint close, Release UP-015, Spec UP-021, RF coverage and a_c refusal/treatment. | Account for the review's value sets as actual results or domain data. Every evaluation/decision has a total owner-defined core mapping; no caller/core loop, label guessing or promotion of failed/unknown work. Exercise failure plus missing coverage and unavailable causes. R3–R4; H2. |
| I3-04 | **Contraction conservation — REPAIR RETURNED.** Consumer Writers preserve triggers, modal force, conditional adoption and exceptions in the ten S findings and affected callers. | Independent source comparison on the repaired cut plus counterexamples distinguishes required, permitted, preferred and prohibited work. Validate trust-boundary admission, gate scope, projection family coverage, optional ODD, uncertainty and authority. R2–R5. |
| I3-05 | **Pillars at real decisions — OPEN; sampled evidence exists.** Tenant design and proof owners connect objects/Markov assumptions, functional design, ODD operation kinds and maps, WHAT/HOW structure, workspace recovery and concrete human/machine bindings to deciding paths. | Appropriate successful, refused and unresolved cases; explicit binding units, boundary, actors, assumptions and failure modes; supported reuse after restart and dependency change. Strong Markov, equivalence and functor claims stay bounded by their proof. R1, R7–R9. |
| I3-06 | **Conservation and replacement relations — OPEN, author draft only.** Tenant proof Writer integrates and verifies the 47 draft relations, corrects mislabeled conservation and the historical “unchanged dispositions” claim, and checks all 691 rows. | Every row has a truthful disposition, complete carrying loci and, if superseded, its own identifiable replacement relation. Compare meaning, not headings/digests; check global bindings and compression rows. Proposed replacements stay pending until accepted. No unapproved removal. R1, R5; H3. |
| I3-07 | **Port accounting — OPEN.** Tenant Writer maps each already-named contribution from `31f28f9` to one receiving owner, affected frontier and disposition. | Source/predecessor/receiver comparison under the selected port-review policy; disclosed authorship limits. No new peer reading or port is selected by this list. The open review-policy decision remains explicit. R2, R5, R10. |
| I3-08 | **Current entry and derived views — OPEN; initial entry fixes implemented.** Packaging Writer reconciles skill routes, compressed bodies, six frame views, a_c landing page, inventories and pins after the final source repairs. | Source/view semantic comparison as well as matching hashes; ordinary entry selects current governing material; generic chain covers human/mixed realisation. E's three initial fixes at `b99ca785` are retained but do not qualify later derivatives. R3, R5–R6, R8. |
| I3-09 | **a_c fidelity and logic acquisition — OPEN; bounded review and generator repair.** Interpretation Writer regenerates the AC-F1 correction and reconciles all selected source/program/maps; independent reviewer checks fidelity and residual acquisition. | Current interpretation preserves obligations, latitude and uncertainty; every claimed family has evidence. Distinguish the 43-clause selected projection from the 62-clause program and finite-model tests from general proofs. Retrieve residual domain policies when needed. R4, R6, R9. |
| I3-10 | **Actual use of final frames — OPEN.** Independent case/oracle author, fresh actors and independent assessment cover each selected task on the exact final frame and subject. | Freeze neutral prompts, acquisition conditions and independently specified expectations before testing. Retain actual packets/results, grade the selected coverage and adjudicate disagreements. A rewritten task or an earlier frame cannot supply current criterion 4 without justified applicability. R6–R7, R11; H4. |
| I3-11 | **Ordinary entry, recovery and measured comparison — BOUNDED EVIDENCE; current qualification open.** Proof owner tests ordinary acquisition and workspace recovery, including triage/carrier entry, under comparable conditions. | Reproducible acquisition and recovery; comparison, if claimed, uses identical tasks/oracles and declared measurement boundaries. Preserve the prior n=1 source exercises as limited comprehension evidence, disclose oracle timing and same-family exceptions, and report pre-clarification versus later judgments separately. No superiority claim from them. R6–R7, R11. |
| I3-12 | **Current conformance and proof closure — OPEN.** Proof owner joins all applicable common discriminators to the repaired source and selected material capabilities. | Cases cover inherited as well as new rules, core and domain joins, binding assumptions, effects and recovery. Formal, mechanical, source-review and use evidence retain distinct standing. Report acquisition/context, elapsed time and spend with uninstrumented portions explicit. No universal arbitrary budget. R2, R4, R7–R9, R11. |
| I3-13 | **Standalone identity and installed use — OPEN; publication-dependent part RESERVED.** Packaging/proof owner separates valid historical provenance from operative predecessor dependence and marks provisional candidate identity. | Owner-selected identity policy; source-blind check of the actual standalone package; when publication is selected, a real manifest and unchanged installed-copy proof. Nineteen negative controls on a hypothetical fixture are bounded evidence, not issued identity or installed qualification. R12. |
| I3-14 | **Independent member review and truthful return — OPEN.** Executive selects source-first independent reviews of the frozen current candidate; ledger Writer records each criterion's result and unresolved dependencies. | All six C3 criteria receive applicable results, with prior findings traced and no author-only repair promoted to acceptance. Reviewers acquire the source within their grant. Record port and same-family limitations; correct current broad claims without rewriting historical reports. Owner checkpoint acceptance remains separate. R5, R10–R12. |
| I3-15 | **Categorical worked join — RESERVED, NOT_SELECTED.** Owner selects the neutral sum-and-histogram thread and its actors/limits under Product. | Its full six-item contract, including the method's own Intent-to-Realisation preservation chain, and independent assessment. Source comprehension or finite toy oracles cannot close it. R9. |
| I3-16 | **Acceptance, integration and release — RESERVED.** Owner decisions retain their existing authority. | Accepted checkpoint/member evidence, separately authorised integration, release identity/materialisation, unchanged installed qualification and adoption as selected. The historical owner-directed merge variance is already recorded; it neither needs an implementation repair nor accepts the candidate. R12. |

## Review-to-work index

Every finding in the supplied review packet has a destination below, including
historical, conditional and policy-dependent items. A destination is not a
finding's closure. Detailed counterexamples remain in their original reports.

| Review findings | Work |
|---|---|
| E-F1, F2, F3 | I3-08; F2 also I3-09 |
| H1; CR1-F1, F2, F3, F7 | I3-01, I3-14 |
| CR1-F4 | I3-03 |
| CR1-F5, F6 | I3-02, I3-03, I3-04 |
| CR1-F8 | I3-05, I3-06, I3-08 |
| H2; CR2-01, 04, 05, 08, 09, 10, 11, 13, 16, 19 | I3-03; caller consistency also I3-04 |
| CR2-02, 03, 12, 14, 15, 17, 18, 21 | I3-02, I3-03, I3-04 |
| CR2-06, 07 | I3-08 |
| CR2-20 | I3-14 |
| CR3-F1, F2 | I3-03 |
| CR3-F3, F7, F8 | I3-02, I3-05 |
| CR3-F4, F5, F6, F9 | I3-05, I3-09, I3-12; demonstrated categorical join also I3-15 |
| H3; CR4-F1, F2, F2b, F5, F6, F7, F8 | I3-06 |
| CR4-F3 | I3-06, I3-08 |
| CR4-F4 | I3-07, I3-14 |
| H4; CR5-01, 02, 03, 12 | I3-10, I3-11 |
| CR5-04 | I3-14 |
| CR5-05 | I3-16: owner-directed historical variance; no candidate defect inferred |
| CR5-06, 11 | I3-11, I3-12, I3-14 |
| CR5-07 | I3-09, I3-12 |
| CR5-08, 13 | I3-13 |
| CR5-09, 10 | I3-08 |
| S-1, 2, 5 | I3-03, I3-04: method repair returned; S-2 also frame/calculus repair |
| S-3, 6, 7, 8 | I3-04: frame/calculus repair returned |
| S-4, 9, 10 | I3-04: profile repair returned; conditional scope checked against source |
| AC-F1 | I3-09: generator repaired, current interpretation proof pending |
| K, no finding within its sample | I3-02, I3-05: bounded evidence only; no whole-corpus closure |

## Sequence after consolidation

1. Complete I3-00 and record the reviewed common input. Merge that common basis
   inward to the tenant under its existing isolation rule.
2. Reconcile design and finish I3-01–05 as one source-consistent increment.
   Triage any common-contract counterexample at its owner before changing HOW.
3. Complete I3-06–09 against that source: dispositions, named ports, derived
   views and interpretation. Freeze a coherent candidate before trials.
4. Complete the applicable I3-10–13 proof, with independently specified tasks,
   exact subjects and recorded limits. Carry reserved publication-dependent
   work explicitly instead of claiming it passed.
5. Obtain I3-14's independent criterion results and return for owner review.
   I3-15 and I3-16 retain their separate selection and acceptance boundaries.

The list does not start another paid run, activate the peer, remove a
predecessor obligation or select a merge/release. It preserves the existing
run-to-completion construction authority while making the next work and its
proof obligations inspectable against the new common standard.
