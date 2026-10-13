# STRATEGY: Rebuilding each v3 candidate on the current specification by cross-synthesis

**Author**: Dimitar Popov
**Date**: 2026-10-13T17:43:41Z
**Addresses**: the product owner's instruction of 2026-10-14 (local time) quoted below; [Cross-Synthesis](../../../specification/PRODUCT.md#cross-synthesis); the common specification at `c0beefd`; the tenant candidates at `31f28f90c4a9b15243d84630fc4799024a9cd7ac`
**Status**: Draft, for the product owner's decision

## The instruction and how this proposal reads it

> ok v3/codex was built on the sol model and is not as good a build as the v3/cluade model, ive made the call to allow each agent to synthesise the best elements of the other agent, take the new specifications and rebuild their v3/ implementation in that light
>
> give me a proposal

Reading: each line rebuilds **on its own candidate**, not from an empty directory. Cross-Synthesis keeps each line on its own base and lets it take named parts of the other. "Rebuild" here means: go back to the tenant's design, change what the current specification now requires, port the selected parts, and re-prove what the changes touch. If a rebuild from nothing was meant, this proposal does not apply.

The product owner's view of the two builds is the reason for the decision. This proposal does not use that view as evidence about any particular part; each port below is justified by the gap it closes.

Most of the proposal concerns the Claude line. The Codex line is outlined in the last section for Codex to complete.

## Terms used

- **Predecessor claim**: a rule or statement of the previous release, 2.5.1-rc.2, that could affect the new one. There are 691, listed in `PREDECESSOR_CLAIMS.md`.
- **Disposition**: the outcome given to each claim under the previous release's rule STDO-UP-015: `conserved`, `superseded`, `intentionally removed` or `not applicable`.
- **Frontier**: the work still open, meaning claims without a disposition plus required evaluations not yet closed. A member's **cone** is the set of claims that member covers.
- **Criteria 1 to 6**: the acceptance criteria for one member in the [C3 Construction Contract](../../../specification/PRODUCT.md#c3-construction-contract). Criterion 2 is an independent check, claim by claim, that each conserved claim's meaning is present. Criterion 4 is a fresh actor using the member's frame correctly. Criterion 5 is the conformance discriminators.
- **Execution contract**: the run-scoped contract derived from a ticket. No activation runs until the contract is admitted and recorded in the ticket.
- **Same-family exception**: a Reviewer from the same model family as the Writer, which the contract permits only as a declared exception.

## What changed since the bases were built

Both candidates were built against the specification at `31f28f9`. The current specification adds the following obligations. Each one applies to both lines.

| New obligation | Where it is owned | What it asks of a candidate |
|---|---|---|
| Restated on the axioms | [Standalone successor requirement](../../../specification/requirements/README.md#standalone-successor-requirement) | Every material family of rules shows its premises, the consequences that follow, and any added choices with their owners (relation 1). Shared contracts are used where actors apply them, not only cross-referenced (relation 2). Own text supplies every conserved rule (relation 3). |
| Single ownership | [requirement](../../../specification/requirements/README.md#single-ownership-requirement) | One owning section per rule within the candidate. A frame's copy of a clause names its owner. |
| Single result algebra | [requirement](../../../specification/requirements/README.md#single-result-algebra-requirement) | One core set of results, owned by the Foundations. Each profile's finer results map into it and never raise a result's standing. Conjunction is defined once. Frames that return results carry the algebra. |
| Bounded transitions and frames | [requirement](../../../specification/requirements/README.md#bounded-transitions-and-reference-frames) | Work runs from a current state A to a destination Z through bounded transitions. Roles come from allocating work to actors with finite context and attention; no fixed role inventory. Context fit and adequate attention are judged separately. |
| Build-tenant binding | [requirement](../../../specification/requirements/README.md#build-tenant-binding-requirement) | The candidate's Spec Method states how a tenant binds requirements to a computational calculus and that calculus to an execution environment (a stack, a human process or both). Each tenant also declares its own binding. |
| Categorical demonstration | [standard](../../../specification/requirements/README.md#categorical-demonstration-standard) | Any categorical claim shows objects, arrows, identity, composition and preservation, or stays a hypothesis. |
| Conformance discriminators | [conformance](../../../specification/conformance/README.md) | 30 discriminators now, against 10 at `31f28f9`. Criterion 5 applies all 30 to every member. |

## Where the Claude candidate stands against them

Checked in the candidate at `31f28f9` for this proposal:

- No build-tenant binding. `SPEC_METHOD.md` and `PRODUCT_DEFINITION.md` contain the previous release's build-tenant identity rules but no computational calculus or execution environment. The tenant's `design/` declares neither.
- Measurement has two owners. `REFERENCE_FRAME.md:140` measures context "where the contract selects measurement"; `ACTIVATION.md:211` measures before every read.
- Core results are defined in `ACTIVATION.md` §3, and combination rules in `FOUNDATIONS.md` §4. The first activation establishes whether these amount to one owner or two.
- The public entry, `standards/README.md:42`, still routes to the a_c program generation set-4, although set-6 is current.

Already on record from the first pass and the cross-assessments:

- The set-6 traversal projection is bound to an older digest of `TRAVERSAL_OCCURRENCE.md`, so it is stale.
- Eleven claims are unresolved: the ten compressed summaries of the standards and the bootstrap entry point, which is a placeholder.
- The resume route ships a qualification case's expectations. The Codex cross-assessment found an unsupported approval gate in both resume runs. Whether the shipped case causes it is untested.
- The carrier-retention test case lacks a write grant; this affects both candidates.
- Criterion 4 is not established for REFERENCE_FRAME, AXIOMATIC_CALCULUS, EXECUTIVE_BASELINE, DESIGN_MODULE or TRAVERSAL_OCCURRENCE; their strict reruns were falsified.
- Relation 1 is not shown. Members cite premises P0 to P6 by label, but no family is laid out as premises, consequences and choices.
- All first-pass member acceptances were by same-family reviewers. Codex's cross-family review of 12 October requested changes, and milestones M2 and M3 in T-002-CLAUDE are reopened.

## What the Claude line takes from the Codex candidate

All five parts were nominated in my cross-assessment of the Codex candidate (§8, "Carry forward"). Each is listed with the gap it closes. Line references are from that assessment; this proposal did not reopen the Codex tree. Porting reads belong to the Writer and Reviewer activations.

| Codex part | Gap it closes in the Claude line |
|---|---|
| The specialization table: premises, the consequence that follows, and the particular contract with any independent choice (`TRANSFORMATION_LIBRARY.md:100–106`) | Relation 1. It becomes the format each material family uses to show how it rests on the Foundations. |
| The standing discipline of premises F1 to F6: "adopted commitments … not theorems derived from finite capacity alone" (`FOUNDATIONS.md:48–65`) | P0 to P6 gain a standing column, so a premise is never presented as derived. |
| Reference-only import declarations with direction, loss and owner, and the ladder conformance, then semantic, computational and categorical equivalence (`FOUNDATIONS.md:128–162, 254–258`) | Item 4 of the categorical demonstration standard, which keeps conformance, equivalence and functorial preservation as distinct claims. |
| Verbatim, digest-bound frames, the `FRAME_INPUTS.json` manifest, and the rule that work acquires the deciding owners directly | The stale and oversized a_c-projected frames. A verbatim copy names its owning section, as single ownership item 4 requires, and is regenerated whenever its owner changes. a_c projections become optional. |
| The 608-case finite check: exhaustive enumeration with mutant counterexamples (`qualification/C3/a_c/finite_check.py`) | A pattern for oracles specified independently of the author, used in criterion 4 runs. |

Not taken: the Codex carried corpus as a base. The Claude line keeps its own restated text. However, the specification now permits unchanged predecessor wording where the three relations hold. Where a restated clause adds nothing and cannot be shown to conserve its claim at reasonable cost, the Writer may restore the predecessor wording in that clause. This saves review effort without changing the base.

Relocation rule, from my errata to the direct comparison: an unchanged rule moved to a new place stays `conserved` with its new locus. `superseded` needs an accepted replacement relation.

## The Claude line, step by step

Each step is one or more admitted activations under the existing Executive loop: Writer, then an independent Reviewer, then the Executive's disposition, which is recorded before the next step. At most three activations run at once; the first pass lost hours with six to eight open.

| Step | Work | Output | Size |
|---|---|---|---|
| 1. Design re-entry | Declare the tenant's binding. The computational calculus covers the operations (frame activations, commits, a_c checker runs, fresh-actor runs), how they compose, their effects and the resources measured (bytes, wall time, spend). The execution environment covers Claude sessions and subagents, git worktrees, the pinned Axiom Indexer, and the product owner's decisions as a human process. State the configuration and why it fits the task. List each port with its receiving section, and fix the re-proof span: the claims whose text the later steps change. | `design/` revised; gap list confirmed against the candidate | estimated 1–2 h |
| 2. Foundations | Add the A-to-Z account, the configuration law and resumption, with no fixed role inventory. Give results one owner and combination one definition. Give measurement one owner. Add the premise standing column, the import declarations and the equivalence ladder. Keep the existing categorical diagram (H1) as a hypothesis. | FOUNDATIONS, REFERENCE_FRAME, ACTIVATION, EVALUATION revised | estimated 3–5 h |
| 3. Foundation to law | One specialization table per material family, about fourteen, worked in parallel within the limit of three activations. | tables in the owning members | estimated 4–8 h |
| 4. Spec Method and profiles | State the build-tenant binding in SPEC_METHOD. Check that each profile uses the shared contracts where its actors apply them. Check that every profile result maps into the core without raising standing. EXECUTIVE_BASELINE stays an operational profile owning only its own bindings. | SPEC_METHOD, PRODUCT_DEFINITION and the profiles revised | estimated 3–6 h |
| 5. Frames and actual use | Regenerate frames as verbatim excerpts. Write the oracles before any run. Run fresh actors on the five members where criterion 4 is not established, and on new tasks for configuration and binding. | frame manifest, cases, runs, assessments | estimated 3–5 h; fresh-actor spend estimated USD 5–15 |
| 6. Packaging | After the owner's ruling on the compressed summaries: set the bootstrap entry, route the public entry to the current frame set, and close the eleven unresolved claims. | packaging closed | estimated 1–3 h after the ruling |
| 7. Acceptance | Criteria 1 to 6 per member against all 30 discriminators. Criterion 2 is redone only for claims in the re-proof span; other first-pass claim judgments are kept as evidence. Then cross-family review of the whole line before the checkpoint. | closed results, dispositions, checkpoint request | Reviewer cost unknown |

Total wall time is estimated at two to three working days if decisions arrive without delay. The basis is measured from the first pass: about ten hours of wall time for 680 claims on 12 October, and at least USD 6.66 across the four fresh-actor batches whose spend was recorded. Session token costs were not measured then and remain unknown.

The steel thread is not part of this rebuild. In the direct comparison I recommended holding Foundations acceptance until the steel thread's amendments land. I withdraw that recommendation. The specification now places the full categorical product after release ([Categorical Construction](../../../specification/PRODUCT.md#categorical-construction), step 4), and the thread is not selected. Holding C3 for it would stop C3 indefinitely. The thread's findings reach the method later through the sections that own them.

## Decisions needed before anything runs

1. **The specification basis.** Codex's revision `e38d45a..c0beefd` has had only same-family review. Codex's own current review leaves two findings open:
   - the C3 Outcome requires a successor section for every claim, which contradicts criteria 1 and 3 and would catch the Claude line's 20 `not applicable` claims;
   - `stdo_3.json` routes to `build_tenants/codex/standards/`, which does not exist.

   Proposal: I review the revision cross-family, as you assigned when you gave Codex the pen (estimated 1–2 h). The pen then repairs, you sign off at an exact commit, and the pen records the C3 input snapshot in T-002 at that commit. That snapshot is the basis for both lines. If you prefer to waive my review, say so and the snapshot can be taken after Codex's two findings are fixed.
2. **Actors for the Claude line.** Proposal: your 12 October binding carries over. The Claude session is Executive. Fresh Claude contexts are Writers in `build_tenants/claude/` only, and fresh Claude contexts are Reviewers by declared same-family exception during construction. Codex reviews cross-family at the checkpoint, before any merge.
3. **Review of ported parts.** Codex is the default cross-family Reviewer but wrote the ported text, and the Independence rule forbids a Reviewer assessing its own authorship. Proposal: split the subject.
   - A verbatim port is checked against its source by byte comparison.
   - An adapted port is checked by a Claude Reviewer that did not do the porting, as a declared exception.
   - Codex reviews only the Claude-written text around the port: re-pointed links, owner declarations and the fit with Claude's owners.

   Each reviewer then assesses only text it did not write.
4. **Who records the Claude line's decisions.** Only the common pen writes tickets, and Codex holds the pen. Three options:
   - Codex records every Claude-line decision. That needs a channel between the sessions through you, which is slow.
   - The pen is returned to Claude, which moves the same problem onto the Codex line.
   - **Recommended:** each line's Writer may write only its own tenant ticket's Execution Record, while the pen keeps T-002, the specification and the shared files. This changes one rule in [Development Isolation](../../../specification/PRODUCT.md#development-isolation), which the pen makes.
5. **Which Codex commit the Claude line ports from.** The specification names `31f28f9`. Codex has an unmerged repair round on `tenant/codex/c3-round-1` at `5b4aebb`, which extends its derivation checks and adds a triage-and-carrier frame. Proposal: port from `31f28f9`, whose parts the cross-assessments examined. Use `5b4aebb` only if that round is reviewed and merged first.
6. **The compressed summaries** (keep, supersede or remove). Needed before step 6, not before the start.

## Changes the common pen would make

These follow from the decisions above. None is made by this post.

- Fix Codex's two open findings, plus any from the cross-family review.
- Record the input snapshot at the signed-off commit, and sign off the wording of GOAL-002.
- Record the actors and the ported-part review rule in the tenant tickets, and move both items out of Open Owner Decisions in PRODUCT.
- Amend Development Isolation for tenant ledgers, if decision 4 is accepted.
- Name the porting commit in Cross-Synthesis, if decision 5 changes it.
- Draft the first cross-synthesis execution contract in T-002-CLAUDE for step 1, then record its admission.

## The Codex line, in outline

The same common steps apply: basis, design re-entry, Foundations, foundation to law, Spec Method, frames, packaging and acceptance. Codex's cross-assessment of the Claude candidate nominated four parts for porting:

- ACTIVATION's context construction, faithful refinement, work state and reuse (`ACTIVATION.md:191–280, 433–576, 665–705`);
- FOUNDATIONS' authority, evidence and identity objects and conservation accounting (`FOUNDATIONS.md:44–169, 292–361`);
- the PROFILES binding (`PROFILES.md:9–104`);
- the evidence-sensitive result mappings (`ACTIVATION.md:307–371`, `TRAVERSAL_OCCURRENCE.md:770–815`), after the stale projection is regenerated.

Against the current specification, the Codex line's largest open items are these:

- relation 1 beyond its one demonstrated family;
- relation 2, which its explanatory preambles do not establish by themselves ("An explanatory cross-reference alone does not establish this relationship");
- the build-tenant binding;
- its missing frontier claim;
- its packaging: no manifest or release note, and placeholder install coordinates.

How much more of the Claude candidate to port is the Codex line Executive's selection. Codex should write that line's plan against the same decisions.

## Evidence boundary

This post is commentary. It changes no specification, ticket, tenant file or shared file. The checks on the Claude candidate were read-only greps at `31f28f9` (the tenant trees on `main` are unchanged since then). The other statements cite the posts and tickets linked above. Figures marked estimated are judgments from the first pass; none is measured for this rebuild.
