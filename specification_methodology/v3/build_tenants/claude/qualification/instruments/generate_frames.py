#!/usr/bin/env python3
"""Generate verbatim reference frames from owning sections; confers no acceptance.

Reads the frame specifications in standards/frames/FRAME_INPUTS.json (frame
id, task, scope, ordered owner#anchor routes). For each route it extracts the
owning section byte for byte, prefixes it with a `Source:` line naming the
member, the anchor and the SHA-256 of the whole owning member, and writes
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
- the section digest is over the exact bytes of that extent, and the frame
  carries those same bytes.

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
import re
import sys
import unicodedata

TENANT_ROOT = Path(__file__).resolve().parents[2]
INPUTS_RELATIVE = Path('standards') / 'frames' / 'FRAME_INPUTS.json'
FRAMES_RELATIVE = Path('standards') / 'frames'
MAX_FRAME_BYTES = 100_000
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


def source_line(owner: str, anchor: str, owner_sha256: str) -> bytes:
    return f'Source: {Path(owner).name}#{anchor} sha256={owner_sha256}'.encode('utf-8')


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
        'Each excerpt below is a verbatim copy of one owning section of a member\n'
        'of this method. The `Source:` line before it names the member and the\n'
        "section's anchor, and gives the SHA-256 of the whole owning member. The\n"
        'owning section decides; this frame owns no determination. Links inside\n'
        "an excerpt are relative to the owning member's directory.\n"
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
            blocks.append((source_line(owner, anchor, member.sha256), extent))
            routes_out.append({
                'owner': owner,
                'owner_sha256': member.sha256,
                'anchor': anchor,
                'section_sha256': digest(extent),
            })
        record = {
            'id': fid,
            'path': str(FRAMES_RELATIVE / f'{fid}.md'),
            'task': frame['task'],
            'scope': frame['scope'],
            'routes': routes_out,
        }
        data = render(record, blocks)
        if len(data) > MAX_FRAME_BYTES:
            raise Refusal(record['path'], None,
                          f'frame would be {len(data)} bytes, over the limit of {MAX_FRAME_BYTES}; '
                          'no excerpt is truncated')
        outputs[root / record['path']] = data
        frames_out.append({
            'id': fid,
            'path': record['path'],
            'task': record['task'],
            'bytes': len(data),
            'sha256': digest(data),
            'scope': record['scope'],
            'routes': routes_out,
        })
    manifest = {
        'kind': index.get('kind'),
        'limits': index.get('limits', []),
        'frames': frames_out,
    }
    outputs[inputs_path] = (json.dumps(manifest, indent=2) + '\n').encode('utf-8')
    return outputs


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
        return 1 if drift else 0
    for path, data in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    for path, data in outputs.items():
        print(f'{path.relative_to(root)} {len(data)} bytes sha256={digest(data)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
