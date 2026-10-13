# REVIEW: Critical review of the frozen Codex v3 candidate

**Author**: Dimitar Popov
**Date**: 2026-10-13T23:57:54Z
**Addresses**: the Codex tenant candidate `build_tenants/codex/`, product source frozen at `9bc8962e44aff2cd1dc29a9bac95356cdccf7cdd`, qualification evidence at `3ad1fca31dc93ba0847bbbbf308312a554daa1f6`; the common specification at the same commit (identical to `main` at `a9adce2`)
**Status**: In progress. This first commit records only the expectations, written before the subject was opened.

## Authority and independence

The product owner asked for this review on 2026-10-14: "ok i want you to do a critical review of the v3/codex candidate", and named its subject: "frozen candidate as V3 iteration 3 work has commenced". The review reads the candidate at the frozen commits above, not the Codex worktree, where iteration 3 is in progress. It repairs nothing.

The reviewer is Claude, a different model family from the candidate's author, Codex. Two limits on that independence:

- Claude authored the competing candidate, which it finished building the night before this review.
- Any part of the Codex candidate ported from the Claude candidate is Claude's authorship. A finding on such a part is marked as not independent.

## Expectations, recorded before opening the subject

Sources: the common specification at the frozen commit, and the installed predecessor `stdo://releases/v2.5.1-rc.2/`. The detailed oracle is the expectations file written for the Claude line's rebuild: [EXPECTATIONS](../../../build_tenants/claude/qualification/C3-SYNTHESIS/EXPECTATIONS.md) on branch `tenant/claude/c3-synthesis`, 87 expectations plus an amendment. Its author read only the common specification and the predecessor, and opened neither candidate, so it applies to either tenant. The expectations below are what this review checks first.

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

## Findings

To follow in the next commit.
