# Oversized evidence transport return

Writer `/root/ac_scale_checkpoint_writer` completed the bounded transport grant.
All ten original frozen compiled files and their historical records remain
unchanged. No proof, gate, model, acceptance, release or Git checkpoint occurred.

The ten paths map 1,140,364,000 bytes to two distinct payloads. Deterministic gzip
produced **27,954,126** and **26,206,415** bytes, totaling **54,160,541 bytes**.
Both are below the conservative 95 MiB remote-member limit. The exact manifest
digest is `59732cdb8f956e07ecc1734c63e5c29b3281f8047c4c58b4e5211409a24635ea`.

Actual preparation compared decompressed bytes with every original. Actual
restoration then reconstructed all ten paths into a disposable copy, compared
them again, and verified existing identical files without changing their inode
or mtime. Original files and historical pin sources were rechecked unchanged.
Only the disposable restoration was removed. Nine synthetic controls cover
determinism/deduplication, conflicts/no overwrite, tampering, bounds, member/path
custody and normal containing-root restoration. No compression or restoration
process remains active.

After complete coverage of the ten selected over-limit paths was verified,
the separately permitted T013 `.gitignore` was created with exactly those ten
anchored paths. Its SHA-256 is
`2a4fdf2306617cecd970c4515c106fb1d6d53b2904cb667dca04ab4b8ef52869`.
Read-only Git checks confirm none was already tracked, each exact pattern
applies, and selected source/log/JSON controls remain unignored. No index,
commit or push effect occurred.

[README.md](README.md) provides verification and safe restoration into a fresh
checkout; [ROUNDTRIP.json](ROUNDTRIP.json) and [EXCLUSIONS.json](EXCLUSIONS.json)
retain the actual observations. The original compression implementation is
preserved separately from the narrow restore-path correction, with exact source
pins, so no execution result is attributed to code that did not produce it.

This closes preparation for independent source/evidence review. New reuse runs
may add oversized members; the eventual checkpoint requires a successor mapping
and fresh coverage audit for those new paths. This cut grants no wildcard
exclusion or future transport coverage. All private origin/key/cache state was
outside the input and write scope.
