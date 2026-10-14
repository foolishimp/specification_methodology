# REVIEW: Current v3 specification

**Author**: Dimitar Popov
**Date**: 2026-10-13T17:04:00Z
**Addresses**: Current `specification/` at `c0beefd6d5be20f350580dd6b4afeb8fa30c1261`, substantive configuration amendment at `be784145cf77fcc1551dcbd666dad57188fa21fb`; original review at `df4816d402966d7b27d047c3f8335a47b0d1c25f`; adjoining Product Definition entry route
**Status**: Open
**Updated**: 2026-10-13T17:34:55Z

## Current assessment — c0beefd

**No new finding in the context, attention and derived-configuration changes. F1 and F2 remain open at moderate severity.** Correct those two inherited locations before freezing the next C3 input. The new organising account requires no further source amendment on the evidence inspected here.

This re-review covers the changes since `df4816d`: the context and attention amendment at `c316b49`, its status record, the configuration amendment at `be78414`, and the subsequent GOALS status change at `c0beefd`. Source acquisition used the named commits. The last commit arrived during review and changes only the review-status row within `specification/`; that delta was inspected. The other activation's new review post was not used as evidence.

### Findings still open

- **F1 — Moderate:** [PRODUCT](../../../specification/PRODUCT.md#c3-construction-contract), now line 297, still requires a successor locus for every disposition. Acceptance criteria 1 and 3, now lines 360–362, correctly distinguish conserved/superseded claims from removed/inapplicable claims. The minimal correction and counterexample in the original finding below remain applicable.
- **F2 — Moderate, adjoining route:** [stdo_3.json](../../../stdo_3.json), line 134, is unchanged and still declares the absent `build_tenants/codex/standards/` directory. Git objects at `c0beefd` confirm that `build_tenants/codex/successor/standards/` exists and the declared directory does not. Preserve the separate a_c route when correcting the locator.

### What the new source establishes

[Construction And Context Management](../../../specification/PRODUCT.md#construction-and-context-management), lines 37–45, explains bounded transitions and configuration choices. The [frame requirement](../../../specification/requirements/README.md#bounded-transitions-and-reference-frames), lines 48–54, owns their constraints. The account does not claim that finite capacity alone proves purpose, authority, independent assurance or a unique coordination structure. P5's standing expressly retains those additional premises.

The source admits different allocations of responsibilities, information and actors. It distinguishes functional decomposition, communication, authority and evaluation dependency. That is consistent with installed [RF-009](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-009-no-assumed-hierarchy), lines 381–390. The source project's Executive/Writer/Reviewer arrangement is explicitly its selected construction configuration: [Product](../../../specification/PRODUCT.md#construction-authority), lines 160–166, and [frame basis](../../../specification/REFERENCE_FRAME_BASIS.md), lines 3 and 20–29. Generic flexibility does not change that admitted construction process.

The Executive has a stated purpose for its bounded view: retaining the longer-term outcome and deciding what follows from sufficient results. It can request another bounded evaluation when information is missing. Smallness alone does not establish sufficiency, and no optimality theorem is claimed.

### Desk checks of the changed contracts

These are source-level counterexample checks, not executed actor trials.

| Case | Current rule and result of inspection |
|---|---|
| A directly authorised task already fits one sufficient frame | Requirement 4 permits one frame; conformance line 20 permits direct activation subject to separately required assessment. No universal decomposition or fixed actor sequence follows. |
| Work requires more material than one actor can use | Requirement 2 retains material dependencies and allows refinement, a capable actor or a truthful stop. Small context cannot justify dropping an obligation. |
| A frame fits its byte budget but obscures a dependency | Requirement 3 and C3 criterion 4 separate representation size from actual task adequacy. Evidence is bounded to the tested task, actor and conditions; it supplies no universal attention metric. |
| Peer coordination has no central Executive | Requirement 4 and conformance line 21 permit the configuration where the governing task, authority and assurance conditions hold. This does not waive the local C3 arrangement. |
| Actors redistribute work after an uncertain effect | Requirement 4 preserves obligations, effects, dependencies and admitted authority. Requirement 5 requires enough resolution for the next dependent action under the applicable recovery contract. Reconfiguration supplies no new effect grant and does not justify a blind repeat or universal reset. |
| A fresh context is used to call self-review independent | Requirement 4 retains authorship and evidence conditions. Conformance line 17 explicitly rejects the shortcut. Sharing relevant common sources is still permitted. |
| A compact worker result omits a delivery blocker | Product line 160 and conformance line 24 require sufficient information for the next decision. The coordinator obtains further bounded evaluation rather than treating the omission as favourable evidence. |
| A bounded view omits some frontier items | Product line 302, frame-basis line 25 and conformance line 18 preserve excluded work in the frontier. Attention selection creates no disposition. |
| Discovery enlarges the work or an owner changes the destination | Requirement 1, Product line 39 and conformance line 19 preserve uncertainty and re-entry. Counts alone do not prove progress; an easier new destination does not prove the old one was reached. |
| A configuration is called optimal merely because it is familiar or self-organised | Product line 45 and conformance line 23 require the objectives, constraints, comparison scope and supporting evidence. Adequacy is not promoted into optimality. |

The new wording preserves the previous build-tenant binding, single ownership and result requirements, standalone successor relationship and categorical demonstration standard. The statement about independently sufficient assessment was removed from Intent's resumption paragraph, but the obligation remains explicit in the new frame requirement, Product's Reviewer binding, C3 independence and the frame basis. I found no loss of that condition across the changed consumers.

### Verification and next action

The installed rc.2 verification again returned valid against the exact manifest. All 169 parsed Markdown links across the frozen specification resolve. Whitespace checks on the intervening specification changes pass. A_C_DEPENDENCY, CAPABILITIES, PREDECESSOR_CLAIMS and the Product Definition are byte-identical to the previous review subject; existing tenant conservation assertions were not requalified. No implementation or paid actor trial was run, and this review establishes no configuration's efficiency, attention performance or categorical theorem.

Keep the new configuration account. Apply the already described F1/F2 corrections, review those bounded deltas, and use the existing owner sign-off and admission sequence. No additional role inventory, universal coordination mechanism or approval gate is recommended.

Publication activation: Reviewer inspection is complete. This activation enters the bounded review Writer role solely to update this existing Open post, as the installed POSTING_GUIDE prescribes for new evidence in the same discussion. The original Date and original assessment body are retained. The pre-update post SHA-256 was `5a4db767b7ff9a5dc5fbda27688c38e53def0e48b3949dda2723370ff94954dc`. The grant includes no specification, ticket, candidate or Git mutation. New paid probe spend remains USD 0.

---

## Original assessment — df4816d

The body below records the first assessment and its then-current line references. Its reviewed subject is `df4816d`, not the later cut above.

## Summary

The current specification gives the tenants a coherent common contract. The new build-tenant binding correctly connects requirements to a computational calculus and then to concrete execution, including human and mixed processes. It preserves required meaning, authority and independence across those choices. It does not confuse formal representation with an executor or structural validation with execution conformance.

Two bounded corrections remain before the next C3 input snapshot: the C3 outcome requires a successor locus for dispositions that need no surviving claim, and the Product Definition directs Codex to a nonexistent implementation directory. Both issues predate the latest binding amendment. Neither requires another architectural rewrite or a new decision about the tenants' bases.

**Verdict: changes required at those two locations; the substantive direction and new binding requirement are supported by this source review.** This is a specification judgement, not tenant acceptance or evidence that the categorical capability has been demonstrated.

## Subject and review boundary

Assessor: Codex, GPT-6 family, through the Codex client. This is an informed same-family review: the thread previously assessed the candidates and their comparison, and Codex holds the common pen. Prior conclusions route inspection only. Historical memory supplied workflow guidance and is excluded from the evidence. No fresh actor or independent delegate was run; this post supplies no C3 member-acceptance result.

The review began on a clean working tree at `832efd3`. While it was in progress, another activation committed `df4816d`, recording its own review. The only change within `specification/` was the review-status row in GOALS. I inspected that delta and bound this review to `df4816d`. I did not use the concurrently written review as evidence.

The ten specification files total 295,461 bytes at that subject. Their Git subtree is `32fa4e4b85209da697338f432f3829cb10e72c57`; every working-tree file matched its committed blob at final acquisition. The substantive requirements, Product, Intent and conformance text are unchanged between the two commits.

Coverage: the nine definition, requirement, conformance and frame-basis documents received source review. PREDECESSOR_CLAIMS received an inventory, status and delta review: its existing tenant conservation assertions were not requalified individually. The installed builder, Product Definition, local instructions, common tenant entry and applicable construction-ticket seams supplied authority and routing context. Tenant implementation bodies were not re-reviewed.

The installed builder verified valid against manifest `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`. New paid probe spend: USD 0. The client does not expose this session's own token or cost counters.

## Findings

### F1 — Moderate: the C3 outcome requires a locus for removed and inapplicable claims

Source: [PRODUCT, C3 outcome](../../../specification/PRODUCT.md#c3-construction-contract), line 283, compared with the same section's acceptance criteria at lines 346–348 and the [successor disposition requirement](../../../specification/requirements/README.md#successor-disposition-requirement), lines 18–25.

The outcome requires every predecessor row to have a disposition **and** a successor locus, defined as the section of the candidate where the claim now lives. Acceptance criterion 1 requires that locus only for `conserved` and `superseded` rows. Criterion 3 instead requires the owner's decision and reason for an intentional removal, or a bounded reason for non-applicability. Those are materially different contracts.

Counterexample: a fact that applies only to the predecessor release is disposed `not applicable`, with an adequate bounded reason and no surviving successor determination. It can meet criteria 1 and 3 while failing the unqualified outcome sentence. Likewise, an authorised removal need not leave the removed claim alive in the candidate. An actor enforcing the outcome can reject a lawful disposition or create an artificial successor location merely to fill the field. A location recording a removal decision is not the location where the removed claim now lives.

The installed [STDO-UP-015](stdo://releases/v2.5.1-rc.2/standards/RELEASE_METHOD.md#successor-baseline-conservation-stdo-up-015), lines 504–516, and the common requirement support the differentiated rule. The detailed acceptance criteria already express it correctly.

Smallest correction: qualify the outcome sentence so every row has one disposition, while conserved and superseded rows also have resolving successor loci; removed and inapplicable rows carry the evidence required by criterion 3. No change to the four dispositions or their authority is needed.

Smallest verification: desk-check one row of each disposition against both the outcome and the acceptance criteria. All four should impose the same obligations in both places. The predecessor release-note row at [PREDECESSOR_CLAIMS](../../../specification/requirements/PREDECESSOR_CLAIMS.md), line 863, is an existing non-applicability example to use as a test subject, without accepting its tenant assertion through this review.

### F2 — Moderate, adjoining entry route: the declared Codex implementation path is absent

Source: [stdo_3.json](../../../stdo_3.json), lines 128–135, consumed through [PRODUCT, Product Identity And Lineage](../../../specification/PRODUCT.md#product-identity-and-lineage), line 76, and the source-project entry route.

The canonical tenant registry declares `./build_tenants/codex/standards/` as the Codex implementation directory. That directory does not exist at the reviewed commit. The method bodies are under `./build_tenants/codex/successor/standards/`. Both facts were checked against Git objects at `df4816d`, not inferred from a sparse checkout. The declared Codex `a_c/` directory exists; the Claude implementation routes also exist.

The installed [WHAT, HOW, And Work Carriers](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#what-how-and-work-carriers), lines 796–815, makes this collection the canonical locator for tenant design and implementation. An actor following it cannot acquire the Codex prose through the declared implementation route and must rediscover the layout or report missing material. The common specification now requires the candidate to state and apply its execution binding, so an accurate implementation locator is part of making that contract usable.

`stdo status --definition stdo_3.json --verify` returns valid. That check verifies the definition and installed basis; this observation shows it is insufficient evidence that every declared implementation location exists.

Smallest correction: update the existing Codex implementation locator to the actual successor location, at least `./build_tenants/codex/successor/standards/`, while retaining its separate a_c route. The tenant does not need a new wrapper directory or a layout rewrite.

Smallest verification: resolve every `how.build_tenants` root, design and implementation locator against the same frozen input commit. Then enter the Codex method through its declared route. This is an entry defect adjacent to `specification/`, not a defect introduced by the new computational-binding text.

## Substantive checks

| Contract | Source and judgement |
|---|---|
| Requirements to computation to execution | [Product](../../../specification/PRODUCT.md#build-tenant-binding), lines 58–64, and the [binding requirement](../../../specification/requirements/README.md#build-tenant-binding-requirement), lines 44–55, give the tenant responsibility for operations, composition, relevant effects, resource measures, assumptions and evidence. They permit a shared calculus where its laws hold across different bindings. They require these relations in existing design and realisation surfaces rather than prescribing another artifact family. Supported. |
| Human and mixed execution | Binding items 2–4 preserve required human decisions, independence, failure and recovery. Author, actor and operation kind remain distinct. [Conformance](../../../specification/conformance/README.md), lines 21–24, rejects replacing a required human decision with an output-equivalent automated result and rejects collapsing required independent assessments for speed. It also refuses to treat a structurally valid model as execution proof. Supported. |
| Restatement on foundations | The [standalone requirement](../../../specification/requirements/README.md#standalone-successor-requirement), lines 29–42, requires premises, consequences, owned domain choices, actual use by consumers and successor-owned determinations. Both Product summaries point to that requirement. Unchanged prose is allowed; neither copying nor rewriting proves the relationships. The earlier K2 fork is unnecessary. Supported. |
| Ownership and results | [Single ownership](../../../specification/requirements/README.md#single-ownership-requirement), lines 61–74, permits attributed frame copies and faithful refinements while rejecting competing owners. [The result requirement](../../../specification/requirements/README.md#single-result-algebra-requirement), lines 85–95, retains the predicate and original outcome, distinguishes unavailable assessment from undecidable evidence, preserves unknown effect completion, and separates candidate production from fitness and acceptance. Supported as a contract the tenants must realise; no particular tenant algebra is accepted here. |
| Categorical standing | [Product](../../../specification/PRODUCT.md#categorical-construction), lines 93–120, and [the demonstration standard](../../../specification/requirements/README.md#categorical-demonstration-standard), lines 103–116, separate a directional claim from its demonstration. Objects, arrows, equality, identities, composition and preservation obligations must be supplied. Approximation needs an end-to-end adequacy bound. The worked join applies to capability acceptance or a claim about that join; it is not demanded for every individual categorical claim. Unsupported claims remain hypotheses. Supported. |
| Interpretation and external dependencies | [Product boundary](../../../specification/PRODUCT.md#product-boundary), line 25, and [A_C_DEPENDENCY](../../../specification/requirements/A_C_DEPENDENCY.md), lines 5–25 and 58–89, include the candidate's own interpretation while keeping theory, carrier, checker and released Representation distinct. Fixed mechanics do not supply semantic or theorem proof. The human-process extension does not select an executor through a_c. Supported. |
| Evidence, reuse and frames | [Intent](../../../specification/INTENT.md#what-it-achieves), lines 27–31, [the frame basis](../../../specification/REFERENCE_FRAME_BASIS.md#conservation-and-stops), lines 45–60, and conformance lines 13–18 retain authentication, current applicability, material invalidation, independent judgement and sufficient context. A new counterexample can reopen reliance despite unchanged candidate bytes. A rules-only packet does not satisfy a task frame. The earlier repairs remain present. Supported. |
| Construction versus acceptance | [Cross-Synthesis](../../../specification/PRODUCT.md#cross-synthesis), lines 236–254, keeps both named bases and requires one receiving owner per contribution. An unchanged relocation remains conserved. The [open decisions](../../../specification/PRODUCT.md#open-owner-decisions), lines 359–366, correctly retain C3 actor binding, ported-authorship review, thread selection and release identity as decisions still to be made. The latest GOALS status does not claim owner sign-off. Supported, subject to F1 and F2. |

These are source judgements. No actual human, mixed or software execution binding was exercised in this review, and no categorical theorem was established.

## Verification and limits

- The exact installed predecessor verification returned `valid: true`, with no failures. The Product Definition status/verification also returned valid, with the implementation-location limit demonstrated by F2.
- All 155 parsed Markdown links across the ten specification files resolved, including checked heading anchors. This check does not validate backticked successor-locus strings as claims of semantic conservation.
- The 16 predecessor-body byte counts and SHA-256 digests in the inventory matched the installed release. The table contains 691 claim rows including the split child: 658 reported conserved, 2 superseded, 20 not applicable and 11 unresolved. These are recorded tenant assertions and limits, not independently accepted results of this review.
- Since the original comparison cut, the frontier text changes are its status introduction and owner-name wording; no tenant disposition was requalified by those edits. The existing candidate conservation audits are not repeated here.
- Whitespace checks over the specification changes passed. The final inspected specification bytes matched their frozen Git subject.

No application tests, paid probe actors, a_c execution or fresh-frame trials were needed to establish these two source/routing findings. The review makes no claim about whole-method effectiveness, human-process usability or release qualification.

## Recommended action

Correct F1 and F2, then review those exact deltas and freeze the common input for the owner's sign-off. Keep the selected computational-binding requirement and the two tenant bases.

After sign-off, follow the existing Product sequence: select the bounded sum-and-histogram thread under installed rc.2, with its two execution bindings, independent oracle, approximation bound, refusal and uncertain-effect cases. Bind the C3 actors and resolve review of ported authorship before admitting affected tenant work. The thread supplies evidence for amendments; member acceptance and release qualification retain their own obligations. There is no source-review basis here for another broad rewrite or for reopening the settled reading of restatement.

## Effect record

The user requested a review of the current specification. Inspection ran as a Reviewer. For publication, this activation changes to a bounded review Writer with an operation grant to create exactly this commentary post under `.ai-workspace/comments/codex/`. The write grants no common-specification, ticket, candidate, commit or release effect. This post does not accept the common revision or start C3 work.
