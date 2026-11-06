# Install STDO Skills 3.0.5

This current package supplies independent Codex and Claude host bindings to the
same verified native STDO workflow owner, plus `stdo-project` for representation,
formal reading and code tracing. The older tenant package trees retain historical
source/evidence; they are not the 3.0.5 installation.

First install the exact 3.0.5 method with its ordinary manager and materialize the
cohort's a_c sources into a selected writable tools directory. Verify the target
Product Definition against that installation. Base a_c commands need Python;
optional pinned Graphify and Lean setup is explicit through
`python3 AC_ROOT/scripts/ac.py bootstrap --help`.

For one selected workspace and host:

```sh
python3 SKILLS_ROOT/scripts/manage_skills.py plan --package SKILLS_ROOT --host codex --workspace WORKSPACE --definition PRODUCT_JSON --method-root INSTALLED_305 --ac-root AC_ROOT
python3 SKILLS_ROOT/scripts/manage_skills.py install --package SKILLS_ROOT --host codex --workspace WORKSPACE --definition PRODUCT_JSON --method-root INSTALLED_305 --ac-root AC_ROOT
```

For optional Graphify/code dependencies, pass `--python` with the exact `python` invocation path returned by the private bootstrap in RUNTIME.json on both plan and install. Its virtualenv invocation path is preserved; physical executable identity is pinned separately. Use `--host claude` for Claude. The installer never enables the other host or
changes global settings. It refuses selected-name collisions and requires exact
native plugin and provider identities. It copies native resources together so
relative references remain valid. Retain the returned receipt digest. The public
entries are `$stdo-project` in Codex and `/stdo-project` in Claude, alongside the
native workflow names. Natural discovery and explicit invocation are separate
host observations.

```sh
python3 SKILLS_ROOT/scripts/manage_skills.py verify --host codex --workspace WORKSPACE --receipt-sha256 EXACT_RECEIPT
python3 SKILLS_ROOT/scripts/manage_skills.py remove --host codex --workspace WORKSPACE --receipt-sha256 EXACT_RECEIPT
```

For an update, preserve the previous exact package and receipt, verify and remove
that selected owned installation, then install the new selected package. Modified,
extra, missing or redirected owned files cause refusal; unrelated host files stay
outside the owned set. This is a cooperative single-writer local lifecycle, not
a transaction across filesystem failures. Preserve partial effects and reconcile
before retry. A package or receipt check is not host behavior qualification.

`release/3.0.5/manifest.json` lists the portable source population. Its entries,
this manifest and their containing relative layout form the Skills package;
no Git checkout or old tenant tree is required at installation.

For an explicitly selected manager store, use the common installed tooling setup's runtime-anchor launcher as `--stdo`. CONFIG retains that exact launcher, underlying manager and selected store/manifest identities. `check-runtime` verifies them before invoking the launcher and requires the fresh manager result to preserve the same selection. An ambient `STDO_STORE` value is not a persistent installation binding. The anchor identifies the runtime only; nominated Product definitions retain their own selected bases.
