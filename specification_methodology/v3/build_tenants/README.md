# Independent Build Tenants

The two build tenants, [Codex](codex/README.md) and [Claude](claude/README.md), each build their own candidate of the common [Product](../specification/PRODUCT.md) as documents. Their designs, prose organisation, a_c encodings and proofs may differ, within the shared meaning the common specification defines.

Each candidate's Spec Method implements the [build-tenant binding requirement](../specification/requirements/README.md#build-tenant-binding-requirement): requirements are realised through a computational calculus bound to a concrete technology stack, human process or mixed environment. Each candidate applies that requirement to its own realisation. Codex and Claude identify the authors; their names alone select no execution environment for the method they express.

The product owner owns the common specification (the WHAT) and its decisions. Codex holds the common construction pen; common changes receive review independent of their author before owner acceptance ([Construction Authority](../specification/PRODUCT.md#construction-authority)). Tenant work follows [Development Isolation](../specification/PRODUCT.md#development-isolation): own branch, own sparse worktree, own territory. A tenant requests a shared change through the pen. A tenant Writer does not edit the common specification, the tickets or its peer's candidate.

## Current Task

I4 proceeds in three stages under [T-001](../.ai-workspace/tickets/active/T-001-common-definition-and-checkpoints.md#iteration-4-common-specification) and [T-002](../.ai-workspace/tickets/active/T-002-c3-successor-construction.md#iteration-4-staging):

1. Codex prepares the common revision, Claude reviews its exact freeze, and the product owner ratifies it.
2. Each tenant rebinds to that ratified input and synthesises its own candidate with selected contributions from its peer, under [Cross-Synthesis](../specification/PRODUCT.md#cross-synthesis).
3. The two frozen candidates receive the shared comparison and the product owner selects the next basis.

I4 common preparation is active. Tenant I4 construction waits for ratification and each line's admitted contract. The closed I3 input and historical contracts remain evidence for their own subjects. The current candidate and donor coordinates, supported repairs and unresolved decisions are in T-002; no live working-tree read substitutes for a named peer commit.

The tenant tickets are [Claude](../.ai-workspace/tickets/active/T-002-CLAUDE-c3-successor-construction.md) and [Codex](../.ai-workspace/tickets/active/T-002-CODEX-c3-successor-construction.md). Each new contract names the common input, own preceding candidate, donor, tasks, actors and resource envelopes. A draft contract starts no work. Common ratification and construction admission accept no tenant candidate or predecessor replacement.

## Territory And Returns

Construction territory is the tenant's own `build_tenants/<tenant>/`. Returns are recorded there, for example in `qualification/RETURNS.md`, and the pen records them in the tenant's ticket.

## Reading The Peer

A tenant reads its peer's candidate only in two cases:

- under [Porting reads](../specification/PRODUCT.md#development-isolation), at the donor commit named in its admitted contract;
- in a review the product owner authorises.

## Reviews

The product owner authorises reviews between tenants one at a time, under Development Isolation. The reviewer:

- reads the reviewed tenant's branch at a named commit;
- records its expectations from the sources before opening the candidate;
- writes the review under `.ai-workspace/comments/<reviewer>/`;
- makes no repair;
- does not supply independent acceptance evidence for work it authored. A donor reading its own port is explicitly supplementary; the receiving line obtains the nonauthor review required by Cross-Synthesis.

Cross-tenant review means assessment of the other tenant's candidate; its access and assignment require the owner's authorisation. Model family is a separate independence condition. A different-family nonauthor reviewing the activating tenant's own candidate does not thereby acquire access to the peer candidate or authority to act for that peer. Its activation, effects, independence and any spend still require the applicable grant. An actual Claude review runs as Claude, and an actual Codex review runs as Codex. The C1 reviews written into peer `qualification/C1_REVIEW.md` files and peer tickets before this rule are historical records, not a template.

## Activation Checks And Stops

Before any effect, each activation:

- verifies the current input snapshot from its input commit, and the fixed builder basis, which is the installed release;
- stops if a material input changes, and records the changed input before continuing;
- names explicitly any additional material source it selects.

Declared shared inputs outside the tenant's sparse checkout are read with `git show <input-commit>:<path>`. The tenant freezes the exact subject it authored, and records its pin, basis, residuals (what it left unresolved) and return in its own return record.

A tenant's self-check is not acceptance. One reviewer's GO cannot close the peer's task or a checkpoint. The product owner resolves conflicts.

## Initial Principles Task

C1's task was each tenant's own `design/PRINCIPLES.md`. C1 closed on 2026-10-11, and its outcome is recorded in [PRINCIPLES](../specification/requirements/PRINCIPLES.md#c1-disposition). The task contract is this file at commit `8a77d02`.
