# STDO Project Quickstart

This guide adds STDO governance to an existing project without changing that
project's folder structure. The result is one Product Definition Overlay that
selects an exact immutable STDO release, locates the project's existing `WHAT`
and `HOW`, and gives agents a small stable discovery bootstrap.

For requirement iteration, ticketing, code/test activation, review, and
delivery status, continue with [Using STDO](plugins/spec/references/GETTING_STARTED.md).

## The Three Things To Keep Separate

- The immutable STDO RC cut owns the selected methodology.
- `stdo_<label>.json` owns the project's exact selection and locator mapping.
- The shared toolchain store contains verified installed bytes; its local path
  is derived machine state and never belongs in the Product Definition.

The moving `specification_methodology/v<version>` tag is the shared-source Git
discovery selector for the highest-ordinal published immutable RC on that line.
It never governs a project directly. Historical unqualified selectors remain
frozen history.

## Prerequisites

- Git
- Python 3.11 or newer
- `pipx`, or another isolated Python application installer
- An immutable STDO cut of the form `v<version>-rc.<n>`

## 1. Install The Toolchain Manager

From the Specification Stack repository root while developing the manager:

```sh
pipx install --force ./specification_methodology
```

When already inside the `specification_methodology/` project directory, use
`pipx install --force .`. The explicit replacement prevents an older manager
from remaining active when the selected cut needs newer ref-resolution
behavior.

For the coordinated STDO 2.5.0 RC4 cut, install from its exact qualified Git
ref and nested Python project after publication:

```sh
pipx install --force \
  "git+https://github.com/foolishimp/specification_methodology.git@specification_methodology/v2.5.0-rc.4#subdirectory=specification_methodology"
```

Confirm the executable is available:

```sh
stdo --version
```

RC4 retains `stdo-toolchain 0.1.2`. Do not install from the moving qualified
selector when reproducibility matters. Historical root-layout cuts use their
historical unqualified refs and do not use the nested `subdirectory` fragment.

## 2. Install One Immutable STDO Cut

Keep the product-local cut distinct from its qualified Git transport ref:

```sh
STDO_CUT='v2.5.0-rc.4'

stdo install "$STDO_CUT"
stdo verify "$STDO_CUT"
```

STDO 2.5.0 RC4 uses product-local cut `v2.5.0-rc.4` and qualified Git ref
`specification_methodology/v2.5.0-rc.4`. Public `stdo:` URIs and `stdo
install` continue to use the product-local cut.

Keep the `manifest_sha256` returned by `install` or `verify`. The Product
Definition pins both the immutable cut and that digest.

The default shared store is platform-specific. Override it when needed with
`STDO_STORE` or the global `--store <path>` option. Never write the resulting
machine-local path into a Product Definition.

## 3. Install Both Project Templates

Resolve both templates from the same installed cut:

```sh
STDO_TEMPLATE_PATH="$(
  stdo resolve \
    "stdo://releases/${STDO_CUT}/standards/templates/PRODUCT_DEFINITION_TEMPLATE.json" |
    python3 -c 'import json, sys; print(json.load(sys.stdin)["path"])'
)"
STDO_FRAME_BASIS_TEMPLATE="$(
  stdo resolve \
    "stdo://releases/${STDO_CUT}/standards/templates/PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md" |
    python3 -c 'import json, sys; print(json.load(sys.stdin)["path"])'
)"
```

Do not copy either target separately. Run the single, tested two-target
transaction under
[New Project](plugins/spec/references/GETTING_STARTED.md#new-project) with these
exact resolved paths. It preflights both sources and targets before writing,
refuses every overwrite, and removes only its own staged or published outputs
if either finalization fails.

The installed frame-basis file is not accepted merely because it exists.
Replace every placeholder, bind it to the project's exact Product and work
authorities, and record the accepting decision before treating it as the
applicable basis.

Use:

- `stdo_default.json` for one default product definition;
- `stdo_<label>.json` for a named product definition; or
- several named definitions for several independently governed products.

Place each definition at the logical root of the product it describes. The
project's existing directories and documents can stay where they are.

## 4. Fill The Overlay

Start by replacing the release placeholders:

```json
{
  "$schema": "stdo://releases/<immutable-cut>/standards/schemas/product-definition.schema.json",
  "constitution": {
    "stdo": {
      "source": {
        "repository": "https://github.com/foolishimp/specification_methodology.git"
      },
      "selector": "stdo://channels/<version>",
      "basis": {
        "uri": "stdo://releases/<immutable-cut>/",
        "manifest_sha256": "<64-lowercase-hex-digest>"
      }
    }
  }
}
```

Then bind the project's actual surfaces:

| Question | Product Definition field |
|---|---|
| Which mutable product-definition line is this? | `product.definition_id` |
| Where is its project root? | `product.source_project` |
| What constitution governs it? | `constitution` and `local_constitution` |
| Which shared evaluation frames apply? | `reference_frame_bases` |
| What is the product? | `what.intent`, `what.product`, `what.specification` |
| How is it realized? | `how.common`, `how.build_tenants` |
| Where does work coordination live? | `ticketing` |
| Which other products are explicitly related? | `composition` |

Important rules:

- `product.definition_id` identifies the mutable definition line, not an
  immutable released Product.
- The selector is discovery input. The basis URI and manifest digest are the
  operative selection.
- Relative project references overlay the existing layout; they do not require
  `specification/`, `build_tenants/`, or `.ai-workspace/` directories.
- Bootstrap targets are relative to the resolved `product.source_project` and
  cannot use absolute paths, parent traversal, symlinks, or reparse points.
- Delete illustrative local disambiguations or composition edges that do not
  apply. Retain explicit empty arrays where the schema requires them.

The complete field-level guide is in
[`specification/standards/templates/README.md`](specification/standards/templates/README.md).

## 5. Synchronize And Verify

Synchronize the exact basis already selected by the definition:

```sh
stdo sync --definition stdo_default.json
stdo status --definition stdo_default.json --verify
```

`sync` never consults the moving selector and never edits the Product
Definition. A missing cut is installed only when its reconstructed manifest
matches the pinned digest.

## 6. Install The Agent Bootstrap

Preview every target first:

```sh
stdo bootstrap --definition stdo_default.json --dry-run
```

Then install or refresh the marker-owned blocks:

```sh
stdo bootstrap --definition stdo_default.json
```

Only the correctly ordered `STDO_BOOTSTRAP_START` to `STDO_BOOTSTRAP_END` span
is manager-owned. Existing prefix and suffix bytes remain project-owned.

## Daily Use

The shell command `stdo status` checks the selected basis. It does not report
Product delivery status:

```sh
stdo status --definition stdo_default.json --verify
```

Before governed work, resolve the accepted Project Reference-Frame Basis named
by the Product Definition, current Goals, affected authority, and admitted work
carrier. Read only the context material to the requested action.

Recreate the exact selected installation on another machine:

```sh
stdo sync --definition stdo_default.json
```

Resolve an owning standard:

```sh
stdo resolve \
  "stdo://releases/${STDO_CUT}/standards/SPEC_METHOD.md"
```

The shared Claude/Codex plugin provides these conversational shorthands:

| Say | Skill |
|---|---|
| `stdo help` | `stdo-help` |
| `stdo ticket` | `stdo-ticket` |
| `stdo work` | `stdo-work` |
| `stdo review` | `stdo-review` |
| `stdo status` | `stdo-status` |

See [Using STDO](plugins/spec/references/GETTING_STARTED.md) for the complete
workflow, role split, triage boundary, and both host installation commands.

## Adopt The Latest Published RC

Adoption is deliberately two-phase. First obtain the read-only plan:

```sh
stdo adopt --definition stdo_default.json --dry-run
```

Review the reported target cut, tag object, commit, tree, manifest digest, and
`plan_sha256`. If that exact transition is accepted, pass the digest in a
separate invocation:

```sh
stdo adopt --definition stdo_default.json \
  --accept-plan-sha256 <plan_sha256>
```

The manager re-derives the plan before installation or mutation. Selector,
target, manifest, or Product Definition drift invalidates the accepted digest.
Run another dry-run and review the new subject instead of bypassing the refusal.

The channel resolver enumerates the line's immutable RC tags and refuses a
lagging selector instead of selecting an older cut. Channel adoption also
refuses a same-line downgrade. To intentionally retain an older cut, keep its
exact `stdo://releases/v<version>-rc.<n>/` URI and manifest digest in the Product
Definition and use `sync`; do not use the latest-version channel for that
choice.

## Monorepos And Hierarchical Repositories

Discover and inspect every definition below a workspace root:

```sh
stdo fleet status --root /path/to/workspace
stdo fleet verify --root /path/to/workspace
```

Fleet writes require explicit whole-selection authorization:

```sh
stdo fleet sync --root /path/to/workspace --all
stdo fleet bootstrap --root /path/to/workspace --all --dry-run
stdo fleet bootstrap --root /path/to/workspace --all
```

Fleet adoption also uses two phases:

```sh
stdo fleet adopt --root /path/to/workspace --all --dry-run
stdo fleet adopt --root /path/to/workspace --all \
  --accept-plan-sha256 <plan_sha256>
```

Directory nesting creates no implicit inheritance or product composition. Each
definition names its own basis and every composition edge explicitly.

## Common Refusals

| Refusal | What to check |
|---|---|
| Schema cut differs from basis | `$schema` and `constitution.stdo.basis.uri` must name the same immutable cut |
| Manifest digest differs | Copy the digest for the exact selected cut; do not substitute another installation |
| Adoption plan differs | The selector, target, manifest, or definition changed; create and review a new dry-run |
| Version-line selector lags | Advance `specification_methodology/v<version>` to the highest published immutable RC; the manager will not adopt the older alias target |
| Channel would downgrade | Retain an older immutable basis explicitly with `sync`, or advance through the latest channel; channel adoption never moves backward |
| Bootstrap target escapes | Make the target relative to `product.source_project` and remove traversal or redirected components |
| Duplicate definition identity | Give independently governed product-definition lines distinct `product.definition_id` values |
| Installed release is damaged | Inspect the reported missing, extra, changed, redirected, or special entry; the manager will not repair it in place |

## Next References

- [`README.md`](README.md) — repository and command overview
- [`design/TOOLCHAIN_MANAGER.md`](design/TOOLCHAIN_MANAGER.md) — executable
  boundary and refusal design
- [`specification/standards/SPEC_METHOD.md`](specification/standards/SPEC_METHOD.md)
  — Product Definition and toolchain authority
- [`specification/standards/RELEASE_METHOD.md`](specification/standards/RELEASE_METHOD.md)
  — immutable RC and selector law
