# Independent Build Tenants

The two build tenants, [Codex](codex/README.md) and [Claude](claude/README.md), each build their own candidate of the common [Product](../specification/PRODUCT.md) as documents. Their designs, prose organisation, a_c encodings and proofs may differ, within the shared meaning the common specification defines.

Each candidate's Spec Method implements the [build-tenant binding requirement](../specification/requirements/README.md#build-tenant-binding-requirement): requirements are realised through a computational calculus bound to a concrete technology stack, human process or mixed environment. Each candidate applies that requirement to its own realisation. Codex and Claude identify the authors; their names alone select no execution environment for the method they express.

The product owner owns the common specification (the WHAT) and its decisions. Codex holds the common construction pen; common changes receive review independent of their author before owner acceptance ([Construction Authority](../specification/PRODUCT.md#construction-authority)). Tenant work follows [Development Isolation](../specification/PRODUCT.md#development-isolation): own branch, own sparse worktree, own territory. A tenant requests a shared change through the pen. A tenant Writer does not edit the common specification, the tickets or its peer's candidate.

## Current Task

C3 reconstruction. Each tenant continues its own candidate line from the exact preceding cut named in its admitted contract and may take named parts of the other's ([Cross-Synthesis](../specification/PRODUCT.md#cross-synthesis)). The original synthesis bases at `31f28f9` remain historical inputs. Codex iteration 3 follows the common pillar and constraint-surface update; the peer line retains its own activation. The work is carried by each tenant's ticket under [T-002](../.ai-workspace/tickets/active/T-002-c3-successor-construction.md):

- [Claude](../.ai-workspace/tickets/active/T-002-CLAUDE-c3-successor-construction.md);
- [Codex](../.ai-workspace/tickets/active/T-002-CODEX-c3-successor-construction.md).

Nothing runs until an execution contract is admitted in that ticket. Each ticket records its current actors, input and limits; historical contracts do not activate a successor. Codex iteration 3 is governed by EC-CODEX-I3-01. The peer line retains its own recorded activation.

## Territory And Returns

Construction territory is the tenant's own `build_tenants/<tenant>/`. Returns are recorded there, for example in `qualification/RETURNS.md`, and the pen records them in the tenant's ticket.

## Reading The Peer

A tenant reads its peer's candidate only in two cases:

- under [Porting reads](../specification/PRODUCT.md#development-isolation), at the commit named in Cross-Synthesis;
- in a review the product owner authorises.

## Reviews

The product owner authorises reviews between tenants one at a time, under Development Isolation. The reviewer:

- reads the reviewed tenant's branch at a named commit;
- records its expectations from the sources before opening the candidate;
- writes the review under `.ai-workspace/comments/<reviewer>/`;
- makes no repair;
- does not assess work it authored.

An actual Claude review runs as Claude, and an actual Codex review runs as Codex. The C1 reviews written into peer `qualification/C1_REVIEW.md` files and peer tickets before this rule are historical records, not a template.

## Activation Checks And Stops

Before any effect, each activation:

- verifies the current input snapshot from its input commit, and the fixed builder basis, which is the installed release;
- stops if a material input changes, and records the changed input before continuing;
- names explicitly any additional material source it selects.

Declared shared inputs outside the tenant's sparse checkout are read with `git show <input-commit>:<path>`. The tenant freezes the exact subject it authored, and records its pin, basis, residuals (what it left unresolved) and return in its own return record.

A tenant's self-check is not acceptance. One reviewer's GO cannot close the peer's task or a checkpoint. The product owner resolves conflicts.

## Initial Principles Task

C1's task was each tenant's own `design/PRINCIPLES.md`. C1 closed on 2026-10-11, and its outcome is recorded in [PRINCIPLES](../specification/requirements/PRINCIPLES.md#c1-disposition). The task contract is this file at commit `8a77d02`.
