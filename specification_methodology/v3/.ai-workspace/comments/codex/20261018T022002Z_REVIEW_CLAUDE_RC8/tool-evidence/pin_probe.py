"""Verify the original RC8 artifact pins from immutable source A."""
import hashlib
import json
from pathlib import Path
import re
import subprocess

repo=Path('/Users/jim/src/apps/specification_methodology')
a='9aee01ffa76cfbde1a6b8f1153a25bd6d71c216e'
prefix='specification_methodology/v3/build_tenants/claude/a_c/i3/'
def blob(name): return subprocess.check_output(['git','-C',str(repo),'show',a+':'+prefix+name])
rows=re.findall(rb'^\| `([^`]+)` \| `([0-9a-f]{64})` \|$',blob('README.md'),re.M)
results=[]
for name,pin in rows:
    value=blob(name.decode());actual=hashlib.sha256(value).hexdigest()
    results.append({'path':name.decode(),'pin':pin.decode(),'actual':actual,'matches':actual==pin.decode(),'bytes':len(value)})
assert len(results)==16 and all(x['matches'] for x in results)
report={'source_A':a,'pin_count':len(results),'all_match':True,'members':results}
Path(__file__).with_name('pin-receipt.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='members'}))
