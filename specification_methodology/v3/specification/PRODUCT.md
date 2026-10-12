# STDO 3 Product

Status: working common Product definition; structure construction selected, principles and capabilities awaiting their checkpoints.

## Product Boundary

STDO 3 is a specification methodology realised as documents. It defines purposeful construction and evaluation for actors with finite context, attention, time and capability.

The target version is the successor of the installed `stdo://releases/v2.5.1-rc.2/` cut (manifest SHA-256 `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`). That cut is both the builder basis of this source project and the predecessor whose semantic claims the successor evolves under [STDO-UP-015](stdo://releases/v2.5.1-rc.2/standards/RELEASE_METHOD.md#successor-baseline-conservation-stdo-up-015). The predecessor's claims are enumerated in [requirements/PREDECESSOR_CLAIMS.md](requirements/PREDECESSOR_CLAIMS.md); that file is the construction frontier. Under the [standalone successor requirement](requirements/README.md#standalone-successor-requirement) the successor consists of the foundational axioms and the full predecessor corpus restated on them, complete without the predecessor remaining operative. Activation of a finite actor is by projected reference frame, never by the corpus as a whole.

The structure distinguishes general foundations, Spec Method as one particular methodology, and optional domain profiles and operational realisations. Proposed algorithmic, informational and computational interpretations are orthogonal concerns.

The source project owns one common WHAT. Codex and Claude are independent build tenants supplying HOW and documentary implementations. Their organisation, wording and encodings may differ while their accepted outputs satisfy the same common contract and independently specified expectations.

The method semantics expressed by tenant documents are distinct from the common construction specification that governs those documents. A tenant design is not a replacement Product definition. a_c interpretations and tools retain separately owned dependency and proof identities.

ABG, HoG and application workflow runtimes remain outside this Product. A worked application, Hello World or Data Mapper is an external example or test subject. Its particulars cannot become generic method functionality by precedent.

## Product Identity And Lineage

Decided by Jim on 2026-10-12.

| Coordinate | Binding |
|---|---|
| Product | STDO Specification Methodology, the existing product line whose 2.* source project is the sibling `../v2/` (repository path `specification_methodology/v2/`, `urn:stdo:product-definition:specification-methodology`) and whose release namespace is `specification_methodology` |
| Target version | v3.0.0, continuing that line; its release identities follow the installed RELEASE_METHOD in the same namespace (`refs/tags/specification_methodology/v3.0.0…`) |
| Predecessor | `stdo://releases/v2.5.1-rc.2/`, immutable, operative as builder until a release decision |
| Construction scope | a separate source-project scope kept apart so the 2.5.1 source project is not overwritten; Codex and Claude are independent build tenants for the same target version. Jim decided on 2026-10-12 that the two source projects live side by side as `specification_methodology/v2/` and `specification_methodology/v3/`; this scope is `specification_methodology/v3/`. |
| Identifiers | `urn:stdo:product-definition:stdo-3`, `urn:stdo-3:bounded-context:method` and the `urn:stdo-3:` tenant identities are identifiers, not names. They do not change with the directory. Only paths and display names change. |

The machine-readable definition [stdo_3.json](../stdo_3.json) carries this identity in its product name and in a local-constitution axiom routed to this section; its schema admits no version field, so the version is stated here.

## Construction Authority

Jim's [recorded instruction](../.ai-workspace/tickets/active/T-001-common-definition-and-checkpoints.md#owner-instruction) authorises the new structure and independent C1 preparation/attempts. Codex held the common construction pen for setup and C1. From 2026-10-12 Claude holds the common pen and Codex reviews every common change before Jim merges it; a review result informs Jim's decision and adopts nothing by itself. The [frame basis](REFERENCE_FRAME_BASIS.md) binds that setup grant to installed STDO 2.5.1 RC2.

This authorisation admits construction boundaries and initial review work. It does not accept the working foundations, future capabilities, implementation, release or adoption. Jim retains the C1 common-principles and C2 capability/acceptance decisions.

C3 disposition grant (accepted by Jim on 2026-10-12 as configuration of the installed STDO-UP-020 disposition relation). For C3 construction the Executive activation named in the [frame basis](REFERENCE_FRAME_BASIS.md#activations-and-owners) may dispose a member restatement as `local_repair`, `re_enter` or `reject` within its grant, and may dispose it `accept` into the tenant's candidate only on a closed author-independent Reviewer result of `satisfied` with every row of the member's frontier cone disposed. Acceptance of the C3 checkpoint, every merge to `main`, every `intentionally removed` disposition and the release decisions remain Jim's. The Reviewer supplies severity as evidence; priority, boundary effect and disposition are the Executive's decisions and are ledgered as separate entries in the work carrier by the common pen, never by the Executive activation itself.

[build_tenants/README.md](../build_tenants/README.md) is the common tenant entry and return HOW selected for initial construction. Tenant effects stay inside their grants; requested common changes return to the common pen. An Executive cannot perform implementation or Git effects under that role.

## Development Isolation

Selected by Jim on 2026-10-11 as local development law for this source
project. It governs how tenant work is isolated and merged; it changes no
installed STDO law and no release cut.

- Lineage. `main` is the sole lineage of this source project. The common
  WHAT (`specification/`, the Product Definition, `.ai-workspace/`) is
  authored on `main` by the common pen.
- Tenant branches. Each build tenant works on a short-lived topic branch
  `tenant/<tenant>/<checkpoint>` cut from `main`, in its own git worktree,
  with a sparse checkout limited to `specification_methodology/v3/specification/`,
  `specification_methodology/v3/.ai-workspace/` and its own
  `specification_methodology/v3/build_tenants/<tenant>/`. The
  peer tenant's directory is not materialised in that worktree.
- Territory. A tenant commits only under its own `build_tenants/<tenant>/`.
  A needed common change is requested from the pen and reaches the tenant by
  merging `main` inward. A tenant does not edit tickets, common files or the
  peer tenant.
- Work carrier (accepted 2026-10-12; corrected to the installed
  [Work-Carrier-To-Execution Rule](stdo://releases/v2.5.1-rc.2/standards/TICKET_METHOD.md#work-carrier-to-execution-rule)).
  C3 work is carried by one upstream authority ticket and one tenant-local
  duplicate per build tenant under `.ai-workspace/tickets/`. Each member
  activation is a run-scoped execution contract derived from the tenant
  ticket, drafted by the pen on the Executive's selection and admitted
  distinctly from drafting; it is not a further ticket. The ticket has one
  writing owner, the common pen, acting as a Writer activation in common
  territory. The pen records each admitted contract, the closed Writer
  result, the Reviewer result, the triage, the Executive's disposition and
  the next authorised activation, each as the Executive decided it, before
  that next activation starts. The Executive activation
  decides and holds no write grant to tickets, common files, candidates or
  worktrees. The tenant Writer's return is written in its own territory
  (`build_tenants/<tenant>/qualification/`) and never in the ticket. The
  ticket is the only action carrier: no Writer activation starts without
  one, and no disposition exists until the pen has ledgered it.
- Inputs. Tenant worktrees use cone mode. A declared shared input outside
  the cone (the plan posts and the matrix under
  `specification_methodology/v2/.ai-workspace/comments/`, the sibling Axiom
  Indexer definition) is read from the snapshot's input commit with
  `git show <input-commit>:<path>`, never from an ambient working tree. A
  file absent from the cone is neither licence to read elsewhere nor
  evidence that the declared input is absent.
- Snapshot. A checkpoint input snapshot names the input commit on `main`
  whose tree holds every member and records each member's hash as read from
  that commit. The ticket entry that records the snapshot is a later,
  descendant commit; the record is excluded from its own tuple.
- Review. Jim authorises reviews between tenants. A reviewer reads the
  reviewed tenant's branch at a named commit, never its working tree, and
  writes only in its own tenant.
- Merge. A tenant branch merges to `main` only on Jim's acceptance of the
  checkpoint review. The branch is deleted and its worktree removed after
  merge. An unmerged tenant branch is work in progress, not a lineage;
  `git worktree prune` runs only after merge.
- Release cuts. `rc/*` and `release/*` remain governed by the installed
  RELEASE_METHOD and are not tenant branches.

## Shared Construction Contract

The [working principles](requirements/PRINCIPLES.md) are the common questions for C1. Each tenant recovers existing source clauses, exposes each proposed derivation's premises, argues claimed independence, preserves hypotheses and critiques possible Spec Method mechanisms. The setup does not decide which proposed foundational derivations succeed.

The frozen [6 October coverage matrix](../../v2/.ai-workspace/comments/codex/20261006T015451Z_MATRIX_AI_DEVELOPMENT_METHODS_STDO_251_BASELINE.md) joins the common C1-inputs-20261011-02 snapshot. Its F27–F30 4/12 score concerns documented coverage on that date, not current effectiveness or automatically selected 3.0 requirements.

Initial attempts are independent. Both can read common input posts and installed source; neither consumes the peer's realisation before the initial frozen returns. Reviews between tenants are authorised by Jim and conducted under [Development Isolation](#development-isolation): the reviewer reads the reviewed tenant's branch at a named commit and writes only in its own tenant. The C1 reciprocal reviews performed before that rule, and their returns in the tenant tickets, are historical records. A review result informs Jim's decision; it does not itself adopt common principles.

Each tenant's C1 principles realisation is reviewed and accepted separately; realisations may differ while answering the common questions. The common WHAT is not replaced by a merged tenant basis. Selection or combination of tenant outputs for a release requires Jim's explicit common-owner decision.

## Checkpoints

- C0: bootstrap the separate scope, common contract and independent entry routes; mechanical readiness and review only.
- C1: independent deep principles attempts and source-first critique; Jim accepts or withholds each tenant's realisation after review. Closed 2026-10-11 with both accepted.
- C2: derive capabilities and a common conformance contract from that basis; Jim selects their scope and acceptance criteria.
- C3 onward: construct the successor under the [C3 Construction Contract](#c3-construction-contract) through Executive-coordinated member restatements, independent evaluation, actual-use frames and separately bound a_c tests.
- Release and adoption: later explicit selections over an exact accepted corpus and dependencies.

C0 cannot close C1; C1 cannot silently close C2. No full standards set, a_c program, worked example or native trial is required for C1.

## C3 Construction Contract

Status: accepted by Jim on 2026-10-12 as this project's configuration of the installed STDO 2.5.1 Executive engagement; C2 closed and C3 selected by that approval ([GOALS](GOALS.md)). Governing process: the baseline's [Complete Engagement Transition](stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md#complete-engagement-transition), [Executive attention and drift locks](stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md#executive-attention-evaluation-and-action), [STDO-UP-020](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#agentic-construction-execution-stdo-up-020) dispositions and TICKET_METHOD admission. Where this section and the installed baseline differ, the baseline governs and this section is corrected. Work authority: [T-002](../.ai-workspace/tickets/active/T-002-c3-successor-construction.md).

Outcome. Each tenant produces a candidate for the target version: its foundational axioms and the full predecessor corpus restated on them per the [standalone successor requirement](requirements/README.md#standalone-successor-requirement), with every row of [PREDECESSOR_CLAIMS.md](requirements/PREDECESSOR_CLAIMS.md) carrying one UP-015 disposition and a successor locus, and with projected reference frames as the activation unit. The predecessor cut stays immutable and operative as builder until a release decision; it is not a component of the successor.

Frontier. The Executive holds `U0` = every `unresolved` row of PREDECESSOR_CLAIMS.md for the tenant, plus every evaluation the contract below requires that is not closed on the current basis. Each tenant declares its own member list and a map from every rc.2 member to the tenant members that receive it. The map is part of the tenant's frontier record and is reviewed with the first member.

Tier obligations. A tenant's organisation and wording are its own; what each tier owes is common:

| Tier | Owes | Receives from the predecessor |
|---|---|---|
| foundations | ontology, principles with standing, result algebra, the reference frame as a first-class object, bounded activation, work state, evidence and authority law | AXIOMATIC_CALCULUS, REFERENCE_FRAME_METHOD, IDENTITY_METHOD, the generic law of SPEC_METHOD and RELEASE_METHOD |
| Spec Method | constitutional chain, requirements and design law, work carriers and triage, assurance and testing law, change classes and re-entry, release mechanics | SPEC_METHOD, TICKET_METHOD, DESIGN_MODULE_METHOD generic law, RELEASE_METHOD |
| profiles | realisation law that imports the tiers above and restates its own predecessor member in full | ODD_METHOD, TRAVERSAL_OCCURRENCE_PROFILE, UX_METHOD, WORLD_MODEL_METHOD, DESIGN_MODULE_METHOD realisation law, STDO_REFERENCE_FRAME_BASELINE frame catalogues and Executive law |
| guides | posting, writing, glossary | POSTING_GUIDE, WRITING_GUIDE, GLOSSARY_GUIDE |
| packaging | manifest, schemas, templates, compressions or their successor, bootstrap, plugin | the non-standard members; disposition may stay `unresolved` during construction and must close before an RC cut |

Activation unit. Each tenant publishes projected reference frames, one per selected task, from its restated corpus (a_c projections or an equivalent the tenant declares). A frame carries the clauses an actor needs for that task and nothing else. A frame, with its subject, is what any actor is activated on. Context is measured in bytes before the actor reads anything and recorded with the activation.

Audiences and tasks (decided 2026-10-12). Audiences: a fresh model actor activated on one frame against a declared subject; a human method owner reading by route; the Writer, Reviewer and Executive actors constructing or assessing the successor itself. Assumed knowledge: none beyond the activated frame and the subject; during construction, the installed predecessor for source routes. Tasks: do a bounded piece of work; resume work another actor left; review work; decide acceptance or release; apply a profile; construct or assess a successor member.

Executive loop. Existing authority is this contract and the ticket. The Executive selects the smallest dependency-ready set `M` from the frontier, normally one member or one declared cone, and activates one Writer per element with the UP-020 intake: exact outcome and checkpoint, the rows in scope, governing invariants, grant and write territory, evidence obligations, exclusions, stop and re-entry conditions, the context, wall and spend envelope, and the exact bounded action. The Writer returns one closed work result: `candidate_ready` with transition evidence (the restated text, its dispositions, its frames, its measured activations), `refused`, `incomplete` or `re_entry_requested`. The Executive evaluates the result, activates the Reviewer for every `candidate_ready` (independent review is required for every member), consumes the Reviewer's closed result, applies the disposition grant above, has the common pen ledger the decision in the ticket, and issues the next already-authorised activation. The Executive activation holds no write grant and never mutates ticket, candidate, common or worktree bytes; a same-actor role change is ledgered by the pen before the effect, and the actor is no longer Executive for that effect.

Acceptance criteria for one member restatement (the C2 contract, accepted 2026-10-12, applied at C3):

1. Every row of the member's frontier cone has exactly one UP-015 disposition and, for `conserved` and `superseded`, a successor locus that resolves.
2. For every `conserved` row the Reviewer's author-independent source comparison finds the claim semantically present in the successor's own text, which is UP-015's semantic conservation evidenced under the standalone successor requirement. A route alone, a label match or a paraphrase that drops a determination fails.
3. Every `superseded` row names the accepted successor relation; every `intentionally removed` row names Jim's decision and reason; every `not applicable` row carries a bounded reason.
4. The member's selected tasks each have a projected frame that fits one bounded activation under the declared envelope, and a fresh actor given only that frame and the subject applies it against expectations specified independently of the author, without private validator knowledge or author memory.
5. The [conformance discriminators](conformance/README.md) hold against the member's text under logical review.
6. The restatement introduces no new obligation without naming the purpose and material relation that require it, and no carrier or process churn.

Independence. The Reviewer is never the author of the subject. By default the Reviewer is a different model family from the Writer; a same-family Reviewer is a declared exception with its reason in the activation record, and its result is marked as such.

Envelopes. Every activation declares its context allowance in bytes, its wall-time allowance and its spend allowance, and reports the measured context before read and the spend after. No universal budget is set by this contract; the Executive selects each envelope per activation and records it.

Closure. C3 closes for a tenant when every row of its frontier is disposed and every member is accepted under the grant above. Jim accepts the checkpoint. Selection or combination of tenant candidates for a release remains his separate decision.

## Open Owner Decisions

- Audiences, tasks, assumed knowledge and the C2 acceptance criteria: DECIDED 2026-10-12, in the [C3 Construction Contract](#c3-construction-contract).
- C3 Executive and Reviewer actors per tenant: OPEN; Jim names them in the tenant tickets. Until then every execution contract stays `drafted`.
- Release lineage: DECIDED 2026-10-12, see [Product Identity And Lineage](#product-identity-and-lineage); the target version continues the existing STDO Specification Methodology line.
- Candidate/RC ref naming: follows the existing `specification_methodology` release namespace under RELEASE_METHOD; the exact candidate ordinal and cut are selected before an RC cut. The earlier `rc/stdo_3/3.0.0` proposal is withdrawn by the lineage decision.
- Construction-scope layout: DECIDED 2026-10-12; `specification_methodology/v2/` and `specification_methodology/v3/` side by side, identifiers unchanged. Performed as its own bounded change, independent of this contract.
- Cohort relation: OPEN before an RC cut. Existing Product IDs and the current cohort remain unchanged; RC2 remains the operative builder basis.

## Dependencies And Acceptance

[The a_c dependency contract](requirements/A_C_DEPENDENCY.md) records exact theory and immutable mechanical subject. The sibling Product Definition is a routing locator, not the pin. No Axiom RC2 Product Install has been selected or verified for this new scope; C1 needs source recovery, not acquisition.

[Conformance questions](conformance/README.md) seed common discriminators. Runnable cases and independently specified expected results are selected at C2. Syntax, valid maps, document count, local approval and historical green ABG/STDO outcomes do not establish current semantic acceptance.

All prior STDO 2.* source, releases, companion Products and stack-release selection remain unchanged.
