# Installing standalone V3 packages

Use `stdo-toolchain 0.1.5` or later. From the repository root, install the current
toolchain implementation with `pipx install --force ./specification_methodology/v2`.
Its source location does not limit the method version it can install.

## Release package

An immutable annotated V3 cut may contain this package at
`specification_methodology/v3/`:

```text
standards/
plugins/spec/                 # carried when present
LICENSE
release/release-note.md
```

The older `specification/standards/` source layout remains supported. A cut
must contain exactly one recognized STDO layout for its selected version.
The installer does not choose `build_tenants/common`, Claude, or Codex, and
does not turn construction commits into releases. Publishing the reviewed
package and assigning its immutable release ref remain separate operations.

No a_c implementation, formal interpretation, or STDO Representation build is
required for this package installation. Every member actually present in the
selected standards and plugin directories is installed and verified. This
does not omit a standard merely because it describes axiomatic calculus.

Once an exact V3 cut is published, use its release record's cut and digest:

```sh
STDO_V3_CUT='<published-immutable-v3-cut>'
STDO_V3_MANIFEST='<published-installed-manifest-sha256>'
stdo install "$STDO_V3_CUT" --manifest-sha256 "$STDO_V3_MANIFEST"
stdo verify "$STDO_V3_CUT" --manifest-sha256 "$STDO_V3_MANIFEST"
stdo resolve "stdo://releases/${STDO_V3_CUT}/standards/README.md"
stdo resolve "stdo://releases/${STDO_V3_CUT}/standards/frames/bootstrap.md"
```

`manifest` and `install` also accept `--repository <repository>` for an exact
release in another Git source. Installation changes the shared store; it does
not change any consumer's Product Definition. The manifest retains canonical
logical `specification/standards` paths for digest compatibility while its Git
tree fields identify the actual published package.

## Consumer setup and migration

A new consumer can resolve `standards/templates/PRODUCT_DEFINITION_TEMPLATE.json`
from the selected cut, fill in its identity, local authorities and locators,
and bind that cut's exact manifest digest. `stdo sync --definition <file>` then
installs its pinned basis; `stdo bootstrap --definition <file>` writes the
declared agent blocks. Verify each selected entrypoint with `stdo resolve`.

An existing V2 consumer needs an explicit owner-reviewed route migration in
addition to a basis change. The current standalone V3 package changes these
entrypoints:

| V2 route | V3 route |
|---|---|
| `standards/authority_compressions/stdo_bootstrap.md` | `standards/frames/bootstrap.md` |
| `standards/REFERENCE_FRAME_METHOD.md` | `standards/REFERENCE_FRAME.md` |
| `standards/STDO_REFERENCE_FRAME_BASELINE.md` | `standards/EXECUTIVE_BASELINE.md` |

Review other selected members, fragments, reference-frame bases and local
authority before using them under V3. These correspondences locate members;
they do not establish equivalence of method meaning. `adopt --dry-run` and its
accepted plan change only the basis and `$schema`, preserving other fields.
`status`, schema validation, and bootstrap installation do not prove that all
authored routes resolve. A green structural check is not completed migration.

`cohort-update` retains its complete selected-cohort contract. It is not needed
to install this standalone method package and has not been changed to bypass
its companion requirements.
