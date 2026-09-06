# STDO Toolchain Manager Design

- Status: active
- Implements: `.ai-workspace/tickets/completed/T-013-create-stdo-toolchain-manager.md`,
  `.ai-workspace/tickets/completed/T-014-make-version-line-selector-latest.md`,
  `.ai-workspace/tickets/completed/T-020-consolidate-specification-stack-monorepo.md`,
  `.ai-workspace/tickets/completed/T-021-qualify-monorepo-release-refs.md`,
  `.ai-workspace/tickets/active/T-029-complete-consumer-cohort-adoption.md`
- Derives from: `specification/PRODUCT.md#product-definition-overlay`
- Supersedes: none
- Superseded by: none

## Boundary

The manager is a dependency-light Python command-line application installed
once per user or build image. It manages exact STDO distribution bytes and
Product Definition routing. It does not evaluate semantic conformance, govern a
consumer workflow, infer product composition, or own a consumer's selection.

The Product Definition is the sole authored selection surface. Its exact basis
is an immutable logical release URI plus the SHA-256 of a deterministic
installed-release manifest. Its version-line selector is discovery input for
the highest-ordinal published immutable RC only.

## Legacy Installer Disposition

ABIogenesis `gen-install.py` supplied three useful precedents: an explicit
verify-only path, idempotent marker-delimited `AGENTS.md`/`CLAUDE.md` updates,
and machine-readable install results. The manager retains those properties.

It intentionally does not retain that installer's adjacent mutable-source copy,
wholesale `.genesis` replacement, fixed project scaffold, or presence-only
standards verification. Those behaviors coupled method upgrades to one source
checkout and rewrote every consumer. The replacement installs immutable cuts in
one shared store and lets each layout-neutral Product Definition select its own
exact basis.

## Components

- `git_source.py` reacquires one annotated immutable RC tag into an isolated
  temporary bare object store and resolves a mutable version-line alias only
  when it matches the highest-ordinal published immutable RC. During the
  shared-source transition it conserves historical unqualified cuts and
  resolves future `specification_methodology/` qualified tags to the unchanged
  product-local cut and public `stdo:` URI. Additional refs to the same exact
  tag object are conserved; equal local cuts naming different tag objects are
  ambiguous and refuse. Channel resolution selects the qualified successor;
  direct logical-cut reacquisition keeps the historical ref when an identical
  preserving alias also exists, so an installed historical manifest does not
  drift. A cut contains
  STDO either at the historical repository root or at the exact monorepo prefix
  `specification_methodology/`, never both. Physical nested paths are projected
  back to project-relative logical source paths before manifest construction.
- `manifest.py` derives the exact tag, commit, trees, standards inventory,
  canonical member-set digest, member bytes, license, release note, and plugin
  payload admitted to an installation. A qualified shared-source cut also
  retains its Project Release Namespace, qualified ref, Project Subtree root,
  and Project Subtree tree; historical manifests remain byte-reproducible.
- `store.py` atomically materializes immutable cuts, records logical URI
  mappings, resolves members within the release root, and detects missing,
  extra, changed, or redirected state.
- `product_definition.py` discovers overlays, validates them against their
  exact schema, reports and synchronizes pinned bases, performs explicit
  selector adoption, and updates marker-bounded agent bootstraps.
- `cohort_update.py` derives and applies one explicitly selected complete
  consumer update using the existing upstream cohort and Product release
  inventories. Temporary Git views and plan/result objects carry observations;
  they do not become a second dependency registry.
- `cohort_assets.py` owns the shared release-asset integrity checks used by
  both this operation and the existing root stack-release checker. The root
  checker imports the extracted functions; the manager supplies an exact Git
  view and the verified STDO inventory to the same checks.
- `cli.py` exposes singular and fleet operations without creating another
  authority surface.

## Store

The logical layout is:

```text
<store>/
├── registry.json
└── releases/
    └── v<version>-rc.<n>/
        ├── manifest.json
        ├── standards/
        ├── plugins/spec/
        ├── release/release-note.md
        └── LICENSE
```

The physical root defaults to the user data directory for the host platform and
may be overridden by `STDO_STORE` or `--store`. Product Definitions never carry
that machine-local path. `stdo://releases/<cut>/...` resolves through the local
registry only after the entry is confined to the expected release directory.

Installation is staged under the store, verified, made read-only, and renamed
atomically. Existing bytes are never repaired or overwritten in place. A
damaged installation fails closed so the operator can inspect it.
Manager-owned store roots, registries, release directories, payload
directories, and payload files must be physical entries of their declared
type. Verification inventories directories, regular files, redirects, and
special entries without following them; every undeclared entry is damage.

## Operations

- `install` names an immutable RC cut directly and changes only the store.
- `sync` installs and verifies the basis already pinned in one definition; it
  never follows the selector and never edits the definition.
- `adopt --dry-run` resolves and reports the exact latest selector target plus a
  digest over current definition bytes, cut, annotated tag, commit, tree, and
  manifest; a lagging selector or same-line downgrade fails closed.
- mutating `adopt` requires that externally accepted digest, re-derives it,
  installs only the bound target, rechecks the definition bytes, then atomically
  changes only `constitution.stdo.basis` and a basis-relative `$schema` URI.
- `bootstrap` owns only one delimited block in each declared agent file and
  preserves all other project bytes exactly. Targets are relative to the
  resolved `product.source_project`; every target is preflighted before writes.
- `fleet` discovers `stdo_<label>.json` files recursively while excluding VCS,
  dependency, generated, and managed-store directories. Every fleet write
  requires `--all`; adoption also requires its aggregate accepted plan digest,
  while bootstrap confines every source project to the fleet root.

## Complete Consumer Update

`cohort-update --definition <path> --selection <path> --dry-run` selects one
consumer by exact definition ID and emits its complete plan. The mutually
exclusive apply form requires `--accept-plan-sha256 <digest>`. A held dry-run
returns exit 1 with explicit source re-entry reasons; an invalid or unaccepted
operation returns exit 2. A successful dry-run is `planned`, never `complete`.
Only a verified successful application is `updated` and `complete: true` for
the explicitly selected relation.

The temporary invocation selection uses `kind: stdo.cohort-update-selection`,
`schema_version: 1`, the consumer `definition_id`, and three selections:

- `cohort`: repository transport, exact project-qualified annotated RC `ref`,
  accepted `tag_object`, and cohort-document `path`. The document supplies the
  STDO cut, Product population, portable member inventories, dependencies and
  publication repository. The existing GitHub publication convention supplies
  immutable commit/member URLs; unsupported publication locators refuse rather
  than infer a URL mapping.
- `companions`: one row per non-STDO cohort Product, naming `product`, its
  existing consumer `target_definition_id`, exact `definition_member`, proposed
  immutable `product_definition` and `contracts` locators, external physical
  `install_root`, and `links` (`path` relative to the consumer source project,
  `member` within the exact Product subtree, or `.` for its root). Each selected
  composition must already exist uniquely. Native routes are ordinary selected
  links; the manager does not discover host policy or claim native-host trigger
  qualification from a link check.
- `derived_context`: the complete owner-selected list of `program`, `map` and
  `bindings` paths relative to the consumer source project. An explicitly empty
  list is a scope selection, not semantic absence inferred by the tool.

The Axiom Indexer adapter reads its existing binding-set and logical-map
carriers. It verifies the map's canonical intrinsic digest, the canonical
program digest, and every declared `resolved_sources` digest. It uses
the existing program's calculus, frame, record-source and residual re-entry
edges and the map's source routes to require complete declared source coverage;
removing a stale observation and recomputing the map digest cannot establish
readiness. Local URIs use
whole-document digest coverage: distinct fragments of the same URI document
share its exact byte evidence, including residual re-entry routes. They use
the existing Indexer Markdown heading convention to verify each required
fragment separately; a whole-document digest cannot satisfy an absent heading.
Physical resolution uses
the longest unique explicit binding prefix, confined to its physical root;
STDO URIs must select the target exact cut and are checked against its immutable
source bytes. If the consumer definition is a source, its proposed bytes are
used. This catches a map that would become stale through the update itself.
This adapter checks existing evidence; it neither executes semantic judgments
nor rewrites or regenerates a program or map. Source owners still own their
completeness and meaning.

Each companion install is the full exact Git Product subtree, with its portable
subject inventory independently verified against the cohort. Installs are
external to the consumer, nonoverlapping, and physically rooted. Files retain
their executable distinction; escaping symlinks, extra directories, changed
members and missing members refuse. Existing installs are never overwritten.
Absent installs are staged and verified before rename. No companion registry
or copied consumer dependency declaration is introduced.

The declared plugin and semantic-index assets are mandatory. The operation
verifies both native plugin manifests at the exact STDO cut and the exact
Representation program, map, validation report and source-corpus carrier at
the companion cut. The shared checker conserves their existing source-release
identity and complete ordered inventory, canonical program/map/report digest
relations, declared program-source coverage, resolved-source digests and exact
release-note member bindings. Missing or stale assets refuse before effects;
portable companion inventory alone cannot prove the complete cohort.

The plan binds selection bytes, definition bytes, immutable source identities,
all link preimages/targets, physical destinations and source observations. The
definition's unrelated fields and every unselected consumer file survive.
After staging, the operation rechecks source evidence and all consumer
preimages. It replaces selected links and then writes the definition atomically
as one file. A caught failure restores changed links and definition bytes and
removes newly created empty consumer directories; immutable staged installs can
remain for reuse. Callers must supply an exclusive consumer write scope. There
is no claim of a multi-path crash transaction: abrupt interruption or rollback
failure requires preimage-based owner recovery and cannot produce complete
readiness. The returned acceptance object is reproducible evidence for that
bounded operation, not a new workflow engine or persistent lock.

## Refusals

The manager refuses unannotated or malformed cut identities, lightweight or
lagging version-line selectors, a selector that does not match the highest
published RC, absent or ambiguous matching RC tags, zero or multiple recognized STDO project
layouts, channel downgrades, unaccepted or stale adoption plans, unexpected
manifest digests, damaged or extra installed entries of any type, store or
registry redirection, URI traversal, cross-basis schema locators, invalid
Product Definition shape or formats, bootstrap boundary escape, malformed
markers, and implicit fleet writes.

## Verification

The executable boundary is tested against unrelated temporary Git releases for
installation, reinstallation, tamper detection, URI escape, exact-basis sync,
latest-selector adoption, lagging-selector and downgrade refusal, marker
idempotence, fleet discovery, and refusal paths. A
repository dogfood tests independently install the immutable released
`v2.4.3-rc.1` and `v2.5.0-rc.1` cuts and check their known commits, inventories,
canonical aggregate digests, and historical manifest bytes. Synthetic
repository tests also prove the exact `specification_methodology/` monorepo
prefix, repository-root and standards-subtree identities, project-relative
logical members, and refusal of absent or ambiguous layouts. A second dogfood
boundary binds the source Product Definition to the exact installed public RC4
builder basis.
