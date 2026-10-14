# Codex rebuild execution

Contract: EC-CODEX-SYN-01 in T-002-CODEX. Common input commit:
`bb76b1d0a158ff5b20c7fd2eb933f8ffc798160b`.

The design records ownership, contribution sources and affected dependency
closure. Construction starts with the core and uses disjoint bounded Writers
for deciding consumers. Writer outputs are candidates, not independent reviews.
Fresh reviews are run on frozen returns. Owner acceptance remains open.

Local limits: selected input at most 160000 bytes per bounded task, 40 minutes;
CLI trials at most 120000 input bytes, 15 minutes, USD 2 each, USD 30 aggregate.
No numerical limit is added to product law. If material scope exceeds an input
limit, split along a supported dependency boundary and record the further read.
