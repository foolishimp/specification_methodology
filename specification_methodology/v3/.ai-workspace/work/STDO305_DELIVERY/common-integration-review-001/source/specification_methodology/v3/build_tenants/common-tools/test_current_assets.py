"""Current packaging controls. A supplied proof control is explicitly a toy run."""
import copy
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import current_assets as a
import documentation_current as docs
import proof_reader_current as proof
import tooling_current as tooling
import tooling_materialize as materializer
import tooling_setup as setup
import tooling_runtime as runtime


def freeze():
    identity = {"version": "3.0.5", "basis_uri": "stdo://releases/v3.0.5/", "members": [
        {"path": "standards/README.md", "bytes": 7, "sha256": a.sha(b"source\n")}], "native_contracts": [
        {"path": "plugins/spec/skills/stdo-work/SKILL.md", "bytes": 7, "sha256": a.sha(b"native\n")}]}
    return {"kind": "stdo.semantic-source-freeze/1", **identity, "source_identity_sha256": a.sha(a.encoded(identity))}


class CurrentToolingTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="stdo-current-tools-"); self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve(); self.repository = self.root / "repository"; self.repository.mkdir()
        owners = {}
        for owner, names in tooling.REQUIRED.items():
            rows = []
            for name in sorted(names):
                path = owner + "/" + name; file = self.repository / path; file.parent.mkdir(parents=True, exist_ok=True)
                raw = b"3.0.5\n" if name == "VERSION" else b"selected package test source\n"
                if name == 'build_tenants/lean/lakefile.toml': raw = b'name = "ac_lean"\nversion = "3.0.5"\n'
                if name == 'build_tenants/graphify/code/ac_support.py': raw = b'SERVER_VERSION = "3.0.5"\n'
                file.write_bytes(raw)
                rows.append({"path": path, "bytes": len(raw), "sha256": a.sha(raw), "git_mode": "100644"})
            owners[owner] = {"version": "3.0.5", "members": rows}
        self.selected = {"kind": "stdo.current-tooling-selection/1", "version": "3.0.5", "owners": owners,
                         "source_freeze": freeze(), "source_identity_sha256": freeze()["source_identity_sha256"]}
        self.selection = self.root / "selection.json"; self.selection.write_bytes(a.encoded(self.selected))

    def build(self, destination=None):
        return tooling.build(self.repository, destination or self.root / "bundle", self.selection, a.sha(self.selection.read_bytes()))

    def test_current_four_product_archive_and_actual_portable_materializer(self):
        result = self.build(); self.assertEqual(result["status"], "bundled")
        bundle = self.root / "bundle"; output = self.root / "tools"
        process = subprocess.run([sys.executable, "-I", "-B", str(bundle / "materialize.py"), "materialize", "--destination", str(output)],
                                 cwd=self.root, capture_output=True, text=True)
        self.assertEqual(process.returncode, 0, process.stdout + process.stderr)
        self.assertEqual(json.loads(process.stdout)["version"], "3.0.5")
        materializer.verify_tree(bundle, output)

    def test_wrong_selection_missing_product_and_missing_entrypoint_refuse(self):
        with self.assertRaisesRegex(ValueError, "selection digest"):
            tooling.build(self.repository, self.root / "wrong", self.selection, "0" * 64)
        for mutation in (lambda x: x["owners"].pop("a_c"), lambda x: x["owners"]["a_c"]["members"].pop()):
            value = copy.deepcopy(self.selected); mutation(value); self.selection.write_bytes(a.encoded(value))
            with self.assertRaises(ValueError): self.build()
        self.assertFalse((self.root / "bundle").exists())

    def test_redirected_selected_member_and_protected_output_refuse_before_write(self):
        member = self.repository / self.selected["owners"]["a_c"]["members"][0]["path"]
        raw = member.read_bytes(); member.unlink(); outside = self.root / "outside"; outside.write_bytes(raw); member.symlink_to(outside)
        with self.assertRaisesRegex(ValueError, "redirected"): self.build()
        self.assertFalse((self.root / "bundle").exists())
        with self.assertRaisesRegex(ValueError, "overlaps"): self.build(self.repository / "a_c/new-bundle")

    def test_exact_archive_tamper_and_extra_member_refuse(self):
        self.build(); files = materializer.read_bundle(self.root / "bundle")
        bad = dict(files); bad["sources.zip"] += b"tamper"
        with self.assertRaises(ValueError): tooling.check_files(bad)
        bad = dict(files); bad["extra"] = b"x"
        with self.assertRaises(ValueError): tooling.check_files(bad)

    def test_unchanged_product_marker_cannot_hide_old_owned_package_version(self):
        row = next(r for r in self.selected['owners']['a_c']['members'] if r['path'].endswith('/lakefile.toml'))
        raw = b'name = "ac_lean"\nversion = "0.1.0"\n'; (self.repository / row['path']).write_bytes(raw)
        row.update(bytes=len(raw), sha256=a.sha(raw)); self.selection.write_bytes(a.encoded(self.selected))
        with self.assertRaisesRegex(ValueError, 'owned Lean package version differs'): self.build()
        self.assertFalse((self.root / 'bundle').exists())

    def test_unchanged_product_marker_cannot_hide_old_owned_server_version(self):
        row = next(r for r in self.selected['owners']['a_c']['members'] if r['path'].endswith('/ac_support.py'))
        raw = b'SERVER_VERSION = "0.1.0"\n'; (self.repository / row['path']).write_bytes(raw)
        row.update(bytes=len(raw), sha256=a.sha(raw)); self.selection.write_bytes(a.encoded(self.selected))
        with self.assertRaisesRegex(ValueError, 'owned MCP server version differs'): self.build()
        self.assertFalse((self.root / 'bundle').exists())


class RuntimeLauncherTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="stdo-anchor-test-"); self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.store = self.root / "store"; self.store.mkdir()
        self.manifest = self.store / "manifest.json"; self.manifest.write_bytes(b"native selection")
        self.manager = self.root / "manager"
        self.manager.write_text("#!" + sys.executable + "\nimport json,sys\nprint(json.dumps({'argv':sys.argv[1:]}))\n"); self.manager.chmod(0o755)
        self.contract = {"manager": str(self.manager), "manager_sha256": a.sha(self.manager.read_bytes()),
                         "store": str(self.store), "manifest": str(self.manifest), "manifest_sha256": a.sha(self.manifest.read_bytes())}
        self.launcher = self.root / "stdo"; self.launcher.write_bytes(setup.launcher_source(self.contract)); self.launcher.chmod(0o755)

    def run_launcher(self, *args):
        return subprocess.run([sys.executable, str(self.launcher), *args], capture_output=True, text=True,
                              env={**os.environ, "STDO_STORE": str(self.root / "wrong ambient store")})

    def test_actual_launcher_fixes_store_and_forwards_literal_argv(self):
        run = self.run_launcher("status", "--definition", "with spaces/$(no-command).json")
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        value = json.loads(run.stdout)
        self.assertEqual(value["argv"], ["--store", str(self.store), "status", "--definition", "with spaces/$(no-command).json"])
        self.assertEqual(value["runtime_launcher"]["sha256"], a.sha(self.launcher.read_bytes()))

    def test_wrong_store_changed_native_and_manager_refuse(self):
        self.assertEqual(self.run_launcher("--store", str(self.root / "other")).returncode, 2)
        self.manifest.write_bytes(b"wrong store member")
        self.assertEqual(self.run_launcher("status").returncode, 2)
        self.manifest.write_bytes(b"native selection"); self.manager.write_text("changed manager")
        self.assertEqual(self.run_launcher("status").returncode, 2)

    def test_anchor_definition_is_explicitly_separate_and_complete(self):
        value = setup.anchor_definition("3.0.5", "a" * 64, "https://example.test/project.git")
        schema = json.loads((Path(__file__).parent.parent / "common/standards/schemas/product-definition.schema.json").read_bytes())
        import jsonschema
        jsonschema.Draft202012Validator(schema).validate(value)
        self.assertEqual(value["composition"], [])
        self.assertIn("runtime-installation-anchor", value["product"]["definition_id"])


class RuntimeDerivationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="stdo-runtime-control-"); self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve(); self.source = self.root / "source"; self.derived = self.root / "runtime"
        self.source.mkdir(); self.derived.mkdir()
        rows = {}
        for name, raw in ((runtime.PROFILE, b"original support profile"), ("scripts/bootstrap.py", b"selected bootstrap source")):
            for base in (self.source, self.derived):
                p = base / name; p.parent.mkdir(parents=True, exist_ok=True); p.write_bytes(raw)
            rows[name] = {"archive_path": "a_c/" + name, "bytes": len(raw), "sha256": a.sha(raw), "git_mode": "100644"}
        self.record = {"kind": "stdo.ac-runtime-derivation/1", "status": "prepared", "version": "3.0.5",
                       "source_root": str(self.source), "runtime_root": str(self.derived), "source_members": rows,
                       "allowed_source_delta": runtime.PROFILE, "generated_roots": list(runtime.GENERATED)}

    def test_exact_initial_mapping_and_undeclared_code_delta_refuse(self):
        runtime.validate(materializer, self.record)
        (self.derived / "scripts/bootstrap.py").write_bytes(b"undeclared changed code")
        with self.assertRaisesRegex(ValueError, "undeclared runtime source delta"):
            runtime.validate(materializer, self.record)

    def test_extra_source_and_unproven_support_profile_refuse(self):
        extra = self.derived / "scripts/new.py"; extra.write_bytes(b"unselected helper")
        with self.assertRaisesRegex(ValueError, "undeclared runtime source member"): runtime.validate(materializer, self.record)
        extra.unlink(); (self.derived / runtime.PROFILE).write_bytes(b"unsupported changed profile")
        with self.assertRaisesRegex(ValueError, "undeclared runtime source delta"): runtime.validate(materializer, self.record)
        bad = dict(self.record, status="support-established", profile_sha256=a.sha(b"unsupported changed profile"))
        with self.assertRaises((ValueError, KeyError)): runtime.validate(materializer, bad, require_support=True)

    def test_wrong_source_root_and_alias_outputs_refuse(self):
        bad = dict(self.record, runtime_root=str(self.source))
        with self.assertRaisesRegex(ValueError, "overlaps"): runtime.validate(materializer, bad)
        alias = self.root / "RUNTIME"
        if alias.exists():
            with self.assertRaisesRegex(ValueError, "aliases"):
                runtime.separate(materializer, alias / "new", self.derived)


class CurrentDocumentationBindingTests(unittest.TestCase):
    def inputs(self):
        source = freeze(); prefix = "source"
        rows = sorted(({**r, "path": prefix + "/" + r["path"]} for r in source["members"] + source["native_contracts"]), key=lambda r:r["path"])
        model = {"id": "urn:test:model", "profile": "a_c.graphify.model/1", "basis": {"subject": {"sha256": a.canonical_sha(rows)}}, "interpretation": {}}
        model_raw = a.encoded(model); identity = a.model_identity(model_raw)
        data = {"profile": "a_c.constraint-explorer/1", "model": identity, "basis": model["basis"], "interpretation": {},
                "sources": {r["path"]: {"text": "source\n" if "README" in r["path"] else "native\n", "sha256": r["sha256"]} for r in rows}}
        files = {"source-freeze.json": a.encoded(source), "model.json": model_raw, "source-manifest.json": a.encoded({"files": rows}),
                 "constraint-explorer/index.html": b'<script id="explorer-data" type="application/json">'+json.dumps(data).encode()+b'</script>', "proofs/PROOFS.json": b"isolated proof adapter"}
        selected = {"kind": "stdo.current-documentation-selection/1", "version": "3.0.5", "source_copy_prefix": prefix}
        for key,path in (("source_freeze","source-freeze.json"),("model","model.json"),("source_manifest","source-manifest.json"),("viewer","constraint-explorer/index.html"),("proof_catalog","proofs/PROOFS.json")):
            selected[key] = {"sha256": a.sha(files[path])}
        files["SELECTION.json"] = a.encoded(selected)
        check = {"version": "3.0.5", "source_identity_sha256": source["source_identity_sha256"], "model": identity}
        return files, check

    def test_source_model_view_join_and_omitted_or_tampered_source_refusal(self):
        files, check = self.inputs()
        with patch.object(proof, "check_files", return_value=check):
            docs.validate_inputs(files)
            bad = dict(files); bad["model.json"] += b" "
            with self.assertRaisesRegex(ValueError, "selected documentation input"): docs.validate_inputs(bad)
            bad = dict(files); data = docs.viewer_data(bad["constraint-explorer/index.html"]); data["sources"].pop(next(iter(data["sources"])))
            bad["constraint-explorer/index.html"] = b'<script id="explorer-data" type="application/json">'+json.dumps(data).encode()+b'</script>'
            selected = json.loads(bad["SELECTION.json"]); selected["viewer"]["sha256"] = a.sha(bad["constraint-explorer/index.html"]); bad["SELECTION.json"] = a.encoded(selected)
            with self.assertRaisesRegex(ValueError, "source population"): docs.validate_inputs(bad)

    def test_proof_of_different_model_cannot_join_current_documentation(self):
        files, check = self.inputs(); check["model"] = {"id": "other", "sha256": "0" * 64}
        with patch.object(proof, "check_files", return_value=check), self.assertRaisesRegex(ValueError, "selected current model"):
            docs.validate_inputs(files)


@unittest.skipUnless(os.environ.get("STDO_PROOF_CONTROL"), "supply the retained toy proof reader for actual evidence integration controls")
class ActualRetainedProofControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = a.read_tree(Path(os.environ["STDO_PROOF_CONTROL"]))

    def test_actual_retained_owner_inspected_toy_has_exact_catalog(self):
        result = proof.check_files(self.files)
        self.assertIn("toy", result["model"]["id"])
        self.assertEqual(result["status"], "checked")

    def test_missing_compiled_artifact_unrelated_claim_and_changed_machinery_refuse(self):
        for path in ("transport/part-001.bin", "machinery/AC/Model.lean", "inspection.json"):
            bad = dict(self.files); bad[path] += b"tamper"
            with self.subTest(path=path), self.assertRaises((ValueError, json.JSONDecodeError)): proof.check_files(bad)
        bad = dict(self.files); value = json.loads(bad["evidence/result.json"]); value["checked_claims"] = value["requested_claims"] = ["unrelated-trivial-claim"]
        bad["evidence/result.json"] = a.encoded(value)
        with self.assertRaisesRegex(ValueError, "visible evidence|proof obligations"): proof.check_files(bad)

    def test_safe_current_page_embedding(self):
        catalog, sources = proof.catalog(self.files); sources = dict(sources)
        hostile = '</script><script src="https://invalid.example"></script>@@APP@@'
        sources["current/GateRun.lean"] = hostile
        page = proof.render(catalog, sources)
        self.assertEqual(page.count(b"</script>"), 2)
        self.assertIn(b"@@APP@@", page); self.assertNotIn(b'<script src=', page)

    def test_actual_current_reader_offline_dom_navigation(self):
        node = shutil.which("node"); self.assertIsNotNone(node)
        path = Path(os.environ["STDO_PROOF_CONTROL"]) / "index.html"
        code = r'''
const assert=require('node:assert/strict'),fs=require('node:fs'),{JSDOM,ResourceLoader}=require('jsdom');
class NoNetwork extends ResourceLoader{fetch(url){throw Error('network '+url)}}
const dom=new JSDOM(fs.readFileSync(process.argv[1],'utf8'),{runScripts:'outside-only',resources:new NoNetwork()});
const w=dom.window,d=w.document,$=id=>d.getElementById(id);w.HTMLElement.prototype.scrollIntoView=function(){};
for(const key of ['fetch','XMLHttpRequest','WebSocket','Worker'])w[key]=()=>{throw Error('network or execution')};
assert.equal(d.querySelectorAll('script[src],link[rel="stylesheet"],iframe,img').length,0);
const data=JSON.parse($('proof-data').textContent);w.eval([...d.querySelectorAll('script')][1].textContent);
assert.ok($('model').textContent.includes(data.catalog.model.sha256));assert.equal($('claims').children.length,5);
assert.ok($('evidence').textContent.includes('theorem_audit'));assert.ok($('limits').textContent.includes('prose'));
const declaration=data.catalog.declarations.find(x=>x.id==='AC.GateData.model_checked');assert.ok(declaration);
$('query').value=declaration.id;$('query').dispatchEvent(new w.Event('input'));
$('results').querySelector('button').click();assert.ok($('reader').textContent.includes(declaration.statement));
$('reader').querySelector('button').click();assert.ok($('reader').querySelector('.source-row.selected'));
assert.equal(Number($('reader').querySelector('.source-row.selected').id.split('-')[1]),declaration.start_line);
const source=data.catalog.sources[0];$('modules').querySelector('button').click();
assert.ok($('reader').textContent.includes(source.file));
assert.equal([...$('reader').querySelectorAll('.source-row')].map(x=>x.children[1].textContent).join('\n'),data.sources[source.file]);
dom.window.close();console.log('current offline reader DOM passed');
'''
        run = subprocess.run([node, "-e", code, str(path)], capture_output=True, text=True, timeout=45)
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)


if __name__ == "__main__":
    unittest.main()
