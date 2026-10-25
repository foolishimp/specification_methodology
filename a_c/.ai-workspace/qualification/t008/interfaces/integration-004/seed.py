"""Adapt only the prior evidence harness to this newly granted frozen cut."""
from pathlib import Path

D = Path(__file__).resolve().parent
prior = D.parent / "integration-003"
text = (prior / "prepare.py").read_text()
replacements = {
    'PRIOR = HERE.parent / "integration-002"': 'PRIOR = HERE.parent / "integration-003"',
    'qualification/t008/code-review-repair-001/implementation-001': 'qualification/t008/code-review-repair-002/implementation-001',
    '5395fd2947157541255168c6a1235136df64e9197d5032b25b31a0f071a4fe74': '842f3f136478b6948196fdd431f207f236c8c3e6ebb5573503726061c5d7bcc5',
    '36f75671b9dbce14e5f06811e180b662deb635b37921695668337466ace9bf25': '23dfafb2d7177d64287fc22002ec039ecc451d03c864a647f3c2deade7b2145c',
    '6b1ce2819e0e96aad32fb87feccb3aeaee1cd37a85c91aa4e1b693b9a15dd709': 'c2ff9be121ee7ccdf6974e257c0d3f0e86b6f92c84a7020d5f2b1f632cd0530f',
    '4c96735d16f6dd67d24b89fb5a6b5b7bdc376de13d8c98c14b833ce346c0662e': 'd944ba73369d3c672ba1b830419260f239d8d1bbfdc6558461412ae1f8978dda',
    '7722ddcbc48ab7dd48e824ccdbec320f30e80dc3b63c0881564ff7ed97ee3450': '597f33aae147fdc0ecc7c85638bf77615a59b856f6ee4ffe65041d1e9b82ef9e',
    '8a09b5a3397a5dc33ba5729ee60be6dcfb53b279ddd5cc52244c2f7018d33c31': '0d1634816568b13986b8a5821d9136df163e9012a1a851e235a26f6560b301f4',
    '17952e1521b247a1b1cb5eee5dc531a1c5a5afab4b2e3b44e4c7927e0ad079dd': 'dd738980b592ef7fb516df984fff9f5b679c53602f7c2cd504c88058fc174a0f',
    'invariance["write_files"]': 'json.loads((AUTHOR / "CANDIDATE.json").read_bytes())["files"]',
    'T008 integration003 closed code-review-repair001': 'T008 integration004 closed code-review-repair002',
    'runs/004-final-selected/execution.json': 'runs/003-final-focused/execution.json',
    '"six_author_snapshots_match"': '"five_author_snapshots_match"',
}
for old, new in replacements.items():
    assert old in text, old
    text = text.replace(old, new)
# In the prior source, these strings are replacements applied to an older runner.
# This predecessor runner is already the integration003 one.
text = text.replace("runner = runner.replace('\"T008 successor002 closed Core/HOW/T008\"', '\"T008 integration004 closed code-review-repair002\"')",
                    "runner = runner.replace('\"T008 integration003 closed code-review-repair001\"', '\"T008 integration004 closed code-review-repair002\"')")
text = text.replace('source_paths |= {ROOT / x for x in required}',
                    'source_paths |= {ROOT / x for x in required}\nsource_paths |= {ROOT / x["path"] for x in invariance["readonly_guards"]}')
text = text.replace('ROOT / "a_c/.ai-workspace/qualification/t008/code-review-repair-001",',
    'ROOT / "a_c/.ai-workspace/qualification/t008/code-review-repair-001",\n    ROOT / "a_c/.ai-workspace/qualification/t008/code-review-repair-002",\n    HERE.parent / "integration-002",')
text = text.replace('    "harness_only_adaptation":', '    "standalone_upstream_rerun_selected": False,\n    "harness_only_adaptation":')
with (D / "prepare.py").open("x", encoding="utf-8") as stream:
    stream.write(text)
