# Native STDO 3.0.2 release recipe

The selected output is a normal immutable standalone release, qualified tag
`specification_methodology/v3.0.2`, logical cut `v3.0.2`, profile `stable-v1`.
Its native parent is `fe4941f56a52ed3697a2b516d8d68948b0ea65d9`. The native
commit contains only the exact selected common payload under
`specification_methodology/v3`. The legacy RC lines and old matched cohort
remain untouched. See [the selection](../SELECTION.md).

`native_release.py` creates new preparation/evidence files and performs only
read-only Git calls. It does not commit, tag, install, push or publish. The
separate Git Writer performs those selected effects. The 23 boundary controls
in `CONTROLS-01.json` exercise synthetic payload/identity/tamper refusals; they
are not an actual release or installation proof.

## Committed source and native cut

Use exact paths and full object IDs returned by the sole Git Writer. Let
`repo` be the checkout, `native_tool` this script, and `native_run` a new
nonexisting directory below this `native-release/` territory. `source_commit`
is the reviewed final source checkpoint; do not use a moving branch name.

```sh
python3 -I -S -B "$native_tool" prepare --repo "$repo" --run "$native_run" \
  --source-commit "$source_commit" \
  --source-path specification_methodology/v3/build_tenants/common
```

Record the returned `source.json` digest as `source_sha256`. The outputs include
exact `native-index-info.z`, commit message and tag message. The Git Writer uses
a separate temporary index, creates a native commit with the declared parent,
and creates the annotated `specification_methodology/v3.0.2` tag using that exact
message. The marker appears exactly once. There is no RC branch or mutable
selector. The selected convenience branch is
`release/specification_methodology/3.0.2` at the native commit.

```sh
python3 -I -S -B "$native_tool" attest --repo "$repo" --run "$native_run" \
  --source-sha256 "$source_sha256" --native-commit "$native_commit"
```

`attest` rejects changed payload paths, bytes, Git modes, parent or annotation.
Record its returned digest as `native_sha256`.

## Distributed manager and isolated installation

Use the exact independently checked `stdo_toolchain-0.1.6-py3-none-any.whl`,
not the installed 0.1.5 manager or a source `PYTHONPATH`. Create an isolated
virtual environment under the run and install that wheel and its declared
Python dependencies. Retain wheel SHA256, pip output, Python version,
`importlib.metadata.version('stdo-toolchain')`, the actual imported
`stdo_toolchain.__file__`, and that file's digest. Use `python -I` for all
manager invocations and remove `PYTHONPATH` from the environment. This prevents
workspace imports from hiding a broken wheel. No global installation changes.

The commands below assume `manager_python` is that environment's Python,
`native_run/tmp` exists, and shell no-clobber mode protects retained reports.

```sh
env -u PYTHONPATH TMPDIR="$native_run/tmp" "$manager_python" -I -m stdo_toolchain.cli \
  manifest v3.0.2 --repository "$repo" > "$native_run/manifest-report.json"
python3 -I -S -B "$native_tool" seal --repo "$repo" --run "$native_run" \
  --source-sha256 "$source_sha256" --native-sha256 "$native_sha256" \
  --manifest-report "$native_run/manifest-report.json"
```

`seal` independently reconstructs the full expected manifest, including
`release.profile = "stable-v1"`, and requires canonical equality. It creates
`SOURCE_SELECTION.json`, `stdo-v3.0.2-manifest.json` and its checksum. Use the
emitted selection digest and native manifest digest in the following commands.

```sh
env -u PYTHONPATH TMPDIR="$native_run/tmp" "$manager_python" -I -m stdo_toolchain.cli \
  --store "$native_run/local-store" install v3.0.2 --repository "$repo" \
  --manifest-sha256 "$manifest_sha256" > "$native_run/install-local.json"
env -u PYTHONPATH "$manager_python" -I -m stdo_toolchain.cli \
  --store "$native_run/local-store" verify v3.0.2 \
  --manifest-sha256 "$manifest_sha256" > "$native_run/verify-local.json"
python3 -I -S -B "$native_tool" installed --run "$native_run" \
  --selection-sha256 "$selection_sha256" --store "$native_run/local-store" \
  --verify-report "$native_run/verify-local.json" --label local
```

Resolve the installed method entry, bootstrap, Product Definition schema and
composition template. This verifies concrete entry paths, not semantic adoption.
The installed proof compares every selected payload member and manifest byte,
rejecting extra or missing entries. Existing stores and consumer bases stay intact.

## Supplemental representation and public assets

Bind the bounded composition/release representation to the same sealed
`SOURCE_SELECTION.json` using `supplement.py build`. Its archive carries exact
selected source documents, authored model, two carriers, provenance, coverage
limits and the existing pinned carrier decoder. It is supplemental to the native
payload; it is not the incomplete earlier whole-method interpretation relabelled.
The portable `verify` path checks custody and both carrier recoveries.

```sh
python3 -I -S -B "$native_dir/supplement.py" build --repo "$repo" \
  --representation "$native_dir/../representation" \
  --selection "$native_run/SOURCE_SELECTION.json" --selection-sha256 "$selection_sha256" \
  --bundle "$native_run/supplement-bundle" \
  --archive "$native_run/stdo-v3.0.2-composition-release-supplement.tar.gz"
# After extraction, this verification needs no originating workspace:
python3 -I -S -B "$extracted/supplement.py" verify --bundle "$extracted"
```

Set `native_dir` to this recipe directory and `extracted` to the archive's
`stdo-v3.0.2-supplement` directory. Rebuilding requires the selected repository
source and decoder pins plus the sealed native selection; the extracted archive
supports portable verification, not a claim of a standalone source rebuild.

Supply primary assets to the native recipe: canonical manifest, exact manager
wheel and the representation `.tar.gz`. `assets` verifies the selected native
manifest and emits checksum sidecars for every primary asset plus `assets.json`.
The wheel has its own distribution identity and source provenance; its presence
does not add executable tooling to the installed methodology payload.

```sh
python3 -I -S -B "$native_tool" assets --run "$native_run" \
  --selection-sha256 "$selection_sha256" \
  --file "$native_run/stdo-v3.0.2-manifest.json" --file "$manager_wheel" \
  --file "$supplement_archive"
```

## Publication and public readback

After source/recipe/manager/representation review and local installed proof,
create the carrier checkpoint containing exact evidence. `publication-plan`
requires that checkpoint to descend from selected source, checks native identity,
assets and installed bytes, fetches remote ref observations read-only, and emits
one atomic push command with explicit destination leases. Its only refs are main,
the stable immutable tag and the selected release branch. The tag must be absent;
legacy same-line aliases or RC tags refuse. The Git Writer executes that command.

```sh
python3 -I -S -B "$native_tool" publication-plan --repo "$repo" --run "$native_run" \
  --selection-sha256 "$selection_sha256" --assets-sha256 "$assets_sha256" \
  --carrier-commit "$carrier_commit"
python3 -I -S -B "$native_tool" published --repo "$repo" --run "$native_run" \
  --plan-sha256 "$plan_sha256"
```

Publish a normal GitHub release for the exact existing tag using `--verify-tag`,
`--prerelease=false` and `--latest=true`, with the complete selected asset paths
and readable release notes, as selected by [PUBLICATION_SELECTION](../PUBLICATION_SELECTION.md).
Retain the returned release record and verify `draft:false`, `prerelease:false`,
exact tag/target and the complete expected asset identity set. Query the public
`repos/foolishimp/specification_methodology/releases/latest` endpoint: its release
ID must match the exact-tag release and its tag must be
`specification_methodology/v3.0.2`, with normal published classification.

Release completion additionally requires downloading every expected asset into a
new directory and passing `check-assets` against the complete frozen inventory and
checksums. Install that downloaded wheel in a second fresh isolated environment,
retain its actual imported module path/version/digest and wheel identity, and
acquire the exact cut from the public Git repository into `public-store`.
Run `installed --label public` with its successful exact-manifest verification
report. A successful push or release-create response alone does not complete
these publication predicates. Latest is discovery metadata; none of these checks
adopts a consumer.

No publication receipt is claimed before these operations occur. Review and
release records state source, transport, semantic and practical limits separately.
