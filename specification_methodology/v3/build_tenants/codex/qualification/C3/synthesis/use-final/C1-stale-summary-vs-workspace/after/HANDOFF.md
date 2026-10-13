# Handoff
- src/limits.py: MAX_ITEMS = 100. This was observed already present on resumption, although the previous handoff said it was unchanged at 50. It was not re-edited. MAX_BATCH = 10 is unchanged.
- docs/limits.md: edit proposed to state 100 items per request. MAX_BATCH 10 is unchanged.
- tests/test_limits.py: edit proposed to assert MAX_ITEMS == 100. MAX_BATCH 10 is unchanged.
- Test status: not run in this session, because no execution tools were available. The earlier 'passing' note is stale. Before these edits, the test asserted 50 while src held 100, so it would have failed.
- Remaining for TICKET-12: confirm the proposed edits were applied, then run tests/test_limits.py. The ticket specifies no independent review or reserved acceptance.
