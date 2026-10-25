# Selecting composition for existing support operations

The operator first establishes the existing native 3.0.1 Product/role policy
and its real operation-owner record. Composition does not create that authority.
Keep the unchanged exact native method profile and the existing source roots,
principals, grants and effect registrations. The local support module has no
runtime dependency on the STDO manager or Skills implementation.

Create a whole-document SourceRef for an operator-authored
`a_c.fd-support.composition/1` document and set it as the startup policy's
optional `composition` member. Pin the resulting policy bytes with the existing
`--policy-sha256` argument. A request cannot substitute another declaration.
The [owning design](../design/fd-composition.md) defines each closed field.

For a direct local entry, use empty `edges` and a binding with `route: []`.
For a Product edge, register both exact definitions, the source definition's
composition index, the relation and every contract; then select that edge ID
in the principal binding. Register only truthfully classified exact resources.
An allowed `summary` with parent `donor` remains excluded if `donor` is excluded,
unless an exact summary export has both an actual disclosure authority SourceRef
and receiver-policy `eligible: true`. These fields record the owner's decisions;
hash verification does not make the decisions lawful or adequate.

A read/context-only binding can select operations `composition.inspect`,
`tools.describe`, `source.read`, and `context.assemble`. No executor, effect grant,
or fabricated predicate is needed for those operations. Its output provenance
must still truthfully describe authored Context text. An ordinary F_P actor with
unknown inherited input selects `output.complete: false`, `require_complete:
false`, `clean_room: false` and `exclude: []`; unknown provenance remains explicit
through subsequent Context/return use. Known unauthorized sources still refuse.
`output.complete: true` and an empty source list assert no external domain
sources beyond retained mediated acquisitions; do not use that assertion for
an actor with unknown external input. A completeness, exclusion or clean-room
policy cannot use the unknown marker to claim eligibility. Target actor
bindings separately restrict Context recipients.

Send the ordinary request envelope through the existing CLI or MCP adapter:

```json
{"schema":"a_c.fd-support.request/1","id":"composition-scope-01","operation":"composition.inspect","arguments":{}}
```

```sh
python3 -B build_tenants/graphify/code/ac_support.py --policy POLICY.json --policy-sha256 POLICY_SHA256 --principal executive call --request REQUEST.json
```

The result identifies selection, declaration, principal/stable actor, engagement,
purpose, route and allowed resource IDs. It does not return the denied registry.
Use `source.read` with an allowed exact SourceRef. Assemble an ordinary native
packet using `context.assemble`; both requester and activated actor selections
are checked. Actor-issued late `source.read` calls use the same guard. Context
fit remains a byte-bound judgment, not semantic adequacy.

The executable test fixture shows the complete declaration and native policy
construction without importing production authority from a demo:

```sh
python3 -B -m unittest discover -s build_tenants/graphify/test_env -p 'test_ac_support_composition.py' -v
```

`test_actor_issued_late_tool_read_and_output_readback` launches a registered
controlled actor through public Context/preflight/dispatch. That actor performs
an actual late CLI read; the parent acquires its finalized output through the
guarded evidence path. The authenticated native closed-return case exercises
capture and checking separately. These fixtures are mechanical evidence, not
an instruction to trust arbitrary executors or fabricate an owner record.

Required OS confinement, unknown raw evidence carriers, generic writes and
additional evaluation ingress are refused in this selected fragment. Revocation
still permits redacted observation/cancellation under an existing lawful grant;
it does not erase prior actor exposure or make a tainted actor fresh.
