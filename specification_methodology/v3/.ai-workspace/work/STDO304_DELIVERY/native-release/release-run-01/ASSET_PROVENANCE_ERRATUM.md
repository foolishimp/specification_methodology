# Asset receipt provenance erratum

The existing `source-preparation-001/public-download-proof.json`, SHA-256
`d371bde341b96d6f895c4dede03c506c6e2d6e26037d9f04a9534921dfdd61a8`, was produced by `native_release.py check-assets`
against the locally copied `release-run-01/public-assets/` directory. The actual
command and result are retained in `entry-asset-local-operations.json`.

**No public download occurred.** The helper's fixed filename, record kind and
`exact_downloads: true` field overstate this invocation's provenance. The
Executive admits this receipt only as exact staged-asset membership and byte
equality against `assets.json`, SHA-256
`0c87123c8f1ed5f9704750ae266bbec130d76bf756c77804ae0eeced8eeda7ad`. It supplies no public reacquisition or
publication evidence. The original receipt and carrier B
`0f8b3acd37eff9fe5df678d1d5a03ecb0fb645eb` remain unchanged.

This erratum changes no source, payload, native identity, asset byte or gate.
The original atomic plan was prepared but never executed. A successor carrier
will include this correction and final local assessments, and a new compatible
plan directory will bind that carrier without replacing the original plan.

After publication, actual HTTP downloads and their transport receipts must be
retained. `check-assets` will then run in a separate fresh compatible public
check directory against those downloaded files. Only that independently bound
receipt can support the public-download claim. Local installation and retained
qualification limits are unaffected.
