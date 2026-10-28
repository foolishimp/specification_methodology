# Build Tenants

The canonical tenant binding is `../stdo_a_c.json#/how/build_tenants`.

| Tenant | Shared WHAT | Concrete realization |
|---|---|---|
| [Graphify](graphify/README.md) | Common `a_c` implementation requirements | Exact declared model-family fragment encoded as a Graphify-compatible graph, structural checks and acquisition operations |
| [Lean/Mathlib](lean/README.md) | Common `a_c` requirements and [FR-001–FR-007](../specification/requirements/formalisation.md) | Source-linked finite formal model, generic checked closure/projection/refusal proofs and executable fixture/certificate checks |

Each tenant binds the common requirements to its computational representation
and real execution stack. It owns its design, implementation and proof surface.
No tenant becomes a separate composed Product through its directory name.
