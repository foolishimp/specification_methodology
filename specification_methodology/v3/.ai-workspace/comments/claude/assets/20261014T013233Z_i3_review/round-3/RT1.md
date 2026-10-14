# RT1: Round 3, closure of the round-2 corrections

**Reviewer**: a Claude context acting as cross-family Reviewer. The common pen is Codex. This report repairs nothing.
**Subject**: frozen `355aa8655cca9c6ba6cf5c414f9bea3032ae89fd`, read from `$R3/subject/specification_methodology/v3/`. Compared with round 2's `55bbf9e` through `$R3/diff_r2_r3.patch`.
**Scope**: round-3 expectations 1 to 8 in `comments/claude/20261014T013233Z_REVIEW_I3_COMMON_SPECIFICATION.md:349–358`; the contract digests; the round-2 disposition record.
**Sources for judging declines**: T-001 at the subject; the C3 contract in `PRODUCT.md`; the installed predecessor at `~/Library/Application Support/STDO/releases/v2.5.1-rc.2/standards/`.

## Path keys

All paths are under the subject's `specification_methodology/v3/`.

| Key | File |
|---|---|
| P, I, G, B | `specification/PRODUCT.md`, `INTENT.md`, `GOALS.md`, `REFERENCE_FRAME_BASIS.md` |
| R, AC, PC | `specification/requirements/README.md`, `A_C_DEPENDENCY.md`, `PREDECESSOR_CLAIMS.md` |
| CF | `specification/conformance/README.md` |
| T1, T2, T2X, T2L, WL | `.ai-workspace/tickets/active/`: T-001, T-002, T-002-CODEX, T-002-CLAUDE, T-002-iteration-3-work |
| D2 | `.ai-workspace/comments/codex/20261014T064039Z_REVIEW_I3_ROUND_2_DISPOSITION_AND_REPAIR.md` |
| INST | the installed `v2.5.1-rc.2/standards/` |

## Results against the round-3 expectations

"Interested" marks a row whose repair adopts wording that a Claude round-2 report proposed. Under the new P:401, the author of adopted wording "cannot supply independent acceptance evidence for it". These rows are therefore defect rechecks only. They are not independent acceptance.

| # | Expectation | Corrected text | Result | Reason |
|---|---|---|---|---|
| 1 | **RR3-01.** Acceptance standing has one record, the ticket. The frontier holds proposals only. | P:334: "Each tenant's frozen frontier records its proposed dispositions and evidence … Acceptance standing comes only from the decisions recorded in that ticket … a frontier may cite those entries but cannot confer or revise acceptance." PC:3: "Each tenant's ticket records its acceptance and reopening decisions". PC:8: "only its ticket supplies acceptance standing. Neither this historical table nor a tenant-authored frontier grants acceptance." PC:18: "citing the ticket for accepted decisions". | **Closed** (interested) | One record remains. This agrees with P:251–252: "no disposition exists until the pen has recorded it". Both prepared contracts say "the common pen records admissions and dispositions in this ticket" (T2X:34, T2L:34). Two unchanged loci omit the word "proposed": R:8 "names its dispositions" and P:288 "where each predecessor claim is disposed". Neither claims acceptance (RT1-08). |
| 2 | **RR3-06.** Admitted bytes match their recorded digests. A successor has its own digest and admission. This applies to every contract admitted at or before `355aa86`, including EC-CLAUDE-I3-01. | T2X:96: "the in-place routing revision at `ca8b9c3` hashed to `bf1557…` and was not admitted … The original block above is restored byte-for-byte from `dad25ef`; its recorded `fc6ed…` admission digest now reproduces." The successors: T2X:28–43 for EC-CODEX-I3-02 and T2L:28–43 for EC-CLAUDE-I3-01. Each says "Admission record: pending … The contract's digest is the UTF-8 block from its `###` heading through its Return line, with one final newline." | **Closed** (interested), with one minor finding (RT1-04) | Every recorded digest reproduces at the subject and at its original admission commit (digest table below). Correction to this review's own premise: at `355aa86`, EC-CLAUDE-I3-01 and EC-CODEX-I3-02 are drafts. They are admitted at `651581c`, outside the frozen subject. The digests recorded there, `3c928885…` (5,163 B) and `b1a8ab97…` (5,089 B), equal the `355aa86` bytes, and those bytes are unchanged through HEAD. |
| 3 | **RR3-05 and M4.** Every accepted item changed since `a7eba66` is listed with its reason. The Development Isolation change and the single-ownership change are presented for the owner's explicit acceptance, not applied as accepted. The constraint-surface requirement states its purpose. | G:42: "They amend historically accepted conditions for the selected construction; the historical C1/C2 dates do not accept these later bytes." G:46–54 list nine changes with reasons, including G:47 "Development Isolation, a local axiom" and G:49 "Single ownership items 2 and 4". R:72: "Purpose and material relation: actors need to recover the constraints governing a task within finite context and attention. Logic compression reduces acquisition and interpretation work while preserving the obligations, permitted choices and unresolved dependencies that determine lawful work." | **Partly closed** (interested) | Closed: the seven omissions RR3-05 named are listed with reasons (G:46–52), and the purpose paragraph exists. Still open: (a) No owner-level change is presented as a named item for the owner's acceptance (RT1-01). (b) Two changes to accepted items are still unlisted: the owner's actor-binding reservation, and criterion 5's new a_c obligation (RT1-02). (c) The table is headed "round-1-to-round-2" (G:42), but its reasons also describe the `355aa86` changes (G:50, :54). |
| 4 | **RR3-04.** Per-criterion results fit the installed single result, or a variance is recorded. | P:202: "The Reviewer returns one closed evaluation of the member's conformance, with one overall result and supporting judgments for all six criteria … The overall result is the conjunction of those judgments under the installed Result Conjunction." P:200: "All six member acceptance criteria are mandatory … A false applicability condition excludes only that obligation … It introduces no new result value and does not waive a criterion." B:28: "one overall result, judgments for all six member criteria, applicability reasons for conditional obligations". | **Closed** (interested) | This matches INST `STDO_REFERENCE_FRAME_BASELINE.md:1371–1379` ("one closed evaluation containing … Reference Frame Method result") and RF-012 (`REFERENCE_FRAME_METHOD.md:409–420`). Applicability follows `REFERENCE_FRAME_METHOD.md:589–608`. P:200–202 state all five elements the installed decision rule requires (`:676–681`): which results are mandatory, how missing and unknown results are handled, the same basis, the owning authority and the veto. D2:72 narrows the "incompatibility" diagnosis. That narrowing holds: nothing installed forbids supporting judgments inside one closed result. One residual: CF:74 says "Five applicable member criteria" (RT1-05). |
| 5 | **RR3-02 and RR3-03.** Process-only rows are out of criterion 5. Whether routed acquisition counts against the limit is decided. | CF:3: "The member-conformance table supplies acceptance criterion 5 … Construction and integrated-closure checks have their own section". CF:66–74 hold the three moved rows, with "They do not add candidate-text predicates to member criterion 5" (CF:68). CF:9: "An absent integrated assessment does not by itself fail a member's local criterion 5." P:403: "The context limit bounds the material concurrently retained in active actor context, including instructions, frame, subject and subsequently acquired material … A 30 KB supplied frame plus 200 KB retained acquisition exceeds a 40 KB context limit". | **Closed** (interested) | Both parts are decided. CF:9 also removes round 2's two-reviewer divergence on the old row 12. P:403 settles counting and timing, and B:29 agrees. P:350 still says "Supplied context is measured in bytes before acquisition", which is consistent with reporting the supplied bytes separately. |
| 6 | **RR3-07 and RR2-08.** One primary per finding, a correct TC-03 record, and the reviews left out of the packet named. | WL:136–139: "H-M rows coordinate aggregate findings in H … the cited constituent CR findings retain the primary of their own row … An H-M row never reassigns a CR finding's closure." WL:182: "For CR3-F6/F9, I3-05 owns closure". T1:39: "TC-03's prior closure covered its sampled routes; RR2-02/RR3-07 reopen it on the aggregate aliases." WL:53 names CC, AR and CON with their dispositions. | **Closed** (interested), with a low residual (RT1-06) | A parse of WL:143–169 finds each of the 78 E, H, CR, S and AC IDs in exactly one plain row. The H-M rows now carry aggregates only. The TC-03 record is corrected, and T1:55 labels the round-1 return (including T1:71) historical. RR2-08's three named reviews are added. The same mechanism still leaves out the three round-2 working reviews (RT1-06). |
| 7 | **M1.** Reasons for the "Axiomatic calculus" row and the renamed rows. INTENT agrees with PRODUCT. Confirmation stays the owner's decision. | T1:37: "'Specification and project structure' collects the WHAT/HOW and tenancy relations. 'World models, identity and Markov objects' identifies the subjects, boundaries and state … 'Information and interpretation' … 'Evidence, correction and authority' connects observation, repair and permission … 'Axiomatic calculus' directly carries the quoted logic-compression instruction." T1:29–35 add four quotations attributed to the owner. I:25: "The [foundational pillars](PRODUCT.md#foundational-reduction) define the contributions"; the alternate list is gone. | **Closed**, apart from the owner's confirmation and a low residual (RT1-07) | Every row RR1 flagged now has a reason, and INTENT routes to the single table. The pen declines again to ask for confirmation: "without requesting the same direction again" (T1:37; D2:101–106). The decline is now better grounded, because T1:29–35 quote the owner on both calculi, Markov objects, outcome-driven development, functional design, the specification method and project structure, and a_c. The quotations do not cover reference frames, information or evidence and authority, which T1:37 attributes to "the earlier context/workspace discussion". The quotations first appear in the repository at `355aa86`, and this review cannot check them against the conversation. Confirming P:39–50 remains the owner's decision. |
| 8 | **RR1-N2.** A rule decides whether more acquisition defeats a reduction, and which deciding paths must be compared. | R:61: "Cover each claimed recurring determination and its materially affected entry and consumer paths. Justified equivalent cases may share a comparison; the independent Reviewer checks the grouping and uncovered material paths." R:63: "An unexplained increase in acquisition or necessary reconciliation prevents a satisfied conclusion that the affected path is simpler … A justified increase preserves a necessary distinction or binding, or follows an explicitly declared tradeoff … A supported elimination witness retains its narrower standing". P:399: criterion 6 applies "within its cone"; "its absence alone does not falsify a supported local claim". | **Closed** (interested), with a low residual (RT1-03) | Both questions are decided, and R:16 now defines "consumer". D2:55 narrows the remedy: local deciding-path comparisons stay per member instead of all moving to the integrated assessment. That holds, because it keeps evidence local without leaving a gap (CF:9, R:66). Residual: "narrower standing" maps to no result value. One reviewer can read P:399's three conditions as satisfied, while another applies R:66 ("unexplained adverse changes … prevent a satisfied reduction conclusion"). |

## RR3-06 digest table

Method: the UTF-8 lines from the block's `###` heading through its last bullet, joined with `\n` and ending with one final `\n`. Checked at the subject `355aa86`, at the original admission commit, and at `65c0210` and HEAD.

| Contract | Range as defined by its record | Lines at `355aa86` | Bytes | Computed SHA-256 | Recorded | Match |
|---|---|---|---|---|---|---|
| EC-CODEX-I3-01 | **Not stated** in its admission (T2X:94). Inferred from the SYN-01 convention: heading through the Closure line | T2X:79–92 | 4,459 | `fc6ed417487bcf6abac656e2da9fd47620632655bda416aeba18006de1f585c9` | T2X:94 `fc6ed417…` | Yes. Also at the admission commit `cae6fe3` and at HEAD. At `55bbf9e` and `ca8b9c3` the block hashed to `bf1557dc…` (4,660 B), as T2X:96 records. |
| EC-CODEX-I3-01 input amendment A1 | **Not stated** (T2X:77). Found by trial: heading through "…or acceptance during consolidation." | T2X:59–75 | 1,111 | `63daa64261017e4f8b525db5c53d60bd916623bdc45c79e4dced76602a8879d1` | T2X:77 `63daa642…` | Yes. Also at the admission commit `5543840` and at HEAD. |
| EC-CODEX-SYN-01 | T2X:155: "the exact EC-CODEX-SYN-01 heading and bullet text through its closure line, including the terminating newline" | T2X:157–169 | 3,652 | `d5df2236d8f07d299ccc58d12f574a1908b1c340ecb3653c1c30ecaeaab186d8` | T2X:171 `d5df2236…` | Yes. Also at the admission commit `bb76b1d` and at HEAD. |
| EC-CODEX-I3-02 | T2X:43: heading through Return, with one final newline | T2X:28–41 | 5,089 | `b1a8ab9713b3425600c87ffcc24b35f387062a1272bfb1446d64d7c294e49ad0` | None at the subject (draft). `651581c` records `b1a8ab97…` | Yes, at `651581c` and HEAD. |
| EC-CLAUDE-I3-01 (interested) | T2L:43: heading through Return, with one final newline | T2L:28–41 | 5,163 | `3c928885b7c185d467ad3764289ae796b259c0982d71f8ee46be6b944860b859` | None at the subject (draft). `651581c` records `3c928885…` | Yes, at `651581c` and HEAD. |
| EC-CLAUDE-001 (historical) | T2L:85: "contract text as committed in c9924e1". Identified by commit, with no digest; the installed rule allows "exact contract identity or digest" (`TICKET_METHOD.md:674–677`) | T2L:73–84 | 2,414 | (not recorded) | commit `c9924e1` | The block through `result consumer` is byte-identical to `c9924e1`. Its heading still reads "(drafted)" while T2L:85 says admitted. This is pre-existing. |
| RF-V2-V3-COMP-01 | T2X:185 admits an activation file by link, with no digest. It is not an execution contract. | — | — | — | — | Not applicable. |

Shared input `C3-I3-R2-01`, recorded at `651581c` outside the subject: all 24 member byte counts and SHA-256 values equal the files at `355aa86`.

## Round-2 disposition record (D2)

**Coverage.** D2:52–88 has one row for each of the 35 round-2 findings: RR1-N1 to N7, RR2-01 to 08 and RR3-01 to 20. D2:90–94 answer observations O-1 and O-2. D2:98–120 answer the finding groups M1 to M10.

**Tally by D2's own labels (35 rows):**
- Corrected: 32. Three of these are record-only corrections: RR2-05, RR2-07 and RR3-17.
- Narrowed: 2.
  - RR1-N2: "Corrected with a narrower remedy than proposed".
  - RR3-04: "the incompatibility diagnosis is narrowed".
- Partly declined: 1. RR3-10: "mandatory directory placement declined".
- Declines at the group level:
  - M1: the owner's verbatim confirmation, "Requiring the owner to repeat that direction verbatim is declined" (D2:104).
  - M2: the universal numeric threshold, kept from round 1 (D2:107–108).

**Tally by verified outcome against the frozen text.** All 35 rows were checked at their cited locus. The eight expectation items were checked in depth.
- Repaired as prescribed or by an equivalent: 31.
- Repaired with a narrowed remedy that holds: 2 (RR1-N2, RR3-04).
- Repaired through the other branch that RR3-10 itself offered: 1 (RR3-10).
- Partly closed: 1 (RR3-05; RT1-01 and RT1-02).
- Declined outright: 0.

Minor residuals in the repaired rows:
- RR3-13: R:121 still says "derived from their normative owners".
- RR3-04: CF:74.
- RR2-08: RT1-06.

**Sample of declines and narrowings:**

| Item | D2 disposition | Judgment against the sources |
|---|---|---|
| M1 confirmation | Declined. "the conversation already supplies it" (D2:104). | Holds in part. T1:29–35 now quote owner words for most rows, and T1:37 states that the table is "not a claimed verbatim owner taxonomy". The rows for reference frames, information, and evidence and authority have no quoted source. Confirmation stays with the owner at sign-off. |
| RR1-N2 | Narrower remedy. Local comparisons stay per member. | Holds. P:399 and CF:9 keep local evidence required. R:66 assigns composition to the integrated assessment. |
| RR3-04 | Diagnosis narrowed. "Supporting judgments are lawful inside a closed evaluation." | Holds. Installed RF-012 and baseline §6 require one closed result per evaluation and do not forbid supporting judgments. P:202 now states the overall result. |
| RR3-10 | Directory placement declined. | Holds. RR3-10 offered two branches, and the pen took the second: "Criterion 4 qualifies standalone successor task use … Freshness excludes unselected private context and automatically loaded repository instructions regardless of working directory" (P:358; B:29). INST RF-013 (`REFERENCE_FRAME_METHOD.md:424–427`) requires reconstruction without undocumented context, which is not a location rule. `SPEC_METHOD.md:2353` only prefers a "fresh sandbox or equivalent isolated environment". |
| M2 numeric threshold | Not inferred (D2:107–108). | Holds. R:63 decides through the removal of determinations and through explained or unexplained adverse change. |

**Accuracy of D2's other claims**, checked:
- RR3-06: the restored 4,459 B block reproduces `fc6ed…`.
- RR2-01: T1:162 labels the snapshot-after-sign-off sentence historical.
- RR3-18: WL:27.
- RR3-11: R:166.
- RR3-12: AC:43.
- RR1-N5: AC:65 and :71.
- RR1-N7: T2:61 and P:342.

## Findings

No finding is blocking or material. RT1-01 keeps expectation 3 partly closed.

| ID | Sev | Claim | Evidence | Smallest correction |
|---|---|---|---|---|
| RT1-01 | minor | The owner-level changes are not presented as named items for the owner's acceptance. None is claimed as accepted. All of them govern construction through the input that `651581c` admits. | Status at the subject: <br>• G:42 "the historical C1/C2 dates do not accept these later bytes"; <br>• G:18 "Final common sign-off remains open"; <br>• WL:212 gives one generic row, "Current common revision sign-off"; <br>• D2:73 says only "Their later acceptance is not attributed to the historical C2 date"; <br>• P:407–414 lists none of them; <br>• T1:41: the input may be "admitted for draft implementation before final common acceptance". <br>The owner-level changes are: <br>• Development Isolation, a local axiom (G:47; R:12); <br>• single-ownership items 2 and 4 (G:49); <br>• the result/data clarification of the owner-entrenched result algebra (G:58); <br>• packaging closure moved earlier (G:51); <br>• the identity decision moved earlier (G:52); <br>• the actor-binding reservation (RT1-02). | Add one line to G:18's required result, or one row in WL's decision table, listing these changes for the owner's explicit acceptance at sign-off. |
| RT1-02 | minor | Two changes to accepted items are still unlisted. | 1. The owner's actor-binding reservation. At `a7eba66` it read: "The Executive and Reviewer actors for each tenant in C3. The product owner names them in the tenant tickets. Until then every execution contract stays `drafted`." G:66 says "Actor binding remains the product owner's". It now reads "Acceptance-review assignments … remain owner decisions. Each ticket records its construction assignment" (P:409; changed in `9810215`). It appears in neither G:44–54 nor G:58. B:25 and B:20 keep part of the reservation. T2:126 still says "OPEN; Jim names the Executive and Reviewer per tenant". <br>2. Criterion 5 now adds "The affected a_c interpretation and acquired views preserve the owned determinations" (P:398). At `a7eba66` it was logical review of the member's text only. G:58 lists only criteria 3, 4 and 6, and G:53 names only the Outcome and closure. | Add both to the G:44–54 table with reasons. Label T2:126 historical, or update it. |
| RT1-03 | low | A "narrower standing" maps to no criterion-6 result. | R:63 "A supported elimination witness retains its narrower standing even when the overall improvement is not established." P:399 lists three conditions that a contraction meets. R:66: "unexplained adverse changes … prevent a satisfied reduction conclusion". D2:154–156 intends to "withhold the broader improvement conclusion". | Add to R:63: "The narrower witness is a supporting finding; the affected reduction conclusion, and criterion 6 for that path, is not `satisfied`." |
| RT1-04 | minor | Two admission records give no byte range for their digests. The digests can be reproduced only by inference. | T2X:94 ("contract SHA-256 `fc6ed…`") and T2X:77 ("SHA-256 `63daa…`") define no range. Only SYN-01 (T2X:155) and the two successors (T2X:43, T2L:43) do. A1's range ends partway through the section, at T2X:75. | Add a note outside both blocks, for example after T2X:96, recording "I3-01: heading through Closure, 4,459 B; A1: heading through '…during consolidation.', 1,111 B". Leave the admitted bytes unchanged. |
| RT1-05 | low | The conformance row contradicts "all six mandatory". | CF:74 "Five applicable member criteria are satisfied and the sixth is missing". P:200 "All six member acceptance criteria are mandatory". | Change it to "Five member criteria". |
| RT1-06 | low | Three reviews are neither in the packet nor named as excluded. This is RR2-08's mechanism in a new place. | The round-2 working reviews are the contract check `20261014T032433Z`, the trace check `20261014T032320Z` and the trace recheck `20261014T033144Z`. They are cited in T1:55 and :69–71, which disposes TC-01 to TC-03. A grep of WL for their IDs returns nothing. WL:117–123 limits the packet to "the round-1/round-2 common reviews listed above". | Add these three reviews to WL:53, with "TC-01 to TC-03 disposed in T-001". |
| RT1-07 | low | A newly quoted owner contribution is not routed to any pillar. | T1:31 quotes "functors between categories through F_C,F_D,F_P in outcome driven development". The outcome-driven development row (P:45) has no functorial content, and T1:37 gives no reason. The substance exists generically at P:17–23, P:124 and WL:102 ("functor claims stay bounded by their proof"). | Add one clause to T1:37 saying that the functorial structure is carried by Categorical Construction and the demonstration standard. |
| RT1-08 | low | Two loci still omit the word "proposed". | R:8 "Each tenant's frontier names its dispositions". P:288 "A frontier record is a tenant's record of where each predecessor claim is disposed". | Add "proposed", or a reference to P:334. |
| RT1-09 | low (interested) | T2L's actor table is current-tense, but it is stale beside the admitted EC-CLAUDE-I3-01. | T2L:66 says "Ledger Writer \| the common pen (Claude)". B:26 says "The common pen (Codex)", and T2L:34 says "the common pen records admissions". T2L:59–67 are not labelled historical, while T2L:51 is. | Label T2L:59–67 as the first-pass binding. |

## Corrections to this review's own round-3 expectations

- Expectation 2 assumed that EC-CLAUDE-I3-01 was admitted at or before `355aa86`. It is a draft there and is admitted at `651581c`, with the digest of the `355aa86` bytes.
- The review record says that after `355aa86`, "main changes only GOALS status lines up to `65c0210`". That is true of `specification/` only. Tickets, Codex review posts and a handoff changed at `651581c` and later.

## Limits

- **Tenant interest.** Claude is a tenant governed by this specification.
  - EC-CLAUDE-I3-01, T2L and RT1-09 concern the Claude line.
  - Rows 1–6 and 8 judge repairs that adopt wording from the round-2 reports RR1, RR2 and RR3. Under P:401, those judgments are defect rechecks and supply no independent acceptance.
- **Material not read.**
  - The owner's conversation is not on record, so the provenance of T1:29–35 cannot be checked.
  - Neither candidate was read.
  - The 691 claim rows were not read. Only PC:1–19 were.
  - D2's statement that the worktrees were clean was not rechecked.
- **Commits outside the frozen subject.** `651581c`, `65c0210` and HEAD were read only for the digest, admission and snapshot checks.
- **Scope.** Expectation 9 (no regressions) and the tenant-contract consistency check belong to other reports. Items noted here were found incidentally.
