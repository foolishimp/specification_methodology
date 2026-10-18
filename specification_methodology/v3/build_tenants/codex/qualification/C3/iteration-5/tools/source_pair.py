"""Show one exact owning source body beside its authored semantic record.

X6 is an on-demand review view. It does not embed every source body in each
runtime value, change native acquisition dependencies or judge fidelity.
"""
import argparse
import json
from context import PACKAGE, library, read, sha


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', required=True)
    args = parser.parse_args()
    inventory = read(PACKAGE/'interpretation/SOURCE_INVENTORY.json')
    pins = {v['path']:v['sha256'] for v in inventory['document_members']}
    raw_account = (PACKAGE/'interpretation/source-account.json').read_bytes()
    if sha(raw_account) != inventory['interpretation']['semantic_account_sha256']:
        raise ValueError('Semantic account differs from its inventory')
    rows = {r['id']:r for r in json.loads(raw_account)['determinations']}
    row = rows[args.id]
    source = (PACKAGE/row['owner']['path']).read_bytes()
    if sha(source) != pins[row['owner']['path']]:
        raise ValueError('Source differs from documentary freeze')
    owner = row['owner']
    if owner.get('unit_scope') == 'whole_member':
        body = source
    else:
        body = b''.join(source.splitlines(keepends=True)[owner['start_line']-1:owner['end_line']])
    if sha(body) != owner['body_sha256']:
        raise ValueError('Owned body differs')
    print(json.dumps({'source_commit':inventory['document_source_input_commit'],
        'source_owner':owner, 'source_utf8':body.decode(), 'authored_semantics':row,
        'standing':'Exact paired review material; no fidelity or acceptance judgment.'},indent=2,ensure_ascii=False))


if __name__ == '__main__':
    main()
