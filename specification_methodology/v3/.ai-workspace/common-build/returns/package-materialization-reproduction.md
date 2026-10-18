# Reproduce exact-candidate package verification

This proves package mechanics for construction commit `494451522072ec34381c644f1ccfa2331f2b1e27`, candidate tree `082df4ea2b7b3658aab528bbfbcfe81234ccc810`. It does not attest a release-shaped source tree, an accepted release or an installation.

The supplied `v3.0.0-rc.9999` cut and qualified ref are fictional verification inputs. The all-zero `tag_object` is an explicit absent-tag sentinel, not an existing tag object. Git confirmed that the qualified ref did not exist. Commit and tree identities are real construction identities, whose source layout contains `build_tenants/common/`. The explanation is preserved separately in [package-materialization-coordinates-explanation.json](package-materialization-coordinates-explanation.json).

## Durable inputs

| Input | Identity |
|---|---|
| Original candidate | The 81 files at `494451522072ec34381c644f1ccfa2331f2b1e27:specification_methodology/v3/build_tenants/common` |
| Checker | `30b70f6e7771535cf50b37e56a51bb595b477364b6c1112acf044c7b76e4ceac` |
| [Frozen inventory](package-final-freeze.json) | `cd140a1ca32e17d8310522cf170b252c1887d7127c8fc17833b4d8e05c608050` |
| [Verification coordinates](package-materialization-coordinates.json) | `20cd8cac3387c8e73c51a61061ab33dfd989a60b1bbe43c7896c85d0f98369f9` |
| [Expected canonical manifest](package-materialization-manifest.json) | `609b8ee9f7b8412fc3e19fd35f95862528f30adb9a708bc211d659a77e91a712` |
| [Installed verifier invocation](package-installed-verifier-run.json) | `c333b20a5441a94f69367ff61514ab1cd94619b15f2e937b2964150fb8923875` |

The original files, inventory and checker are present at the construction commit. The coordinate, manifest and receipt files accompany this construction proof checkpoint. The materialized directory is disposable and is not part of the durable reproduction basis.

## Procedure

1. Restore the exact candidate, checker and frozen inventory from the construction commit into a fresh temporary directory. `git archive` can restore these three paths without changing the source worktree or index:

   ```sh
   git archive 494451522072ec34381c644f1ccfa2331f2b1e27 \
     specification_methodology/v3/build_tenants/common \
     specification_methodology/v3/.ai-workspace/common-build/tools/package_tools.py \
     specification_methodology/v3/.ai-workspace/common-build/returns/package-final-freeze.json \
     | tar -x -C /absolute/path/to/new-reproduction-directory
   ```

2. Use the [authenticated launcher](../tools/README.md#trusted-invocation), with the selected checker pin above and the restored package/inventory paths. Supply the exact coordinates file and its pin above. The materialization arguments are:

   ```text
   materialize --root RESTORED_COMMON \
     --inventory RESTORED_FINAL_FREEZE \
     --inventory-sha256 cd140a1ca32e17d8310522cf170b252c1887d7127c8fc17833b4d8e05c608050 \
     --coordinates SELECTED_COORDINATES_JSON \
     --coordinates-sha256 20cd8cac3387c8e73c51a61061ab33dfd989a60b1bbe43c7896c85d0f98369f9 \
     --destination NEW_MATERIALIZED_DIRECTORY \
     --report NEW_MATERIALIZATION_RECEIPT_JSON
   ```

3. Require the generated `manifest.json` to hash to `609b8ee9f7b8412fc3e19fd35f95862528f30adb9a708bc211d659a77e91a712`. All 81 package files must appear unchanged at their original paths; `manifest.json` is the one added file. There are 62 standards members, 17 plugin members, one licence and one release note.

4. Authenticate the saved installed-verifier run record against its pin above. Its `argv` contains the exact inline verifier/schema-validation program. Reuse that program with the new materialized root and restored inventory path. In the recorded seven-element argument vector, replace element 4 (package root) and element 6 (inventory path). Element 0 selects the installed toolchain interpreter and element 5 the installed basis schema. If reproducing in another environment, explicitly select equivalent dependencies and compare their observed source/schema pins; do not infer identity merely from a version label.

5. Require exit status zero, no installed-verifier failures, both installed and candidate schema validations to pass, canonical manifest bytes and standards digest to reproduce, and complete frozen member identity to match. Retain the new stdout/exit status and runtime/source pins as the new execution's evidence. Absolute paths and recording timestamps can differ; the frozen inventory, coordinates and canonical manifest pins above must match.

The original invocation, stdout, stderr and exit status are in [package-materialization-run.json](package-materialization-run.json) and [package-installed-verifier-run.json](package-installed-verifier-run.json). The generated manifest is preserved directly, without committing a redundant copy of the materialized directory. [package-installed-verifier.json](package-installed-verifier.json) includes observed loaded STDO-toolchain source-file pins, both schema pins and runtime identities; these do not claim authentication of the entire Python dependency closure.

## Recorded result and limits

The original run passed all declared checks. The standards aggregate is `c60b469b34e80c61e8e8ce5d4f48eb4f12777dfda37ce88f561cf9c12609a1fb`. Materialization used `/private/tmp/stdo-common-materialization-m3mwg8pm/package`; that temporary location may later disappear.

No `stdo install` was run. No release source path, release/tag ref, selector, install registry or remote was created or changed. The authored proof supplies no independent semantic review, owner replacement decision, candidate acceptance or release approval. The unchanged 29 fixture controls were not rerun for this execution.
