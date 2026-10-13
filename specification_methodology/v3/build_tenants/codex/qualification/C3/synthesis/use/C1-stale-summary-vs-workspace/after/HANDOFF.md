# Handoff
- src/limits.py: MAX_ITEMS = 100 (already present when this session started; the previous handoff's claim that it was still 50 was stale; MAX_BATCH = 10 unchanged)
- docs/limits.md: edit proposed to state 'Maximum items per request: 100' (batch size 10 unchanged)
- tests/test_limits.py: edit proposed to assert MAX_ITEMS == 100 (MAX_BATCH == 10 unchanged)
- Tests NOT run in this session (no execution capability). The previous 'passing' status is stale: before the test edit, inspection shows the test asserted 50 against a source value of 100.
- Remaining for TICKET-12: confirm the proposed docs/tests edits were applied, then run tests/test_limits.py. Closure stays open until both are observed.
