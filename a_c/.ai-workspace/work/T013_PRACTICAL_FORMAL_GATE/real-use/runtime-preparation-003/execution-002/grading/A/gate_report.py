"""Report saved gate labels and data without authenticating them."""
import hashlib
import json
import math
from pathlib import Path
import sys

SCHEMA = 'a_c.formal-gate.result/1'
CATEGORIES = {'verified': 'verified_claims_reported', 'unsupported': 'unsupported_contract',
              'incomplete': 'check_incomplete'}
REFUSALS = {
    'Insufficient record budget; verified refusal, no truncated projection': 'record_budget_refusal',
    'Supplied Graphify view differs from actual formal result/boundary mapping': 'supplied_view_mismatch',
    'signature: expected object': 'malformed_model',
}


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('duplicate object key')
        result[key] = value
    return result


def finite_float(value):
    number = float(value)
    if not math.isfinite(number):
        raise ValueError('non-finite JSON number')
    return number


def reject_constant(value):
    raise ValueError('non-finite JSON number')


def make_report(raw):
    data = json.loads(raw.decode('utf-8'), object_pairs_hook=unique_object,
                      parse_float=finite_float, parse_constant=reject_constant)
    if not isinstance(data, dict):
        raise ValueError('expected object root')
    if data.get('schema') != SCHEMA:
        raise ValueError('unknown schema')
    status = data.get('status')
    if not isinstance(status, str) or status not in (*CATEGORIES, 'refused'):
        raise ValueError('unknown status')
    shapes = {'reason': (str, type(None)), 'request_sha256': (str, type(None)),
              'selections': (list, type(None))}
    for key in ('inputs', 'model', 'runtime_identity', 'evidence', 'observations', 'context_binding'):
        shapes[key] = (dict, type(None))
    for key, types in shapes.items():
        if key in data and not isinstance(data[key], types):
            raise ValueError('wrong type for ' + key)
    for key in ('checked_claims', 'requested_claims', 'limits'):
        if key in data and (not isinstance(data[key], list) or
                            not all(isinstance(x, str) for x in data[key])):
            raise ValueError('expected string array for ' + key)
    elapsed = (data.get('observations') or {}).get('elapsed_seconds')
    state = 'unknown' if elapsed is None else 'invalid'
    if type(elapsed) in (int, float) and elapsed >= 0:
        state = 'reported'
    category = CATEGORIES.get(status, REFUSALS.get(data.get('reason'), 'other_refusal'))
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


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    try:
        if len(args) != 1:
            raise ValueError('usage: gate_report.py RESULT.json')
        output = json.dumps(make_report(Path(args[0]).read_bytes()), ensure_ascii=True, allow_nan=False)
    except (OSError, ValueError, RecursionError) as exc:
        print('gate_report: ' + str(exc), file=sys.stderr)
        return 2
    print(output)
    return 0


if __name__ == '__main__':
    sys.exit(main())
