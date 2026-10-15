# R2b: readback of the ported contributions

You are a same-family (Claude) nonauthor reviewer with no context beyond
this file and `PORTS-PACKET.md`. Read only those two files. The packet
holds, for each of six parts ported at iteration 3 from the Codex
candidate at `31f28f9` and for three adaptations made at iteration 4 from
the Codex candidate at `d490dd6`: the source text at the donor commit, the
receiving text of this candidate, and the Writer's own record of what was
ported and how it was adapted. The Writer's record is an input to your
comparison, never its evidence.

Under the ratified common text a received contribution keeps its author
(the Codex tenant); you are the receiving line's same-family nonauthor
reviewer, and this reading is the independent assessment the line owes
for each port. For each of the nine items judge:

- `fidelity`: `verbatim` (the receiving text copies the source byte for
  byte where the record says verbatim), `adapted_as_recorded` (every
  difference between source and receiver is one the record names, with
  the reason the record gives), `adapted_beyond_record` (name each
  difference the record does not name), or `not_comparable` (say why).
- `owner`: does the receiving text live in exactly one owning section or
  instrument, with no link to `build_tenants/codex/` and every term
  resolved in this candidate? `ok` or `defect`.
- `meaning`: does the adaptation keep the determination the source made
  (what it requires, permits, prohibits, and when), or change it? `kept`,
  `changed` (say how), or `instrument` (the item is a tool, not law).
- For the three I4 adaptations (C3, C4, C5): does the receiver do what
  the record says and nothing more? `as_recorded`, `less` or `more`, with
  one sentence.

Return one JSON file at the path the activation names:

```json
{"review": "R2b", "reviewer": "sonnet, same-family nonauthor, fresh context",
 "items": [
   {"item": "port 1", "fidelity": "adapted_as_recorded", "owner": "ok", "meaning": "kept", "note": "<at most 40 words>"}
 ],
 "findings": [
   {"id": "R2b-01", "item": "port 3", "severity": "High | Medium | Low", "what": "<one sentence>", "quote": "<at most 25 words>", "smallest_repair": "<at most 30 words>"}
 ]}
```

Items are `port 1` to `port 6`, `C3`, `C4`, `C5`. Write nothing else
anywhere. When done, print one line per item with its three judgments.
