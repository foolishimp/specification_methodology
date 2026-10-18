"""Bind the existing RC4 operations to the final repair's immutable inputs."""
import importlib.util
from pathlib import Path
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
TENANT = HERE.parents[3]
PRIOR = TENANT / 'qualification/C3/rc4/integration'
spec = importlib.util.spec_from_file_location('rc5_existing_operations', PRIOR / 'integrate.py')
selected = importlib.util.module_from_spec(spec)
spec.loader.exec_module(selected)
rc1 = selected.rc1
INPUTS = rc1.read(HERE / 'INPUTS.json')
selected.HERE, selected.PRIOR, selected.INPUTS = HERE, PRIOR, INPUTS
selected.operations.HERE, selected.operations.PRIOR = HERE, PRIOR
selected.operations.INPUTS = INPUTS
rc1.HERE, rc1.INPUTS = HERE, INPUTS

prior_conservation, prior_verify = selected.conservation, selected.verify


def conservation(args, context):
    prior_conservation(args, context)
    # The illustrative replacement is part of the existing RF-005 question.
    # Preserve both exact relations and their pending owner decisions.
    questions = rc1.read(HERE / 'REPLACEMENT_QUESTIONS.json')
    added = [q for q in questions['questions'] if q['id'] == 'RC5-WORKED-BINDING']
    owners = [q for q in questions['questions'] if any(
        r['relation']['id'] == 'RC1-CONSUMER-R002' for r in q.get('rows', []))]
    if len(added) != 1 or len(owners) != 1:
        raise ValueError('Expected one pending RF-005 replacement question')
    owners[0]['rows'].extend(added[0]['rows'])
    questions['questions'].remove(added[0])
    rc1.write(HERE / 'REPLACEMENT_QUESTIONS.json', questions)


def verify(args, context, build):
    prior_verify(args, context, build)
    inventory = rc1.read(HERE / 'CANDIDATE.json')
    inventory['kind'] = 'stdo.review-candidate'
    rc1.write(HERE / 'CANDIDATE.json', inventory)


selected.conservation, selected.verify = conservation, verify

if __name__ == '__main__':
    selected.main()
