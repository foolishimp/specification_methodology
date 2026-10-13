"""Refresh exact derivative routes and digests; does not confer semantic acceptance."""
import hashlib
import json
from pathlib import Path
import re
import unicodedata

base = Path(__file__).resolve().parents[2]
root = base / 'successor'
std = root / 'standards'

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def slug(v):
    v = re.sub(r'<[^>]*>', '', v).replace('`', '').lower()
    v = unicodedata.normalize('NFC', v)
    return re.sub(r'\s', '-', re.sub(r'[^\w\-\s]', '', v))

def relocate(match):
    value = match[2]
    if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', value):
        return match[0]
    if value.startswith('#'):
        raise ValueError('Local fragment needs an owning member coordinate')
    return match[1] + '../' + value + match[3]

def refresh():
    for path in (std / 'authority_compressions').glob('*.md'):
        text = path.read_text()
        if not text.startswith('---\n'):
            continue
        front, body = text[4:].split('---', 1)
        single = re.search(r'^source_ref: (.+)$', front, re.M)
        if single:
            front = re.sub(r'^source_digest: [0-9a-f]{64}$',
                           'source_digest: ' + sha((path.parent / single[1]).resolve()), front, flags=re.M)
        for match in list(re.finditer(r'^  ([\w/.-]+): ([0-9a-f]{64})$', front, re.M)):
            owner = std / match[1]
            if not owner.is_file():
                raise ValueError('Absent compression owner: ' + str(owner))
            front = front.replace(match[0], '  ' + match[1] + ': ' + sha(owner))
        path.write_text('---\n' + front + '---' + body)

    index_path = Path(__file__).with_name('FRAME_INPUTS.json')
    index = json.loads(index_path.read_text())
    for frame in index['frames']:
        target = root / frame['path']
        parts = [target.read_text().split('\nSource:', 1)[0].rstrip()]
        for entry in frame['routes']:
            owner = root / entry['owner']
            text = owner.read_text()
            headings = list(re.finditer(r'^(#{2,6}) (.+)$', text, re.M))
            matches = [(i, h) for i, h in enumerate(headings) if slug(h[2]) == entry['anchor']]
            if len(matches) != 1:
                raise ValueError('Ambiguous or absent selected heading: ' + entry['anchor'])
            i, h = matches[0]
            end = next((n.start() for n in headings[i + 1:] if len(n[1]) <= len(h[1])), len(text))
            raw = text[h.start():end].rstrip() + '\n'
            rendered = re.sub(r'(\[[^\]]*\]\()([^\n]+?)(\))', relocate, raw)
            parts.append(f"\nSource: [{owner.name} — {h[2]}](../{str(Path(entry['owner']).relative_to('standards'))}#{entry['anchor']}); "
                         f"SHA256 `{sha(owner)}`.\n\n" + rendered)
            entry['owner_sha256'] = sha(owner)
            entry['section_sha256'] = hashlib.sha256(raw.encode()).hexdigest()
        target.write_text('\n'.join(parts).rstrip() + '\n')
        frame['sha256'] = sha(target)
        frame['bytes'] = target.stat().st_size
    for view in index.get('source_linked_summaries', []):
        target = root / view['path']
        links = []
        for entry in view['routes']:
            owner = root / entry['owner']
            entry['owner_sha256'] = sha(owner)
            location = str(Path(entry['owner']).relative_to('standards'))
            links.append(f"- [{owner.name} — {entry['anchor']}](../{location}#{entry['anchor']}); member SHA256 `{sha(owner)}`.")
        text = re.sub(r'<!-- SOURCE_PINS_START -->.*?<!-- SOURCE_PINS_END -->',
                      '<!-- SOURCE_PINS_START -->\n'+'\n'.join(links)+'\n<!-- SOURCE_PINS_END -->',
                      target.read_text(), flags=re.S)
        target.write_text(text)
        view['sha256'] = sha(target)
        view['bytes'] = target.stat().st_size
    index_path.write_text(json.dumps(index, indent=2) + '\n')
    print('Compression pins and %d excerpt views refreshed; no semantic verdict inferred.' % len(index['frames']))


if __name__ == '__main__':
    refresh()
