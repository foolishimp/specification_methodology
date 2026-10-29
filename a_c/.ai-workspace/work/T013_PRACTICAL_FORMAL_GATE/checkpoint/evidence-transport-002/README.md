# Successor exact public-evidence transport

This maps 24 public compiled proof files to two deterministic gzip payloads:
the original ten aliases, four reuse-qualification aliases, eight actual-path
aliases and two installed-package aliases. All original raw files remain in
place. The original transport and its historical closure remain unchanged.
Compression preserves remote byte custody; it creates no proof or new result.

`SELECTED.json` binds every T013-relative path, raw byte count, raw SHA-256 and
the exact original manifest that records it. `PREPARE.json` records complete
byte comparison. `ROUNDTRIP.json` records restoration into an absent disposable
tree, exact byte/hash comparison, repeated verification without inode/mtime
changes, and final comparison with the unchanged originals.

| Public payload | Exact raw bytes | Compressed bytes | Aliases |
| --- | ---: | ---: | ---: |
| `GateLocalNames.olean.private`, `6a2baff9b75dbe94…` | 118,435,848 | 27,954,126 | 12 |
| `GateExternalNames.olean.private`, `e4a66c78c10f6a71…` | 109,636,952 | 26,206,415 | 12 |

The mapped raw total is 2,736,873,600 bytes; the two unique compressed payloads
total 54,160,541 bytes. They are byte-identical to transport001's payloads and
each is below the conservative 95 MiB remote-file bound. The source guard keeps
the previous `lean/` and `reuse/` rule and adds only the ten literal new
`real-use/` and `package/` aliases in `GUARD-SELECTION.json`. It admits no new
prefix. `TRANSPORT-DELTA.patch` shows the complete mechanism change.

Thirteen small controls cover exact new paths, nearby/unlisted paths, traversal,
private components, case variants, symlinks, payload and output bounds, filesystem
overlap, existing-target conflicts and repeated no-overwrite restoration.
Canonical paths, forbidden components, size/hash checks and restore mechanics
are otherwise unchanged. `.olean.private` names public Lean compiled evidence;
private origin selections, keys, stores and support caches are not transported.

## Restore the exact frozen evidence

Use the manifest hash authenticated by the independently reviewed checkpoint,
not a hash obtained only from an untrusted payload. From this directory, set
`ABSOLUTE_T013_ROOT` to the destination checkout's T013 work directory:

```sh
python3 -B transport.py verify --transport payload \
  --manifest-sha256 7846c894f88b08f4ed9a772578339e4ced67af5bdca5ec843711a141452f12ea

python3 -B transport.py restore --transport payload \
  --manifest-sha256 7846c894f88b08f4ed9a772578339e4ced67af5bdca5ec843711a141452f12ea \
  --destination ABSOLUTE_T013_ROOT

python3 -B transport.py verify --transport payload \
  --manifest-sha256 7846c894f88b08f4ed9a772578339e4ced67af5bdca5ec843711a141452f12ea \
  --originals ABSOLUTE_T013_ROOT
```

The standard-library tool needs Python 3.11+ and atomic hard-link support.
Absent targets are restored with bounded decompression and atomic no-replacement
publication. Existing identical targets are verified without rewriting; any
conflicting target refuses before creating missing outputs. Partial restoration
can leave exact completed files, which a later invocation verifies. Keep inputs
and destinations quiescent; hostile concurrent host mutation is outside scope.

`COVERAGE.json` binds the final filename/stat population and exact appended
ignore lines. There are no wildcard exclusions. No source, log, JSON or proof
meaning is omitted. Every original raw artifact stays local and reconstructible.
This closure supplies transport readiness; independent review and an authorized
Git checkpoint are separate operations.
