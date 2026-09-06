"""Compute exact-output and custody observations; make no semantic judgment."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

HERE = Path(__file__).resolve().parent
PYTHON = '/private/tmp/stdo-rc5-installed-manager-20260906/bin/python'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def parse_final(text):
    value = text.strip()
    blocks = list(re.finditer(r'```(?:json)?[ \t]*\n(.*?)\n```', value, re.S))
    if len(blocks) == 1:
        block = blocks[0]
        return json.loads(block.group(1)), {'kind': 'single_fenced_json',
            'prefix': value[:block.start()].strip(), 'suffix': value[block.end():].strip()}
    return json.loads(value), {'kind': 'bare_json'}


def main():
    selection = json.loads((HERE / 'coverage-selection.json').read_text())
    observations = []
    for case in selection['contexts']:
        directory = Path(case['directory'])
        if not (directory / 'execution-result.json').is_file():
            observations.append({'context': case['name'], 'status': 'execution_incomplete'})
            continue
        result = json.loads((directory / 'execution-result.json').read_text())
        row = {'context': case['name'], 'execution_result_sha256': sha(directory / 'execution-result.json'),
               'exit_code': result['exit_code'], 'timed_out': result['timed_out'],
               'worksite_unchanged': not result['snapshot_changes'],
               'semantic_disposition': 'Not computed. Independent oracle assessment is required.'}
        try:
            final, presentation = parse_final((directory / 'final.txt').read_text())
            row['presentation'] = presentation
            required = {'delivery_decision', 'evidence_disposition', 'qualification_sequence',
                        'handoff_sections', 'joined_request'}
            row['required_fields_present'] = required <= final.keys()
            rows = final['handoff_sections']
            joined = final['joined_request']
            native = json.loads((Path(case['worksite']) / 'native-context.json').read_text())
            executable = Path(native['axiom_root']) / 'build_tenants/core/code/ac.py'
            argv = [PYTHON, str(executable), 'join', '--input', '/dev/stdin']
            source = json.dumps(rows, ensure_ascii=False)
            repeats = [subprocess.run(argv, input=source, capture_output=True, text=True, timeout=30)
                       for _ in range(2)]
            row.update(final_sha256=sha(directory / 'final.txt'), executable_sha256=sha(executable),
                       argv=argv, join_exit_codes=[r.returncode for r in repeats],
                       join_stderr=[r.stderr for r in repeats],
                       returned_join_matches_cli=all(r.returncode == 0 and r.stdout == joined for r in repeats),
                       repeated_cli_bytes_equal=repeats[0].stdout == repeats[1].stdout,
                       observed_join_sha256=hashlib.sha256(repeats[0].stdout.encode()).hexdigest(),
                       actual_native_invocation='Inspect retained raw tool trace independently; reproduction alone does not prove native use.')
            (directory / 'parsed-final.json').write_text(json.dumps(final, indent=2, ensure_ascii=False) + '\n')
            (directory / 'reproduced-join.txt').write_text(repeats[0].stdout)
        except (OSError, ValueError, KeyError, TypeError, subprocess.SubprocessError) as error:
            row['final_observation_error'] = repr(error)
        observations.append(row)
    report = {'candidate_revision': selection['candidate_revision'],
              'observer_sha256': sha(Path(__file__)),
              'scope': 'Computable output and custody facts only; repeated CLI calls do not repeat stochastic judgments.',
              'contexts': observations}
    (HERE / 'mechanical-observations.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
