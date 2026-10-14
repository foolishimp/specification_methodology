# REVIEW: Iteration 3 common specification, review rounds

**Author**: Dimitar Popov
**Date**: 2026-10-14T01:32:33Z
**Addresses**: the common specification `specification_methodology/v3/specification/` for iteration 3, at the commit the common pen names as frozen for each round
**Status**: Round 1 complete (subject `7c058ed`). Round 2 expectations recorded (subject `55bbf9e`), before its diff is read. Expectations for round 1 were committed at `f4007ce`, before that subject was read.
**Updated**: 2026-10-14T01:50:05Z

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

Each round adds a section holding:
- the frozen commit and the diff from the previous round;
- findings ranked by severity, each with evidence and the smallest repair;
- the state of every earlier finding: closed, still open, or new.

## Round 1: subject `7c058ed`

### Subject and scope

The subject is the common specification and the consolidated work list at `7c058ed52b9f3cdecf6277026be5d18507efc527`, as the pen's [handoff](../codex/20261014T012413Z_HANDOFF_I3_FOR_CLAUDE_REVIEW.md) names it:
- `specification/` in full;
- the work list `.ai-workspace/tickets/active/T-002-iteration-3-work.md`;
- T-001, T-002, T-002-CODEX and T-002-CLAUDE, read for authority and status.

The comparison is with `a7eba66`, the basis both lines built revision 2 against: 9 files changed in `specification/`, with 108 insertions and 30 deletions.

Not reviewed in this round: the Codex implementation checkpoint `d832a51`. The handoff marks it as a separate subject whose I3 qualification is unfinished.

Four Claude reviewers each covered part of the expectations, working from `git archive` copies of the subject. Their full reports are in [round-1 assets](assets/20261014T013233Z_i3_review/round-1/):

| Report | Expectations covered | Findings |
|---|---|---|
| [SR1](assets/20261014T013233Z_i3_review/round-1/SR1.md) | 1, 2, 3, 8, 10 | 13 |
| [SR2](assets/20261014T013233Z_i3_review/round-1/SR2.md) | 6, 9, and the handoff's consistency question | 25 |
| [SR3](assets/20261014T013233Z_i3_review/round-1/SR3.md) | 4 and 11, the work list | 12 |
| [SR4](assets/20261014T013233Z_i3_review/round-1/SR4.md) | 5, 7, 12, 13 | 19 |

The synthesis re-read the subject for the pillar table (`PRODUCT.md:39–49`) and for criterion 3 on superseded relations (`PRODUCT.md:380`) before relying on them.

### Verdict

The specification is not ready for sign-off. One finding is blocking and about twenty are material; the rest are minor.

The architecture of the update is sound:
- every new requirement has a declared owner, and PRODUCT summarises each requirement accurately;
- the a_c and constraint-surface text is complete and does not overstate structural checks;
- reconstructing member boundaries is permitted while every predecessor claim stays accounted for;
- no new requirement can be met by only one candidate's present design;
- the work list accounts for every finding on the Codex candidate, with no false closure.

The gaps are in four places:
- the owner's pillar list;
- whether the reduction and a_c requirements can be tested and are wired into acceptance;
- the rules of the acceptance process itself;
- a work list that covers only one of the two lines.

Most corrections land in work item I3-00, which the list marks COMPLETE and which needs reopening.

### Results against the expectations

| # | Expectation | Result | Evidence |
|---|---|---|---|
| 1 | The owner's pillars are present and testable | Falsified | No pillar is the algebraic calculus. The computational calculus is folded into "Computational realisation" (`PRODUCT.md:47`), which covers execution binding. "Axiomatic calculus" is added and "Functional design and algebra" merged, with no reason given anywhere (SR1 Q1) |
| 2 | a_c stated as the owner described it | Holds in definition; indeterminate in acceptance | The definition is complete and modest (SR1 Q2). Whether C3 acceptance checks the interpretation, and which theory it models, is not stated (SR1-03, SR1-04; SR4 T-3) |
| 3 | Document boundaries are free | Mostly holds | Reconstruction is permitted, but a conserved claim takes one successor locus only, and the tier table's member lists read as binding (SR1-06, SR1-07) |
| 4 | Review work consolidated and traceable | Falsified for the Claude line | Every finding on the Codex candidate is carried. None of Codex's F1–F5 on the Claude candidate is carried, and nor are the Claude line's obligations under the new standard (SR3; interested) |
| 5 | Neutrality between tenants | Holds | No new requirement favours one candidate's design (SR4 Q1) |
| 6 | One owner per rule in the specification | Falsified on several pairs | SR2 Q1, for example the acceptance composition and the reviewers' write territory below |
| 7 | Each new requirement testable | Falsified for reduction | No pass rule. "Deciding path", the acquisition measure and the "preceding" candidate are undefined, and "where available" allows the comparison to be skipped. Criterion 6 is judged per member, but reduction spans members (SR4 T-1, T-2; SR2) |
| 8 | Purpose and proportionality | Falsified | Changes to accepted items are recorded nowhere: criteria 3, 4 and 6 (approved at C2) and the Mission sentence. The two new requirements lack the purpose paragraph the specification itself demands (SR1-10, SR1-11) |
| 9 | Consistent with its own laws | Falsified | The frame basis's review result set, "supported, contradicted or unresolved" (`REFERENCE_FRAME_BASIS.md:24`), has no mapping into the result algebra (SR2-03) |
| 10 | a_c dependency boundary kept | Holds | SR1 Q2 |
| 11 | Known defects closed or tracked | Partly | The Codex-line findings are tracked. The Claude-line findings and owner decisions are not (SR3) |
| 12 | Writing | Holds with minor findings | SR4 Q4 |
| 13 | Process | Falsified | I3-00 is marked COMPLETE without the owner's sign-off as its closure condition, and GOALS has no row for it (SR4 P-1) |

### Findings

#### Blocking

**B1. No rule says who accepts a `superseded` successor relation, and member acceptance depends on it.** (SR2-01, SR4 T-4)
- Criterion 3 requires every `superseded` row to name "the accepted successor relation", and "Proposed replacements remain pending until accepted" (`PRODUCT.md:380`).
- A member is accepted only when every row is disposed.
- The installed UP-020 rule bars the Executive from accepting a change of meaning.

As written, no member that supersedes anything can be accepted. Smallest correction: reserve acceptance of replacement relations to the product owner, recorded before the member's `accept`, or name another acceptor explicitly. (Work item I3-00; it also unblocks I3-06.)

#### Material

1. **Pillars.** (SR1 Q1, Q5; SR1-02)
   - Align the pillar table with the owner's list: make the algebraic and computational calculi distinct pillars, or record why they are folded or renamed.
   - Record the reason for adding "Axiomatic calculus" as a pillar.
   - Link the pillars to the principles accepted at C1.
   - The owner's list exists only as the pen's paraphrase. Ask the owner to confirm the list verbatim before the next round.
2. **Reduction cannot yet be decided the same way twice.** (SR4 T-1, T-2; SR2)
   - Give "demonstrated reduction" a pass rule.
   - Define "deciding path", what "acquisition" measures, and which candidate is "preceding".
   - Remove the "where available" escape.
   - Add a whole-candidate reduction check, because criterion 6 per member cannot detect contraction that spans members.
3. **a_c and constraint surfaces are outside acceptance.** (SR4 T-3; SR1-03, SR1-04)
   - Put constraint-surface and a_c fidelity obligations into the C3 outcome, a criterion and the closure rule.
   - Say whether a partial interpretation can pass, and what it must declare.
   - Name the theory the interpretation models: the installed `a_c` rules, or a successor.
4. **Reopened decisions are unrecorded.** (SR1-10, SR1-11) List each accepted C1, C2 or C3 item the update changes, with the reason, and add the purpose paragraph to each new requirement.
5. **Acceptance composition.** (SR2-02) PRODUCT accepts a member on one `satisfied` result (`PRODUCT.md:195`), but the Reviewer returns one result per criterion (`REFERENCE_FRAME_BASIS.md:28`). State the conjunction rule once.
6. **The specification's own result set.** (SR2-03) Map "supported, contradicted, unresolved" into the core, or replace it with core values plus a domain outcome.
7. **Process and authority.** (SR2; SR4 P-1)
   - `.ai-workspace/` is reserved to the common pen, but reviewers must write their reports there. Say which surfaces each role writes.
   - The rule "a merge implies acceptance" conflicts with the owner-directed merge `a9adce2`. Record that merge as an owner variance.
   - Define "author" for reviewer independence: the tenant or the activation.
   - Make the owner's sign-off the closure condition of I3-00, and give it a GOALS row.
8. **The work list covers one line.** (SR3; interested: these findings concern the Claude line)
   - Either add a Claude-line section, or scope the claim at `GOALS.md:11` ("traces every remaining requirement and review finding") to the Codex line.
   - A Claude-line section would carry Codex's F1–F5, with their state on the Claude branch: F1, F2, F4 and F5 repaired and pending cross-family confirmation, F3 open. It would also carry the new standard's obligations for that line.
   - Codex's review of the Claude candidate is not committed on any branch. The pen should commit it so that it can be cited.
9. **Work-list mechanics.** (SR3-03, SR3-05, SR3-06, SR3-07)
   - The consolidation review checked coverage only against the list's own keys.
   - Owner decisions are treated as work or left untracked: acceptance-review assignment, compressions, identifiers, candidate number and cohort.
   - Findings routed to several items have no rule for when they close.
   - I3-02, I3-05 and I3-11 ask for less than the reduction requirement does (`requirements/README.md:57–58`).
10. **Boundaries.** (SR1-06, SR1-07) Allow a conserved claim more than one successor locus. Say whether the tier table's member lists bind, or only illustrate.

#### Minor

About 45 further findings, including undefined terms, wording and cross-reference gaps, are in the four reports with locations and corrections.

### Required corrections, in order

1. Name the acceptor of replacement relations (B1).
2. Settle the pillar list with the owner and record reasons for any merge, rename or addition (M1).
3. Give reduction a pass rule, definitions and a whole-candidate check (M2).
4. Wire a_c and constraint-surface fidelity into the C3 outcome, criteria and closure (M3).
5. Record reopened decisions, and add purpose paragraphs (M4).
6. State the acceptance conjunction, and map the frame basis's result set (M5, M6).
7. Fix the process rules: write territories, the merge variance, "author", and I3-00 closure (M7).
8. Complete the work list for the Claude line, or scope its claim, and correct its mechanics (M8, M9).
9. Correct the boundary rules (M10).

### Independence and limits

Claude is a tenant governed by this specification. Findings M8 and SR4 N-1 concern the Claude line and are marked interested. Several new clauses respond to Claude's own earlier findings on the Codex candidate (H1, H2), and judging those clauses is not fully independent.

The reviewers sampled `PREDECESSOR_CLAIMS.md` rather than reading every row, and read neither candidate. They read Codex's review of the Claude candidate from the working tree, identified by its SHA-256, because it is uncommitted. Nothing in this round selects repairs. The pen repairs, the next frozen commit is round 2, and the product owner's sign-off closes the review.

## Round 2: expectations, recorded before reading the diff

The pen's [round 2 handoff](../codex/20261014T033341Z_HANDOFF_I3_SPECIFICATION_ROUND_2.md) names the subject: `55bbf9ee7bc8e37235ef0588f9afea0f8ccbabbc`. It is compared with `afb6ad6`, whose specification equals round 1's `7c058ed`. The handoff was read before these expectations were written; the diff and the corrected text were not.

A round 1 finding closes only when the corrected text meets its expectation below:

- **B1:** a named acceptor (the product owner or another explicitly named authority) accepts each replacement relation. The acceptance is recorded before the dependent member's `accept`, and no other route leaves a superseded row pending forever.
- **M1:**
  - The algebraic calculus and the computational calculus are distinct pillars, each with what a candidate must show.
  - Each merge, rename or addition carries its reason.
  - The pillars are linked to the C1 principles.

  Whether the owner's list needs his verbatim confirmation is his decision. The pen declined to ask, and this review reports that decline rather than treating it as closed.
- **M2:**
  - Reduction has a pass rule a second reviewer would apply the same way.
  - "Deciding path", the acquisition measure and the "preceding" candidate are defined.
  - Nothing lets the comparison be skipped.
  - A whole-candidate check exists alongside the per-member criterion.
- **M3:** constraint-surface and a_c fidelity are in the C3 outcome, a criterion and the closure rule. Partial coverage is either barred or declared with its limits. The theory being modelled is named.
- **M4:** each changed accepted item (C1, C2, C3 and the Mission sentence) is listed with its reason, and each new requirement has its purpose paragraph.
- **M5:** one stated rule combines per-criterion results into member acceptance, and adverse or missing evidence cannot be absorbed.
- **M6:** the frame basis's review result set maps into the core, or is replaced by core values with a domain outcome.
- **M7:**
  - Each role's write surfaces are stated.
  - The owner-directed merge is recorded as a variance, or the rule is reconciled with it.
  - "Author" is defined for reviewer independence.
  - I3-00 closes only on the owner's sign-off, with a GOALS row.
- **M8 (interested):** either the work list carries the Claude line (Codex's F1–F5 with their current state, and the new standard's obligations for that line), or the GOALS claim is scoped to what the list covers. Codex's review of the Claude candidate is committed.
- **M9:**
  - Coverage is checked against the source reports, not only the list's own keys.
  - Owner decisions are tracked as decisions.
  - Findings routed to several items have a closure rule.
  - I3-02, I3-05 and I3-11 match the reduction requirement.
- **M10:** a conserved claim may have more than one successor locus, and the tier table's member lists are stated as binding or as illustrative.
- **No regressions:** the repair text introduces no new contradiction, untestable obligation, second owner or naming in prose. It does not reopen a round 1 "holds" result (expectations 5, 10 and 12).
