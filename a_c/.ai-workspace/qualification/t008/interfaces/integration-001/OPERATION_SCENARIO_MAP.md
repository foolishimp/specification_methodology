# Mechanical operation/scenario evidence

The exact JSON map lists named executed controls, retained durable request/result envelopes and each operation's unexecuted variants. Source mentions locate tests; they are not branch-coverage claims.

| Operation | FD requirement | Distinct retained operation envelopes | Available statuses |
| --- | --- | ---: | --- |
| checks.evaluate | REQ-AC-FD-010 | 23 | ok |
| context.assemble | REQ-AC-FD-005 | 0 |  |
| contract.preflight | REQ-AC-FD-006 | 3 | refused |
| dispatch.cancel | REQ-AC-FD-007 | 0 |  |
| dispatch.observe | REQ-AC-FD-007 | 0 |  |
| dispatch.start | REQ-AC-FD-007 | 0 |  |
| events.wait | REQ-AC-FD-007 | 0 |  |
| evidence.read | REQ-AC-FD-003 | 8 | ok, refused |
| graph.project | REQ-AC-FD-003 | 0 |  |
| records.find | REQ-AC-FD-003 | 0 |  |
| records.read | REQ-AC-FD-003 | 0 |  |
| refresh.prepare | REQ-AC-FD-012 | 3 | ok |
| relations.query | REQ-AC-FD-004 | 1 | ok |
| resources.aggregate | REQ-AC-FD-013 | 0 |  |
| results.conjoin | REQ-AC-FD-010 | 0 |  |
| return.capture | REQ-AC-FD-008 | 0 |  |
| return.check | REQ-AC-FD-008 | 0 |  |
| review.prepare | REQ-AC-FD-009 | 0 |  |
| source.read | REQ-AC-FD-003 | 10 | ok, refused |
| tools.describe | REQ-AC-FD-001 | 11 | ok, refused |
| work.project | REQ-AC-FD-011 | 1 | ok |
| work.write | REQ-AC-FD-011 | 1 | ok |
| workspace.observe | REQ-AC-FD-002 | 9 | ok |

All 242 tenant tests passed with no skips, joined strict typing passed9files, and the separate pinned actual upstream trial passed9checks. Fixtures support no actual model usability or semantic acceptance claim. Real actor calls and every input/role/host/failure variant outside the named controls remain unperformed.
