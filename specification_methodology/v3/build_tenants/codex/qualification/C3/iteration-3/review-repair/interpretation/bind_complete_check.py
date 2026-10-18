"""Bind completed native mechanics to an unchanged frozen complete package."""
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
Q = HERE.parents[1]
sys.path.insert(0, str(Q))
spec = importlib.util.spec_from_file_location('check_interpretation', Q / 'check_interpretation.py')
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)
build = check.build
DOC = '2476713d315c00ac61d336a3281d67e4a384d4ce'
PACKAGE = 'ef5e514f5ffff4176b55ca687e56fe3c8b97efc1'
PROOF = Q / 'a_c/current/checks/20261014T173301.151017Z/MECHANICAL_RESULT.json'


def main():
    prior = build.read(PROOF)
    check.require(prior['valid'] and prior['package_unchanged'], 'Native proof did not complete on a stable subject')
    check.require(prior['document_source_input_commit'] == DOC, 'Native proof names another documentary source')
    check.require(check.package_inventory(DOC) == PACKAGE, 'The complete package is not the selected freeze')
    for path, key in [(build.OUTPUT / 'program.json', 'program_sha256'),
                      (build.OUTPUT / 'map.json', 'map_sha256'),
                      (build.OUTPUT / 'source-account.json', 'semantic_account_sha256'),
                      (build.ACCOUNT, 'account_sha256'),
                      (Path(build.__file__), 'generator_sha256'),
                      (Q / 'check_interpretation.py', 'checker_sha256')]:
        check.require(build.sha(path.read_bytes()) == prior[key], 'Changed proof premise: ' + str(path))
    current, _ = build.semantic_projection(build.read(build.ACCOUNT))
    build.validate_account(current)
    check.assert_compilation(current, build.read(build.OUTPUT / 'program.json'), build.read(build.OUTPUT / 'MAPPING.json'))
    result = {'valid': True, 'document_source_input_commit': DOC,
              'complete_package_input_commit': PACKAGE,
              'account_input_commit': prior['account_input_commit'],
              'native_proof': str(PROOF.relative_to(Q)),
              'native_proof_sha256': build.sha(PROOF.read_bytes()),
              'account_sha256': prior['account_sha256'],
              'program_sha256': prior['program_sha256'], 'map_sha256': prior['map_sha256'],
              'complete_inventory_sha256': build.sha((Q / 'CANDIDATE.json').read_bytes()),
              'relationship': 'Exact unchanged package, account and checker/generator; prior native controls and cold relocation apply to this frozen package.',
              'limits': prior['limits']}
    (HERE / 'COMPLETE_PACKAGE_BINDING.json').write_bytes(build.json_bytes(result))
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
