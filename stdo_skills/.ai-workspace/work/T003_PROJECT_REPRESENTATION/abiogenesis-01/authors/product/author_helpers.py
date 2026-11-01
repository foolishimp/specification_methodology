"""Test-run serialization and exact grounding only; semantic strings are authored in each script."""
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
WORK = HERE.parents[1]
PROVIDER = Path('/Users/jim/src/apps/specification_methodology/a_c/build_tenants/graphify/code')
sys.path.insert(0, str(PROVIDER))
import ac_generate as gen


class Answer:
    def __init__(self, index):
        self.index = index
        self.chunk = json.loads((WORK/'run/generation/chunks.json').read_text())[index]
        self.sections = self.chunk['segments']
        self.value = {name: [] for name in ('concepts','constraints','relations','latitude','residuals','dispositions','limitations')}
        self.handled = set()

    def ground(self, indices):
        if isinstance(indices, int): indices = [indices]
        if isinstance(indices, tuple) and len(indices)==2 and isinstance(indices[1],str): indices=[indices]
        # Full exact supplied section is selected by the author as its re-entry.
        # This function computes no interpretation or authority.
        out = []
        for i in indices:
            quote = None
            if isinstance(i, tuple): i,quote=i
            s = self.sections[i]
            if quote is not None:
                offset=s['text'].index(quote)
                start=s['start_line']+s['text'][:offset].count('\n')
                out.append({'section_id':s['id'],'start_line':start,
                            'end_line':start+quote.count('\n'),'quote':quote})
                self.handled.add(i)
                continue
            lines = s['text'].splitlines()
            while lines and not lines[-1]: lines.pop()
            assert lines
            out.append({'section_id': s['id'], 'start_line': s['start_line'],
                        'end_line': s['start_line']+len(lines)-1, 'quote':'\n'.join(lines)})
            self.handled.add(i)
        return out

    def concept(self, section, key, label, definition, conditions=(), exceptions=()):
        self.value['concepts'].append(dict(key=key,label=label,definition=definition,
            conditions=list(conditions),exceptions=list(exceptions),grounding=self.ground(section)))

    def constraint(self, section, key, targets, statement, conditions=(), exceptions=(), uncertainty=''):
        self.value['constraints'].append(dict(key=key,applies_to_keys=targets,statement=statement,
            conditions=list(conditions),exceptions=list(exceptions),uncertainty=uncertainty,grounding=self.ground(section)))

    def relation(self, section, key, source, target, kind, meaning, governing=False, conditions=(), exceptions=()):
        self.value['relations'].append(dict(key=key,source_key=source,target_key=target,kind=kind,
            meaning=meaning,governing=governing,conditions=list(conditions),exceptions=list(exceptions),grounding=self.ground(section)))

    def latitude(self, section, key, targets, allowed, forbidden):
        self.value['latitude'].append(dict(key=key,applies_to_keys=targets,allowed=allowed,forbidden=forbidden,grounding=self.ground(section)))

    def residual(self, section, key, subject, uncertainty, consequence):
        self.value['residuals'].append(dict(key=key,subject_key=subject,uncertainty=uncertainty,consequence=consequence,grounding=self.ground(section)))

    def omit(self, section, reason):
        self.handled.add(section)
        self.value['dispositions'].append(dict(section_id=self.sections[section]['id'],decision='omitted',keys=[],reason=reason))

    def save(self, limitations=()):
        assert self.handled == set(range(len(self.sections))), ('unhandled sections',set(range(len(self.sections)))-self.handled)
        existing = {d['section_id'] for d in self.value['dispositions']}
        for s in self.sections:
            if s['id'] in existing: continue
            records = [r for f in ('concepts','constraints','relations','latitude','residuals') for r in self.value[f]
                       if any(g['section_id']==s['id'] for g in r['grounding'])]
            residual = any(r in self.value['residuals'] for r in records)
            self.value['dispositions'].append(dict(section_id=s['id'],decision='residual' if residual else 'retained',
                keys=[r['key'] for r in records],reason='Authored meanings and constraints retain this supplied section; unresolved meanings remain explicit.' if residual else 'Authored records retain the supplied source meaning and its conditions.'))
        self.value['limitations'] = list(limitations)
        gen.author_check(self.value,self.chunk)
        path=HERE/f'answer-{self.index:02d}.json'
        if path.exists(): raise ValueError('draft exists; retain it and use a new revision')
        path.write_text(json.dumps(self.value,ensure_ascii=False,indent=2)+'\n')
        print(json.dumps({'chunk':self.chunk['id'],'answer':str(path),'counts':{k:len(v) for k,v in self.value.items()}}))
