# Native 3.0.1 RC1 preparation

This is a bounded Writer's preparation, not independent assessment of its own output. It targets an immutable **test candidate** with the predecessor's claim scope unless subsequent evidence establishes more. No inherited acceptance, method qualification or consumer adoption is asserted.

Root reviews the script and this recipe before effects. Root exclusively performs every Git write/ref operation, installation, fresh-actor invocation and publication. `native_release.py` itself permits only read-only Git verbs and writes new records inside this directory. It never commits, tags, fetches, installs or pushes. All output names are create-only. A failed step leaves its partial run visible; do not repurpose it or overwrite its records. Use a new run directory after repair. The preparation delivered here has no candidate-dependent outputs.

## Bound inputs and identities

- Builder: installed STDO `v2.5.1-rc.2`, manifest `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`.
- Native predecessor: `0a04feb788c080183b58cf4a162e88372be1d87e`, manifest `069285ad5a79d59ca2dd835e34a54b3e537b0eeef99c29994b18c339dbe62232`.
- New cut: `v3.0.1-rc.1`; namespace `specification_methodology`; native package root `specification_methodology/v3`.
- The source candidate commit and its package path are supplied after the source freeze. Its package is projected blob-for-blob and mode-for-mode into the native tree. The new native commit has exactly the selected old native commit as parent. The source candidate is a separately identified construction origin, not a fabricated Git parent of the native commit.
- The complete native repository tree contains only that payload under `specification_methodology/v3`. Unexpected root paths, package extras, missing members, changed modes, symlinks, submodules and special Git entries refuse. The payload must contain its release note, licences, entry and target-version plugin manifests. File counts are derived, never assumed to remain 81.
- `SOURCE_SELECTION.json` is emitted only after a real local annotated tag and the manager's manifest are checked. Its `native` coordinates identify the release-shaped commit/path/tree; `source_candidate` identifies the construction commit/path/tree. The representation Writer consumes this same selection with its emitted SHA256.

The inventory digest is SHA256 of the path-sorted array of `{path,bytes,sha256}`, encoded as UTF-8 JSON with sorted object keys, no whitespace and unescaped Unicode. Paths are POSIX and package-relative. Git blob/mode fields remain in the complete rows but are excluded from this particular digest. The installed manifest is an added manager artifact and is excluded from the source payload inventory.

## Root recipe: source freeze through local install

Replace the uppercase coordinates with the selected exact values; they are intentionally not guessed. Run steps sequentially and stop on any nonzero exit. These commands are a future recipe, not execution evidence. Use the 301 worktree for `--repo`, so the manifest path is repository-relative.

```sh
release_repo=/Users/jim/src/apps/specification_methodology-301
native_dir="$release_repo/specification_methodology/v3/.ai-workspace/work/STDO301_DELIVERY/native-release"
native_tool="$native_dir/native_release.py"
native_run="$native_dir/runs/rc1-001"
source_commit=FULL_FROZEN_SOURCE_COMMIT
source_package=specification_methodology/v3/build_tenants/common

python3 -I -S -B "$native_tool" prepare --repo "$release_repo" \
  --run "$native_run" --source-commit "$source_commit" --source-path "$source_package"
```

Record the printed `source.json` SHA256 as `source_sha256`. `prepare` validates the immutable source and emits a NUL-delimited index recipe, source inventory, commit message and tag message. It does not materialize or modify the common candidate. Root then creates the native tree using a fresh alternate index; this does not replace the checkout's index or working tree:

```sh
native_git_index="$native_run/native.index"
GIT_INDEX_FILE="$native_git_index" git -C "$release_repo" read-tree --empty
GIT_INDEX_FILE="$native_git_index" git -C "$release_repo" update-index -z --index-info < "$native_run/native-index-info.z"
native_tree=$(GIT_INDEX_FILE="$native_git_index" git -C "$release_repo" write-tree)
native_commit=$(git -C "$release_repo" commit-tree "$native_tree" \
  -p 0a04feb788c080183b58cf4a162e88372be1d87e \
  -F "$native_run/native-commit-message.txt")
git -C "$release_repo" tag -a -F "$native_run/tag-message.txt" \
  specification_methodology/v3.0.1-rc.1 "$native_commit"

python3 -I -S -B "$native_tool" attest --repo "$release_repo" \
  --run "$native_run" --source-sha256 "$source_sha256" --native-commit "$native_commit"
```

Record the emitted `native.json` SHA256 as `native_sha256`. Do not force an existing tag or substitute a fictional object ID. The tag annotation carries the exact source commit/path/tree, predecessor and test-candidate standing. The `attest` check binds the genuine tag object and peel, whole repository tree, exact one-parent relation and source trailers.

The installed manager is `/Users/jim/.local/bin/stdo` version 0.1.5, using `/Users/jim/.local/pipx/venvs/stdo-toolchain/bin/python`. It already accepts the standalone V3 layout; no V2 toolchain edit is needed. `TMPDIR` confines the manager's temporary Git snapshot underneath this run. Use shell no-clobber behavior for redirected reports.

```sh
mkdir "$native_run/tmp"
set -C
TMPDIR="$native_run/tmp" stdo manifest v3.0.1-rc.1 \
  --repository "$release_repo" > "$native_run/manifest-report.json"

python3 -I -S -B "$native_tool" seal --repo "$release_repo" \
  --run "$native_run" --source-sha256 "$source_sha256" \
  --native-sha256 "$native_sha256" --manifest-report "$native_run/manifest-report.json"
```

Record the emitted `SOURCE_SELECTION.json` SHA256 as `selection_sha256`. Read `native.manifest_sha256` as `manifest_sha256`. The script extracts canonical manifest bytes from the manager's report and independently compares the exact identities, complete members and canonical path-sensitive standards digest. It emits `stdo-v3.0.1-rc.1-manifest.json` and its checksum. Do not publish the CLI report wrapper as the manifest asset.

```sh
TMPDIR="$native_run/tmp" stdo --store "$native_run/local-store" install v3.0.1-rc.1 \
  --repository "$release_repo" --manifest-sha256 "$manifest_sha256" \
  > "$native_run/install-local.json"
stdo --store "$native_run/local-store" verify v3.0.1-rc.1 \
  --manifest-sha256 "$manifest_sha256" > "$native_run/verify-local.json"
python3 -I -S -B "$native_tool" installed --run "$native_run" \
  --selection-sha256 "$selection_sha256" --store "$native_run/local-store" \
  --verify-report "$native_run/verify-local.json" --label local
```

This is a fresh actual installation from an annotated local tag. It requires Git and the existing manager, but no external service or network dependency beyond local repository acquisition. It uses neither the shared install store nor a consumer Product Definition. The independent byte comparison covers every source payload file and the added manifest, rejects extras, and refuses a stale passing verifier report when installed bytes change.

Run the four selected task packets against this installed root, using separate fresh actors and the independent oracle carrier described below. These bounded tasks cannot discharge all inherited C3 or representation actual-use gaps.

## Root recipe: exact assets and guarded publication

After the separately reviewed supplemental representation is frozen from the same `SOURCE_SELECTION.json`, bind its archive and the native manifest. Existing old35fb assets remain untouched. This command emits deterministic sidecars and an exact asset inventory; it performs no publication:

```sh
python3 -I -S -B "$native_tool" assets --run "$native_run" \
  --selection-sha256 "$selection_sha256" \
  --file "$native_run/stdo-v3.0.1-rc.1-manifest.json" \
  --file "$representation_archive"
```

Record the emitted `assets.json` SHA256 as `assets_sha256`. The selected files and generated sidecars are the release assets. Do not substitute a different archive after this point. The separate representation evidence must establish its claimed scope; asset hashes do not do so.

Root creates the local selector and native branches only after the preceding gates and applicable source/review decisions are satisfied. `carrier_commit` is the reviewed main carrier B containing the source freeze and selected records/assets. It must descend from both the source candidate and the observed current remote main. Do not retarget either native immutable cut to B.

```sh
git -C "$release_repo" tag -a -m 'STDO 3.0.1 selector: immutable RC1 test candidate; acceptance pending' \
  specification_methodology/v3.0.1 "$native_commit"
git -C "$release_repo" branch rc/specification_methodology/3.0.1 "$native_commit"
git -C "$release_repo" branch release/specification_methodology/3.0.1 "$native_commit"

python3 -I -S -B "$native_tool" publication-plan --repo "$release_repo" \
  --run "$native_run" --selection-sha256 "$selection_sha256" \
  --assets-sha256 "$assets_sha256" --carrier-commit "$carrier_commit"
```

The plan rechecks exact native identity, installed bytes and asset bytes, snapshots all remote refs, refuses preexisting new-line destinations and any published 3.0.1 RC, and emits one exact `push_argv`. It contains five destination refs: main at B, RC/release branches at C, immutable annotated tag T, annotated selector S. Each immutable tag is create-only; each mutable destination uses its captured expected direct object ID or absence in an explicit lease. Full source object IDs prevent local ref drift from changing the checked bytes. The endpoint is fixed to `https://github.com/foolishimp/specification_methodology.git`.

Root reviews the plan, records its SHA256 as `plan_sha256`, and only then executes its exact argument vector. Do not reconstruct it manually, weaken leases, retry with force, or split the transaction. A lease failure stops the operation; Root reacquires and requalifies a new plan/run. Existing V2/common/old V3 refs are outside the push set.

```sh
python3 -I -S -B -c 'import hashlib,json,pathlib,subprocess,sys
p=pathlib.Path(sys.argv[1]); b=p.read_bytes()
if hashlib.sha256(b).hexdigest()!=sys.argv[2]: raise SystemExit("plan changed")
subprocess.run(json.loads(b)["push_argv"],check=True)
' "$native_run/publication-plan.json" "$plan_sha256"

python3 -I -S -B "$native_tool" published --repo "$release_repo" \
  --run "$native_run" --plan-sha256 "$plan_sha256"
```

The remote proof checks direct objects, annotated peels and all other observed refs unchanged. Concurrent unrelated ref changes stop the full-preservation claim for reconciliation. This is transport evidence, not semantic or owner acceptance.

Root may then publish the exact selected assets and previously reviewed notes with the existing GitHub CLI. `--verify-tag` prevents GitHub from manufacturing a tag on main. Pass the precise paths listed in `assets.json`, including its generated sidecars; do not use broad directory globs.

```sh
gh release create specification_methodology/v3.0.1-rc.1 \
  --repo foolishimp/specification_methodology --verify-tag --prerelease --latest=false \
  --target "$native_commit" \
  --title 'STDO 3.0.1 RC1 test candidate' --notes-file "$reviewed_release_notes" \
  "$native_run/stdo-v3.0.1-rc.1-manifest.json" \
  "$native_run/asset-checksums/stdo-v3.0.1-rc.1-manifest.json.sha256" \
  "$representation_archive" "$representation_checksum"
```

Here `representation_checksum` names the generated sidecar under `asset-checksums`, not a recomputed or independently supplied file. Record actual release/asset metadata and download the four exact assets into a new directory:

```sh
gh api repos/foolishimp/specification_methodology/releases/tags/specification_methodology%2Fv3.0.1-rc.1 \
  > "$native_run/github-release.json"
gh api repos/foolishimp/specification_methodology/releases/latest \
  > "$native_run/github-latest.json"
representation_name=${representation_archive##*/}
gh release download specification_methodology/v3.0.1-rc.1 \
  --repo foolishimp/specification_methodology --dir "$native_run/public-downloads" \
  --pattern 'stdo-v3.0.1-rc.1-manifest.json' \
  --pattern 'stdo-v3.0.1-rc.1-manifest.json.sha256' \
  --pattern "$representation_name" --pattern "$representation_name.sha256"
```

Check the actual release has `draft: false`, `prerelease: true`, target C and the selected tag; its ID differs from `github-latest.json`. Compare actual asset names/byte lengths to `assets.json`, preserve the published URLs, then verify the downloaded bytes and public install:

```sh
python3 -I -S -B "$native_tool" check-assets --run "$native_run" \
  --assets-sha256 "$assets_sha256" --directory "$native_run/public-downloads"

TMPDIR="$native_run/tmp" stdo --store "$native_run/public-store" install v3.0.1-rc.1 \
  --repository https://github.com/foolishimp/specification_methodology.git \
  --manifest-sha256 "$manifest_sha256" > "$native_run/install-public.json"
stdo --store "$native_run/public-store" verify v3.0.1-rc.1 \
  --manifest-sha256 "$manifest_sha256" > "$native_run/verify-public.json"
python3 -I -S -B "$native_tool" installed --run "$native_run" \
  --selection-sha256 "$selection_sha256" --store "$native_run/public-store" \
  --verify-report "$native_run/verify-public.json" --label public
```

Fresh public reacquisition must reproduce the same manifest and complete payload. Verify nondraft/prerelease/not-latest flags explicitly. No consumer adoption or global plugin activation is part of this sequence. Final source bookkeeping uses a later carrier commit and cannot move the native tag.

## Focused installed-route tasks

`qualification/tasks/` contains four actor packets derived from the approved proposal, before acquisition of candidate-author changes. `qualification/oracles/expected.json` is a separate assessor-only carrier. Root pins both, supplies only the chosen task to a fresh actor, binds exact installed manifest/root, capability, permitted output, acquisition routes, time/spend/context envelope and required measurement, and retains the actor's actual inputs/results. Do not provide the oracle or author session to the actor. A nonauthor assessor judges the results; this Writer cannot supply independent assessment of this harness or these expectations.

These tasks test installed acquisition and the listed P301 distinctions. They are not whole-method practical qualification, a provider-family-independence assertion, or proof that every C3 frame fits its envelope. The actor must expose missing clauses, access or ambiguity rather than silently use source author text or the proposal.

## Reproduce the delivered source-independent controls

```sh
python3 -I -S -B "$native_dir/test_native_release.py"
python3 -I -S -B "$native_tool" --help
```

The controls create only synthetic byte/path fixtures under `scratch/`; they perform no Git mutation, candidate build, manager installation, remote operation or actor invocation. Candidate-specific staging and end-to-end installation remain unperformed until Root's later activation. The old full-cohort `scripts/check_stack_release.py` is not invoked against its V2 manifest to certify this explicitly selected standalone relation.
