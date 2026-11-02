import hashlib, json, pathlib, sys
root=pathlib.Path(__file__).resolve().parent
name=sys.argv[1]
if name not in {'direct','issuer','worker','bad-review','review'}: raise SystemExit(2)
a=json.loads((root/'admissions'/f'{name}.json').read_text())
p=root/a['contract']
actual=hashlib.sha256(p.read_bytes()).hexdigest()
valid=(a['authority']=='fixture-owner' and a['decision']=='admitted' and actual==a['contract_sha256'])
print(json.dumps({'contract':a['contract'],'contract_sha256':actual,'admission_sha256':hashlib.sha256((root/'admissions'/f'{name}.json').read_bytes()).hexdigest(),'decision':'admitted' if valid else 'rejected','mechanism':a['mechanism'],'authority':a['authority'],'cause':None if valid else 'exact contract digest mismatch'}))
raise SystemExit(0 if valid else 2)
