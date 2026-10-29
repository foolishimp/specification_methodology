"""Faithful reporting of saved gate results, without authentication."""
import hashlib
import json
import sys
from decimal import Decimal
from pathlib import Path


def unique(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError('duplicate object key')
        out[key] = value
    return out


def reject(value):
    raise ValueError('non-finite JSON number')


def encode(value):
    """Preserve decimal precision without conversion through binary floats."""
    if isinstance(value, Decimal):
        return str(value)
    if isinstance(value, dict):
        return '{' + ','.join(json.dumps(k) + ':' + encode(v) for k, v in value.items()) + '}'
    if isinstance(value, list):
        return '[' + ','.join(encode(v) for v in value) + ']'
    return json.dumps(value, allow_nan=False)


def report(raw):
    data = json.loads(raw.decode('utf-8'), object_pairs_hook=unique,
                      parse_float=Decimal, parse_constant=reject)
    if not isinstance(data, dict):
        raise ValueError('expected object root')
    if data.get('schema') != 'a_c.formal-gate.result/1':
        raise ValueError('unknown schema')
    status = data.get('status')
    if status not in ('verified', 'refused', 'unsupported', 'incomplete'):
        raise ValueError('unknown status')
    for key in ('reason', 'request_sha256'):
        if key in data and data[key] is not None and not isinstance(data[key], str):
            raise ValueError('invalid ' + key)
    for key in ('checked_claims', 'requested_claims', 'limits'):
        if key in data and (not isinstance(data[key], list) or
                            any(not isinstance(v, str) for v in data[key])):
            raise ValueError('invalid ' + key)
    for key in ('inputs', 'model', 'runtime_identity', 'evidence', 'observations', 'context_binding'):
        if key in data and data[key] is not None and not isinstance(data[key], dict):
            raise ValueError('invalid ' + key)
    if 'selections' in data and data['selections'] is not None and not isinstance(data['selections'], list):
        raise ValueError('invalid selections')
    categories = {'verified': 'verified_claims_reported', 'unsupported': 'unsupported_contract',
                  'incomplete': 'check_incomplete'}
    reasons = {
        'Insufficient record budget; verified refusal, no truncated projection': 'record_budget_refusal',
        'Supplied Graphify view differs from actual formal result/boundary mapping': 'supplied_view_mismatch',
        'signature: expected object': 'malformed_model',
    }
    category = categories.get(status, reasons.get(data.get('reason'), 'other_refusal'))
    elapsed = (data.get('observations') or {}).get('elapsed_seconds')
    state = 'unknown' if elapsed is None else 'invalid'
    if type(elapsed) in (int, Decimal) and elapsed >= 0:
        state = 'reported'
    return {
        'schema': 't013.gate-result-report/1',
        'source': {'raw_sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)},
        'reported': data,
        'summary': {'status': status, 'category': category,
                    'checked_claim_count': len(data['checked_claims']) if 'checked_claims' in data else None,
                    'requested_claim_count': len(data['requested_claims']) if 'requested_claims' in data else None},
        'cost': {'elapsed_seconds': {'state': state, 'value': elapsed if state == 'reported' else None},
                 'tokens': {'state': 'unknown', 'value': None},
                 'money_usd': {'state': 'unknown', 'value': None}},
        'standing': {'input_authenticated': False, 'grants_authority': False,
                     'establishes_semantic_acceptance': False},
    }


def main():
    if len(sys.argv) != 2:
        print('usage: gate_report.py FILE', file=sys.stderr)
        return 2
    try:
        output = encode(report(Path(sys.argv[1]).read_bytes()))
    except (OSError, ValueError, UnicodeError, RecursionError) as exc:
        print('gate_report: ' + str(exc), file=sys.stderr)
        return 2
    print(output)
    return 0


if __name__ == '__main__':
    sys.exit(main())
