# REVIEW: Codex v3 iteration 3 candidate

**Author**: Dimitar Popov
**Date**: 2026-10-14T15:10:55Z
**Addresses**: the Codex tenant candidate at `3aaa2f2cf0d6f24a734a33c258373a58feceaf87` on `tenant/codex/c3-iteration-3`, the frozen package returned under `EC-CODEX-I3-02` as `candidate_ready`; its common input `C3-I3-R2-01` at `355aa8655cca9c6ba6cf5c414f9bea3032ae89fd`
**Status**: Complete for the frozen subject. Expectations part A (`e4e72b0`) and part B (`2f93f78`) were committed before the subject was opened.
**Updated**: 2026-10-14T15:57:59Z (findings)

## Authority and independence

The product owner asked for a full review of version 3 iteration 3: the specification update and Codex's build of it. The request reached this session through a reviewer subagent he messaged directly. It continues his earlier assignment of cross-family review to Claude. The specification is reviewed in rounds in a separate post ([I3 specification review](20261014T013233Z_REVIEW_I3_COMMON_SPECIFICATION.md)). This post reviews the candidate, and it repairs nothing.

The reviewer is Claude, a different model family from the author, Codex. Limits:
- Claude builds the competing candidate.
- Claude wrote the findings on Codex's iteration 2 that this iteration answers.
- Any part ported from the Claude candidate is Claude's authorship, and findings on such parts are marked not independent.

The candidate is read at `3aaa2f2`. The tenant files on `main` hold an earlier candidate and are not this subject.

## Expectations, part A: closure of the iteration 2 findings

The [critical review of the frozen iteration 2 candidate](20261013T235754Z_REVIEW_CODEX_V3_FROZEN_CANDIDATE.md) found four High and seven Medium groups. Each closes only when the iteration 3 candidate meets the expectation below.

- **H1, foundation to law.** Every material family of deciding rules shows its premises, the consequences that follow, and its added choices with owners, at the place where actors use it. This holds under the common specification's definition of a material family at `355aa86`. The design and the return claim no more coverage than the text shows.
- **H2, one result algebra across members.**
  - Every result-value set in every member maps value by value into the core, or is declared a recorded state with its purpose.
  - No set relies only on a general rule that does not decide a unique value.
  - The sprint-close classification and the UP-015 dispositions are covered.
  - No two sections decide the same question.
- **H3, conservation record.**
  - Each row whose meaning changed is `superseded`, naming its own replacement relation and replacing owner. Under the specification at `355aa86`, the product owner must have accepted that relation, or the row stays pending.
  - The conservation record's history entries state the disposition changes truthfully.
- **H4, actual use.**
  - Each frozen frame or acquisition view is tried by fresh actors, starting from the frozen bytes.
  - The oracles are specified by someone other than the author, and the actor instructions do not paraphrase expected answers.
  - The runs are graded independently, and the claims are limited to the tasks and actors tried.
- **M1, second deciders.** Conjunction, reuse validity, sprint close, and fit against adequate attention each have one owner.
- **M2, packaging against the Foundations.** The compressions do not deny the Foundations' standing. Compression bodies are checked for meaning, not only re-pinned.
- **M3, ports from the Claude candidate.** Each port is named, owned in one section, inside a frontier cone with its disposition, and compared with its source and with the predecessor (not independent).
- **M4, evidence process.**
  - Oracle independence and the instructions are as in H4.
  - Grading covers every run that is claimed.
  - Review packets are not assembled by the author with stated expectations.
  - No verdict is changed without new evidence.
- **M5, a_c interpretation.** The current interpretation covers what the common specification at `355aa86` requires. It resolves to its owning sources and has independent fidelity evidence, and the landing page selects it.
- **M6, identity and version.** Successor identity does not depend on predecessor bytes, or the dependence is stated as open. The version is not asserted before the owner's decision.
- **M7, premises and tiers.** The premises are traced by name where they are used. No choice is presented as derived. No mandatory member depends on an optional profile.

## Expectations, part B: independent oracle

[ORACLE.md](assets/20261014T151055Z_codex_i3_review/ORACLE.md) was written from the common specification at `355aa86` and the installed predecessor. Its author opened no candidate, no comment and no tenant ticket.

| Group | Expectations |
|---|---|
| a, pillars | 11 |
| b, the successor relationships, including reduction | 12 |
| c, constraint surfaces and the a_c interpretation | 10 |
| d, ownership and the result algebra | 11 |
| e, transitions, recovery and acquisition | 8 |
| f, build-tenant binding | 5 |
| g, categorical demonstration | 6 |
| h, frontier and dispositions | 11 |
| i, acceptance, actual use and independence | 12 |
| j, conformance rows | 55 |

It also holds 12 negative expectations and records 12 ambiguities in the specification. Where the specification is ambiguous, findings name the reading they rely on.

## Scope

The subject was read from a `git archive` copy of `3aaa2f2`: 1,698 files, about 96 MB. Since iteration 2, `successor/` changed in 44 files, with about 227,000 lines added, most of them generated.

One reviewer read the conservation map at `939ce0c`. That copy is pinned to the frozen package, while the copy inside `3aaa2f2` is unpinned and its return is stale (CB4).

Five Claude reviewers each covered one area. Their reports are in [assets](assets/20261014T151055Z_codex_i3_review/):

| Report | Area | Expectations |
|---|---|---|
| [CB1](assets/20261014T151055Z_codex_i3_review/CB1.md) | pillars, relation 1, reduction | H1, M7; oracle a, b |
| [CB2](assets/20261014T151055Z_codex_i3_review/CB2.md) | ownership, result algebra, transitions, binding, categorical, frames | H2, M1; oracle d to g |
| [CB3](assets/20261014T151055Z_codex_i3_review/CB3.md) | a_c interpretation, constraint surfaces, packaging, identity | M2, M5, M6; oracle c |
| [CB4](assets/20261014T151055Z_codex_i3_review/CB4.md) | frontier, dispositions, replacement relations, ports | H3, M3; oracle h |
| [CB5](assets/20261014T151055Z_codex_i3_review/CB5.md) | actual use, evidence process, acceptance, return claims | H4, M4; oracle i |

## Verdict

Iteration 3 is a large improvement on iteration 2 on every axis this review measured:
- Arguments from the foundations: from 12 to 75 of 77 numbered laws.
- Result-value sets mapped or declared: from 32 to 65 of 79.
- Competing owner pairs: from 18 to 6.
- The six mislabelled conservation rows are corrected.
- A complete a_c interpretation now passes the pinned checker, and checking the same frozen bytes again reproduces the result byte for byte.
- The compressed summaries are rewritten for meaning.
- The return claims no acceptance and states its limits truthfully.

As frozen, the candidate still does not meet C3:
- relation 1 is incomplete under the specification's own definition of a material family;
- reduction is not demonstrated;
- ten value sets are unmapped;
- 116 rewritten `conserved` rows were not re-assessed;
- the a_c interpretation is largely unreviewed for fidelity;
- criterion 4 is not evidenced for any frozen frame;
- the ports are not compared with their source and the predecessor.

One gap waits on the product owner rather than the candidate: all 51 replacement relations need his acceptance before any dependent member is accepted. Acceptance is his decision.

## State of the iteration 2 findings

| Finding | State | Evidence |
|---|---|---|
| H1, foundation to law | **Not closed**; much improved | Numbered laws argued rose from 12 to 75 of 77. Under the `355aa86` definition of a material family, 314 of 460 deciding units are argued, 60 partly and 86 not at all, mostly in Spec, REFERENCE_FRAME, ODD and the Executive baseline. The account packaged with the method has 127 hollow arguments, which file the whole rule as the policy choice. Spec, Ticket and Release have almost no real ones. In five of the six frames actors read, 33 of 35 law excerpts arrive without their family table. The design and the return still claim more coverage than the text shows (CB1) |
| H2, one result algebra | **Not closed**; much improved | 65 of iteration 2's 79 value sets are mapped or declared recorded states, and 10 are unmapped. Iteration 2 had 32 against 47. Sprint close, the UP-015 dispositions and the coverage predicate are now mapped, and conjunction is defined once. The 10 unmapped sets are in the Executive baseline, SPEC, TICKET, ODD and TRAVERSAL (CB2-01) |
| H3, conservation record | **Partly closed** | The six rows found last time are `superseded` with their own relations, and the history entry is corrected exactly. All 691 rows are disposed (639 `conserved`, 51 `superseded`, 1 `not applicable`), and all 2,524 locus references resolve. Still open: 116 `conserved` rows were rewritten in iteration 3 without re-assessment, and 8 in a 75-determination sample now change scope or modal force under `conserved`. Several relations do not name everything they replace (CB4) |
| H4, actual use | **Partly closed** | Criterion 4 is not evidenced for any frame at `3aaa2f2`. Actors entered at a skill file rather than on a frame, and one context ran all six tasks. One arm read 6–74% of each frame, plus owner sections no frame carries. No activation declared a context limit. All three arms score 30 of 30 on assertions the fixture text decides, the predecessor included, and there is no no-method arm, so the results cannot be attributed to frame content. Freshness is not established (CB5-01 to CB5-03) |
| M1, second deciders | **Partly closed** | 16 of 18 pairs are closed. Conjunction, reuse validity and sprint close each have one owner. Fit against adequate attention still has two deciders and no Foundations owner. Six pairs remain, two of them new (CB2) |
| M2, packaging against the Foundations | **Partly closed** | The compressions no longer deny the Foundations' standing, their bodies were rewritten for meaning, and all 32 pins hold (CB3) |
| M3, ports from the Claude candidate | **Not closed** (not independent) | No port has been compared with its source and the predecessor, and the port records conflict with each other (CB4) |
| M4, evidence process | **Largely closed** | The oracle was frozen about two hours before the actors, the actor prompt is neutral, all 90 assertions are graded, and no verdict was rewritten. The grading and one working review are called "independent" without declaring their same-family exception (CB5) |
| M5, a_c interpretation | **Not closed**; much improved | Re-running the pinned checker on the frozen bytes reproduces its validation and map byte for byte: 734 clauses, 0 diagnostics. Every element resolves to its owning source, and entry selects the current interpretation. Still open (CB3): every SPEC row flattens section-specific premises into F1 to F6, every TICKET row carries the wrong premise set, open questions the source leaves are filed as policy choices, 2 of 16 sampled rows are unfaithful, 626 of 697 rows are unreviewed, and the use trial read no interpretation bytes |
| M6, identity and version | **Not closed** | Successor identity is still bound to predecessor coordinates, and version 3.0.0 is still asserted (CB3-07, CB3-08) |
| M7, premises and tiers | **Partly closed** | Premises are named in the prose but not in the account. The old "derives" text is fixed, but "Derived" headings remain. Two Spec rules depend unconditionally on DESIGN_MODULE, now labelled an optional profile (CB1) |

## Results against the independent oracle (part B)

| Group | Result |
|---|---|
| a, pillars | 8 accounted for, 3 partly, 0 missing. No argument names its pillar (CB1) |
| b, successor relationships | Relation 1 as H1. Relation 4, reduction, has no positive witness on deciding paths: the eight elimination candidates are "comparison pending" and the per-consumer records are stale. Against the predecessor, matched use emitted 20.9% more bytes and read 133% more method text; the return discloses this and claims no reduction. Of seven claimed contractions, 2 verify against both baselines, 1 against iteration 2 only, and 2 partly. One weakens a World Model prohibition into a preference, and one, the Release exact-cut contraction, is absent (CB1) |
| c, a_c and constraint surfaces | As M5. One three-line rule projects to 2.57 MB, larger than the whole 1.8 MB package (CB3-05) |
| d, ownership and the result algebra | As H2 and M1 |
| e, f and g, transitions, binding and categorical | Hold in content. Iteration 2's gaps in the tenant's own binding declaration and in naming functorial preservation persist (CB2) |
| h, frontier and dispositions | As H3. All 51 replacement relations are pending the owner's acceptance (CB4) |
| i, acceptance and actual use | As H4. Nothing is presented as accepted. Limits and spend are not declared or reported for activations (CB5-05) |

Frames hold: all 98 excerpts are exact, and every frame carries the core result algebra (CB2).

The return's claims tested by CB5: 16 supported, 4 partly supported, 2 not tested. CB1 and CB2 find its coverage and ownership claims stronger than the method text supports.

## Smallest repairs, in order

1. **Relation 1.** Give the 86 unargued deciding units and the 127 hollow arguments real premise-to-consequence arguments, starting with Spec, Ticket and Release. Carry the family tables in frames, and limit the design's and return's coverage claims to what is shown (H1).
2. **Reduction.** Complete the eight pending comparisons on actual deciding paths against both baselines. Restore the World Model prohibition, and supply or withdraw the Release exact-cut contraction (oracle b).
3. **Result algebra.** Map the 10 remaining value sets, and give fit against attention one Foundations owner (H2, M1).
4. **Conservation.** Re-assess the 116 rewritten `conserved` rows. Re-dispose the eight that changed meaning, and complete each relation's account of what it replaces (H3).
5. **a_c fidelity.** Correct the SPEC and TICKET premise sets. Carry open questions as residuals that block dependent work, and repair the two unfaithful rows. Review the remaining rows independently, and bound the 2.57 MB projection (M5).
6. **Actual use.** Run each frozen frame alone, under a declared limit, with a no-method control and fresh contexts, on tasks the fixture text does not already decide (H4).
7. **Ports.** Compare each port with its source and the predecessor, and reconcile the port records. This needs the product owner's ported-part review policy (M3).
8. **Identity and version.** Unbind successor identity from predecessor coordinates or declare it open, and mark the version provisional (M6).

## Independence and limits

- **Not independent.** The reviewers are Claude-family, the family of the competing tenant. Findings on the five parts ported from the Claude candidate (CB1, CB2-03, CB4's M3) are marked not independent.
- **Sampling.** The reviewers sampled. CB1 checked 7 claimed contractions, CB3 17 interpretation elements and CB4 75 determinations, each partly re-checked directly. Two reviewers used read-only sub-reviews of large members.
- **What was not done.** No fresh actors were run. The pinned checker was re-run only on the frozen bytes. This post selects no repair and accepts nothing.
