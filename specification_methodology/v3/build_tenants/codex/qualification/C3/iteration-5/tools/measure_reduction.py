"""Measure declared source routes, not actor acquisition or task efficiency."""
import argparse
from pathlib import Path
from context import HERE, PACKAGE, INPUTS, library, git_bytes, read, sha, write


PATHS = [
 ('P01', ['FOUNDATIONS#result-conjunction','REFERENCE_FRAME_METHOD#result-conjunction'],
  ['REFERENCE_FRAME_METHOD#result-conjunction','AXIOMATIC_CALCULUS#ac-007-constraint-and-refusal'], 'EVALUATION_CONJUNCTION'),
 ('P02', ['FOUNDATIONS#workspace-and-context','TRANSFORMATION_LIBRARY#workrecovery-specialization'],
  ['SPEC_METHOD#agentic-construction-execution-stdo-up-020'], 'WORK_RECOVERY'),
 ('P03', ['SPEC_METHOD#construction-assessment-and-delegation','STDO_REFERENCE_FRAME_BASELINE#engagement-applicability'],
  ['SPEC_METHOD#construction-assessment-and-delegation'], 'TRIAGE_CARRIER'),
 ('P04', ['SPEC_METHOD#what-how-and-work-carriers'], [], 'DOMAIN_BINDING'),
 ('P05', ['SPEC_METHOD#universal-intake-triage'], ['SPEC_METHOD#universal-intake-triage'], 'TRIAGE_CARRIER'),
 ('P06', ['SPEC_METHOD#agentic-construction-execution-stdo-up-020'],
  ['SPEC_METHOD#agentic-construction-execution-stdo-up-020'], 'DOMAIN_BINDING'),
 ('P07', ['TRANSFORMATION_LIBRARY#faithful-projection','REFERENCE_FRAME_METHOD#rf-017-proportional-compression'],
  ['REFERENCE_FRAME_METHOD#rf-017-proportional-compression'], 'CONSTITUTIONAL_DERIVATION'),
 ('P08', ['FOUNDATIONS#judgment-and-authority','FOUNDATIONS#result-conjunction'],
  ['SPEC_METHOD#construction-assessment-and-delegation','REFERENCE_FRAME_METHOD#result-conjunction'], 'MEMBER_CONSTRUCTION_ASSESSMENT'),
 ('P09', ['RELEASE_METHOD#successor-baseline-conservation-stdo-up-015','IDENTITY_METHOD#release-version-boundary'],
  ['RELEASE_METHOD#successor-baseline-conservation-stdo-up-015','IDENTITY_METHOD#release-version-boundary'], 'RELEASE_ADOPTION'),
 ('P10', ['SPEC_METHOD#bounded-context-semantic-resolution','GLOSSARY_GUIDE#labels-with-several-senses'],
  ['SPEC_METHOD#bounded-context-semantic-resolution'], None),
 ('P11', ['WORLD_MODEL_METHOD#markov-object-construction-law'],
  ['WORLD_MODEL_METHOD#markov-object-construction-law'], None),
 ('P12', ['AXIOMATIC_CALCULUS#ac-017-interpretation-fidelity','TRANSFORMATION_LIBRARY#faithful-projection'],
  ['AXIOMATIC_CALCULUS#ac-017-interpretation-fidelity'], None),
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source-commit', required=True)
    parser.add_argument('--theory-root', type=Path, required=True)
    args = parser.parse_args()
    import build_interpretation as build
    build.documentary_inventory(args.source_commit)
    build.verify_dependencies(args.theory_root)
    section = library('synthesis/check_artifacts.py').section
    from context import REPO
    def data(subject, name):
        if subject == 'current':
            return (PACKAGE/name).read_bytes()
        if subject == 'preceding':
            return git_bytes(INPUTS['prior_account_commit'], (PACKAGE/name).relative_to(REPO))
        return (args.theory_root/name).read_bytes()
    def route(subject, identifier):
        name, anchor = identifier.split('#')
        path = 'standards/'+name+'.md'
        try:
            raw = data(subject,path)
            body = section(raw.decode(),anchor)[1].encode()
            return {'route':path+'#'+anchor,'member_sha256':sha(raw),
                    'selected_subtree_sha256':sha(body),'selected_subtree_bytes':len(body)}
        except (ValueError, FileNotFoundError, KeyError):
            return {'route':path+'#'+anchor,'standing':'selected route absent; sufficiency unestablished'}
    rows=[]
    for identifier, current, predecessor, frame in PATHS:
        selected={s:[route(s,x) for x in (predecessor if s=='rc2' else current)]
                  for s in ('current','preceding','rc2')}
        curated={}
        for subject in selected:
            name='standards/frames/'+str(frame)+'.md'
            if frame is None or subject=='rc2':
                curated[subject]={'standing':'no same named curated assembly selected'}
            else:
                try:
                    raw=data(subject,name)
                    curated[subject]={'path':name,'bytes':len(raw),'sha256':sha(raw)}
                except Exception as error:
                    if subject!='preceding':
                        raise
                    curated[subject]={'standing':'no same named prior assembly', 'reason':type(error).__name__}
        rows.append({'path':identifier,'selected_owner_routes':selected,'curated_view':curated,
            'complete_path_sufficiency':'not established by byte measurement',
            'ordinary_discovery':'not_performed','actual_actor_acquisition_bytes':None,
            'actual_route_hops':None,'retained_context':None,
            'new_decider_elimination':'none claimed from argument expansion'})
    entry={}
    for subject in ('current','preceding','rc2'):
        entry[subject]=[]
        for name in ('standards/README.md','standards/authority_compressions/stdo_bootstrap.md',
                     'standards/authority_compressions/stdo_compressed.md'):
            raw=data(subject,name);entry[subject].append({'path':name,'bytes':len(raw),'sha256':sha(raw)})
    raw_totals={}
    names=[p.relative_to(PACKAGE) for p in sorted((PACKAGE/'standards').glob('*.md'))]
    for subject in ('current','preceding','rc2'):
        total=0; missing=[]
        for name in names:
            try:total+=len(data(subject,str(name)))
            except (FileNotFoundError,KeyError):missing.append(str(name))
        raw_totals[subject]={'bytes':total,'missing_current_names':missing}
    write(HERE/'REDUCTION_MEASUREMENTS.json',{
        'source_commit':args.source_commit,'protocol_sha256':sha((HERE/'REDUCTION_PROTOCOL.md').read_bytes()),
        'preceding_package':INPUTS['prior_account_commit'],'encoding_basis':build.MANIFEST_SHA,
        'entry_artifacts':entry,'raw_member_totals':raw_totals,'paths':rows,
        'interpretation':'Selected source-subtree and offered artifact sizes only; no measured actor workflow or context-cost advantage.',
        'known_tradeoff':'Expanded arguments increase document acquisition. Their practical benefit requires independent use evidence.',
        'inherited_reduction_evidence': {
            'record': '../iteration-4/REDUCTION_MEASUREMENTS.json',
            'scope': 'I4 selector-owner witness remains an historical claim, not a new I5 gain.'},
        'new_assurance_routes': [route('current', identifier) for identifier in (
            'FOUNDATIONS#construction-assurance',
            'FOUNDATIONS#change-impact-and-evidence-retention',
            'SPEC_METHOD#transition-evidence-and-proof-cadence')],
        'new_assurance_scope': 'New I5 obligations are reported separately; they do not replace the fixed twelve comparison paths.'})
    print({'paths':len(rows),'raw_member_bytes':{k:v['bytes'] for k,v in raw_totals.items()}})


if __name__=='__main__':
    main()
