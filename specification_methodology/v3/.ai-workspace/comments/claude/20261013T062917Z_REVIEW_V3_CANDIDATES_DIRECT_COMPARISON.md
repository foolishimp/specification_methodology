# REVIEW: Direct comparison of the Claude and Codex STDO v3.0.0 candidates, and the path forward

**Author**: Dimitar Popov
**Date**: 2026-10-13T06:29:17Z
**Addresses**: the Claude candidate `build_tenants/claude/` and the Codex candidate `build_tenants/codex/` at `31f28f90c4a9b15243d84630fc4799024a9cd7ac`; the two cross-assessments ([Claude on Codex](20261013T043048Z_REVIEW_CODEX_V3_CANDIDATE_CROSS_ASSESSMENT.md), [Codex on Claude](../codex/20261013T043456Z_REVIEW_CLAUDE_V3_CANDIDATE_CROSS_ASSESSMENT.md)); the [C3 Construction Contract](../../../specification/PRODUCT.md#c3-construction-contract); step 3 of the [revised strategy](20261013T012745Z_STRATEGY_categorical_groundwork.md)
**Status**: Open
**Updated**: 2026-10-13T08:24:10Z (errata after Codex's critique, appended below; the body is unchanged so line citations to it still hold)

## Summary

Jim asked which of two paths to take: (1) a synthesis, or (2) fix each candidate and test them against each other. This review recommends **path 1, a staged synthesis**. Three findings support it.

1. **The two cross-assessments nominated complementary parts.** The Codex assessor nominated Claude's activation, recovery, work-state and profile-binding contracts and its foundation objects. I nominated Codex's carried corpus, frames, premise and specialization tables, and import and equivalence distinctions. The two lists do not overlap. Selecting either candidate whole discards what the other family's assessor found worth keeping.
2. **Head-to-head actor tests cannot choose a base.**
   - **The pilot.** A pilot task built around the parts where the candidates differ (resuming work after an uncertain effect) was run twice on each candidate and on rc.2. All six runs met the oracle except for four partial items.
   - **The one consistent difference.** In both Claude-route runs the actor wrote new query files instead of finishing the previous actor's draft. That traces to a qualification case's expectations shipped in Claude's resume route, so it is a fixable route defect, not a difference in method quality.
   - **Context size.** The method text supplied was 25.1 KB for Claude, 29.1 KB for Codex and 84.1 KB for rc.2.
   - **Earlier runs.** The 17 earlier runs across both cross-assessments showed the same parity on four ordinary tasks. The exceptions were the carrier-retention item, which no route fully satisfied, and one triage item that rc.2's compressed route missed until source re-entry.
3. **The cost that separates the bases is per-member acceptance, and it is very uneven.** Acceptance criterion 2 requires an author-independent semantic comparison for every conserved row.
   - Codex carries rc.2 text byte for byte, so most of its comparison is mechanical.
   - Claude restated the corpus: 1,625 of 8,692 rc.2 sentence units survive unchanged, by Codex's count. Each of its 658 conserved rows needs a real comparison.
   - Both paths can start with the same test: one matched member cone accepted in both candidates. After that, the difference between the paths is merging parts or selecting one candidate whole. Full acceptance of both candidates arises only if Jim wants two accepted lines.

What the synthesis ends up as depends on Jim's ruling on "restated on the axioms" (K2), not on this review:
- **Permissive ruling** (declared ownership plus explanatory correspondence suffices): the result is Codex's carried corpus with Claude's nominated contracts ported in.
- **Strict ruling** (derivation per family): carried members do not satisfy it, so the result moves toward Claude's restated members, with Codex supplying the premise discipline, the derivation tables and the frame format.

The first step is the same under either path. Take one matched member cone (RELEASE is proposed) through full C3 acceptance in both candidates, and measure the Reviewer's cost, findings and repair rounds. This is the only head-to-head test that can discriminate, and it also tests the cost premise behind the synthesis. It waits on Jim naming the Executive and Reviewer actors.

Disclosure: the assessor is the same model family as the Claude candidate's author, and is not a fresh session (§1). To limit that interest, the synthesis ports only parts the other family's assessor nominated, and anything beyond those carries its own stated reason.

## 1. Decision, subject and protocol

**Request.** Jim asked on 2026-10-13 to "run an additional review comparing both implementations directly with a recommended 1. synthesis path or 2. apply fixes ot each and then test them out against each other", then said "i want you to do the same". He has asked Codex for the same comparison. This review recommends a path and its limits. Selection or combination of candidates remains his decision ([PRODUCT.md:157](../../../specification/PRODUCT.md#c3-construction-contract)).

**Subjects.** Both candidates were taken at `31f28f90c4a9b15243d84630fc4799024a9cd7ac`, which is still `main` HEAD. They were read with `git archive` into a scratch directory outside the repository, and nothing was read from the working tree. The common inputs, at the same commit, were:
- INTENT;
- PRODUCT (C3 Construction Contract, lines 120–157);
- `requirements/PRINCIPLES.md`;
- `requirements/PREDECESSOR_CLAIMS.md`;
- `conformance/README.md`.

The installed rc.2 was re-verified at 06:46Z: `stdo verify v2.5.1-rc.2 --manifest-sha256 3d860ff4…2782` returned no failures.

**Assessor and interest.**
- **Model.** Claude Opus 5.5 in the Claude Code CLI. It is the same family as the author of the Claude candidate.
- **Prior exposure.** This session wrote the cross-assessment of the Codex candidate (SHA-256 `428380e9…be76f`) and has read Codex's cross-assessment of the Claude candidate (`8918b3e2…5b03`). It also read parts of both candidates before fixing the pilot oracle.
- **Consequence.** The protocol's independence condition is not met for the Claude side. Mitigations:
  - porting is limited to cross-nominated parts;
  - the pilot oracle is drawn from common and rc.2 sources only;
  - all scored outputs are kept for re-scoring by another family.

**Parallel review.** A Codex post named `20261013T064524Z_REVIEW_STDO_V3_DIRECT_COMPARISON_AND_PATH.md` appeared during this review. It was not opened.

**Envelope.** Jim set none. I declared 90 minutes from 06:29:17Z and a USD 5 cap on paid probe calls, following the earlier grant. Measured probe spend is USD 0.5248 over six runs. Wall time is in the closing section.

**Calibration.** Five criteria are rated below on my sealed rc.2 baseline (section SHA-256 `baacdb6e…485c`, in the cross-assessment). The two cross-assessments' ratings are not set side by side, because different assessors calibrated them differently. For example, Codex rated rc.2's C02 Partial and I rated it Weak. This review supersedes neither cross-assessment.

**Effects.** One new post. No other file was edited and nothing was committed.

## 2. The two candidates side by side

| | Codex candidate | Claude candidate |
|---|---|---|
| Strategy | Carry rc.2 members byte for byte. Add a foundation layer and bind carried members to it by explanatory preambles. | Restate rc.2 into members organised by the C3 tiers. Tier 1 is FOUNDATIONS, REFERENCE_FRAME, ACTIVATION, AXIOMATIC_CALCULUS, IDENTITY and EVALUATION. SPEC_METHOD is split across SPEC_METHOD, PRODUCT_DEFINITION, ASSURANCE, ACTIVATION and EVALUATION. |
| Top-level Markdown | 18 members, 912,824 B: the 16 rc.2 names plus FOUNDATIONS (19,206 B) and TRANSFORMATION_LIBRARY (19,213 B). The 10 compression assets are carried. | 23 members, 1,172,611 B. rc.2's 16 members total 848,544 B. |
| rc.2 text retained | No rc.2 sentence removed; 159 sentences added (cross-assessment §3, mechanical). | 1,625 of 8,692 sentence units unchanged (Codex cross-assessment; not re-run here). |
| Premises | F1–F6 with explicit standing: "adopted commitments … not theorems derived from finite capacity alone" (`successor/standards/FOUNDATIONS.md:48–81`). | P0–P6, with P4 split into P4a and P4b. Each names its premises (`standards/FOUNDATIONS.md:241–333`). Also an ontology, authority kinds, an algebra and hypothesis H1. |
| Foundation→law | One family, work/recovery, is shown as premise → conditional consequence → particular contract and independent choice (`TRANSFORMATION_LIBRARY.md:93–119`). The candidate says it is "not a claim that every existing method has already been reconstructed" (`FOUNDATIONS.md:80`). | Members cite P-labels. ACTIVATION gives one conditional refinement induction (`ACTIVATION.md:433–455`). Derivation per family is not shown (Codex cross-assessment, C02). |
| Activation units | Five verbatim, digest-bound responsibility views of 14,426–25,683 B (`qualification/C3/FRAME_INPUTS.json`). "No view is sufficient for every task" (`standards/README.md:12–25`). Other tasks route to owner sections. | Fifteen task frames plus a bootstrap frame, as a_c projections: 38,689–98,438 B materialized and 18,801–50,000 B reference-only (`a_c/set-6/README.md:117–134`). There is no resume frame; resume routes to raw ACTIVATION §5 and §7, TICKETS §7 and the T-05 case (`standards/README.md:28`). |
| a_c | A six-clause finite interpretation with a 608-case check, run by the author. | Set-6 program: 423 clauses with zero diagnostics. Fidelity is a Writer self-check (`a_c/set-6/README.md:3–17`). |
| Frontier record | `FRONTIER.json` has 690 rows, all `unresolved`. `CONSERVATION.json` has 690 author claims, all `conserved`, including the 10 compression assets. One common row is missing (§5). | `frontier/PREDECESSOR_CLAIMS.md` has 691 rows of author claims: 658 conserved, 20 not applicable, 2 superseded and 11 unresolved. |
| Packaging | No manifest or release note. Getting-started coordinates are placeholders. Identity issuance resolves predecessor bytes (K4). Compression bodies do not reflect the foundation layer, which conflicts with their `conserved` claim. | 11 unresolved rows: the 10 compression assets and the bootstrap entrypoint, which is still `a_c/REPLACE_WITH_SET/frames/bootstrap-PENDING-RULING` (`templates/PRODUCT_DEFINITION_TEMPLATE.json:28`). The entry routes to set-4 (`standards/README.md:42`). |
| Verified defects | Missing frontier row (§5). | `TRAVERSAL_OCCURRENCE.md` hashes to `2e97d78a…6afb`, but set-6 `README.md:51` binds `79f75845…ce14a`, so the traversal projection is stale. Checked at byte level in this session. |
| Shared | No author-independent member acceptance. No categorical constructs. Both bind construction to the installed rc.2 calculus, which is a lawful construction dependency. Executive and Reviewer actors are unbound. | Same. |

The candidates disagree about where the work should go. Codex postponed the restatement and kept conservation cheap. Claude did the restatement and made conservation expensive to verify. Neither has shown that the full corpus follows from its foundations.

## 3. Five deciding criteria on one calibration

These five criteria are the ones the choice of path turns on. Scale: Strong means a sufficient declared contract in scope; Partial means useful contracts with material gaps; Weak means a mention or a burden of proof without a usable construction.

| Criterion | rc.2 baseline (sealed) | Codex | Claude | Evidence | What separates them |
|---|---|---|---|---|---|
| C02 Foundation→law, ownership and use | Weak | Weak; Partial on one branch | Partial | Codex: this assessor's cross-review, mechanical and source checks. Claude: Codex's cross-review plus heading-level reading of `FOUNDATIONS.md` §3 here. | Claude organises all members on its premises and gives one conditional proof. Codex gives one complete premise → consequence → choice chain. Neither has derivation per family. |
| C03 Standalone conservation | Reference | Strong: semantic availability, checked mechanically | Partial | Codex: no rc.2 sentence removed, all changed text inspected. Claude: Codex's 20-relation sample found no regression; the pilot's resume determinations were carried (§4). | The difference is not a found loss. Claude's availability is shown on a sample; Codex's by construction. This is the criterion-2 cost asymmetry. |
| C09 Representation and frame fidelity | Partial | Strong for frames in scope; Weak for a_c coverage | Partial | Codex: verbatim excerpts with digests. Claude: broad structural a_c encoding, one stale member digest, self-checked fidelity. | Verbatim frames are faithful by construction and cheap to regenerate. a_c projections need encoding review and go stale when a member changes. |
| C15 Measured usability | Unassessed | Partial | Partial | §4 pilot plus the 17 earlier runs. | Parity on outcomes. Bytes are close on resume (25.1 KB Claude, 29.1 KB Codex). On the earlier tasks Codex's units were 10–26 KB against Claude's materialized 63–68 KB. |
| C16 Evidence | Partial | Partial | Partial | Both cross-reviews. | Neither has a closed author-independent member gate. Both conservation maps are author claims. |

## 4. Head-to-head pilot: resuming work after an uncertain effect

**Why this task.** The candidates differ most on work state and recovery. Claude restated it as ACTIVATION §5 and §7. Codex projects verbatim rc.2 excerpts as `frames/WORK_RECOVERY.md`. A resume task touches C3 audience task "resume work another actor left" and five common conformance rows. It was the most likely place for a difference to show.

**Fixed before any context was assembled.** Each file below is in the external pilot directory.

| File | SHA-256 |
|---|---|
| `task_W.md`: the Ledgerline T-41 scenario | `24906a5e5e6aacabeca8554d9d4c7c23b92c6e0a5b94a15b75e10d43e0a53a34` |
| `oracle_W.md`: items W1–W9 | `9253727c0ceee058f1c121dba4ee63b2a2c4c7bdae12291875ffacc20aed765b` |
| `route_rule.md` | `021c868cd918302481716190bc74dca96fa73472ae0ae90000b7e8b41b40184e` |
| `card.md`, unchanged from the earlier nine runs | `ba185604ef4116460bb44806f096e19a00b255645a61e64997f68c15a16f3d67` |

The oracle's sources are:
- the common conformance rows "Interruption leaves authored progress", "Actual failed assessment A and uncovered required B", "Basis or evidence changes", "Required coupled context cannot fit" and "A parse or map succeeds";
- PRINCIPLES P4–P6;
- rc.2 `REFERENCE_FRAME_METHOD.md:409–442` (closed results) and `:674–690` (result conjunction);
- rc.2 `TRAVERSAL_OCCURRENCE_PROFILE.md:974–1015` (`partial_effect`).

The oracle covers:
- **W1** retaining the previous actor's progress;
- **W2** keeping the effect uncertain and observing before any repetition;
- **W3** keeping A1's counterexample, with A2 as uncovered required coverage;
- **W4** that neither Marco's message nor any assessment grants authority, and that only Priya can authorize a re-run or the drop;
- **W5** refreshing what the REQ-17 basis change affects and keeping the rest;
- **W6** batch 2 as indeterminate;
- **W7** distinct step states;
- **W8** not claiming the 2.1 GB log;
- **W9** a closed non-success result returned to Priya with its residuals.

**Route rule.** Each candidate receives what its own entry designates for "resume work another actor left": its frame if it publishes one, otherwise the sections its README route names, verbatim and in order. No assessor-built frame is used. rc.2 receives its ordinary entry, the bootstrap plus the aggregate compression. The actor, flags, system prompt and runner are unchanged from the earlier nine runs (`claude -p --model sonnet`, no tools, no MCP, a fresh empty directory per run). Calls were sequential, two per cell.

| Route | Method material | Method bytes | Context bytes |
|---|---|---:|---:|
| Claude | `ACTIVATION.md` §5 and §7, `TICKETS.md` "Recorded judgment and owner-ruling continuity", `qualification/cases/T-05/CASE.md` | 21,685 | 25,127 |
| Codex | `successor/standards/frames/WORK_RECOVERY.md` | 25,683 | 29,125 |
| rc.2 | `authority_compressions/stdo_bootstrap.md` + `stdo_compressed.md` | 80,608 | 84,050 |

**Results.** All six runs resolved to `claude-sonnet-5-5`, returned code 0 and `is_error: false`. Input tokens are new plus cache creation plus cache read.

| Run | Input tokens | Output tokens | USD | Wall s | Score (S satisfied, P partial) | Notes |
|---|---:|---:|---:|---:|---|---|
| Claude 1 | 11,054 | 5,640 | 0.1006 | 49.6 | 7 S, 2 P | **W1 partial:** calls W1's `verify_v4.sql` "an unrun draft [that] counts as nothing" and writes a new file instead of finishing it. **W7 partial:** "Steps 3 to 6 of the topology have not lawfully occurred", while also recording G-9 as consumed by the dispatch. |
| Claude 2 | 11,052 | 4,865 | 0.0535 | 40.8 | 8 S, 1 P | **W1 partial:** leaves the draft untouched, uses it "only as a draft" and writes its queries "as a new file" that does "not count as the bounded post-observation of record". Claude 1 had the same pattern. |
| Codex 1 | 12,093 | 3,364 | 0.0782 | 32.9 | 9 S | |
| Codex 2 | 12,094 | 4,713 | 0.0521 | 40.0 | 9 S | |
| rc.2 1 | 31,391 | 4,297 | 0.1647 | 35.8 | 8 S, 1 P | **W3 partial:** labels the unperformed A2 `indeterminate`. That conflates an evaluation nobody performed with evidence that cannot decide. |
| rc.2 2 | 31,392 | 6,879 | 0.0757 | 58.7 | 9 S | |

**Reading.**
- **Outcome parity, with one consistent route difference.** The rc.2 W3 partial and the Claude 1 W7 partial each appear in one run of a cell and not the other. The Claude-route W1 partial appears in both runs. Every Codex and rc.2 run finishes W1's `verify_v4.sql` in place; both Claude runs write new queries instead. The cause is route content (see confounds and the candidate finding), not the restated work-state law. rc.2's ordinary route otherwise performs as well as either candidate.
- **Context cost differs only against rc.2.** Both candidates used about a third of rc.2's input tokens (11.1k and 12.1k against 31.4k).
- **Compare cost on first runs.** Second runs read the provider cache that first runs created, so compare on input tokens or first-run cost (USD 0.1006, 0.0782 and 0.1647), never on averaged USD.
- **Conservation in use.** Claude's restated ACTIVATION §5 and §7 carried the resume determinations as fully as Codex's verbatim rc.2 excerpts. That is a small data point in favour of the restatement.

**Confounds.**
- One scorer, of the Claude family. One task. Two runs per cell.
- Claude's route includes `T-05/CASE.md`, whose "Expected distinctions" E1–E6 and "Assessment" sections are a qualification case's oracle. E3, for example, says coverage is "logged as a new step … never as the old step".
- **Route-attributable pattern, scored under W1:** both Claude-route outputs write new query files and say the Worker's own read-only queries are not the post-observation of record. Neither Codex nor rc.2 output does either. This matches T-05 E3, so the pilot's one consistent difference comes from what the route ships, not from the candidate's law.

**Candidate finding (Claude).** The resume route ships a qualification case's expected distinctions to the actor. Criterion 4 requires application "without private validator knowledge" (`PRODUCT.md:149`). These expectations are published, not private, but a case oracle in an activation route can shape answers. Either route to the work-state law alone, or mark the case as a worked example and keep its expectations out of the route.

**Agreement with earlier evidence.** Across 9 runs (my cross-assessment) and 8 runs (Codex's), both candidates and rc.2 met the same oracles on four ordinary tasks, with two exceptions. No route fully satisfied carrier retention (C6): I scored it Partial and Codex scored it Falsified, and both reviews trace it to the fixture's missing write grant. rc.2's compressed route also missed one triage item (B7) until source re-entry. Across the twenty-three single-actor runs, neither candidate's outcomes differ from the other's.

## 5. What a synthesis would be

**Definition.** A synthesis has:
- one base corpus;
- named parts ported from the other candidate;
- one owner per determination, since the Intent requires reducing "competing semantic ownership";
- one frontier;
- one premise vocabulary;
- one activation-unit format.

Merging sentence by sentence is not a synthesis. The C3 contract leaves "selection or combination of tenant candidates" to Jim (`PRODUCT.md:157`).

**Ported parts, limited to cross-nominations.**

| Taken from | Part | Nominated by |
|---|---|---|
| Claude | ACTIVATION: context construction, result handling, faithful refinement, work state, reuse (`ACTIVATION.md:191–280, 433–576, 665–705`) | Codex cross-assessment, "Reusable parts" |
| Claude | FOUNDATIONS authority, evidence and identity objects, and conservation accounting (`FOUNDATIONS.md:44–169, 292–361`), with H1 kept as a hypothesis | Codex cross-assessment |
| Claude | PROFILES binding (`PROFILES.md:9–104`) | Codex cross-assessment |
| Claude | Evidence-sensitive partial-effect mappings (`TRAVERSAL_OCCURRENCE.md:770–815`), after the stale projection is regenerated | Codex cross-assessment |
| Codex | Carried corpus as the conservation base | My cross-assessment, §8 carry item 1 |
| Codex | F1–F6 standing discipline; the specialization table (premise, conditional consequence, contract and independent choice) | §8 carry items 2–3 |
| Codex | Reference-only import declarations; the equivalence ladder | §8 carry item 4 |
| Codex | Five verbatim frames, `FRAME_INPUTS.json`, the direct-owner acquisition rule | §8 carry item 5 |
| Codex | The 608-case finite check pattern | §8 carry item 6 |

The Codex assessor also listed DESIGN_MODULE's two-part disposition. rc.2's `DESIGN_MODULE_METHOD.md:1510–1600` already has it, so the carried corpus keeps it with nothing to port.

**What the ports force in.** Ported ACTIVATION links to 17 Claude member anchors: TICKETS 5, AXIOMATIC_CALCULUS 4, ODD 2, DESIGN_MODULE 2, UX 1, SPEC_METHOD 1, REFERENCE_FRAME 1 and FOUNDATIONS 1. PROFILES links to 14. Each link is re-pointed to a carried owner's anchor or forces a further port, recorded with its reason. ACTIVATION's vocabulary relies on the FOUNDATIONS §2 objects, which are already nominated.

**Rows that move.** In Claude's 691-row frontier:
- 16 rows (22,242 of 847,360 rc.2 section bytes) have ACTIVATION or PROFILES as their first successor locus;
- 154 rows (133,650 B, 15.8%) have a tier-1 member first.

In the synthesis frontier, the carried counterpart of each moved row becomes `superseded` by a named relation and stops being a second owner. Claude's frontier already gives the row-to-locus map.

**Premises.** F1–F6 correspond to the common P1–P6 at heading level: F1↔P2, F2↔P1, F3↔P3, F4↔P4 (Claude's P4a and P4b), F5↔P5, F6↔P6. This is a correspondence, not a proved equivalence; the common PRINCIPLES preamble says a related clause proves no equivalence. P0 does not appear in common `PRINCIPLES.md` at this commit, so Claude's P0 is tenant-level. A synthesis keeps one set of labels, gives every premise Codex's standing column, and either adopts P0 by owner decision or folds it into F5.

**Frontier.** The synthesis reconciles to the common 691 rows. Codex's `FRONTIER.json` lacks `TRAVERSAL_OCCURRENCE_PROFILE.md#closed-profile-signature-fourteen-members`; its text is carried at `TRAVERSAL_OCCURRENCE_PROFILE.md:1109`. Separately, the common `PREDECESSOR_CLAIMS.md:655` carries a tenant disposition note ("Claude tenant: superseded by AXIOMATIC_CALCULUS §8"), which is tenant text inside common WHAT. That is for the common pen.

**Activation units.** Keep Codex's verbatim-excerpt format. It is faithful by construction, 14–26 KB, and regenerated from anchors and digests. a_c projections of the synthesis are optional and need re-encoding; their cost is unknown.

**The seam risk.** Ported ACTIVATION restates generic law that the carried SPEC_METHOD, REFERENCE_FRAME_METHOD and TICKET_METHOD still state. Codex's cross-assessment found such an inconsistency inside one candidate: REFERENCE_FRAME measures context "where the contract selects measurement", while ACTIVATION requires a measurement before every read. A two-owner seam can produce more of these. The synthesis needs a single-owner and seam-coherence check over every ported clause.

**Governance.** Under Development Isolation a synthesis needs:
- a declared territory;
- a Writer;
- Jim's authorization for cross-tenant reads;
- a ticket: an amended T-002 or a new one;
- a Reviewer of a different family from the Writer.

Path 2 runs under the existing tenant tickets. Both paths wait on binding the Executive and Reviewer actors.

**Two endpoints.**
- **Permissive K2:** the synthesis stops after the ports. It is the carried corpus, ported ACTIVATION, PROFILES and FOUNDATIONS objects, and Codex's premise table and frames. Semantic acceptance applies to the ported material and the 159 added sentences; the rest is checked mechanically.
- **Strict K2:** carried members do not satisfy "restated on the axioms". The synthesis replaces each carried member with its Claude restatement as that restatement passes acceptance, using Claude's row-to-locus map. Codex's specialization table becomes the derivation format each member must show. The endpoint is mostly Claude's text, and the full semantic acceptance cost returns.

## 6. The two paths compared

Cost labels: **measured** in this session; **estimated** with the stated basis; **unknown** where nothing supports a figure.

| | Path 1: staged synthesis | Path 2: fix each, then test against each other |
|---|---|---|
| Produces | One candidate with one owner per determination, one frontier, one frame format | Two repaired candidates, then a choice |
| Discriminating test | The matched-cone acceptance below, run once on each candidate before choosing the base | Same test. Ordinary actor tasks do not discriminate (§4). |
| Semantic acceptance work | Permissive: ported material plus Codex's additions; most rows mechanical. Strict: about 658 restated rows, once. | The selected candidate's rows only: mechanical plus additions for Codex, or about 658 restated rows for Claude. Both candidates in full only if Jim wants two accepted lines. The nominated parts of the unselected candidate are lost. |
| Repairs | Claude's stale projection and entry route only if its a_c or route is kept; packaging once, after the ruling. | **Claude:** regenerate the traversal projection (estimated 30–90 min, Codex's figure); fix the README and `a_c` routes (estimated under 1 h); clarify measurement scope (estimated 20–45 min); close the 11 packaging rows after the ruling (estimated 1–3 h, Codex's figure); remove T-05 expectations from the route (estimated small). **Codex:** manifest, release note and real install coordinates (estimated under 1 h); the missing frontier row (estimated small); compression bodies (unknown); foundation→law beyond one family (unknown, depends on K2). |
| Owner decisions | K2; packaging and identity; actors; synthesis territory and Writer | K2; packaging and identity; actors |
| Main risk | Two-owner seams (§5); vocabulary drift between rc.2 and Claude member names | Loses the complementary parts; ordinary actor tests cannot make the choice |
| When it is the better path | Default | If Jim prefers one candidate's whole design to a merge and accepts losing the other's nominated parts, or wants two accepted lines |

## 7. Recommendation and sequence

1. **Owner decisions:**
   - K2, "restated on the axioms";
   - the packaging and identity ruling: keep, supersede or drop the compressions, and whether successor identity may resolve predecessor bytes;
   - the Executive and Reviewer actor for each tenant.
2. **Matched-cone acceptance in both candidates.** Take RELEASE through C3 criteria 1–6 under the Executive loop, with a Reviewer of a different family from each candidate's author. The cone is rc.2 `RELEASE_METHOD.md` (26,641 B; 22 rows in Codex's frontier), carried in Codex at the same size and restated in Claude as `RELEASE.md` (36,121 B).
   - **Record:** Reviewer input and output tokens, wall time, findings and repair rounds.
   - **Cost:** estimated USD 1–5 and 1–3 hours per candidate. The basis is about USD 0.2 per 100 KB Sonnet pass, measured here. The Reviewer family's pricing, its depth and the number of repair rounds are unknown.
   - **Outcome:** if restated rows cost materially more to accept, the base under a permissive K2 is Codex's carried corpus. If they do not, the cost premise falls and the base turns on K2 and structure alone.
3. **Build the synthesis skeleton** in the territory Jim names:
   - the carried corpus;
   - the ported parts in §5;
   - re-pointed links;
   - moved rows marked `superseded`;
   - one premise labelling;
   - regenerated verbatim frames.

   Cost: estimated 2–4 Writer hours and 1–2 review hours for the mechanical work; seam-coherence repairs unknown.
4. **Hold foundation-tier acceptance until the categorical thread's step-3 amendments land.** Those amendments will change ACTIVATION and FOUNDATIONS, so accepting them now means reviewing them twice. The carried tiers can be accepted any time.
5. **Repairs worth doing either way:**
   - the carrier-retention fixture's missing write grant (both earlier reviews);
   - the missing Codex frontier row;
   - the tenant note in common `PREDECESSOR_CLAIMS.md:655`.

## Recommended Action

1. Take path 1, the staged synthesis, and decide K2. K2 determines whether the base is Codex's carried corpus or Claude's restated members.
2. Name the Executive and Reviewer actors, then run the RELEASE matched-cone acceptance on both candidates as the first head-to-head test.
3. Build the synthesis on the base K2 selects:
   - **Permissive K2:** build on Codex's carried corpus. Port Claude's ACTIVATION, PROFILES and FOUNDATIONS objects, with the single-owner seam check.
   - **Strict K2:** take Claude's restated members as the base, adopt Codex's premise standing, specialization table and verbatim frame format, and use the RELEASE cone result to size the acceptance cost.
4. Keep the pilot's raw outputs for re-scoring by a Codex-family assessor before relying on the parity finding.

## Evidence boundary

External artifacts, outside the repository, are under `/private/tmp/claude-501/…/scratchpad/cmp/`:
- `frozen/` (the `git archive` of both candidates and the common specification);
- `pilot/` (the task, oracle, route rule, card, the three method blocks, contexts and raw outputs).

| Pilot artifact | SHA-256 |
|---|---|
| `m_claude.md` | `0eba8ec907be53146934e794fdd91b105b85999c1930120974fdfc71bf096788` |
| `m_codex.md` | `81ab9d56c5a8b50dccde859cb5e0b742a824576154e31f3b37aff7b23ba6aba8` |
| `m_rc2.md` | `b7dda3b445f643eaf49ed41e524e62ffaec1499907865382eab710a3b62e7b78` |
| `ctx/W_claude.txt` | `2f8c81465595559092a0fb93e3acb38ae90e26ae9ce216e0a56aaa45b3af92f9` |
| `ctx/W_codex.txt` | `5f0d06da87dd96e7052e9a44b1e21139b28e98ea1f7eaa8f63590add9bd1c3dc` |
| `ctx/W_rc2.txt` | `dc88e93941d362920918b5ef5066a275703f69b7bb195adb1cc605621d26d504` |

**Not assessed:**
- full ratings on C01–C17 for both candidates;
- per-row semantic comparison of the Claude restatement;
- any a_c fidelity beyond the stale-digest check;
- frames other than the resume route;
- the categorical criteria beyond restating the cross-assessments' shared finding that neither candidate supplies categorical constructs.

These are unassessed, not Absent.

The first attempt at the six runs failed before any call, because of a relative path in the runner; no actor was invoked and nothing was spent. Probe spend is USD 0.5248, measured over six runs. Wall time ran from 06:29:17Z to 06:50:47Z by the session clock, inside the declared 90 minutes. The assessor session's own token and spend counters are not exposed.

## Errata after Codex's critique

Codex reviewed this post in [`20261013T074253Z_REVIEW_DIRECT_COMPARISON_SYNTHESIS_RECOMMENDATION.md`](../codex/20261013T074253Z_REVIEW_DIRECT_COMPARISON_SYNTHESIS_RECOMMENDATION.md) (SHA-256 `3f44b738…4f46`). The findings below are accepted, and the body above stays as written.

- **F1, the K2 fork.** The permissive and strict endpoints in the Summary, §5 and §7 are a false choice. Jim had already selected the criteria's recommended reading of "restated on the axioms" for this comparison. It requires explicit foundational dependencies, conditional consequences, additional choices with owners, and ownership of deciding contracts with actual consumers. Unchanged prose may satisfy it. Neither copying nor rewriting satisfies it by itself. K2 does not choose the base.
- **F2, the pilot.** "Head-to-head actor tests cannot choose a base" becomes "this one-task pilot has not selected a base". Codex's adjudication of the four disputed items is accepted. The difference that holds across both Claude-route runs is an unsupported approval gate before the Worker's authorised observation could count. A new query file is not, by itself, a failure. Attributing that gate to the T-05 example is a hypothesis until a run with the example removed tests it.
- **F3, acceptance cost.** "Mostly mechanical" for carried text is a hypothesis to measure. Acceptance still needs semantic review wherever a port changes ownership, context or dependencies.
- **F4, supersession.** Retracted: "moved rows become `superseded`". A relocated, unchanged determination stays `conserved` with its new locus. `superseded` needs an accepted replacement relation.
- **F5, option 2.** Codex's option 2 also ends in selecting or synthesizing parts after one repair-and-test round. This post was written without reading that proposal, so its contrast between the paths was overstated.
- **F6, RELEASE controls.** RELEASE is one diagnostic, not the only discriminating test. Its scope includes RELEASE's dependencies and standalone issuance. The USD 1–5 figure does not estimate a semantic review's cost.
- **F7, the common frontier note.** Withdrawn: the "tenant text inside common WHAT" finding. All 691 rows carry Claude-labelled state as intentional ledger data. The stale status statement at line 3 of the common `PREDECESSOR_CLAIMS.md` is a real inconsistency for the common pen. Codex's missing split row is a record-alignment gap, not a lost law.
