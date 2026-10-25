# Common representation packaging preparation

The application-specific packager, exact offline display dependencies and
portable verification helpers are prepared. This document records tooling
preparation; it does not claim a closed final model, final bundle, archive,
semantic acceptance or publication.

The represented subject is common source checkpoint
`35fb4824a064a84df5af214a0d0e2da597c18ac6`, package tree
`7f2070b61c848b42b4dfb3af1e0ce53869de1aa1`. Its complete81-file snapshot,
58-file primary semantic selection and separate derived/metadata classes remain
unchanged. [SOURCE-READINESS.md](SOURCE-READINESS.md) retains the method's
unaccepted/unpublished `not_ready` standing. The common candidate is a subject
of this representation; the installed builder remains exact STDO v2.5.1-rc.2.

## Prepared inputs and operations

[package_release.py](package_release.py) accepts an explicitly selected,
closed proposal directory containing `model.json`, `carrier.json`,
`coverage.json` and `result.json`, plus the actual pinned-upstream export.
The export may be `graph.json` in that directory or an explicit `--graph` path.
Every supplied artifact is copied byte-for-byte. Both carriers must decode to
the unchanged model, and result/coverage identities must match. No F_P meaning,
original disposition, signature, record or existing study is rewritten.

The additional inputs are one explicitly curated public JSON construction
receipt and one or more explicit public review documents. Only those files
are copied. Raw run directories, invocation bodies, event streams, native
configuration and hidden reasoning remain outside the distributable artifact.
The receipt may retain opaque evidence hashes and recorded usage/settings;
the recipient does not thereby obtain complete private acquisition replay.

The eventual artifact identifier is `a_c-stdo-v3-common-35fb4824`. No Product
version, RC, tag or source verifier sentinel is repurposed as its version.
The default fresh output locations are `bundle/` and `dist/` beneath this
application. An existing bundle, archive or archive checksum refuses overwrite.

The proposed bundle includes:

- Exact model, reversible carrier, actual upstream export, result and coverage.
- Complete81-file frozen source, its three custody/selection manifests and
  line-addressed source views.
- The unchanged stdlib-only codec snapshot, SHA256
  `2f5de4d600e13904dc8cba3791ebdd83fe6ebb0c339654c86392baf9c2bd3667`,
  with runnable validate/decode/find/inspect/project and source-reentry commands.
- A readable official Graphify record view, a complete machine-readable record
  graph, and a searchable exact-record/source-grounding browser. Record-family
  colours are explicit grouping, not inferred communities. Display selection,
  omitted records, collapsed parallel occurrences and external-coordinate
  omissions are reported separately from the full reversible carrier.
- Public construction/review receipts, current release standing, a complete
  inventory, per-file checksums and a deterministic tar.gz with an external
  archive checksum. Owners, permissions, ordering and timestamps are fixed.

The exact Graphify checkout is
`fe085cedddde3a18554f8749b230bfe47f3dcce7`; the prepared exporter source and
license/notice subset is under [release_tools/upstream/](release_tools/upstream/).
The exported HTML's only changes are an explicit scope/navigation banner and
the exact runtime URL rewrite. The original HTML digest is retained so those
two changes can be inverted and checked.

The vendored vis-network9.1.6 JavaScript is byte-identical to Graphify's official
SRI pin:

`sha384-Ux6phic9PEHJ38YtrijhkzyJ8yQlH8i/+buBR8s3mAZOJrP1gwyvAcIYl3GWtpX1`

Its raw SHA256 is
`576bb887733eb01bb52ee75b90ef46d818454de5fddb5b616fb8a298d307ca12`.
The exact package metadata and Apache2.0/MIT license files are retained under
[release_tools/vendor/](release_tools/vendor/), with download URLs and hashes.
No runtime CDN or model service is required.

## Check preparation now

From this application directory, using the existing environment:

```sh
../../.venv/bin/python3 -B package_release.py check-preparation --upstream /path/to/the/pinned/graphify/checkout
```

This checks all frozen source members, selected codec, prepared dependencies,
official SRI, exact exporter files and clean pinned upstream identity. It emits
no final bundle. Helper controls exercised the actual pinned exporter on an
existing toy fixture, full display partitioning/reference-occurrence counts,
exact inversion of the two display changes, deterministic archive bytes,
protected archive refusal, dependency tamper rejection and unsafe-path refusal.
Those fixture outputs are owned scratch evidence, not a common representation.

The activation, original source/unrelated guards, dependency custody and bounded
preparation results are under
[t010/packaging](../../.ai-workspace/qualification/t010/packaging/).
Full extraction/replay and tamper controls over the final common artifact are
still downstream of the exact closed model and its review.

## Reserved release decisions and verification limits

Final artifact construction is waiting for the Executive's exact `MODEL-CLOSED`
handoff. Preparation does not close any source-method release gate or a_c
Product qualification obligation. Structural validation, exact source custody,
carrier recovery, semantic fidelity, owner acceptance and publication remain
separate claims. Graph connectivity supplies no governing closure or truth.

No applicable license for the a_c-owned codec, authored interpretation or new
packaging was found at a_c or repository root. Existing source, upstream,
vis-network and selected builder licenses are preserved in their own scope.
An owner-selected distribution permission is a concrete prerequisite to public
distribution; no third-party license is applied to a_c-owned material here.
Owner acceptance/release disposition remains reserved.

Interactive behavior remains unverified. The available browser policy blocked
an already-open older I5 local page. That action was stopped, and no HTTP,
headless, CLI browser or alternate surface was used to bypass it. No browser or
server was started by this preparation. The unused ordinary loopback preview
helper does not constitute UI verification; any later new-artifact preview
requires a genuinely permitted channel. Static generation and CLI checks alone
do not prove search, selection, filtering or neighbor navigation.
