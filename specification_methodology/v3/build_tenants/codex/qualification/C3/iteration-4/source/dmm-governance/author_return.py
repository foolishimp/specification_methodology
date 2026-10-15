#!/usr/bin/env python3
"""Author the one-heading account input and check the bounded source repair."""
import copy
import hashlib
import json
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
TENANT = HERE.parents[4]
ROOT = TENANT.parents[3]
PREFIX = str(TENANT.relative_to(ROOT))+'/'
SOURCE = 'cd19955505a0350b5d9b0f19d00c89e6d1810aa6'
I3 = '199c6d29bc02590a8b7f252043fc43223c09808d'
ACCOUNT_SHA = 'b8c43489311b387045de129db459ef1bf29c1334724fcccc36474ea9565fedcd'
BEFORE_FILE_SHA = '0cd7e6b9809d03e47b3de52a44fad00db1f102cc679a4b8ce8ce3929560f19a0'
IDENTITY = 'DESIGN_MODULE_METHOD.11a-governancestrategy-separation-rule'
PATH = 'standards/DESIGN_MODULE_METHOD.md'
ANCHOR = '11a-governancestrategy-separation-rule'
HEADING = '## 11A. Governance/Strategy Separation Rule\n'
OLD_ROW_SHA = '24925da4a2c5c4f9e100ace809a50a64bc9c05448b424ec0d4d2ba3e519adde1'
AUDIT_WHEN = 'When assessing this governance/strategy argument, its applicability, its conservation or its fidelity. This is source provenance, not a new unconditional operational input.'


def sha(value):
    return hashlib.sha256(value if isinstance(value,bytes) else value.encode()).hexdigest()


def git_bytes(commit,path):
    return subprocess.check_output(['git','show',commit+':'+path],cwd=ROOT)


def section(raw):
    lines=raw.decode().splitlines(keepends=True)
    starts=[i for i,line in enumerate(lines) if line==HEADING]
    assert len(starts)==1
    start=starts[0]
    end=next((i for i in range(start+1,len(lines)) if re.match(r'^#{1,2} ',lines[i])),len(lines))
    return ''.join(lines[start:end]),start+1,end


def pin(raw):
    text,start,end=section(raw)
    return {'path':PATH,'anchor':ANCHOR,'start_line':start,'end_line':end,
            'sha256':sha(text),'hash_boundary':'Exact UTF-8 bytes from the heading start through the line before the next same-or-higher-level heading, including this heading, separator and terminal newlines.'}


def dump(name,value):
    (HERE/name).write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n')


def main():
    account_path=TENANT/'qualification/C3/iteration-4/DETERMINATIONS.json'
    account_bytes=account_path.read_bytes()
    assert sha(account_bytes)==ACCOUNT_SHA,'Receiving account drift.'
    account=json.loads(account_bytes)
    by_id={row['id']:row for row in account['determinations']}
    row=by_id[IDENTITY]
    original_account=json.loads(git_bytes(I3,PREFIX+'qualification/C3/iteration-3/DETERMINATIONS.json'))
    i3row=next(item for item in original_account['determinations'] if item['id']==IDENTITY)
    assert row['argument']==i3row['argument'],'A distinct current local argument needs explicit preservation review.'

    before=git_bytes(SOURCE,PREFIX+'successor/'+PATH)
    current=(TENANT/'successor'/PATH).read_bytes()
    assert sha(before)==BEFORE_FILE_SHA
    before_section=section(before)[0]
    current_section=section(current)[0]
    added=current_section[current_section.index('For this rule,'):current_section.index('Lawful governance publication includes:')]
    assert added and current_section.count(added)==1
    assert current_section.replace(added,'',1)==before_section
    assert current.replace(added.encode(),b'',1)==before,'An effect escaped the granted source section.'
    i3source=git_bytes(I3,PREFIX+'successor/'+PATH)
    assert section(i3source)[0]==before_section,'The operative preimage differs from I3.'

    argument=copy.deepcopy(row['argument'])
    old_families=argument.get('source_family_arguments',[])
    removed=[entry for entry in old_families if entry.get('source_row',{}).get('sha256')==OLD_ROW_SHA]
    assert len(removed)==1
    argument['source_family_arguments']=[entry for entry in old_families if entry not in removed]
    argument['premises']=['F2','F4','F6']
    argument['instance_premises']=[
        'At this applicable boundary, the bound ratified responsibility fixes whether strategy ownership is part of its role.',
        'The actual operation or decision grant fixes what the boundary may do; governance information is not that grant.'
    ]
    argument['pillar_contributions']={
        'interpretation':'F2 distinguishes information about state and admissible routes from a prescription for the actor; a governance encoding cannot silently change that meaning.',
        'typed_composition':'F4 conserves each actor\u2019s responsibility and authority across the governance handoff; an observation or route helper does not acquire the other actor\u2019s strategy role through composition.',
        'evidence_and_authority':'F6 separates evidence from permission; accurate governance information cannot confer the other actor\u2019s strategy grant.'
    }
    argument['conditional_consequence']='For the bound responsibility and actual grant, governance publication preserves the information/strategy distinction and each actor\u2019s authority. If strategy ownership is not explicitly part of this boundary\u2019s ratified responsibility, its governance information cannot authorize imperative strategy law or hidden replacement judgment. Explicitly ratified strategy ownership retains its stated exception within the owned role and actual grant.'
    argument['policy_choices']=[
        'This DMM rule chooses the governance/strategy publication distinction and its existing listed lawful and unlawful forms. F2/F4/F6 explain the authority boundary without deriving the complete domain list or imposing governance-only responsibility on every system.'
    ]
    argument['owned_exceptions']={
        'ratified_strategy_ownership':'The boundary may prescribe strategy when that ownership is explicitly part of its ratified responsibility, within that owned role and actual grant.',
        'assessment_boundary':'The existing exception for explicitly owned assessment remains separate and unchanged; it is not tightened into a new ratification requirement.'
    }
    argument['source_refs']=[
        {'path':PATH,'anchor':ANCHOR,'role':'provenance','required_when':AUDIT_WHEN},
        {'path':'standards/FOUNDATIONS.md','anchor':'foundational-commitments','role':'provenance','required_when':AUDIT_WHEN},
        {'path':'standards/FOUNDATIONS.md','anchor':'interpretation-and-representation','role':'provenance','required_when':AUDIT_WHEN},
        {'path':'standards/FOUNDATIONS.md','anchor':'typed-composition-and-conservation','role':'provenance','required_when':AUDIT_WHEN},
        {'path':'standards/FOUNDATIONS.md','anchor':'judgment-and-authority','role':'provenance','required_when':AUDIT_WHEN}
    ]
    argument['local_source_argument']={
        'path':PATH,'anchor':ANCHOR,'sha256':sha(added),
        'hash_boundary':'The two added paragraphs, beginning For this rule and ending before Lawful governance publication includes, with terminal blank line.',
        'role':'provenance','required_when':AUDIT_WHEN}
    changed={key for key in set(argument)|set(row['argument']) if argument.get(key)!=row['argument'].get(key)}
    for key,value in row['argument'].items():
        if key not in changed:
            assert argument[key]==value
    assert argument['standing']==row['argument']['standing']
    for field in ('predicate','obligations','permissions_exceptions','dependencies','dependency_relations','result_mapping','applicability','inputs'):
        assert row[field]==i3row[field],field
    semantic_id_strings=[]
    def scan(value,path):
        if isinstance(value,str) and value in by_id: semantic_id_strings.append(path)
        elif isinstance(value,list):
            for i,v in enumerate(value): scan(v,path+'['+str(i)+']')
        elif isinstance(value,dict):
            for k,v in value.items(): scan(v,path+'.'+k)
    scan(argument,'argument')
    assert not semantic_id_strings

    patch={
        'schema_version':'stdo.authored-semantic-fields-patch.v1',
        'activation':'I4-DMM-GOVERNANCE-ARGUMENT',
        'standing':'Authored one-heading source/account input; independent source fidelity remains unassessed.',
        'frozen_semantic_preimage':I3,
        'source_preimage_commit':SOURCE,
        'receiving_account_sha256':ACCOUNT_SHA,
        'integration':'Apply this one ID after the existing source patches. Exclude profile-routing\u2019s unresolved §11A-only argument binding for this same ID rather than co-applying it. Regenerate source clauses, ranges and owner pins from the new source. All non-argument semantic fields remain unchanged.',
        'patches':[{
            'id':IDENTITY,'source_before':pin(before),'source_current':pin(current),
            'i3_source_heading_sha256':pin(i3source)['sha256'],
            'argument_preimage_sha256':sha(json.dumps(row['argument'],sort_keys=True,separators=(',',':'),ensure_ascii=False)),
            'argument_preimage_hash_boundary':'Canonical UTF-8 JSON with sorted keys, compact separators, ensure_ascii false, no terminal newline.',
            'semantic_fields':{'argument':argument},
            'changed_argument_fields':sorted(changed),
            'replacement_justification':'The held current argument equals I3 and contains only the obsolete coarse family wrapper, policy and source copy; no distinct local clause argument is removed. The new argument is grounded at the operative §11A consumer. Any later local change conflicts with this preimage and must be retained/reviewed rather than silently overwritten.',
            'preserved_fields':['predicate','obligations','permissions_exceptions','dependencies','dependency_relations','result_mapping','applicability','inputs','all other non-argument semantic fields'],
        }]
    }
    dump('ACCOUNT_PATCH.json',patch)
    cases=[
        ('Governance truth','No strategy ownership; publish state, pressure or route eligibility.','lawful publication','The original lawful list remains exact.'),
        ('Unowned repair direction','No strategy ownership; prescribe how the downstream actor repairs.','unlawful strategy drift','The first unlawful form remains exact; F2/F4/F6 explain its boundary.'),
        ('Ratified strategy role','Strategy ownership explicitly belongs to ratified responsibility, with the actual grant.','strategy exception remains available','The original opening exception remains exact and the argument expressly preserves it.'),
        ('Owned assessment','Budgets, scores or ratings assess the actor within an explicitly owned assessment boundary.','assessment exception remains available','The existing assessment exception remains exact; the argument does not require additional strategy ratification.'),
        ('Unowned replacement assessment','Budgets, scores or ratings recreate another actor\u2019s judgment without ownership of that assessment boundary.','unlawful strategy drift','The original conditional prohibition remains exact.'),
        ('Hidden doctrine','A governance-only prompt, projection or route helper becomes replacement strategy doctrine.','unlawful strategy drift','The original hidden-doctrine and replacement-engine clauses remain exact.'),
        ('Optional profile boundary','A system has not adopted the applicable DMM profile or does not trigger this boundary relation.','no new universal governance-only mandate','The source governing relation and account applicability remain unchanged; the local argument selects no universal responsibility configuration.')
    ]
    dump('SAME_CASE_GUARDS.json',{
        'standing':'Source-linked author assessments and byte-preservation guards; not independent fidelity proof.',
        'owner':{'path':PATH,'anchor':ANCHOR},'before':pin(before),'current':pin(current),
        'cases':[{'name':name,'instance':instance,'before':outcome,'after':outcome,'reason':reason} for name,instance,outcome,reason in cases]
    })
    assert account_path.read_bytes()==account_bytes
    checks={
        'activation':'I4-DMM-GOVERNANCE-ARGUMENT','standing':'Author structural checks, not independent fidelity acceptance.',
        'source_before_sha256':sha(before),'source_current_sha256':sha(current),
        'source_before':pin(before),'source_current':pin(current),
        'single_insertion_only':True,'all_existing_section_bytes_preserved':True,
        'all_other_source_sections_byte_identical':True,'i3_and_before_section_equal':True,
        'current_and_i3_argument_equal_before_change':True,
        'distinct_local_argument_removed':False,'obsolete_coarse_family_copies_removed':len(removed),
        'non_argument_semantic_fields_changed':[],
        'new_exact_semantic_id_values':semantic_id_strings,
        'same_case_guards':len(cases),'receiving_account_unchanged':True,
        'source_argument_added_bytes':len(added.encode()),
        'limits':['No generated account is written.','Parent source/account integration and independent review remain outstanding.','The argument selects no new strategy owner, approval gate, required record or profile adoption.']
    }
    dump('CHECKS.json',checks)
    print(json.dumps({key:checks[key] for key in ('source_before_sha256','source_current_sha256','single_insertion_only','all_other_source_sections_byte_identical','obsolete_coarse_family_copies_removed','same_case_guards','receiving_account_unchanged','source_argument_added_bytes')},indent=2))


if __name__=='__main__':
    main()
