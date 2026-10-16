"""Authored I5 patch coordinates. Helpers pin source; they infer no meaning.

Protocol stdo.i5.authored-account-patch/v1: common_input, source_preimage,
producer, owner_paths, updates, new_rows. Each update names id, exact immediate
preimage_body_sha256/candidate_body_sha256 and replacement semantic_fields.
new_rows contains complete authored determinations with exact owner body pins.
Use existing account vocabulary; any new semantic field requires a declared
compiler change. No deletion or implicit source replacement is supported.
"""
import re
import unicodedata
from context import PACKAGE, sha

PROTOCOL = 'stdo.i5.authored-account-patch/v1'


def slug(value):
    value = unicodedata.normalize('NFC', re.sub(r'<[^>]*>', '', value).replace('`', '').lower())
    return re.sub(r'\s', '-', re.sub(r'[^\w\-\s]', '', value))


def heading_units(raw):
    """Exact immediate sections, including the heading and terminal whitespace."""
    lines = raw.splitlines(keepends=True)
    found, counts, offset, fence = [], {}, 0, None
    for number, line in enumerate(lines, 1):
        value = line.decode('utf-8')
        marker = re.match(r'^\s{0,3}(`{3,}|~{3,})', value)
        if marker:
            mark = marker[1]
            if fence is None:
                fence = (mark[0], len(mark))
            elif fence[0] == mark[0] and len(mark) >= fence[1]:
                fence = None
        elif fence is None:
            match = re.match(r'^(#{1,6})\s+(.+?)\s*#*\s*$', value)
            if match:
                stem = slug(match[2]); n = counts.get(stem, 0); counts[stem] = n + 1
                found.append({'anchor': stem + ('-' + str(n) if n else ''), 'start_line': number,
                              'byte_start': offset, 'level': len(match[1]), 'heading': match[2]})
        offset += len(line)
    for index, item in enumerate(found):
        following = found[index + 1] if index + 1 < len(found) else None
        item['byte_end'] = following['byte_start'] if following else len(raw)
        item['end_line'] = following['start_line'] - 1 if following else len(lines)
        item['body'] = raw[item['byte_start']:item['byte_end']]
    return {item['anchor']: item for item in found}


def source_path(path):
    from pathlib import Path
    relative = Path(path)
    if relative.is_absolute() or '..' in relative.parts or str(relative).startswith('interpretation/'):
        raise ValueError('Expected a documentary package path')
    return relative


def source_unit(path, anchor, raw=None):
    path = source_path(path)
    raw = (PACKAGE / path).read_bytes() if raw is None else raw
    try:
        return heading_units(raw)[anchor]
    except KeyError as error:
        raise ValueError('Missing source heading: ' + str(path) + '#' + anchor) from error


def make_owner(path, anchor, raw=None):
    path = source_path(path)
    raw = (PACKAGE / path).read_bytes() if raw is None else raw
    unit = source_unit(path, anchor, raw)
    return {'path': str(path), 'anchor': anchor, 'start_line': unit['start_line'],
            'end_line': unit['end_line'], 'body_sha256': sha(unit['body'])}


def source_block(path, anchor, identifier='c1', raw=None):
    """Explicitly select a full immediate section as a block, without grading it."""
    unit = source_unit(path, anchor, raw)
    return {'id': identifier, 'byte_start': unit['byte_start'], 'byte_end': unit['byte_end'],
            'sha256': sha(unit['body'])}
