"""Finite custody, source-navigation and offline DOM controls; no Lean execution."""
from __future__ import annotations

import copy
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

import proof_reader as reader

ROOT = Path(__file__).resolve().parents[4]
LEAN = ROOT / "a_c/build_tenants/lean"
REPORT = ROOT / "a_c/.ai-workspace/work/T011_LEAN_FORMALISATION/review/full-path-001/report.json"


def embedded(raw):
    match = re.search(r'<script id="proof-data" type="application/json">(.*?)</script>', raw.decode(), re.S)
    return json.loads(match.group(1))


class ProofReaderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sources = {name: (LEAN / name).read_bytes() for name in reader.SOURCES}
        cls.report = REPORT.read_bytes()
        cls.payload = reader.create_payload(cls.sources, cls.report)
        cls.catalog = json.loads(cls.payload["PROOFS.json"])
        cls.by_id = {d["id"]: d for d in cls.catalog["declarations"]}

    def test_exact_source_and_report_custody(self):
        result = reader.check_payload(self.payload)
        self.assertEqual((result["status"], result["members"], result["sources"]), ("checked", 11, 8))
        self.assertEqual(reader.sha(self.payload["report.json"]), reader.REPORT_SHA256)
        report = json.loads(self.report)
        data = embedded(self.payload["index.html"])
        for name, raw in self.sources.items():
            self.assertEqual(raw, self.payload["sources/" + name])
            self.assertEqual(reader.sha(raw), report["source_sha256"][name])
            self.assertEqual(data["sources"][name].encode(), raw)
        self.assertEqual(self.catalog["report"]["audited_declaration_contracts"], 204)
        self.assertEqual(self.catalog["report"]["projection_outputs"], 46)
        self.assertEqual(self.catalog["report"]["underbudget_refusals"], 46)
        self.assertEqual(self.catalog["report"]["allowed_axioms"], ["Classical.choice", "Quot.sound", "propext"])
        for claim in reader.CLAIMS:
            self.assertTrue(set(claim["declarations"]) <= self.by_id.keys())

    def test_exact_profile_instance_boundaries(self):
        for name, start, end in (("AC.Closed", 19, 20), ("AC.Witness", 30, 32),
                                 ("AC.CertificateValid", 45, 47), ("AC.witnessDecidable", 34, 41)):
            d = self.by_id[name]
            self.assertEqual((d["start_line"], d["end_line"]), (start, end))
            self.assertTrue(all(start <= ref["line"] <= end for ref in d["references"]))
        self.assertEqual(self.by_id["AC.witnessDecidable"]["kind"], "Instance")
        self.assertNotIn("instance", self.by_id["AC.Witness"]["statement"])
        self.assertNotIn("Decidable", self.by_id["AC.Witness"]["statement"])
        self.assertIn("AC.Witness", {r["target"] for r in self.by_id["AC.witnessDecidable"]["references"]})
        self.assertEqual({r["target"] for r in self.by_id["AC.Witness"]["references"]}, {"AC.Dependencies"})
        self.assertIn("Anonymous instances", self.catalog["catalog_scope"])

    def test_masking_named_kinds_and_anonymous_commands(self):
        source = ('namespace Demo\n'
                  'def one : Nat := 1\n'
                  'instance : Inhabited Nat := ⟨one⟩\n'
                  '/- theorem Fake : False := by\n /- nested -/ -/\n'
                  'instance chosen : Inhabited Nat := ⟨one⟩\n'
                  'example : one = 1 := rfl\n'
                  'def text : String := "theorem hidden := one"\n'
                  '-- theorem ignored : False := by\n'
                  'theorem valid : one = 1 := rfl\n'
                  'end Demo\n')
        declarations, _ = reader.source_catalog({"Demo.lean": source})
        ds = {d["id"]: d for d in declarations}
        self.assertEqual(set(ds), {"Demo.one", "Demo.chosen", "Demo.text", "Demo.valid"})
        self.assertEqual(ds["Demo.one"]["end_line"], 2)
        self.assertEqual((ds["Demo.chosen"]["kind"], ds["Demo.chosen"]["end_line"]), ("Instance", 6))
        self.assertEqual(ds["Demo.text"]["references"], [])
        self.assertEqual(ds["Demo.valid"]["references"], [{"target": "Demo.one", "token": "one", "line": 10}])
        self.assertEqual(ds["Demo.valid"]["statement"], "theorem valid : one = 1")

    def test_source_and_report_tamper_refuse(self):
        changed = dict(self.sources)
        changed["AC/Closure.lean"] += b"\n"
        with self.assertRaisesRegex(ValueError, "checked Lean source changed"):
            reader.create_payload(changed, self.report)
        report = json.loads(self.report)
        report["source_sha256"]["AC/Closure.lean"] = reader.sha(changed["AC/Closure.lean"])
        with self.assertRaisesRegex(ValueError, "report identity changed"):
            reader.create_payload(changed, reader.canonical(report))

    def test_payload_mutations_refuse(self):
        for name in ("index.html", "PROOFS.json", "sources/AC.lean", "report.json"):
            with self.subTest(name=name):
                changed = dict(self.payload)
                changed[name] += b" "
                with self.assertRaises(ValueError):
                    reader.check_payload(changed)
        missing = dict(self.payload)
        del missing["sources/AC/Run.lean"]
        with self.assertRaisesRegex(ValueError, "member set changed"):
            reader.check_payload(missing)
        with self.assertRaisesRegex(ValueError, "member set changed"):
            reader.check_payload({**self.payload, "extra.txt": b"extra"})

    def test_build_refusal_precedes_effect_and_symlink_refusal(self):
        with tempfile.TemporaryDirectory(prefix="proof-reader-negative-") as temp:
            root = Path(temp)
            invalid = root / "invalid-report.json"
            invalid.write_bytes(self.report + b" ")
            output = root / "not-created"
            with self.assertRaisesRegex(ValueError, "report identity changed"):
                reader.build(LEAN, invalid, output)
            self.assertFalse(output.exists())
            output.mkdir()
            with self.assertRaisesRegex(ValueError, "already exists"):
                reader.build(LEAN, REPORT, output)
            (output / "link.lean").symlink_to(LEAN / "AC.lean")
            with self.assertRaisesRegex(ValueError, "redirected proof member"):
                reader.read_payload(output)

    def test_portable_cli_build_and_check(self):
        with tempfile.TemporaryDirectory(prefix="proof-reader-portable-") as temp:
            root = Path(temp)
            tool = root / "proof_reader.py"
            shutil.copyfile(reader.__file__, tool)
            bundle = root / "proofs"
            build = subprocess.run([sys.executable, "-B", "-I", str(tool), "build", "--lean-root", str(LEAN),
                                    "--report", str(REPORT), "--output", str(bundle)], cwd=root,
                                   capture_output=True, text=True, timeout=30)
            self.assertEqual(build.returncode, 0, build.stdout + build.stderr)
            check = subprocess.run([sys.executable, "-B", "-I", str(tool), "check", str(bundle)], cwd=root,
                                   capture_output=True, text=True, timeout=30)
            self.assertEqual(check.returncode, 0, check.stdout + check.stderr)
            self.assertEqual(json.loads(check.stdout)["status"], "checked")
            self.assertEqual(reader.read_payload(bundle), self.payload)

    def test_safe_embedding_and_single_pass_template(self):
        hostile = '</script><script src="https://invalid.example/attack.js"></script><img src=x onerror=alert(1)>@@APP@@ &\u2028'
        catalog = copy.deepcopy(self.catalog)
        catalog["claims"][0]["summary"] = hostile
        sources = {name: raw.decode() for name, raw in self.sources.items()}
        sources["AC.lean"] = hostile
        page = reader.render(catalog, sources, self.report)
        data = embedded(page)
        self.assertEqual(data["sources"]["AC.lean"], hostile)
        self.assertEqual(data["catalog"]["claims"][0]["summary"], hostile)
        self.assertEqual(page.count(b"</script>"), 2)
        self.assertNotIn(b'<script src=', page)
        self.assertNotIn(b'<img ', page)
        self.assertIn(b"@@APP@@", page)

    def test_generated_page_offline_dom_navigation(self):
        node = shutil.which("node")
        self.assertIsNotNone(node, "Node is required for the finite offline DOM qualification")
        with tempfile.TemporaryDirectory(prefix="proof-reader-dom-") as temp:
            page = Path(temp) / "index.html"
            page.write_bytes(self.payload["index.html"])
            result = subprocess.run([node, "-e", DOM_TEST, str(page)], env=os.environ.copy(),
                                    capture_output=True, text=True, timeout=45)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("offline proof reader DOM checks passed", result.stdout)


DOM_TEST = r"""
const assert = require('node:assert/strict');
const fs = require('node:fs');
const {pathToFileURL} = require('node:url');
const {JSDOM, ResourceLoader} = require('jsdom');
class DenyResources extends ResourceLoader { fetch(url) { throw Error('network resource: ' + url); } }
const html = fs.readFileSync(process.argv[1], 'utf8');
const dom = new JSDOM(html, {url:pathToFileURL(process.argv[1]).href,runScripts:'outside-only',resources:new DenyResources()});
const w=dom.window,d=w.document,$=id=>d.getElementById(id);
for(const key of ['fetch','XMLHttpRequest','WebSocket','Worker']) w[key]=()=>{throw Error('network/execution attempted: '+key);};
w.HTMLElement.prototype.scrollIntoView=function(){};
w.HTMLDialogElement.prototype.showModal=function(){this.open=true;};
w.HTMLDialogElement.prototype.close=function(){this.open=false;};
assert.equal(d.querySelectorAll('script[src],link[rel="stylesheet"],iframe,img').length,0);
const data=JSON.parse($('proof-data').textContent),ids=new Map(data.catalog.declarations.map(x=>[x.id,x]));
const scripts=[...d.querySelectorAll('script')];assert.equal(scripts.length,2);
w.eval(scripts[1].textContent);
assert.equal($('reader').dataset.view,'claim');
assert.match($('reader').textContent,/Selecting A/);
d.querySelector('[data-claim="budget"]').click();
$('reader').querySelector('[data-target="AC.insufficient_budget_refuses"]').click();
assert.equal($('reader').dataset.declaration,'AC.insufficient_budget_refuses');
assert.equal(JSON.parse(decodeURIComponent(w.location.hash.slice(1))).id,'AC.insufficient_budget_refuses');
assert.equal($('reader').querySelector('.statement').textContent,ids.get('AC.insufficient_budget_refuses').statement);
assert.match($('reader').querySelector('.kind').textContent,/Theorem/);
assert.match($('reader').textContent,/Source references \(lexical\)/);
$('reader').querySelector('[data-source]').click();
assert.equal($('reader').dataset.view,'file');assert.equal($('reader').dataset.declaration,undefined);
assert.equal(Number(d.querySelector('.source-row.selected').dataset.line),ids.get('AC.insufficient_budget_refuses').start_line);
$('back').click();assert.equal($('reader').dataset.declaration,'AC.insufficient_budget_refuses');
const linked=$('reader').querySelector('[data-target="AC.project"]');assert.ok(linked);linked.click();
assert.equal($('reader').dataset.declaration,'AC.project');assert.match($('reader').querySelector('.kind').textContent,/Definition/);
$('back').click();assert.equal($('reader').dataset.declaration,'AC.insufficient_budget_refuses');
$('query').value='witnessDecidable';$('query').dispatchEvent(new w.Event('input'));
assert.equal($('results').querySelectorAll('button').length,1);
$('results').querySelector('button').click();assert.equal($('reader').dataset.declaration,'AC.witnessDecidable');
assert.match($('reader').querySelector('.kind').textContent,/Instance/);
$('kind').value='Theorem';$('kind').dispatchEvent(new w.Event('change'));assert.equal($('results').querySelectorAll('button').length,0);
$('query').value='';$('kind').value='';$('module').value='AC/Model.lean';$('module').dispatchEvent(new w.Event('change'));
for(const button of $('results').querySelectorAll('button'))assert.equal(ids.get(button.dataset.declaration).file,'AC/Model.lean');
for(const source of data.catalog.sources){
 const button=[...$('modules').querySelectorAll('button')].find(x=>x.dataset.file===source.file);button.click();
 const text=[...$('full-source').querySelectorAll('.source-text')].map(x=>x.textContent).join('\n');
 assert.equal(text,data.sources[source.file]);
}
$('evidence-open').click();assert.equal($('evidence').open,true);
assert.match($('evidence-body').textContent,/204 audited declaration contracts, not that many independent mathematical results/);
assert.match($('evidence-body').textContent,/Audited allowed axioms/);
assert.ok($('evidence-body').textContent.includes(data.catalog.report.sha256));
for(const axiom of ['Classical.choice','Quot.sound','propext'])assert.ok($('evidence-body').textContent.includes(axiom));
assert.match($('evidence-body').textContent,/Current importer\/generator.*not requalified/);
$('evidence-close').click();assert.equal($('evidence').open,false);
assert.equal(d.querySelector('a[href="../index.html"]').textContent,'Documentation home');
dom.window.close();console.log('offline proof reader DOM checks passed');
"""


if __name__ == "__main__":
    unittest.main()
