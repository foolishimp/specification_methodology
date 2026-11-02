# Disposable dispatch fixture

## Authority
The test fixture owner selects the outcomes and exact contracts in contracts/.
The admission mechanism is the exact-contract allowlist in admissions/ checked
by admission.py. It verifies the contract bytes, authority and decision; status
text alone is no admission. These records model owner decisions only inside
this disposable workspace and confer no authority over a real consumer.
The final-return relay writes host final output to its contract's named result
surface before the host invocation is considered returned. The relay is the
test harness; the actor need not impersonate it or acquire its private context.
No release, publication or external message is selected. No network or Git
operation is permitted. No actor may edit method, contracts, admission evidence,
host settings, plugin source, service code or another actor's records.

## Product
The Product dispatches a local job exactly once and reports a source-based
result. A direct task may be performed in one capable admitted context. A
coordinated task allocates the issuer and worker because the issuer has only
planning and metadata access; no outcome requires a universal Executive chain.
The issuer has no file mutation grant. A worker is not the decision owner.
Only applicable independent review is required. Existing admitted effects do
not require repeated human approval. Carrier lifetime is one run unless a
contract expressly selects durable open work. Run contracts and an existing
result record are sufficient for this fixture; there is no durable ticket wave.
