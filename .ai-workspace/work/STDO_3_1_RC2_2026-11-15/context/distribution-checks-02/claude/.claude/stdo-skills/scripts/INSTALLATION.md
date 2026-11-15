# Install the selected Skills package

This installs current Codex or Claude bindings, Purpose Context access and the
current first-use guides into a selected workspace. The native method and Purpose
Context remain separately selected Products. Release mode binds the exact 3.1.0-rc.2 native cut and separate Product pins.
The explicit development mode remains unversioned. Neither mode upgrades an
existing installation or adopts a method on the consumer's behalf.

## Select the inputs

Use Python 3.11+ and absolute paths. Before installation, obtain:

- An existing target Product Definition and its verified, complete native STDO
  installation. A new project uses that method's Getting Started/templates to
  establish these first.
- The exact STDO manager that resolves that installation. For a private/custom
  store, use its existing launcher so `status` and the installer use the same
  store. A default global `stdo` is not interchangeable with that launcher.
- The matching independent Purpose Context distribution selected by this Skills
  package's `specification/composition/DEPENDENCIES.json`. Verification checks
  its pinned public manifest and every listed member; no visual runtime is needed.

For the selected release, obtain `stdo-products-v3.1.0-rc.2.zip` and
`cohort-release-v3.1.0-rc.2.json` from the same immutable release and verify their
published identities/member inventories. Select its `stdo_skills` package and
`purpose_context` Product. The native method is acquired separately through its
manager using the shared release recipe. See [release and migration](../RELEASE.md).
Consumers of that package do not rebuild it.
All `/absolute/...` values below are placeholders for your selected paths.

```sh
stdo_python=/absolute/path/to/python3
stdo_package=/absolute/verified/products/stdo_skills

stdo_workspace=/absolute/target/workspace
stdo_definition=/absolute/target/stdo_project.json
stdo_manager=/absolute/selected/stdo
stdo_context_root=/absolute/selected/purpose_context
stdo_host=codex
"$stdo_manager" status --definition "$stdo_definition" --verify
```

Require `installed: true`, `valid: true` and no failures. Set `stdo_method_root`
to the exact `path` returned by that command; it contains `manifest.json` and
`standards/`. Do not substitute the source tree or a different release. Select
`stdo_host=claude` for Claude. The commands work in bash or zsh.

```sh
stdo_method_root=/absolute/verified/native-release
"$stdo_python" -B "$stdo_package/scripts/manage_skills.py" plan \
  --package "$stdo_package" --workspace "$stdo_workspace" --host "$stdo_host" \
  --definition "$stdo_definition" --method-root "$stdo_method_root" \
  --stdo "$stdo_manager" --python "$stdo_python" \
  --purpose-context "$stdo_context_root"
```

Inspect the selected components and destination roots. The installer validates
the package, method manager/store, complete native plugin, interpreter and
Purpose Context before writing. It refuses collisions with existing owned roots.
To include optional visual documentation, add `--visual-root /absolute/selected/a_c`
to both plan and install. That separately pinned component adds `stdo-project`;
its extraction prerequisites belong to Representation Tools. No Lean is required.

## Install and verify

Invoke the selected package's installer with the same inputs:

```sh
mkdir -p "$stdo_workspace"
"$stdo_python" -B "$stdo_package/scripts/manage_skills.py" install \
  --package "$stdo_package" --workspace "$stdo_workspace" --host "$stdo_host" \
  --definition "$stdo_definition" --method-root "$stdo_method_root" \
  --stdo "$stdo_manager" --python "$stdo_python" \
  --purpose-context "$stdo_context_root" \
  > "$stdo_workspace/stdo-install-$stdo_host.json"
cat "$stdo_workspace/stdo-install-$stdo_host.json"
```

Continue only after an `installed` result. Retain its exact receipt path and
`receipt_sha256`; they identify the files this installation owns.

```sh
stdo_receipt_sha=$("$stdo_python" -c 'import json,sys; print(json.load(open(sys.argv[1]))["receipt_sha256"])' "$stdo_workspace/stdo-install-$stdo_host.json")
"$stdo_python" -B "$stdo_package/scripts/manage_skills.py" verify \
  --workspace "$stdo_workspace" --host "$stdo_host" \
  --receipt-sha256 "$stdo_receipt_sha"

case "$stdo_host" in
  codex) stdo_host_root="$stdo_workspace/.agents" ;;
  claude) stdo_host_root="$stdo_workspace/.claude" ;;
esac
stdo_adapter="$stdo_host_root/skills/stdo-context/scripts/provider.py"
"$stdo_python" -B "$stdo_adapter" describe \
  > "$stdo_workspace/stdo-context-$stdo_host.json"
cat "$stdo_workspace/stdo-context-$stdo_host.json"
stdo_public_pin=$("$stdo_python" -c 'import json,sys; print(json.load(open(sys.argv[1]))["manifest_sha256"])' "$stdo_workspace/stdo-context-$stdo_host.json")
```

The installed core five wrappers retain the selected native frontmatter and
canonical workflow references. Claude also binds native refresh. Both hosts add
one thin `stdo-context` adapter and current guides under `stdo-skills/` for a
release package (`stdo-skills-dev/` in development mode).
The returned canonical skill and catalog stay in the independently pinned Purpose
Context Product. Keep those selected dependency roots and the manager available.

Continue with [Getting Started](../GETTING_STARTED.md) for purpose selection,
actual query construction and expected work/review outcomes. Public operations
are forwarded unchanged through `"$stdo_python" -B "$stdo_adapter" context -- ...`.
For a full runtime recheck, use:

```sh
"$stdo_python" -B "$stdo_package/scripts/manage_skills.py" check-runtime \
  --configuration "$stdo_host_root/stdo-skills/CONFIG.json"
```

Installation verifies a binding. It does not adopt the SDLC default, replace
the target constitution, prove semantic coverage or demonstrate automatic host
pickup. The release package requires its actual native method to match the
consumer's verified Product basis. Both new indexes bind that exact native cut.
The retained development SDLC entry remains a separate explicit source selection.
For development mode, use `stdo-skills-dev/CONFIG.json` for the runtime check.

## Remove or replace an installation

Removal is an explicit action, not a setup step. Use the recorded host, workspace
and receipt digest with the installer that owns that receipt:

```sh
"$stdo_python" -B "$stdo_package/scripts/manage_skills.py" remove \
  --workspace "$stdo_workspace" --host "$stdo_host" \
  --receipt-sha256 "$stdo_receipt_sha"
```

This removes only exact receipt-owned roots, including their guide copies. It
preserves unrelated files and does not require an available external provider.
Changed owned files, broadened roots or a changed receipt refuse removal; preserve
and reconcile them. An interrupted install may leave partial effects: a refusal
is not a rollback. Do not retry by deleting broad host directories.

There is no implicit update or global migration. To replace an installation,
first retain its receipt and resolve any local changes, then remove it through
its owning installer and install the newly selected package into fresh roots.
Old 3.0.5-era receipts require their original installer. Preserve immutable
releases and existing global installations. Final release packaging must bind
indexes, assessments and host payloads to its actual source cut.

## Build a package from authorized source

Consumers use the verified distributed package above. Release builders invoke
the package constructor only after the actual native tag/install exists:

```sh
"$stdo_python" -B stdo_skills/scripts/package.py --out /absolute/fresh/skills-package \
  --version 3.1.0-rc.2 --method-root "$stdo_method_root" \
  --method-manifest-sha256 b691b0249c82ff39033ae636c4eaa0ab44bafee3732c79a227eb9409d53776c4 \
  --purpose-context "$stdo_context_root"
```

The version and digest must agree with the actual native manifest. For an
unversioned source development package, omit all three release arguments.
These modes keep separate inventories/runtime receipts and do not turn local
construction into public release or semantic qualification.

For release construction, `--purpose-context` selects the actual portable
Purpose Context tree and verifies its public members/native binding. Its pin is
written into this package's dependency declaration; the source development
dependency stays unchanged. The package inventory records that transformation.
