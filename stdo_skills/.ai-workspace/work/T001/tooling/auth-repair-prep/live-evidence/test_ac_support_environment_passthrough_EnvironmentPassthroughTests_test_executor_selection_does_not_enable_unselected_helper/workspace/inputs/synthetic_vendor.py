import json,os,socket,sys
sys.stdin.buffer.read()
value=os.environ.get("CLAUDE_CODE_OAUTH_TOKEN")
with socket.create_connection(("127.0.0.1",int(sys.argv[1])),timeout=3) as connection:
 connection.sendall(b"0" if value is None else b"1"+value.encode())
 connection.shutdown(socket.SHUT_WR)
if value is None:
 print(json.dumps({"type":"result","subtype":"error","is_error":True,"error":"authentication_failed","result":"Synthetic credential missing","total_cost_usd":0}))
 raise SystemExit(1)
print(json.dumps({"type":"result","subtype":"success","is_error":False,"result":json.dumps({"schema":"a_c.fd-support.closed-return/1","opaque":"synthetic transport only"})}))
