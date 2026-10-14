# RR2: Round 2, findings M6–M9, the disposition record and the working reviews

**Reviewer**: a Claude context acting as cross-family Reviewer for round 2. It repairs nothing.
**Subject**: frozen `55bbf9ee7bc8e37235ef0588f9afea0f8ccbabbc`. Its `specification/` tree is `bcc5e10`, the same tree as at `dad25ef` and `be582ae`.
**Compared with**: round 1 subject `7c058ed`, whose specification is unchanged at `afb6ad6`.
**Scope**: M6–M9; the disposition record's coverage of SR1–SR4 and A1–A9; and the three working reviews cited by the handoff.

## Independence

- Claude wrote the round-1 findings that are being judged here, so this is not a fully independent judgment of whether they closed.
- M8, the F index, SR4 N-1/N-4 and the Claude line's ticket concern the Claude line. Those judgments are marked **interested**.
- No context in this review authored the specification, the work list or either candidate. This context shares a model family with the Claude candidate's authors. That matters for the interested judgments above.
- **Result labels.** This report is itself a common-definition review under RF:24, so its labels map to the installed family as follows:
  - closed, or "Yes" in the sample → `satisfied` for that expectation or disposition;
  - partly closed, still open, or "Partly"/"No" in the sample → `falsified`, with the residual named.

## Path keys

**Under `$R2/subject/specification_methodology/v3/`:**

| Key | File |
|---|---|
| P | `specification/PRODUCT.md` |
| R | `specification/requirements/README.md` |
| RF | `specification/REFERENCE_FRAME_BASIS.md` |
| G | `specification/GOALS.md` |
| CAP | `specification/requirements/CAPABILITIES.md` |
| PC | `specification/requirements/PREDECESSOR_CLAIMS.md` |
| WL | `.ai-workspace/tickets/active/T-002-iteration-3-work.md` |
| T1 | T-001 |
| T2 | T-002 |
| TX | T-002-CODEX |
| T2C | T-002-CLAUDE |
| D | the disposition record `comments/codex/20261014T030729Z_…` |
| CC | the contract check `…T032433Z_…` |
| TC | the trace check `…T032320Z_…` |
| F | the peer report `…T000519Z_…` |

**Outside the frozen subject, read at `cab9800`:**
- **H**: the handoff `…T033341Z_HANDOFF_I3_SPECIFICATION_ROUND_2.md`.
- **TR**: the trace recheck `…T033144Z_…`.

`cab9800` also edits the status text in G:11 and G:18 ("ready for Claude's round-2 review"). As a result, `main`'s specification tree is now `a6118fb`, not `bcc5e10`. H:12–17 discloses this as a "current work-status projection". The edit changes no requirement.

## 1. Results for M6–M9

### M6: the frame basis's result set

**Expectation.** The review result set maps into the core, or it is replaced by core values with a domain outcome.

**Corrected text.**
- RF:24 now reads: "Returns a closed installed Reference Frame Method evaluation, with scoped clause results, evidence and limits."
- The value set "supported, contradicted or unresolved" no longer appears anywhere in `specification/` or the active tickets (checked by grep).
- P:200 names the installed result family.

**Result: closed.** One low residual remains: "scoped clause results" is not bound to installed values (RR2-04).

### M7: process and authority

**Expectations and corrected text:**

1. **Write surfaces.**
   - P:212–217: the common pen writes "The common WHAT (`specification/` and the Product Definition) and common work records"; "An authorised Reviewer writes its own review under `.ai-workspace/comments/<reviewer>/`".
   - RF:25–28 give a surface per role:
     - the Executive has "no write grant of any kind";
     - the ledger Writer "Writes tickets only";
     - the Reviewer "Writes only its review".
   - TX:63–64 now agree with these rows (TC-02, corrected).

   **Closed.**
2. **Merge variance.**
   - P:264–266: "only on the product owner's acceptance of the checkpoint review, or an explicit owner-directed variance recorded in the ticket. A visibility merge supplies no acceptance."
   - WL:111 links the actual instruction.

   **Closed.**
3. **"Author".** P:399: "The Reviewer does not assess its own authorship, including a material contribution to the subject or the repair under review … A fresh context or another model name alone does not establish it."

   **Closed.** P:399 does not settle whether a Reviewer who prescribed a correction may assess it (RR2-06).
4. **I3-00 closure.**
   - WL:95's exit requires an "owner sign-off separately recorded".
   - G:18 adds the row "Iteration 3 common specification".

   **Closed.**

**Result: closed.**

### M8: the work list covers one line (*interested*)

**Expectation.** Either the work list carries the Claude line, or the GOALS claim is scoped to what the list covers. Codex's review of the Claude candidate is committed.

**Corrected text:**
- The pen took the scoping branch. G:11 now says the list "joins common requirements to Codex execution work and the declared review packet. It separately indexes reported peer findings with no peer assignment or current-status claim."
- WL:7–8: "execution assignments and implementation status below concern Codex only. Reported peer findings have a separate unassigned index."
- T2:30 agrees.

**The committed peer report:**
- F is committed at `dad25ef`. Its SHA-256 is `758baef0…12fe8`, identical to the hash SR3 recorded for the untracked file. TC:175 confirms the file is 27,817 bytes.
- F is keyed at WL:50: "Historical report; current peer disposition unassessed".
- WL:173–187 index F1–F5 as "UNASSIGNED / CURRENT DISPOSITION UNASSESSED". Each row names its R anchor.

**Fidelity of the index (*interested*).** The rows faithfully represent F:
- F4 carries F's own limit, "No defect in the unmodified model's output is established" (F:135).
- F5 carries F's "manual workaround" (F:147).
- Severities are not carried. The H/CR rows omit them too, so the two lines are treated alike.

**Consistency with GOALS.** "Historical reported findings; current peer disposition is unassessed and unassigned" (H:23–24, WL:175–176) agrees with G:11. G:19 keeps "The peer line retains its own activation record". The work list does not adopt the Claude reviewer's round-1 statement that F1, F2, F4 and F5 were repaired (TC:191–192). That is correct: carrying it would be a tenant's self-assessment presented as current status.

**Result: closed through the scoping branch.** Observation O-1 below records what this leaves untracked. It is not a defect of the pen, whose grant excludes Claude's ticket (T1:27).

### M9: work-list mechanics

**1. Coverage checked against source reports.** Partly met.
- What was checked: TC checked the new F index against F (TC:175, 188–192) and the H-M aliases against the H report's lines 125–157 (TC:183). Round 1's SR3 had already checked E, CR, S and AC against their sources.
- What remains: the packet is still defined by the list itself. WL:115–117 says "The finite packet is the reviews named in the source table above", and its exclusions are not named: CC `…T001000Z`, AR `…T234754Z` and CON. Their findings are disposed elsewhere.
- D:114 calls this "not inherently circular". That holds for the key-to-report direction only (RR2-08).

**2. Owner decisions tracked as decisions.**
- WL:189–201 is a decision table with "Needed before" triggers.
- It covers every decision SR3-05 listed: assignments, ported-part policy, compressions, identifiers, candidate/cut identity, cohort and the steel thread.

**Closed.**

**3. Closure rule for multi-destination findings.**
- WL:120–126: "Unless a row explicitly assigns a different primary or separates distinct parts, its first-listed work item owns the finding's closure."
- After TC-03 this resolves CR1-F5/F6 and CR3-F3/F7/F8 to I3-02.

**Closed.** A conflict between alias primaries and constituent primaries remains (RR2-02).

**4. I3-02, I3-05 and I3-11 match the reduction requirement.**
- I3-02 (WL:97): "Compare actual decisions and acquisition with exact rc.2 and Codex iteration 2 on comparable tasks and conditions."
- I3-05 (WL:100): "Independently specified successful, refused and unresolved cases."
- I3-11 (WL:106): "the required reduction comparison binds rc.2, Codex iteration 2 …"
- These match R:59 (item 5) and R:62 (item 6).

**Closed.**

**Result: partly closed.** Parts 2–4 are closed. Part 1 is partly met (RR2-08). Part 3 has a low residual (RR2-02).

## 2. Disposition record D

### Coverage

D lists every finding ID:

| Report | IDs listed | Where in D |
|---|---|---|
| SR1 | 13 of 13 | D:65–77 |
| SR2 | 25 of 25 | D:83–107 |
| SR3 | 12 of 12 | D:113–123, with 01–02 grouped |
| SR4 | 19 of 19 table rows | D:129–146 |
| A1–A9 | 9 of 9 | D:156–164 |

- SR4's table treats W-1 to W-3 as one row. D adds the observations N-4 and P-7 to its SR4 rows.
- B1 and M1–M10 are at D:35–45.
- H:19–20's claim that the record "evaluates every SR1–SR4 finding and A1–A9 ambiguity" is true by ID.

### Tally by the record's own labels (69 IDs)

| Label | Count | IDs |
|---|---|---|
| Corrected, added, linked, moved, generalised or surfaced | 42 | |
| Clarified, aligned, or retained and recorded | 17 | |
| Partly confirmed or contested, with a text change | 4 | SR1-02, SR1-04, SR2-23, N-1 |
| Narrowed | 2 | W-0, W-1–W-3 |
| Declined | 4 | SR1-08, SR1-11, SR2-13, P-2 |

The observation N-4 is also declined.

### Tally by verified outcome against the frozen text

| Outcome | SR1 | SR2 | SR3 | SR4 | Total |
|---|---|---|---|---|---|
| Repaired: the text meets the finding's correction or an equivalent | 12 | 24 | 10 | 16 | 62 |
| Narrowed, with a stated reason | 0 | 1 (06) | 2 (03, 08) | 2 (W-0, W-1–3) | 5 |
| Declined | 1 (11) | 0 | 0 | 1 (P-2) | 2 |
| Not applicable | 0 | 0 | 0 | 0 | 0 |

- **A1–A9:** eight are resolved in the text. A8 is retained as not applicable: no port is selected (WL:102).
- **Labels that differ from substance:**
  - SR1-08 and SR2-13 are labelled declined, but the text adopts the prescription.
  - SR1-02, SR1-04 and SR2-23 are labelled partly confirmed or contested, but are fully repaired.

### Sample

The sample has 22 rows and includes every decline.

| ID | Disposition in D | Corrected text | Does the reason hold? |
|---|---|---|---|
| SR1-08 | "Prescription declined … State that it derives from claim dispositions and proves no conservation" | P:332: "is navigation derived from claim dispositions; it does not prove conservation" | Not a decline. The text is SR1-08's own correction. The label is wrong (RR2-07). |
| SR1-11 | "No mandatory paragraph label added … existing requirement owners state them" | R:51 states a purpose for reduction ("simpler to determine and apply while preserving its necessary distinctions"). R:66–76, the constraint-surface requirement, has only "Source:" | Partly. It holds for reduction. It does not hold for constraint surfaces, under P:397 ("adds no new obligation without naming its purpose and material relation") (RR2-03). |
| SR2-13 | "Alleged contradiction declined … distinguished explicitly" | CAP:3: "The questions below are review prompts for those obligations, not separately optional capability contracts" | Yes. The edit removes the ambiguity. Declining the word "contradiction" is harmless. |
| SR4 P-2 | "T-001 already supersedes the old sign-off gate for construction" | T1:49–51: "The owner's instruction authorises continuing Codex construction … The following Selected Contract is historical …" | It holds for construction authority. T1:128 still reads "The next C3 snapshot is recorded in T-002 after common sign-off", unlabelled (RR2-01). |
| SR4 N-4 (obs.) | "Bias claim declined" | No change needed. R:59 now binds "the preceding candidate of that tenant line" | Holds, but answers a claim that was not made. N-4 said "not a defect of form". *Interested* (RR2-07). |
| SR4 N-1 | "claim that no historical acceptance existed is unsupported" | PC:3, :8–10: "reported historical state, not current member acceptance"; "after the same-family acceptance recorded in T-002-CLAUDE" | The relabel closes N-1, and T2C:125 shows that acceptance did exist. The rebuttal targets a claim that was not made: SR4 proposed "reopened, not accepted". *Interested.* |
| SR2-23 | "Timing clarified, not a proven contradiction" | P:342: "must close before C3 closure"; P:410: "precedes any dependent member or C3 acceptance" | Yes. |
| SR3-03 | "not inherently circular" | WL:115–118 defines the packet with no all-history claim | Partly. The packet is still self-defined, and its exclusions are not named. |
| SR3-08 | "Reviewer identity is bound at activation; no premature assignments" | WL:103: "reported by the author"; WL:109: "bind each reviewer at activation" | Yes. Checker assignment is owner-reserved (P:407). |
| SR2-06 | "Material design and repair contributions count as authorship; neutral coordination alone does not" | P:399 | Yes for authorship. The question of a Reviewer who prescribed a correction remains open (RR2-06). |
| SR4 T-4 | Names the acceptor and "reject[s] automatic acceptance … by member acceptance" | P:202: "The product owner accepts any replacement that changes predecessor meaning" | Yes. SR4 offered member-bundled acceptance only "for example". Installed UP-020 bars it. |
| SR4 W-0 / W-1–3 | "Define load-bearing terms … Do not delete material distinctions" | R:59 defines "deciding path" and "acquisition". "consumer" is still undefined. "contracted" persists at P:397 and R:45 | Partly (O-2). |
| SR1-09 | "materiality means an effect on required meaning, permitted work or acceptance" | R:16, same wording | Yes. |
| SR1-13 | "explain states used in material evaluations or authorised decisions" | R:146: "Where it contributes to a material evaluation or authorised decision" | Yes. |
| SR2-03 | "Corrected common-definition result vocabulary" | RF:24 | Yes (M6). |
| SR2-05 | "Historical documentation clarified" | P:264–266 variance clause; TX:30–32 | Yes. Repaired despite the label. |
| SR2-22 | "Corrected current frontier versus historical … columns" | P:332: "Each tenant's current dispositions … are recorded in its own frontier"; PC:3 | Yes. |
| SR3-01/02 | "Corrected omitted peer report and overbroad GOALS projection" | WL:50, :173–187; G:11 | Yes (M8). *Interested.* |
| SR3-06 | "Added finding closure against its original counterexample" | WL:120–126 | Yes, with the residual in RR2-02. |
| SR3-07 | "Corrected I3-02 … I3-05 … I3-11" | WL:97, :100, :106 | Yes (M9.4). |
| SR4 P-6 | "Correct current ticket timestamps" | T1, T2 and TX `updated_at` are all `2026-10-14T03:26:53Z` at the subject | Yes. |
| A4 | "Packaging can own formats and carry method-owned value sets" | R:117: "packaging owns representation formats … deriving method determinations from their normative owners" | Yes. |

## 3. Working reviews cited by the handoff

| Review | Subject | What it covered | Independence declaration | Support for the handoff |
|---|---|---|---|---|
| CC: contract check | `dad25ef`, specification tree `bcc5e10`, which is unchanged through `55bbf9e` | Ten predicates (CC:51–61): B1 / T-4, M5, M1 (SR1-01/02), M2 (T-1/2), integrated reduction (SR1-12, T-2), M3 (SR1-03, T-3), SR1-04/05, projections, M10 (SR1-06/07/08), authorship, result/data. It disclaims tracking/process (CC:65). | Accurate. It is same-family and fresh, read the Claude reports after the primary source, and declared the exception (CC:18). The predicate list was set by the repair author's session acting as Executive (T1:29, :33). This is disclosed in T1, not in CC. | "`satisfied` … in the bounded common-law scope" (H:59) is accurate. |
| TC: trace check | `dad25ef` | SR2-01–25 and SR3-01–12, row by row. A1–A9 through SR3-12. The F and H-M aliases against their source reports. Whitespace qualification. | Accurate. TC:13 says "no contribution … in this activation". TC:27 discloses that the disposition record was supplied. | "`falsified` … three low" (H:60) is accurate, and the original is preserved. |
| TR: trace recheck | `be582ae`, then `55bbf9e` | TC-01–03, plus its own intermediate TC-04, the digest boundary. | Accurate in its own terms: "not a fresh blind replication"; "authored no … repair" (TR:27–31). It does not say that the TC-03 repair adopts the options it proposed itself (TC:128–129 against WL:120–124; see RR2-06). | "`satisfied` at `55bbf9e`" (H:61) is accurate. The recorded digest `bf1557dc…` reproduces over TX lines 58–71 (4,660 bytes) at `55bbf9e`. |

**Coverage gap.** No working review checked:
- SR1-09, 10, 11 and 13;
- SR4 N-1–N-5, T-5–T-7, P-1–P-7, W-0 and W-1–W-3.

That population includes two of D's declines, SR1-11 and P-2. Both have residuals (RR2-01, RR2-03). H:63–65 says only that the results "support this repair handoff". It does not name the unchecked population (RR2-05). H:77–80 also claims protected scope; `git diff --stat afb6ad6 cab9800` touches no `build_tenants/` or `comments/claude/` file.

## Findings

None of these blocks the scope reviewed here.

### RR2-01: low; blocks the next input selection only

**Claim.** It is ambiguous whether the next tenant input needs owner sign-off first.

**Evidence.**
- T1:128 says "The next C3 snapshot is recorded in T-002 after common sign-off". It sits in a C1 section and is not labelled superseded.
- T1:51 supersedes only the Selected Contract.
- WL:196 gates only "Treating round 2 as accepted common law" on sign-off.
- H:93 at `cab9800`: "After common review, explicitly select and record the next tenant input".

**Smallest correction.** Mark T1:128 historical, or state in WL:196 whether input selection waits for sign-off.

### RR2-02: low; mildly interested

**Claim.** The primaries named on alias rows conflict with the primaries their constituent rows give by the first-listed rule.

**Evidence.**
| Alias row | Alias primary | Constituent | Constituent row and its primary |
|---|---|---|---|
| H-M1 (WL:157) | I3-02 | CR2-04, CR2-09 | WL:135, I3-03 |
| H-M2 (WL:158) | I3-08 | CR4-F3 | WL:143, I3-06 |
| H-M4 (WL:160) | I3-10 | CR5-04 | WL:146, I3-14 |
| H-M4 (WL:160) | I3-10 | CR5-06 | WL:148, I3-11 |
| H-M7 (WL:163) | I3-01 | CR2-21 | WL:136, I3-02 |

This is TC-03's counterexample in a new place. TR:49 left the alias primaries out of its check ("retain their scope").

**Smallest correction.** One sentence: an alias row's primary records the aggregate finding, and constituents close under their own rows.

### RR2-03: low

**Claim.** The constraint-surface requirement states no purpose or material relation, although the specification requires one of every new obligation.

**Evidence.**
- R:66–76 has only "Source:".
- P:397 requires that a restatement add "no new obligation without naming its purpose and material relation".
- Five sibling sections carry such a paragraph: R:88, 103, 125, 148 and 167.
- D:75 declines SR1-11.

**Smallest correction.** Add one purpose sentence to R:66–68.

### RR2-04: low; applies to this review too

**Claim.** Two reviews under the same frame used different clause vocabularies. This report maps its own labels in the Independence section.

**Evidence.**
- RF:24 does not bind "scoped clause results" to installed values.
- CC:47 returns `satisfied` for each clause.
- TC:135–164 uses "Supported", "Partly corrected" and "Supported as a clarification". It defines them at TC:135, but maps them to no installed value.

**Smallest correction.** RF:24: "with clause results in the installed result family".

### RR2-05: low

**Claim.** The handoff does not state which part of the round-1 findings the working reviews left unchecked.

**Evidence.** Section 3 above; H:63–65.

**Smallest correction.** One sentence in H or T1 naming the population that no working review checked.

### RR2-06: low; applies to this review too

**Claim.** P:399 defines authorship as "material contribution to the subject or the repair under review". It does not say whether a Reviewer whose finding prescribed the correction may then assess it.

**Evidence.**
- TR assessed the TC-03 rule it had offered (TC:128–129).
- This Claude round assesses corrections its own round prescribed.

**Smallest correction.** One clause in P:399, for example: "proposing a correction is disclosed and does not by itself bar assessment".

### RR2-07: low; partly interested

**Claim.** Some of D's labels misstate the outcome or the claim being answered.

**Evidence.**
- SR1-08 is labelled "Prescription declined", but P:332 adopts that prescription.
- SR2-13 is labelled declined, but CAP:3 was edited as prescribed.
- N-1 is answered by rebutting "no historical acceptance". SR4 proposed "reopened, not accepted".
- N-4 is answered as a "Bias claim". SR4 said "not a defect of form".

There is no consequence for the specification.

**Smallest correction.** A follow-up note in the pen's next record. Frozen D stays as written.

### RR2-08: low

**Claim.** The review packet is defined by the list's own source table, and the reviews it leaves out are not named. So a coverage check against that packet cannot detect an omitted review, which is the same mechanism that missed F in round 1.

**Evidence.**
- WL:115–117: "The finite packet is the reviews named in the source table above … The index does not claim coverage of every historical project review."
- Three reviews are absent from WL:43–52 without being named:
  - the common-contract review `…T001000Z`, whose F1 is disposed at TX:73;
  - the applicability record `…T234754Z`, whose substance sits under key E;
  - the consolidation review `…T011752Z`, which raised no finding.
- D:114 disposes SR3-03 as "not inherently circular".

**Smallest correction.** Add one row naming these three reviews and the place where each one's findings are disposed.

### Observations

**O-1 (*interested*).**
- No surface on `main` holds the Claude line's obligations under the iteration-3 standard.
- WL:177 routes uptake to the peer's "own ticket". T2C:30 still reads "State: drafted, not started", yet F reviews that line's revision 2 at `768cf8c`.
- The pen's grant excludes T2C (T1:27). Who records the peer line's state on `main` is the owner's decision. This is not a defect of the round-2 text.

**O-2.** Out of scope here, for expectation 12:
- "consumer" remains undefined;
- "contracted" (P:397, R:45) persists beside "reduction".

## What holds

- **Repairs.** M6, M7 and M8 close against the round-2 expectations. M9 is partly closed: parts 2–4 close, and part 1 is met for each key's direction but not for the packet's own boundary (RR2-08).
- **The peer report.** It is committed byte-identical to the file read in round 1. Its index is faithful and does not adopt a tenant's claims about itself (*interested*).
- **The disposition record.** D accounts for all 69 finding IDs, A1–A9 and both observations. 62 of the 69 are repaired as prescribed or by an equivalent. Of the two remaining declines, P-2 holds for construction authority and SR1-11 holds for reduction; each leaves one low residual.
- **Process.**
  - The three working reviews state accurate subjects, results and limits.
  - The falsified TC is preserved rather than rewritten.
  - The TX digest note reproduces.
  - Protected scope holds.
- **Repeated rule.** The result/data anti-evasion rule (R:146) and the conjunction (P:200) are stated once and consumed consistently.

## Limits

- The reviewer read neither candidate.
- It verified the installed builder clauses only through the citations in CC and TC.
- It did not rerun H's link or whitespace counts.
- It sampled 22 of the 69 dispositions in depth, and classified the rest from D against targeted reads of the cited lines.
