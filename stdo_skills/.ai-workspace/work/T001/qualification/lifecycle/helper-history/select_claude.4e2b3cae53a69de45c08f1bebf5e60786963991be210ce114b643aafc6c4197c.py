"""Select the exact Root-selected repaired bundle for a prepared fixture."""
import argparse
import json
from pathlib import Path
from prepare_lifecycle import QUAL, PRODUCT, PYTHON, pin, save, sha

SELECTED = '42d246cbe2fcf1414b0fd7ed094be74d6f2607595525555caa52618d8999f79a'


def select(fixture_path):
    fixture=json.loads(fixture_path.read_text());assert fixture['tenant']=='claude'
    pkg=PRODUCT/'build_tenants/claude';assert sha(pkg/'INVENTORY.md')==SELECTED
    s=json.loads((QUAL/'selections/claude-automatic.json').read_text())
    helper=pkg/'skills/stdo-release-install/scripts/manage_install.py'
    checker=pkg/'tests/check_package.py'
    s.update({'lane':fixture['lane'],'standing':'Root selected exact repaired physical candidate for bounded trials; independent semantic readback and acceptance remain separate',
        'candidate_record':pin(pkg/'INVENTORY.md'),'install_documentation':pin(pkg/'INSTALL.md'),
        'tenant_root':str(pkg),'package_root':str(pkg/'skills'),
        'package_files':[{'path':str(p.relative_to(pkg/'skills')),'sha256':sha(p)} for p in sorted((pkg/'skills').rglob('*')) if p.is_file()],
        'fixture_record':pin(fixture_path),'timeout_ms':600000,
        'install_binding':{'kind':'claude-bundle-installer/1','action':'install','helper':pin(helper)},
        'install_checks':{'before':[{'argv':[str(PYTHON),'-I','-B',str(checker)],'dependencies':[pin(PYTHON),pin(checker),pin(helper)]}],'after':[]},
        'install_scope':'Complete five-skill bundle and its actual shipped installer receipt; no individual-skill sufficiency claim'})
    s.pop('documentation_gap',None)
    out=QUAL/'selections'/('claude-'+fixture['lane']+'.json');save(out,s);return out


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('fixture',type=Path);a=p.parse_args();print(json.dumps(pin(select(a.fixture.resolve()))))
