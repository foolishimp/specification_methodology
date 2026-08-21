<!-- STDO_BOOTSTRAP_START -->
## STDO Bootstrap

This scope is routed by an STDO Product Definition Overlay.

Before constitutional work:

1. Resolve the applicable `stdo_<label>.json` for the requested Product scope.
2. Use `constitution.stdo.basis`, not its mutable selector, as the operative basis.
3. Resolve and verify that exact installed release through the STDO toolchain manager.
4. Load the Product Definition's declared bootstrap entrypoint, then exact owning standards as needed.
5. Fail closed when no Product Definition or more than one applicable definition remains.

Mutable methodology source, another installed version, a cache entry, and this
bootstrap cannot replace the exact basis selected by the Product Definition.
<!-- STDO_BOOTSTRAP_END -->
