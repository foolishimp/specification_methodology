# REQ-P-BASIS-AND-IDENTITY — Basis, Census, And Product Identity

Family: `REQ-P-BASIS-*`
Status: active
Category: constraint / guarantee
Design ownership: deferred independently to each registered build tenant; no
tenant design is accepted

Derives from: `../PRODUCT.md#product-identity`,
`../PRODUCT.md#product-authority`

## Purpose

Make the source corpus and every immutable assessment coordinate decidable
before a tenant representation is constructed.

## Requirements

**REQ-P-BASIS-001**: Every assessment shall select one exact installed STDO
release URI and its deterministic installed-manifest SHA-256. A mutable channel,
branch, workspace, cache entry, or unverified checkout shall not be operative
Source STDO authority.

**REQ-P-BASIS-002**: The Source STDO corpus shall contain every member of the
selected manifest's complete `standards.members` inventory in its declared
order and with its declared digest. Auxiliary release assets shall remain
provenance inputs unless Source STDO explicitly assigns them semantic authority.

**REQ-P-BASIS-003**: Acquisition shall verify the installed manifest, member
set, member order, member types, and member digests before semantic census or
tenant construction begins. Any mismatch blocks the assessment.

**REQ-P-BASIS-004**: The source census shall assign a stable source locator to
every standards member, owned normative clause, declared identity, material
term occurrence, semantic relation, required state, and refusal condition that
can change interpretation or conformance.

**REQ-P-BASIS-005**: Every material term occurrence shall resolve under the
Source STDO semantic-address tuple:

```text
(term, bounded-context identity, owning authority, selected basis, governed scope)
```

The representation may deduplicate occurrences that resolve to one concept,
but it shall preserve the occurrence-to-concept mapping and every scope in
which the resolution applies.

**REQ-P-BASIS-006**: A filename, heading, directory, glossary row, schema field,
equal spelling, or similar topology shall not create a concept identity,
bounded context, owner, relation, or equivalence. Zero or multiple lawful
resolutions shall remain explicit unresolved or ambiguous findings.

**REQ-P-BASIS-007**: The source census shall classify each standards member and
semantic surface by its Source STDO authority role, including deciding,
non-deciding index, derived compression, schema realization, template,
provenance, or other source-declared role. A derived or non-deciding surface
shall not be promoted by representation.

**REQ-P-BASIS-008**: One immutable STDO Representation Product identity shall
bind all coordinates listed by `PRODUCT.md#product-identity`, including the
exact Source STDO, Product WHAT, build tenant, carrier basis, representation
profile, artifact set, mappings, findings, evidence, and disposition.

**REQ-P-BASIS-009**: Each build tenant shall publish a stable tenant identity.
Each representation profile shall publish a distinct versioned identity and a
digest over its complete admitted profile bytes. Equal output shape across two
tenants or profiles shall not establish equal Product identity.

**REQ-P-BASIS-010**: Every external carrier basis shall be immutable and
reacquirable. Its coordinate shall identify the authoritative source, exact
version or object, governed member scope, member-set identity, and acquisition
method. A moving documentation page or package selector is insufficient.

**REQ-P-BASIS-011**: A discovery selector may locate a candidate basis but
shall not enter construction, comparison, or acceptance until it resolves to
and is accepted as an exact immutable coordinate.

**REQ-P-BASIS-012**: Every artifact, map, projection, measurement, finding,
test vector, and receipt shall bind the complete Product identity or an exact
content-addressed parent that binds it. Reuse across a different basis or
profile requires regeneration and a new identity.

**REQ-P-BASIS-013**: No tenant artifact or external carrier shall become a
second Source STDO authority. All represented meanings and relations shall
retain exact source semantic addresses even when the carrier uses different
names or structural identities.

**REQ-P-BASIS-014**: A candidate with an unresolved basis, incomplete source
census, digest mismatch, ambiguous semantic address, missing owner, or
unacquirable carrier basis shall receive disposition `blocked` and shall not be
admitted as a complete or limited Product.
