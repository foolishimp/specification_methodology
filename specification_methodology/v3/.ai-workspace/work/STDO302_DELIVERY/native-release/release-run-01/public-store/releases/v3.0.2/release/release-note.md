# STDO 3.0.2

STDO 3.0.2 is the standalone native methodology release using the `stable-v1`
profile. Its immutable annotated tag is `specification_methodology/v3.0.2`,
its logical cut is `stdo://releases/v3.0.2/`, and its native predecessor is
published 3.0.1 RC1, commit `fe4941f56a52ed3697a2b516d8d68948b0ea65d9`.
The public installed manifest binds the exact tag, commit, trees and payload
members. No RC suffix or second mutable selector belongs to this cut.
Earlier RC-labelled cuts remain proper immutable releases with their existing
selector semantics; this release does not reclassify or move them.

The package contains the method standards and distributed `spec` plugin. Start
with the [method entry](../standards/README.md),
[templates](../standards/templates/README.md) and
[installation guidance](../plugins/spec/references/GETTING_STARTED.md#new-project).
The [licence](../LICENSE) applies. Install using the separately distributed
`stdo-toolchain 0.1.6` wheel and its checksum; the native tag does not contain
the manager's Python source package. The manifest and checksum are public
release assets. Installation preserves other installed versions and changes
no Product Definition or host plugin selection automatically.

## Changes

[Product composition](../standards/PRODUCT_DEFINITION.md#9-recursive-discovery-and-explicit-composition)
adds PC-01–PC-07: recursive independently enterable Products, leaf and composite
scope, explicit dependency contracts, integrated outcome responsibility,
route-specific authority, context eligibility and adequacy, and material
invalidation with retained history. Tenants remain realizations. Reachability
never grants transitive authority; an authorized detailed dependency inventory
is permitted without requiring every encapsulated dependency to be flattened.
The [contract template](../standards/templates/PRODUCT_COMPOSITION_CONTRACT_TEMPLATE.md)
and [worked example](../standards/examples/PRODUCT_COMPOSITION.md) make these
conditions concrete, including shared leaves, incompatible replacement,
source leakage and continuation limits.

[Release profiles](../standards/RELEASE.md#stable-cuts) now support a directly
published stable semantic-version cut alongside the conserved RC profile.
The stable line requires its explicit annotation and manifest profile, refuses
legacy selector collisions and keeps its tag immutable. Changed qualifying
bytes after stable publication require a new version. Discovery and explicit
digest-bound consumer adoption remain separate.

## Evidence and retained limits

The composition source, tooling and Skills construction received independent
review, including supported repairs, before the release increment. Native frames
are generated from their current owners. Release preparation adds targeted
stable/legacy identity checks and exact package/install verification. Public
release records bind those observations to the actual published subject.

The separate a_c/Graphify supplement covers composition clauses and the changed
release-profile contract, with exact source grounding and carrier recovery.
It is not an installed dependency and does not complete the earlier incomplete
whole-method interpretation. Mechanical recovery does not establish semantic
acceptance, optimal compression or practical delivery/cost improvement.
Whole-method qualification remains bounded by the inherited recorded evidence;
publishing this release does not assert new general qualification.

Skills' installed 3.0.1 basis, a_c's 2.5.1 construction basis and the older v2
matched cohort remain unchanged. The source repository also carries separate
manager, a_c and Skills increments; co-location does not add them to this native
payload or migrate their consumers. Adoption requires each consumer's explicit
selection and applicable compatibility assessment.
