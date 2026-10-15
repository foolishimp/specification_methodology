"""Carry exact predecessor claims and proposed relations into the I4 subject.

This checks coordinates and records affected carrying loci. It makes no new
semantic disposition, owner decision or evidence-reuse assertion.
"""
import argparse
import copy
import json
from collections import Counter, defaultdict
from context import HERE, PRIOR, REPO, PACKAGE, INPUTS, git_bytes, library, read, sha, write


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source-commit', required=True)
    args = parser.parse_args()
    build = library('iteration-3/build_interpretation.py')
    build.documentary_inventory(args.source_commit)
    cc = library('iteration-3/check_conservation.py')
    old = read(PRIOR/'CONSERVATION.json')
    original = git_bytes(INPUTS['starting_tenant'], (PRIOR/'CONSERVATION.json').relative_to(REPO))
    if sha(original) != sha((PRIOR/'CONSERVATION.json').read_bytes()):
        raise ValueError('Historical map changed')
    expected = cc.coordinates.common_rows(git_bytes(INPUTS['common_input'], cc.COMMON_PATH).decode())
    rows = copy.deepcopy(old['rows'])
    proposal_path=HERE/'source/selector-conservation/ROW_AMENDMENT.json'
    proposal=read(proposal_path)
    if (proposal['common_input_commit']!=INPUTS['common_input'] or
        proposal['account_preimage']['sha256']!=sha(original) or
        proposal['owner_decision'].get('status')!='pending' or
        proposal['owner_decision'].get('record') is not None or
        proposal['accepted_disposition'] is not None):
        raise ValueError('Conservation proposal basis or authority changed')
    matches=[i for i,row in enumerate(rows) if row['id']==proposal['claim_id']]
    if len(matches)!=1:
        raise ValueError('Conservation proposal has no unique claim')
    index=matches[0]
    canonical=json.dumps(rows[index],sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
    if (sha(canonical)!=proposal['preconditions']['original_row_canonical_sha256'] or
        rows[index]!=proposal['original_row']):
        raise ValueError('Conservation proposal row preimage changed')
    replacement=proposal['proposed_row']
    for field in ('id','source_member','source_anchor'):
        if replacement[field]!=rows[index][field]:
            raise ValueError('Conservation proposal changed claim identity')
    coordinate=library('iteration-3/review-repair/interpretation/repair_account.py')
    for route,pin in proposal['replacement_locus_pins'].items():
        path,anchor=route.split('#',1)
        raw=(PACKAGE/path).read_bytes()
        if sha(raw)!=pin['member_sha256'] or sha(coordinate.heading_units(raw)[anchor]['body'])!=pin['body_sha256']:
            raise ValueError('Replacement source changed; reassess proposal: '+route)
    rows[index]=copy.deepcopy(replacement)
    if len({r['id'] for r in rows}) != len(rows) or {r['id'] for r in rows} != set(expected):
        raise ValueError('Common frontier and inherited dispositions differ')
    source_cache, old_cache, loci, member_pins = {}, {}, {}, {}
    affected = []
    for row in rows:
        if row['source_member'] != expected[row['id']]:
            raise ValueError('Wrong predecessor member: ' + row['id'])
        changed = []
        for route in row.get('successor_loci', [row.get('successor_locus')]):
            if not route:
                continue
            path, _, anchor = route.partition('#')
            if path not in source_cache:
                source_cache[path] = (PACKAGE/path).read_bytes()
                old_cache[path] = git_bytes(INPUTS['starting_tenant'], (PACKAGE/path).relative_to(REPO))
                member_pins[path] = {'sha256':sha(source_cache[path]),'bytes':len(source_cache[path])}
            body = cc.section_body(source_cache[path].decode(), anchor).encode()
            prior_body = cc.section_body(old_cache[path].decode(), anchor).encode()
            loci[route] = {'sha256':sha(body),'bytes':len(body),'member_sha256':sha(source_cache[path])}
            if body != prior_body:
                changed.append(route)
        if row.get('successor_locus'):
            row['successor_sha256'] = member_pins[row['successor_locus'].split('#')[0]]['sha256']
        row['current_review'] = {
            'source_commit':args.source_commit,'standing':'independent_I4_assessment_pending',
            'changed_carrying_loci':changed,
            'reuse':'Earlier source comparisons retain their exact subjects. Current applicability and semantic fidelity are not established by these coordinates.'}
        if changed:
            affected.append({'id':row['id'],'changed_loci':changed,'disposition':row['disposition']})
        relation = row.get('successor_relation')
        if row['disposition'] == 'superseded' and (not relation or not relation.get('replacement_loci')):
            raise ValueError('Replacement relation absent: '+row['id'])
    current = {'kind':'stdo.i4.author-conservation-account','schema_version':3,
        'input_commit':INPUTS['common_input'],'candidate_source_commit':args.source_commit,
        'preimage':{'commit':INPUTS['starting_tenant'],'path':str((PRIOR/'CONSERVATION.json').relative_to(REPO)),
                    'sha256':sha(original)},
        'source_member_pins':old['source_member_pins'],
        'successor_member_pins':member_pins,'successor_locus_pins':loci,
        'rows':rows,'affected_rows':affected,
        'proposal_inputs':[{'path':str(proposal_path.relative_to(HERE)),
                            'sha256':sha(proposal_path.read_bytes()),
                            'claim':proposal['claim_id'],'standing':proposal['standing']}],
        'standing':'Inherited author dispositions with exact current carrying coordinates; no new owner acceptance or semantic reuse decision.'}
    write(HERE/'CONSERVATION.json',current)
    write(HERE/'FRONTIER.json',{'kind':'stdo.i4.frontier-projection','source_commit':args.source_commit,
        'conservation_sha256':sha((HERE/'CONSERVATION.json').read_bytes()),
        'rows':[{'id':r['id'],'disposition':r['disposition'],
                 'relation':r.get('successor_relation',{}).get('id'),
                 'acceptance':r.get('acceptance'),'current_review':r['current_review']['standing']} for r in rows]})
    grouped = defaultdict(list)
    for row in rows:
        if row['disposition']=='superseded':
            grouped[row['comparison_group']].append({'claim':row['id'],
                'relation':row['successor_relation'],
                'dependencies':row.get('shared_replacement_dependencies',[])})
    write(HERE/'REPLACEMENT_QUESTIONS.json',{
        'kind':'stdo.i4.owner-question-input','source_commit':args.source_commit,
        'groups':dict(grouped),'standing':'Input to the common pen for consolidation by substantive question. No disposition is accepted here.'})
    print({'rows':len(rows),'affected_rows':len(affected),'dispositions':dict(Counter(r['disposition'] for r in rows))})


if __name__=='__main__':
    main()
