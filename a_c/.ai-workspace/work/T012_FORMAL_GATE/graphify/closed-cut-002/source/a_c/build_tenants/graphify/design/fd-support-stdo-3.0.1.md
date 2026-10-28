# Native STDO 3.0.1 support binding

This is the bounded successor binding for the existing Graphify support tools.
Its consumer method is released `stdo://releases/v3.0.1-rc.1/`, manifest
`60356364a412dbde8cffe68fe0eda4e2749b0162acce93495534eee13b223df8`, native commit
`fe4941f56a52ed3697a2b516d8d68948b0ea65d9`. The a_c builder remains its selected
installed 2.5.1 RC2. The [profile](fd-method-stdo-3.0.1.json) pins the native
owner files. The [requirements](../../../specification/requirements/fd-stdo-3.0.1-binding.md)
own this increment's WHAT. Existing [public wire and computational design](fd-support.md)
owns the shared realization, with the changes below. This is a development
candidate, not evidence of complete calculus or ordinary actor qualification.

## Native contract mapping

| Native owner | Existing carrier/computation retained | Preservation and boundary |
|---|---|---|
| REFERENCE_FRAME §11 | Packet groups, exact source acquisition, rendered Context, actor envelope | Identity/revision, subject/basis, relations/invariants, authorities, inputs/tools, dependencies, consumer and stop/change remain explicit. Rendered byte fit is not semantic sufficiency. |
| ACTIVATION §1 Intake; EXECUTIVE_BASELINE §19 | Packet plus supplied grant and exact source references | Governed outcome, accepted transformation relations and shared-machinery dispositions belong in the supplied deciding sources/grant. The tool does not infer them or claim it checks their semantic sufficiency. Role additions retain the native Worker/Reviewer/Executive coordinates; Reviewer technical-triage capability is in generic actor capability and source references. |
| ACTIVATION §1 Admission | Product-located owner record, exact mechanism digest, grant, preconditions, preflight contract receipt | Drafting does not admit. A source-authorized operator selects the actual owner binding and grant; preflight validates that exact contract. No role/profile name or example setup grants authority. |
| ACTIVATION §3 | Closed return: evaluations, not_performed, work_result, residuals | An available report can say construction incomplete; report availability does not satisfy construction or unperformed assessment. The original actor values are preserved. Semantic legality remains an evaluation obligation. |
| ACTIVATION §7; FOUNDATIONS observation sufficiency | Original return, consumer/context coordinates, explicit observations, invalidators and dependencies | Consumers retain currentness and continuation distinctions; byte equality alone supplies no applicability claim. Existing return checks retain unknowns and compare supplied coordinates. No general context compression or future-behaviour theorem is claimed. |
| FOUNDATIONS Results; SPEC_METHOD §11 | Public operation_outcome | B(op) means the requested exact output/effect-evidence payload is available. The original cause-tagged mapping is retained with the native Results parent. Successful dispatch/observation is neither task success nor physical effect completion. |
| AXIOMATIC_CALCULUS §5 | Named domain operations and bounded predicate primitives | No blanket F_D reclassification. A native F_D claim needs its own closed domain/dependencies/outcomes/termination argument. Source acquisition and external execution remain named operations; an LLM's semantic output remains F_P. |

Example: a process times out and yields a complete observation with unknown
external completion. `dispatch.observe` may satisfy B(observe); its effect is
still unknown. An authenticated actor report of `incomplete` preserves that
construction-availability value; absent assessments stay in `not_performed`.
The operation's availability result does not convert either into success.

## Shared implementation and selected profile

The two supported profiles have curated exact id/digest pairs. Runtime carries
the selected pair from the operator policy; no caller supplies executable
profile logic. Native startup also requires the consumer Product Definition's
exact 3.0.1 release URI and manifest. Profile bytes are reacquired and hashed.
Catalogs, output parents, provenance, packet/return basis and effect replay
checks use that selected identity. RC9 history and source pins remain intact.

The common algorithms are retained because the mapped native contracts above
require the same declared coordinate and evidence relations. A future material
semantic difference requires a separately justified implementation change;
a matching carrier shape alone would not justify reuse.

All existing public operations are exposed for this bounded profile except
`results.conjoin`, which refuses `unsupported_check` and is omitted from native
CLI/MCP inventory. The only existing conjunction schema/operator is RC9-specific.
An Executive may perform its declared native F_P decision over original results;
it must not present that decision as a tool-computed native conjunction.
Models queried through record/graph operations retain their own exact model
basis; selecting this tool profile neither migrates nor accepts a model.

## Public setup and use

For source acquisition on an explicitly selected consumer, from any directory:

```sh
python3 -B "$ac_root/build_tenants/graphify/examples/fd-support/prepare_readonly.py" \
  --out "$fresh_setup" --profile stdo-3.0.1 \
  --product-root "$consumer_root" --definition-name stdo_skills.json
```

`SETUP.json` gives the exact policy path and digest; `requests/describe.json`,
`read-product.json` and `observe.json` are ready public requests. Read-only setup
registers no work grant or executor. Its mechanism coordinate uses the real
implementation digest, but the demonstration operator record is not an admitted
Product work owner. It cannot perform preflight, dispatch or authoritative writes.

```sh
python3 -B "$ac_root/build_tenants/graphify/code/ac_support.py" \
  --policy "$policy" --policy-sha256 "$policy_sha256" --principal executive \
  call --request "$request"
```

`mcp` in place of `call --request ...` serves the same full envelopes. Invoke
`tools.describe` for each selected operation's actual request and result schemas.

### Real work policy: operator recipe

The public mechanism is the existing `product-policy-preflight/1`; the policy is
trusted operator configuration, not an actor-supplied work request. Use the
[Product-bound admission contract](fd-support.md#product-bound-admission-and-exact-dispatch)
and the public schemas. The required preparation is:

1. Record the actual owner instruction, selected outcome, limits and permitted
   effects. Reference an existing Product-local JSON owner record through a
   supported URI slot in the Product Definition (for example a declared
   `reference_frame_bases` authority). The policy's `definition_locator` is the
   JSON Pointer to that exact URI. The record has `mechanism`, `result_surface`
   and `scope`; the selected mechanism source/digest names the current
   `ac_support_core.py`, and the surface names the actual protected evidence
   root, namespace and consumer. The tool verifies record/definition agreement;
   hashes do not authenticate the human who selected it.
2. Supply exact SourceRefs for the Product Definition, native profile, owner,
   role bindings and deciding task/source/evidence files. Register their roots
   and read scopes. Mark only granted Worker territory writable; keep policy,
   implementation, method and protected evidence outside that territory.
3. Register fixed principals with their actor/role/provenance and operation
   permissions. Bind an existing grant: authority_sources, outcome, authorized
   principals/targets, operations/tools, executor IDs, territory, preconditions,
   admission selection and notification sink. Its admission selection names
   the exact mechanism/source/owner, required predicates and allowed override
   sources; use empty collections only when the actual work contract requires
   none. Do not create dummy satisfied predicates or approval receipts.
4. Register the actual fixed executor: executable and digest, full argv, all
   declared dependencies, cwd/environment, actor identity, settings/tool set,
   effect scope, stdin Context mode, decoder and observations. The existing
   [actor CLI adapter](../examples/fd-support/README.md#optional-cli-transport-helper)
   can invoke either host. Preserve its fixed-plan and actual-output contract.
   Native profile selection does not qualify a provider, model or executor.
5. Freeze the complete policy bytes/digest. Public `context.assemble` consumes
   the caller-selected packet and exact sources. Public `contract.preflight`
   creates the actual admission receipt only after its checks pass.
   `dispatch.start` takes that receipt, not arbitrary argv. Observe completion;
   `return.capture` takes the actual retained final stdout and original return
   contract, followed by `return.check`. The Executive consumes these results
   and decides the next authorized action.

A complete policy has the same closed fields as the existing public contract:
`schema`, `id`, `product`, `method_profile`, `sources`, `principals`, `grants`,
`predicates`, `operators`, `executors`, `event_sinks`, `independence_policy`,
`evidence_root`, `limits`, `authority_sources`. For this profile, `operators`
may be empty; a native conjunction registration is not currently supported.
The shipped tests construct synthetic authority only inside isolated fixtures;
they are not an ordinary admission generator.

## Verification and remaining work

`test_ac_support_native301.py` exercises native public CLI discovery/source/
observation, legacy-profile rejection, exact Product-basis rejection, reassembled
activation retry refusal, material-source staleness before launch, and an actual
local subprocess through capture/check preserving an incomplete work report.
The actor is a controlled deterministic transport fixture. Existing core,
effects and CLI/MCP tests cover the retained RC9 path. Real Codex/Claude use,
semantic migration assessment, context adequacy, and Product acceptance remain
separate evidence obligations.
