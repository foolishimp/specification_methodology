# REQ-P-BASIS-AND-IDENTITY — Basis And Index Identity

Family: `REQ-P-BASIS-*`
Status: Active
Category: Constraint / Guarantee
Design ownership: deferred independently to each registered build tenant; no
tenant design is accepted

Derives from: `../PRODUCT.md#product-identity`,
`../PRODUCT.md#product-authority`

## Purpose

Bind each reusable Programmatic Semantic Index Product to exact immutable
source, Product, tenant, carrier, profile, and content coordinates without
making a workspace invocation or qualification record part of index identity.

## Requirements

**REQ-P-BASIS-001**: Construction shall select one exact installed Source STDO
release URI and its deterministic installed-manifest SHA-256. A mutable channel,
branch, workspace, cache entry, or unverified checkout shall not be operative
Source STDO authority.

**REQ-P-BASIS-002**: Construction shall verify every member of the selected
manifest's complete `standards.members` inventory in declared order and against
its declared digest before deriving index content. Auxiliary release assets
remain non-semantic unless Source STDO assigns them another role.

**REQ-P-BASIS-003**: Every representation profile shall bind one exact build
tenant and immutable carrier basis. A discovery selector may locate a candidate
basis but shall not enter construction until resolved and explicitly selected as
an exact coordinate. The carrier-basis coordinate shall contain at least the
repository identity, immutable commit, authority root, authority-tree identity,
and exact authority inventory. Its tenant-owned typed identity shall be the
SHA-256 of the RFC 8785 canonical coordinate bytes.

**REQ-P-BASIS-004**: Every represented semantic atom, edge, and constraint shall
carry or resolve to its exact Source STDO semantic address and acquisition route.
A filename, heading, lexical match, directory, glossary row, carrier label, or
graph position shall not invent semantic identity.

**REQ-P-BASIS-005**: Equal spelling across bounded contexts shall not establish
equal meaning. Every material semantic address preserves its term, bounded
context, owning authority, selected basis, and governed scope coordinates, or an
exact Source STDO relation that supplies them.

**REQ-P-BASIS-006**: Every common identity coordinate and Product coordinate
shall use RFC 8785 JSON Canonicalization Scheme bytes over an I-JSON-compatible
value. A raw parser shall reject duplicate object names before canonicalization.
Strings shall enter JCS as their exact Unicode scalar values without a separate
normalization pass. The governing coordinate schema decides value types and
array order before JCS; an implementation default shall not.

**REQ-P-BASIS-007**: The canonical carrier bytes shall be content-addressed
before Product identity is issued. The Product WHAT member set and coordinate
object shall use the exact ordering and canonicalization defined by
`PRODUCT.md#product-identity`:

```text
program_content_identity = sha256(canonical_index_bytes)
```

`program_content_identity` names the canonical encoding of the Source STDO
Symbolic Axiomatic Program. It does not identify or imply a frozen-GTL
`GtlProgram`.

The immutable `urn:stdo-representation:product:sha256:<digest>` identity then
binds exact Source STDO, Product WHAT, tenant, carrier basis, representation
profile, and `program_content_identity`.

**REQ-P-BASIS-008**: Construction, validation, measurement, qualification,
acceptance, release, and invocation records shall point to the Product identity.
The Product identity shall not include the identities or digests of records that
can exist only after that Product has been constructed.

The canonical index may embed the pre-content Product coordinates. It shall
not embed its own final content digest or Product identity. The release manifest
binds those values after canonical index bytes exist.

**REQ-P-BASIS-009**: A workspace input, reasoning intent, selected invocation
frame, model, prompt, response, token price, and usage record are invocation
coordinates. They shall not alter or substitute for Programmatic Semantic Index
Product identity.

**REQ-P-BASIS-010**: No tenant index, carrier type, generated graph identity,
constraint, source map, validation result, or LLM response shall become a second
Source STDO authority. Source-owned meaning remains reachable through exact
semantic addresses.

**REQ-P-BASIS-011**: A wrong or unresolved Source STDO basis, carrier basis,
profile identity, source address, or canonical content digest shall refuse
construction or structural admission. It shall not be converted into a
probabilistic semantic guess.

**REQ-P-BASIS-012**: A tenant profile shall name the exact canonicalization
algorithm for its complete carrier bytes and every identity coordinate. If the
carrier adds framing bytes such as a final line feed, the profile shall state
whether those bytes enter content identity. Competing escaped, normalized,
ordered, or whitespace variants shall refuse rather than acquire rival identity.
