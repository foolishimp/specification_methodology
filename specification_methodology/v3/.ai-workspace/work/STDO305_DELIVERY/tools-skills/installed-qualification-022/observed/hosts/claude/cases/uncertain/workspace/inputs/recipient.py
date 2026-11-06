import hashlib,json,sys
from pathlib import Path
raw=sys.stdin.buffer.read(); target=Path(sys.argv[1])
target.mkdir(exist_ok=True)
(target/'received-stdin.bin').write_bytes(raw)
count=target/'count'; count.write_text(str((int(count.read_text()) if count.exists() else 0)+1))
body=json.loads(raw.split(b'\n',1)[1]); views=[p['views'] for p in body['projections']]
encoded=json.dumps(views,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
(target/'received-views.json').write_bytes(encoded)
print(json.dumps({'stdin_sha256':hashlib.sha256(raw).hexdigest(),'views_sha256':hashlib.sha256(encoded).hexdigest(),'count':int(count.read_text())}))
