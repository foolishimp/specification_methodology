"""Executive-selected lossless recovery proposal; never records Product carriers."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ORIGINAL_SHA = '0500a0df9c1b98728a4770fb28c11d10f643101be050a941758f5614b63e0e71'
PREFIX = b'All admitted inputs are read. Expectations derived from source and requirements, then compared against the candidate export. Returning the specified JSON.\n\n```json\n'


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def pairs(items):
    result = {}
    for key, value in items:
        if key in result:
            raise ValueError('duplicate JSON key')
        result[key] = value
    return result


def decode(raw):
    if not raw.startswith(PREFIX) or not raw.endswith(b'\n```') or raw.count(b'```') != 2:
        raise ValueError('not exactly the observed inert prefix and one final JSON fence')
    start, end = len(PREFIX), len(raw) - 3
    body = raw[start:end]
    value = json.loads(body.decode('utf-8'), object_pairs_hook=pairs)
    if not isinstance(value, dict) or set(value) != {'review_markdown', 'bug_report_markdown'}:
        raise ValueError('original return schema mismatch')
    if not isinstance(value['review_markdown'], str) or not value['review_markdown']:
        raise ValueError('empty or non-string review')
    if value['bug_report_markdown'] is not None and not isinstance(value['bug_report_markdown'], str):
        raise ValueError('invalid report field')
    return start, end, body, value


def main():
    original = HERE / 'runs/R1/FINAL.txt'
    raw = original.read_bytes()
    assert digest(raw) == ORIGINAL_SHA
    start, end, body, value = decode(raw)
    negative = []
    for label, bad in [('second-fence', raw + b'\n```json\n{}\n```'), ('changed-prefix', b'x' + raw), ('duplicate-key', PREFIX + b'{"review_markdown":"a","review_markdown":"b","bug_report_markdown":null}\n```'), ('malformed-object', PREFIX + b'{bad}\n```')]:
        try:
            decode(bad)
        except (ValueError, UnicodeError):
            negative.append({'case': label, 'refused': True})
        else:
            raise AssertionError(label)
    out = HERE / 'recovery/R1'
    assert not out.exists()
    out.mkdir(parents=True)
    (out / 'OBJECT.json').write_bytes(body)
    fields = {}
    for key, text in value.items():
        if text is not None:
            data = text.encode('utf-8')
            (out / (key + '.txt')).write_bytes(data)
            fields[key] = {'path': key + '.txt', 'bytes': len(data), 'sha256': digest(data)}
        else:
            fields[key] = None
    original_measure = HERE / 'runs/R1/MEASUREMENT.json'
    assert json.loads(original_measure.read_text())['transport_recorded'] is False
    proposal = {'standing': 'separate recovery proposal pending independent verification before named recording or E1; original R1 transport remains failed', 'authority': 'Executive explicitly selected lossless single-fence recovery of retained R1 only', 'original': {'path': str(original), 'bytes': len(raw), 'sha256': digest(raw), 'measurement': str(original_measure), 'measurement_sha256': digest(original_measure.read_bytes())}, 'selected_span': {'start_inclusive': start, 'end_exclusive': end, 'bytes': len(body), 'sha256': digest(body), 'trailing_newline_retained': True}, 'fields': fields, 'decoder_sha256': digest(Path(__file__).read_bytes()), 'negative_checks': negative, 'limitations': 'No wording, uncertainty, family-independence or qualification is repaired. This does not prove original raw-JSON compliance. No model invocation or Product carrier is written by this proposal.'}
    (out / 'PROPOSAL.json').write_text(json.dumps(proposal, indent=2) + '\n')
    print(json.dumps(proposal, indent=2))


if __name__ == '__main__':
    main()
