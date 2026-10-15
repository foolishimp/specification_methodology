# Triage of R1, the source-first reading of three family tables

R1 ran on Fable at max effort in a fresh context (`reviews/R1.json`;
136,262 tokens, 12 minutes): 70 rows judged (EXECUTIVE_BASELINE 19,
DESIGN_MODULE 26, ODD 25), 11 rows with a `weak` or `defect` judgment,
14 findings (1 Medium, 13 Low), every `rule_link` `not_checked` as the
instructions required. One repair round by the Executive; every finding
repaired in the owning table. The rows stay author text until the
successor readback (I4-09).

| Id | Disposition | Where |
|---|---|---|
| R1-01 | repaired: the no-route reading is this profile's choice, named in the choice column, and P2 is applied to it | EXECUTIVE_BASELINE row 3 |
| R1-02 | repaired: F15, product lineage objects, imported in the preamble (eight families) and cited in the row | EXECUTIVE_BASELINE preamble, row 7 |
| R1-03 | repaired: the consequence ends at "outcome"; the three criteria are the profile's choice in the choice column | EXECUTIVE_BASELINE row 9 |
| R1-04 | repaired: P4b cited and used for the non-re-acquirability step; the unused P6 dropped | EXECUTIVE_BASELINE row 11 |
| R1-05 | repaired: F13 cited | EXECUTIVE_BASELINE row 12 |
| R1-06 | repaired: "derived from P0 and P6" and "derived from P0 and P2" in the seven rows | DESIGN_MODULE rows 2, 7, 8, 9, 10, 13, 17 |
| R1-07 | repaired: F18 imported in the preamble and cited in the row | DESIGN_MODULE preamble, row 1 |
| R1-08 | repaired: P3 cited for "one" | DESIGN_MODULE row 10 |
| R1-09 | repaired: the views claim is the row's instance premise; P2 cited for the projection duty | DESIGN_MODULE row 15 |
| R1-10 | repaired: P3 cited for "one owner", P6 kept for "no rival authority" | DESIGN_MODULE row 23 |
| R1-11 | repaired: P0 cited and each clause attributed | ODD row 1 |
| R1-12 | repaired: P3 cited for "exactly one" | ODD row 7 |
| R1-13 | repaired: P5 cited for "fails closed" | ODD row 8 |
| R1-14 | repaired: per-clause "By Pn … so" attributions written for the 18 rows named (1, 3, 4, 7, 8, 10 to 15, 17, 18, 21 to 25), from the premises each row already cited; no premise was added except those of R1-11 to R1-13 | ODD table |

Scope limit carried: the "Rule in this member" links were not followed
by R1; whether each linked section states the consequence remains
`unresolved` for all 70 rows.
