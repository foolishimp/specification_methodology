#!/usr/bin/env python3
"""Tests for generate_frames.py: the five generator requirements of
design/CROSS_SYNTHESIS.md part 5, the RW1 F14 sections, byte-identical
regeneration, the frame layout and link rebasing.

Run: python3 -I qualification/instruments/test_generate_frames.py
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import posixpath
import re
import shutil
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
TENANT = HERE.parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


gf = load('generate_frames', HERE / 'generate_frames.py')
bs = load('bounded_step', HERE / 'bounded_step.py')


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def member(text: str, name='standards/X.md'):
    return gf.Member(name, text.encode('utf-8'))


def codex_extent(text: str, anchor: str) -> str:
    """Codex refresh_views.py lines 52-58 at 31f28f9, re-implemented for comparison."""
    headings = list(re.finditer(r'^(#{2,6}) (.+)$', text, re.M))
    matches = [(i, h) for i, h in enumerate(headings) if gf.slug(h[2]) == anchor]
    i, h = matches[0]
    end = next((n.start() for n in headings[i + 1:] if len(n[1]) <= len(h[1])), len(text))
    return text[h.start():end]


class TempTree:
    """A tenant-shaped temporary root with standards/ and standards/frames/."""

    def __init__(self, members, frames, kind='verbatim_reference_frames'):
        self.dir = tempfile.TemporaryDirectory()
        self.root = Path(self.dir.name)
        (self.root / 'standards' / 'frames').mkdir(parents=True)
        for name, text in members.items():
            (self.root / 'standards' / name).write_bytes(text.encode('utf-8'))
        self.inputs = self.root / 'standards' / 'frames' / 'FRAME_INPUTS.json'
        self.inputs.write_text(json.dumps({'kind': kind, 'limits': [], 'frames': frames}, indent=2) + '\n')

    def files(self):
        return {p.relative_to(self.root): p.read_bytes()
                for p in sorted(self.root.rglob('*')) if p.is_file()}

    def run(self, *args):
        return gf.main(['--root', str(self.root), *args])

    def close(self):
        self.dir.cleanup()


def frame(fid, *routes, task='t', scope='s'):
    return {'id': fid, 'task': task, 'scope': scope,
            'routes': [{'owner': f'standards/{o}', 'anchor': a} for o, a in routes]}


DOC = """# DOC

## 1. Alpha

Alpha text.

```markdown
# Template
## Inside heading
```

Alpha after fence.

### Alpha sub

Sub text.

~~~~
## Tilde inside
```
## Still inside the tilde block
~~~~

Tail of alpha sub.

## 2. Beta

Beta text.
"""


class SlugRule(unittest.TestCase):
    """Requirement 1: one heading-slug rule."""

    def test_examples(self):
        self.assertEqual(gf.slug('RF-012 Closed results'), 'rf-012-closed-results')
        self.assertEqual(gf.slug('11. The activation packet'), '11-the-activation-packet')
        self.assertEqual(gf.slug('The workspace and an actor\'s account'), 'the-workspace-and-an-actors-account')
        self.assertEqual(gf.slug('`code` <b>tag</b> x'), 'code-tag-x')

    def test_agrees_with_bounded_step_on_every_member_heading(self):
        for path in sorted((TENANT / 'standards').glob('*.md')):
            m = gf.load_member(TENANT, f'standards/{path.name}')
            for index, _, title, anchor in m.headings:
                line = gf.bare(m.lines[index])
                other = bs.HEADING.match(line)
                self.assertIsNotNone(other, f'{path.name}:{index + 1}')
                self.assertEqual(anchor, bs.slug_of(other.group(2)), f'{path.name}:{index + 1}')


class FencedCode(unittest.TestCase):
    """Requirement 2: fenced code is not structure."""

    def test_headings_inside_fences_are_neither_anchors_nor_ends(self):
        m = member(DOC)
        anchors = [h[3] for h in m.headings]
        self.assertEqual(anchors, ['doc', '1-alpha', 'alpha-sub', '2-beta'])
        self.assertEqual({h[3] for h in m.fenced_headings},
                         {'template', 'inside-heading', 'tilde-inside', 'still-inside-the-tilde-block'})

    def test_section_runs_to_next_outside_heading_of_equal_or_higher_level(self):
        m = member(DOC)
        _, _, extent = m.section('1-alpha')
        text = extent.decode()
        self.assertTrue(text.startswith('## 1. Alpha\n'))
        self.assertIn('## Inside heading\n', text)
        self.assertIn('## Still inside the tilde block\n', text)
        self.assertTrue(text.endswith('Tail of alpha sub.\n\n'))
        self.assertNotIn('## 2. Beta', text)
        _, _, sub = m.section('alpha-sub')
        self.assertTrue(sub.decode().startswith('### Alpha sub\n'))
        self.assertTrue(sub.decode().endswith('Tail of alpha sub.\n\n'))

    def test_last_section_runs_to_end_of_member(self):
        _, _, extent = member(DOC).section('2-beta')
        self.assertEqual(extent.decode(), '## 2. Beta\n\nBeta text.\n')

    def test_close_needs_same_character_at_least_as_long(self):
        text = '## A\n\n````\n```\n## not a heading\n~~~~\n````\n\n## B\n'
        m = member(text)
        self.assertEqual([h[3] for h in m.headings], ['a', 'b'])
        _, _, extent = m.section('a')
        self.assertIn(b'## not a heading', extent)

    def test_fence_indented_up_to_three_spaces_opens(self):
        m = member('## A\n\n   ```\n## inside\n   ```\n\n## B\n')
        self.assertEqual([h[3] for h in m.headings], ['a', 'b'])

    def test_level_one_heading_ends_a_section(self):
        m = member('## A\n\nx\n\n# Top\n\ny\n')
        _, _, extent = m.section('a')
        self.assertEqual(extent, b'## A\n\nx\n\n')

    def test_codex_rule_would_cut_the_section_short(self):
        self.assertTrue(len(codex_extent(DOC, '1-alpha')) < len(member(DOC).section('1-alpha')[2].decode()))


class Refusals(unittest.TestCase):
    """Requirement 3: refusal, never truncation; each refusal names member and line."""

    def refused(self, text, anchor='a'):
        with self.assertRaises(gf.Refusal) as caught:
            member(text).section(anchor)
        return caught.exception

    def test_absent_anchor(self):
        r = self.refused('## B\n\nx\n', 'a')
        self.assertIn('matches no heading', r.reason)
        self.assertEqual(r.member, 'standards/X.md')

    def test_anchor_only_inside_fence_names_its_line(self):
        r = self.refused('## B\n\n```\n## A\n```\n', 'a')
        self.assertEqual(r.line, 4)
        self.assertIn('only a heading inside a fenced block', r.reason)

    def test_duplicate_anchor(self):
        r = self.refused('## A\n\nx\n\n## A\n\ny\n', 'a')
        self.assertEqual(r.line, 1)
        self.assertIn('lines 1, 5', r.reason)

    def test_section_would_end_inside_open_fence(self):
        r = self.refused('## A\n\n```\n## B\n', 'a')
        self.assertEqual(r.line, 4)
        self.assertIn('would end inside the fenced block opened at line 3', r.reason)

    def test_fence_open_at_end_of_member(self):
        r = self.refused('## A\n\nx\n\n## B\n\n~~~\ny\n', 'a')
        self.assertEqual(r.line, 7)
        self.assertIn('still open at the end of the member', r.reason)

    def test_fence_like_line_indented_four_spaces(self):
        with self.assertRaises(gf.Refusal) as caught:
            member('## A\n\n    ```\n## B\n')
        self.assertEqual(caught.exception.line, 3)
        self.assertIn('indented by four or more spaces', caught.exception.reason)

    def test_fence_like_line_indented_four_spaces_inside_a_fence(self):
        with self.assertRaises(gf.Refusal) as caught:
            member('## A\n\n```\n    ~~~\n```\n')
        self.assertEqual(caught.exception.line, 4)

    def test_fence_like_line_indented_by_tab(self):
        with self.assertRaises(gf.Refusal) as caught:
            member('## A\n\n\t```\n')
        self.assertEqual(caught.exception.line, 3)

    def test_setext_equals_under_text(self):
        with self.assertRaises(gf.Refusal) as caught:
            member('## A\n\nTitle\n=====\n')
        self.assertEqual(caught.exception.line, 4)
        self.assertIn('setext', caught.exception.reason)

    def test_setext_dashes_under_text(self):
        with self.assertRaises(gf.Refusal) as caught:
            member('## A\n\nTitle\n---\n')
        self.assertEqual(caught.exception.line, 4)

    def test_rule_after_blank_line_or_inside_fence_is_not_refused(self):
        member('## A\n\nText\n\n---\n\n```\nText\n---\n```\n')

    def test_refusal_writes_no_file(self):
        tree = TempTree({'M.md': '## A\n\nx\n\n## B\n\ny\n'},
                        [frame('good', ('M.md', 'a')), frame('bad', ('M.md', 'absent'))])
        try:
            before = tree.files()
            self.assertEqual(tree.run(), 2)
            self.assertEqual(tree.files(), before)
        finally:
            tree.close()

    def test_frame_over_limit_is_refused_not_truncated(self):
        big = '## A\n\n' + ('x' * 99 + '\n') * (gf.MAX_FRAME_BYTES // 100 + 10)
        tree = TempTree({'M.md': big}, [frame('big', ('M.md', 'a'))])
        try:
            before = tree.files()
            self.assertEqual(tree.run(), 2)
            self.assertEqual(tree.files(), before)
        finally:
            tree.close()

    def test_overlapping_routes_are_refused(self):
        tree = TempTree({'M.md': DOC}, [frame('o', ('M.md', '1-alpha'), ('M.md', 'alpha-sub'))])
        try:
            self.assertEqual(tree.run(), 2)
        finally:
            tree.close()


class InputRefusals(unittest.TestCase):
    """The remaining refusal sites of the generator, each refused with nothing written."""

    def assert_refused(self, tree, reason):
        try:
            before = tree.files()
            with self.assertRaises(gf.Refusal) as caught:
                gf.build(tree.root, tree.inputs)
            self.assertIn(reason, caught.exception.reason)
            self.assertEqual(tree.run(), 2)
            self.assertEqual(tree.files(), before)
            return caught.exception
        finally:
            tree.close()

    def test_owner_outside_standards(self):
        tree = TempTree({'M.md': '## A\n'}, [])
        (tree.root / 'other').mkdir()
        (tree.root / 'other' / 'M.md').write_text('## A\n')
        tree.inputs.write_text(json.dumps({'kind': 'k', 'limits': [], 'frames': [
            {'id': 'f', 'task': 't', 'scope': 's', 'routes': [{'owner': 'other/M.md', 'anchor': 'a'}]}]}))
        self.assert_refused(tree, 'not a member under standards/')

    def test_owner_missing(self):
        self.assert_refused(TempTree({'M.md': '## A\n'}, [frame('f', ('Absent.md', 'a'))]),
                            'does not exist')

    def test_member_not_utf8(self):
        tree = TempTree({}, [frame('f', ('M.md', 'a'))])
        (tree.root / 'standards' / 'M.md').write_bytes(b'## A\n\n\xff\n')
        r = self.assert_refused(tree, 'not valid UTF-8')
        self.assertEqual(r.line, 3)

    def test_malformed_frame_id(self):
        self.assert_refused(TempTree({'M.md': '## A\n'}, [frame('Bad Id', ('M.md', 'a'))]),
                            'malformed or repeated')

    def test_repeated_frame_id(self):
        self.assert_refused(TempTree({'M.md': '## A\n'}, [frame('f', ('M.md', 'a')), frame('f', ('M.md', 'a'))]),
                            'malformed or repeated')

    def test_frame_without_routes(self):
        self.assert_refused(TempTree({'M.md': '## A\n'}, [frame('f')]), 'has no routes')

    def test_unreadable_inputs(self):
        tree = TempTree({'M.md': '## A\n'}, [])
        tree.inputs.write_text('{not json')
        self.assert_refused(tree, 'frame inputs unreadable')


class Digests(unittest.TestCase):
    """Requirement 4: digests over the full extent; the frame carries those bytes."""

    def setUp(self):
        self.tree = TempTree({'DOC.md': DOC, 'M.md': '## A\n\nno trailing newline'},
                             [frame('f', ('DOC.md', '1-alpha'), ('M.md', 'a'), ('DOC.md', '2-beta'))])

    def tearDown(self):
        self.tree.close()

    def test_manifest_and_frame(self):
        self.assertEqual(self.tree.run(), 0)
        manifest = json.loads(self.tree.inputs.read_text())
        entry = manifest['frames'][0]
        data = (self.tree.root / entry['path']).read_bytes()
        self.assertEqual(entry['bytes'], len(data))
        self.assertEqual(entry['sha256'], sha256(data))
        self.assertIn(f'Size of this frame: {len(data)} bytes.'.encode(), data)
        for route in entry['routes']:
            owner_bytes = (self.tree.root / route['owner']).read_bytes()
            self.assertEqual(route['owner_sha256'], sha256(owner_bytes))
            m = gf.Member(route['owner'], owner_bytes)
            start, end, extent = m.section(route['anchor'])
            self.assertEqual(route['section_sha256'], sha256(extent))
            line = (f'Source: {Path(route["owner"]).name}#{route["anchor"]} '
                    f'sha256={route["owner_sha256"]}').encode()
            self.assertIn(line + b'\n\n' + gf.rebase(m, start, end), data)
        self.assertIn(b'## Still inside the tilde block\n', data)
        self.assertTrue(data.endswith(b'\n'))
        self.assertEqual(list(manifest), ['kind', 'limits', 'frames'])
        self.assertEqual(list(entry), ['id', 'path', 'task', 'bytes', 'sha256', 'scope', 'routes'])
        self.assertEqual(list(entry['routes'][0]), ['owner', 'owner_sha256', 'anchor', 'section_sha256'])


class Regeneration(unittest.TestCase):
    """Regeneration is byte-identical; a changed member is detected as drift."""

    def test_byte_identical_and_drift(self):
        tree = TempTree({'DOC.md': DOC}, [frame('f', ('DOC.md', '1-alpha'), ('DOC.md', '2-beta'))])
        try:
            self.assertEqual(tree.run(), 0)
            first = tree.files()
            self.assertEqual(tree.run('--check'), 0)
            self.assertEqual(tree.run(), 0)
            self.assertEqual(tree.files(), first)
            (tree.root / 'standards' / 'DOC.md').write_text(DOC.replace('Beta text.', 'Beta text, changed.'))
            self.assertEqual(tree.run('--check'), 1)
            self.assertEqual(tree.run(), 0)
            manifest = json.loads(tree.inputs.read_text())
            routes = manifest['frames'][0]['routes']
            old = json.loads(first[Path('standards/frames/FRAME_INPUTS.json')])['frames'][0]['routes']
            self.assertNotEqual(routes[0]['owner_sha256'], old[0]['owner_sha256'])
            self.assertEqual(routes[0]['section_sha256'], old[0]['section_sha256'])
            self.assertNotEqual(routes[1]['section_sha256'], old[1]['section_sha256'])
        finally:
            tree.close()

    def test_tenant_regeneration_is_byte_identical_in_memory(self):
        inputs = TENANT / gf.INPUTS_RELATIVE
        first = gf.build(TENANT, inputs)
        second = gf.build(TENANT, inputs)
        self.assertEqual(first, second)


# RW1 finding F14: sections that end early under the Codex rule at a heading
# inside a fenced block. Anchors are those of the current members.
F14_SECTIONS = [
    ('REFERENCE_FRAME.md', '11-the-activation-packet'),
    ('REFERENCE_FRAME.md', 'minimal-activation-binding'),
    ('REFERENCE_FRAME.md', '13-minimal-declarations'),
    ('REFERENCE_FRAME.md', 'minimal-frame-declaration'),
    ('REFERENCE_FRAME.md', 'minimal-frame-set-declaration'),
    ('POSTING_GUIDE.md', '6-structure'),
    ('TICKETS.md', '6-implementation-migration'),
    ('TICKETS.md', 'declaration-and-checklist'),
    ('TICKETS.md', '8-recommended-shapes'),
]


class F14Sections(unittest.TestCase):
    """Requirement 5: each RW1 F14 section is extracted to its full extent."""

    def test_full_extent(self):
        for name, anchor in F14_SECTIONS:
            with self.subTest(section=f'{name}#{anchor}'):
                m = gf.load_member(TENANT, f'standards/{name}')
                start, end, extent = m.section(anchor)
                level = next(h[1] for h in m.headings if h[0] == start)
                inside = [h for h in m.fenced_headings if start < h[0] < end]
                self.assertTrue(inside, 'the section holds a heading line inside a fenced block')
                for index, _, _, _ in inside:
                    self.assertIn(m.lines[index], extent)
                following = [h for h in m.headings if h[0] >= end]
                if following:
                    self.assertEqual(following[0][0], end)
                    self.assertLessEqual(following[0][1], level)
                else:
                    self.assertEqual(end, len(m.lines))
                text = m.data.decode('utf-8')
                self.assertLess(len(codex_extent(text, anchor).encode()), len(extent),
                                'the Codex rule would end this section early')


class TenantFrames(unittest.TestCase):
    """The frame inputs of this tenant build within the limit and route the result algebra."""

    def test_frames(self):
        inputs = TENANT / gf.INPUTS_RELATIVE
        outputs = gf.build(TENANT, inputs)
        manifest = json.loads(outputs[inputs])
        ids = [f['id'] for f in manifest['frames']]
        for fid in ('rf-task-a', 'rf-task-b', 'ac-task-a', 'traversal-task-f'):
            self.assertIn(fid, ids)
        for entry in manifest['frames']:
            self.assertLessEqual(entry['bytes'], gf.MAX_FRAME_BYTES)
            routes = [(r['owner'], r['anchor']) for r in entry['routes']]
            self.assertIn(('standards/FOUNDATIONS.md', 'results'), routes)
            data = outputs[TENANT / entry['path']]
            sources = re.findall(rb'^Source: (\S+)#(\S+) sha256=([0-9a-f]{64})(?: rows=\d+/\d+ [^\n]*)?$', data, re.M)
            self.assertEqual([(Path(o).name, a) for o, a in routes],
                             [(s[0].decode(), s[1].decode()) for s in sources])


def rebased(text: str, name='standards/M.md') -> str:
    """The whole member `text` as its frame would carry it."""
    m = member(text, name)
    return gf.rebase(m, 0, len(m.lines)).decode('utf-8')


# A member with every link form the rule names. Each line's expected
# rebasing from standards/frames/ is in LINKED_EXPECTED.
LINKED = """## A

See [X](X.md#a), [X file](X.md), [here](#a), [query](?v=1) and ![img](img/p.png).
Up [spec](../../specification/requirements/README.md#single-result-algebra-requirement).
Kept [rc2](stdo://releases/v2.5.1-rc.2/standards/X.md#a), [web](https://example.org/x.md),
[mail](mailto:a@example.org), [root](/abs/X.md) and [empty]().
Title [t](X.md "a title") and angle [s](<Y Z.md#b>) and nested [a [b] c](X.md#n).
A link whose text
spans [two
lines](X.md#two).
Code `[c](X.md)` and ``[d](X.md) ` x`` stay; a span `[e](X.md)
over two lines` stays.
Escaped \\[f](X.md) and notation f[t](a, b) are not links.

[ref]: X.md#r
[abs]: stdo://x/Y.md

- item [li](X.md#li)
  continued `code
- next` item [li2](X.md)

| col | [cell](X.md#c) |

```markdown
[fenced](X.md#f)
```

~~~
[tilde](#t)
~~~
"""

LINKED_EXPECTED = """## A

See [X](../X.md#a), [X file](../X.md), [here](../M.md#a), [query](../M.md?v=1) and ![img](../img/p.png).
Up [spec](../../../specification/requirements/README.md#single-result-algebra-requirement).
Kept [rc2](stdo://releases/v2.5.1-rc.2/standards/X.md#a), [web](https://example.org/x.md),
[mail](mailto:a@example.org), [root](/abs/X.md) and [empty]().
Title [t](../X.md "a title") and angle [s](<../Y Z.md#b>) and nested [a [b] c](../X.md#n).
A link whose text
spans [two
lines](../X.md#two).
Code `[c](X.md)` and ``[d](X.md) ` x`` stay; a span `[e](X.md)
over two lines` stays.
Escaped \\[f](X.md) and notation f[t](a, b) are not links.

[ref]: ../X.md#r
[abs]: stdo://x/Y.md

- item [li](../X.md#li)
  continued `code
- next` item [li2](../X.md)

| col | [cell](../X.md#c) |

```markdown
[fenced](X.md#f)
```

~~~
[tilde](#t)
~~~
"""


class LinkRebasing(unittest.TestCase):
    """F5: relative links in an excerpt resolve from standards/frames/; nothing else changes."""

    def test_every_link_form(self):
        got = rebased(LINKED).splitlines()
        want = LINKED_EXPECTED.splitlines()
        self.assertEqual(len(got), len(want))
        for n, (g, w) in enumerate(zip(got, want), 1):
            self.assertEqual(g, w, f'line {n}')

    def test_relative_and_in_member_fragment(self):
        self.assertEqual(rebased('[a](X.md#a)\n'), '[a](../X.md#a)\n')
        self.assertEqual(rebased('[a](#a)\n', 'standards/FOUNDATIONS.md'), '[a](../FOUNDATIONS.md#a)\n')
        self.assertEqual(rebased('[a](sub/Y.md)\n'), '[a](../sub/Y.md)\n')

    def test_absolute_and_stdo_unchanged(self):
        for text in ('[a](stdo://releases/v2.5.1-rc.2/standards/X.md#a)\n', '[a](https://example.org/#x)\n',
                     '[a](urn:stdo:concept:x)\n', '[a](/X.md#a)\n', '[a](//host/X.md)\n'):
            with self.subTest(text=text):
                self.assertEqual(rebased(text), text)

    def test_fenced_code_untouched(self):
        text = '## A\n\n```text\n[a](X.md#a) F_K[v](X_v)\n```\n\n````\n```\n[b](#b)\n````\n'
        self.assertEqual(rebased(text), text)

    def test_owner_in_a_subdirectory(self):
        self.assertEqual(rebased('[a](X.md#a) [b](#b)\n', 'standards/schemas/S.md'),
                         '[a](../schemas/X.md#a) [b](../schemas/S.md#b)\n')

    def test_section_digest_is_over_owner_bytes_and_check_compares_rebased(self):
        owner = '## A\n\nSee [b](#b) and [X](X.md#x).\n\n## B\n\nBody.\n'
        tree = TempTree({'M.md': owner, 'X.md': '## X\n'}, [frame('f', ('M.md', 'a'))])
        try:
            self.assertEqual(tree.run(), 0)
            manifest = json.loads(tree.inputs.read_text())
            route = manifest['frames'][0]['routes'][0]
            raw = b'## A\n\nSee [b](#b) and [X](X.md#x).\n\n'
            copy = b'## A\n\nSee [b](../M.md#b) and [X](../X.md#x).\n\n'
            self.assertEqual(route['section_sha256'], sha256(raw))
            self.assertNotEqual(route['section_sha256'], sha256(copy))
            path = tree.root / 'standards' / 'frames' / 'f.md'
            data = path.read_bytes()
            self.assertIn(copy, data)
            self.assertNotIn(raw, data)
            self.assertEqual(tree.run('--check'), 0)
            path.write_bytes(data.replace(copy, raw))
            self.assertEqual(tree.run('--check'), 1)
            self.assertEqual(tree.run(), 0)
            self.assertEqual(path.read_bytes(), data)
        finally:
            tree.close()


class TenantLinkResolution(unittest.TestCase):
    """F5: from the published location standards/frames/, every rebased link of every tenant
    frame resolves to the target its original resolves to from the owner's directory, the
    target file exists, and each fragment names a heading of its target member."""

    LINK = re.compile(r'\]\(([^)\s]+)')   # this test's own finder, not the generator's

    def test_resolution_from_frames_directory(self):
        inputs = TENANT / gf.INPUTS_RELATIVE
        manifest = json.loads(gf.build(TENANT, inputs)[inputs])
        pairs, seen = 0, set()
        frames_dir = gf.FRAMES_RELATIVE.as_posix()
        for entry in manifest['frames']:
            for route in entry['routes']:
                if (route['owner'], route['anchor']) in seen:
                    continue
                seen.add((route['owner'], route['anchor']))
                m = gf.load_member(TENANT, route['owner'])
                start, end, extent = m.section(route['anchor'])
                raw_lines = gf.split_lines(extent)
                copy_lines = gf.split_lines(gf.rebase(m, start, end))
                self.assertEqual(len(raw_lines), len(copy_lines))
                owner_dir = posixpath.dirname(route['owner'])
                for k, (raw, copy) in enumerate(zip(raw_lines, copy_lines)):
                    where = f'{route["owner"]}:{start + k + 1}'
                    if m.fenced[start + k]:
                        self.assertEqual(raw, copy, where)
                        continue
                    originals = self.LINK.findall(raw.decode('utf-8'))
                    copies = self.LINK.findall(copy.decode('utf-8'))
                    self.assertEqual(len(originals), len(copies), where)
                    for original, rebased_link in zip(originals, copies):
                        pairs += 1
                        if gf.SCHEME.match(original) or original.startswith('/'):
                            self.assertEqual(original, rebased_link, where)
                            continue
                        path, _, fragment = original.partition('#')
                        new_path, _, new_fragment = rebased_link.partition('#')
                        target = posixpath.normpath(posixpath.join(owner_dir, path)) if path else route['owner']
                        resolved = posixpath.normpath(posixpath.join(frames_dir, new_path))
                        self.assertEqual((resolved, new_fragment), (target, fragment), where)
                        self.assertTrue((TENANT / resolved).is_file(), f'{where}: {rebased_link} names no file')
                        if fragment and resolved.endswith('.md'):
                            anchors = {h[3] for h in gf.Member(resolved, (TENANT / resolved).read_bytes()).headings}
                            self.assertIn(fragment, anchors, f'{where}: {rebased_link} names no heading')
        self.assertGreater(pairs, 0)




class RowSelection(unittest.TestCase):
    """Requirement 6 of design/CROSS_SYNTHESIS.md part 5: `rows: frame-anchors`."""
    TEXT = (
        '# M\n\n## Entry\n\ntext\n\n## Foundation to law\n\npreamble\n\n'
        '| Instance premise | Standing |\n|---|---|\n| I1 | adopted |\n\n'
        '| Premises, with standing | Consequence that follows | Rule in this member that states it | Added choice | Pillar |\n'
        '|---|---|---|---|---|\n'
        '| P1 | by P1 so a | [§1](#entry) | none | 1 |\n'
        '| P2 | by P2 so b | [§9](#other) | none | 2 |\n'
        '| P3 | by P3 so c | [Y §2](Y.md#yy); [§1](#entry) | none | 3 |\n'
        '| P4 | by P4 so d | (#entry) in code `[x](#entry)` | none | 4 |\n\n'
        'after the table\n\n## Other\n\nz\n')

    def test_keeps_header_prose_and_cited_rows_only(self):
        m = member(self.TEXT, 'standards/M.md')
        start, end, _ = m.section('foundation-to-law')
        idx, total, kept, _ = gf.select_rows(m, start, end, 'standards/M.md', {'M.md': {'entry'}, 'Y.md': set()})
        text = b''.join(m.lines[i] for i in idx).decode()
        self.assertEqual((total, kept), (4, 2))
        self.assertIn('| I1 | adopted |', text)            # non-family table kept whole
        self.assertIn('| P1 | by P1 so a', text)
        self.assertIn('| P3 | by P3 so c', text)
        self.assertNotIn('| P2 | by P2 so b', text)
        self.assertNotIn('| P4 |', text)                    # bare (#entry) is not a link destination
        self.assertIn('preamble', text); self.assertIn('after the table', text)

    def test_cross_member_link_counts_when_that_owner_route_is_carried(self):
        m = member(self.TEXT, 'standards/M.md')
        start, end, _ = m.section('foundation-to-law')
        idx, total, kept, _ = gf.select_rows(m, start, end, 'standards/M.md', {'Y.md': {'yy'}})
        self.assertEqual((total, kept), (4, 1))

    def test_build_records_rows_and_marks_source_line(self):
        tree = TempTree({'M.md': self.TEXT, 'Y.md': '# Y\n\n## yy\n\nq\n'},
                        [{'id': 'f', 'task': 't', 'scope': 's', 'routes': [
                            {'owner': 'standards/M.md', 'anchor': 'entry'},
                            {'owner': 'standards/M.md', 'anchor': 'foundation-to-law', 'rows': {'mode': 'frame-anchors'}}]}])
        try:
            out = gf.build(tree.root, tree.inputs)
            frame = out[tree.root / 'standards/frames/f.md'].decode()
            manifest = json.loads(out[tree.inputs].decode())
            self.assertIn('rows=2/4 selected by the anchors this frame carries', frame)
            rows = manifest['frames'][0]['routes'][1]['rows']
            self.assertEqual((rows['mode'], rows['selected'], rows['total']), ('frame-anchors', 2, 4))
            self.assertEqual(len(rows['excerpt_sha256']), 64)
        finally:
            tree.close()


class Bindings(unittest.TestCase):
    """I5, E2E-01: a frame binds obligations by owner section and digest without copying it;
    --check tells section drift from owner-digest-only drift."""

    def test_binds_rendered_and_recorded(self):
        fr = frame('f', ('M.md', 'a'))
        fr['binds'] = [{'text': 'binds the relation', 'owner': 'standards/M.md', 'anchor': 'b'},
                       {'text': 'plain bind'}]
        tree = TempTree({'M.md': '## A\n\nalpha\n\n## B\n\nbeta\n'}, [fr])
        try:
            self.assertEqual(tree.run(), 0)
            data = (tree.root / 'standards/frames/f.md').read_text()
            owner = sha256((tree.root / 'standards/M.md').read_bytes())
            self.assertIn('Binds:\n\n- binds the relation (M.md#b sha256=' + owner + ')\n- plain bind\n', data)
            self.assertNotIn('\nbeta\n', data.split('Routes, in order:')[0])
            entry = json.loads(tree.inputs.read_text())['frames'][0]
            self.assertEqual(list(entry), ['id', 'path', 'task', 'bytes', 'sha256', 'scope', 'binds', 'routes'])
            self.assertEqual(entry['binds'][0]['owner_sha256'], owner)
            self.assertEqual(entry['binds'][0]['section_sha256'], sha256(b'## B\n\nbeta\n'))
            self.assertEqual(entry['binds'][1], {'text': 'plain bind'})
            self.assertEqual(tree.run('--check'), 0)
        finally:
            tree.close()

    def test_malformed_binds_refused(self):
        for bad in ('text', [], [{'owner': 'standards/M.md', 'anchor': 'a'}], [{'text': 'x', 'owner': 'standards/M.md'}],
                    [{'text': 'x', 'owner': 'standards/M.md', 'anchor': 'absent'}]):
            fr = frame('f', ('M.md', 'a'))
            fr['binds'] = bad
            tree = TempTree({'M.md': '## A\n'}, [fr])
            try:
                before = tree.files()
                self.assertEqual(tree.run(), 2, bad)
                self.assertEqual(tree.files(), before)
            finally:
                tree.close()

    def test_check_distinguishes_section_drift_from_owner_drift(self):
        import contextlib, io
        fr = frame('f', ('M.md', 'a'))
        fr['binds'] = [{'text': 'bind', 'owner': 'standards/M.md', 'anchor': 'c'}]
        tree = TempTree({'M.md': '## A\n\nalpha\n\n## B\n\nbeta\n\n## C\n\ngamma\n'}, [fr])
        try:
            self.assertEqual(tree.run(), 0)
            member = tree.root / 'standards/M.md'
            member.write_text(member.read_text().replace('beta', 'beta more'))
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                self.assertEqual(tree.run('--check'), 1)
            self.assertIn('owner-drift-only: f', out.getvalue())
            self.assertNotIn('section-drift', out.getvalue())
            member.write_text(member.read_text().replace('gamma', 'gamma more'))
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                self.assertEqual(tree.run('--check'), 1)
            self.assertIn('section-drift: f bind M.md#c', out.getvalue())
            member.write_text(member.read_text().replace('alpha', 'alpha more'))
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                self.assertEqual(tree.run('--check'), 1)
            self.assertIn('section-drift: f M.md#a', out.getvalue())
        finally:
            tree.close()

    def test_tenant_frames_all_bind_the_construction_relation(self):
        manifest = json.loads((TENANT / 'standards/frames/FRAME_INPUTS.json').read_text())
        for fr in manifest['frames']:
            owners = {(b.get('owner'), b.get('anchor')) for b in fr.get('binds') or []}
            self.assertIn(('standards/ACTIVATION.md', 'construction-relation'), owners, fr['id'])


class ConsumerItems(unittest.TestCase):
    """I5-02: in a rows-mode excerpt the consumers paragraph keeps only the items of the kept rows."""

    TEXT = ("## Foundation to law\n\npreamble\n\n"
            "| Premises, with standing | Consequence that follows | Rule in this member that states it | Added choice | Pillar |\n"
            "|---|---|---|---|---|\n"
            "| P1 | by P1 so a | [entry](#entry) | none | 1 |\n"
            "| P2 | by P2 so b | [other](#other) | none | 1 |\n"
            "| P3 | by P3 so c | [entry](#entry) | none | 1 |\n"
            "| P4 | by P4 so d | [yy](Y.md#yy) | none | 1 |\n\n"
            "Consumers of these rows, one list per row:\n\n"
            "- Row 1, a: [X](#entry).\n- Row 2, b: [X](#other).\n- Row 3, c: no separate consumer applies.\n- Row 4, d: [Y](Y.md#yy).\n\n"
            "Each consumer applies the rule (P2, P6).\n\n## Entry\n\ntext\n\n## Other\n\ntext\n")

    def test_consumers_paragraph_omitted(self):
        m = member(self.TEXT, 'standards/M.md')
        start, end, _ = m.section('foundation-to-law')
        idx, total, kept, omitted = gf.select_rows(m, start, end, 'standards/M.md', {'M.md': {'entry'}})
        text = b''.join(m.lines[i] for i in idx).decode()
        self.assertEqual((total, kept, omitted), (4, 2, 4))
        self.assertNotIn('- Row ', text)
        self.assertNotIn('Consumers of these rows', text); self.assertNotIn('Each consumer applies', text)
        self.assertIn('| P1 | by P1 so a', text); self.assertIn('preamble', text)

    def test_build_records_consumer_items(self):
        fr = frame('f', ('M.md', 'foundation-to-law'), ('M.md', 'entry'))
        fr['routes'][0]['rows'] = {'mode': 'frame-anchors'}
        tree = TempTree({'M.md': self.TEXT}, [fr])
        try:
            self.assertEqual(tree.run(), 0)
            data = (tree.root / 'standards/frames/f.md').read_text()
            self.assertIn('rows=2/4 selected by the anchors this frame carries; the consumers paragraph of 4 items is omitted', data)
            self.assertNotIn('- Row 1, a', data)
            rows = json.loads(tree.inputs.read_text())['frames'][0]['routes'][0]['rows']
            self.assertEqual(rows['consumers_omitted'], 4)
        finally:
            tree.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
