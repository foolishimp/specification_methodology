# Codex RC1 package and later release path

The current deliverable is a complete, reviewable Codex package. The owner will
assess both lines before choosing a release subject. This preparation selects no
tenant, merge, immutable tag, installed basis, cohort, or publication. It builds
the whole package now and identifies the later gates without making those gates
prerequisites for comparing the two packages.

The admitted source is common C3-I5-06 at
`4c340f7adec9f3c893e3e267b23e4cadeb357854`, Codex preimage
`99f932cfece1a7c9ba6f85c44c47d2403a486aa7`, and package commit
`b2ad4d99a9ab6873cded9ffdfbc416ef1e0e23a5`. Entry HEAD is
`60eb7a2d43d9ac2d9557eae94a51db192209f06b`. All three Codex commits carry the same
successor tree, `c218f62208518fc184faae7a2e5aca16b65f93a9`. The continuing source
repair is a later subject; rerun the command below once against its integrated
freeze. This document supplies packaging feasibility, not candidate acceptance.

## Runnable review delivery

Use the installed toolchain's Python, which has the inspected `stdo_toolchain`
modules. The helper takes a full commit and a fresh, explicit scratch directory.
It reads Git objects without creating objects or refs. It copies only the whole
selected successor, the exact encoding-theory Install's declared members and
the exact seven-member Axiom checker Product. It includes existing licenses and
records the absence of an Axiom license at its Product and repository roots.
No `.git`, credential file, unrelated history, private cache or native host is
included.

```sh
cd /Users/jim/src/apps/specification_methodology-codex
RC1_PACKAGE_COMMIT=b2ad4d99a9ab6873cded9ffdfbc416ef1e0e23a5
RC1_PACKAGE_OUTPUT=/tmp/codex-rc1-final-review-bundle
/Users/jim/.local/pipx/venvs/stdo-toolchain/bin/python -B \
  specification_methodology/v3/build_tenants/codex/qualification/C3/rc1/release-preparation/preview_package.py \
  --repository "$PWD" --revision "$RC1_PACKAGE_COMMIT" \
  --output "$RC1_PACKAGE_OUTPUT" \
  --theory-root '/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2' \
  --record
```

Replace `RC1_PACKAGE_COMMIT` with the exact final integrated package commit.
Choose a fresh output directory. `--record` refreshes only this directory's
small package/dependency inventories and receipts. Omit it for an exploratory
scratch run. It does not change the candidate or common records.

Outputs are `codex-rc1-review-package.tar.gz` (all candidate bytes),
`codex-rc1-review-bundle.tar.gz` (candidate plus admitted dependencies),
`PACKAGE_MEMBERS.json`, `DEPENDENCY_MEMBERS.json`, `PREVIEW_RECEIPT.json`, and
`BUNDLE_REACQUISITION.json`. The bundle includes its inventories and usage guide.
The helper extracts the archive into a fresh scratch directory, verifies every
candidate/dependency byte, and invokes the exported `interpretation/bindings.py`
against the bundled theory. It does not run the old qualification suites or the
checker's task-dependent projection.

Python 3.13 was exercised for this binding operation. The exported binding
script and checker import only standard-library modules. Python, Git, the
toolchain used to construct the archive, and native Codex/Claude hosts are not
bundled. Given the existing Python runtime, the verified local binding command
uses no network; provisioning a new runtime offline is untested. The encoding
theory remains the immutable RC2 dependency. Copying it supplies no acceptance
of a final v3 encoding choice and does not make the predecessor govern the
successor's method meaning.

The measured preview contains 90 candidate members, 38,576,100 uncompressed
bytes, plus 79 exact dependency members and three bundle metadata members.
The candidate archive SHA-256 is
`c22925e5d7f3917ff756992adab94491e9657c21adc6f63f5dd25b3ed3b42604`;
the dependency-complete bundle SHA-256 is
`9f2843102777d99d9e398c49a19536231d47a27ab0b32abb54cdb74f662bdcb7`.
All 81 documentary pins match. Program/map digest relations match. Fresh
archive extraction and the exported binding operation pass. These are
packaging observations on the frozen pre-repair subject.

## Minimal actual installer route

The existing `GitSnapshot._detect_project_root` selects the major version from
the cut. For a v3 cut it accepts exactly one of `specification/standards`,
`specification_methodology/specification/standards`, or
`specification_methodology/v3/specification/standards`. The current tenant path
is outside that selection. The installed module bytes match the inspected
code at entry HEAD; no installer redesign is needed to use the v3 path.

After a candidate is selected, its release Writer can promote these exact
members into an isolated release construction subject:

| Candidate member | Existing-toolchain release coordinate |
|---|---|
| `successor/standards/**` | `specification_methodology/v3/specification/standards/**` |
| `successor/plugins/spec/**` | `specification_methodology/v3/plugins/spec/**` |
| `successor/LICENSE` | `specification_methodology/v3/LICENSE` |
| New exact release-scoped note | `specification_methodology/v3/releases/v3.0.0.md` |

The scratch promotion includes the first three rows byte-for-byte. The actual
loader selects `specification_methodology/v3` through a filesystem adapter.
Its real manifest constructor then refuses the missing release note. That
probe establishes path feasibility; it is not acquisition of a tagged release.

The resulting standards set has 62 members and member-set SHA-256
`64ae5615ec268578b8211108fe2821a8453721cd994a6a1a37a2c837b7352fdd`.
There are 17 plugin members. Current plugin manifests say `3.0.0`; the proposed
RC1 cohort requires `3.0.0-rc.1`, so release-scoped version reconciliation is
real work, not a passed gate.

`stack_release.json`'s `source_subtree` is not an alternate installer input.
It maps carrier locations for frozen historical subjects. Both the loader and
the cohort checker's frozen STDO identity still require
`<project-subtree>/specification/standards`. A future v3 cut records
`subtree: specification_methodology/v3` directly.

## Interpretation delivery and genuine owner choices

`stdo install` materializes standards, plugin, LICENSE and release note only.
It excludes the candidate README and all nine `interpretation/` files. A
standards-only promotion therefore cannot deliver this Product's complete
documents-plus-interpretation subject. The complete review bundle already
preserves those parts for comparison.

For the eventual release, the narrow proposal is to keep the existing matched
cohort and deliver the accepted interpretation through STDO Representation's
existing consumer acquisition. The owning Product must accept that subject and
its source linkage. A tenant interpretation does not become Representation by
copying or by a matching version string. The alternative of putting an
interpretation inside the standards closure can use the same installer, but
requires a deliberate inventory/source-path/self-reference design and binding
repair. It is not the current candidate layout and is not required for the
review bundle.

The following decisions retain their existing owners:

| Decision | Concrete choice to settle after both package assessments |
|---|---|
| Release subject | Select Codex or Claude with its exact freeze and acceptance. A different future scope requires owner repricing. |
| Interpretation and acquisition | Adopt the narrow matched-Representation proposal, or another explicitly complete Product-member/acquisition boundary. |
| Encoding basis | Choose the released interpretation's exact theory and independently establish the changed relation. The current construction dependency remains RC2 and cannot be rewritten. |
| Compression and identifiers | Keep, supersede or remove the carried compressions; issue/accept the a_c and Traversal Occurrence Profile identities under the Product's existing decision. The review package preserves them all. |
| Exact cut and cohort | Select the immutable `specification_methodology` cut and required companion versions. `v3.0.0-rc.1` is a proposed path-probe label here. |

The existing checker currently requires a cohort program's `source_basis` to be
`stdo://releases/v3.0.0-rc.1/standards/`, a versioned program URI, the exact
tag-derived corpus inventory, and matching validation/map digests. The current
program instead uses `repo://codex-v3/successor/` and an iteration-3 program URI.
Its method-source routes need rebinding after the selected corpus is frozen.
Its `calculus_ref` is a separate RC2 identity: the existing generic cross-cut
route check rejects that identity in both the program and map. Merely replacing
every old URI would falsify the encoding basis. If the owner keeps that exact
separate theory in the released interpretation, the existing cohort contract
and validator need an explicitly scoped distinction between method-source
identity and encoding-theory identity. If a successor theory is selected,
its interpretation/checker relation needs the corresponding qualification.
Neither choice calls for building an unrelated release framework.

## Later release construction with existing commands

The repository's `STACK_RELEASE.md` selects the complete three-Product cohort
for an unqualified release instruction. The present owner instruction is
narrowed to both reviewable candidates before selection. Current v2 source,
cohort bytes, tags, installs and selectors remain preserved throughout this
preparation. Their historical commit-B `status: candidate` field does not mean
RC2 is unpublished or that this preview can reuse its identity for v3.

Once the required choice and exact effect grants exist, the existing path is:

1. Freeze selected documentary/plugin/license/release-note/qualification bytes
   in commit A. Bind predecessor dispositions and complete required member and
   integrated assessments on that exact subject. Create its annotated STDO tag
   locally through the separately activated Git Writer.
2. Obtain the real tag-dependent manifest, then install and verify that cut in
   a fresh store. Its digest cannot be computed as a release identity before
   the actual annotated tag exists.
3. Prepare the same-version Axiom and Representation Products and native
   distributions through their owners. Perform affected semantic authoring,
   documentary source rebinding and regeneration from the exact STDO Install;
   preserve justified unchanged evidence. Freeze their exact inventories,
   dependency and release-note digests, public endpoint, observed remote ref
   expectations, full version lines and their digest in cohort commit B.
4. Run the content gate at B. Create the child annotated tags and the three
   Products' selector/RC/release refs locally. Run the refs gate. Only its exact
   checked `push_argv` can be used for atomic publication under the selected
   publication grant. No sequential or unguarded push is substituted.
5. Run the published gate, reacquire the published subjects into a fresh
   consumer fixture, and verify its declared complete acquisition. Later
   bookkeeping is commit C; no immutable tag moves.

Callable commands, with actual gate inputs supplied:

```sh
stdo --store "$RC1_FRESH_STORE" manifest "$RC1_CUT" --repository "$RC1_RELEASE_REPOSITORY"
stdo --store "$RC1_FRESH_STORE" install "$RC1_CUT" \
  --repository "$RC1_RELEASE_REPOSITORY" --manifest-sha256 "$RC1_MANIFEST_SHA256"
stdo --store "$RC1_FRESH_STORE" verify "$RC1_CUT" --manifest-sha256 "$RC1_MANIFEST_SHA256"
stdo --store "$RC1_FRESH_STORE" resolve "stdo://releases/$RC1_CUT/standards/README.md"
python3 scripts/check_stack_release.py --phase content --revision "$RC1_COMMIT_B"
python3 scripts/check_stack_release.py --phase refs --revision "$RC1_COMMIT_B" --remote origin
python3 scripts/check_stack_release.py --phase published --revision "$RC1_COMMIT_B" --remote origin
```

Run the checker from the selected full release carrier. In this sparse review
worktree it is absent; the inspected frozen script can instead be extracted to
scratch and invoked with the installed toolchain's Python and explicit
`--root /path/to/release-carrier`. The system `python3` alone did not supply the
toolchain import when the checker was extracted outside its repository layout.
No checker modification was needed.

For fresh public STDO acquisition, set `RC1_RELEASE_REPOSITORY` to the frozen
literal public endpoint and use a new `RC1_FRESH_STORE`. This command path
provides corpus/plugin acquisition; complete companion acquisition uses the
existing `cohort-update` path:

```sh
stdo --store "$RC1_FRESH_STORE" cohort-update \
  --definition "$RC1_CONSUMER_DEFINITION" --selection "$RC1_CONSUMER_SELECTION" --dry-run
stdo --store "$RC1_FRESH_STORE" cohort-update \
  --definition "$RC1_CONSUMER_DEFINITION" --selection "$RC1_CONSUMER_SELECTION" \
  --accept-plan-sha256 "$RC1_ACCEPTED_PLAN_SHA256"
stdo --store "$RC1_FRESH_STORE" status --definition "$RC1_CONSUMER_DEFINITION" --verify
```

The selection must identify that fixture's exact definition ID, an annotated
child tag at commit B carrying `stack_release.json`, its direct tag object and
repository, both companion Products, their exact definition members, explicit
nonoverlapping install roots, native links, immutable definition/release-record
URLs and declared derived-context bindings. Each companion must already have
exactly one selected composition in the consumer definition. An empty
`derived_context` list is valid only for a genuinely fresh fixture with none.
These are required inputs, not values to guess from an archive. The included
`GATE_INPUTS.json` records their present absence. External existing-consumer
migration remains outside default publication scope.

## Evidence and reading boundary

The deciding implementation is at entry HEAD:
`specification_methodology/v2/src/stdo_toolchain/git_source.py:406`,
`manifest.py:53`, `manifest.py:131`, `cli.py:32`,
`cohort_assets.py:74`, `cohort_update.py:445`, and
`scripts/check_stack_release.py:495`, `:538`, `:853`, `:1317`.
The owning contracts are full `STACK_RELEASE.md`; current `stack_release.json`;
common `PRODUCT.md` Product Boundary, Dependencies and Acceptance, Construction
Authority and Open Owner Decisions; `requirements/A_C_DEPENDENCY.md`; the exact
installed RC2 RELEASE_METHOD's subtree, exact-cut, cohort, Product-subject and
acceptance clauses; and the admitted ACTIVATION/PACING records.

No held expectations, private peer worktree contents or peer candidate were
read. The full common Product was initially requested in an oversized batch;
that output was truncated, and only the deciding sections were then reread.
Acquisition accounting conservatively charges the whole initially requested
file. This return does not assert a full Product-content or full tooling audit.
There was no additional paid actor call, checker qualification run, external
network call, installation, Git mutation, candidate repair or publication.
