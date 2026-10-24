# Native preparation working readback

Root independently read the complete `native_release.py` (SHA256 `2fb80545cdad39ce44ca4d9713949f5c21a81c79177a46f81635e00e9a6d5c4c`) and its executable recipe after the native Writer returned. The root did not author this harness. This is a same-family nonauthor working readback of release mechanics, not the covering method review or owner acceptance.

Result: satisfied for the bounded predicate that the prepared mechanism is suitable for the selected source-to-native staging and verification path. No actionable defect found in the inspected scope.

The inspection followed immutable source blobs and modes through the alternate-index recipe, native root/parent/source-trailer checks, exact annotated-tag text and peel, canonical manager manifest, complete installed-byte comparison, asset pinning, explicit-lease atomic publication plan, and direct remote objects/peels/download checks. It confirmed that the helper performs only read-only Git operations and leaves all Git effects, installations and publication to the separately activated Root Writer. Existing outputs are preserved. The existing native RC1 manifest confirms the logical `releases/v<version>.md` source-path convention used by the independent manifest construction.

The 20 supplied source-independent controls were rerun with `python3 -I -S -B test_native_release.py`; all passed. They include nonregular Git modes, unexpected root members, altered parent/tag standing, source/manifest/installed-byte changes, stale passing verifier evidence and output redirection. The controls created only their synthetic scratch fixtures.

Actual native projection, tag, manifest production, isolated installation, fresh-actor use and publication were still unperformed at this readback. The later execution receipts must establish those boundaries. Source-to-representation semantics and exact owner acceptance remain outside this result.
