"""Public host installer paths; controlled native/manager fixtures, no model calls."""
from pathlib import Path
import json
import os
import re
import shutil
import subprocess
import unittest
from urllib.parse import unquote, urljoin, urlsplit

import test_install_305 as installation

m = installation.m


def links(text):
    return re.findall(r'\[[^\]]*\]\(([^)\n]+)\)', text)


def local_target(source, destination):
    resolved = urlsplit(urljoin(source.as_uri(), destination))
    if resolved.scheme != 'file':
        return None, None
    return Path(unquote(resolved.path)), unquote(resolved.fragment)


def anchors(text):
    """ATX anchors used by the selected native Markdown, excluding code fences."""
    result = set(); fence = None; counts = {}
    for line in text.splitlines():
        if line.startswith(('```', '~~~')):
            marker = line[:3]; fence = None if fence == marker else marker
        elif fence is None:
            match = re.match(r'^#{1,6}\s+(.*?)\s*#*$', line)
            if match:
                base = re.sub(r'[^\w -]', '', match.group(1).lower()).replace(' ', '-')
                count = counts.get(base, 0); counts[base] = count + 1
                result.add(base if count == 0 else base + '-' + str(count))
    return result


class NativeRouteTests(unittest.TestCase):
    def setUp(self):
        self.fixture = installation.Install305Tests('test_plan_has_no_effect')
        self.fixture.setUp(); self.addCleanup(self.fixture.doCleanups)
        self.events = []; self.observations = {}
        f = self.fixture
        target = f.root / 'native method with spaces #percent% (3.0.5)'
        f.method.rename(target); f.method = target; f.args.method_root = target
        self.native = target / 'plugins/spec'
        self.guide = self.native / 'references/GETTING_STARTED.md'
        self.documentation = []
        for link in links(self.guide.read_text()):
            path, fragment = local_target(self.guide, link)
            if path is not None and not path.exists():
                self.assertTrue(path.is_relative_to(target / 'standards'))
                path.parent.mkdir(parents=True, exist_ok=True)
                heading = fragment.replace('-', ' ') if fragment else 'Controlled canonical documentation fixture'
                path.write_text('# ' + heading + '\n')
                self.documentation.append(path)
        self.assertEqual(len(self.documentation), 9)
        self.select_native()
        self.addCleanup(self.retain_observations)

    def select_native(self):
        """A selected synthetic manager verifies the full fixture, including docs."""
        f = self.fixture
        native = m.tree(self.native)
        standards = m.tree(f.method / 'standards')
        manifest = {'release': {'cut': 'v3.0.5'},
                    'auxiliary': {'plugin': {'installed_root': 'plugins/spec',
                        'member_count': len(native), 'members': [{'path': k, 'sha256': m.sha(v)} for k, v in native.items()]}},
                    'standards': {'installed_root': 'standards', 'member_count': len(standards),
                        'members': [{'path': k, 'sha256': m.sha(v)} for k, v in standards.items()]}}
        raw = m.encode(manifest); (f.method / 'manifest.json').write_bytes(raw)
        definition = json.loads(f.definition.read_bytes())
        definition['constitution']['stdo']['basis']['manifest_sha256'] = m.sha(raw)
        f.definition.write_bytes(m.encode(definition))
        self.manager_log = f.root / 'manager-calls.jsonl'
        f.manager.write_text(
            '#!/usr/bin/env python3\n'
            'from pathlib import Path\nimport hashlib,json,sys\n'
            'assert sys.argv[1] == "status" and sys.argv[-1] == "--verify"\n'
            'definition=Path(sys.argv[sys.argv.index("--definition")+1])\n'
            'basis=json.loads(definition.read_bytes())["constitution"]["stdo"]["basis"]\n'
            'root=Path(' + repr(str(f.method)) + ')\n'
            'log=Path(' + repr(str(self.manager_log)) + ')\n'
            'with log.open("a") as out:out.write(json.dumps(sys.argv)+"\\n")\n'
            'failures=[]\n'
            'try:\n'
            ' raw=(root/"manifest.json").read_bytes();manifest=json.loads(raw)\n'
            ' if hashlib.sha256(raw).hexdigest()!=basis["manifest_sha256"]:failures.append("manifest")\n'
            ' for group in (manifest["auxiliary"]["plugin"],manifest["standards"]):\n'
            '  for row in group["members"]:\n'
            '   path=root/group["installed_root"]/row["path"]\n'
            '   if hashlib.sha256(path.read_bytes()).hexdigest()!=row["sha256"]:failures.append(str(path))\n'
            'except (OSError,ValueError,KeyError):failures.append("missing or malformed installation")\n'
            'print(json.dumps({"basis":basis["uri"],"manifest_sha256":basis["manifest_sha256"],'
            '"installed":root.is_dir(),"valid":not failures,"failures":failures,"path":str(root),"definition":str(definition)}))\n')

    def retain_observations(self):
        destination = os.environ.get('STDO_SKILLS_NATIVE_CUSTODY')
        if destination:
            path = Path(destination); path.mkdir(parents=True, exist_ok=True)
            value = {'case': self.id(), 'events': self.events, 'observations': self.observations,
                     'scope': 'Actual public CLI over controlled native/manager/provider inputs; no LLM or released-native qualification.'}
            with (path / (self._testMethodName + '.json')).open('xb') as out:
                out.write(m.encode(value))

    def cli(self, command, host='codex', receipt=None, expected=0, package=None):
        f = self.fixture
        args = ['--host', host, '--workspace', str(f.workspace)]
        if command in ('plan', 'install'):
            args += ['--package', str(package or f.package), '--definition', str(f.definition),
                     '--method-root', str(f.method), '--ac-root', str(f.ac),
                     '--stdo', str(f.manager), '--python', m.sys.executable]
        elif command == 'check-runtime':
            args = ['--configuration', str(m.paths(f.workspace, host)[1] / 'CONFIG.json')]
        else:
            args += ['--receipt-sha256', receipt]
        argv = [m.sys.executable, '-B', str(installation.ROOT / 'scripts/manage_skills.py'), command, *args]
        result = subprocess.run(argv, capture_output=True, text=True)
        self.events.append({'argv': argv, 'returncode': result.returncode,
                            'stdout': result.stdout, 'stderr': result.stderr})
        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        return json.loads(result.stdout)

    def snapshot(self, root=None):
        return {k: m.sha(v) for k, v in m.tree(root or self.fixture.method).items()}

    def test_both_public_routes_keep_canonical_links_metadata_and_safe_removal(self):
        original = self.snapshot(); observations = []
        for host in ('codex', 'claude'):
            base, bundle, receipt_path = m.paths(self.fixture.workspace, host)
            self.cli('plan', host); self.assertFalse(base.exists())
            installed = self.cli('install', host); receipt = installed['receipt_sha256']
            self.cli('verify', host, receipt); self.cli('check-runtime', host)
            config = json.loads((bundle / 'CONFIG.json').read_bytes())
            record = json.loads(receipt_path.read_bytes())
            self.assertEqual(config['native_workflow'], record['native_workflow'])
            self.assertEqual(config['native_workflow']['root'], str(self.native))
            self.assertFalse((bundle / 'native').exists())
            for name in (*m.CORE, *(('stdo-refresh',) if host == 'claude' else ())):
                wrapper = base / 'skills' / name / 'SKILL.md'
                body = wrapper.read_text(); destination = re.search(r'\[native workflow\]\(([^)]+)\)', body).group(1)
                self.assertIn('%20', destination); self.assertIn('%23', destination)
                path, fragment = local_target(wrapper, destination)
                expected = self.native / ('claude-skills/refresh/SKILL.md' if name == 'stdo-refresh' else 'skills/' + name + '/SKILL.md')
                self.assertEqual(path, expected); self.assertEqual(fragment, '')
                self.assertEqual(body.split('---', 2)[1], re.sub(r'^name:[^\n]*', 'name: ' + name, path.read_text().split('---', 2)[1], flags=re.M))
                for link in links(body):
                    local, _ = local_target(wrapper, link)
                    self.assertTrue(local.is_file(), (wrapper, link))
            # Exercise the user's actual chain, then every local guide route.
            help_path = self.native / 'skills/stdo-help/SKILL.md'
            guide_link = next(x for x in links(help_path.read_text()) if 'GETTING_STARTED.md' in x)
            guide, _ = local_target(help_path, guide_link); self.assertEqual(guide, self.guide)
            resolved = []
            for link in links(guide.read_text()):
                target, fragment = local_target(guide, link)
                if target is None: continue
                self.assertTrue(target.is_file(), (link, target))
                if fragment: self.assertIn(fragment, anchors(target.read_text()), (link, fragment))
                resolved.append({'link': link, 'target': str(target), 'fragment': fragment})
            observations.append({'host': host, 'local_getting_started_routes': resolved})
            unrelated = base / 'skills/unrelated/SKILL.md'; unrelated.parent.mkdir(); unrelated.write_text('unrelated')
            calls = self.manager_log.read_bytes()
            self.cli('remove', host, receipt)
            self.assertEqual(self.manager_log.read_bytes(), calls, 'Removal must not invoke the native dependency')
            self.assertEqual(unrelated.read_text(), 'unrelated'); self.assertFalse(bundle.exists())
            self.assertEqual(self.snapshot(), original)
        self.observations.update(native_unchanged=original, routes=observations)

    def test_complete_frontmatter_preserves_multiline_and_optional_invocation_fields(self):
        source = self.native / 'skills/stdo-work/SKILL.md'
        header = ('---\nname: stdo-work\ndescription: >-\n  A multiline native description\n  with a second line.\n'
                  'argument-hint: "<value with spaces>"\ndisable-model-invocation: true\n'
                  'user-invocable: false\nallowed-tools: Read, Write\nmodel: inherit\ncontext: fork\n'
                  'agent: reviewer\nmetadata:\n  name: nested-name\n  custom: "yes"\nhooks:\n  Stop: []\n---\n')
        source.write_text(header + '\n# Native body\n'); self.select_native()
        for host in ('codex', 'claude'):
            self.cli('plan', host); self.cli('install', host)
            base, _, _ = m.paths(self.fixture.workspace, host)
            self.assertTrue((base / 'skills/stdo-work/SKILL.md').read_bytes().startswith(header.encode()))

    def test_malformed_native_frontmatter_refuses_plan_before_host_effects(self):
        source = self.native / 'skills/stdo-work/SKILL.md'
        for body in ('name: no-delimiter\ndescription: invalid\n',
                     '---\nname: stdo-work\nname: duplicate\ndescription: invalid\n---\n'):
            source.write_text(body); self.select_native()
            for host in ('codex', 'claude'):
                self.cli('plan', host, expected=2)
                self.assertFalse(m.paths(self.fixture.workspace, host)[0].exists())

    def test_canonical_changes_refuse_verification_but_never_block_owned_removal(self):
        for host in ('codex', 'claude'):
            installed = self.cli('install', host); receipt = installed['receipt_sha256']
            base, bundle, _ = m.paths(self.fixture.workspace, host); owned = self.snapshot(base / ('stdo-' + m.VERSION))
            for target in [self.documentation[0], self.native / 'skills/stdo-work/SKILL.md', self.fixture.method / 'manifest.json']:
                original = target.read_bytes(); target.write_bytes(original + b'changed\n')
                try:
                    self.cli('verify', host, receipt, expected=2); self.cli('check-runtime', host, expected=2)
                    self.assertEqual(self.snapshot(bundle), owned)
                finally: target.write_bytes(original)
            missing = self.fixture.root / ('held-' + host); self.fixture.method.rename(missing)
            try:
                native_before = self.snapshot(missing)
                self.cli('verify', host, receipt, expected=2); self.cli('check-runtime', host, expected=2)
                calls = self.manager_log.read_bytes(); self.cli('remove', host, receipt)
                self.assertEqual(self.manager_log.read_bytes(), calls)
                self.assertEqual(self.snapshot(missing), native_before)
            finally: missing.rename(self.fixture.method)

    def test_legacy_receipt_removal_stays_owned_file_only(self):
        for host in ('codex', 'claude'):
            self.cli('install', host)
            base, bundle, receipt_path = m.paths(self.fixture.workspace, host)
            config = json.loads((bundle / 'CONFIG.json').read_bytes()); del config['native_workflow']
            (bundle / 'CONFIG.json').write_bytes(m.encode(config))
            shutil.copytree(self.native, bundle / 'native')
            receipt = json.loads(receipt_path.read_bytes()); del receipt['native_workflow']
            receipt['files'] = {root + '/' + name: m.sha(raw) for root in receipt['roots'] for name, raw in m.tree(base / root).items()}
            receipt_path.write_bytes(m.encode(receipt)); digest = m.sha(receipt_path.read_bytes())
            before = self.snapshot(); calls = self.manager_log.read_bytes()
            self.cli('verify', host, digest); self.cli('remove', host, digest)
            self.assertEqual(self.manager_log.read_bytes(), calls); self.assertEqual(self.snapshot(), before)
        self.observations['legacy_scope'] = 'Controlled prior-schema owned-copy receipts; separate actual pre-repair installs are retained in the task evidence.'

    def test_changed_source_does_not_silently_refresh_published_package(self):
        original = (installation.ROOT / 'release/3.0.5/manifest.json').read_bytes()
        self.cli('plan', package=installation.ROOT, expected=2)
        self.assertEqual((installation.ROOT / 'release/3.0.5/manifest.json').read_bytes(), original)
        self.assertFalse(m.paths(self.fixture.workspace, 'codex')[0].exists())


if __name__ == '__main__': unittest.main()
