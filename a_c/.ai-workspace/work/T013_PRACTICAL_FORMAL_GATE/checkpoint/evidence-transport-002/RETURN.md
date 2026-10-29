# Successor transport return

All 24 observed public proof files over 95 MiB are covered: the original ten
aliases plus 14 new aliases from prior reuse qualification, the failed and
successful actual Context checks, two actual reuse checks and installed package
qualification. Every raw file matches its known identity and original manifest.

Two deterministic gzip payloads preserve 2,736,873,600 mapped raw bytes in
54,160,541 compressed bytes. Both compressed files are byte-identical to
transport001. Manifest SHA-256:
`7846c894f88b08f4ed9a772578339e4ced67af5bdca5ec843711a141452f12ea`.
Selection SHA-256:
`8455357d55bd1dfe8234161b76418cbf0adf5f5111a7e4fce7b94bb98d4f9674`.

Actual restoration created all 24 files in a disposable tree, compared every
byte stream and SHA-256 with the originals, then repeated restoration without
rewriting any existing file. Final comparisons confirm every original still
has its recorded inode, mtime and contents. Only disposable restored copies were
removed. The complete selected transport operation took 51.44 seconds.

The successor source changes only its compiled-path guard: ten frozen literal
real-use/package paths join the existing lean/reuse rule. Generic path, private
component, symlink, bounds, digest, overlap and no-overwrite controls are unchanged.
The complete patch and source pins are retained. Thirteen small controls pass,
including all newly admitted aliases, nearby/unlisted variants and safe refusal.

Coverage was checked before appending 14 exact `.gitignore` paths. The previous
ten lines and all transport001 files are preserved. No wildcard exclusion,
source/log/JSON omission, private origin/support acquisition, raw-file removal,
proof/actor invocation or Git effect occurred. `README.md` gives the exact restore
commands. The source/evidence successor is ready for independent review; this
return authorizes neither checkpoint nor release.
