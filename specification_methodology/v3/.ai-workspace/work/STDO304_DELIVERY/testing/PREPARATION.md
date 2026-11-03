Release preparation/test activation: 3.0.4

Reviewed predecessor source: 4568edeeba415a877f1b9a4dd5ac9aeb404f6d7e. The Writer is preparing a narrow release-metadata/helper-constant delta. No successor actor qualification is selected. The construction basis remains installed 2.5.1-rc.2.

The reusable 3.0.3 recipe is STDO303_DELIVERY/native-release/release-run-01/LOCAL_RETURN.md plus its manager-local-operations.json and entry-asset-local-operations.json. These provide procedure history, not proof of this new cut.

Selected bounded checks after the Writer freeze:
1. Existing `python3 -B -m unittest -v test_documentation test_tooling` from build_tenants/common-tools. It includes native payload omission, required manifest/wheel, exact installed tooling materialization, input tampering and missing-helper checks; all writes are disposable test directories.
2. Real current-payload native validator plus in-memory stale release declaration and stale plugin-version negative controls, if not already covered by those tests.
3. Confirm unchanged skill bodies, helper code/tests and all frame input/output bytes against already-reviewed source evidence. Reuse the exact 35-reader, 13-frame and five-skill checks where their dependencies match. The Writer owns final package/docs/tooling preflight; test support will pin and consume those results, avoiding duplicates.

Later, after the Executive/Writer creates an exact native tag and manifest, use installed manager 0.1.6 with `--store <unique temporary store>` for `install v3.0.4 --repository <local repo> --manifest-sha256 <sealed digest>`, `verify`, and concrete `resolve` calls. Independently compare the complete installed file set against native Git bytes plus canonical manifest; exercise installed tooling check/materialize/verify in a distinct temporary directory. Repeat acquisition against the public HTTPS repository only after publication. No new dependency download is required for the already-installed manager.

Effects are limited to this testing directory and isolated disposable runtime directories. No candidate edits, Git mutations, browser, Lean, global install, model sessions or consumer adoption. Acceptance/disposition remains Executive/owner-owned; Reviewer assessment remains separate.
