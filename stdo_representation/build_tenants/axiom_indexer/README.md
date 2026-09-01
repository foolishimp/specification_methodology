# Axiom Indexer Build Tenant

Identity: `urn:stdo-representation:build-tenant:axiom-indexer`

Status: active STDO Representation `2.5.0` tenant; no local executable code

## Selected dependency

```text
Axiom Indexer exact immutable cut:
  v2.5.0-rc.4
qualified ref:
  refs/tags/axiom_indexer/v2.5.0-rc.4
publication state:
  published in the coordinated atomic RC4 cohort
tag object:
  4750e09639c118f1097d4ea046fe23d26713f96b
peeled commit:
  a953ad4634fbfaefb8bdffaccdf4eff651a1e3a2
repository tree:
  093302db57bfb2e7beeed7f02dfc6d7090921a15
Project Subtree tree:
  3f71c3c2df99008b9521e338a7837c553f87173a
Product member inventory SHA-256:
  7df380d5c41be4482f06668c5fe1043cd08643daa9f40d83be3c0ff40a8ff7e6
executable SHA-256:
  dfb4d7f1e6b06b9c215154a00b689ce82d7cd36e1ec80ee8f93da9c20798b672
```

The dependency owns URI resolution, released validation, logical-index
instantiation, and pure ordered joining. This tenant does not copy or fork that
code.

During the completed coordinated two-commit construction, the sibling
`../../../axiom_indexer/` checkout supplied the exact seven-member candidate
mechanics above. That bounded use is construction evidence, not the immutable
dependency. Ordinary and release use require the annotated cut, its exact
commit-B coordinates, and the same member inventory.

## Product artifacts

```text
representation/stdo-v2.5.0-rc.4/
  axiomatic-program.json
  logical-constraint-map.json
```

The program is the LLM-authored STDO specialization of the Axiom Indexer
`a_c.text` surface and is the semantic compression. The map is the exact
deterministic constraint index produced from the unchanged valid compression
and invocation-local bindings. These published-cut artifacts represent exact
Source STDO `v2.5.0-rc.4`; publication and validation do not by themselves
accept the Product.

Runtime Binding Sets and validation reports contain installation-specific
evidence and remain outside the portable Product member set. The native skill
under `../../skills/stdo-representation/` tells Codex and Claude how to use
these artifacts and the exact dependency.

This tenant claims no complete admitted `a_c` model, GTL, GraphFunction,
automatic frame selection, deterministic prompt packet, or model runtime.
