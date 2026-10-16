#!/usr/bin/env python3
"""Generate reference frames copied from owning sections; confers no acceptance.

Reads the frame specifications in standards/frames/FRAME_INPUTS.json (frame
id, task, scope, ordered owner#anchor routes). For each route it extracts the
owning section byte for byte, rebases its relative link destinations (Link
rebasing below), prefixes it with a `Source:` line naming the member, the
anchor and the SHA-256 of the whole owning member, and writes
standards/frames/<id>.md with a short header (task, purpose, routes, measured
size). It records owner_sha256, section_sha256, the frame's bytes and sha256
back into FRAME_INPUTS.json. Regeneration from the same inputs is
byte-identical; a changed member changes the recorded digests.

Section rule (design/CROSS_SYNTHESIS.md, part 5, requirements 1 to 4):
- one heading-slug rule, `slug` below, copied from the Codex generator;
- a fenced code block opens at a line of three or more backticks or tildes
  indented by at most three spaces and closes only at a line of the same
  character at least as long; no line inside it is a heading;
- a heading is `#` to `######` and a space, at column 0, outside fenced
  blocks; a section ends at the next heading of equal or higher level, or
  at the end of the member;
- the section digest is over the exact bytes of that extent in the owning
  member. The frame carries those bytes with only their relative link
  destinations rebased.

Link rebasing. A relative destination in an excerpt is relative to the
owning member's directory; in the frame it must resolve from
standards/frames/ to the same target. `rebase` prefixes each relative
destination with the path from the frames directory to the owner's
directory (`X.md#a` becomes `../X.md#a`), and rewrites an in-member
fragment against the owning member (`#a` in FOUNDATIONS.md becomes
`../FOUNDATIONS.md#a`). A destination with a scheme (`stdo://`, `https:`,
`mailto:`) or starting with `/` is unchanged. Fenced code and inline code
spans are unchanged. Inline links, images and link reference definitions
are rebased. Not rebased: HTML attributes such as `href`, and indented code
blocks, which this rule does not recognise; a four-space-indented line is
read as text, as in a list continuation. The rewrite is a deterministic
function of the extent and the owner path, so `--check` compares against
the same rebased bytes. Adapted from Codex `relocate`
(qualification/C3/refresh_views.py:20-26, called at :59, at 31f28f9). Codex
refuses an in-member fragment and does not skip code; here the fragment is
rewritten against the owner coordinate and code is skipped.

Row selection (I4-06, tradeoff TO1). A route may carry
`"rows": {"mode": "frame-anchors"}`. Its excerpt then keeps prose, headings,
blank and fenced lines, every table header and separator, every row of a
table whose header has no `Consequence` column, and, in a family table,
only the rows whose link destinations (`#anchor` or `MEMBER.md#anchor`)
name an anchor that another route of the same frame carries in that
member. Such an excerpt is not a byte copy of its section: its `Source:`
line says `rows=k/n`, the manifest records `selected`, `total` and the
excerpt digest beside the section digest, and the omitted rows stay in
the owning member. `select_rows` below is the one implementation and has
a test.

Bindings (I5, E2E-01). A frame may carry `"binds"`: a list of items, each
with `text` and optionally an `owner` and `anchor`. The header renders them
under `Binds:`; an item that names an owner section is rendered with the
member's SHA-256 and recorded in the manifest with `owner_sha256` and
`section_sha256`, like a route, but the section is not copied. A bind names
an obligation the activation of the frame binds (the construction relation
of ACTIVATION §1; the assurance relations of FOUNDATIONS §4) and owns no
determination. `--check` reports, for each frame that would change, whether
an owning or bound section changed (`section-drift`) or only a member's
digest changed while every carried section is byte-identical
(`owner-drift-only`); the exit status is 1 in both cases.

Refusal, never truncation: on any refusal no file is written, the refusal is
printed as `refusal: <member>:<line>: <reason>` and the exit status is 2.

Usage:
  generate_frames.py [--root DIR] [--inputs PATH]      write frames and manifest
  generate_frames.py --check [--root DIR] [--inputs PATH]
                                                       exit 1 if any file would change
  generate_frames.py --list MEMBER [--root DIR]        print anchors, lines, bytes
"""
import argparse
import hashlib
import json
from pathlib import Path
import posixpath
import re
import sys
import unicodedata

TENANT_ROOT = Path(__file__).resolve().parents[2]
INPUTS_RELATIVE = Path('standards') / 'frames' / 'FRAME_INPUTS.json'
FRAMES_RELATIVE = Path('standards') / 'frames'
MAX_FRAME_BYTES = 160_000
FRAME_ID = re.compile(r'^[a-z0-9][a-z0-9-]*$')

# Ported verbatim from Codex qualification/C3/refresh_views.py:12-18 at 31f28f9.
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def slug(v):
    v = re.sub(r'<[^>]*>', '', v).replace('`', '').lower()
    v = unicodedata.normalize('NFC', v)
    return re.sub(r'\s', '-', re.sub(r'[^\w\-\s]', '', v))
# End of the verbatim port.


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


HEADING = re.compile(r'^(#{1,6}) (.+)$')
FENCE_OPEN = re.compile(r'^( {0,3})(`{3,}|~{3,})')
FENCE_LIKE = re.compile(r'^([ \t]*)(`{3,}|~{3,})')
SETEXT_UNDERLINE = re.compile(r'^ {0,3}(=+|-+)[ \t]*$')


class Refusal(Exception):
    """A refusal names the member and, where one exists, the line."""

    def __init__(self, member, line, reason):
        super().__init__(member, line, reason)
        self.member = member
        self.line = line
        self.reason = reason

    def __str__(self):
        where = f'{self.member}:{self.line}' if self.line else f'{self.member}'
        return f'refusal: {where}: {self.reason}'


def split_lines(data: bytes):
    """Lines with their terminators kept; joining them gives `data` back."""
    parts = data.split(b'\n')
    lines = [p + b'\n' for p in parts[:-1]]
    if parts[-1]:
        lines.append(parts[-1])
    return lines


def bare(line: bytes) -> str:
    text = line.decode('utf-8')
    if text.endswith('\n'):
        text = text[:-1]
    if text.endswith('\r'):
        text = text[:-1]
    return text


class Member:
    """One member read once as bytes, with its structure under the section rule."""

    def __init__(self, name: str, data: bytes):
        self.name = name
        self.data = data
        self.sha256 = digest(data)
        try:
            data.decode('utf-8')
        except UnicodeDecodeError as exc:
            line = data[:exc.start].count(b'\n') + 1
            raise Refusal(name, line, 'not valid UTF-8')
        self.lines = split_lines(data)
        # fenced[i] is True when line i is a fence delimiter or inside a fenced block.
        self.fenced = [False] * len(self.lines)
        # open_after[i] is the fence (char, length, opening line) still open after line i.
        self.open_after = [None] * len(self.lines)
        self.headings = []   # (index, level, title, anchor) outside fenced blocks
        self.fenced_headings = []   # (index, level, title, anchor) inside fenced blocks
        self.open_at_end = None
        self._scan()

    def _scan(self):
        fence = None
        previous_is_text = False
        for i, raw in enumerate(self.lines):
            line = bare(raw)
            like = FENCE_LIKE.match(line)
            if like and ('\t' in like[1] or len(like[1]) >= 4):
                raise Refusal(self.name, i + 1,
                              'fence-like line indented by four or more spaces '
                              '(or by a tab); its reading depends on context the rule does not decide')
            if fence is not None:
                self.fenced[i] = True
                char, length, _ = fence
                close = re.match(r'^ {0,3}(' + re.escape(char) + r'{' + str(length) + r',})[ \t]*$', line)
                heading = HEADING.match(line)
                if heading:
                    self.fenced_headings.append((i, len(heading[1]), heading[2], slug(heading[2])))
                if close:
                    fence = None
                self.open_after[i] = fence
                previous_is_text = False
                continue
            opened = FENCE_OPEN.match(line)
            if opened:
                fence = (opened[2][0], len(opened[2]), i + 1)
                self.fenced[i] = True
                self.open_after[i] = fence
                previous_is_text = False
                continue
            if previous_is_text and SETEXT_UNDERLINE.match(line):
                raise Refusal(self.name, i + 1,
                              'a line of only "=" or "-" stands directly under a text line '
                              'outside a fenced block; it may be a setext heading underline')
            heading = HEADING.match(line)
            if heading:
                self.headings.append((i, len(heading[1]), heading[2], slug(heading[2])))
                previous_is_text = False
                continue
            previous_is_text = line.strip() != ''
        self.open_at_end = fence

    def section(self, anchor: str):
        """Return (start index, end index, extent bytes) for the one heading with `anchor`."""
        matches = [h for h in self.headings if h[3] == anchor]
        if not matches:
            inside = [h for h in self.fenced_headings if h[3] == anchor]
            if inside:
                raise Refusal(self.name, inside[0][0] + 1,
                              f'anchor "{anchor}" matches only a heading inside a fenced block')
            raise Refusal(self.name, None, f'anchor "{anchor}" matches no heading outside fenced blocks')
        if len(matches) > 1:
            lines = ', '.join(str(h[0] + 1) for h in matches)
            raise Refusal(self.name, matches[0][0] + 1,
                          f'anchor "{anchor}" matches {len(matches)} headings outside fenced blocks (lines {lines})')
        start, level, _, _ = matches[0]
        end = len(self.lines)
        for index, other_level, _, _ in self.headings:
            if index > start and other_level <= level:
                end = index
                break
        return self.extent(start, end)

    def extent(self, start: int, end: int):
        """Bound check of one extent: it must not end inside an open fenced block."""
        if end > start and self.open_after[end - 1] is not None:
            opened_at = self.open_after[end - 1][2]
            raise Refusal(self.name, end,
                          f'section starting at line {start + 1} would end inside the fenced block '
                          f'opened at line {opened_at}')
        if self.open_at_end is not None:
            raise Refusal(self.name, self.open_at_end[2],
                          'fenced block opened here is still open at the end of the member')
        return start, end, b''.join(self.lines[start:end])


def load_member(root: Path, owner: str) -> Member:
    path = (root / owner)
    standards = (root / 'standards').resolve()
    resolved = path.resolve()
    if standards not in resolved.parents:
        raise Refusal(owner, None, 'owner is not a member under standards/')
    if not path.is_file():
        raise Refusal(owner, None, 'owner member does not exist')
    return Member(owner, path.read_bytes())


SCHEME = re.compile(r'^[A-Za-z][A-Za-z0-9+.-]*:')
REFERENCE_DEFINITION = re.compile(r'^( {0,3}\[(?:[^\]\\\n]|\\.)+\]:[ \t]*)(<[^<>\n]*>|\S+)')
BLOCK_START = re.compile(r'^ {0,3}(\||[-*+](?: |$)|\d{1,9}[.)](?: |$))')


def rebase_destination(destination: str, owner: str) -> str:
    """One link destination, rebased from the owner's directory to the frames directory."""
    angle = destination.startswith('<') and destination.endswith('>')
    target = destination[1:-1] if angle else destination
    if not target or SCHEME.match(target) or target.startswith('/'):
        return destination
    if target.startswith(('#', '?')):
        target = posixpath.basename(owner) + target
    prefix = posixpath.relpath(posixpath.dirname(posixpath.normpath(owner)), FRAMES_RELATIVE.as_posix())
    target = f'{prefix}/{target}'
    return f'<{target}>' if angle else target


def _code_spans(text: str):
    """[start, end) of each inline code span: a backtick string closed by one of equal length."""
    spans, i, n = [], 0, len(text)
    while i < n:
        if text[i] == '\\':
            i += 2
            continue
        if text[i] != '`':
            i += 1
            continue
        j = i
        while j < n and text[j] == '`':
            j += 1
        k, close = j, None
        while k < n:
            if text[k] != '`':
                k += 1
                continue
            m = k
            while m < n and text[m] == '`':
                m += 1
            if m - k == j - i:
                close = m
                break
            k = m
        if close is None:
            i = j
        else:
            spans.append((i, close))
            i = close
    return spans


def _skip_space(text: str, i: int) -> int:
    while i < len(text) and text[i] in ' \t\n':
        i += 1
    return i


def _destination(text: str, i: int):
    """(start, end) of the destination of an inline link whose `(` is at i - 1, or None if no link."""
    n = len(text)
    start = i = _skip_space(text, i)
    if i < n and text[i] == '<':
        j = i + 1
        while j < n and text[j] not in '<>\n':
            j += 2 if text[j] == '\\' else 1
        if j >= n or text[j] != '>':
            return None
        end = j + 1
    else:
        depth, j = 0, i
        while j < n:
            ch = text[j]
            if ch == '\\' and j + 1 < n:
                j += 2
                continue
            if ch in ' \t\n' or ord(ch) < 0x20:
                break
            if ch == '(':
                depth += 1
            elif ch == ')':
                if depth == 0:
                    break
                depth -= 1
            j += 1
        if depth:
            return None
        end = j
    k = _skip_space(text, end)
    if k > end and k < n and text[k] in '"\'(':
        closer = ')' if text[k] == '(' else text[k]
        m = k + 1
        while m < n and text[m] != closer:
            m += 2 if text[m] == '\\' else 1
        if m >= n:
            return None
        k = _skip_space(text, m + 1)
    if k >= n or text[k] != ')' or end == start:
        return None
    return start, end


def _rebase_inline(text: str, owner: str) -> str:
    """Rebase the destination of every inline link and image in one block of text."""
    code = _code_spans(text)
    out, last, openers, i, c = [], 0, 0, 0, 0
    while i < len(text):
        while c < len(code) and code[c][1] <= i:
            c += 1
        if c < len(code) and code[c][0] <= i:
            i = code[c][1]
            continue
        ch = text[i]
        if ch == '\\':
            i += 2
            continue
        if ch == '[':
            openers += 1
        elif ch == ']' and openers:
            openers -= 1
            if text.startswith('(', i + 1):
                found = _destination(text, i + 2)
                if found:
                    start, end = found
                    out.append(text[last:start])
                    out.append(rebase_destination(text[start:end], owner))
                    last = end
                    i = end
                    continue
        i += 1
    out.append(text[last:])
    return ''.join(out)


def _rebase_block(lines, owner: str) -> str:
    """One block of consecutive text lines: leading reference definitions, then inline links."""
    head = []
    for index, line in enumerate(lines):
        definition = REFERENCE_DEFINITION.match(line)
        if not definition:
            break
        head.append(line[:definition.start(2)] + rebase_destination(definition[2], owner)
                    + line[definition.end(2):])
    else:
        index = len(lines)
    return ''.join(head) + _rebase_inline(''.join(lines[index:]), owner)


def rebase(member: Member, start: int, end: int) -> bytes:
    """The extent of lines [start, end) of `member` with its relative link destinations rebased."""
    return rebase_lines(member, range(start, end))


LINK_DESTINATION = re.compile(r'\]\(([^)\s]+)\)')


def select_rows(member: Member, start: int, end: int, owner: str, anchors_by_owner: dict):
    """Line indices of the extent [start, end) keeping, in every table whose header has a
    `Consequence` column, only the rows that link to a section this frame carries.

    Prose, headings, blank and fenced lines, table headers and separators, and every row of
    a table that is not a family table are kept. A family-table row is kept when one of its
    link destinations is `#anchor` (this member) or `MEMBER.md#anchor` and that anchor is a
    route of this frame in that member. Returns (indices, family rows total, rows kept)."""
    indices, total, kept = [], 0, 0
    state = None  # None: outside a table; 'header', 'separator', then ('family', bool)
    for i in range(start, end):
        raw = bare(member.lines[i]).lstrip(' ')
        is_row = (not member.fenced[i]) and raw.startswith('|')
        if not is_row:
            state = None
            indices.append(i)
            continue
        text = member.lines[i].decode('utf-8')
        if state is None:
            state = ('header', 'Consequence' in text)
            indices.append(i)
            continue
        if state[0] == 'header':
            state = ('rows', state[1])
            indices.append(i)
            continue
        if not state[1]:
            indices.append(i)
            continue
        total += 1
        keep = False
        for destination in LINK_DESTINATION.findall(re.sub(r'`[^`]*`', '', text)):
            path, _, anchor = destination.partition('#')
            if not anchor or path.startswith(('http', 'stdo:', '/', 'mailto:')):
                continue
            target = Path(owner).name if path == '' else Path(path).name
            if anchor in anchors_by_owner.get(target, set()):
                keep = True
                break
        if keep:
            indices.append(i)
            kept += 1
    return indices, total, kept


def rebase_lines(member: Member, indices) -> bytes:
    """The given lines of `member`, in order, with their relative link destinations rebased.

    Fenced lines and blank lines are copied unchanged. The other lines are
    grouped into blocks, which end at a blank or fenced line; a heading, a
    table row and a list item marker start a new block, and a heading or a
    table row is a block of its own. An inline code span never crosses a
    block, and nothing inside one is rewritten.
    """
    pieces, block = [], []

    def flush():
        if block:
            pieces.append(_rebase_block(block, member.name))
            block.clear()

    heading_lines = {h[0] for h in member.headings}
    for i in indices:
        text = member.lines[i].decode('utf-8')
        if member.fenced[i] or bare(member.lines[i]).strip() == '':
            flush()
            pieces.append(text)
            continue
        single = i in heading_lines or bare(member.lines[i]).lstrip(' ').startswith('|')
        if single or BLOCK_START.match(text):
            flush()
        block.append(text)
        if single:
            flush()
    flush()
    return ''.join(pieces).encode('utf-8')


def source_line(owner: str, anchor: str, owner_sha256: str, note: str = '') -> bytes:
    return f'Source: {Path(owner).name}#{anchor} sha256={owner_sha256}{note}'.encode('utf-8')


def binds_block(frame: dict) -> str:
    binds = frame.get('binds') or []
    if not binds:
        return ''
    lines = ['Binds:', '']
    for b in binds:
        line = f'- {b["text"]}'
        if b.get('owner'):
            line += f' ({Path(b["owner"]).name}#{b["anchor"]} sha256={b["owner_sha256"]})'
        lines.append(line)
    lines += ['', 'A `Binds:` item names an obligation the activation of this frame binds, with',
              'the owning section and the digest of its member where it names one; the item',
              'copies no section and owns no determination. A changed owner changes the digest.', '']
    return '\n'.join(lines) + '\n'


def header(frame: dict, size: int) -> bytes:
    routes = '\n'.join(
        f'{n}. [{Path(r["owner"]).name}#{r["anchor"]}](../{Path(r["owner"]).name}#{r["anchor"]})'
        for n, r in enumerate(frame['routes'], 1))
    text = (
        f'# Reference frame {frame["id"]}\n'
        '\n'
        f'Task: {frame["task"]}\n'
        '\n'
        f'Purpose: {frame["scope"]}\n'
        '\n'
        + binds_block(frame) +
        'Each excerpt below copies one owning section of a member of this method\n'
        'byte for byte, except a `rows=k/n` excerpt (see below) and except that\n'
        'each relative link destination is rebased\n'
        'to resolve from this directory to the same target. Fenced code, inline\n'
        'code and absolute and `stdo://` links are unchanged. The `Source:` line\n'
        "before an excerpt names the member and the section's anchor, and gives\n"
        'the SHA-256 of the whole owning member. The section digest recorded in\n'
        "FRAME_INPUTS.json is over the owner's bytes, not over this copy. The\n"
        'owning section decides; this frame owns no determination. An excerpt\n'
        'whose `Source:` line says `rows=k/n` is a family table of which only\n'
        'the k rows that cite a section this frame carries are copied, with the\n'
        "table's preamble, header and every non-family table; the other rows\n"
        "stay in the owning member and are not copied. The frame's\n"
        'qualification, not this selection, decides whether the frame is\n'
        'sufficient for its task.\n'
        '\n'
        'Routes, in order:\n'
        '\n'
        f'{routes}\n'
        '\n'
        f'Size of this frame: {size} bytes.\n'
    )
    return text.encode('utf-8')


def render(frame: dict, blocks) -> bytes:
    body = b''
    for line, extent in blocks:
        body += b'\n' + line + b'\n\n' + extent
        if not extent.endswith(b'\n'):
            body += b'\n'
    size = 0
    for _ in range(10):
        data = header(frame, size) + body
        if len(data) == size:
            return data
        size = len(data)
    raise RuntimeError('frame size did not reach a fixed point')


def build(root: Path, inputs_path: Path):
    """Return {path: bytes} for every frame and the manifest, or raise Refusal."""
    try:
        index = json.loads(inputs_path.read_bytes().decode('utf-8'))
    except (OSError, ValueError) as exc:
        raise Refusal(str(inputs_path), None, f'frame inputs unreadable: {exc}')
    members = {}
    outputs = {}
    seen_ids = set()
    frames_out = []
    for frame in index.get('frames', []):
        fid = frame.get('id', '')
        if not FRAME_ID.match(fid) or fid in seen_ids:
            raise Refusal(str(inputs_path), None, f'frame id "{fid}" is malformed or repeated')
        seen_ids.add(fid)
        if not frame.get('routes'):
            raise Refusal(str(inputs_path), None, f'frame "{fid}" has no routes')
        blocks = []
        routes_out = []
        spans = {}
        anchors_by_owner = {}
        for route in frame['routes']:
            if not (route.get('rows') or {}).get('mode'):
                anchors_by_owner.setdefault(Path(route['owner']).name, set()).add(route['anchor'])
        for route in frame['routes']:
            owner, anchor = route['owner'], route['anchor']
            if owner not in members:
                members[owner] = load_member(root, owner)
            member = members[owner]
            start, end, extent = member.section(anchor)
            for other_start, other_end, other_anchor in spans.get(owner, []):
                if start < other_end and other_start < end:
                    raise Refusal(owner, start + 1,
                                  f'frame "{fid}": route "{anchor}" overlaps route "{other_anchor}"')
            spans.setdefault(owner, []).append((start, end, anchor))
            mode = (route.get('rows') or {}).get('mode')
            if mode == 'frame-anchors':
                indices, total, kept = select_rows(member, start, end, owner, anchors_by_owner)
                block = rebase_lines(member, indices)
                note = f' rows={kept}/{total} selected by the anchors this frame carries'
            elif mode:
                raise Refusal(str(inputs_path), None, f'frame "{fid}": unknown rows mode "{mode}"')
            else:
                block, note, total, kept = rebase(member, start, end), '', None, None
            blocks.append((source_line(owner, anchor, member.sha256, note), block))
            entry = {
                'owner': owner,
                'owner_sha256': member.sha256,
                'anchor': anchor,
                'section_sha256': digest(extent),
            }
            if mode:
                entry['rows'] = {'mode': mode, 'selected': kept, 'total': total, 'excerpt_sha256': digest(block)}
            routes_out.append(entry)
        binds_out = None
        if 'binds' in frame:
            binds_in = frame['binds']
            if (not isinstance(binds_in, list) or not binds_in
                    or not all(isinstance(b, dict) and isinstance(b.get('text'), str) and b['text'].strip()
                               for b in binds_in)):
                raise Refusal(str(inputs_path), None, f'frame "{fid}": binds must be a non-empty list of items with text')
            binds_out = []
            for b in binds_in:
                item = {'text': b['text']}
                if b.get('owner') or b.get('anchor'):
                    owner, anchor = b.get('owner'), b.get('anchor')
                    if not owner or not anchor:
                        raise Refusal(str(inputs_path), None, f'frame "{fid}": a bind names both owner and anchor or neither')
                    if owner not in members:
                        members[owner] = load_member(root, owner)
                    member = members[owner]
                    _, _, extent = member.section(anchor)
                    item.update({'owner': owner, 'owner_sha256': member.sha256,
                                 'anchor': anchor, 'section_sha256': digest(extent)})
                binds_out.append(item)
        record = {
            'id': fid,
            'path': str(FRAMES_RELATIVE / f'{fid}.md'),
            'task': frame['task'],
            'scope': frame['scope'],
            'routes': routes_out,
        }
        if binds_out is not None:
            record['binds'] = binds_out
        data = render(record, blocks)
        if len(data) > MAX_FRAME_BYTES:
            raise Refusal(record['path'], None,
                          f'frame would be {len(data)} bytes, over the limit of {MAX_FRAME_BYTES}; '
                          'no excerpt is truncated')
        outputs[root / record['path']] = data
        entry_out = {
            'id': fid,
            'path': record['path'],
            'task': record['task'],
            'bytes': len(data),
            'sha256': digest(data),
            'scope': record['scope'],
        }
        if binds_out is not None:
            entry_out['binds'] = binds_out
        entry_out['routes'] = routes_out
        frames_out.append(entry_out)
    manifest = {
        'kind': index.get('kind'),
        'limits': index.get('limits', []),
        'frames': frames_out,
    }
    outputs[inputs_path] = (json.dumps(manifest, indent=2) + '\n').encode('utf-8')
    return outputs


def report_section_drift(root: Path, inputs_path: Path, outputs: dict):
    """For each frame that would change, say whether a carried section changed or only a member digest."""
    try:
        before = json.loads(inputs_path.read_bytes().decode('utf-8'))
        after = json.loads(outputs[inputs_path].decode('utf-8'))
    except (OSError, ValueError, KeyError):
        return
    old = {f.get('id'): f for f in before.get('frames', [])}
    for frame in after.get('frames', []):
        prior = old.get(frame['id'])
        if not prior or frame.get('sha256') == prior.get('sha256'):
            continue
        old_routes = {(r['owner'], r['anchor']): r.get('section_sha256') for r in prior.get('routes', [])}
        old_binds = {(b.get('owner'), b.get('anchor')): b.get('section_sha256') for b in prior.get('binds') or []}
        changed = [f'{Path(r["owner"]).name}#{r["anchor"]}' for r in frame['routes']
                   if old_routes.get((r['owner'], r['anchor'])) != r.get('section_sha256')]
        changed += [f'bind {Path(b["owner"]).name}#{b["anchor"]}' for b in frame.get('binds') or [] if b.get('owner')
                    if old_binds.get((b['owner'], b['anchor'])) != b.get('section_sha256')]
        if changed:
            for c in changed:
                print(f'section-drift: {frame["id"]} {c}')
        else:
            print(f'owner-drift-only: {frame["id"]}')


def list_member(root: Path, owner: str):
    member = load_member(root, owner)
    print(f'{owner} sha256={member.sha256} bytes={len(member.data)}')
    for index, level, _, anchor in member.headings:
        try:
            size = str(len(member.section(anchor)[2]))
        except Refusal as refusal:
            size = f'refused: {refusal.reason}'
        print(f'{index + 1:>6} {"#" * level:<6} {size:>7}  {anchor}')


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--root', type=Path, default=TENANT_ROOT)
    ap.add_argument('--inputs', type=Path)
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument('--check', action='store_true')
    mode.add_argument('--list', metavar='MEMBER')
    args = ap.parse_args(argv)
    root = args.root.resolve()
    inputs_path = (args.inputs or root / INPUTS_RELATIVE).resolve()
    try:
        if args.list:
            list_member(root, args.list)
            return 0
        outputs = build(root, inputs_path)
    except Refusal as refusal:
        print(str(refusal), file=sys.stderr)
        return 2
    if args.check:
        drift = [p for p, data in outputs.items()
                 if not p.is_file() or sha(p) != digest(data)]
        for p in drift:
            print(f'drift: {p.relative_to(root)}')
        if drift:
            report_section_drift(root, inputs_path, outputs)
        return 1 if drift else 0
    for path, data in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    for path, data in outputs.items():
        print(f'{path.relative_to(root)} {len(data)} bytes sha256={digest(data)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
