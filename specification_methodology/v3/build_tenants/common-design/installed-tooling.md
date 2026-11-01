# Installed tooling design

Implements [TOOL-01–TOOL-05](../../specification/requirements/INSTALLED_TOOLING.md)
with the existing native manifest and manager. `standards/tooling/` holds exactly
`sources.zip`, `TOOLING.json`, `materialize.py` and `README.md`. The archive avoids
treating imported historical Markdown references as current standards routes.
It preserves the original relative source layout; no runtime API is changed.

The explicit [selection](../common-tools/tooling-selection.json) binds 191 regular
files and their Git modes, blobs, sizes and SHA-256 identities at
`9c9626ffd20ea88a75ac8143802c13f4f828ec1c`: current Graphify and Lean tenants,
both Skills packages, their common contract/provider files, and the native STDO
license. Vendored renderer licenses/notices are preserved. Historical work
records, private origin, caches, virtual environments and binaries are excluded.
The sole work-record exception is the public current Skills T-003 ticket,
required by the unchanged Codex package's current source-route pin. It supplies
no executable import or new authority. Source tests remain reference material; unsupported fixture/host closures are
not advertised as runnable. The two package checks are a declared finite subset.

[tooling.py](../common-tools/tooling.py) constructs a deterministic ZIP from
that exact Git cut, refusing a mismatched working source. It verifies installed
payload against the selection, guide and materializer implementation. The fixed inventory commitment also refuses a self-consistent narrowed source
archive claiming the selected commit. The
standalone [materializer](../common-tools/tooling_materialize.py) uses only
Python's standard library. Its installed copy checks the whole bundle, exact
member set, duplicate/case/Unicode identities, sizes, regular modes, digests
and file/directory collisions before creating any output. It refuses existing
targets, traversal, symlink ancestors and overlap with the immutable release.
Existing destination ancestors are compared by filesystem identity; case and
Unicode aliases cannot bypass the installed-root boundary.
The absent output must have an existing canonical parent. Extraction uses
exclusive creation and verifies the resulting pristine tree.

The normal manager's manifest authenticates the complete bundle, including its
inventory and verifier. This is custody, not a signature or trust bootstrap for
arbitrarily substituted verifier/inventory pairs. The finite archive is bounded
to 512 files and 64 MiB uncompressed. Concurrent hostile mutation of a selected
writable parent is outside this local materialization contract.

After extraction, the user selects mutable output and dependency environments.
The direct project representation path uses stdlib Python and its explicitly
selected manager. Optional code extraction binds the existing pinned Graphify
Git checkout and parser environment; no subject/test code is executed. The
Lean source package includes public support manifests but not the previously
qualified 3.25 GB Darwin-arm64 support tree. Bootstrap is explicit and runs
only in the writable copy. No fresh-machine proof execution is asserted.

`native_release.validate_payload` requires both documentation and tooling gates.
The normal release assets remain the native manifest and manager wheel with
checksums; the installed ZIP is not a separate optional release asset. A fresh
disposable real-manager installation qualifies all member bytes, logical
resolution, source-independent materialization, public CLI build/reuse and
refusals. Independent review precedes release; this preparation creates no main
repository tag, release object, public artifact or consumer adoption.
