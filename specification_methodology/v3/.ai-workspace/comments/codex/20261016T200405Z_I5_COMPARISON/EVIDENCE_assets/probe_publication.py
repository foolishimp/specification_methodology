#!/usr/bin/env python3
"""Exercise the frozen Codex publication binding in a temporary archive only."""
import hashlib
import io
import json
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path
from acquire import ASSETS, REPO, record
from probe_evidence import CODEX, CX

def main():
    prefix=CX+'successor/'
    archive=subprocess.check_output(['git','archive',CODEX,prefix],cwd=REPO)
    with tempfile.TemporaryDirectory(prefix='ec-i5-evidence-') as directory:
        scratch=Path(directory)
        with tarfile.open(fileobj=io.BytesIO(archive)) as stream:
            for member in stream.getmembers():
                if member.isdir(): continue
                if not member.isfile() or not member.name.startswith(prefix) or '..' in Path(member.name).parts:
                    raise ValueError('Unexpected archive member')
                target=scratch/member.name
                target.parent.mkdir(parents=True,exist_ok=True)
                target.write_bytes(stream.extractfile(member).read())
        package=scratch/prefix
        invocation=[sys.executable,'-B',str(package/'interpretation/bindings.py'),'--theory-root','/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2']
        def run():
            p=subprocess.run(invocation,capture_output=True,text=True)
            return {'exit_code':p.returncode,'stderr':p.stderr.strip(),'stdout_sha256':hashlib.sha256(p.stdout.encode()).hexdigest()}
        positive=run()
        target=package/'standards/FOUNDATIONS.md'
        original=target.read_bytes()
        target.write_bytes(original+b'\nIndependent scratch perturbation.\n')
        source_negative=run()
        target.write_bytes(original)
        target=package/'interpretation/program.json'
        target.write_bytes(target.read_bytes()+b'\n')
        carrier_negative=run()
    result={'subject':CODEX,'package_prefix':prefix,'positive':positive,'source_byte_change':source_negative,'program_byte_change':carrier_negative,'limits':['Scratch cold binding and exact hash controls only; native checker projection was not rerun.','Full frozen package member matching is separately measured by probe_evidence.py.','No semantic fidelity, context fit, actual use, acceptance or release judgment follows.']}
    output=json.dumps(result,indent=2)+'\n'
    (ASSETS/'probe_publication.json').write_text(output)
    record('independent scratch publication probe',output,CODEX+':'+prefix)

if __name__=='__main__':main()
