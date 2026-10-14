# SR2: single ownership, coherence and self-consistency of the I3 common specification

**Reviewer**: SR2, a Claude context acting as a cross-family specification Reviewer. It has no repair grant and is not the author of the subject.
**Subject**: `specification_methodology/v3/specification/` frozen at `7c058ed`. The previous accepted basis is `a7eba66`.
**Scope**: review expectations 6 (one owner per rule) and 9 (consistency with the method's own laws), and the handoff's question: are single ownership, the result algebra, workspace recovery, bounded acquisition and human/machine build tenancy consistent?
**Citations**: `file:line` is relative to the subject's `specification/` directory unless prefixed. `inst:` means the installed `v2.5.1-rc.2/standards/`. Ticket citations are read at `7c058ed`.

## Q1. Questions decided in more than one place

| # | Question | Loci | Owner declared? | Consistent? |
|---|---|---|---|---|
| 1 | Single result algebra | PRODUCT:108-119, 279, 326, 334; README:119-140; INTENT:17; conformance:50-53 | Yes. PRODUCT:119: "The precise obligation is the single result algebra requirement" | Content agrees. PRODUCT:334 and conformance:53 restate README:136 item 7 without pointing to it. The decision-outcome scope is ambiguous inside the owner itself (SR2-07). |
| 2 | Single ownership | PRODUCT:15; INTENT:17; README:97-117; conformance:49 | Yes | Agrees, except README:111 item 4 against the constraint-surface fidelity rule (SR2-09). |
| 3 | Standalone successor relationships | PRODUCT:13, 188, 314; README:29-45; GOALS:9 | Yes | Agrees. All loci list the same four relationships. |
| 4 | Reduction | PRODUCT:13, 37-51, 383; README:43, 47-58; INTENT:15; CAPABILITIES:8; conformance:10-16; RFB:45 | Yes (PRODUCT:51) | Content agrees. Its scope (whole candidate) and its acceptance gate (per member) differ (SR2-08). |
| 5 | Constraint surfaces and a_c fidelity | INTENT:23; PRODUCT:49, 51, 86; README:60-70; A_C_DEPENDENCY:60-69; RFB:45; CAPABILITIES:9; conformance:18-22 | Yes (PRODUCT:51, A_C_DEPENDENCY:60) | Agrees on meaning. Two fidelity-evidence lists exist (SR2-20). No tier owner and no acceptance gate (SR2-10). |
| 6 | Workspace, current state and basis | INTENT:35; PRODUCT:55; README:67 (item 4), 80; PRINCIPLES:65; conformance:41-42; PRODUCT:241-249 | Yes, by link. The link's label names no item (SR2-18). | Agrees. README:80 reconciles the workspace as truth surface with the snapshot basis. It also duplicates a local axiom (SR2-19). |
| 7 | Frames and bounded acquisition | INTENT:31; PRODUCT:59, 334, 381, 387; README:72-82; PRINCIPLES:57; RFB:20, 25, 29; conformance:28-30, 38, 40 | Yes (PRODUCT:59) | Agrees, except the fresh-actor conditions against declared acquisition routes (SR2-12). |
| 8 | Configuration | INTENT:33; PRODUCT:61-63, 178-184; README:79; RFB:3; conformance:34-37 | Yes | Agrees. |
| 9 | Build-tenant binding | INTENT:25; PRODUCT:17-23, 44, 88-94, 170; README:84-95; PRINCIPLES:81; conformance:45-48 | Yes (PRODUCT:90) | Agrees on author, actor and operation kind. The C3 tenants' own "applying" has no gate (SR2-15). |
| 10 | Port ownership and dispositions | PRODUCT:258-262, 266-286, 394; README:20-27, 113; RFB:27-28 | Partly. PRODUCT:279 restates README:113 and the disposition rule without citing them. | Agrees. |
| 11 | Common WHAT and its write territory | PRODUCT:168, 205-207, 250-253; RFB:28 | Two definitions | Contradictory (SR2-04). |
| 12 | Merge and acceptance | PRODUCT:197, 254-255; GOALS:11 | PRODUCT | Contradicted by the recorded state (SR2-05). |
| 13 | Acceptance criteria and their standing | PRODUCT:376-383; GOALS:17-18, 31; RFB:28-29; conformance:3 | Yes (PRODUCT) | GOALS' status claim does not match the current text (SR2-14). |
| 14 | Member accept condition | PRODUCT:195; RFB:28; inst:STDO_REFERENCE_FRAME_BASELINE.md:1373, 1414 | PRODUCT | Contradictory (SR2-02). |
| 15 | Reviewer independence | PRODUCT:176, 182, 385; README:79; conformance:31; RFB:24, 28 | Partly | "Author" is undefined (SR2-06). |
| 16 | Tier of ownership | PRODUCT:67-73, 322-330; README:104-109, 115 | Two rules | In tension (SR2-11). |
| 17 | Checkpoint state, frozen input | PRODUCT:292-297; GOALS:3, 11, 13-25; T-001 | Conflicting owner declarations | Values agree. Owners conflict (SR2-17). |
| 18 | Capability obligations | CAPABILITIES:3, 21; PRODUCT:125; README:6; GOALS:17 | Unclear | Contradictory (SR2-13). |
| 19 | Local axioms | README:12; PRODUCT:106; `stdo_3.json` `local_constitution.axioms` (2 entries) | Yes | Consistent. |
| 20 | Successor-relation acceptance | README:21, 27; PRODUCT:279, 315, 380, 190-197 | **None** | Circular (SR2-01). |

## Q2. Contradictions

The following pairs cannot both hold:

- **SR2-01.** A superseded row must name an *accepted* relation before review can pass. That relation stays pending until accepted, but no locus grants anyone acceptance of it, and member `accept` requires the row to be disposed first. The installed UP-020 proxy limit (inst:SPEC_METHOD.md:1566-1568) excludes the Executive from accepting a change of meaning.
- **SR2-02.** PRODUCT:195 accepts on "a closed result of `satisfied`". RFB:28 returns "one closed Reference Frame Method result per acceptance criterion". The installed baseline requires "one closed evaluation" (inst:...BASELINE.md:1373), and PRODUCT:310 makes the baseline govern.
- **SR2-04.** PRODUCT:168 defines the common WHAT as `specification/`. PRODUCT:206 defines it as `specification/`, the Product Definition and `.ai-workspace/`, written by the pen. PRODUCT:251-252 and RFB:28 have reviewers write in `.ai-workspace/comments/<reviewer>/`.
- **SR2-05.** PRODUCT:254-255 merges a tenant branch "only on the product owner's acceptance". GOALS:11 records "neither its merge nor later construction constitutes acceptance" for `a9adce2`.
- **SR2-13.** CAPABILITIES:3 says the reconstruction "must provide the capabilities". CAPABILITIES:21 and PRODUCT:125 make obligations depend on a capability being selected, and no capability selection is recorded (GOALS:17 records only criteria, audiences and tasks).
- **SR2-14.** GOALS:31 says the "per-member acceptance criteria (2026-10-12)" were decided. The diff `a7eba66→7c058ed` rewrites criteria 3, 4 and 6 (PRODUCT:380-383), and GOALS has no revision-record entry for iteration 3.
- **Conformance demands more than its owner.** Conformance:26-27 require each planned judgement to be "authenticated against its producer, subject, basis and supporting evidence". No common requirement owns authentication: "authent" occurs only in conformance and in GOALS:51. The obligation is defensible as conserved predecessor law (inst:REFERENCE_FRAME_METHOD.md, Result Conjunction, "Missing, wrong-subject ... remain unresolved"), but no locus cites it (SR2-25).
- **No contradiction found in these places:** PRODUCT requirement summaries against their owners (items 1-10 above). The local axioms. INTENT against PRODUCT.

## Q3. Coherence of the five areas

**Result algebra.**
- The owner, PRODUCT:110 → README:126, and the conformance rows agree on the core rules: no raising of standing, the predicate travels with the value, and recorded data is separate from judgment.
- The one internal tension is SR2-07. README:127 says "No evaluation or decision outcome exists outside the core". README:134 says "assessment and acceptance remain separate results", and README:138 says "Assessing a condition and exercising authority ... remain distinct". A builder cannot tell whether `accept` and `reject` are core values or authorised actions that cite core results. Two compliant candidates can therefore diverge on the core's value set.

**Workspace recovery.** This area is coherent.
- README:80 binds three things: the observed subject to its contract basis ("including committed snapshots"), drift to re-entry ("does not silently rebind the basis"), and resumption to current material state.
- This agrees with INTENT:35, PRINCIPLES:65, conformance:41-42, and Development Isolation's snapshot inputs (PRODUCT:241-249).
- Defects are minor: the label "current-state and basis rule" (PRODUCT:55) names no item, "workspace" is never defined, and README:80 copies the local sparse-file rule (SR2-18, SR2-19).

**Bounded acquisition.**
- Context fit and attention adequacy are separated consistently: README:78, PRODUCT:334, 381 and 387, and conformance:29.
- Tension 1: criterion 4's fresh actor has "only that frame and the subject" (PRODUCT:381) and starts "outside any repository" (RFB:29). Frames may instead carry "declared acquisition routes" (PRODUCT:334, README:67), and known relations "enter through declared authoritative inputs" (README:77). Whether the actual-use test permits acquisition is undetermined (SR2-12).
- Tension 2: frames are "generated from the a_c form of the members" (PRODUCT:334), so they are projections. README:111 treats a frame's content as a "copy" that is defective if it "differs" and is repaired "by copying again". That cannot govern a compressed projection, which README:68 judges by "the same owned determination for their declared use" with a declared adequacy bound (SR2-09).
- The Executive's "never the candidate text" (RFB:25) conflicts with a `candidate_ready` whose "evidence of the change" is "the restated text" (PRODUCT:366) (SR2-21).

**Human/machine build tenancy.** This area is coherent within the requirements.
- The chain requirements calculus → computational calculus → execution environment is defined once (PRODUCT:92) and bound once (README:88).
- Author, actor and operation kind are kept distinct at PRODUCT:44 and 94, README:89, and conformance:46-47.
- The pillar row at PRODUCT:47 and PRINCIPLES:81 agree.
- Gaps:
  - PRODUCT:170 obliges the C3 tenants themselves to be "applying the build-tenant binding requirement", but no criterion checks it and its content for a document candidate is not stated (SR2-15).
  - The three accounts are "proposes[d]" at PRODUCT:17 but asserted at INTENT:21 and PRODUCT:94.
  - INTENT:13 speaks of "algebraic and computational accounts", which is not the algorithmic/informational/computational triple (SR2-24).

**Single ownership against the new requirements.**
- Reduction's member-boundary freedom fits the many-to-many disposition mapping (README:56; PRODUCT:188), and the profiles row was correctly relaxed from "restates its own predecessor member in full" (base) to "shared owners" (PRODUCT:328).
- Three tensions remain:
  1. PRODUCT:67 says the tier obligations "bind the predecessor coverage each owes", and README:104 says "The owning tier follows the tier obligations". The "Receives" column routes whole predecessor members by tier. README:105-109 and 115 assign ownership by generality. When a foundations-routed member contains profile-only law, or the profile-routed baseline contains generic law, the two rules disagree. PRODUCT:67 also says "three tiers", while the tier table and README:104-109 have five owners (SR2-11).
  2. Reduction is a whole-candidate property ("whole set of material deciding rules", README:40; "across the predecessor and the candidate", README:52; "actual deciding paths", README:57). Its only gate is per member (criterion 6, PRODUCT:383), and Closure (PRODUCT:389) has no candidate-level check (SR2-08).
  3. The constraint-surface requirement has no tier owner in PRODUCT:322-330. It is absent from the C3 Outcome (PRODUCT:312-316), though GOAL-002 requires "usable constraint surfaces in prose and a_c" (GOALS:9). Its fidelity evidence (README:69) is attached to no acceptance criterion (SR2-10).

## Q4. The specification's own consistency with its laws

The specification's own value sets:

| Value set | Locus | Mapped into a result algebra? |
|---|---|---|
| `supported`, `contradicted`, `unresolved` per clause | RFB:24 (Common definition frame) | **No.** "unresolved" merges indeterminate, out_of_frame, invalid_basis and not-performed. This breaches the installed RF-012 extension rule ("preserving explicit indeterminate, out-of-frame, and invalid-basis pressure", inst:REFERENCE_FRAME_METHOD.md:421-422) and README:131 and 136 by analogy. This is the frame under which common changes are reviewed (SR2-03). |
| semantic conservation / demonstrated reduction / mere relocation | RFB:45 | Not stated whether this is data or result. README:138 requires the owner to say how a decision using it returns through the core (SR2-16). |
| `candidate_ready`, `refused`, `incomplete`, `re_entry_requested` | PRODUCT:365-369; RFB:27 | Yes, through the installed baseline (inst:...BASELINE.md:475-487, 1321), which PRODUCT:310 makes govern. The subject omits the accompanying RF result that the baseline requires (inst:...:638) (SR2-16, minor). |
| `accept`, `local_repair`, `re_enter`, `reject` | PRODUCT:192-195 | Installed UP-020 law. Whether these are core values depends on SR2-07. |
| `satisfied` ... `invalid_basis` | PRODUCT:195; RFB:28 | Yes. This is the installed family, named explicitly. |
| "GO", "no further changes required", "four changes required", "changes requested" | GOALS:15, 19, 41, 47, 51 | No. These record review judgements, which PRODUCT:113 says are stated in the core. Mostly history, but GOALS:15 and 19 are current state cells (SR2-16). |
| CLOSED, SELECTED, NOT_SELECTED | GOALS:13-21 | Lifecycle data. Only SELECTED is defined (GOALS:3) (SR2-16). |

On authority and acceptance:
- **SR2-01.** The acceptance of supersession relations has no owner.
- **SR2-02.** The member accept rule has no declared conjunction. README:135 ("Conjunction ... defined once") and the installed Result Conjunction ("A declared decision rule consumes closed frame results") both require one.
- **SR2-05.** The recorded merge contradicts the merge-implies-acceptance rule.
- **SR2-06.** "Author" is undefined for independence. Conformance:31 rejects "An author opens a fresh context to review its own candidate", and README:79 says "a fresh context alone does not satisfy independence". Meanwhile GOALS:51 records "Two fresh same-family source reviews", and the I3 consolidation review (codex/20261014T011752Z, lines 3-13) is a "fresh nonauthor Reviewer" activated by the pen's recorder under a declared same-family exception. Whether such an activation is "the author" cannot be decided from the text. This is a definitional gap, not a process verdict.
- **SR2-04.** Reviewers write into territory that PRODUCT:206 reserves to the pen.

## Findings

| ID | Severity | Claim | Evidence | Smallest correction |
|---|---|---|---|---|
| SR2-01 | blocking | No locus grants acceptance of a successor relation, yet member acceptance presupposes it. A reviewer cannot return `satisfied` on criterion 3 for any `superseded` row. | PRODUCT:380 "Every `superseded` row names the accepted successor relation ... Proposed replacements remain pending until accepted"; PRODUCT:195 `accept` "only when ... `satisfied` and every row of the member's frontier cone is disposed"; README:21, 27; PRODUCT:197 lists the owner's reservations without relations; PRODUCT:190-195 grants dispositions of restatements only. The obvious owner is excluded by governing law. inst:SPEC_METHOD.md:1566-1568 says a proxy "may accept preservation ... It cannot change Product meaning, requirements, governing authority, or accepted design". A supersession replaces a predecessor determination, which is not preservation, and PRODUCT:310 makes installed law govern. So the Executive's `accept` cannot lawfully carry relation acceptance. | Reserve acceptance of each successor relation to the product owner, or to a stated delegation that holds that authority, recorded before member `accept`. Criterion 3 then checks that the relation is accepted, and the Reviewer evaluates the proposed relation beforehand. Add the reservation to PRODUCT:197. |
| SR2-02 | material | The accept rule needs one `satisfied`, while the Reviewer returns six per-criterion results. No conjunction is declared, and the per-criterion return departs from the governing baseline. | PRODUCT:195 "a closed result of `satisfied`"; RFB:28 "one closed Reference Frame Method result per acceptance criterion"; inst:...BASELINE.md:1373 "returns one closed evaluation", :1414 "applies any declared result conjunction"; README:135; PRODUCT:310 | PRODUCT:195: "returns `satisfied` on every applicable criterion; any other result on a criterion withholds `accept`; an inapplicable criterion states its bounded reason". |
| SR2-03 | material | The common-definition frame returns an unmapped three-value set that collapses distinct results. | RFB:24 "a judgement of supported, contradicted or unresolved"; inst:REFERENCE_FRAME_METHOD.md:421-422; README:131 | RFB:24: "Returns one closed Reference Frame Method result per affected clause." |
| SR2-04 | material | The common WHAT and its write territory are defined twice, and the definitions contradict each other. Reviewer writes are forbidden by one locus and required by another. | PRODUCT:168 "one common WHAT: the specification in `specification/`"; PRODUCT:206-207 "The common WHAT (`specification/`, the Product Definition, `.ai-workspace/`) is written on `main` by the common pen"; PRODUCT:251-252; RFB:28 | PRODUCT:206-207: "The common WHAT (`specification/`, the Product Definition) and the tickets are written on `main` by the common pen; reviews are written as Review states." |
| SR2-05 | material | The merge rule makes a merge imply acceptance, but the recorded merge has no acceptance. Neither locus names the variance. | PRODUCT:254-255 "merges to `main` only on the product owner's acceptance"; GOALS:11 "neither its merge nor later construction constitutes acceptance"; work list CR5-05 "owner-directed historical variance" | Add to Merge: "An owner-directed visibility merge is recorded as such and supplies no acceptance." Alternatively, name `a9adce2` as an owner variance in GOALS:11. |
| SR2-06 | material | "Author" is undefined for independence, so a reviewer cannot decide whether a fresh same-family activation directed by the authoring session satisfies "independent of their author". | PRODUCT:176, 385; README:79; conformance:31; GOALS:51; codex/20261014T011752Z:3-13 | README:79 item 4: define the author of a subject as the activations that produced it and any actor that directed them or shares their working context. State whether common-definition review admits a same-family nonauthor. |
| SR2-07 | material | The result algebra's scope over decisions is ambiguous, so builders can diverge on the core's value set. | README:127 "No evaluation or decision outcome exists outside the core"; README:134; README:138 "Assessing a condition and exercising authority ... remain distinct"; PRODUCT:119. The divergence has already occurred: the I3 consolidation review (codex/20261014T011752Z:17-21) reads the subject as requiring "every evaluation or decision outcome to have an owner-defined, predicate-sensitive core mapping", which is the decisions-in-core reading that README:134 and 138 do not settle. | README:127: "No evaluation outcome exists outside the core; a decision names the closed core results it consumes and the authority it exercises." The opposite choice also works, but one must be stated. |
| SR2-08 | material | Reduction and foundation-to-law accounting are whole-candidate obligations with only a per-member gate. Closure has no candidate-level check. | README:40, 52, 57; PRODUCT:376 "for one member restatement", 383, 389 | Closure (PRODUCT:389): add "and an independent candidate-level review of the standalone and reduction relationships returns `satisfied`". |
| SR2-09 | material | The frame "copy" rule conflicts with projection fidelity for a_c-generated frames. | README:111 "A copy that differs from its owner is a conformance defect, repaired by copying again"; README:68; PRODUCT:334 "generated from the a_c form" | README:111: "A frame's copy or projection of a clause names its owning locus; a verbatim copy that differs is repaired by copying again; a projection is judged under constraint-surface item 5." |
| SR2-10 | material | Constraint surfaces have no tier owner and no acceptance gate. Their required fidelity evidence attaches to no criterion. | PRODUCT:322-330 (absent); PRODUCT:312-316 (Outcome omits a_c); GOALS:9; PRODUCT:25; README:69 "Required fidelity evidence"; A_C_DEPENDENCY:62 "selected" | Add the candidate's a_c interpretation to the C3 Outcome. Name the criterion that takes the README:69 evidence. Add constraint-surface law to the foundations "Owes" cell. |
| SR2-11 | material | Tier routing by predecessor member conflicts with ownership by generality. "Three tiers" conflicts with the five owners. | PRODUCT:67 "bind the predecessor coverage each owes"; PRODUCT:326-328; README:104 "The owning tier follows the tier obligations"; README:105-109, 115; PRODUCT:67-73 | PRODUCT:67: "...assign which tier accounts for each predecessor member; each determination's owning locus follows the single ownership requirement and may lie in another tier." Call guides and packaging owners, not tiers. |
| SR2-12 | material | Criterion 4's fresh-actor conditions exclude the declared acquisition routes that frames may rely on. | PRODUCT:381 "given only that frame and the subject"; PRODUCT:342; RFB:29 "outside any repository"; PRODUCT:334; README:67, 77 | PRODUCT:381: "given only that frame, the subject and the authoritative inputs the frame declares". |
| SR2-13 | material | The standing of CAPABILITIES is contradictory, so a reviewer cannot tell whether its bullets are acceptance conditions. | CAPABILITIES:3 "must provide"; CAPABILITIES:21 "Every selected capability"; PRODUCT:125; README:6; GOALS:17 | CAPABILITIES:3: state which capabilities are C3 obligations and through which criterion, or restore "questions until selected". |
| SR2-14 | material | GOALS presents the current acceptance criteria as decided on 2026-10-12, but criteria 3, 4 and 6 were rewritten afterwards. A reviewer cannot tell whether the current text carries owner authority. | GOALS:17, 31; diff `a7eba66→7c058ed` at PRODUCT:380-383; no I3 entry in GOALS:37-57 | GOALS:31: "...criteria (2026-10-12; amended at <commits>; amendments await owner sign-off)". Add an I3 revision entry. |
| SR2-15 | material | The C3 tenants must be "applying" the binding requirement, but its content for a document candidate and its gate are unstated. | PRODUCT:170; README:86, 88; conformance:45; PRODUCT:376-383 (no criterion) | PRODUCT:170: state whether the tenant declares its own computational calculus and execution binding, and which criterion checks it, or say that "applying" means the candidate's Spec Method states it. |
| SR2-16 | minor | The specification's own construction vocabularies are uncited or unmapped: Writer variants lack their RF result, GOALS uses verdict words, RFB:45 has a classification, and only SELECTED is defined. | PRODUCT:365-369; RFB:27, 45; GOALS:3, 15, 19, 41, 47, 51; inst:...BASELINE.md:638 | One sentence in the C3 contract: construction results use the installed result family and the baseline's work-result mapping. Write GOALS verdicts as RF results or mark them as quotations. |
| SR2-17 | minor | Conflicting owner declarations for checkpoint state and for the frozen input. | PRODUCT:297 "state ... is in GOALS"; GOALS:3; GOALS:23 "T-001 owns checkpoint state"; GOALS:11 "T-001 owns ... frozen input" against GOALS:25 and the work list ("recorded in T-002's snapshot") | Name one owner for each. |
| SR2-18 | minor | The link label names no rule, and "workspace" is undefined. | PRODUCT:55 "current-state and basis rule"; README:80; INTENT:35 | Name README:80 item 5 and define workspace at PRODUCT:55. |
| SR2-19 | minor | A generic requirement repeats a local git rule. | README:80 "an absent sparse file is not evidence of absence"; PRODUCT:244-245 | README:80: "absence from a partial view is not evidence of absence". |
| SR2-20 | minor | Two a_c fidelity-evidence lists do not reference each other. | README:69; A_C_DEPENDENCY:62-69 | Have A_C_DEPENDENCY:62 cite README:69 as the owner of the case comparison. |
| SR2-21 | minor | The Executive may not read candidate text, but the result it evaluates is the restated text. | RFB:25 "never the candidate text"; PRODUCT:366, 370 | PRODUCT:366: "evidence identifying the restated text". |
| SR2-22 | minor | The frontier source is ambiguous. The common file shows Claude's state as "accepted" while GOALS says acceptances were reopened. | PRODUCT:320 "every `unresolved` row of PREDECESSOR_CLAIMS.md for that tenant"; PREDECESSOR_CLAIMS:9, 11, 16; GOALS:18 | PRODUCT:320: "...in the tenant's frontier record". PREDECESSOR_CLAIMS:9: "reported state". |
| SR2-23 | minor | C3 closure depends on packaging rows whose owner decision is scheduled only before the RC cut. | PRODUCT:330, 389, 396 | State whether packaging rows are inside C3 closure. |
| SR2-24 | minor | The standing and naming of the three accounts drift. | PRODUCT:17 "proposes"; INTENT:13 "algebraic and computational accounts"; INTENT:21; PRODUCT:94 | Use one standing and the algorithmic/informational/computational names. |
| SR2-25 | minor | The conformance authentication rows have no cited owner. | conformance:26-27; no "authent" in requirements | Cite the owning requirement or the conserved predecessor claim. |

Counts: 1 blocking, 14 material, 10 minor.

## What holds

- Every new requirement has a declared owner, and the owner's summaries in PRODUCT, INTENT, CAPABILITIES and RFB restate it faithfully. These cover the result algebra, reduction, constraint surfaces, frames, binding and single ownership. Nothing restated in PRODUCT is narrower or wider than its owner.
- Workspace recovery is reconciled with snapshot bases and drift (README:80; PRODUCT:241-249).
- The build-tenant chain and its distinctions between author, actor and operation kind are consistent across six loci.
- Reduction's freedom over boundaries agrees with the many-to-many disposition mapping (PRODUCT:188). The profiles row no longer forces full restatement.
- "Baseline governs" (PRODUCT:310) is precedence between products, not a rule between loci, so it does not breach README:114.
- Writer results reach RF-012 through the installed mapping. The Reviewer's result family is named (PRODUCT:195).
- The local axioms agree (README:12; `stdo_3.json`, two axioms; PRODUCT:106).
- The port-review independence conflict is kept as an open owner decision (PRODUCT:394).
- The approximation rules agree (README:68 with README:149).

## Limits

- The review is read-only over the frozen subject.
- PREDECESSOR_CLAIMS was read only for its header and a sample of rows.
- Tickets were read at `7c058ed` only to test GOALS' claims.
- Tenant candidates were not read.
- The installed release was read only at RF-012, AC-007, UP-015, UP-020, RF Result Conjunction and the baseline's Worker, Reviewer and Executive steps.
- Expectations 1-5, 7-8 and 10-13 were not assessed, except where they bear on ownership.
- Independence: SR2 is a Claude context, and the Claude build tenant is governed by this subject.
- Severity is judged by whether a builder can construct, and a reviewer can accept, against the text.
