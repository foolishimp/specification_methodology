import json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent/'checker/scripts'))
import formal_gate
base=Path(__file__).resolve().parent
try:
 result=formal_gate.verify(json.loads((base/'request.json').read_text()),base/'api-evidence')
 print(json.dumps({'returned':result}))
except Exception as exc:
 print(json.dumps({'escaped_exception':type(exc).__name__,'message':str(exc)}))
