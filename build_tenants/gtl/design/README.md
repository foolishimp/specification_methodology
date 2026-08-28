# GTL Tenant Design

Status: `STDO.gtl 0.7.0` profile proposed; its exact frozen-carrier path is
implemented and verified, but no design is accepted for production
construction.

The exact frozen carrier basis is recorded in [`GTL_BASIS.md`](GTL_BASIS.md).
The proposed direct mapping is
[`GTL_REPRESENTATION_PROFILE.md`](GTL_REPRESENTATION_PROFILE.md). Human
acceptance must bind that file's exact bytes and SHA-256 before construction.

The current candidate uses the exact frozen TypeScript `ModulePublication`
carrier and a compact programmatic semantic-index Rule configuration rather
than the non-admissible legacy `Module { graphs[] }` sketch. Version `0.7.0`
also binds the complete canonical represented-record payload into semantic
selection.

The profile maps the common closed identity universe, semantic atoms, typed
edges, and passive constraints directly into frozen GTL. It defines the
canonical `stdo.gtl` bytes, source routes, external `F_P` traversal boundary,
`F_D` structural refusals, `F_H` selection dependency, and measurement boundary.

It shall not extend GTL, define a private dialect, introduce an intermediate
graph, create a deterministic semantic evaluator, or import HoG/ABG runtime
semantics.
