"""Selected same-Reviewer candidate phase through existing public APIs; no dispatch."""
import importlib.util, json, sys
from pathlib import Path
HERE=Path(__file__).resolve().parent.parent
spec=importlib.util.spec_from_file_location('review_candidate_base',HERE/'prepare_review.py')
m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
real_save=m.save
SESSION='628dfe7c-13d9-4c76-8146-64fd9787ee38'
EXPECTATION='9ed61889acb0caaec032092f45fbfa888ea63b6ae74b0be56d1301990c67bc4a'
CONTINUITY='''
This is the candidate phase of the same actual Reviewer session 628dfe7c-13d9-4c76-8146-64fd9787ee38. Your real source-first expectation is sha256:9ed61889acb0caaec032092f45fbfa888ea63b6ae74b0be56d1301990c67bc4a, produced by review.prepare in the completed source-only continuation. The original 300-second source-only attempt timed out; the 600-second continuation completed and recorded the artifact. Those facts are preserved, not reclassified as candidate review. Root selects a fresh 900-second candidate phase. Retain your disclosed bootstrap and tool-runtime exposure.

Use that expectation unchanged. Do not repeat schema or expectation construction. Acquire candidate exactly once via the supplied review.prepare candidate request. Source payloads can be base64; decode only in memory, or use source.read encoding=utf8 for selected source text. No scratch-file/request-file writes. Use source acquisition evidence plus direct read-only source inspection as needed. The common and tool increment and Codex tenant are the exact 36-file population; Claude tenant is not in this claim. Keep actual paths and meaningful falsifiers ahead of counts. No Q01-Q12 host qualification is supplied by this static review. Return the original contract object before the 900-second bound, with any missing scope explicit.
'''
def save(path,value):
    if path.name=='TASK.md' and path.parent.name=='candidate':
        value=value.replace('within a 1200-second aggregate Reviewer budget','under Root\'s explicit continuation budget')+CONTINUITY
    if path.name=='STARTUP.txt' and path.parent.name=='candidate':
        value='Continue your existing actual Reviewer session; the real expectation is '+EXPECTATION+'. '+value
    if path.name=='actor-plan.json' and path.parent.name=='candidate':
        value['argv'] += ['--resume',SESSION,'--system-prompt-snapshot','off']
        value['argv'][value['argv'].index('--append-system-prompt')+1]=(path.parent/'STARTUP.txt').read_text().rstrip('\n')
        value['dependencies']=[m.pin(Path(x['path'])) if Path(x['path']).name=='STARTUP.txt' else x for x in value['dependencies']]
    return real_save(path,value)
m.save=save
r=m.prepare(HERE/'claude-selection-static-2.json','c34922698cf3dae29ee481ce0260f1d90c75c976f61e4c3f036707ac1f0aa561','candidate',EXPECTATION,True,'claude-setup2')
print(json.dumps(r,indent=2))
