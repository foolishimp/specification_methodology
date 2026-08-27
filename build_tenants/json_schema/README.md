# JSON Schema Build Tenant

Identity: `urn:stdo-representation:build-tenant:json-schema`

Status: registered; exact carrier basis, representation profile, design, and
artifacts unselected.

This tenant tests a representation made from canonical JSON instance documents
whose structural constraints are validated by an exact JSON Schema dialect.
JSON Schema is not itself the represented instance corpus, and schema validity
alone does not prove semantic fidelity.

The tenant fails closed until the basis gate in
[`design/JSON_SCHEMA_BASIS.md`](design/JSON_SCHEMA_BASIS.md) is satisfied.

Execution and runtime behavior are outside this tenant.
