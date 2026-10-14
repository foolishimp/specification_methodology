# REVIEW: Iteration 3 common specification, review rounds

**Author**: Dimitar Popov
**Date**: 2026-10-14T01:32:33Z
**Addresses**: the common specification `specification_methodology/v3/specification/` for iteration 3, at the commit the common pen names as frozen for each round
**Status**: Expectations recorded. The subject is not yet frozen, so no finding is recorded.

## Authority and independence

The product owner, 2026-10-14: "you will need to review I3 spec and there will be rounds of repair until we are satisfied with the specification".

Codex holds the common pen and writes the specification. Claude reviews each frozen round and repairs nothing. Each round's subject is the commit the pen names as frozen; a moving `main` is never reviewed.

Two limits on independence. Claude is a build tenant whose candidate the specification governs. Claude has also seen the specification at intermediate commits while building. In particular, it wrote a provisional builder's oracle from `6c2debb`, which is now set aside. That oracle is not used here, because it was derived from the specification under review.

## Sources of the expectations

The product owner's recorded instructions for iteration 3, in T-001 at `main` `6c2debb`:

- Verbatim: "update v3/specification given the current pillars, and then do v3 iteration 3".
- Verbatim: "i want the v3 iteration3 work plus the review work to be consolidated - the means complete the v3/sepicification update for iteration 3, then make a list of the work from the reviews and the updated specification, that way it can tracked to the new standard".
- As recorded by the pen, not verbatim:
  - the algebraic and computational calculi are two of the essential reductions, alongside Markov objects, ODD transformations, functional design, the Spec Method and project structure, reference frames, information semantics, and evidence and authority;
  - a_c is "logic compression of the prose that creates constraint surfaces within which work can happen";
  - preserving inherited document boundaries is not the outcome.

The earlier owner direction recorded in T-001 also applies, verbatim:
- "worker, executive, revierwer emerge out of reference frames";
- "our entire methodology is about defining A, defining Z and managing the series of transitions to Z";
- "build_tenant is exactly the purpose of bounding the requirements ( aka requirements calculus ) to the computation calculus".

Also used:
- the accepted C1 and C2 decisions;
- the C3 Construction Contract as accepted on 2026-10-12;
- the installed predecessor `stdo://releases/v2.5.1-rc.2/`;
- the defects that cross-family and working reviews found in both candidates (listed under expectation 11);
- the writing standard the product owner set for specification surfaces: no floral language, every term defined at first use, roles not names, no product naming by acronym or version.

## Expectations, recorded before the subject is frozen

1. **The owner's pillars are all present and testable.** Each pillar named in the instruction appears with the contribution the reconstruction must account for:
   - the algebraic calculus and the computational calculus, as two distinct reductions;
   - Markov objects;
   - ODD transformations;
   - functional design;
   - the Spec Method and project structure;
   - reference frames;
   - information semantics;
   - evidence and authority.

   A pillar the pen merged, renamed or added is identified as such, with its reason. Each contribution says what a candidate must show for it.
2. **a_c is stated as the owner described it.** a_c is the logic compression of the prose, and it yields constraint surfaces within which work can happen. The specification says:
   - what a constraint surface contains;
   - how it is derived from the owning prose;
   - how prose, model and task views stay faithful to one another;
   - what checks that fidelity.

   It does not overstate what a structural check establishes.
3. **Document boundaries are free.** The specification permits reconstructing member boundaries from responsibilities. It does not require predecessor file names, headings or sequence. It still keeps every material predecessor claim accounted for.
4. **The review work is consolidated and traceable.** There is one list of work, drawn from the reviews and the updated specification, in which each item names:
   - its source finding;
   - the requirement it is tracked to;
   - its subject or line;
   - its status.

   The list covers the findings on both candidates, including this reviewer's review of the frozen Codex candidate and Codex's review of the Claude candidate. A review finding never becomes a requirement merely by being listed.
5. **Neutrality between tenants.** The common WHAT does not encode one tenant's HOW: its file layout, frame format, tooling or chosen premises. A requirement that only one candidate's present design can meet is a defect unless the product owner chose it.
6. **One owner per rule inside the specification.** PRODUCT, requirements, conformance, GOALS and the frame basis do not decide the same question twice or contradict one another. Each new requirement has one owning section and is referred to elsewhere.
7. **Each new requirement is testable.** It has an observable acceptance condition, says what evidence closes it, and states what a candidate must do to fail it. "Demonstrated reduction" and "contraction on actual deciding paths" in particular say what is compared, against what, and how a reviewer decides.
8. **Purpose and proportionality.** Each new obligation names its purpose and the material relation it protects, with no unsupported process overhead. Where a new requirement reopens an accepted C1, C2 or C3 decision, it names that decision and the reason.
9. **Consistency with the method's own laws.** The specification's rules about results, authority, evidence, configuration and recovery agree with what the specification requires candidates to say. It does not, for example, demand a single result algebra while using an unmapped value set itself.
10. **The a_c dependency boundary is kept.** The theory, interpretation, carrier and checker keep separate identities. Selecting and running a checker remains a separate decision.
11. **Known defects are closed or tracked.** Each item below is either resolved in the specification or tracked in the work list:
    - the open ambiguities recorded by both lines' expectation writers;
    - this reviewer's findings H1 to H4 and M1 to M7 on the Codex candidate;
    - Codex's findings F1 to F5 on the Claude candidate;
    - the ported-part review policy, which is still an open owner decision.
12. **Writing.** Plain and direct throughout, every term defined at first use, roles not names, and no product naming by acronym or version in prose.
13. **Process.** The subject is frozen at a named commit, with a record of what changed since the previous round, and the product owner's sign-off is the closure condition.

## Rounds

None yet. Each round will add a section holding:
- the frozen commit and the diff from the previous round;
- findings ranked by severity, each with evidence and the smallest repair;
- the state of every earlier finding: closed, still open, or new.
