# REVIEW: Revised v3 specification, intent and meaning

**Author**: Dimitar Popov
**Date**: 2026-10-13T14:19:23Z
**Addresses**: Common specification at `698485dd87cb83b875506686ca8e01a5ccedfbdb` on main; subsequent changes to the revision previously reviewed at `e96be6fb7f85cac0815f88d6ba7a9180185e2dd6`
**Status**: Open

## Summary

**Changes required before this revision becomes the next tenant input.** The selected direction is recoverable and the detailed requirements retain much of it. The explanatory rewrite introduces two material contract conflicts and weakens three explanations or checks. These are bounded common-specification repairs.

The Intent needs a clearer argument. It moves from a mission sentence into definitions, a five-part inventory, ownership rules, a result algebra, a program analogy, promises about recovery and a construction sequence. The reader must infer how these things serve the mission. Several explanatory substitutions also change what a worker would do. Adding definitions has therefore increased the amount to read without reliably preserving the distinctions being explained.

The mission sentence is Jim's example, recorded at [T-001](../../tickets/active/T-001-common-definition-and-checkpoints.md), lines 292–297. The findings concern its elaboration and the consistency of the resulting specification. They do not reopen the two tenant bases, the single result algebra, or the selected relational meaning of “restated on the axioms.”

My earlier GO covered the three-commit contract at `e96be6f`. It did not cover the later Intent rewrites and context pass now under review. Its two clarifications have been repaired.

## Analysis

### F1 — S2: the required a_c output is both inside and outside the product

Frozen locations: [INTENT](../../../specification/INTENT.md#what-the-product-is), lines 13 and 27; [PRODUCT](../../../specification/PRODUCT.md#product-boundary), lines 5 and 25; [A_C_DEPENDENCY](../../../specification/requirements/A_C_DEPENDENCY.md), lines 11 and 89.

Intent and Product include the method's rules represented in a_c in the deliverable. Product then says a_c interpretations and their checking tools “are owned separately from this product.” This groups the candidate's required interpretation with the external checker and excludes both through the same boundary statement.

Separate identity and proof boundaries do not settle Product membership. The installed [Axiomatic Calculus](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#position), lines 33–47, distinguishes the calculus, its interpretation and its encoding; separate Product acceptance and release are additional decisions. A_C_DEPENDENCY already distinguishes tenant outputs from the separately released STDO Representation.

Counterexample: a Writer supplies the method documents and declines to supply or own their interpretation, citing Product's boundary. That reading conflicts with the deliverable stated at Product line 5. Conversely, requiring the candidate's interpretation does not authorize modifying or releasing the external checker or canonical Representation.

Correction: state candidate membership separately from semantic ownership, dependency identity and release authority. The candidate supplies its required a_c interpretation. External checking tools and the existing released Representation retain their own ownership. The candidate interpretation retains its own exact subject and proof boundary.

### F2 — S2: the restatement gloss adds an apparent rewriting obligation

Frozen locations: [PRODUCT](../../../specification/PRODUCT.md#product-boundary), line 13, and [Construction Authority](../../../specification/PRODUCT.md#construction-authority), line 125; [Standalone Successor Requirement](../../../specification/requirements/README.md#standalone-successor-requirement), lines 31–42.

Product explains “restated on the axioms” as “rewritten so that each rule rests on the axioms.” It later defines a member restatement as a predecessor member “rewritten into a tenant's candidate.” Requirements expressly permits unchanged predecessor text when it carries the three required relationships, and states that the proportion rewritten proves none of them.

Counterexample: a candidate retains an existing rule's wording, exposes its foundational premises and additional policy choices, and makes the consuming method use the shared contract. Requirements permits this. A Writer or Reviewer treating the new Product definition as a textual rewrite requirement can reject it or perform unnecessary rewriting.

The direction selected by Jim is a relationship between foundations, deciding law, actual use and standalone conservation. It is stronger than copying old prose beneath new headings, but it is not a demand to change each sentence.

Correction: make both Product explanations refer to that existing relational definition. Preserve the requirement to demonstrate foundational integration. Make neither textual similarity nor textual difference an acceptance test.

### F3 — S3: authentication has become confirmation of planning

Frozen location: [conformance/README](../../../specification/conformance/README.md), line 13; compare the same row at `e96be6f`.

The earlier discriminator requires every planned assessment slot to be authenticated. The rewrite says every planned assessment is “verified as genuinely planned.” These are different checks. Plan membership does not establish that a returned judgment came from the right producer, concerned the right subject and basis, or carries its supporting evidence.

Counterexample: A is an authentic failure, B is uncovered required coverage, and another genuinely planned slot contains a judgment copied from a different subject. All assessments can be genuinely planned while that returned judgment remains misbound.

Correction: restore authentication and explain the bindings it checks. Keep B as required coverage outside the completed planned assessment set, so the intended aggregation case still reaches its consumer. This finding concerns the adequacy of the discriminator; no runtime admission was exercised or shown to fail.

### F4 — S3: the reuse promises omit their conditions

Frozen locations: [INTENT](../../../specification/INTENT.md#what-it-achieves), lines 39–40; [REFERENCE_FRAME_BASIS](../../../specification/REFERENCE_FRAME_BASIS.md#conservation-and-stops), line 56.

Intent says a reviewer can check a result without redoing the work, and a result stays valid until something it was based on changes. This does not explain the applicability, invalidation and independent-evaluation conditions retained in the governing rule.

The installed [Reference Frame Method](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#return-a-closed-result), lines 630–641, requires those conditions. A declared revising observation can invalidate reliance on a result, and an independent evaluator must still acquire sufficient evidence and supply its own judgment.

Counterexample: the candidate and earlier test evidence remain unchanged, but a new counterexample defeats the claimed coverage. Byte stability cannot preserve reliance on that coverage claim. A review may also need to repeat a relevant observation; having a prior result does not waive that need.

“Basis changes” could be read broadly enough to include these cases. Intent leaves that essential reading implicit, while promising unconditional validity and avoided work. This is an explanatory omission, not evidence that a new runtime rule has been adopted.

Correction: describe reuse as conditional on current applicability and continuing validity. Retain progress across interruption; reopen affected claims when their invalidation conditions hold. Independent assessment may reuse valid evidence while still doing the work its own judgment requires. This requires no new log, carrier or universal revalidation step.

### F5 — S3: a reference frame is explained as only a rule document

Frozen locations: [INTENT](../../../specification/INTENT.md#mission), line 9, and lines 28 and 38; [REFERENCE_FRAME_BASIS](../../../specification/REFERENCE_FRAME_BASIS.md#activations-and-owners), lines 31–41.

Intent calls a frame “a document holding only the rules that task must follow.” The local frame basis instead binds purpose, exact subject and inputs, governing basis, capability, permitted effects, required relations, evidence, stop conditions and return. The installed [Reference Frame Method](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#canonical-compression), lines 12–20, makes those relations part of an activated evaluation.

Counterexample: an actor receives relevant clauses and a task description but no applicable effect grant or sufficient evidence. The packet meets the introductory description while failing the actual activation contract.

Correction: explain the frame as the bounded contract and material needed for a particular evaluation or task. A published document projects that frame; collecting rules alone does not establish sufficient context. Preserve frame-based activation and the declared capability limits.

### Why the Intent is still difficult to use

The governing [Specification Surface Rule](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#specification-surface-rule) assigns Intent the purpose and directional scope. The [Writing Guide](stdo://releases/v2.5.1-rc.2/standards/WRITING_GUIDE.md#practical-layer-checks) asks whether downstream work can be derived from the statement and whether it belongs at that layer. Neither rule requires unexplained shorthand.

Three explanatory relationships need to come before the inventory:

- **Purpose to method:** explain how an explicit purpose becomes requirements against which different realisations can be built and judged. This is what a consumer can do with the method.
- **Foundations to decisions:** explain that shared premises and declared policy choices govern actual method rules and result composition. Merely adding an axioms section does not supply that relationship.
- **Categorical accounts to preservation:** explain why algorithmic description, information meaning and computation are separate accounts, and what a demonstrated mapping between them allows a builder or reviewer to establish.

The current Intent uses “things built” and “steps” to explain categories, then calls the specification a program, without connecting these statements to those separate accounts. Product lines 17–23 and PRINCIPLES lines 81–87 retain the distinction more clearly. Intent also calls every represented rule an axiom without distinguishing foundational premises from laws or consequences represented in the formal language. That explanation should preserve the foundation-to-law relationship rather than suggesting each rule is an independent premise.

The five-part inventory mixes methodological tiers with a representation and task projections. Those can all be parts of the delivered product, but their different roles need to be stated. The compiler analogy and steel-thread sequence primarily explain this construction campaign, already owned in Product and Goals. They take attention from the consumer outcome in Intent.

The result is an introductory description whose reader must repair its meaning by consulting the detailed requirements. The correction is a connected explanation of the chosen method, with accurate terms and qualified outcomes.

### Corrections already supported

The previous review's findings are closed within their stated scope:

- The categorical standard applies items 1–5 to individual claims as applicable, and reserves the worked join for categorical capability acceptance or a claim asserting that join.
- Current routing names C3 and the two actual local axioms. The tenant entry contract and both instruction files agree with the current cross-synthesis phase.
- T-002 makes reactivation of an indeterminate result conditional on a capable, authorised next evaluation.

The single result algebra still preserves predicate and domain outcome, non-performance, uncertainty and effect distinctions. Each tenant retains its own frozen base at `31f28f9`. Porting requires a named source and receiving owner. Executive and Reviewer bindings, and the arrangement for reviewing ported authorship, remain open. The revision admits no cross-synthesis execution contract.

The categorical demonstration standard keeps mathematical proof, structural checks, independent oracle tests and unresolved claims distinct. This review supplies no proof of the proposed categories or maps and requires no unclaimed categorical equivalence, sheaf theorem or universal construction.

### Small residual corrections

These predate the explanatory rewrite and are not new architectural findings:

- A_C_DEPENDENCY line 13 still quotes `../axiom_indexer/stdo_default.json` as the Product Definition's locator. The actual composition field is `../../axiom_indexer/stdo_default.json`. State the actual field and its reference base.
- PREDECESSOR_CLAIMS line 3 still describes a proposed frontier awaiting merge from `common/c3-contract`. Its current status belongs with its current consolidated frontier state; obsolete proposal status belongs in history.
- Product line 189, frame-basis line 28 and tenant-entry line 33 still route review writing into a tenant. Jim's later placement ruling puts reviews in `.ai-workspace/comments/`. Align that routing with the ruling without granting a reviewer peer-tenant write access.

## Recommended Action

Return this revision to the common pen for the bounded corrections above before freezing the next tenant input.

Restructure Intent around four connected statements:

1. **Purpose and outcome.** Define a method by which people and computational actors construct and change software and processes from an explicit purpose, with independent realisations judged against common requirements.
2. **Foundational structure.** Establish the commitments and additional policy choices from which the Spec Method and profiles obtain their deciding rules. Shared meanings have one owner; results compose through one algebra.
3. **Chosen mathematical direction.** Describe the separate algorithmic, informational and computational accounts, the preservation obligations on their relationships, and the role and limits of the axiomatic representation.
4. **Use and adequacy.** Give bounded actors sufficient task frames, truthful outcomes and lawful recovery while retaining applicable progress. Supply a standalone method and evaluate it through its own declared process.

This is a proposed structure for the pen's rewrite, not replacement constitutional text. Keep the product inventory, exact contract definitions and construction sequence at their existing appropriate owners. Give enough context to understand the mission without re-defining each owner's rules in the introduction.

The observed failure pattern is that explanatory synonyms replace technical predicates: restatement becomes rewriting; separate identity becomes external ownership; authentication becomes planning membership; an activated frame becomes a rule document. The existing requirement to check consistency across the affected specification layers is sufficient to catch these changes. A new method layer or governance procedure is unnecessary.

Re-review the affected meanings and their consumers after correction. Preserve the repaired routing, worked-join scope and conditional reactivation. The owner still decides acceptance and the next construction activation.

## Verification and limits

- Source was read from frozen Git objects at `698485dd87cb83b875506686ca8e01a5ccedfbdb`, compared with `e96be6f` and the pre-revision base `15cc8458a783d5c3f2cbd61d252bdcad73e4f987`.
- The combined range from that base contains 19 changed files: the 15 listed files, the earlier review post, and PRINCIPLES, PREDECESSOR_CLAIMS and the Product Definition. The two extra Markdown files change only owner-name references; the definition changes its display name. Existing frontier dispositions were not requalified.
- The earlier review post matches SHA-256 `b762555c468e1bb0ffaa371b39c616ac4b4518682123c91b88ccfa47ba43092d`; its historical verdict is unchanged.
- Installed builder `v2.5.1-rc.2`, manifest `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`, verified valid with no failures. Current Product Definition verification also returned valid with no failures. Frozen-diff whitespace checking passed. These checks establish no semantic acceptance.
- Two bounded read-only evaluations covered Intent meaning and common-contract consistency. Their findings were checked against the frozen sources in this review.
- No tenant implementation was read or altered, and no actor trial, a_c semantic evaluation, C3 member acceptance or release qualification was performed.
- The only write is this review post in the authorised Codex comments directory, performed as a separately scoped review Writer. No common specification, ticket, candidate, commit, branch or release was changed.

