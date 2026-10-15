# Triage of R2b-2 (successor readback of the ported receivers) and batch 10

R2b-2 ran on Fable at max in a fresh context (`reviews/R2b2.json`, with
`reassess/batch-10.json`; 161,592 tokens, 12 minutes). Of the 13 R2b
findings, 11 are read back as repaired and 2 as partly: R2b-03 (the port
list's row 3 still described REFERENCE_FRAME §1 as the receiver of the
rule sentences) and R2b-12 (the positive reproductions wait for the
freeze, as scheduled). Six new findings, one repair round:

| Id | Disposition | Where |
|---|---|---|
| R2b2-01 | repaired: row 3 names two receivers, the rule's sentences in FOUNDATIONS §2 and the declaration in REFERENCE_FRAME §1; the cone table has a FOUNDATIONS entry for part 3 | CROSS_SYNTHESIS port list, cone table |
| R2b2-02 | repaired: Codex 141–144, 155–156 and 160–162 | CROSS_SYNTHESIS part 3 |
| R2b2-03 | repaired: the declaration states direction (from each source member to this context), loss (none) and the target context with its owning member, in one sentence, as the rule requires; it restates no other part of the rule | REFERENCE_FRAME §1 |
| R2b2-04 | repaired: the rows exception added to row 5's mode cell | CROSS_SYNTHESIS port list |
| R2b2-05 | repaired: the addition described as the receiver states it (placement at the entry section, instance premises first, imported families for a profile's table) | CROSS_SYNTHESIS part 1 |
| R2b2-06 | repaired: the gloss described as the receiver's (finite capacity as the bound on an actor's envelope, P0) | CROSS_SYNTHESIS part 2 |

Batch 10: `DESIGN_MODULE_METHOD.md#4` was `changed` because the binding
sentence had conditioned every preferred shape on practicality; "where it
is practical" is deleted, the one predecessor item keeping its own "where
practical". `STDO_REFERENCE_FRAME_BASELINE.md#closure` was `indeterminate`
only for condition 22's twelve families, enumerated in EXECUTIVE_BASELINE
§11; that section is now a named locus of the row. Both rows and the
repaired declaration go to one last readback (`reassess/batch-11.md`),
after which no further round runs: whatever stays `changed` becomes a
proposed replacement and whatever stays `indeterminate` is reported so.
