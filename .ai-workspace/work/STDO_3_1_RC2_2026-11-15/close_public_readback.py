"""Read actual public-install evidence and close the release's publication conditions."""
from pathlib import Path
import datetime
import hashlib
import json
import subprocess

w = Path(__file__).resolve().parent


def read(path):
    return json.loads(path.read_text())


def api(endpoint):
    return json.loads(subprocess.check_output(['gh', 'api', endpoint]))


plan = read(w / 'REF_PLAN.json')
published = read(w / 'REF_PUBLISH.json')
assert published['exit'] == 0 and published['remote_readback_valid']
assert '--atomic' in published['argv'] and published['refs'] == 25
public = read(w / 'public-readback/RESULT.json')
assets = read(w / 'public-readback/ASSET_READBACK.json')
assert public['valid'] and assets['valid'] and public['assets'] == 6
assert public['product_members'] == 225 and '3.1.0rc2' in public['manager_version']
remote_raw = subprocess.check_output(['git', '-C', str(w.parents[2]), 'ls-remote', 'origin'], text=True)
remote = dict((line.split('\t')[1], line.split('\t')[0]) for line in remote_raw.splitlines())
for row in plan['refs']:
    assert remote[row['destination']] == row['object'], row['destination']
    if row['destination'].startswith('refs/tags/'):
        assert remote[row['destination'] + '^{}'] == row['commit']
assert all(remote[ref] == obj for ref, obj in plan['protected_predecessor_refs'].items())
before = read(w / 'RC1_PUBLIC_BEFORE.json')
old = api('repos/foolishimp/specification_methodology/releases/' + str(before['release_id']))
old_assets = [{'name': a['name'], 'id': a['id'], 'bytes': a['size'], 'digest': a['digest']} for a in old['assets']]
assert old_assets == before['assets'] and old['tag_name'] == before['tag']
assert old['draft'] == before['draft'] and old['prerelease'] == before['prerelease']
latest = api('repos/foolishimp/specification_methodology/releases/latest')
assert latest['id'] == public['release_id'] and not latest['draft'] and not latest['prerelease']
assert latest['tag_name'] == 'specification_methodology/v3.1.0-rc.2'
checks = read(w / 'public-readback/host-checks/RESULT.json')
prior = read(w / 'assessed-packaged/RESULT.json')
assert all(op['passed'] for op in checks['operations'])
contexts = []
for host, details in checks['hosts'].items():
    prior_rows = prior['hosts'][host]['contexts'] + prior['hosts'][host]['boundary_controls']
    for row in details['contexts'] + details['boundary_controls']:
        name = row.get('purpose', row.get('case'))
        if not row.get('delivery'):
            assert name in ['missing-boundary', 'null-boundary', 'ill-typed-boundary']
            assert row['covered'] is False and row['selection_status'] == 'incomplete'
            contexts.append({'host': host, 'case': name, 'covered': False, 'delivery': None})
            continue
        original = next(item for item in prior_rows if item.get('purpose', item.get('case')) == name)
        body = read(Path(row['delivery']) / 'CONTEXT.json')['payload']
        previous = read(Path(original['delivery']) / 'CONTEXT.json')['payload']
        assert body == previous, (host, name, 'Public context payload differs from assessed package')
        assert row['covered'] and body['covered']
        if name == 'acceptance':
            assert row['W35'] == 'true' and row['W26'] == 'false'
        contexts.append({'host': host, 'case': name, 'covered': True,
                         'payload_equal_assessed_archive': True,
                         'query_sha256': body['query_sha256']})
    assert details['removed']
assert sum(row['covered'] for row in contexts) == 12
browser = read(w / 'public-readback/visual-browser/RESULT.json')
assert browser['status'] == 'passed' and len(browser['checks']) == 12 and not browser['errors']
assert browser['artifact_sha256'] == browser['artifact_sha256_after'] == 'b0fddc7ab3882446c4090c1d72e411e096593803f676bd244eccaa14db944b23'
cohort_path = w / 'public-readback/assets/cohort-release-v3.1.0-rc.2.json'
assert cohort_path.read_bytes() == (w / 'assets' / cohort_path.name).read_bytes()
result = {'kind': 'stdo.rc2.publication-conditions-closure/1',
          'performed_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'valid': True, 'release_id': public['release_id'], 'url': public['url'],
          'atomic_ref_count': 25, 'current_remote_objects_match': True,
          'rc1_tags_and_assets_preserved': True, 'latest_normal_release': True,
          'public_assets': 6, 'companion_members': 225,
          'public_host_operations': len(checks['operations']), 'contexts': contexts,
          'public_browser_checks': 12, 'cohort_sha256': hashlib.sha256(cohort_path.read_bytes()).hexdigest(),
          'native_release_note_C1': 'Closed by the actual cohort, assessments, atomic publication, public acquisition and fresh installation evidence.',
          'human_exact_cut_acceptance': 'Not performed or implied by publication.',
          'consumer_adoption': 'No existing consumer selection or global installation changed.'}
(w / 'PUBLIC_CLOSURE.json').write_text(json.dumps(result, indent=2) + '\n')
(w / 'REMOTE_AFTER.txt').write_text(remote_raw)
print(json.dumps({k: v for k, v in result.items() if k != 'contexts'}))
