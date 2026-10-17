"""Every count the release record states, read from the record itself (I5-10, after two hand-typed count
errors in the RC1 record). Writes qualification/C3-ITER5/COUNTS.json and prints it. Run from the tenant
root with python3 -I. The release note, results table and handoff take their figures from this file.
"""
import collections, json, os, re
C = {}
files = []
for dp, _, fs in os.walk('standards'):
    for f in fs:
        if '__pycache__' not in dp: files.append(os.path.relpath(os.path.join(dp, f), 'standards'))
by = collections.Counter(p.split('/')[0] if '/' in p else ('member' if p.endswith('.md') else 'other') for p in files)
C['standards_files'] = len(files); C['members'] = by['member']; C['schemas'] = by['schemas']; C['templates'] = by['templates']; C['frame_files'] = by['frames']
C['other_top_level'] = by['other']
C['plugin_files'] = sum(len(fs) for dp, _, fs in os.walk('plugins/spec'))
rev = json.load(open('frontier/REVIEW.json')); rows = rev['rows']
C['frontier_rows'] = len(rows)
C['by_disposition'] = dict(collections.Counter(r['disposition'] for r in rows))
res = collections.Counter(r.get('semantic_review', {}).get('result') for r in rows if r['disposition'] == 'conserved')
C['conserved_by_review_result'] = dict(res)
C['conserved_unread'] = res.get('indeterminate', 0)
C['conserved_read'] = sum(v for k, v in res.items() if k != 'indeterminate')
C['proposed_replacements'] = sum(1 for r in rows if r.get('proposed_replacement'))
s = open('standards/CONFORMANCE.md', encoding='utf-8').read()
ids = re.findall(r'^\| (\d+|J\d+|UC-\d+|AS-\d+) \|', s, re.M)
C['discriminators'] = {'member': sum(i.isdigit() for i in ids), 'integrated': sum(i.startswith('J') for i in ids),
                       'universal_construction': sum(i.startswith('UC') for i in ids), 'assurance': sum(i.startswith('AS') for i in ids)}
p = json.load(open('a_c/i3/axiomatic-program.json')); C['ac_clauses'] = len(p['clauses']); C['ac_frame_indexes'] = len(p['frame_indexes'])
disp = ''.join(open('a_c/i3/dispositions/' + f, encoding='utf-8').read() for f in os.listdir('a_c/i3/dispositions'))
C['ac_sections'] = {k: disp.count(f'| {k} |') for k in ('encoded-in-part', 'no determination', 'not-encoded-i3')}
fr = json.load(open('standards/frames/FRAME_INPUTS.json'))['frames']
C['frames'] = len(fr); C['frame_bytes_largest'] = max(f['bytes'] for f in fr); C['frame_bytes_total'] = sum(f['bytes'] for f in fr)
C['frame_largest'] = max(fr, key=lambda f: f['bytes'])['id']
json.dump(C, open('qualification/C3-ITER5/COUNTS.json', 'w'), indent=1); print(json.dumps(C, indent=1))
