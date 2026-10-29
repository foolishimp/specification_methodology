# Independent review — package repair 002 and evidence transport 001

**No actionable S0–S4 defect found in the selected scope.** The remaining S3
filesystem-alias overlap condition is discharged. The three earlier packaging
conditions stay discharged. The oversized-evidence transport preserves the exact
selected historical bytes and has a bounded, non-overwriting restore path.
This supports these preparations; it does not establish an actual final package,
remote checkpoint, installation, proof result or public release.

Reviewer: `/root/ac_scale_worker`, separately activated by `/root`. This Reviewer
authored earlier Lean scaling work but neither selected packaging nor transport
implementation. This assessment makes no independent claim about those Lean
proofs or the reuse implementation. Only this review directory was written.

## Exact subjects

| Subject | Selected SHA-256 |
| --- | --- |
| `package/repair-002/CLOSED.json` | `36db58e2f3d6dd2101db37d9f12f0d5f49638630bfd2a3f1ae4a139545e8696a` |
| `package/repair-002/PINS.json` | `5591b81fbcb3c7765085fc17911a6b87cd5daab742659837f4228f42918d37e7` |
| `package/repair-002/INVENTORY_PLAN.json` | `90e99f4f4345f4443416a3ce9a1c2f34a4b72dac331cd7088f7528d0d42af02e` |
| `checkpoint/evidence-transport-001/CLOSED.json` | `29a4f12fcfc243bfd489745b1f6b21202e4dee80931660d0afac86af3fc6b296` |
| `checkpoint/evidence-transport-001/PINS.json` | `06a59223e6fc3631509cedfd7ed607ab14d9ddaf7c7ed246dee6840ece1c9a8c` |
| Actual retained transport round trip | `30e1cc3972d7d8112ef67631482de3dff795950b140e51ef7303222e61ed576d` |

All nine package and fourteen transport member pins match, as do the selected
closures, plan and T013 `.gitignore`. The prior review closure remains
`d0be2ecca918d495924bd48be7a8be273dcc94be1b996f36d07a71f580f044d7`.

## Discharged packaging conditions

| Condition | Assessment and actual path |
| --- | --- |
| S2 qualified-host identity versus distributable public identity | Discharged and conserved. `package/repair-002/package_source.py:180` derives the fixed public projection by removing only `.cache/formal-origin-v1/selection.json`; `:212` binds every remaining pin to its original payload coordinate. The full qualified identity remains recorded. The recipe at `RECIPE.md:72` requires a distinct origin-free installation observation and does not transfer reuse eligibility. The in-memory discriminator preserves the original full identity and removes exactly the one fixed coordinate, without reading it. |
| S2 case-sensitive private exclusions | Discharged and conserved. `package_source.py:73` folds components, suffixes and special origin spellings before `regular()` performs metadata acquisition at `:99`. Mixed-case private/cache/key controls refuse. No private material was acquired. |
| S3 `..` root aliases | Discharged and conserved. `package_source.py:115` refuses before overlap, metadata and output operations. The read-only controls confirmed this ordering. |
| Residual S3 case-alias root overlap | Discharged by this repair. `package_source.py:126` retains lexical checks and compares each existing root with the other path's existing ancestors through `samefile` at `:149`. Build (`:298`), archive (`:312`) and extraction (`:361`) all call it before acquisition or output. Six probes using this host's actual `/Users` versus `/users` aliases, in both spellings, refused before any file open or directory creation. Unavailable identity propagates refusal; genuinely separate existing roots remain allowed. |

The whole package module's AST outside `separate()` is identical to repair 001,
including constants, imports and the previously repaired contracts. All ten
predecessor member pins remain unchanged. All 63 payload destinations are
conserved; only five package-control source coordinates move to repair 002.
The retained nineteen author tests have zero skips. They were inspected and
hashed, not rerun because they create packages and extractions.

`PROBES.json` records the independent, effect-blocked entry-point checks.
One initial probe placed an output beneath a regular file and was correctly
refused by `NotADirectoryError`; `PROBE_ATTEMPT-001.json` records that probe-shape
correction. No source or output was created by either probe.

## Oversized-evidence custody and restore

The mapping in `SELECTED.json` exactly equals the transport manifest's ten paths,
hashes and lengths. Its two payloads total **54,160,541 compressed bytes**, each
below the selected 95 MiB bound, and carry **1,140,364,000 mapped raw bytes**.
Independent streaming decompression compared every byte against all ten existing
originals, not only their reported hashes. Both raw identities and compressed
identities match. Eight original public-run manifest member pins still agree;
the two `correction-011` objects remain correctly described as directly bound
raw identities with historical source context, not invented prior object pins.
Original size, inode and modification time were unchanged by this review.

The actual path is bounded and preserves existing files:

- `checkpoint/evidence-transport-001/transport.py:133` requires the externally
  selected manifest digest and complete deduplicated payload coverage. Rows
  enforce count, per-member and total restored-size bounds at `:105`.
- `:167` checks compressed size/hash and streams decompression with at most one
  byte beyond the declared raw bound, refusing an overrun. It checks the complete
  raw size/hash at `:183`. Independent read-only controls on an actual payload
  refused both a too-small raw bound and a wrong raw digest.
- `:236` validates all payloads and compares every existing target before creating
  missing outputs. Each new member is fully checked in a temporary file, then
  published by non-replacing atomic hard link at `:265`. The documented partial
  failure behavior leaves only completed exact new files; rerun verifies them.
- Root/member symlinks, noncanonical paths, private coordinates and case-colliding
  mappings refuse. The normal containing T013 destination is allowed because its
  actual mapped `lean/` targets are separate from the transport directory.
  A case-alias overlap discriminator refused before payload reads or writes.

The exact ten `.gitignore` patterns match the ten selected raw paths, with no
wildcard or future-file exclusion. All oversized files in the five selected
historical directories are covered. The original public manifests, failed run,
logs and source records are not replaced by compressed custody. The manifest's
compression-writer digest matches the separately retained writer; the subsequent
restore-path correction is not misattributed to the original compression run.

The nine retained author controls and real disposable restore/compare/repeat
record are coherent and pinned. I did not repeat extraction or restoration.
`CUSTODY.json` records my independent byte comparison and history checks;
`CONSERVATION.json` records the remaining source/path controls.

## Remaining scope

No selected prior packaging condition remains open. These limits remain:

1. This is prepared remote byte custody, not observed remote publication or fresh
   remote acquisition. Commit/push and post-acquisition verification are separate.
2. The transport covers only the ten selected files. New oversized reuse or proof
   outputs require the explicitly selected successor coverage audit/mapping.
3. The proposed package plan is not a final candidate selection. No unlisted file
   was present in its closed namespaces at this review's snapshot; completed
   integration can change that population and still requires final source freeze
   and inventory review. No final source bundle, archive or repack was produced.
4. Origin-free identity observation, exact local support setup, installed use and
   release remain unqualified. Transport does not mint proof/reuse eligibility,
   semantic acceptance or authority. Quiescent local inputs and destinations and
   an independently trusted manifest hash remain explicit prerequisites.

No S0, S1, S2, S3 or S4 finding is issued. No packaging, extraction, restore,
compiler, proof, origin/key, actor, installation or Git operation was performed
by this Reviewer. The review is complete for the exact subjects above.
