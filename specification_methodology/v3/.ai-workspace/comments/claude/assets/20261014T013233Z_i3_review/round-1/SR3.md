# SR3: Cross-family review of the iteration 3 consolidated work list

**Reviewer**: a Claude context acting as cross-family Reviewer. It repairs nothing.
**Subject**: the work list `T-002-iteration-3-work.md`, frozen at `7c058ed`, with T-001, T-002, T-002-CODEX, T-002-CLAUDE and `specification/` at the same commit.
**Scope**: expectations 4 and 11 of the review-expectations post, and the handoff question: does the work list account for the review findings and the updated standard, with adequate closure evidence?

## Independence disclosure

- The work list carries findings that Claude made: H1–H4, M1–M7, minors and CR1–CR5. S was also produced by a fresh Claude context (T2X:168).
- The work list also concerns the Claude candidate, through Codex's F1–F5.
- Every judgment about how Claude's findings or the Claude line are represented is marked **interested**.
- No context in this review authored the work list or either candidate. The Reviewer does share a model family with the authors of the Claude candidate, Hrep and S.

## Path keys

- Subject files under `$S/subject/specification_methodology/v3/`:
  - `.ai-workspace/tickets/active/`:
    - **WL**: `T-002-iteration-3-work.md`
    - **T1**: `T-001-common-definition-and-checkpoints.md`
    - **T2**: `T-002-c3-successor-construction.md`
    - **T2X**: `T-002-CODEX-…`
    - **T2C**: `T-002-CLAUDE-…`
  - `specification/`:
    - **P**: `PRODUCT.md`
    - **R**: `requirements/README.md`
    - **C**: `conformance/README.md`
    - **G**: `GOALS.md`
- Reports, read at `7c058ed` under `v3/.ai-workspace/comments/`:
  - **Hrep**: `claude/20261013T235754Z_REVIEW_CODEX_V3_FROZEN_CANDIDATE.md`
  - **CR1–CR5** and **EXP**: `claude/assets/20261013T235754Z_codex_review/`
  - **E**: `codex/20261013T234239Z_…`
  - **AR**: `codex/20261013T234754Z_…`
  - **S**: `codex/20261014T003000Z_ITERATION_3_SOURCE_REVIEW/REVIEW.md`
  - **K**: `codex/20261014T004200Z_…`
  - **AC**: `codex/20261014T010500Z_…`
  - **CC**: `codex/20261014T001000Z_…`
  - **CON**: `codex/20261014T011752Z_…`
- **Frep**: `codex/20261014T000519Z_REVIEW_CLAUDE_V3_REVISION_2_PURPOSE_AND_IMPLEMENTATION.md`. It is **not present at `7c058ed`**: `git cat-file -e` fails. It is untracked in the working tree, 27,817 bytes, SHA-256 `758baef0ed7c14fc9afae3695fba1f39765c05c7cf88e1fde09383f0d8012fe8`. `git log --all -- <path>` returns nothing, so it is in no commit on any ref. Its own record says "nothing was committed" (Frep:220). It is dated 2026-10-14T00:05:19Z, 65 minutes before the consolidation commit `6c2debb` (01:10:12Z), so the omission is not a late arrival.
- **XP**: the review-expectations post `claude/20261014T013233Z_REVIEW_I3_COMMON_SPECIFICATION.md`. It is dated 01:32:33Z, after the subject commit (01:22:38Z). It is used for scope and as later context, not as a standard the frozen subject could have met.

## Verdict

**Codex candidate.** The work list accounts for every finding on the Codex candidate in its packet:
- E 3;
- CR 60, reached through H1–H4 and M1–M7;
- S 10;
- AC 1.

Its R-trace resolves. The status vocabulary separates returned repair from proof and acceptance.

**Expectation 4 and the handoff question: not met.**
- The work list omits all five findings that Codex made on the Claude candidate.
- No surface in the subject tracks the updated standard's work for the Claude candidate.
- The completeness check was run against the work list's own packet, so it could not detect either omission.

**Expectation 11.**
- H1–H4 and M1–M7 are tracked. The M items are tracked only through their CR constituents.
- F1–F5 are untracked.
- The ported-part policy is tracked only inside work items.
- Four of the nine expectation-writer ambiguities (A4, A5, A6, A8) are neither resolved nor tracked.

## Coverage table

| Report (candidate examined) | Finding IDs | Carried (named) | Merged | Omitted | Evidence |
|---|---|---|---|---|---|
| E, Codex reviewing its own iteration 2 | F1–F3 | 3 | 0 | 0 | WL:44, WL:115 |
| AR, applicability record (Codex) | confirms E F1–F3; no new ID | — | 3, via E | 0 | AR:9–13; not keyed in WL:42–48, but its substance sits in E's key |
| Hrep principal (Codex), *interested* | H1–H4 | 4 | 0 | 0 | WL:90 (H1), :92 (H2), :95 (H3), :99 (H4); WL:116, :120, :127, :130 |
| Hrep medium (Codex), *interested* | M1–M7 | 0 | 7 | 0 | Mapped only through CR IDs, Hrep:125–144 → WL:116–136 (crosswalk below) |
| Hrep minor rows (Codex), *interested* | 8 rows | 0 | 8 | 0 | Hrep:150–157 → CR3 F-4–F-9, CR2-10–19, CR4 F5/7/8, CR5-11/12 |
| Hrep process note (Codex), *interested* | merge variance | 1 | 0 | 0 | Hrep:171 → CR5-05 → I3-16, WL:132 |
| CR1 | F1–F8 | 8 | 0 | 0 | WL:116–119 |
| CR2 | 01–21 | 21 | 0 | 0 | WL:120–123 |
| CR3 | F-1–F-9 | 9 | 0 | 0 | WL:124–126 |
| CR4 | F1, F2, F2b, F3–F8 | 9 | 0 | 0 | WL:127–129 |
| CR5 | 01–13 | 13 | 0 | 0 | WL:130–136 |
| S (Codex, Claude-family reviewer), *interested* | 1–10 | 10 | 0 | 0 | WL:47, WL:137–139. S's open item on the old entry defects (S:158–167) is merged into I3-08. |
| K (Codex) | none raised | — | — | — | WL:46, WL:141 |
| AC (Codex) | AC-F1 | 1 | 0 | 0 | WL:48, WL:140 |
| CC, common contract review | F1 (low) | 0 | 0 | not in WL | Closed elsewhere: T2X:71, "Finding F1 is resolved by this selection" |
| CON, consolidation review | none | — | — | — | CON:42 |
| **Frep, Codex reviewing the Claude candidate**, *interested* | **F1–F5** | **0** | **0** | **5** | No key in WL:42–48; no index row in WL:113–141; not a member of the I3-02 snapshot (T2:231–262); no entry in T2C after 2026-10-12T15:43 (T2C:257) |

**Symmetry, interested.**
- On the Codex candidate, 74 finding-level IDs are covered: E 3, CR 60, S 10, AC 1. All have a destination.
- On the Claude candidate, 0 of 5 have a destination.
- The asymmetry is structural. WL:6–8 says: "assignments and implementation status below concern Codex only. The peer keeps its own ticket". T2:30 calls the work list the index "for Codex".
- The peer ticket carries nothing either. T2C:30 still reads "State: drafted, not started", and T2C has no iteration 3 entry.

## Q1. Coverage detail

**Frep findings and where the updated standard would anchor them**

None of these findings has a destination in the work list. Each could be tracked under an existing requirement, with no new requirement:

| Finding | Severity | Anchor in the updated standard |
|---|---|---|
| F1: frame revision reopens nothing | High | R:80 ("Admissible contrary evidence reopens the affected claim") |
| F2: unknown termination masks a demonstrated failure | High | R:127 and R:129–132 |
| F3: no current a_c interpretation | High completion gap | R:64–69; C:22 |
| F4: finite oracle misses invalid reported values | Medium | R:70; R:135 |
| F5: frame links broken | Low | R:67, R:69 |

**M crosswalk** (*interested*). Every M maps through its CR constituents to at least one item. None is named.

| M | Constituents (Hrep:125–144) | Destination items |
|---|---|---|
| M1 | CR2-02, 03, 04, 09; CR3 F-3 | I3-02, I3-03, I3-04, I3-05 |
| M2 | CR2-06, 07; CR4 F3; CR5-09 | I3-06, I3-08 |
| M3 | CR4 F4 | I3-07, I3-14 |
| M4 | CR5-02, 03, 04, 06 | I3-10, I3-11, I3-12, I3-14 |
| M5 | CR5-07, CR5-10 | I3-08, I3-09, I3-12 |
| M6 | CR5-08, CR5-13 | I3-13 |
| M7 | CR1 F2, F3; CR2-21 | I3-01, I3-02, I3-03, I3-04, I3-14 |

## Q2. Traceability

| Required element (XP:60–66) | Result | Evidence |
|---|---|---|
| Source finding | Partly. Six rows name a source in-row: I3-01 H1, I3-03 H2, I3-06 H3, I3-10 H4, I3-08 E, I3-09 AC-F1. The rest rely on the reverse index. The index is complete for its packet. It has no per-finding state, and several findings have three or four destinations. | WL:90–105; WL:113–141; WL:110, "A destination is not a finding's closure" |
| Requirement tracked to | Holds. Every row ends with R labels. Labels are disclaimed as new identifiers (WL:52–53). All twelve anchors resolve against the R and P headings. R11 points at the whole conformance file, not at the 16 new rows. | WL:57–68 |
| Subject or line | Weak. Subjects are given as commits (WL:30–34). Rows name members or areas, such as "Ticket sprint close, Release UP-015, Spec UP-021" (WL:92), but cite no lines in the current subject `de8232a`. Lines live only in the original reports, at older subjects. | WL:30–34, WL:89–105 |
| Status | Holds for 16 rows. I3-00 uses COMPLETE, which the vocabulary does not define (WL:79–84). | WL:89 |
| No requirement created by listing | Holds. No row turns a finding into an obligation without an R anchor. | Below |

**No requirement by listing.**
- I3-01 explicitly refuses the 77-law partition (WL:90).
- Several findings correspond to new conformance rows:
  - H1 → C:10
  - M7 / CR2-21 → C:15
  - H3 → C:52
  - H2 → C:51
  - H4 / CR5-02 → C:30
  - AC-F1 → C:21
  - E-F2 / CR5-10 → C:22
- Those rows entered through the common amendment (T1:31, reviewed by CC and CON). They did not enter through the list.
- Limit: their acceptance as common law remains the owner's (T1:65).

## Q3. Closure evidence per item

| Item | State | Closure condition observable? | Who checks; independence | Assessment |
|---|---|---|---|---|
| I3-00 | COMPLETE | Yes | CON: nonauthor, same-family declared exception (CON:10–13); Executive disposition T2:264–270 | Not a false closure against its own exit proof. Spec bytes are unchanged from the reviewed `6c2debb` to input B `7b2f933` (`git diff --stat` is empty). The row itself discloses that owner acceptance is separate (WL:89; T1:65; frame basis row 24, "common acceptance is the product owner's"). Two residual problems: COMPLETE is not in the defined vocabulary (WL:79–84), and the coverage part was checked only against the work list's own keys (CON:34–35). See SR3-03 and SR3-04. |
| I3-01 | OPEN | Yes | "Independent review", family not bound | Adequate condition; checker family unstated (SR3-08) |
| I3-02 | REPAIR RETURNED | Partly | Unnamed | Omits R:57's comparison of decisions and acquisition with rc.2 and iteration 2 (SR3-07) |
| I3-03 | REPAIR RETURNED | Yes | Unnamed | Adequate condition; checker unstated |
| I3-04 | REPAIR RETURNED | Yes | "Independent source comparison" | Adequate. The repair records exist at `de8232a`: `METHOD_REVIEW_REPAIR` 160 lines, `FRAME_REVIEW_REPAIR` 234, `PROFILE_REVIEW_REPAIR` 186. |
| I3-05 | OPEN | Weak | Unnamed | "Appropriate … cases" (WL:94) cannot be checked. Omits "independently specified" (R:58). |
| I3-06 | OPEN | Yes | Implied | Strong. Pending replacements are kept distinct from accepted ones, as P:380 and R:27 require. |
| I3-07 | OPEN | Blocked | Depends on "the selected port-review policy" | The builder cannot meet this until the owner decides (P:394). No decision row records the dependency (SR3-05). |
| I3-08 | OPEN | Partly | "Semantic comparison", checker unnamed | "Initial entry fixes implemented" is the author's claim. S could not verify it (S:158–167). Compressions work presupposes an open decision (SR3-05). |
| I3-09 | OPEN | Yes | "Independent reviewer" | Adequate. "Retrieve residual domain policies when needed" is not a closure condition. |
| I3-10 | OPEN | Yes | Independent oracle author, fresh actors, independent assessment | Strong |
| I3-11 | BOUNDED EVIDENCE | Yes | Proof owner | Honest scope. "Comparison, if claimed" weakens R:57 (SR3-07). |
| I3-12 | OPEN | Yes | Proof owner, author side | Criterion 5's review is routed to I3-14 |
| I3-13 | OPEN / partly RESERVED | Partly blocked | Owner-selected identity policy | The decision is embedded in the exit proof, not tracked as a decision |
| I3-14 | OPEN | Blocked for acceptance-grade results | "Executive selects … independent reviews" | P:393 reserves acceptance-review assignments to the owner, and says no `accept` exists until they and the ported-part policy are resolved (SR3-05, SR3-08) |
| I3-15 | RESERVED, NOT_SELECTED | n/a | Owner | Correctly tracked as a decision |
| I3-16 | RESERVED | n/a | Owner | "Variance is already recorded" cites no locus (SR3-11) |

No item claims closure without its stated evidence. The defects are:
- an undefined COMPLETE label;
- unnamed checkers;
- two exit proofs weaker than R:57–58;
- two exit proofs that are blocked by owner decisions but not marked as blocked.

## Q4. Updated standard against each candidate

The common requirements bind both candidates (R:3; C:5). The work list routes every new obligation to Codex only (WL:6–8). T2C carries none of them.

| New or changed obligation | Codex item | Claude candidate |
|---|---|---|
| Fourth relationship, reduction (R:43; R:47–58; P:383 criterion 6) | I3-01, 02, 04, 07, 12, 14 | Untracked. Frep:202–206 says a later Claude revision "needs an explicit bound task and evidence". |
| Constraint surfaces and a_c (R:60–70) | I3-08, 09, 10, 11 | Untracked. Frep F3 already shows no current interpretation. |
| Supersession paragraph (R:27); criterion 3 (P:380) | I3-06 | Untracked. Frep:194 records 7 superseded rows as author claims. |
| Single ownership item 8 (R:115) | I3-02 | Untracked |
| Recorded-state paragraph (R:138); refinement item 2 (R:127) | I3-03 | Untracked. Frep F2 bears on R:127. |
| Current-state and basis amendment (R:80) | I3-05, I3-11 | Untracked. Frep F1 bears on it directly. |
| Criterion 4 amendment (P:381) | I3-10 | Untracked |
| 16 new conformance rows (C:10–22, :30, :51, :52) | I3-12 and specific items | Untracked |

G:11 states that the work list "traces each remaining requirement and review finding to work, status and closure evidence", without the Codex-only qualifier. For the peer line that statement is false (SR3-02).

## Q5. Open owner decisions

| Decision (owner: P:393–398) | How the work list carries it | Result |
|---|---|---|
| Acceptance-review assignments (P:393) | I3-14: "Executive selects source-first independent reviews" (WL:103) | Treated as Executive work. The owner reservation is not stated. |
| Ported-part review policy (P:394; XP:77) | Inside I3-07's exit ("selected port-review policy … decision remains explicit", WL:96); I3-14 "record port … limitations" | Mentioned inside work. No decision row, and no "before the first cone with a contribution is accepted" trigger. |
| Steel thread (P:395) | I3-15 RESERVED, NOT_SELECTED | Tracked as a decision |
| Compressions kept, superseded or removed (P:396) | I3-08 schedules reconciling "compressed bodies" | Treated as work. Retention is presupposed. |
| Identifiers for a_c concepts and the Traversal Occurrence Profile (P:396) | I3-13 "Owner-selected identity policy" | Partly. Identifier issuance is not named. |
| Candidate number and RC cut (P:397) | I3-13 "marks provisional candidate identity" (work); I3-16 "release identity" | The decision is not named |
| Cohort relation (P:398) | Absent | Untracked |

## Expectation 11: ambiguities recorded by the expectation writers (*interested*)

These are the Claude line's A1–A9 (EXP:180–189, :234–236). The work list mentions none of them. Whether the specification resolves each one belongs to other reviewers, so the results below are tentative.

| ID | Status |
|---|---|
| A1 | Resolved: R:86–90 |
| A2 | No decision needed. EXP:183 accepts either reading. |
| A3 | Partly resolved by R:138; carried by I3-03 |
| A4 | Unresolved and untracked. R:109 still says "packaging owns no method determination" and says nothing about schema value lists. |
| A5 | Unresolved and untracked. No tier is named for the categorical standard (R:104–109). |
| A6 | Unresolved and untracked. R:146 still says "as far as they apply". |
| A7 | Partly resolved. R:40 states the form of accounting but not who judges a family material. |
| A8 | Unresolved and untracked. P:281–286 still say the parts are "proposed" and selected by the Executive; I3-07 selects no new port. |
| A9 | Resolved: R:80 |

No separate ambiguity register for the Codex line was located (see Limits).

## Findings

| ID | Severity | Claim | Evidence | Smallest correction |
|---|---|---|---|---|
| SR3-01 | High (*interested*) | Codex's five findings on the Claude candidate (F1–F5) are omitted, and the report is not in the repository at the subject commit. The common pen's territory included Codex commentary. | `git cat-file -e 7c058ed:…/20261014T000519Z_…` fails; `git log --all` on the path is empty; file untracked, SHA-256 `758baef0…`; dated 00:05:19Z, before `6c2debb` at 01:10:12Z; Frep:220; WL:42–48, :113–141; T2:231–262; T1:31; T2C:257 | Commit Frep as written. Add key **F** to WL:42–48 and index rows F1–F5, each with its R anchor (Q1), destination "peer line, unassigned", status RESERVED (owner activation). This needs no peer-ticket write or activation. |
| SR3-02 | Medium (*interested*) | The updated standard's work on the Claude candidate is tracked nowhere, and G:11 claims full tracing. | R:3; C:5; WL:6–8; T2:30; T2C:30, :68–75; Frep:202–206; G:11 | Add a peer-line section that lists the Q4 obligations against the Claude candidate at `768cf8c`, all RESERVED. Otherwise qualify G:11 with "for the Codex line" and name where peer obligations are held. |
| SR3-03 | Medium | The completeness and "no false closure" check was circular: it was made against the work list's own keys, and "supplied review packet" bounds the work list's own completeness claim. The packet definition excludes Frep and A1–A9 without saying so. | CON:34–42; WL:109; T1:23 | State the packet definition and its exclusions in WL:109. After SR3-01 and SR3-02, rerun the coverage check against all reviews of both candidates. |
| SR3-04 | Low | I3-00 "Common standard and consolidation — COMPLETE" uses a state outside the defined vocabulary. The row discloses that owner acceptance is separate, but the label reads as the standard being settled. Later context: the owner has since directed review rounds on this standard (XP:10, dated after the subject). | WL:79–84, :89; T2X:34; T1:65; REFERENCE_FRAME_BASIS.md:24 | Split I3-00 into "consolidation recorded — COMPLETE" (and define COMPLETE as recording work done, with no acceptance) and "common standard — IN OWNER REVIEW", with owner sign-off as its exit. |
| SR3-05 | Medium | Owner decisions are treated as work or not tracked: acceptance-review assignment (I3-14), compressions (I3-08), identifiers and candidate number (I3-13, partly), cohort (absent). The ported-part policy appears only inside I3-07. I3-07 and I3-14 cannot close until these decisions are made. | P:393–398; WL:96, :97, :102, :103, :105 | Add a decision table: each P:393–398 decision, its owner, its "needed before" trigger, and the items it blocks, with status RESERVED. Mark I3-07 and I3-14 as blocked on them. |
| SR3-06 | Medium | Multi-destination findings have no per-finding closure rule. For example, CR3 F-6 and F-9 are small text fixes routed partly to RESERVED I3-15, so a reviewer cannot tell when a finding closes. | WL:110, :121, :126 | Add a closing-item column (or a rule such as "closes when all listed items close") and per-finding status. |
| SR3-07 | Medium | Two exit proofs are weaker than the reduction requirement. I3-02 requires no comparison of decisions and acquisition with the predecessor and iteration 2, and I3-11 makes the comparison optional ("if claimed"). I3-05's cases are not "independently specified". | R:57, R:58; WL:91, :94, :100 | Add the R:57 comparison (both baselines are available) to I3-02's exit, and add "independently specified" to I3-05. |
| SR3-08 | Low | Exit proofs leave the checker or its independence unbound, so a reviewer cannot tell whether same-family working reviews suffice. The phrase "Initial entry fixes implemented" is unverified. | WL:91–94, :97, :100–102; P:385; K:5–6; AC:5–8; CON:10–13; S:158–167 | For each item, name the checker. State whether a same-family working review suffices, or route the item through I3-14 under P:385. Label the I3-08 fixes as the author's claim. |
| SR3-09 | Low (*interested*) | M1–M7 and the minor rows are reachable only through their CR constituents, while expectation 11 names M1–M7. | WL:116–136; Hrep:125–157; XP:75 | Add the M crosswalk from Q1 to the index. |
| SR3-10 | Low | No row cites a line or locus in the current subject. | WL:30–34, :89–105 | Per item, name the member and section at `de8232a`, or state that lines are held in the source report at its own subject. |
| SR3-11 | Low (*interested*) | "Variance is already recorded" cites no locus. The substance is at T2X:28 and G:11, but neither names the Development Isolation merge rule. | WL:105; Hrep:171; P:254–255 | Cite T2X:28 and G:11 and name P:254–255 as the varied rule. |
| SR3-12 | Low (*interested*) | Expectation-writer ambiguities A4, A5, A6 and A8 are neither resolved nor tracked. | EXP:185–189; R:104–109, :146; P:281–286 | Track each one as a common-pen or owner decision, or record its resolution. |

## What holds

- Every CR finding ID (60 of 60) has a destination, and H1–H4 are named in their item rows. E, S and AC are fully carried. CC's single finding is closed at T2X:71.
- Representation of Claude's findings is fair (*interested*):
  - H counts are bounded to the iteration 2 inventory (WL:45).
  - K's absence of findings does not close H1–H4 (WL:46).
  - The data/result clarification does not close H2 by renaming (CON:22–25).
  - CR5-05 is recorded as owner-directed with no candidate defect (WL:132), which matches Hrep:171.
  - The 77-law granularity caveat is respected (WL:90 against Hrep:97).
- The R labels resolve and are disclaimed as non-constitutional. No row creates a requirement by listing.
- The status vocabulary denies acceptance (WL:79–85). The cited repair records exist at `de8232a`.
- The I3-06 and I3-10 exit proofs are observable and adequate.
- The I3-00 review subject and snapshot B have identical specification bytes.
- The steel thread is tracked as a decision (I3-15). The work list itself selects no peer work, merge, release or paid run (WL:157–160).

## Limits

- Frep was read from the untracked working tree. Its identity is fixed only by the SHA-256 above.
- The Reviewer did not re-evaluate any finding or tenant repair, and did not judge whether the specification itself resolves A1–A9, beyond the tentative table.
- One targeted look found no separate ambiguity register for the Codex line (`de8232a:…/qualification/C3/APPLICABILITY.md`). Expectation 11's "both lines" is checked here for the Claude line's EXP only.
- Earlier-iteration cross-assessments and common reviews were not inventoried, including `codex/20261013T170400Z_…` and `…T043456Z_…`.
- The Reviewer is Claude-family, which is the author family of Hrep, S and the Claude candidate. Judgments on those are marked interested.
