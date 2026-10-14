# CR4: Cross-Family Review of the Codex v3 Synthesis Candidate

Reviewer: a Claude context, cross-family to the Codex Writer. Read-only; nothing repaired.
Subject: `build_tenants/codex/` frozen at `9bc8962`. The scratch copy of `successor/` and `design/` is byte-identical to `git archive 9bc8962` (checked with `diff -rq`).
Evidence: `qualification/` at `3ad1fca`, a descendant of `9bc8962`.
Common inputs: the files under `$S/common` match the hashes recorded at 9810215 (PREDECESSOR_CLAIMS `fbeb8fd…`, PRODUCT `5527d27…`, requirements README `032541f…`).
Base: Codex candidate at `31f28f9`. Predecessor: installed v2.5.1-rc.2.
Scripts and intermediate data are kept outside the subject, in `scratchpad/cr4work/`.

Verdicts use these terms:
- **holds**: the predecessor meaning is present with the same modal force.
- **elsewhere**: the meaning is present, but not at the recorded locus.
- **changed**: the meaning or force differs from the predecessor.

## 1. Frontier completeness

| Check | Result |
|---|---|
| Rows in FRONTIER.json / CONSERVATION.json | 691 / 691. The id sets are identical, there are no duplicates, and disposition, locus and successor SHA agree field by field. |
| Match to the common PREDECESSOR_CLAIMS.md (691 rows: 635 sections, 1 synthetic Traversal child, 36 non-body, 19 auxiliary) | Exact set equality, once the `standards/` prefix is stripped from the 36 non-body ids. |
| Dispositions | 657 `conserved`, 33 `superseded`, 1 `not applicable` (`release/release-note.md`, with a bounded reason), 0 `intentionally removed`, 0 `unresolved`. |
| Loci for conserved and superseded rows | 690 loci, one per row. All 690 resolve to an existing file and heading: 0 missing files, 0 missing anchors. Two UX em-dash headings resolve through explicit `<a id>` anchors. 0 mismatches between `successor_sha256` and the frozen file SHA. |
| Fourteen-members row (`TRAVERSAL_OCCURRENCE_PROFILE.md#closed-profile-signature-fourteen-members`) | Absent at `31f28f9` (690 rows). Restored at `7e698cb` (691). The 107-byte sentence is carried verbatim (frozen TOP L1343–1344). The successor AC derivation list still declares 14 addresses, so the count stays true for the bound edition. **Holds.** |
| Standing | All 691 rows read `review: current_independent_review_pending` and `acceptance: owner_review_open`. 656 of the 657 conserved rows carry no note on what is carried; only the fourteen-members row has one. |
| Independent checking | None at row level. The synthesis reviews were Claude-family (`claude-opus-5-5`, 32 runs). Integration reviews read Codex diff hunks against the Codex preimage 5b4aebb, not rc.2 rows. `final-integration-profiles/RESULT.md` says: "'Lost predecessor claim' means lost relative to the preimage hunk. I could not check whether a PREDECESSOR_CLAIMS row dispositions it." Most integration reviews bind 875a56e or 9982ab8. Only the a_c rechecks and the effect-owner check reach 146e6ad or 9bc8962. **The dispositions are author claims.** |

History of the dispositions:
- From `31f28f9` through `a746559`, every row is `conserved` (690, then 691).
- At `3ad1fca`, the map is 657/33/1, against common input 9810215.

## 2. Conservation sample (criterion 2)

Method:
- Word-level diffs of predecessor → frozen for all 78 section rows whose locus text changed between base and frozen. The changes break down as:
  - 49 conserved rows;
  - 29 superseded rows;
  - 0 locus changes;
  - base sections ≈ predecessor bytes (556 of 636 locus sections are byte-identical to rc.2).
- A sentence search of the whole frozen package for every rc.2 sentence missing from its locus. 113 sentences are not verbatim anywhere: 105 removed in this synthesis and 8 already absent at base. Each one was then read by hand, because most are rewordings.
- Coverage: 42 determinations sampled across 35 rows, weighted to SPEC, RF, STDO_RFB, TOP and TL.

| # | Row [disp] | Predecessor (rc.2) | Candidate (9bc8962) | Verdict |
|---|---|---|---|---|
| 1 | RF#return-a-closed-result [C] | "An unchanged consumer checks exact applicability and reuses a valid closed result. Role, conversation or resumption changes alone do not invalidate it." | Locus: "The consumer applies the core workspace/context validity rule before reuse." FOUNDATIONS#workspace-and-context: "Unchanged independent work remains usable" (permissive), with no role/conversation clause. SPEC_METHOD L1397: "A new role, conversation or resumption reuses valid C after checking exact applicability." | Elsewhere (SPEC); the locus points to a weaker owner |
| 2 | RF#return-a-closed-result [C] | "Changed material inputs or a declared revising observation invalidates the affected result before reliance" | SPEC L1398–1400: "…material evidence invalidates its affected claims before reliance"; FOUNDATIONS: "Changed support reopens the affected dependent claims" | Elsewhere |
| 3 | RF#evaluate [C] | "applies the frame's declared invariants, evidence rules, and result algebra" | "…and predicate-bound core result refinement under RF-012" | Holds (re-pointed) |
| 4 | RF#reference-frame [C] | "\(R\) is the closed result algebra" | "\(R\) is the shared core result algebra with the frame's declared refinements" | Changed, minor: the owner of R moves from the frame to FOUNDATIONS under a conserved label |
| 5 | RF#rf-012-closed-results [S] | Five-value baseline family; "an externally owned compatible extension may refine this algebra while preserving explicit indeterminate, out-of-frame, and invalid-basis pressure" | Five verdicts owned by FOUNDATIONS; refinement "cannot erase a failure, unknown, refusal, non-performance or uncertain effect" | Supersession justified; values conserved |
| 6 | RF#result-conjunction [S] | "Missing, wrong-subject, conflicted or indeterminate mandatory results remain unresolved under the declared rule" | "conflict annotates retained contradictory contributions and cannot downgrade an authenticated applicable falsification" | Changed (a conflict containing a falsification becomes falsified); correctly superseded |
| 7 | RF#result-conjunction [S] | "Common agreement cannot discard a constraint or material counterexample found by only one contributor." | "Counting agreeing frames cannot discharge another frame's constraint." plus FOUNDATIONS conjunction rule 1 | Holds |
| 8 | STDO_RFB#3-worker-returns-to-executive [C] | "Every coordinated Worker activation terminates in one closed work result sent to Executive." | "Every **completed** coordinated Worker activation returns one closed work result … Interruption or loss of the actor is observed as unreturned work" | **Changed** (universal obligation narrowed) under a conserved label |
| 9 | STDO_RFB#3-worker-returns-to-executive [C] | "`satisfied -> candidate_ready`, `falsified -> refused`, `indeterminate -> incomplete`, and `out_of_frame \| invalid_basis -> re_entry_requested`" | "Each refined case accompanies exactly one core verdict under the mapping in `Work result`" (where `incomplete, postcondition_defeated` → `falsified`) | **Changed** (fixed mapping replaced) under a conserved label |
| 10 | STDO_RFB#work-result [S] | "`incomplete` accompanies `indeterminate`"; "The mapping is total and exclusive" | Cause-qualified table; "total over these declared cases" | Correctly superseded |
| 11 | STDO_RFB#executive [C] | "It holds the complete Product view and current MVP or release mandate" | "maintains a sufficient bounded delivery view … the Executive need not load the whole Product" | **Changed** under a conserved label |
| 12 | STDO_RFB#7-executive-disposes-and-checkpoints [C] | "revalidates the complete Product view" | "revalidates the sufficient bounded delivery view" | **Changed** under a conserved label |
| 13 | STDO_RFB#closure [S] | "maps exclusively from one closed Reference Frame Method result"; "complete Product view" | "maps to one core verdict on its exact predicate"; "sufficient bounded delivery view" | Correctly superseded. The over-labelling hypothesis does not hold here. |
| 14 | STDO_RFB#status-and-authority-boundary [C] | Table: "frame declaration, activation, result algebra, conjunction, … \| `REFERENCE_FRAME_METHOD.md`" | Result and conjunction reassigned to `FOUNDATIONS.md`; RF keeps "frame-specific result refinement" | **Changed** (owner reassigned) under a conserved label |
| 15 | STDO_RFB#complete-engagement-transition [C] | "same sufficient intake, work-result algebra" | "…work-result refinement" | Holds |
| 16 | STDO_RFB#reviewer-result-and-triage-projection [C] | "total across the Reference Frame Method result algebra" | "total across the shared core verdicts as bound by RF-012" | Holds |
| 17 | STDO_RFB#executive-attention-evaluation-and-action [S] | "The Executive retains the frontier and closed-result ledger in attention" | "acquires the portion of the durable … closed results material to its current decision … cannot drop a material dependency" | Correctly superseded |
| 18 | SPEC#manifesto [C] | "We require **code** to be derivable from requirements and design" | "We require **realisation** to be derivable…" (the chain states "code is the software case") | Holds (generalised; code is still covered) |
| 19 | SPEC#universal-intake-triage [S] | Six change classes, e.g. "`realization_refactor`: local code, configuration, or attribute change … must prove no upstream drift" | Same six classes; code → "implementation, procedure"; flow through "Realisation" | Classes hold; the supersession covers the added current-state intake step |
| 20 | SPEC#constitutional-chain [S] | "Projection reconstructs current truth from the event stream." | "presents the observations relevant to a declared question … does not require every consumer to replay a complete" stream | Correctly superseded |
| 21 | SPEC#proportional-disposition [S] | "Assessment returns one of these semantic dispositions"; re_enter: "Product, requirement, identity, lifecycle, authority, public contract, or accepted design must change" | "returns evidence and a proposed semantic disposition. Only the existing decision authority applies that disposition"; re_enter: "without an owning-layer change" | Correctly superseded. The enumerated layer list becomes generic. |
| 22 | SPEC#checkpoint-continuation-progress-and-churn [C] | "A proposed restart identifies why repair of retained work is insufficient, which obligations and evidence survive, and which causal assumptions change" | "If a proposed recovery instead discards or rebuilds work, identify why repair … which causal assumptions change and which existing operation grant permits that effect" | Holds. "Restart" is redefined; an added grant condition is stricter. |
| 23 | SPEC#position [C] | "make software re-derivable, auditable, and correctable" | "make governed work re-derivable…" | Holds (generalised) |
| 24 | AC#derivation-provenance [C] | "The definitions and laws below are the **sole normative authority** for the meaning of `a_c`" | "…own the `a_c` specialization … and explicitly consume its common result and composition owners" | **Changed** (exclusivity removed) under a conserved label |
| 25 | AC#traversals-and-functor-kinds [C] | "\(\Omega_v\) is its closed stop algebra" | "closed stop refinement. The traversal binds each outcome … to one core verdict" | Holds (closedness kept) |
| 26 | AC#ac-007-constraint-and-refusal [S] | "A failed, missing, indeterminate, out-of-scope, or invalid-basis result follows the declared result algebra rather than being coerced to success." | Core mapping table; "no refusal is coerced to success"; "Missing mandatory evaluations remain explicit coverage residuals" | Correctly superseded; anti-coercion kept |
| 27 | TOP#op-002-atomic-semantic-admission [C] | "Missing, conflicting, or inconsistent members refuse the cut." | "A demonstrated missing or inconsistent required member defeats the complete-cut predicate; missing judgment support keeps the cut unadmitted … No unresolved or refused cut admits a subset." | Partly changed: non-admission holds, but the refusal outcome is split and "conflicting" is dropped, under a conserved label |
| 28 | TOP#closed-profile-signature-fourteen-members [C] | "For the calculus edition bound by this profile publication candidate, that population has fourteen members." | Verbatim | Holds |
| 29 | TOP#closed-constraint-judgment-residual-and-stop-kinds [S] | "stale source frontier retains hold plus `stale_frontier` and requires reconstruction" | "its `hold` decision with cause `stale_frontier` prevents use and requires reconstruction. Unknown currentness is indeterminate." | Substance holds; superseded for the verdict mapping |
| 30 | TOP#candidate-judgment-event-and-relation-separation [S] | "A missing cut judgment, non-`admitted` decision, wrong subject or digest, or cross-basis judgment refuses the semantic cut." | "…leaves the semantic cut unadmitted; these conditions do not all establish the same verdict"; "a held or absent judgment alone does not fabricate a refusal" | Correctly superseded (the compression contradicts it: see F3) |
| 31 | DESIGN#3-core-rule [C] | "If a reader must inspect … mutable workspace state … to determine what the system means, the design is too imperative" | "must infer governing meaning from … mutable workspace conventions … rather than the admitted contract … Inspecting current workspace state remains necessary" | Holds; narrowing qualifier (state → conventions), same force |
| 32 | DESIGN#8-totality-rule [C] | Whole section | Verbatim, plus a result-record binding | Holds |
| 33 | DESIGN#cross-view-axiom-evaluation [S] | "The design pack **must evaluate** every applicable … axiom with one of: `pass`; `fail`; `not_applicable`, with a reason." | "The design pack **evaluates** … using the shared result algebra"; a supported `not_applicable` falsifies applicability | Superseded. The modal shifts from "must" to the indicative. |
| 34 | TICKET#execution-contracts [C] | "log the admitted execution basis **into runtime/event truth**" | "record … **on the selected durable work surface**" | **Changed** (event-truth duty relaxed) under a conserved label; the relation sits only on the SPEC chain row |
| 35 | TICKET#recorded-judgment-and-owner-ruling-continuity [S] | "A new role or conversation alone is not an invalidator." | Dropped at the locus; present at SPEC L1397 | Elsewhere |
| 36 | TICKET#condition-based-closure-and-reuse [S] | "evidence presence alone is not satisfaction" | "evidence presence alone is not completion"; closure through core conjunction | Holds (could have stayed conserved) |
| 37 | WRITING#practical-layer-checks [C] | "…rewrite or delete." | "…delete within the owning authority. A predecessor determination retains its recorded UP-015 disposition…" | Holds; added restriction |
| 38 | POSTING#boundary [C] | Section text | Verbatim, plus "report any judgment through the complete core result" | Holds; new duty on commentary, with its purpose named through F2/F6 |
| 39 | README#standards-library [C] | "Project-local copies remain possible when explicitly bound and verified, but are not the default." and six further claims | README#distribution-and-entry: "A local copy is operative only when explicitly bound and verified; it is not the default." The rest is in README#method-owners. | Elsewhere (inherited from base) |
| 40 | WM#admissibility, UX#13b, RELEASE#acceptance-criteria, ODD#11.5 [C] | Section texts | Verbatim, plus additive result/conjunction bindings | Holds |
| 41 | TOP#finite-reference-domain-table [C] | "This table is the complete specialization of `RefDomain_Sigma_occurrence(record_kind, qualified_field)`" (rows cover the 14-field AC-014 Judgment) | Same completeness sentence (L212). Adds `J:*.predicate` and `J:*.residuals` rows and "close all nineteen Judgment fields". | Holds: the completeness claim is kept and the row set is extended as a consequence of the superseded AC-014 (14 → 19 fields) |
| 42 | TOP#mutable-subject-effect-relation [S] | "`refused_effect` … with evidence that no **authorized** mutation began" (L984) | "…with evidence that no mutation began" (L1138) | Correctly superseded (stricter) |

**Tally (42 determinations):**
- 18 hold.
- 4 are present elsewhere, with an incomplete or weaker locus: #1, 2, 35, 39.
- 9 changed under a conserved label: #4, 8, 9, 11, 12, 14, 24 and 34, plus #27, which is partly changed.
- 11 are correctly superseded, with their meaning changed: #5, 6, 10, 13, 17, 20, 21, 26, 30, 33, 42.

**Possible over-labelled supersession.** Four `superseded` rows have locus text byte-identical to the predecessor section. They are either over-labelled, or superseded by an external clause such as DESIGN's new Governing Relations; the record names no such clause.
- `DESIGN#2-position`;
- `DESIGN#transformation-admission-completeness-stdo-up-016`;
- `RF#rf-002-finite-attention`;
- `RF#closure`.

**TRANSFORMATION_LIBRARY.** It carries no frontier row; nor does FOUNDATIONS. Its changes from base to frozen remove restatements of SPEC and FOUNDATIONS owners (UP-020 accept/repair/re-enter/reject conditions, retry/churn, acquisition). Each removed determination survives at its single owner: SPEC#proportional-disposition, or FOUNDATIONS#bounded-construction ("Repeating a failed relation needs a supported causal change"). No predecessor determination is lost through TL.

## 3. Compressions

The AC, DESIGN, ODD, SPEC, TICKET and UX compressions changed only in their `source_digest` pin and the removed `generated_by/at` (4-line diffs). TOP and the bootstrap gained a preamble. `stdo_compressed` updated its pins and three passages. Every compression keeps `stale_if_source_digest_changes: true`, and the pins now equal the changed members' SHAs, so the staleness guard reports them fresh.

| Compression | Statement | Member | Result |
|---|---|---|---|
| `stdo_compressed.md` L275 | "`Goals -> Intent -> Product Definition -> Requirements -> Design -> Code -> Events -> Projection -> …`" | SPEC_METHOD L1003: "… Design → Realisation → Observations → Projection → Delta" (row superseded) | **Contradicts** |
| `traversal_occurrence_profile.compressed.md` L152–153 | "A missing cut judgment or non-admitted decision refuses." | TOP L945–947: "…leaves the semantic cut unadmitted; these conditions do not all establish the same verdict"; L963: "a held or absent judgment alone does not fabricate a refusal" | **Contradicts** |
| `plugins/spec/references/GETTING_STARTED.md` L588 (auxiliary, conserved) | "Executive combines that evidence with the complete Product view" | STDO_RFB#executive: "need not load the whole Product" | Contradicts (stale) |
| `stdo_compressed.md` (Worker mapping, result family, Executive view) | Updated to the Work-result refinement, FOUNDATIONS verdicts and bounded Product frontier | Members | Consistent |
| `spec_method.compressed.md` L365 | "Assess a bounded candidate as `accept`, `local_repair`, `re_enter`, or `reject`." | SPEC#proportional-disposition: assessment proposes; decision authority applies | Coarser; not contradictory |
| `axiomatic_calculus.compressed.md` | No Judgment field list is restated, so the 14 → 19 change has nothing to contradict | AC-014 | No contradiction found |

**Disposition consequence.** The common granularity rule says a compression "is disposed with reference to that body's rows". Two compressions are recorded as `conserved` although the body rows they compress are `superseded`:
- `stdo_compressed` compresses SPEC#constitutional-chain;
- the TOP compression compresses TOP#candidate-judgment.

Six compressions (AC, DESIGN, ODD, SPEC, TICKET, UX) were re-pinned with no content change while their bodies gained 1–4 superseded rows each.

## 4. Cross-Synthesis ports (not independent)

This reviewer is the source family for every ported part, so these port findings are **not independent**.

**What the Codex line took.** DESIGN.md "Source contributions" names five parts from the Claude tree at `31f28f9`:
1. ACTIVATION context construction and refinement.
2. ACTIVATION work state and reuse.
3. FOUNDATIONS evidence, identity and conservation.
4. PROFILES binding.
5. ACTIVATION/TRAVERSAL evidence-sensitive result maps.

**Form of the ports.** They are concept reconstructions, not text copies:
- 6-word shingles that are new in frozen and absent from both rc.2 and the Codex base match the Claude standards only 11 times. The matches are incidental phrases, e.g. "the design pack evaluates every applicable".
- `METHOD_RETURN.md` confirms this: "reconstructed the owned consumers on the Codex source rather than copying the peer corpus".

**Requirements of the Cross-Synthesis contract (PRODUCT.md, "Cross-Synthesis"):**

| Requirement | Finding |
|---|---|
| Each part is named | Yes, in DESIGN.md. |
| One owning section per part | Not met. Receivers are multi-section, e.g. "Foundations workspace/context and bounded construction; library Acquire" and "Family use contracts and Spec tenant binding". |
| Inside one member's frontier cone | Not met. The receivers FOUNDATIONS and TRANSFORMATION_LIBRARY carry 0 frontier rows, and no frontier row records a contribution. |
| The disposition it supports | Not recorded. |
| Reviewer compares with source and predecessor | Not done. No review prompt contains Claude source text. `core-review` states "imported-source fidelity and owner approval of review policy are outside this judgment". T-002-CODEX plans "nonauthor Codex working checks for imported source", but no result is retained. |
| Written only in Codex territory | Holds. No Codex-construction commit touches paths outside `build_tenants/codex/`. The other non-codex changes from 31f28f9 to 3ad1fca are common-input commits (ancestors of 9810215) or the common T-002 record `14fedcd`. |

**Fidelity spot check (not independent).** The source for contribution 2 is Claude ACTIVATION §7. It states "a role, conversation or resumption change alone invalidates nothing … invalidate the affected result before reliance". The receiving owner, FOUNDATIONS#workspace-and-context, omits both clauses, and RF now delegates to that owner (sample #1, #35). The clauses survive only at SPEC L1397. ACTIVATION §5 restart/idempotence is reproduced faithfully: FOUNDATIONS "A workspace that retains partial progress does not make every operation idempotent"; SPEC checkpoint "discards or rebuilds work".

## 5. Findings

| ID | Severity | Claim | Evidence | Origin | Smallest repair |
|---|---|---|---|---|---|
| F1 | High | Six `conserved` rows carry a changed predecessor meaning; two more are minor or partial. Each should be `superseded` with a named relation, or have its predecessor text restored. | Sample #8, 9, 11, 12, 14, 24, 34; minor #4, partial #27. In each case the base section equals rc.2 and the change is at 9bc8962. | Introduced | Re-dispose STDO_RFB#executive, #3, #7, #status-and-authority-boundary, AC#derivation-provenance and TICKET#execution-contracts as superseded, naming the owner and relation. Review RF#reference-frame and TOP#op-002. |
| F2 | High | The conservation record makes a false statement about its own history. | CONSERVATION.json `synthesis.meaning` (new at 3ad1fca) reads "Author loci and pins refreshed; dispositions and historical judgment subjects unchanged." The trace shows a746559: 691 conserved; 3ad1fca: 657/33/1 (34 dispositions changed). | Introduced | Correct `synthesis.meaning`, and list the 34 changed dispositions with the commit. |
| F2b | Low | The `limits` entry is ambiguous beside 33 supersessions. | `limits`: "No removal, supersession, checkpoint acceptance or release is selected by this map". Identical at a746559. It is readable as "not decided here". | Inherited | Reword to "proposed, not accepted". |
| F3 | Medium | Compressions and a plugin reference contradict the changed members. Re-pinned digests defeat the staleness guard. Compression dispositions are not taken with reference to their bodies' superseded rows. | §3: `stdo_compressed` L275; TOP compression L152–153; GETTING_STARTED L588. Both compressions are `conserved` while their body rows are `superseded`. Six compressions were re-pinned without a content change. | Introduced (re-pin) | Regenerate the affected statements from the members, or unpin them so they read as stale. Re-dispose the compression rows against their bodies' rows. |
| F4 | Medium | The Cross-Synthesis contract is unmet for the ports: no single owning section, no frontier cone, no supported disposition, no source/predecessor comparison. | §4; DESIGN.md table; review prompts; T-002-CODEX L44. | Introduced | Record each part as part → one section → rows/disposition. Run the source + predecessor comparison under the owner's ported-part policy. |
| F5 | Medium | Determinations moved out of their recorded locus. The single-locus field cannot express multi-locus carry. | #1, #2, #35: the role/conversation clause is at SPEC L1397 only, while the RF locus delegates to FOUNDATIONS, which lacks it. #39: README claims are in other README sections. | Introduced (#1, #35); inherited (#39) | Add the carrying loci, or restate the clause in FOUNDATIONS#workspace-and-context. |
| F6 | Medium | `superseded` rows do not name an identifiable, accepted replacement relation (criterion 3). | 33 rows share 14 reason strings (one string covers 5 rows; three strings cover 4 rows each). Every locus is the old section, not the replacing owner. Four rows are byte-identical to rc.2 (DESIGN#2-position, DESIGN#UP-016, RF#rf-002, RF#closure). | Introduced | Give each row its replacing owner anchor and relation. For the four unchanged rows, name the replacing clause or re-dispose them as conserved. |
| F7 | Low | New "Governing Relations" sections in DESIGN, IDENTITY, ODD, TOP, UX and WM re-bind every consumer to the core record and conjunction, with no per-row note. Unflagged supersessions are likely; F1 shows them in the Baseline. | ODD Governing Relations: "The consumers below return the shared result record and use result conjunction for required obligations." 656 of 657 conserved rows have no note. | Introduced | Row-level independent check of each member under a global binding. |
| F8 | Low | Modal and scope shifts inside superseded rows are not called out. | #33 "must evaluate" → "evaluates"; #21 the enumerated re-entry layers become generic. | Introduced | Note them in the relation text. |

## 6. What holds

- The frontier is complete and exact: 691/691, with one disposition each. All 690 loci resolve, the SHA pins match, and the fourteen-members row is restored and true.
- 556 of 636 locus sections are byte-identical to rc.2. Most of the 49 changed conserved rows only add bindings and keep the predecessor text verbatim, e.g. DESIGN#8, WM#admissibility, UX#13b, the RELEASE rows, ODD#11.5, IDENTITY#parsing-law.
- Where a change is substantive, `superseded` is generally applied correctly: RF-012, result conjunction, Work result, the SPEC chain, proportional disposition, TOP candidate judgment, STDO_RFB#closure.
- Of the 55 non-body rows, schemas, most templates and most plugin members are byte-identical to rc.2. The template changes are additive. The release-note `not applicable` reason is bounded.
- TRANSFORMATION_LIBRARY loses no predecessor determination. Single ownership improved: the UP-020 conditions are now stated once, at SPEC.
- No port text was copied, and no Codex construction write was found outside Codex territory.
- RETURN.md truthfully calls the map an author map: "A resolving locus is not independent semantic acceptance". It lists the open obligations. F2 is the exception.

## 7. Limits

- 42 determinations out of 49 changed conserved rows and 29 changed superseded rows were sampled. The 558 sections that did not change from base to frozen were checked only mechanically (byte or sentence identity); they are not semantically re-read under the new global bindings (F7).
- This reviewer is Claude, the family of the port source, so §4 and F4/F5 are not independent on fidelity.
- Non-body rows were checked in two ways. Content checks covered:
  - every base → frozen diff (compressions, two templates, the stdo-work skill);
  - targeted greps of the compressions and plugin references for superseded statements.

  The remaining members were checked by SHA identity only, against rc.2 or the base.
- Conformance discriminators (criterion 5), actual use (criterion 4) and the a_c interpretation are out of scope.
- `14fedcd` is a common ticket record on main. Git authorship (owner identity on all commits) does not reveal which actor wrote it.
