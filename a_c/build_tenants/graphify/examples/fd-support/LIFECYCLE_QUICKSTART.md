# Lifecycle quickstart: Executive, Worker and Reviewer

Status: provisional candidate written by the T-008 Worker under grant `urn:a-c:grant:T008:guide:001`;
not reviewed, disposed or accepted. The tools report "provisional construction; independent
integrated qualification and owner acceptance pending", and REQ-AC-FD/FDV remain Deferred.

This page maps one bounded software task onto the public operations. What roles, results,
admission, independence and acceptance mean stays with the method owners listed in the
[tenant HOW](../../design/fd-support.md); this page does not restate them.

## Ground rules

- A trusted operator starts each process with an exact policy, its SHA-256 and one fixed
  principal ([setup](README.md)). No request changes policy, principal, grants, executors or
  territory, and a role name grants nothing.
- Every call is one envelope `{schema, id, operation, arguments}` in integer-only JSON; unknown
  fields refuse. Reuse an `id` only for an exact, already-authorized retry.
- `status` is transport only (`ok`/exit 0, `refused`/2, `error`/1). `operation_outcome.core_value`
  `satisfied` meets only that operation's stated output-availability predicate, never task success.

## 1. Executive: discover, bind, hand off

1. **Discover.** `tools.describe` with `{"operation": "<name>"}` returns that operation's exact
   schemas, effect flag, prerequisites, refusal codes and `unsupported` list. Read it first.
2. **Bind.** `workspace.observe` the exact scopes (an absent file reports `exists: false`) and
   `source.read` each deciding source with `encoding: "utf8"`. Keep the Observation ref from
   `result.artifact`. A SourceRef `sha256` names the whole parent; a `selector` only narrows reads.
3. **Assemble.** `context.assemble` takes `packet` (`activation`, `frame`, `subject_basis`,
   `attention`, `actor_authority`, `evidence_relations`, `stop_change`, one-role
   `profile_additions`), `models`, `sources`, `late_acquisition` and `envelope`. Its
   `boundaries.activation_identity` is the activation coordinate the actor must return.
4. **Hand off.** `contract.preflight` (`context`, `grant_id`, `executor_id`, `result_key`,
   `observations`) checks the packet against an existing grant and cannot mint one.
   `dispatch.start` (`preflight`) rechecks preimages, then launches the registered executor;
   follow it with bounded `events.wait` or `dispatch.observe`.
5. **Expose proof.** Name exact SourceRefs and a structured ReviewClaim `{id, candidate_sources}`
   in the Reviewer packet, so the Reviewer acquires source and proof itself, not a summary.

## 2. Worker: acquire, observe, write once, return

1. `source.read` (utf8) the TASK, instructions, grant and ReturnContract the packet names. A
   base64 copy inside the Context is not acquisition.
2. Take your own `workspace.observe` of target and sources. Observations stay bound to the policy
   that made them; the Executive's are not your Writer currentness.
3. `work.write` the granted target only (example below). `sha256: null` demands an absent preimage;
   a present file, changed basis or missing premise refuses. Never switch target or retry silently.
4. Re-acquire the postimage with `source.read` at the returned hash, and the write's operation
   evidence with `evidence.read`.
5. Return one `a_c.fd-support.closed-return/1` object: `schema`, `id`, `frame`, `activation`,
   `subject`, `basis`, `actor`, `consumer`, `evaluations`, `not_performed`, `work_result`,
   `residuals`, `invalidators`. `candidate_ready` needs the exact candidate SourceRef plus actual
   transition evidence; otherwise report `incomplete`, `refused` or `re_entry_requested`.

## 3. Reviewer: expectations before candidate bytes

1. `review.prepare` with `phase: "expectation"`, the `claim`, governing `sources`,
   `candidate: null` and an `expectation_body` (`text`, `source_inputs`) records source-derived
   expectations first. All eight argument keys are required; pass `null` or `[]` where unused.
2. A later activation uses `phase: "candidate"` with the same claim, the exact `candidate`,
   `proof`, a `comparison` or `null`, and the earlier `expectations` ArtifactRef. Prior exposure
   is reported; unobserved exposure stays unknown.
3. Diffs and binding checks are not findings. Findings, severity and recommendations are the
   Reviewer's F_P output in its own closed return.

## 4. Executive: capture, check, choose

`return.capture` authenticates only final output from the registered dispatched Attempt.
`return.check` reports binding, currentness, duplicate and conflict findings; `results.conjoin`
runs only a registered `claude-rc9.conjunction/1` plan. The caller then selects the next
already-authorized action; no check result selects it.

## Full-envelope usage reference

From `a_c/`; `call` prints one response object and `mcp` serves the same operations:

```sh
python3 build_tenants/graphify/code/ac_support.py --policy "$POLICY" --policy-sha256 "$POLICY_SHA" --principal "$PRINCIPAL" call --request req.json
python3 build_tenants/graphify/code/ac_support.py --policy "$POLICY" --policy-sha256 "$POLICY_SHA" --principal "$PRINCIPAL" mcp
```

Discover with `{"schema": "a_c.fd-support.request/1", "id": "exec-describe-001", "operation":
"tools.describe", "arguments": {"operation": "work.write"}}`. The write that created this file:

```json
{"schema": "a_c.fd-support.request/1", "id": "w022-write-guide", "operation": "work.write",
 "arguments": {"grant_id": "urn:a-c:grant:T008:guide:001", "mode": "replace", "interpretation": null,
  "target": {"engine": "workspace-regular-file", "root": "product", "object": null, "sha256": null,
   "selector": null, "path": "build_tenants/graphify/examples/fd-support/LIFECYCLE_QUICKSTART.md"},
  "record": {"text": "<this file's bytes, elided>", "provenance": {"engine": "workspace-regular-file",
   "root": "product", "path": ".ai-workspace/qualification/t008/live-binding-001/TASK.md", "object": null,
   "selector": null, "sha256": "6d777ece58832ec57185f47cbe69f714222329e600b3a190acac63d7d744fff2"}},
  "observations": [{"id": "sha256:96e3ffd13f76ecedb20dedb8443abb468c0d791bad4da4aa60eaf036465a68c4",
   "sha256": "96e3ffd13f76ecedb20dedb8443abb468c0d791bad4da4aa60eaf036465a68c4"}]}}
```

In `mcp` mode each tool takes this same envelope as input (this guide's authoring run used the `ac`
server's `source_read` tool with `operation: "source.read"`). "MCP server/discover" is unsupported.

## Keep four kinds of output apart

| Kind | From | Establishes | Never establishes |
|---|---|---|---|
| Exact-byte/structural evidence: hashes, Observations, `operation_outcome`, refusals, diffs, an `F_D[v]` judgment from `checks.evaluate` | the tool | these bytes, this shape, one finite registered predicate on its basis | fitness, attention, independence, acceptance |
| Performed F_P judgment: a closed-return evaluation (`predicate`, `domain_outcome`, `core_value`, `evidence`, `residuals`, `invalidators`) | the Worker or Reviewer that performed it | that actor's judgment on its stated subject and basis; unperformed ones sit in `not_performed` with no verdict | anyone else's agreement |
| Recommendation: a Reviewer finding or proposed change | the Reviewer | evidence for the owner | any change before its owner acts |
| Owner disposition | Root `/root` for this task; the Product owner for acceptance and release | the decision at that boundary | the other boundary: task disposition is not Product acceptance |

## Effects and currentness

- Only the Worker/Writer holding the named grant may mutate its named target, via `work.write`;
  Executive and Reviewer acquire and assess only.
- Expectations precede candidate bytes; the order is observed per principal and claim, and fresh
  contexts or one model family certify no independence. The caller selects each next action.
- `held(effect)` or `error` (e.g. `effect_completion_unknown`) means the effect may or may not have
  happened: acquire actual state first. A timeout or cancel proves neither completion nor
  rollback; another dispatch needs explicit `retry_of` plus the grant's reconciliation predicate.
- Each dependent effect rechecks its observations and refuses on drift, naming the changed
  premise. Git HEAD is metadata, not current bytes.

## Unsupported and qualification boundaries

- `tools.describe` lists as unsupported: other method cuts, semantic sufficiency certification,
  inferred semantic edges, arbitrary executable predicates, OS sandboxing, external producer
  authentication, MCP server/discover, and benefit or acceptance claims.
- Registered processes are not OS-confined; the deployment is a cooperative local account. Hashes
  identify bytes but do not authenticate who wrote a grant; pasted or externally run output stays
  unauthenticated evidence.
- This guide claims no savings, quality gain, complete calculus, adoption or release. Its review
  and Root's disposition are separate later steps.

## Sources acquired for this guide

- [TASK](../../../../.ai-workspace/qualification/t008/live-binding-001/TASK.md) `6d777ece58832ec57185f47cbe69f714222329e600b3a190acac63d7d744fff2`
- [Product](../../../../specification/PRODUCT.md) `9ebc8342affe8c5e0afb08ebe22f3f98f73f7bdc64db00eee17674c47274bef7`, [FD requirements](../../../../specification/requirements/fd-support-tools.md) `e3fcebd7e9fbc60dc36ed4c02ee834a96f14226af134809c938169d4712dfc23`, [FDV requirements](../../../../specification/requirements/fd-support-verification.md) `3746e614a5ddc3f0a551e926998f16d6101cc037c5c43b879b4447b017a8dbdf`
- [Tenant HOW](../../design/fd-support.md) `faefdf2432759859780d962ca1028f44f7ebca9a5f6a11c324c27ddc258d521f`: Public wire grammar, Returned actor payload, Packet carrier, Returns, review and qualified checks, Role-specific return contract
- [Setup](README.md) `eca9c4cbfbd7ad4b712a7d1e8fc73f8cec42b0fb196967b77890833997018f94`
- `tools.describe` for `work.write` and `workspace.observe`: method profile `urn:a-c:fd-support:method:claude-rc9:executive:1` `bdb937545c13d2cea8eaa93507102cff7c2ea41ca0fc169a8ec84c81003dc7d1`, builder STDO v2.5.1-rc.2 manifest `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`
