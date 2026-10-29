# Exact failing owner-currentness excerpt from the executed inline operator recorder.
# Surrounding activation/source checks completed; setup effects after this excerpt did not run.
receipt=read(p/'owner-binding/RECEIPT.json');ticket=r/'.ai-workspace/tickets/active/T-013-practical-formal-gate.md'
assert sha(ticket)==receipt['ticket_after_sha256']=='c5c8ed56ebfef3f51406be4b63d7d1fd3976de294ce0a64c801ea3f4da44fefc'
assert sha(r/'stdo_a_c.json')==receipt['definition_sha256']
raw_owner=''.join(ticket.read_text().splitlines(keepends=True)[148:225]);owner=json.loads(raw_owner)
canonical=lambda v:json.dumps(v,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()
assert hashlib.sha256(canonical(owner)).hexdigest()==receipt['selected_json_sha256']
