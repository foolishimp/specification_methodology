# Product composition and mediated actor information

Construction selection: owner instruction “ok implement it”, 2026-10-26;
Worker `/root/composition_ac_worker`, Executive `/root`. This design precedes
implementation; the bounded ingress/refusal detail below is aligned with the
constructed candidate. Independent review and qualification remain separate decisions.
The owning requirements are [FC-01–FC-07](../../../specification/requirements/fd-composition.md).
The existing [public support contract](fd-support.md) and
[native binding](fd-support-stdo-3.0.1.md) retain their meanings.

## Boundary and inputs

The trusted startup policy may add `composition: SourceRef`. It selects exact
bytes of an `a_c.fd-support.composition/1` document. Ordinary requests cannot add
or replace this source or its grants. Absence preserves the existing contract.
This is a finite deterministic check of already selected declarations. An F_P
actor/owner interprets source authority and context adequacy. Runtime code never
imports the mutable STDO manager or parses arbitrary prose into permissions.

The closed document has these fields:

| Field | Meaning |
|---|---|
| `schema`, `id` | Exact document kind and stable selection identity |
| `authority_sources` | Nonempty exact SourceRefs supporting the operator selection |
| `edges` | Named source/target definition pins, expected identities, selected composition index, relation and contract SourceRefs |
| `resources` | Named exact source refs, owning Product identity, `complete` provenance flag and finite `parents` resource IDs |
| `bindings` | A binding for each selected principal: engagement, purpose, route, operation/source allow lists, exclusions, eligible exports, provenance and exposure requirements, and output provenance declaration |

Edge declarations identify `source_definition`, `source_id`, `index`,
`target_definition`, `target_id`, `relation` and `contracts`. The tool reads the
selected definition's exact `composition[index]`, checks the actual target
identity and exact source/target continuity, and binds the relation/contracts to their
declared local URI and exact source. Supported local references and fragments
are checked. Remote/custom resolution is refused, not fetched. The manager's
broader fleet resolution is a separate operation with its own result.
All edge SourceRefs pin whole documents; URI fragments are checked inside those
exact bytes. The first source is the selected runtime Product definition, and
each subsequent source is the preceding exact target. Same identity with
different bytes cannot substitute at a route join.
Markdown fragment scanning excludes fenced/indented examples, comments,
escaped HTML and inline code before recognizing actual anchors. Its finite
local scanner is source-level algorithm reuse with recorded custody, not a
runtime import from the manager or a claim to render arbitrary Markdown.

Each resource has `source`, `owner`, `complete` and `parents`. Parents name
information provenance, not an access grant. Cyclic provenance is refused;
finite route cycles alone grant no additional source. Resource IDs stay stable
across changes so previous exposure can be compared to current exclusions.

Each binding has `engagement`, `purpose`, `route`, `operations`, `allow`,
`exclude`, `exports`, `require_complete`, `clean_room`, `host_isolation`, and
`output`. Route is an ordered list of edge IDs, beginning at the selected
consumer Product; adjacent target/source identities agree. Empty route means
local entry. `allow` explicitly selects resource IDs; it is not a traversal
closure. An export entry names `resource`, an exact disclosure `authority`
SourceRef and boolean `eligible`. Eligibility is the receiver's explicit
source-bound policy assertion. The tool establishes neither its semantic truth
nor the authority of whoever authored it.

`output` has `complete` and `sources`: the registered actor/executor's declared
external output dependencies, supplemented by retained mediated acquisitions
and the actual input context. It does not assert that arbitrary external code
cannot obtain undeclared information. Ordinary bindings with `require_complete:
false`, `clean_room: false` and no exclusions may retain explicitly unknown
ancestry and continue. This grants no additional source access and establishes
neither complete provenance nor source-clean F_P content. A completeness,
clean-room or exclusion policy holds on unresolved ancestry. Unknown markers
survive authored Contexts, actor delivery, output, return acquisition and future
stricter re-entry. An enforced-host-isolation request is
unsupported in this cooperative local implementation.

## One guard on the actual paths

`composition.inspect {}` returns the selected actor, engagement/purpose, route,
allowed resource IDs, binding/source digests and checked scope. It exposes no
denied registry or denied content. Without a selection it reports
`selected: false`. Discovery describes the finite supported operations.

Ordinary source/model/work projections and review acquisitions check the actual
recipient. Context assembly checks the activated target, including declared
late sources, before constructing the retained context. A requester with wider
reads cannot thereby deliver those reads to a narrower Worker. The same checks
run again at preflight and dispatch, bound to the current exact declaration.

Only explicitly supported retained-content shapes are traversed. The guard
checks the original inline sources, generated-context input and producing
actor provenance before evidence or captured returns are exposed. Unknown raw
carriers or unsupported operations refuse under the selected binding. A
content hash and an existing artifact locator are not disclosure permission.

The initial retained readback fragment is authenticated returns and actual
finalized, complete process-output envelopes. Whole Context envelopes contain
protected composition metadata and are refused; admitted actor delivery renders
their original actor body. Raw operation/history/claim carriers are refused.
Review expectation reuse requires the same stable actor and exact policy.
`work.write`, additional admission predicates/overrides/retained observations,
alternate-Context return comparisons and additional return predicates are
unsupported under this optional binding until their content disclosure
contracts are supplied. Existing unbound operations retain their old contract.
Preflight returns its disposition and fixed checks without protected recheck
metadata; observation returns a history-completeness flag without raw gaps.

Every permitted source is checked against its exact registered source selector.
An allowed whole source may supply a narrower selection; a line/pointer grant
cannot widen into the whole parent. Provenance closure is evaluated without
disclosing the excluded parents' bytes. A forbidden parent taints a derived
source unless that exact derived export is both disclosure-authorized and
receiver-eligible. It does not authorize reading the forbidden parent itself.

Currentness rechecks acquire actual source bytes rather than trusting the Git
commit label. Pinned old immutable versions remain legitimate selections;
switching a selection requires its own compatible policy/basis. Unrelated
unacquired resources do not become mandatory rereads.

## Exposure, returns and recovery

Acquisition evidence records the stable actor identity, selected declaration,
engagement/route, exact resource/provenance coordinates and prepared channel.
Existing transport flush and Context delivery observations establish actual
mediated delivery; preparation is not silently relabeled as delivery.
Prepared public responses with missing transport receipts, partial Context
writes, and reserved attempts without delivery observations are conservatively
possible exposure. A positive zero-byte Context write is distinguished from
partial delivery. The guard preserves this uncertainty instead of claiming a
clean history. Inline Context text retains its author's declared and observed
provenance, including when no SourceRef names that influence in the packet.
The rendered Context boundary reports `declared_input_provenance_complete`;
`false` retains an open fact rather than asserting clean or complete ancestry.

On a clean-room continuation, the tool queries complete protected actor history.
Previous delivered resources are assessed against current exclusions even when
the principal label or policy digest changed. Incomplete historical provenance
or uncertain relevant delivery remains a hold. Deleting a file, narrowing a
grant or changing an engagement label does not establish an unexposed actor.
A fresh eligible actor needs a separately truthful stable identity and binding.

Captured actor output retains its original bytes/producer. The output guard
combines the registered output declaration with context and delivered-source
provenance, and checks the receiving actor. It never sanitizes or substitutes
an allegedly equivalent result. Required unavailable output is a refusal with
the retained effect still observable, not a claim that the process did nothing.

Existing grant checks still own effect authority. Cancellation remains available
under its existing grant; observation/wait returns a redacted control view with
completion/termination facts and protected output references, not arbitrary
event payloads or executor arguments. Output acquisition remains independently
guarded. This permits reconciliation without reopening denied information.

## Evidence and limits

Public CLI tests exercise the actual source → context → preflight/dispatch →
late acquisition → captured return route with a registered controlled process.
They include separate Worker/Reviewer scopes, shared-route permission,
unknown/forbidden derivation, eligible export, dirty bytes, changed exclusions,
principal relabeling and redacted recovery. Existing profile tests run as
regression. No actor authentication workaround or broad generation campaign is
selected. Source pins, exact tests and residual unsupported cases are retained
under `a_c/.ai-workspace/work/PRODUCT_COMPOSITION_01/`.

The executable fixture and operator setup sequence are described in
[the composition example](../examples/fd-composition.md). `composition.inspect`
and guarded `tools.describe` enumerate this finite fragment. MCP `tools/list`
remains the static schema catalog; every call still traverses the same guard.

The declaration and host are trusted premises. This code checks a finite
source-bound information policy, not semantic compatibility, optimal context,
arbitrary hidden provenance, full-calculus conformance or OS isolation.
