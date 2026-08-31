# JSON Schema Carrier Basis

Status: unselected; construction is blocked

Before representation-profile design is accepted, this tenant must select and
record:

- the exact JSON Schema dialect and canonical dialect URI;
- immutable normative specification and metaschema acquisition coordinates;
- the exact vocabulary set and required assertion behavior;
- the JSON data model and canonicalization basis used for artifact identity;
- format-assertion behavior and any non-portable validation checks;
- implementation-independent conformance cases; and
- lifecycle and invalidation conditions.

The STDO Product Definition schema's use of Draft 2020-12 does not implicitly
select that dialect for this tenant. A locally installed validator, moving web
page, package default, or familiar `$schema` value is not an accepted immutable
carrier basis.
