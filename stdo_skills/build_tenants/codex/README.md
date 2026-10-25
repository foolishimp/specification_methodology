# Codex STDO work candidate

This tenant packages one progressive skill, stdo-work. It targets the host mechanics documented for codex-cli 0.164.0 and the exact STDO v3.0.1-rc.1 basis. It is a construction candidate, not an accepted release or qualified host installation.

Start at [SKILL.md](skills/stdo-work/SKILL.md). The [design](design/DESIGN.md) maps SK-01 through SK-13 to the algorithm, host and required proof. [Qualification](skills/stdo-work/references/qualification.md) retains every Q01–Q12 obligation. Explicit invocation is `$stdo-work`; ordinary relevant tasks use host automatic discovery. Success in one lane does not establish the other.

The T-002 composition increment adds conditional dependency verification and
trusted a_c context routing. It retains the installed 3.0.1 basis and earlier
qualification limits; the current package inventory selects the new source cut.

## Read-only package check

```sh
python3 -B /absolute/path/to/codex/tests/verify_package.py /absolute/path/to/codex
```

The inventory binds every ordinary regular file under this tenant except inventory.json itself; retain that manifest's digest separately. Checks cover exact inventory, skill metadata, contained resolvable local resources and declared source hashes. No host/model invocation or semantic verdict follows.

## Repository-local installation

Use only an authorized disposable target for initial qualification. Set the following paths to the selected exact tenant and target workspace. Keep a copy of the complete tenant and inventory outside all skill discovery roots as the install receipt.

```sh
set -eu
tenant=/absolute/path/to/exact/codex
target=/absolute/path/to/authorized/workspace
destination="$target/.agents/skills/stdo-work"
python3 -B "$tenant/tests/verify_package.py" "$tenant" --destination "$destination"
mkdir -p "$target/.agents/skills"
cp -R "$tenant/skills/stdo-work" "$destination"
python3 -B "$tenant/tests/verify_package.py" "$tenant" --installed "$destination"
```

The destination preflight refuses an existing directory, symlink or symlink ancestor. It is a finite custody check, not a grant. Do not choose a target inside the package. Copy the entire skill folder; its references remain relative. Do not change global settings or install the other tenant.

Open Codex in that workspace, observe discovery and perform a fresh explicit invocation separately. Updates are normally detected; restart if stale and keep the earlier failure. The host source is identified in the packaged source-routes.json; no automatic-discovery guarantee is made.

## Update or remove only the owned installation

Retain the previous complete tenant, its inventory digest and destination as the old receipt. Before any update or removal, compare the actual installed directory against that previous package:

```sh
python3 -B "$previous_tenant/tests/verify_package.py" "$previous_tenant" --installed "$destination"
```

If files differ, are extra, missing, symlinked or custody is unknown, stop replacement/removal and report the conflict. Preserve local modifications and unrelated configuration.

For update, also verify the new tenant. Move only the verified old stdo-work directory to an authorized, absent retained directory outside every discovery root, then use the installation recipe with the new tenant. Record both inventory identities. If copying is interrupted, reconcile actual files before any retry or rollback. This deliberately retains the previous selected package instead of merging directories.

For removal after the old receipt check, remove only the exact verified destination. Do not remove its .agents/skills parent, other skills, another tenant or host configuration. Obtain a fresh directory observation after removal and retain evidence of unrelated entries. Removal and update remain unperformed Q12 host operations in this construction.

## Current proof limits

The Worker records author instruction assessment and finite package checks outside this frozen package in its activation's work surface. Actual-host Q01–Q12 trials, independent review, publication and owner acceptance remain open. The original failed construction remains historical evidence; this successor neither erases it nor invents a previous successful write.
