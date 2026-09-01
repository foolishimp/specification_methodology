# REQ-P-RELEASE-COUPLING — Exact Cut Alignment

Family: `REQ-P-RELEASE-COUPLING-*`
Status: Active

Derives from: `../PRODUCT.md#coordinated-release-identity`

**REQ-P-RELEASE-COUPLING-001**: Every successor Axiom Indexer release shall
select one exact immutable Source STDO cut and installed-manifest digest before
candidate qualification.

**REQ-P-RELEASE-COUPLING-002**: The Axiom product-local cut suffix shall equal
the selected Source STDO cut suffix. The Axiom cut shall use the distinct
`axiom_indexer` Project Release Namespace and shall preserve separate Product,
member, claim, review, and acceptance identities.

**REQ-P-RELEASE-COUPLING-003**: The Axiom Product inventory shall contain only
the generic resolver, validator, map-instantiation, joiner, schema, and native
interface declared by its release record. A sibling semantic program or
logical map shall not become an Axiom Product member through co-location or
coordinated version text.

**REQ-P-RELEASE-COUPLING-004**: A downstream STDO Representation release shall
bind the exact released Axiom cut used to validate and instantiate its
source-linked semantic program. Source STDO changes shall cause that Product to
re-author affected semantic entries and regenerate its map under its own
authority.

**REQ-P-RELEASE-COUPLING-005**: Candidate qualification shall verify the exact
installed STDO basis, the coupled cut identity, the complete Product member
inventory, normal and optimized implementation tests, project-qualified ref
profile, and exclusion of sibling semantic assets.
