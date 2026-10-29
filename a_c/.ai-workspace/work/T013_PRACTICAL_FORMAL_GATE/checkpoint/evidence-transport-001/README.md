# Exact oversized-evidence transport

Ten existing T013 compiled proof files exceed Git's 100 MiB per-file boundary.
This transport preserves their exact bytes in two deduplicated gzip payloads.
Every original remains unchanged locally. Source, logs, JSON, prior manifests
and evidence meaning are not excluded or rewritten. Compression is remote byte
custody, not a replacement proof, fresh gate result or release.

`SELECTED.json` binds the ten original T013-relative paths, raw SHA-256 values
and sizes. Eight have matching existing public-run manifest pins. The two
`correction-011` members are directly hash-bound; that directory's `SOURCES.json`
is retained as historical context, not misrepresented as a prior compiled-member
pin. The selected input digest is:

`622acb13cd10c2ad0d736bf1db33767607248bc9b89f4c5ad4eea3a92b22bedd`

The trusted transport manifest is `payload/MANIFEST.json`, raw SHA-256:

`59732cdb8f956e07ecc1734c63e5c29b3281f8047c4c58b4e5211409a24635ea`

| Raw SHA-256 prefix | Exact raw bytes | Compressed bytes | Original path occurrences |
| --- | ---: | ---: | ---: |
| `6a2baff9b75dbe94` | 118,435,848 | 27,954,126 | 5 |
| `e4a66c78c10f6a71` | 109,636,952 | 26,206,415 | 5 |

All 1,140,364,000 mapped raw bytes are carried by 54,160,541 compressed bytes.
Each compressed file is below the tool's conservative 95 MiB limit. The tool
refuses oversized compressed members; it does not split or omit them silently.
Compression uses stdlib gzip, level 9, no filename and timestamp zero. Python
and zlib versions and the exact compression-writer digest are recorded. Synthetic
tests reproduce identical compressed bytes on this selected implementation;
other zlib versions need only decompress to the exact raw identity.

## Verify and restore a fresh checkout

Use the source-reviewed `transport.py` and the manifest hash from the independent
checkpoint handoff. A digest supplied only by the same untrusted transport does
not authenticate it. No network, installer, proof assistant or extra dependency
is needed; Python 3.11+ and a filesystem supporting atomic hard links suffice.

From this directory, replace `ABSOLUTE_T013_ROOT` with the new checkout's exact
`a_c/.ai-workspace/work/T013_PRACTICAL_FORMAL_GATE` path:

```sh
python3 -B transport.py verify --transport payload \
  --manifest-sha256 59732cdb8f956e07ecc1734c63e5c29b3281f8047c4c58b4e5211409a24635ea

python3 -B transport.py restore --transport payload \
  --manifest-sha256 59732cdb8f956e07ecc1734c63e5c29b3281f8047c4c58b4e5211409a24635ea \
  --destination ABSOLUTE_T013_ROOT

python3 -B transport.py verify --transport payload \
  --manifest-sha256 59732cdb8f956e07ecc1734c63e5c29b3281f8047c4c58b4e5211409a24635ea \
  --originals ABSOLUTE_T013_ROOT
```

Restore reconstructs exact absent files at their original relative paths. It
only verifies existing identical files and refuses any differing file before
creating missing outputs. It never overwrites. All compressed streams and
existing targets are checked first. New data is decompressed with a declared
output bound into a temporary regular file, then atomically linked to the absent
destination without replacement. A partial failure may leave already completed
new files; rerunning verifies those exact files and restores the remaining ones.

Paths are restricted to explicitly mapped public `.olean.private` evidence under
`lean/` or `reuse/`. Those compiled Lean files are not private reuse credentials.
Cache/key/origin directories, noncanonical paths, symlinks, case collisions,
unlisted/altered compressed members and unsafe output overlap refuse. The normal
transport directory may live below the containing T013 root because its actual
payload paths and restored `lean/` paths are disjoint. Existing-ancestor
filesystem identities protect against case aliases as well as lexical overlap.
Inputs and destinations must remain quiescent; hostile concurrent mutation of
the host is outside this local utility's guarantee.

## Retained evidence and checkpoint boundary

`PREPARE.json` records successful compression and exact comparison with all ten
originals. `compression-writer.py` preserves the writer used for that observation;
`transport.py` includes the subsequent narrow correction permitting restoration
to the containing checkpoint root while protecting actual payload destinations.
No recompression or proof result was substituted. `ROUNDTRIP.json` records real
restoration of all ten files into a disposable directory, full decompressed-byte
comparison, repeat verification without inode/mtime changes, and unchanged
originals/historical pins. Only the disposable restored copies were removed.

The exact T013 `.gitignore` entries are permitted only after those observations
and complete selected-directory coverage. They name these ten raw paths, with
no wildcard or future-file exclusion. The original files stay on disk. All
compressed payloads, their maps, original public evidence manifests and this
restore procedure travel through ordinary Git.

New reuse gates can create more oversized files. Before the final checkpoint,
perform a new explicit coverage audit and, when needed, a separately selected
successor mapping. This transport does not claim coverage of future evidence.
Independent source/evidence review and any eventual commit/push remain separate.
