# REVIEW: Codex v3 iteration 3 candidate

**Author**: Dimitar Popov
**Date**: 2026-10-14T15:10:55Z
**Addresses**: the Codex tenant candidate at `3aaa2f2cf0d6f24a734a33c258373a58feceaf87` on `tenant/codex/c3-iteration-3`, the frozen package returned under `EC-CODEX-I3-02` as `candidate_ready`; its common input `C3-I3-R2-01` at `355aa8655cca9c6ba6cf5c414f9bea3032ae89fd`
**Status**: Expectations parts A and B recorded before the subject was opened. Review in progress.

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

## Findings

To follow.
