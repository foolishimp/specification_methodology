# STRATEGY: STDO Skills consumption of native a_c support

**Author:** Codex, Writer `/root/composition_proposal_writer`  
**Date:** 2026-10-25  
**Addresses:** The missing durable Skills → a_c composition declaration  
**Status:** Open — draft relation for Product-owner adoption

## Skills AC support

Identity: `urn:stdo-skills:composition:a-c-native-support:proposal-1`.
Source: `urn:stdo:product-definition:stdo-skills`, located by [Skills definition](../../../stdo_skills.json).
Target: `urn:stdo:product-definition:a-c-implementations`, located by [a_c definition](../../../../a_c/stdo_a_c.json).

This directed relation consumes a_c's bounded native STDO 3.0.1 support capability
to construct and operate the two Skills tenants. The [Skills Product](../../../specification/PRODUCT.md)
and [SK-04 through SK-11](../../../specification/requirements/README.md) already require supported tool use, adequate
context, lawful delegation, review and recovery. Its current `composition: []`
omits that dependency. [The proposed edge](../../../../specification_methodology/v3/.ai-workspace/work/PRODUCT_COMPOSITION_PROPOSAL_01/PROPOSED_SKILLS_AC_EDGE.json) would locate this relation
without changing the schema. It is staged separately from the operative overlay.

### Selected meanings and versions

| Coordinate | Exact selection |
|---|---|
| Skills builder and initial consumer method | `stdo://releases/v3.0.1-rc.1/`, manifest `60356364a412dbde8cffe68fe0eda4e2749b0162acce93495534eee13b223df8`, native `fe4941f56a52ed3697a2b516d8d68948b0ea65d9` |
| a_c builder | `stdo://releases/v2.5.1-rc.2/`, manifest `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`; this is not the consumer method |
| Selected provider implementation | Graphify tenant files at repository commit `0ec4b6c94f6255f6057416fec9d4c77feddf1b06`; exact acquired file hashes in [source custody](../../../../specification_methodology/v3/.ai-workspace/work/PRODUCT_COMPOSITION_PROPOSAL_01/SOURCE-CUSTODY.json) |
| Native profile | `urn:a-c:fd-support:method:stdo-3.0.1-rc.1:executive:1`, SHA-256 `a886047e50b8a45c3b47addea0f0809dca2a6c54ac35948df5e01893cc30bbf7` |
| Computational contract | [Native binding](../../../../a_c/build_tenants/graphify/design/fd-support-stdo-3.0.1.md) plus [shared public support design](../../../../a_c/build_tenants/graphify/design/fd-support.md), constrained by [native requirements](../../../../a_c/specification/requirements/fd-stdo-3.0.1-binding.md) |
| Skills frame/host binding | [Product frame basis](../../../specification/REFERENCE_FRAME_BASIS.md) plus the selected Codex or Claude tenant contract and actual host/executor configuration |

The provider is a development implementation with bounded evidence, not an
accepted release or blanket calculus-conformance claim. The relation freezes the
selected provider bytes for its candidate use. Later mutable changes require
explicit source acquisition and compatibility disposition; the directory's latest
contents are not silently substituted for this selection. Exact runtime and
executor dependencies remain per-activation inputs, not facts established by the
repository commit alone.

### Consumed operations and their owners

The selected design owns request/result schemas, supported profiles, failure
behavior and checked properties. This relation imports them rather than restating
their implementations. The required operation families are discovery and exact
source/workspace acquisition; caller-selected context assembly; contract
preflight; registered dispatch/observation; original return capture/check;
source-first review preparation; and separately authorized Writer effects.

`results.conjoin` is unsupported for this native profile. Actor selection of
material sources and semantic judgment remain F_P work under STDO. A successful
transport, assembled Context or complete receipt is not semantic adequacy,
physical completion, task acceptance or release authority.

STDO owns methodology; Skills owns the agent-facing outcome and tenant behavior;
a_c owns supplied tool contracts and implementation. The Graphify library/carrier
can support discovery without becoming a fourth authority. Codex and Claude remain
two tenants of Skills; this edge creates no separate Product for either.

### Authority, purpose and information boundary

Jim retains the Product decisions. Skills' admitted frame basis and exact work
instruction bind the actor and permitted operation. The existing a_c public
contract supplies operation eligibility, not a grant to any caller. Its trusted
operator policy registers the actual principal, source/read scopes, authority
sources, grant, executor, effect territory and return consumer. A request cannot
grant itself territory or replace those records.

The present instruction authorizes drafting and reviewing this relation. It does
not supply a runtime grant. A subsequent use must select its existing lawful work
authority and actual preflight relation; this document supplies neither a dummy
owner approval nor a satisfied admission predicate.

| Actor or component | Material supplied for its purpose | Boundary retained |
|---|---|---|
| Skills Executive | Selected Skills outcome/basis, a_c public contracts, compatibility limits, actual observations and closed returns | Selects within its grant; no mutation or target-meaning authority follows from coordination |
| Skills Worker/Writer | Skills requirement and selected tenant sources, public support contracts and exact permitted task inputs | Writes only named Skills territory; no a_c mutation, peer-tenant donor read or private implementation exposure follows from the dependency |
| Independent Reviewer | Governing sources first, then exact candidate, proof and selected comparison; additional causal-cone material where separately authorized | Inspection can exceed published interfaces under an explicit grant; it does not authorize copying that material into Worker context or owning the repair |
| Registered a_c executor | Exact implementation/configuration needed to perform the selected operation, with granted observation/effect surfaces | Executing provider code is not automatically exposing that code as actor context; actual tool outputs still obey disclosure and information-eligibility conditions |

These are binding requirements for selected activations, not prefilled grants for
all actors. A clean-room engagement adds its exact eligible-source and derivation
policy, permitted exports, prior-exposure rules and enforcement claim. No clean-room
standing is retroactively asserted for the existing Skills construction.

The dependency does not grant access to every a_c model, source file, retained
actor output, upstream Graphify resource or transitively reachable Product. An
adequate provider contract may encapsulate its implementation dependencies. A
far-side condition material to Skills' result, authority or evidence must remain
represented and available through an authorized route. A separately authorized
inspection may investigate it without turning all internals into durable consumer
dependencies.

Returned contexts, tool outputs and summaries preserve material producer/source
identity, allowed onward use and restrictions. An export is usable only when its
owner permits disclosure and the receiving engagement admits its information and
provenance. Forwarding a prohibited implementation summary is still exposure.
Changes to read scope cannot erase exposure already delivered to an actor.

### Independent entry and operation path

Skills can be entered from its own definition and frame basis with the selected
installed methodology, provider sources/runtime, supported host, and actual
operator configuration. It requires no enclosing orchestration Product. The
Codex and Claude entry commands remain those of their own tenant designs; this
relation does not interchange their transports or assume child authentication.

For read-only discovery, the existing native setup recipe is:

```sh
stdo status --definition stdo_skills/stdo_skills.json --verify
python3 -B a_c/build_tenants/graphify/examples/fd-support/prepare_readonly.py   --out "$fresh_setup" --profile stdo-3.0.1   --product-root "$skills_root" --definition-name stdo_skills.json
```

Here `fresh_setup` names a new operator-selected output directory and `skills_root`
is the actual Skills Product root. The recipe is shown from the repository root.
Its output supplies acquisition examples only: it registers no work grant or
executor and is not the admission path for construction. This package did not run
this setup or a worker trial.

For real work, use the [native operator recipe](../../../../a_c/build_tenants/graphify/design/fd-support-stdo-3.0.1.md#real-work-policy-operator-recipe):
bind the actual owner, source refs, policy and fixed executor; assemble selected
context; obtain the actual `contract.preflight` receipt; dispatch that receipt;
observe completion and effects; capture and check the original return. The owning
contract determines each operation's result, support and refusal. No new CLI or
policy schema is introduced here.

### Failures, change and evidence

A missing/different target identity, mismatched profile/source pin, unresolved
contract, unsupported native operation, absent grant or incompatible actor/host
binding withholds the dependent action. An uncertain effect is reconciled before
retry under the provider's actual contract. Native profile selection does not
repair authentication or qualify an executor.

Skills' evidence distinguishes method semantics, provider operation, host
transport, actor output and resulting Product behavior. Evidence records the
actual subject, provider/profile/configuration and material inputs. A contract or
implementation change selects affected Skills expectations, call paths and
qualification cases. A new provider version alone changes neither the selected
old version nor the standing of historical evidence. Reuse on a new selection
requires established applicability; unknown impact keeps the dependent claim open.

A revoked operation grant stops future affected work and prompts assessment of
existing reliance. A newly excluded source already exposed to an actor triggers
the engagement's exposure disposition; deleting the file or receipt is no remedy.
Current a_c's cooperative local account is not OS confinement. Where isolation is
required, unrestricted host paths and inherited knowledge must be addressed by the
actual execution arrangement and its declared limits.

### Adoption and remaining decisions

The owner may adopt this exact relation, or a supported revision, after its
bounded review. Adoption consists of selecting the provider contract/cut and its
standing, promoting the relation to the chosen Skills-owned authority surface,
and inserting the corresponding edge with any locator adjustment. It leaves the
methodology basis and both tenant identities unchanged. Each effectful activation
still needs its own supported binding.

The remaining decisions are the selected provider's eligibility for the intended
use, the exact per-engagement grants and any clean-room policy/host assurance, and
the normal Skills delivery disposition. This draft does not resolve the recorded
Claude Q05 handoff gap or establish comparative efficiency. The companion
[acceptance cases](../../../../specification_methodology/v3/.ai-workspace/work/PRODUCT_COMPOSITION_PROPOSAL_01/ACCEPTANCE_CASES.md) name the evidence needed for this relation and the
proposed tooling extension.
