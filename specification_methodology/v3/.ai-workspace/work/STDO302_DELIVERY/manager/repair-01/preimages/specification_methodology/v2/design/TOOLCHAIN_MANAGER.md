# STDO Toolchain Manager Design

- Status: active
- Implements: `.ai-workspace/tickets/completed/T-013-create-stdo-toolchain-manager.md`,
  `.ai-workspace/tickets/completed/T-014-make-version-line-selector-latest.md`,
  `.ai-workspace/tickets/completed/T-020-consolidate-specification-stack-monorepo.md`,
  `.ai-workspace/tickets/completed/T-021-qualify-monorepo-release-refs.md`,
  `.ai-workspace/tickets/completed/T-029-complete-consumer-cohort-adoption.md`,
  `.ai-workspace/tickets/completed/T-034-support-standalone-v3-installation.md`
- Derives from: `specification/PRODUCT.md#product-definition-overlay`
- Supersedes: none
- Superseded by: none

## Boundary

### Stable-v1 release acquisition

The owner's selected STDO 3.0.2 release adds an immutable stable profile to the
manager in version 0.1.6. It implements the prospective common RELEASE contract;
the v2 source builder remains its pinned 2.5.0 RC4. Installed releases and legacy
RC semantics are conserved.

Stable syntax is `vMAJOR.MINOR.PATCH` with canonical decimal components. Syntax
normalization is not release classification. Actual acquisition requires the
qualified annotated ref, its matching embedded tag name, direct commit target,
and exactly one unindented `STDO-Release-Profile: stable-v1` annotation line.
The fresh version line must contain neither RC refs in either namespace nor a
historical bare alias. RC absence alone is insufficient. An explicit profile
tag also cannot become a legacy selector if RC refs are subsequently added.

Only stable manifests add `release.profile = stable-v1`. The legacy canonical
manifest algorithm and installed identities remain unchanged. The successor
manifest schema couples stable syntax to its profile/qualified coordinates;
the successor Product Definition schema permits the new exact basis URI.
Installed byte verification enforces that profile relation in addition to
existing member checks. Wrong digests, payload tampering and identity drift
continue to refuse before replacement.

Stable channel discovery returns the same exact tag, with `cut_ordinal = null`.
There is no second selector and no implicit next-patch adoption. Legacy channels
retain their prior highest-RC and historical/qualified-transition algorithm;
their selected annotations must not assert an explicit final-release profile.
The existing same-line downgrade guard also refuses stable-to-RC regression.
Different version-line selection remains explicit; no global version-policy
algorithm is introduced. Complete V2 cohort updating retains its existing
contract and is not widened into a synthetic stable cohort.

The native standalone package does not carry this Python project. Distribution
therefore includes a separately checksummed manager wheel. Qualification binds
the actual wheel import/entrypoint to the changed source and exercises stable
install/verify/URI and pinned-definition paths from an isolated environment.

### Selected composition-verification increment

The owner's 26 October 2026 instruction selects the implementation of the
reviewed recursive Product-composition proposal. The manager increment restores
the existing Product Definition target, identity, relation and contract
resolution obligations. The source builder remains the exact `v2.5.0-rc.4`
basis in `stdo_default.json`; this does not adopt the methodology amendment.

`fleet verify` checks each selected definition and its explicitly declared
composition closure. `--root` selects definitions; `--resolver-root` optionally
declares a larger local acquisition boundary, without selecting unrelated
Products or granting operation authority. The default boundary is the selected
directory, or a selected file's parent. Each target is checked against its own
schema and installed basis. Shared targets are acquired once while every edge
retains its own index, relation and contract observations. Cycles terminate by
visited physical definition identity; a mechanical cycle establishes neither
work readiness nor semantic compatibility. Duplicate Product identities refuse.

The resolver supports local relative/absolute and local `file:` references
inside that boundary, and exact immutable `stdo:` references through the
explicitly selected installed Store. It does not fetch network resources,
install missing cuts or resolve mutable selectors. Unsupported schemes or
fragment formats are reported as unsupported rather than resolved or silently
ignored. Local symlink components and path escapes refuse before acquisition.
Markdown fragments use the shared Axiom Indexer heading convention, outside
fenced examples, plus explicit HTML anchors. Markdown escapes and matching
backtick spans (including multiline spans) cannot supply those HTML anchors;
raw tags are consumed as units so their attributes are not interpreted as code
delimiters. The existing heading-slug function is unchanged. This bounded
fragment scanner is not a general Markdown renderer. JSON fragments use JSON Pointer;
HTML fragments use explicit IDs/anchor names. A directory contract establishes
directory existence, not an enumeration or assessment of all its descendants.

`composition.verify_composition` is the reusable read-only API. Its report
retains the resolver boundary, limits, definition and acquired-file digests,
per-edge reference results and exact failures. Graph limits and per-file size
limits fail closed; unavailable or changed inputs are not successful resolution.
There is no authority-prose interpreter, proof of semantic sufficiency,
filesystem sandbox or hostile concurrent mutation guarantee. This increment
does not add a runtime dependency on any sibling Product.

The manager is a dependency-light Python command-line application installed
once per user or build image. It manages exact STDO distribution bytes and
Product Definition routing. It does not evaluate semantic conformance, govern a
consumer workflow, infer product composition, or own a consumer's selection.

The Product Definition is the sole authored selection surface. Its exact basis
is an immutable logical release URI plus the SHA-256 of a deterministic
installed-release manifest. Its version-line selector is discovery input for
the highest-ordinal published immutable RC, or the exact stable-v1 tag on a
fresh stable version line.

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
  drift. A cut selects exactly one source layout: `specification/standards`
  below the historical repository root, `specification_methodology/`, or the
  cut's major-version root `specification_methodology/v<major>/`. V3 also
  supports the standalone package described below. Physical paths are projected
  back to canonical logical source paths before manifest construction.
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

## Standalone V3 Package

For a V3 cut, the published project root may instead contain `standards/`,
`plugins/spec/`, `LICENSE`, and `release/release-note.md`. The project root is
exactly `specification_methodology/v3/`. Build tenants are not searched or
selected. If both `standards/` and `specification/standards/` exist there, or
another recognized project layout competes, acquisition refuses. Missing
required package members refuse; the adapter does not fall back to another
layout's release note. The existing optional plugin rule remains unchanged.

The adapter maps `standards/<member>` to logical
`specification/standards/<member>` and the package release note to logical
`releases/v<line>.md`. Installed paths and the canonical path-sensitive
standards digest recipe remain unchanged. The recorded project and standards
trees are the actual Git trees of the selected physical package. The manifest
schema and all historical manifest bytes remain unchanged. A physical layout
does not supply release authority: acquisition still requires an exact annotated
immutable cut and validates any expected manifest digest.

Basic install, manifest, verify, resolve, sync, adopt, and bootstrap operations
have no a_c or Representation prerequisite. The separately selected
`cohort-update` operation retains its existing contract. A V2-to-V3 consumer
migration must explicitly review entrypoints and other selected routes;
adoption still changes only the exact basis and `$schema`. Schema validation
does not establish that every declared locator resolves. The
[V3 installation guide](../V3_INSTALLATION.md) identifies the changed built-in
entrypoints without introducing automatic route rewriting.

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
the program's calculus, frame, record-source, residual re-entry and optional
frame-index source edges and the map's source routes to require complete
declared source coverage. Frame-index membership sources are required directly
from the program even if the map omits their routes and observations;
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

Each companion install contains the cohort's exact qualified inventory, the
selected Product Definition and release record, and its declared semantic-index
assets. All are acquired at the exact companion commit; the plan binds this
install closure separately from the independently verified qualified inventory.
Unselected historical fixtures and other subtree content are not installed.
Selected native routes and symlink targets must resolve within this closure;
missing members, unsafe links and traversal refuse. Installs are
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
