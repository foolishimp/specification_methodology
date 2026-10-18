# Build Tenants

The canonical tenant binding is `../stdo_a_c.json#/how/build_tenants`.

| Tenant | Shared WHAT | Concrete realization |
|---|---|---|
| [Graphify](graphify/README.md) | Common `a_c` implementation requirements | Exact declared model-family fragment encoded as a Graphify-compatible graph, structural checks and acquisition operations |

Each tenant binds the common requirements to its computational representation
and real execution stack. It owns its design, implementation and proof surface.
No tenant becomes a separate composed Product through its directory name.
