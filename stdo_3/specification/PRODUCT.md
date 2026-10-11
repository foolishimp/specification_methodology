# STDO 3 Product

Status: working common Product definition; structure construction selected, principles and capabilities awaiting their checkpoints.

## Product Boundary

STDO 3 is a specification methodology realised as documents. It defines purposeful construction and evaluation for actors with finite context, attention, time and capability.

The structure distinguishes general foundations, Spec Method as one particular methodology, and optional domain profiles and operational realisations. Proposed algorithmic, informational and computational interpretations are orthogonal concerns.

The source project owns one common WHAT. Codex and Claude are independent build tenants supplying HOW and documentary implementations. Their organisation, wording and encodings may differ while their accepted outputs satisfy the same common contract and independently specified expectations.

The method semantics expressed by tenant documents are distinct from the common construction specification that governs those documents. A tenant design is not a replacement Product definition. a_c interpretations and tools retain separately owned dependency and proof identities.

ABG, HoG and application workflow runtimes remain outside this Product. A worked application, Hello World or Data Mapper is an external example or test subject. Its particulars cannot become generic method functionality by precedent.

## Construction Authority

Jim's [recorded instruction](../.ai-workspace/tickets/active/T-001-common-definition-and-checkpoints.md#owner-instruction) authorises the new structure and independent C1 preparation/attempts. Codex holds the common construction pen. The [frame basis](REFERENCE_FRAME_BASIS.md) binds that setup grant to installed STDO 2.5.1 RC2.

This authorisation admits construction boundaries and initial review work. It does not accept the working foundations, future capabilities, implementation, release or adoption. Jim retains the C1 common-principles and C2 capability/acceptance decisions.

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
  with a sparse checkout limited to `stdo_3/specification/`,
  `stdo_3/.ai-workspace/` and its own `stdo_3/build_tenants/<tenant>/`. The
  peer tenant's directory is not materialised in that worktree.
- Territory. A tenant commits only under its own `build_tenants/<tenant>/`.
  A needed common change is requested from the pen and reaches the tenant by
  merging `main` inward. A tenant does not edit tickets, common files or the
  peer tenant.
- Inputs. Tenant worktrees use cone mode. A declared shared input outside
  the cone (the plan posts and the matrix under
  `specification_methodology/.ai-workspace/comments/`, the sibling Axiom
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

The frozen [6 October coverage matrix](../../specification_methodology/.ai-workspace/comments/codex/20261006T015451Z_MATRIX_AI_DEVELOPMENT_METHODS_STDO_251_BASELINE.md) joins the common C1-inputs-20261011-02 snapshot. Its F27–F30 4/12 score concerns documented coverage on that date, not current effectiveness or automatically selected 3.0 requirements.

Initial attempts are independent. Both can read common input posts and installed source; neither consumes the peer's realisation before the initial frozen returns. Reviews between tenants are authorised by Jim and conducted under [Development Isolation](#development-isolation): the reviewer reads the reviewed tenant's branch at a named commit and writes only in its own tenant. The C1 reciprocal reviews performed before that rule, and their returns in the tenant tickets, are historical records. A review result informs Jim's decision; it does not itself adopt common principles.

There is one accepted common basis after C1 disposition, not two competing tenant WHATs. Selection or combination of later tenant outputs requires Jim's explicit common-owner decision.

## Checkpoints

- C0: bootstrap the separate scope, common contract and independent entry routes; mechanical readiness and review only.
- C1: independent deep principles attempts and source-first critique; Jim resolves material conflicts and accepts or withholds one common basis.
- C2: derive capabilities and a common conformance contract from that basis; Jim selects their scope and acceptance criteria.
- C3 onward: construct selected documents through actual-use steel threads, independent evaluation and separately bound a_c tests.
- Release and adoption: later explicit selections over an exact accepted corpus and dependencies.

C0 cannot close C1; C1 cannot silently close C2. No full standards set, a_c program, worked example or native trial is required for C1.

## Open Owner Decisions

- Audiences, tasks and assumed knowledge: OPEN; Jim selects them before C2 acceptance criteria are fixed.
- Release lineage: OPEN; continuation of the specification_methodology method line versus a separate STDO 3 release line.
- Candidate/RC version, namespace and ref naming, including a proposed rc/stdo_3/3.0.0 name: OPEN before an RC cut.
- Cohort relation: OPEN before an RC cut. Existing Product IDs and the current cohort remain unchanged; RC2 remains the operative builder basis.

## Dependencies And Acceptance

[The a_c dependency contract](requirements/A_C_DEPENDENCY.md) records exact theory and immutable mechanical subject. The sibling Product Definition is a routing locator, not the pin. No Axiom RC2 Product Install has been selected or verified for this new scope; C1 needs source recovery, not acquisition.

[Conformance questions](conformance/README.md) seed common discriminators. Runnable cases and independently specified expected results are selected at C2. Syntax, valid maps, document count, local approval and historical green ABG/STDO outcomes do not establish current semantic acceptance.

All prior STDO 2.* source, releases, companion Products and stack-release selection remain unchanged.
