# 2D label repair

The owner reported absent labels in 2D. The pinned `3d-force-graph` dimension
handler deletes each node's `z` and `vz` when changing to two dimensions. The
viewer's label loop required a finite `x`, `y` and `z`, so it hid every planar
label before projection.

The adapter now projects labels at depth zero in 2D and uses the actual node
depth in 3D. Invalid required coordinates still hide pending labels. This changes
only presentation, with no model, source, logical edge or proof alteration.

The focused regression executes the exact dimension-change handler extracted
from the hash-verified pinned renderer. [Before](before.json) fails with
`2D labels remain visible without node.z`. [After](labels-after.json) passes on
both the source viewer and actual exported ABIogenesis HTML: 3D → 2D → 3D → 2D,
zero-depth projection, and invalid-coordinate controls. Graphics/projection are
stubbed; this is an offline DOM/adapter check, not a visual WebGL observation.
All seven existing [navigation checks](navigation-after.json) also pass.
JavaScript syntax and whitespace checks pass.

The current application is
[`a_c/applications/abiogenesis-constraint-explorer/index.html`](../../../../applications/abiogenesis-constraint-explorer/index.html),
SHA-256 `ef302f3a2eba432b08f4e45cb817d01675a122916931eaf4cf394da726ab190a`.
Reload that file to use the repaired labels. [Generation](generate.json) and
[final artifact identity](final-artifact.json) bind the exact output. Its full
embedded model/source/graph data equals the predecessor. The live Skills provider
manifest refreshes only the viewer JavaScript member; its other 19 pins remain
unchanged.

The independently reviewed navigation predecessor is retained as
`previous-index.html`, with its exact JavaScript, artifact record and provider
manifest alongside it. Its review is not presented as a review of this repair.
No new independent review, browser interaction, commit, push or release was
performed for this bounded fix.
