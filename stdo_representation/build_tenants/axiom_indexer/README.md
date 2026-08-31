# Axiom Indexer Build Tenant

Identity: `urn:stdo-representation:build-tenant:axiom-indexer`

Status: active thin `0.1.0` tenant; no local executable code

## Selected dependency

```text
Axiom Indexer tag object:
  e7afc8a42a7123aebe91cb7582cb037b1aae612d
peeled commit:
  dc3e00998da36dae6ac7b76b340431a85096c83c
repository tree:
  8c9ad5f5e99a60c18fb8c1802471753afb226272
Product member inventory SHA-256:
  7df380d5c41be4482f06668c5fe1043cd08643daa9f40d83be3c0ff40a8ff7e6
```

The dependency owns URI resolution, released validation, logical-map
instantiation, and pure ordered joining. This tenant does not copy or fork that
code.

## Product artifacts

```text
representation/stdo-v2.5.0-rc.1/
  axiomatic-program.json
  logical-constraint-map.json
```

The program is the LLM-authored STDO specialization of the Axiom Indexer
`a_c.text` surface. The map is the exact deterministic view produced from the
unchanged valid program and invocation-local bindings.

Runtime Binding Sets and validation reports contain installation-specific
evidence and remain outside the portable Product member set. The native skill
under `../../skills/stdo-representation/` tells Codex and Claude how to use
these artifacts and the exact dependency.

This tenant claims no complete admitted `a_c` model, GTL, GraphFunction,
automatic frame selection, deterministic prompt packet, or model runtime.
