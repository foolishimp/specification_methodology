# R1: source-first reading of three family tables

You are a same-family (Claude) nonauthor reviewer with no context beyond
this file and `FAMILY-PACKET.md`. Read only those two files.

The packet gives, verbatim: FOUNDATIONS §3 Commitments (the commitments
P0 to P6 and the standing of each), FOUNDATIONS §3 Foundation to law (the
format every family table follows), and the family tables of
EXECUTIVE_BASELINE, DESIGN_MODULE and ODD.

For every row of the three family tables judge:

- `premises`: does each cited commitment exist in FOUNDATIONS §3, and is
  the standing written in the row the standing FOUNDATIONS §3 gives it
  (P0 recovered; P1, P2, P3, P4a, P6 independent; P4b derived from P0 and
  P2; P5 derived from P0 and P6)? Instance premises must be labelled as
  such; imported families must be labelled as imported. Answer `ok`,
  `defect` (say which premise) or `unclear`.
- `follows`: does the consequence follow from the cited premises by the
  inference the row states ("By … so …")? Answer `ok`, `defect` (say why
  it does not follow, in one sentence) or `weak` (it follows only with an
  unstated premise; name it).
- `policy`: is every added domain or policy choice in the row labelled as
  a choice with an owner, and never presented as a consequence of the
  commitments? Answer `ok`, `defect` or `none` (no choice in the row).
- `pillar`: does the Pillar cell name a pillar or say none? Answer `ok`
  or `empty`.
- `rule_link`: `not_checked` for every row (the linked sections are not in
  your packet). Do not guess.

Return one JSON file at the path the activation names:

```json
{"review": "R1", "reviewer": "sonnet, same-family nonauthor, fresh context",
 "tables": [
   {"member": "EXECUTIVE_BASELINE", "rows": [
     {"row": 1, "premises": "ok", "follows": "ok", "policy": "none", "pillar": "ok", "rule_link": "not_checked", "note": ""}
   ]}
 ],
 "findings": [
   {"id": "R1-01", "member": "...", "row": 3, "severity": "High | Medium | Low", "what": "<one sentence>", "quote": "<at most 25 words>", "smallest_repair": "<at most 30 words>"}
 ]}
```

Number rows in the order they appear in each table, starting at 1. Every
row must appear exactly once. Write nothing else anywhere. When done,
print the counts per member of rows with any `defect` or `weak`.
