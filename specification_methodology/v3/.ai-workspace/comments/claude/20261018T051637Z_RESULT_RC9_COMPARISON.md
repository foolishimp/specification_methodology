# Result: evaluation of the two RC9 candidates, with the basis recommendation

Author: the Claude tenant session. It wrote the Claude line and ran this
evaluation as its test manager, so its judgment carries an author's
interest. It executes the [plan](20261018T042139Z_PLAN_RC9_COMPARISON.md)
committed at `71c0a82c` before any reading result, and the
[rule resolution](20261018T045136Z_PLAN_RC9_COMPARISON_RULE_RESOLUTION.md)
committed at `34089acf` before any read 2 result. The owner's instruction
was: "I want a full evaluation between the two implementations, and which
one should I take to V3 released". The owner runs Codex's evaluation of the
same subjects in parallel; this session has not opened it. This post is
commentary. It accepts, merges or releases nothing.

## Answer

**No.** Neither candidate is a qualified choice under the ratified
[Candidate Comparison](../../../specification/PRODUCT.md#candidate-comparison)
rule. All six criteria are `unresolved` on both. The shared actual-use
protocol has not been recorded or run, and a desk trace cannot satisfy
criterion 4. Taking either line to a v3 release now is the owner's
decision outside that rule.

**Basis recommendation: the Codex line, with its fidelity repairs made
before release.** Read 2 shows parity on decision correctness: each line
decides all ten scenarios as the common text requires. Under the rule as
resolved before read 2, parity gives Codex. Read 1's material Claude lead
does not change the recommendation; it sets the tradeoff that comes with
it:

- Codex reached the same ten decisions with 54% of Claude's bytes. It is
  nearer a release that meets the written Product:
  - its interpretation is complete and packaged;
  - its authority compressions are carried;
  - its identity gate covers every member;
  - no review finding is open.
- Codex's owner text drops at least one clause from 16 of the 65 common
  expectations. Fifteen of those clauses are carried in full nowhere in its
  corpus. The heaviest:
  - "outcome evidence" in the condition for claiming an outer outcome
    (CR-9);
  - the premises of conditional proofs (CR-3);
  - the rule that a corrected run is not an unchanged independent test
    (AR-31);
  - any subsection for the sixth assurance relation.

  No scenario exposed these gaps, but an actor relying on Codex's text
  would not learn the clauses. The common text supplies their wording, so
  the repair is bounded. Each repair also rebuilds the interpretation
  determinations over the changed lines.
- The Claude line carries every common expectation across its corpus, and
  the readers found its routes the more precise. It still owes:
  - 183 sections and 15 members of interpretation;
  - the ten authority compressions;
  - 419 semantic conservation readings;
  - repairs to its entry and its record.

  It also cost 1.86 times Codex's bytes on these scenarios.

The rule gives Codex whether or not the owner's baseline scoping narrows
the release's a_c.STDO requirement, because read 2 found no decision that
the Codex text gets wrong. The rule was fixed before read 2. The author's
interest lies with the other line.

## Subjects

| Line | Exact subject | Identity checked |
|---|---|---|
| Codex | package `5592168e26759f37e730aed12c030a6061709ec4`, checkpoint `c46e9f96` on `tenant/codex/c3-iteration-5`; label `3.0.0-rc.9` | five label and coordinate files differ from the reviewed `5a5b5ad8`; every other byte is identical |
| Claude | commit A `c2cfa9b908d1722ae3f26c32fa4ece691083bdc3` (tag object `ac905d6`), commit B `3a209713` on `tenant/claude/c3-synthesis`; label `3.0.0-rc.9` | commit A holds the content; commit B adds its review package; the package's reproduction changes only its two declared records |
| Common input; builder | C3-I5-06 `4c340f7`; installed `v2.5.1-rc.2` | both lines bind it |

Both worktrees and `main` stayed at these commits for the whole evaluation,
apart from this session's own posts.

## What each candidate is

Measured by this session from Git objects. "rc.2" is the installed
predecessor `v2.5.1-rc.2`.

| Measure | Codex | Claude | rc.2 |
|---|---|---|---|
| Method members | 18 files, 1,205,622 bytes (1.42× rc.2) | 23 files, 2,083,876 bytes (2.46×) | 16 files, 848,544 bytes |
| Paragraphs of 80 or more characters copied verbatim from rc.2 | 1,929 of 2,647 (73%); 53% of bytes | 163 of 2,374 (7%); 3% of bytes | — |
| Task frames | 7, 525,729 bytes, largest 99,366 | 12, 1,184,208 bytes, largest 144,806 against a capacity of 160,000 | — |
| a_c interpretation: the axiomatic-calculus account of the method's determinations | 709 determinations; their source spans cover 21,310 of 21,687 standards lines (98%) and every leaf section except the glossary (2 of 16 covered) and the standards entry (0 of 4); packaged with program, map, source account and consumer entry | 155 clauses over parts of 24 sections in 8 members; 183 sections and 15 members not encoded; not in the release manifest | — |
| Authority compressions: short normative restatements pinned to their owners | 10 carried, 32 pins match | none; deferred under decision Q8 | 10 |
| Installed package | 90 members, 38,958,677 bytes | 62 standards members (23 Markdown members, 13 frame files, 2 schemas, 24 templates), 17 plugin files, licence, release note | — |
| Conservation record: one row per predecessor claim | 691 rows: 595 conserved, 95 superseded, 1 not applicable. Every row is an author proposal marked `indeterminate` in the record. Outside it, I5 test 2 read 25 conserved rows blind on the I5 subject: 23 conserved, 2 undecidable | 650 rows: 603 conserved, 28 superseded, 19 not applicable, stored as `not` (finding E2). Nonauthors read 184 conserved rows: 182 conserved, 2 changed and since repaired. 419 unread | — |
| Owner decisions pending | 95 replacements in 36 questions | 28 rows in Q1 to Q19, plus Q8 (compressions) and process decisions Q11 to Q16 | — |
| How a member shows the law it derives from the foundations | family tables over groups of sections, for example SPEC_METHOD Method Families and FOUNDATIONS Core contract derivations; per-determination arguments in the interpretation | family tables in every member, 318 rows or more, each with a consumers paragraph | — |

## Gates, reproduced in disposable clones

| Check | Codex | Claude |
|---|---|---|
| The line's own reproduction command or commands | `package.py verify`: exit 0 in 11 s; only elapsed time and checkout path differ from the committed receipts | the 13 commands of REVIEW-PACKAGE-RC9: all exit 0 in 16 s; only the two declared files change |
| One word changed from "must" to "may" in SPEC_METHOD | exit 1: "Documentary member differs from source freeze" | caught by the frame check, because a frame quotes that sentence |
| The same change in a member no frame quotes (UX) | exit 1: "Documentary member differs from source freeze: standards/UX_METHOD.md" ([log](assets/20261018T042139Z_RC9_COMPARISON/CODEX_UX_FAULT.log)) | all six gates exit 0 |

Codex's gate compares every member with its source freeze. The Claude
line's member identity rests on commit A and its manifest; no gate checks a
working-tree member that no frame quotes.

## Findings

### Raised in the cross-family reviews since the I5 comparison

Standing at the RC9 subjects. Rows citing text were checked against the
RC9 bytes.

Raised by Codex against the Claude line:

| Finding | Severity | At RC9 | Repair read back by |
|---|---|---|---|
| R1 installed package lacks bootstrap schema and template | Major | repaired | Codex, candidate 3 |
| R2 observation must separate subjects, not predicate truth | Medium | repaired | Codex, candidate 3 |
| R3 functional preference made absolute; necessity exception lost | Medium | repaired | Codex, candidate 3 |
| R4 generic tickets enforce an optional recurrence policy | Medium | withdrawn by Codex, since rc.2 already imposed it; owner decision Q18 | Codex, candidate 3 |
| R5 and C3-01 ODD no-action outside the result algebra | Medium | repaired | Codex, candidate 5 |
| R6 conformance member imports its oracle | Medium | repaired, scoped as a qualification map | Codex, candidate 3 |
| R7 and C3-04 stale interpretation entry | Low | repaired | Codex, candidate 5 |
| C3-02 freeze command exits 0 after failed controls | Medium | repaired | Codex, candidates 5 and 8 |
| C3-03 Design family omits the F13 import | Low | repaired | Codex, candidate 5 |
| C5-01 repeated design surprise forces `design_reframe`, and four more sites where a symptom decides a cause | Medium | repaired | Codex, candidate 8 |
| C5-02 enumeration helper exits 0 on failure | Low | repaired | Codex, candidate 8 |
| RC8-01 a reported failure read as actual disagreement | Low | repaired in rc.9 | **no nonauthor yet** |
| I5 E2 a disposition value truncates `not applicable` to `not` | Low | **open**: 19 rows in `frontier/REVIEW.json` | rechecked by this session |

Raised by Claude against the Codex line:

| Finding | Severity | At RC9 | Repair read back by |
|---|---|---|---|
| RC1 a rival reuse rule (RF-005) in every frame | material | repaired | Claude, root-cause review |
| RC1 authority without a single owner | material | repaired: one owner, Judgment and authority | Claude, root-cause review |
| RC1 the construction owner drops seven conditions and adds three | material | repaired | Claude, root-cause review |
| RC1 and root cause: a constitutional gap at intake writes Goals or Intent, at four sites | material | repaired at every site found | Claude, RC4 readback |
| Root cause: UP-007 authorship rewritten while recorded conserved | material | repaired | Claude, RC4 readback |
| RC4-1 Reviewer compression narrower than its source | Low | repaired | Claude, final readback |
| RC4-2 Worked Binding recorded conserved | Low | repaired; now a proposed supersession | Claude, final readback |
| RC4-3 the tenth drift signal names no drift | Low | repaired | Claude, final readback |
| RC4-4 items 1 and 2 | Low | withdrawn by Claude; the sources already stated them | — |
| RC4-4 item 3 Totality omits continuation and recovery | Low | repaired | Claude, final readback |
| three inherited interpretation shortcuts | Low | repaired | Claude, final readback |
| I5 S2, Codex's own: the generic assessor names "exact live code" | Low to Medium | repaired: "exact live realisation under the selected computational binding" | this session, RC9 |
| RC1 foundation-to-law for inherited rules stated only outside the text | disputed | a design difference, not an agreed defect | — |

### Found in this evaluation

None of these changes a scenario decision. Each was confirmed by this
session on the RC9 bytes.

- Claude line:
  - the installed entry `standards/README.md` still opens with a stale
    `Status:` line ("under construction member by member … the first pass
    (steel threads T1 to T4) is its starting text"); found by this session;
  - the entry's frame table lists 10 of the 12 frames, and
    `acceptance-release` and `member-build-assess` appear nowhere in the
    entry; read 2b;
  - no frame's stated task covers evaluating and reusing results after a
    change; six frames are named after trial tasks; read 2a.
- Codex line:
  - no task row in the entry covers realising requirements as a build
    tenant, so S7's decision is assembled from four places in SPEC_METHOD;
    read 2b;
  - Test Case Authority and the Ambiguity Governance Rule are reachable
    from no task row; read 2a.

Net: Codex's final content carries no open review finding and has a clean
cross-family readback. The Claude line carries one open Low finding (E2),
one Low repair without a nonauthor readback (RC8-01) and three entry
defects.

## Read 1: owner-text fidelity, blind

The key is revealed: **A is the Claude line, B is the Codex line**, in all
three reads. The preimage
`A=claude;B=codex;salt=d0fb7c66cc854a8ed6bfb411b6852686` hashes to
`16e4156b…0507`, the value committed in the plan. At I5 the key was the
reverse: A Codex, B Claude.

One fresh-context Fable reader, author of neither line, graded the same 65
expectations as I5 test 1 against each line's named owner sections. Its
grades:

- `present`: the named owner section carries the expectation with the same
  meaning and force;
- `present elsewhere`: another passage of the supplied files carries it;
- `changed`: a condition, list item, distinction or determination is
  dropped or altered;
- `absent`, `cannot decide`, and `contradiction` with the specification.

| Line, run | present | present elsewhere | changed | absent | cannot decide | contradictions |
|---|---|---|---|---|---|---|
| Claude, I5 | 55 | 3 | 6 | 0 | 1 | 0 |
| Claude, RC9 | **59** | 5 | 1 | 0 | 0 | 0 |
| Codex, I5 | 42 | 2 | 19 | 1 | 1 | 0 |
| Codex, RC9 | **42** | 7 | 16 | 0 | 0 | 0 |

By group, as present / elsewhere / changed:

| Group (expectations) | Claude I5 | Claude RC9 | Codex I5 | Codex RC9 |
|---|---|---|---|---|
| Construction relation (27) | 24 / 2 / 1 | 26 / 1 / 0 | 16 / 1 / 9, 1 absent | 18 / 3 / 6 |
| Assurance relations (31) | 30 / 0 / 1 | 31 / 0 / 0 | 25 / 0 / 6 | 23 / 0 / 8 |
| Frame basis (7) | 1 / 1 / 4, 1 undecided | 2 / 4 / 1 | 1 / 1 / 4, 1 undecided | 1 / 4 / 2 |

The gap in `present` widened from 13 to 17, mostly on the Claude side.
Claude's `present` rose from 55 to 59 while Codex's stayed at 42. Codex
gained 2 in the construction relation and lost 2 in the assurance
relations. Its `changed` fell from 19 to 16 and its `present elsewhere`
rose from 2 to 7. Different reader instances graded the two runs, so the
movement mixes change in the text with reader variance.

Every one of Codex's 16 `changed` is partial. The reader found the main
obligation carried and one clause, list item or rationale missing, and it
marked three as minor. Those with the most force:

- CR-9: "outcome evidence" became a preservation argument in the
  condition under which a decomposition may claim the outer outcome;
- CR-3: "under the build-tenant binding" and "conditional proofs retain
  their premises and scope" are missing from the construction owner;
- AR-31: "a corrected run is not an unchanged independent test" is
  missing from evidence reuse;
- AR-28 and AR-29: the sixth assurance relation, formal representation and
  demonstration, has no subsection in Codex's owner text.

The other eleven are CR-7, AR-3 and AR-6 (the reader's minor ones), CR-8,
CR-23, CR-27, AR-8, AR-17, AR-30, FB-2 and FB-3. The
[read 1 report](assets/20261018T042139Z_RC9_COMPARISON/READ1_REPORT.md)
gives each with its evidence. Claude's one `changed` is FB-2, the return's
three-way distinction between semantic conservation, demonstrated reduction
and mere relocation. Codex also lacks it.

**Supplementary whole-corpus check, by the test manager, not blind.** The
packet gave the reader Claude's ACTIVATION and FOUNDATIONS but only Codex's
FOUNDATIONS, so a clause Codex states in another member could not count.
This session searched both whole RC9 corpora (all members, frames and
entries) for each missing clause, by phrase and by concept:

- Claude's FB-2 is carried at `standards/EVALUATION.md:469–476` and in the
  member-build-assess frame, line 11;
- Codex's FB-3 is carried in substance by its two entries: "Structural
  validation does not establish semantic fidelity or acceptance"
  (`successor/README.md:27`) and "No view supplies universal task
  sufficiency" (`successor/standards/README.md:61`);
- Codex's CR-3 build-tenant binding is owned by SPEC_METHOD and applied at
  `DESIGN_MODULE_METHOD.md:1632`; the conditional-proof clause is not found;
- Codex's CR-8 conditions concurrency on its composition law
  (`FOUNDATIONS.md:662`) but states no permission to proceed concurrently;
- the clauses missing from the other thirteen, including the four
  rewordings CR-7, CR-9, AR-3 and AR-6, are not found anywhere in Codex's
  corpus.

Across whole corpora, Claude carries 65 of 65 expectations. Codex carries
50 in full and the other 15 in part. A phrase and concept search can miss
a carrier worded far from the common text. The Claude line restates the
common wording closely, so both the reader's grades and this check may
favour it.

## Read 2: ten scenarios by route, blind

Two more fresh-context Fable readers, authors of neither line, traced S1 to
S5 and then S6 to S10 on both candidates, under the same key. Each reader
entered at the candidate's installed `standards/README.md`. For S5 it
entered at the frame it chose from the frames' task statements. It followed
only declared routes: links, sections the text names, and frame source
lines. It recorded:

- hops: sections acquired beyond the entry;
- bytes acquired;
- reconciliations of passages that decide one point differently;
- decisions no route reached.

Only after all its traces did it grade each scenario against
[EXPECTED.md](assets/20261018T042139Z_RC9_COMPARISON/EXPECTED.md):

- `delivered`: decided by route, completely, as the expected distinction
  says;
- `partly`: decided in part, off-route, or only after a reconciliation;
- `not delivered`: decided differently or left undecided;
- `cannot tell`.

| Scenario | Claude | hops | bytes | Codex | hops | bytes |
|---|---|---|---|---|---|---|
| S1 a report labelled "bug" at intake | delivered | 13 | 88,424 | delivered | 5 | 37,375 |
| S2 resuming from a summary the workspace contradicts | delivered | 6 | 60,639 | delivered | 4 | 24,794 |
| S3 lawful steps, failed acceptance condition | delivered | 7 | 100,552 | delivered | 3 | 23,186 |
| S4 relaxing a threshold so the realisation passes | delivered | 21 | 111,909 | delivered | 12 | 57,728 |
| S5 reusing evidence after a requirement change | delivered | 9 | 43,237 | delivered | 7 | 35,320 |
| S6 a Product rule the requirements omit | delivered | 9 | 54,882 | delivered | 8 | 43,198 |
| S7 requirements realised as a human process | delivered | 5 | 54,668 | delivered | 12 | 61,693 |
| S8 a parity bit as the only observation | delivered | 6 | 125,941 | delivered | 7 | 49,742 |
| S9 a broken decoder reports a failure | delivered | 9 | 100,071 | delivered | 7 | 47,305 |
| S10 acceptance with a pending replacement | delivered | 4 | 42,543 | delivered | 10 | 40,936 |
| **Total** | **10 of 10** | 89 | 782,866 | **10 of 10** | 75 | 421,277 |
| Median per trace | | 8 | 74,532 | | 7 | 42,067 |

Codex acquired 54% of Claude's bytes overall. It used fewer bytes on 9 of
the 10 scenarios (all but S7) and fewer hops on 7.

Reconciliations and unreachable decisions:

- S1, Claude: the reader reconciled "classify the report as a lawful
  change" in SPEC_METHOD Procedures with gap analysis that "keeps open what
  the evidence cannot yet separate".
- S4, Codex: the reader could not reach, from any task row, the
  ticket-level rule against editing a test to match the code. The expected
  distinction does not require that rule.
- S7, Codex: the reader noted that the family table at the head of
  SPEC_METHOD disclaims its own modal force, so the actor must confirm the
  rule in the owner sections. They carry it.

No other trace needed a reconciliation or left a decision unreachable.
Read 2b judged the three expected distinctions marked "Test manager's
reading" (S6, S8, S9) to be correct applications of their quoted sources.

Where the readers judged each line most likely to mislead a fresh actor:

- **Codex, by omission.**
  - Test Case Authority and the Ambiguity Governance Rule are reachable
    from no task row (S4, S1).
  - No task row covers a build-tenant binding. The human-process
    permission sits in the SPEC_METHOD Method procedure list, filed under
    an unrelated family row (S7).
  - Intake leans on undefined shorthand: F1 to F6, and Z.
  - Read 2a also flagged its "ordinary work entry" as missing. That plugin
    file is in the package at
    `successor/plugins/spec/skills/stdo-work/SKILL.md`; only the packet
    left it out.
- **Claude, by routing and volume.**
  - No frame's stated task covers evaluating and reusing results (S5). The
    chosen frame paraphrases the reuse owner, and an actor choosing
    `acceptance-release` would miss it.
  - The frame table hides the two frames made for acceptance and member
    assessment (S10).
  - Route labels land one hop short: "prove a realisation" lands in
    EVALUATION, while the deciding sentence is in ACTIVATION.
  - Routes name whole sections whose family tables and consumer lists
    decide nothing new. This was roughly half of every acquired range, and
    it made S8 and S9 cost 2 to 2.5 times Codex's.

The readers credited the Claude text with precision at the point of
decision. Its routes are task-shaped and land on the rule for S6, S7 and
S10, and ACTIVATION 331–334 states S4's distinction verbatim. Its effect
values give the most exact treatment of an unknown external write (S2),
and it reaches the test-edit rule by route. The two readers' verdicts on
cost were:

- read 2a: Codex "lets a fresh actor act correctly more reliably at lower
  cost";
- read 2b: Codex is cheaper "on four of five", and Claude "is the more
  reliable guide where the question concerns the build-tenant binding, and
  its routes are more precise everywhere, at roughly 1.5× the bytes".

## Hypotheses

| Hypothesis | Outcome |
|---|---|
| H1: the I5 gap of 13 `present` narrows to at most 5, and neither line contradicts the specification | **falsified**: the gap is 17; no contradictions |
| H2: each line delivers at least 8 of 10 scenarios; neither is `not delivered` on S1 to S5 | **holds**: 10 of 10 each; no `partly` or `not delivered` |
| H3: Codex delivers S6 and S7; Claude delivers S8 and S9 | **holds**: the repaired classes are delivered on both lines |
| H4: Claude's median bytes per trace exceed Codex's, and its median hops are no more than Codex's | **falsified in part**: bytes 74,532 against 42,067, as predicted; hops 8 against 7, against the prediction |

## Standing per criterion

| Criterion | Codex | Claude |
|---|---|---|
| 1 dispositions and loci | `unresolved`: 691 rows with one disposition each; 2,250 local links resolve; 32 compression pins match; no cross-family check of the dispositions | `unresolved`: 650 rows with one disposition each; 771 loci resolve; 19 values truncated (E2); no cross-family check |
| 2 conservation | `unresolved`: every row `indeterminate` in its own record; 25 rows read blind at I5 on an earlier subject; 73% of paragraphs verbatim, so wording identity is mechanically checkable, but coherence with the new foundations needs reading | `unresolved`: 184 of 603 read by nonauthors, 419 unread; 97% of bytes rewritten, so each row needs a semantic reading |
| 3 accepted replacements | `unresolved`: 95 proposals in 36 questions | `unresolved`: 28 rows, plus the deferred compressions |
| 4 actual use | `unresolved`: nothing run on RC9 | `unresolved`: nothing run; trial design and 7 hashed expectation sets from I4 |
| 5 discriminators and interpretation fidelity | `unresolved`: 80 conformance rows `not_performed`; 6 author logical evaluations for the binding repair; whole interpretation packaged with 19 negative identity controls; no independent fidelity assessment | `unresolved`: 52 member discriminators, 3 of the 7 integrated-closure discriminators and 9 construction and 12 assurance discriminators mapped to cases and logical-review checks; no logical review recorded; interpretation partial, same-family fidelity review only |
| 6 reduction | `unresolved`: byte measures only | `unresolved`: 8 of 46 paths route-traced against rc.2 at I3 and I4 |

Read 2's hop and byte counts measure what a desk reader acquired on these
ten scenarios. They indicate acquisition cost. They are not the
deciding-path comparison against the predecessor that criterion 6 needs.

## Distance to a v3 release

A release here means the cut that the Product and the stack-release
procedure describe:

- an accepted candidate whose six criteria and integrated closure hold;
- the owner's replacement decisions recorded;
- a packaged a_c interpretation;
- a coordinated cohort under one version: plugin, Axiom Indexer, STDO
  Representation, and the generated a_c.STDO program and map.

Neither line is there.

Work both lines owe, whichever is chosen:

- the shared actual-use protocol, recorded by the common pen, and its run
  (criterion 4);
- the logical reviews of the discriminators (criterion 5);
- deciding-path reduction evidence (criterion 6);
- the owner's packaging, cohort and cut decisions, then the release
  mechanics.

Work that differs:

| | Codex | Claude |
|---|---|---|
| Fidelity repairs (read 1) | 15 clauses carried in full nowhere, including a subsection for the sixth assurance relation; each repair rebuilds the interpretation determinations over the changed lines | none |
| Routing repairs the traces suggest | task rows for a build-tenant binding (S7) and for test-case authority and ambiguity governance (S4, S1); plain terms for F1 to F6 and Z at intake | the two frames missing from the entry's frame table; a frame or route for evaluating and reusing results (S5); route labels that land one hop short |
| Open findings | none | E2 (19 values), the stale entry line, RC8-01's readback |
| Owner replacement decisions | 95 rows in 36 questions | 28 rows in Q1 to Q19, plus Q8 and Q11 to Q16 |
| Nonauthor conservation reading still owed | 595 author proposals; wording identity is checkable for the verbatim 73% | 419 rows, each a semantic reading |
| a_c interpretation | complete and packaged; independent fidelity assessment owed | 183 sections and 15 members to encode, then fidelity, then packaging |
| Authority compressions | carried and pinned | 10 to write and pin |
| Acquisition on the ten scenarios | 421 KB, 75 hops | 783 KB, 89 hops |
| Corpus to maintain | 1.21 MB, 18 members: rc.2's layout plus two new members | 2.08 MB, 23 members in a reconstructed layout; the largest frame at 90% of capacity |

When admitting the Claude line's rebuild, the owner scoped three of its
gaps as follow-on work: "im going to put those out of scope as they can be
done by any llm, i's after the baseline STDO V3". The three are:

- complete interpretation coverage;
- the remaining actual-use expectation sets;
- the authority compressions.

Under that scoping they fall after a baseline v3. The stack-release
procedure counts a re-authored a_c.STDO program and map for the released
corpus as part of any release request "unless the owner explicitly narrows
the requested operation". Whether the scoping narrows the v3 release is the
owner's decision. It changes the Claude line's cost to release but not
this recommendation (see Answer).

## Limits

- **Reader family.** The readers and the test manager are Claude family,
  the same family as the Claude line. The owner's parallel Codex evaluation
  is the counterpart.
- **Blinding is weak.** Tenant names were scrubbed. Member names,
  structure and style still identify the lines, and the Claude entry's
  stale `Status:` line survives scrubbing as "the [tenant] tenant's
  candidate".
- **Who wrote the tests.** The test manager wrote S6 to S10 and the three
  readings marked as such in EXPECTED.md. S1 to S5 come from this line's
  own RC1 review of Codex.
- **Desk traces only.** All reads are desk traces, so they give no
  evidence for criterion 4. Byte counts follow each reader's reading.
  Claude's routes name whole sections without saying where to stop, so its
  counts are full-section reads.
- **Packet asymmetry in read 1.** The packet held two Claude files and one
  Codex file. The supplementary check covers the asymmetry but is not
  blind.
- **Reader variance.** Different reader instances ran I5 and RC9, so part
  of the I5-to-RC9 movement is reader variance.
- **Tool calls and departures from procedure:**
  - read 1: 32 tool calls; it read the two candidates' owner sections in
    one batch rather than strictly in turn;
  - read 2a: 45 tool calls; it located named sections by heading index,
    and for S5 read the owner sections directly instead of the frames'
    verbatim copies;
  - read 2b: 42 tool calls; it located sections by heading map, and for S7
    on Codex found the Method section by grep before confirming that a
    family row names it.
- **Codex's evaluation not read.** This session did not open Codex's
  comparison directory `comments/codex/20261018T040150Z_RC9_COMPARISON/`.

## Records

[assets/20261018T042139Z_RC9_COMPARISON/](assets/20261018T042139Z_RC9_COMPARISON/)
holds:

- the three reader reports:
  [read 1](assets/20261018T042139Z_RC9_COMPARISON/READ1_REPORT.md),
  [read 2a](assets/20261018T042139Z_RC9_COMPARISON/READ2A_REPORT.md) and
  [read 2b](assets/20261018T042139Z_RC9_COMPARISON/READ2B_REPORT.md);
- the revealed [key](assets/20261018T042139Z_RC9_COMPARISON/KEY.json);
- the packet hashes, the scenarios and expectations, and the builder and
  measurement scripts.

The 76 packet files still match their recorded hashes.

## Not decided here

The owner's choice; the shared protocol, which the common pen records; any
acceptance, merge, push or release.
