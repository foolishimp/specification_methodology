"""Focused three-defect regression controls; real-bundle replay is separate."""
from pathlib import Path
from types import SimpleNamespace
import hashlib
import importlib.util
import json
import shutil
import sys
import tarfile
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'app'))
import package_release as package
import public_receipts as receipts


class PackagingRepairs(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='ac-common-release-repair-', dir=ROOT / 'tmp')
        self.root = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def refuse_build_without_input_processing(self, bundle, dist):
        with patch.object(package, 'preparation', side_effect=AssertionError('input processing reached')):
            with self.assertRaisesRegex(ValueError, 'overlap|outside|preserve|already exists'):
                package.build(SimpleNamespace(bundle=bundle, dist=dist))

    def test_build_dist_equal_bundle_refuses_before_outputs(self):
        path = self.root / 'new-output'
        self.refuse_build_without_input_processing(path, path)
        self.assertFalse(path.exists())

    def test_build_dist_nested_bundle_refuses_before_outputs(self):
        path = self.root / 'new-output'
        self.refuse_build_without_input_processing(path, path / 'dist')
        self.assertFalse(path.exists())

    def test_build_relative_dotdot_overlap_refuses_before_outputs(self):
        path = self.root / 'bundle'
        with package.chdir(self.root):
            self.refuse_build_without_input_processing(Path('bundle'), Path('uncreated/../bundle/dist'))
        self.assertFalse(path.exists())
        self.assertFalse((self.root / 'uncreated').exists())

    def test_build_symlink_alias_overlap_refuses_before_outputs(self):
        real = self.root / 'real'; real.mkdir()
        alias = self.root / 'alias'; alias.symlink_to(real, target_is_directory=True)
        self.refuse_build_without_input_processing(real / 'bundle', alias / 'bundle/dist')
        self.assertFalse((real / 'bundle').exists())

    def test_build_bundle_nested_under_archive_file_refuses(self):
        dist = self.root / 'dist'
        bundle = dist / (package.ARTIFACT + '.tar.gz') / 'bundle'
        self.refuse_build_without_input_processing(bundle, dist)
        self.assertFalse(dist.exists())

    def test_existing_bundle_is_preserved(self):
        bundle = self.root / 'bundle'; bundle.mkdir(); marker = bundle / 'marker'; marker.write_bytes(b'keep')
        self.refuse_build_without_input_processing(bundle, self.root / 'dist')
        self.assertEqual(marker.read_bytes(), b'keep')

    def test_existing_archive_is_preserved_without_creating_bundle(self):
        dist = self.root / 'dist'; dist.mkdir(); archive = dist / (package.ARTIFACT + '.tar.gz'); archive.write_bytes(b'keep archive')
        bundle = self.root / 'bundle'
        self.refuse_build_without_input_processing(bundle, dist)
        self.assertFalse(bundle.exists()); self.assertEqual(archive.read_bytes(), b'keep archive')

    def test_existing_checksum_is_preserved_without_creating_bundle(self):
        dist = self.root / 'dist'; dist.mkdir(); sidecar = dist / (package.ARTIFACT + '.tar.gz.sha256'); sidecar.write_bytes(b'keep checksum')
        bundle = self.root / 'bundle'
        self.refuse_build_without_input_processing(bundle, dist)
        self.assertFalse(bundle.exists()); self.assertEqual(sidecar.read_bytes(), b'keep checksum')

    def test_direct_archive_nested_output_refuses_without_writing(self):
        bundle = self.root / 'bundle'; bundle.mkdir(); (bundle / 'one.txt').write_bytes(b'one')
        with self.assertRaisesRegex(ValueError, 'overlap|outside'):
            package.archive(bundle, bundle / 'dist/archive.tar.gz')
        self.assertFalse((bundle / 'dist').exists())

    def test_direct_archive_symlink_alias_refuses_without_writing(self):
        bundle = self.root / 'bundle'; bundle.mkdir(); (bundle / 'one.txt').write_bytes(b'one')
        alias = self.root / 'alias'; alias.symlink_to(bundle, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, 'overlap|outside'):
            package.archive(bundle, alias / 'archive.tar.gz')
        self.assertEqual(sorted(p.name for p in bundle.iterdir()), ['one.txt'])

    def test_direct_archive_equal_bundle_refuses(self):
        bundle = self.root / 'bundle'; bundle.mkdir()
        with self.assertRaisesRegex(ValueError, 'overlap|outside'):
            package.archive(bundle, bundle)

    def assert_safe_archive(self, bundle, output):
        bundle.mkdir(parents=True); (bundle / 'one.txt').write_bytes(b'one')
        result = package.archive(bundle, output)
        with tarfile.open(output, 'r:gz') as archive:
            self.assertEqual(archive.getnames(), [package.ARTIFACT + '/one.txt'])
            self.assertEqual(archive.extractfile(archive.getmembers()[0]).read(), b'one')
        self.assertEqual(result['sha256'], hashlib.sha256(output.read_bytes()).hexdigest())
        return output.read_bytes()

    def test_safe_sibling_layout_and_determinism(self):
        one = self.assert_safe_archive(self.root / 'a/bundle', self.root / 'a/dist/archive.tar.gz')
        two = self.assert_safe_archive(self.root / 'b/bundle', self.root / 'b/dist/archive.tar.gz')
        self.assertEqual(one, two)

    def test_safe_dist_parent_of_bundle_is_supported(self):
        self.assert_safe_archive(self.root / 'dist/bundle', self.root / 'dist/archive.tar.gz')

    def test_direct_archive_preserves_existing_archive_and_checksum(self):
        bundle = self.root / 'bundle'; bundle.mkdir(); output = self.root / 'archive.tar.gz'; output.write_bytes(b'original')
        with self.assertRaisesRegex(ValueError, 'archive exists'):
            package.archive(bundle, output)
        self.assertEqual(output.read_bytes(), b'original')
        output.unlink(); sidecar = self.root / 'archive.tar.gz.sha256'; sidecar.write_bytes(b'original checksum')
        with self.assertRaisesRegex(ValueError, 'checksum already exists'):
            package.archive(bundle, output)
        self.assertFalse(output.exists()); self.assertEqual(sidecar.read_bytes(), b'original checksum')

    def test_original_and_portable_projection_are_exact_and_idempotent(self):
        original = (ROOT / 'proof/preimages/SOURCE-READINESS.md').read_bytes()
        portable = (ROOT / 'inputs/source-readiness-portable.md').read_bytes()
        first = package.source_readiness_projection(original).encode()
        self.assertEqual(first, portable)
        self.assertEqual(package.source_readiness_projection(portable).encode(), portable)
        self.assertEqual(hashlib.sha256(portable).hexdigest(), '2dec9cece18e6b9a318a75460b8c8191f75014f92bb4306691e55929b8df859a')

    def test_changed_original_and_changed_portable_are_refused(self):
        for path in ['proof/preimages/SOURCE-READINESS.md', 'inputs/source-readiness-portable.md']:
            raw = (ROOT / path).read_bytes()
            with self.subTest(path=path), self.assertRaisesRegex(ValueError, 'source-readiness'):
                package.source_readiness_projection(raw.replace(b'not_ready', b'now_ready', 1))

    def test_unverified_projected_flag_does_not_authorize_input(self):
        with self.assertRaisesRegex(ValueError, 'source-readiness'):
            package.source_readiness_projection(b'# captured-workspace projection\nprojected: true\n')

    def evidence_fixture(self):
        root = self.root / 'evidence-fixture'; (root / 'evidence/reviews/review-001').mkdir(parents=True)
        shutil.copyfile(ROOT / 'inputs/original-RELEASE.json', root / 'RELEASE.json')
        shutil.copyfile(ROOT / 'inputs/authoring-public.json', root / 'evidence/authoring-public.json')
        for path in (ROOT / 'inputs/review').iterdir():
            shutil.copyfile(path, root / 'evidence/reviews/review-001' / ('receipt.json' if path.name == 'bounded-review.json' else path.name))
        expected = json.loads((ROOT / 'inputs/authoring-public.json').read_text())['bindings']
        return root, expected

    def test_actual_bound_public_evidence_remains_valid(self):
        root, expected = self.evidence_fixture()
        self.assertEqual(receipts.bundle_evidence(root, expected)['bounded_review_receipts'], 1)

    def test_wrong_missing_or_different_source_index_fields_refuse(self):
        for key, value in [('source_commit', '0' * 40), ('package_tree', '0' * 40), ('source_commit', None), ('package_tree', None)]:
            with self.subTest(key=key, value=value):
                root, expected = self.evidence_fixture() if not (self.root / 'evidence-fixture').exists() else (self.root / 'evidence-fixture', json.loads((ROOT / 'inputs/authoring-public.json').read_text())['bindings'])
                release = json.loads((ROOT / 'inputs/original-RELEASE.json').read_text())
                if value is None:
                    del release[key]
                else:
                    release[key] = value
                (root / 'RELEASE.json').write_text(json.dumps(release))
                with self.assertRaisesRegex(ValueError, 'source commit/package tree'):
                    receipts.bundle_evidence(root, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
