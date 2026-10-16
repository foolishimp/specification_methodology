# Independent finite witness for EC-I5-COMP-01 semantics, case 4.
# No candidate implementation is executed and no universal theorem is claimed.
import itertools,json
omega=list(itertools.product((False,True),('irrelevant-A','irrelevant-B')))
pi=lambda s:s[0]
q=lambda s:s[0]
t=lambda o:'satisfied' if o else 'falsified'
pairs=[(a,b) for a in omega for b in omega]
result={
 'domain':omega,
 'predicate':'required fact is true',
 'observation':'required fact; omits irrelevant annotation',
 'two_distinct_subjects_have_same_observation':any(a!=b and pi(a)==pi(b) for a,b in pairs),
 'owner_observation_sufficiency':all(pi(a)!=pi(b) or q(a)==q(b) for a,b in pairs),
 'checker_sound_satisfied':all(t(pi(s))!='satisfied' or q(s) for s in omega),
 'checker_sound_falsified':all(t(pi(s))!='falsified' or not q(s) for s in omega),
 'checker_decides_all_cases':all(t(pi(s)) in ('satisfied','falsified') for s in omega),
 'claude_consumer_literal_extra_evidence_trigger':any(a!=b and pi(a)==pi(b) for a,b in pairs),
 'scope':'Finite interpretation witness only; no candidate execution or actual-use/context-fit evidence.'
}
print(json.dumps(result,indent=2))
