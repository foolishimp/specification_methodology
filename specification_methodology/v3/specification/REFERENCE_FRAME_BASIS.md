# Project Reference-Frame Basis

This file binds the installed release's roles and reference frames to this source project. It states which activations exist, what each works on and returns, and who may perform it.

## Declaration

| Coordinate | Binding |
|---|---|
| Declaration | urn:stdo-3:reference-frame-basis:bootstrap-v1 |
| Product | urn:stdo:product-definition:stdo-3 |
| Governing method | stdo://releases/v2.5.1-rc.2/ |
| Manifest SHA256 | 3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782 |
| Construction authority | [Product](PRODUCT.md#construction-authority) |
| Subject | This source project, and only tenant or case territory that is explicitly selected |

The installed [Reference Frame Method](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#reference-frame-laws) and its [baseline](stdo://releases/v2.5.1-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md#canonical-compression) supply the roles and the rules for evaluation. This binding copies no profile and creates no runtime.

## Activations And Owners

The rows bind the installed baseline frames under the [C3 Construction Contract](PRODUCT.md#c3-construction-contract) and [Cross-Synthesis](PRODUCT.md#cross-synthesis). The Executive and Reviewer actors for each tenant are not yet named, and an actor that is not named can be given no activation.

| Activation | Subject and result | Actor binding and limits |
|---|---|---|
| Common definition | The shared purpose, boundary, checkpoints and affected clauses. Returns each relation as supported, contradicted or unresolved. | The common construction pen (Claude), with Codex reviewing. Common acceptance is the product owner's. |
| C3 Executive | Works on the tenant's frontier (`PREDECESSOR_CLAIMS.md` rows and required evaluations), the ticket record as read, and closed Writer and Reviewer results. Selects the next set of work `M`, starts activations, reads their results, decides each disposition within the grant, and issues the next authorised activation. | The product owner, or one activation the product owner selects. It holds no write grant of any kind: not to tickets, common files, candidates, peer territory or worktrees. The C3 ledger Writer below records its decisions before the next activation. Its context is limited to the frontier and closed results, never the candidate text. |
| C3 ledger Writer | The C3 tickets. Opens each with the triage the Executive performed. Records each closed Writer result, Reviewer result, triage, Executive disposition and next authorised activation as the Executive decided it. | The common pen (Claude, with Codex reviewing), as a Writer activation in common territory. Writes tickets only, with no authority over candidates, tenants or decisions. |
| C3 Writer | One member or declared frontier cone. Produces the restated text, its dispositions, its frames and their measured activations. Returns `candidate_ready`, `refused`, `incomplete` or `re_entry_requested`, with evidence of the change. | The tenant's own model family, in its own territory only. It may read the peer candidate under [Porting reads](PRODUCT.md#development-isolation). Its context, wall-time and spend limits are declared in the activation, and its context is measured before it reads. |
| C3 Reviewer | One frozen member at a named commit, the predecessor source and independently obtained expectations. For a named contribution, it also reads the part's source in the peer candidate at the commit named in [Cross-Synthesis](PRODUCT.md#cross-synthesis), under [Porting reads](PRODUCT.md#development-isolation). Returns one closed Reference Frame Method result per acceptance criterion, with findings and their severity, and no repair. | Independent of the author. A different model family from the Writer by default; the same family only as a declared exception with its reason. Writes only in its own tenant. |
| C3 fresh actor | One frame and one subject. Produces the actual-use evidence for acceptance criterion 4. | Any model family. It starts with no prior context, outside any repository and outside any path from which instruction files load. Its context is measured before it reads and recorded. |

Each activation binds the following:

- its purpose;
- its exact subject and the inputs it came from;
- the governing basis and source routes;
- capability and access;
- permitted effects;
- the relations it must preserve;
- evidence;
- stop conditions;
- what it returns.

These apply within the scope actually selected. A label alone confers no authority.

## Conservation And Stops

The following are kept distinct:

- the common specification (WHAT);
- each tenant's realisation (HOW);
- work state;
- observations;
- candidate output;
- acceptance judgement.

Unknown premises and unknown applicability stay explicit. Unchanged source recovery and valid judgements may be reused while their validity conditions hold. A judgement that must be independent stays independent.

An authority relation that matters and is missing, stale, contradictory or outside the actor's territory stops the action that depends on it. The case is returned to the relation's owner. Tenant territory and stops are bound by the [tenant entry contract](../build_tenants/README.md).

Verifying the bootstrap shows only that the installed release is present and that routing to it works. This file adds no proposed axiom to the installed release's law.
