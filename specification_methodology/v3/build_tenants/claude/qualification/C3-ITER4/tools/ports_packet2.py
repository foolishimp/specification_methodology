"""The second ports packet (I4-09): the receivers as repaired after R2b, with the records and the donor
sources of the ports whose receivers changed. Run from the tenant root with python3 -I."""
import os, re, subprocess, sys
sys.argv = [sys.argv[0], '--whole']
exec(open('qualification/C3-ITER4/tools/modal_batches.py').read().split('rev = json.load')[0])
REPO='/Users/jim/src/apps/specification_methodology-claude'; CODEX='specification_methodology/v3/build_tenants/codex/'
def show(c, p, a=None, b=None):
    t=subprocess.run(['git','-C',REPO,'show',f'{c}:{p}'],capture_output=True,text=True).stdout.split('\n')
    return '\n'.join(t[a-1:b] if a else t)
def whole(path, anchor): return sections_whole(path).get(anchor) or '(not found)'
def lines(path, a, b): return '\n'.join(open(path, encoding='utf-8').read().split('\n')[a-1:b])
out=["# R2b successor packet: the ported receivers after the R2b repairs\n\nThe first ports readback (R2b, `reviews/R2b.json`) made 13 findings; `reviews/TRIAGE-R2.md` records each disposition. This packet gives the receivers as they now stand, the corrected records, and the donor sources again where a receiver changed. Read everything here and nothing else.\n"]
out.append("\n## The triage record (the Writer's dispositions, an input to your judgment)\n\n```markdown\n"+open('qualification/C3-ITER4/reviews/TRIAGE-R2.md').read()+"\n```\n")
out.append("\n## The port records as corrected (CROSS_SYNTHESIS, source coordinates, port list and 'How each part is adapted')\n\n```markdown\n"+lines('design/CROSS_SYNTHESIS.md',23,260)+"\n```\n")
out.append("\n## Receivers now\n")
for label, path, anchor in [('REFERENCE_FRAME §1 Imports into this context (port 3)','standards/REFERENCE_FRAME.md','imports-into-this-context'),('FOUNDATIONS §2 Imports between members (port 3)','standards/FOUNDATIONS.md','imports-between-members'),('EVALUATION §6 Conformance of realisations (port 4)','standards/EVALUATION.md','6-conformance-of-realisations'),('ACTIVATION §2 Context construction under an envelope (port 5, acquisition rule)','standards/ACTIVATION.md','2-context-construction-under-an-envelope'),('FOUNDATIONS §3 Foundation to law (port 1)','standards/FOUNDATIONS.md','foundation-to-law'),('FOUNDATIONS §3 Commitments (port 2)','standards/FOUNDATIONS.md','3-commitments')]:
    out.append(f"\n### {label}\n\n```markdown\n{whole(path, anchor).strip()}\n```\n")
m=open('standards/FOUNDATIONS.md',encoding='utf-8').read().split('\n'); k=[i for i,l in enumerate(m) if 'family-import rule' in l]
out.append("\n### FOUNDATIONS §3, the PROFILES line (R2b-05)\n\n```text\n"+'\n'.join(m[k[0]-1:k[0]+2] if k else ['(not found)'])+"\n```\n")
out.append("\n### The frame generator, docstring and header (port 5, R2b-07, R2a-05)\n\n```python\n"+lines('qualification/instruments/generate_frames.py',1,80)+"\n```\n\n```python\n"+'\n'.join([l for l in open('qualification/instruments/generate_frames.py').read().split('\n') if True][0:0])+"\n```\n")
g=open('qualification/instruments/generate_frames.py').read(); i=g.index('def select_rows'); j=g.index('def rebase_lines'); h=g.index('def source_line'); h2=g.index('def render')
out.append("\n```python\n"+g[i:j]+"\n```\n\n```python\n"+g[h:h2]+"\n```\n")
out.append("\n### The row-selection tests (R2b-07)\n\n```python\n"+open('qualification/instruments/test_generate_frames.py').read().split('class RowSelection')[1].split("if __name__")[0]+"\n```\n")
out.append("\n### The checker controls (C5, R2b-12, R2b-13)\n\n```python\n"+open('qualification/C3-ITER4/tools/ac_controls.py').read()+"\n```\n\n```json\n"+open('qualification/C3-ITER4/returns/ac_controls.json').read()+"\n```\n")
out.append("\n### The frontier review tool (C3, R2b-10, R2b-11)\n\n```python\n"+open('qualification/C3-ITER4/tools/frontier_review.py').read()+"\n```\n")
out.append("\n### The port evaluation record (I4 adaptations)\n\n```markdown\n"+open('qualification/C3-ITER4/ports.md').read()+"\n```\n")
out.append("\n## Donor sources again\n")
for label,p,a,b in [('port 3, Codex FOUNDATIONS 128-162 at 31f28f9',CODEX+'successor/standards/FOUNDATIONS.md',128,162),('port 4, Codex FOUNDATIONS 249-258 at 31f28f9',CODEX+'successor/standards/FOUNDATIONS.md',249,258),('port 1, Codex TRANSFORMATION_LIBRARY 93-112 at 31f28f9',CODEX+'successor/standards/TRANSFORMATION_LIBRARY.md',93,112),('port 2, Codex FOUNDATIONS 48-65 at 31f28f9',CODEX+'successor/standards/FOUNDATIONS.md',48,65),('port 5, Codex SKILL.md 18-39 at 31f28f9',CODEX+'successor/plugins/spec/skills/stdo-work/SKILL.md',18,39)]:
    out.append(f"\n### {label}\n\n```text\n{show('31f28f9',p,a,b)}\n```\n")
open('qualification/C3-ITER4/reviews/PORTS-PACKET-2.md','w').write(''.join(out)); print('PORTS-PACKET-2 bytes', sum(len(x) for x in out))
