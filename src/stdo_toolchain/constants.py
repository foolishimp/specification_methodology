"""Shared protocol constants."""

OFFICIAL_REPOSITORY = "https://github.com/foolishimp/specification_methodology.git"
REGISTRY_KIND = "stdo.install-registry"
REGISTRY_VERSION = 1
MANIFEST_KIND = "stdo.installed-release-manifest"
MANIFEST_VERSION = 1
PRODUCT_DEFINITION_KIND = "stdo.product-definition"

BOOTSTRAP_START = "<!-- STDO_BOOTSTRAP_START -->"
BOOTSTRAP_END = "<!-- STDO_BOOTSTRAP_END -->"
BOOTSTRAP_TEXT = """## STDO Bootstrap

This scope is routed by an STDO Product Definition Overlay.

Before constitutional work:

1. Resolve the applicable `stdo_<label>.json` for the requested Product scope.
2. Use `constitution.stdo.basis`, not its mutable selector, as the operative basis.
3. Resolve and verify that exact installed release through the STDO toolchain manager.
4. Load the Product Definition's declared bootstrap entrypoint, then exact owning standards as needed.
5. Fail closed when no Product Definition or more than one applicable definition remains.

Mutable methodology source, another installed version, a cache entry, and this
bootstrap cannot replace the exact basis selected by the Product Definition."""
