# Axiom Indexer Build Tenant

Identity: `urn:stdo-representation:build-tenant:axiom-indexer`

## Selected dependency

Use the exact RC5 Axiom Indexer dependency and full seven-member inventory
bound by [the Representation release record](../../releases/v2.5.0.md) and
[cohort carrier](../../../stack_release.json). Those records own the exact
source, executable, schema, output contract and cut identities. This tenant
contains no local executable, copied validator or second materializer.

Axiom owns resolution, validation, logical-index generation, explicit
reference-only/materialized projections and exact ordered text joining.
An LLM authors and selects semantics; code follows declared references.

## Product artifacts

```text
representation/stdo-v2.5.0-rc.5/
  axiomatic-program.json
  logical-constraint-map.json
```

The program is the canonical authored semantic compression; its map is a
deterministic index over that unchanged program. Local bindings, source-corpus
records and validation reports supply external exact-source evidence.
The complete [native skill](../../skills/stdo-representation/SKILL.md) provides
the installed route. A dogfood directory is not a runtime dependency.

## Selected frame-index construction

The [semantic design](FRAME_INDEX_PROJECTIONS.md) binds two overlapping
complete-update Worker/Reviewer indexes, shared rules, supporting premises,
conditions, exceptions and residuals. The current published/candidate subject
is identified by the exact release record; earlier authored runs retain their
own evidence. Applicable task facts, semantic judgments, independent review
and owner rulings remain external to the deterministic projections.

No complete admitted `a_c` model, automatic frame selection, GTL,
GraphFunction or model runtime is claimed by this tenant.
