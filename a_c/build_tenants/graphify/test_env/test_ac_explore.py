from contextlib import redirect_stderr, redirect_stdout
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

from fixture_support import TENANT, toy_model

sys.path.insert(0, str(TENANT / "code"))
import ac_graph as ac
import ac_explore as explorer


class ConstraintExplorerTests(unittest.TestCase):
    def setUp(self):
        self.document = toy_model()
        self.model = ac.validate(self.document)
        self.data = explorer.view_data(self.document)

    def test_native_and_actual_carrier_have_identical_view(self):
        graph = ac.materialize(self.model).document
        self.assertEqual(self.data, explorer.view_data(graph))
        graph["nodes"].pop()
        with self.assertRaises(ac.Refusal):
            explorer.view_data(graph)

    def test_all_exact_records_and_external_resolutions_survive(self):
        nodes = {n["id"]: n for n in self.data["nodes"]}
        self.assertEqual(set(nodes), set(self.model.records) | set(self.model.external))
        for rid, record in self.model.records.items():
            self.assertEqual(nodes[rid]["record"], record.fields)
            self.assertEqual(nodes[rid]["family"], record.family)
        for rid, resolution in self.model.external.items():
            self.assertEqual(nodes[rid]["record"], resolution)

    def test_visible_dependency_graph_agrees_with_public_projection_for_every_seed(self):
        edges = [(l["source"], l["target"]) for l in self.data["links"] if l["layer"] == "required"]
        for seed in self.model.records:
            reached = {seed}
            while True:
                expanded = reached | {b for a, b in edges if a in reached}
                if expanded == reached:
                    break
                reached = expanded
            self.assertEqual(reached, set(ac.project(self.model, [seed])["included"]))

    def test_parallel_self_relations_and_typed_occurrences_are_not_collapsed(self):
        links = self.data["links"]
        self.assertEqual(len(links), len({l["id"] for l in links}))
        relations = [l for l in links if l["layer"] == "relation"]
        records = [r for r in self.model.records.values() if r.family == "relations"]
        self.assertEqual(len(relations), len(records))
        self.assertTrue(any(l["source"] == l["target"] for l in relations))
        for record in records:
            link = next(l for l in relations if l["record_id"] == record.identity)
            self.assertEqual((link["source"], link["target"], link["kind"]),
                             (record.fields["source"], record.fields["target"], record.fields["kind"]))
        references = [l for l in links if l["layer"] == "reference"]
        self.assertEqual([(r.owner, list(r.path), r.target) for r in self.model.references],
                         [(l["source"], l["path"], l["target"]) for l in references])

    def test_embedded_data_cannot_break_out_of_script_or_reenter_template(self):
        self.data["title"] = '</title><script>alert(1)</script>@@APP@@'
        payload = '</script><img src=x onerror=alert(1)> & @@CSS@@'
        self.data["nodes"][0]["record"]["display_test"] = payload
        self.data["nodes"][0]["record"]["big_integer"] = 10**80 + 1
        rendered = explorer.render(self.data)
        encoded = rendered.split('<script id="explorer-data" type="application/json">', 1)[1].split('</script>', 1)[0]
        self.assertNotIn('<', encoded)
        self.assertEqual(json.loads(encoded), self.data)
        self.assertIn('&lt;/title&gt;', rendered)

    def test_source_embedding_refuses_escape_and_missing_source(self):
        for path in ('../escape.md', 'absent.md'):
            with self.subTest(path=path), tempfile.TemporaryDirectory() as directory:
                with patch.object(explorer, 'groundings', return_value=[{'path': path}]):
                    with self.assertRaises(ac.Refusal):
                        explorer.view_data(self.document, directory)

    def test_output_refuses_existing_input_without_changing_it(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / 'model.json'
            ac.write_json(source, self.document)
            before = source.read_bytes()
            with redirect_stderr(io.StringIO()):
                self.assertEqual(explorer.main([str(source), '--out', str(source)]), 2)
            self.assertEqual(source.read_bytes(), before)
            output = Path(directory) / 'reader.html'
            with redirect_stdout(io.StringIO()):
                self.assertEqual(explorer.main([str(source), '--out', str(output)]), 0)
            self.assertIn('explorer-data', output.read_text())

    def test_layered_and_force_exports_embed_the_exact_same_representation(self):
        from html.parser import HTMLParser

        class ResourceParser(HTMLParser):
            def handle_starttag(self, tag, attributes):
                attrs = dict(attributes)
                if tag == 'script':
                    self_test.assertNotIn('src', attrs)
                if tag == 'link':
                    self_test.assertTrue(attrs.get('href', '').startswith('data:'))

        self_test = self
        self.data['nodes'][0]['record']['literal'] = '</script><img src=x> @@APP@@'
        self.data['nodes'][0]['record']['large_integer'] = 10**80 + 1
        for layout in ('unified', 'force', 'layered'):
            page = explorer.render(self.data, layout)
            encoded = page.split('<script id="explorer-data" type="application/json">', 1)[1].split('</script>', 1)[0]
            self.assertEqual(json.loads(encoded), self.data)
            ResourceParser().feed(page)
            self.assertIn('data-renderer="' + layout + '"', page)
        unified = explorer.render(self.data)
        self.assertIn('data-renderer="unified"', unified)
        self.assertEqual(unified.count('<script id="explorer-data"'), 1)
        self.assertIn('id="mode-layered"', unified)
        with self.assertRaises(ac.Refusal):
            explorer.render(self.data, 'unknown')

    def test_layered_public_cli_and_carrier_do_not_need_force_vendor(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / 'carrier.json'
            ac.write_json(source, ac.materialize(self.model).document)
            output = Path(directory) / 'layered.html'
            with redirect_stdout(io.StringIO()):
                self.assertEqual(explorer.main([str(source), '--out', str(output), '--layout', 'layered']), 0)
            self.assertIn('globalThis.ACTracks', output.read_text())
            with patch.object(explorer, 'ASSETS', Path(directory)):
                for name in ('explorer.html', 'explorer.css', 'explorer.js', 'layered.js', 'layered.css'):
                    (Path(directory) / name).write_bytes((TENANT / 'code/viewer' / name).read_bytes())
                self.assertIn('globalThis.ACTracks', explorer.render(self.data, 'layered'))


if __name__ == '__main__':
    unittest.main()
