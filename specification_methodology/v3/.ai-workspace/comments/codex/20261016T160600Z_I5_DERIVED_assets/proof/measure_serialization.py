"""Record immutable artifact sizes, separately from same-input factoring.

This observes serialized bytes. It does not measure actor context, process
memory, source fidelity, qualification sufficiency or practical efficiency.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess


HERE = Path(__file__).resolve().parents[1]
REPO = next(p for p in HERE.parents if (p / '.git').exists())
TENANT = 'specification_methodology/v3/build_tenants/codex/'
I5 = TENANT + 'qualification/C3/iteration-5/'
PRIOR = '62318d3b0be35985a0397aa39daee0ec8836eabc'
TOOLING = 'fd450061c39a5fbb10625c99b64a52b518d1d00e'


def blob(commit, path):
    return subprocess.check_output(['git', 'show', commit + ':' + path], cwd=REPO)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--package-commit', required=True)
    args = parser.parse_args()
    resolved = subprocess.check_output(
        ['git', 'rev-parse', args.package_commit + '^{commit}'], cwd=REPO,
        text=True).strip()
    if resolved != args.package_commit:
        raise ValueError('Use the full immutable package commit')
    artifacts = {}
    for label, commit in [('preceding_I4', PRIOR), ('current_I5', resolved)]:
        artifacts[label] = {'commit': commit, 'members': {}}
        for name in ('source-account.json', 'program.json', 'map.json'):
            raw = blob(commit, TENANT + 'successor/interpretation/' + name)
            artifacts[label]['members'][name] = {
                'bytes': len(raw), 'sha256': digest(raw)}
        artifacts[label]['total_bytes'] = sum(
            item['bytes'] for item in artifacts[label]['members'].values())
    receipt_raw = blob(TOOLING, I5 + 'interpretation/TOOLING_CHECK.json')
    qualification = json.loads(receipt_raw)['qualification']
    costs = qualification['same_semantic_input_costs']
    totals = {kind: value['actual_program_file_bytes'] +
                   value['actual_native_map_file_bytes']
              for kind, value in costs.items()}
    if not qualification['expanded_matches_original_program']:
        raise ValueError('No exact same-input equivalence evidence')
    result = {
        'kind': 'stdo.i5.serialized-artifact-cost',
        'measurement_script_sha256': digest(Path(__file__).read_bytes()),
        'published_artifacts': artifacts,
        'same_input_factoring': {
            'receipt_commit': TOOLING,
            'receipt_path': I5 + 'interpretation/TOOLING_CHECK.json',
            'receipt_sha256': digest(receipt_raw),
            'semantic_input_commit': qualification['frozen_I4_commit'],
            'semantic_account_sha256': qualification['source_account_sha256'],
            'program_and_map_bytes': totals,
            'saved_bytes': totals['expanded'] - totals['referenced'],
            'exact_expansion': qualification['equivalence']['exact_expansion']},
        'limits': [
            'The fixed-I4 comparison isolates qualification-reference factoring.',
            'Current-I5 totals also contain new obligations and metadata; they do not isolate the optimization.',
            'The pinned native map format still copies the program clauses.',
            'Serialized bytes are neither peak RSS nor retained context, attention or task-completion cost.',
            'Native session cost, active host context and comparative practical efficiency remain unmeasured.']}
    output = HERE / 'SERIALIZED_COST.json'
    output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'artifact_bytes': {
        key: value['total_bytes'] for key, value in artifacts.items()},
        'fixed_input_saved_bytes': result['same_input_factoring']['saved_bytes']}))


if __name__ == '__main__':
    main()
