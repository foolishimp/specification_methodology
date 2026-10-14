# REVIEW: Iteration 3 common specification, review rounds

**Author**: Dimitar Popov
**Date**: 2026-10-14T01:32:33Z
**Addresses**: the common specification `specification_methodology/v3/specification/` for iteration 3, at the commit the common pen names as frozen for each round
**Status**: Round 3 complete (subject `355aa86`, with the admissions recorded at `651581c`; expectations at `eff198e`). Round 2 complete (`55bbf9e`; `81695e5`). Round 1 complete (`7c058ed`; `f4007ce`).
**Updated**: 2026-10-14T04:31:25Z (round 2 findings)

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

## Round 2: findings, subject `55bbf9e`

### Scope

The subject is the corrected specification and work list at `55bbf9ee7bc8e37235ef0588f9afea0f8ccbabbc`, compared with `afb6ad6`. The changes cover 13 files, with 219 insertions and 97 deletions. Also read:
- the pen's [disposition record](../codex/20261014T030729Z_REVIEW_I3_ROUND_1_DISPOSITION_AND_REPAIR.md) for every round 1 finding;
- its three working reviews.

`cab9800`, which adds the handoff and edits GOALS status lines, lies outside the frozen subject.

Three Claude reviewers split the work. Their reports are in [round-2 assets](assets/20261014T013233Z_i3_review/round-2/):
- [RR1](assets/20261014T013233Z_i3_review/round-2/RR1.md): closure of B1, M1 to M5 and M10;
- [RR2](assets/20261014T013233Z_i3_review/round-2/RR2.md): M6 to M9, the disposition record and the working reviews;
- [RR3](assets/20261014T013233Z_i3_review/round-2/RR3.md): a regression pass over every changed line.

### Verdict

The round made substantial progress, but the specification is not yet ready for sign-off.

- The blocking finding is closed.
- Six of the ten material groups are closed, and four are partly closed.
- The disposition record accounts for all 69 round 1 findings and the nine ambiguities: 62 repaired, 5 narrowed, 2 declined. Both declines hold in part, and four of its labels misstate what was done (RR2).
- The repair text introduced seven new material defects. They are narrow, but two touch rules the owner selected, and one breaks a recorded contract digest.

### State of the round 1 findings

| Finding | Round 2 state | Evidence |
|---|---|---|
| B1, acceptor of replacement relations | **Closed** | The product owner accepts each replacement relation before the dependent member is accepted (`PRODUCT.md:202`). Declining to let member acceptance carry the replacement is sound under the installed UP-020 (RR1) |
| M1, pillars | **Partly closed** | The algebraic and computational calculi are now distinct pillars, linked to the C1 principles. Still missing: a reason for the "Axiomatic calculus" row and for four renamed or broadened rows. `INTENT.md:13` names the pillars differently (RR1) |
| M1, owner's pillar list | **Open, the owner's decision** | The pen declined to ask for the owner's confirmation. The only owner words on record are the instruction sentence, and the list is the pen's paraphrase (T-001:45). A second paraphrase by the pen omits the algebraic calculus. The owner's sign-off can confirm `PRODUCT.md:39–50` (RR1) |
| M2, reduction testable | **Partly closed** | Definitions, a pass rule and a whole-candidate check now exist. New gap RR1-N2: no rule decides whether more acquisition defeats a reduction, or which deciding paths must be compared |
| M3, a_c in acceptance | **Closed** | RR1 |
| M4, reopened decisions recorded | **Partly closed** | Four contract changes are unlisted, two of which move owner decisions earlier. The constraint-surface requirement still states no purpose (RR1). See also RR3-05 |
| M5, acceptance composition | **Closed** in intent | See RR3-04 for its fit with the installed builder |
| M6, the frame basis's result set | **Closed** | The frame basis now returns the installed evaluation (RR2) |
| M7, process and authority | **Closed** | All four points are in the text (RR2) |
| M8, work list covers one line | **Closed by scoping** (interested) | GOALS now limits the list's claim to the Codex line. Codex's review of the Claude candidate is committed byte-identical, and F1 to F5 are indexed as unassessed. The Claude line's iteration 3 obligations are tracked nowhere, which fits the fact that its iteration 3 is not admitted (RR2) |
| M9, work-list mechanics | **Partly closed** | Decision tracking, the closure rule and the three items are fixed. Coverage is still checked against a packet the list defines itself, and the reviews it leaves out go unnamed (RR2-08) |
| M10, boundaries | **Closed** | RR1 |

### New findings from the repair text (RR3)

All seven are material and none is blocking.

1. **RR3-01. Member acceptance now has two records, and the author writes one of them.** The new frontier text and the predecessor-claims header put acceptance standing in the tenant's own frontier, which the author tenant writes (`PRODUCT.md:332`; `PREDECESSOR_CLAIMS.md:673`). The unchanged `PRODUCT.md:249–250` says the ticket, written by the pen, is the only record of a disposition. Correction: the tenant frontier records proposed dispositions; acceptance standing lives only in the ticket.
2. **RR3-02. Three new conformance rows are process checks in a per-member table.** Criterion 5's table separates correct candidates from defective ones (`conformance/README.md:3`). Row 60 can pass or fail no candidate text, and row 12 lets two reviewers reach different member decisions. Correction: move these rows to the process or closure rules they test.
3. **RR3-03. Criterion 4's limit test cannot be decided the same way twice.** Acquisition through declared routes is now allowed, but the Limits paragraph speaks only of context "measured before reading". Correction: say whether routed acquisition counts against the declared limit, and when it is measured.
4. **RR3-04. The Reviewer's return does not match the installed builder.** The installed Reviewer returns one closed evaluation with one result. PRODUCT now asks for a six-result return and an "applicable mandatory" conjunction, and the installed builder governs where the two differ (`PRODUCT.md:321`). Correction: state the per-criterion results as refinements whose conjunction yields the installed single result, or record the variance.
5. **RR3-05. The record of changed accepted items omits this round's own changes.** Among them:
   - criterion 1 now requires "all successor loci" and drops "that resolves";
   - a change to Development Isolation, which is a local axiom;
   - a change to the single-ownership law the owner selected.

   Correction: list each with its reason. The two owner-level changes need the owner's explicit acceptance.
6. **RR3-06. An admitted contract was edited in place.** T-002-CODEX still records the block as the admitted contract under digest `fc6ed…`, but its bytes now hash to `bf1557…`. The installed ticket method makes the digest the evidence of admission. Correction: restore the admitted bytes and record a successor contract with its own digest and admission.
7. **RR3-07. The closure rule conflicts with the new work-list rows.** The first-listed item is primary under the new rule, but the new H-M rows give a second primary for findings already routed above: CR2-04 and CR2-09, CR2-21, CR4-F3, CR5-04 and CR5-06. TC-03 is therefore not closed, although `T-001:37` records it as repaired. Correction: give each finding one primary item, and correct the TC-03 record.

The reports list a further 13 minor findings from RR3 and low findings RR2-01 to RR2-08. RR2-01 asks whether the next tenant input waits for sign-off, and matters when that input is selected.

### What holds

- Expectation 5 (neutrality between tenants) holds.
- Expectation 10 (the a_c dependency boundary) holds and is strengthened, with minor drift at `requirements/README.md:162` and `A_C_DEPENDENCY.md:43`.
- Expectation 12 (writing) holds, with minor findings.
- The three working reviews are accurate within their stated scopes. None of them checked SR1-09 to SR1-11, SR1-13 or SR4's N, T-5 to T-7, P and W findings, which include both declines (RR2).

### Required corrections for round 3

1. Remove the second acceptance record (RR3-01). Restore the admitted contract's bytes, and record any successor contract separately (RR3-06).
2. List every changed accepted item, including this round's changes, with reasons. Bring the Development Isolation change and the single-ownership law change to the owner for explicit acceptance (RR3-05, M4).
3. Fit the per-criterion results to the installed Reviewer's single result, or record the variance (RR3-04).
4. Move the process-only conformance rows out of criterion 5 (RR3-02). Decide whether routed acquisition counts against the limit (RR3-03).
5. Give each finding one primary work item, correct the TC-03 record, and name the reviews the coverage packet leaves out (RR3-07, RR2-08).
6. Record reasons for the "Axiomatic calculus" row and the renamed pillars, and align the INTENT naming (M1).
7. Add a rule on acquisition growth and on which deciding paths must be compared (RR1-N2).
8. Add the purpose paragraph to the constraint-surface requirement (M4).

Two decisions are the product owner's:
- whether to confirm the pillar list at `PRODUCT.md:39–50` as his own;
- whether to accept the two owner-level changes in RR3-05.

### Independence and limits

Claude is a governed tenant. M8 and some RR3 wording judgements concern the Claude line, or wording the pen adopted from Claude's round 1 corrections; the reports mark them interested. The reviewers read the subject from `git archive` copies at `55bbf9e`, sampled the predecessor-claims rows, and read neither candidate.

## Round 3: expectations, recorded before reading the diff

**Subject.** `355aa8655cca9c6ba6cf5c414f9bea3032ae89fd`, "Repair I3 round-two common contract and prepare tenant successors". It is the shared input `C3-I3-R2-01` that both tenants' iteration 3 contracts bind (T-002; `EC-CLAUDE-I3-01` in T-002-CLAUDE). The comparison is with round 2's `55bbf9e`: 8 specification files, with 98 insertions and 51 deletions. After `355aa86`, `main` changes only GOALS status lines up to `65c0210`, and this round reads them as status only.

**Authority.**
- The product owner instructed the pen to "do that close the round 2 findings" (recorded in T-001).
- He then answered this reviewer: "Wait for round 3 (Recommended)" before sign-off, and "Claude line" for iteration 3.
- GOALS records "Final common sign-off remains open".

**What closes each round 2 item.** A round 2 required correction or partly closed finding closes only when the text at `355aa86` meets it:

1. **RR3-01:** acceptance standing has one record, the ticket written by the pen. The tenant frontier records proposals only.
2. **RR3-06:** the admitted contract's bytes match its recorded digest. Any successor contract has its own digest and admission. This applies to every contract admitted at or before `355aa86`, including `EC-CLAUDE-I3-01`.
3. **RR3-05 and M4:** every accepted item changed since `a7eba66` is listed with its reason, including round 2's own changes. The Development Isolation change and the single-ownership law change are presented for the owner's explicit acceptance, not applied as accepted. The constraint-surface requirement has its purpose paragraph.
4. **RR3-04:** the per-criterion results fit the installed Reviewer's single result, or the variance is recorded.
5. **RR3-02 and RR3-03:** process-only conformance rows are out of criterion 5. Whether routed acquisition counts against the limit is decided.
6. **RR3-07 and RR2-08:** each finding has one primary work item, the TC-03 record is correct, and the reviews left out of the coverage packet are named.
7. **M1:** reasons are recorded for the "Axiomatic calculus" row and the renamed pillars, and INTENT's pillar naming agrees with PRODUCT. Confirming the pillar list remains the owner's decision.
8. **RR1-N2:** a rule decides whether more acquisition defeats a reduction, and which deciding paths must be compared.
9. **No regressions:** the repair text introduces no new contradiction, untestable obligation, second owner, retroactive rebinding or naming in prose, and earlier "holds" results stay held.

**Also checked.** Whether the tenant contracts admitted at `355aa86` are consistent with the specification they bind: territory, authority, comparison baselines, and resource and acceptance limits. One of them, `EC-CLAUDE-I3-01`, governs this reviewer's own line, so judgements on it are marked interested.

## Round 3: findings, subject `355aa86` and records at `651581c`

### Correction to this review's own record

The round 3 expectations said that after `355aa86`, `main` changes only GOALS status lines. That holds only for `specification/`. Commit `651581c` also changes the tickets: it records the shared input snapshot and admits both tenant contracts.

The expectations also assumed that `EC-CLAUDE-I3-01` was admitted by `355aa86`. It was still a draft there. It was admitted at `651581c`, with a digest equal to its `355aa86` bytes.

This round reviews both commits: the specification at `355aa86`, and the admissions at `651581c` as records about it.

### Scope and reports

The subject was read from `git archive` copies. Two Claude reviewers each covered part of the expectations. Their reports are in [round-3 assets](assets/20261014T013233Z_i3_review/round-3/):
- [RT1](assets/20261014T013233Z_i3_review/round-3/RT1.md): closure of the round 2 corrections, contract digests, and the pen's [round 2 disposition record](../codex/20261014T064039Z_REVIEW_I3_ROUND_2_DISPOSITION_AND_REPAIR.md);
- [RT2](assets/20261014T013233Z_i3_review/round-3/RT2.md): a regression pass over the 770 changed lines, and the tenant contracts against the specification.

### Verdict

The specification text is close to ready for sign-off. Seven of the eight round 2 corrections are closed and one is partly closed. Of the 35 rows in the round 2 disposition record, 34 hold against the text. No blocking finding remains in the text.

What is left concerns governance more than content:
- One regression removes the product owner's sign-off from I3-00's exit.
- The changes to accepted conditions are listed, but none is put to the owner as an item to accept, and two are still unlisted.
- The Claude-line contract was admitted without an owner-selected admitting activation. The owner's recorded words do not decide when it starts.

These are owner decisions and narrow recording repairs.

### State of the round 2 corrections (RT1)

| Correction | State |
|---|---|
| RR3-01, one acceptance record | **Closed** |
| RR3-06, admitted contract bytes | **Closed**. Every admitted EC-CODEX digest reproduces, at `355aa86` and at its original admission commit. Two records with no stated byte range reproduce only by inference (minor) |
| RR3-04, Reviewer result shape | **Closed**. The Reviewer returns one closed evaluation, and its overall result is the conjunction of the six criterion judgements under the installed Result Conjunction (`PRODUCT.md:202`) |
| RR3-02 and RR3-03, process rows and routed acquisition | **Closed** |
| RR3-07 and RR2-08, one primary per finding, TC-03, packet coverage | **Closed** |
| M1, pillar reasons and INTENT alignment | **Closed**. T-001 now records the owner's pillar inputs and the reasons for the table's groupings. Whether to confirm the pillar list remains the owner's decision |
| RR1-N2, acquisition growth and deciding paths | **Closed** |
| RR3-05 and M4, changed accepted items and purpose | **Partly closed** (see the next list) |

What remains open under RR3-05 and M4:
- **Not put to the owner.** GOALS lists nine changes to accepted conditions with reasons (`GOALS.md:46–54`), including Development Isolation, a local axiom, and single ownership items 2 and 4. It states that "the historical C1/C2 dates do not accept these later bytes". None of the changes is put to the owner as a named item to accept, although they already govern construction through the input admitted at `651581c` (RT1-01).
- **Two changes still unlisted** (RT1-02):
  - the owner's actor-binding reservation;
  - criterion 5's new a_c obligation.
- **Mislabelled table.** It is headed "round-1-to-round-2", but its rows also describe the `355aa86` changes.

### New findings (RT2)

1. **RT2-03 (material, regression): I3-00 no longer requires the owner's sign-off to close.** A gate sentence in T-001 was rewritten in place, and I3-00 is marked "CLOSED FOR CONSTRUCTION". GOALS still says "Final common sign-off remains open". This reopens round 1's M7, which round 2 had recorded closed. Correction: I3-00's exit is the owner's sign-off. Construction under the owner's instruction may proceed meanwhile, and that standing is recorded as such.
2. **RT2-01 (material, interested): the admitting activation for `EC-CLAUDE-I3-01` is not one the owner selected.** It was admitted by the Executive role of the Codex common-pen activation (`651581c:T-001:47`). The contract itself names the Claude tenant session as that line's Executive, and the frame basis requires the owner, or an activation he selects, to admit. Correction: the owner confirms or re-admits the contract, and the pen records his decision.
3. **RT2-02 (material, interested): the owner's recorded words do not decide when the Claude-line contract starts.** "Do that close the round 2 findings" supports preparing both contracts. Starting before sign-off, on `355aa86`, is the pen's reading; starting after sign-off is the Claude Executive's. The owner's later answers to this reviewer ("Wait for round 3", "Claude line") are recorded only in the Claude tenant ledger, not in any ticket. Correction: the pen records those answers verbatim in T-002-CLAUDE.

Minor findings are in the two reports.

### What holds

- **Both tenant contracts.** They are symmetric line by line and consistent with the specification they bind. Their digests and the 24 input hashes reproduce, and Codex's admission is lawful apart from the unnamed actor in RT2-01 (RT2).
- **Earlier holds.** Neutrality, the a_c dependency boundary and the writing standard still hold, and nothing is presented as signed off.

### Decisions for the product owner

1. **Accept the changes to accepted conditions.** Accept or reject, as named items, the nine changes at `GOALS.md:46–54`, plus the two unlisted ones in RT1-02. Development Isolation is a local axiom, and single ownership items 2 and 4 is a law the owner selected; both need his explicit word.
2. **Confirm the pillar list** at `PRODUCT.md:39–50` against his inputs as recorded in T-001.
3. **Decide the Claude-line contract.** Confirm or re-admit `EC-CLAUDE-I3-01`, and say when it starts. His answer to this reviewer was "Claude line", to start after round 3 and sign-off.
4. **Sign off the specification** at `355aa86`, once the pen restores sign-off as I3-00's exit (RT2-03). Signing off with decisions 1 to 3 recorded is enough to close this review.

### Independence

Claude is a governed tenant, and RT2-01 and RT2-02 concern its own line. Most round 3 closures adopt wording from this review's round 2 reports, so under `PRODUCT.md:401` they are defect rechecks, not independent acceptance.
