# Receiving and handling handoff — view A candidate

Fictitious test content only. Source identity: `urn:stdo-3:trial:codex:t1:handoff:v1`.
This candidate supplies receiving, handling and uncertainty instructions for
O1/O2/O4 from clauses S0–S5. All supplied batches start HOLD.

## Record before handling

Match and record the batch identity. Keep the original reading and its original
unit, the seal observation and the receipt time together. Retain raw data beside
every conversion. Record an actual receipt time when it becomes available; the
fixture supplies none. Do not use the Writer's run time as a receipt time, infer
a missing unit, or invent a signature.

A labelled F reading means Fahrenheit. Convert only a known F reading using
`C=(F-32)*5/9`. The permitted band is **2 through 8 C inclusive**
(`2 <= C <= 8`). A missing unit stays unknown and prevents a supported conversion.

## Supplied current batch record

| Batch | Original reading | Original unit | Seal | Conversion | Band / eligibility observation | Current status | Receipt time | Signed release decision |
|---|---:|---|---|---|---|---|---|---|
| A-17 | 41 | F | intact | (41-32)*5/9 = 5 C | In band; temperature eligible | HOLD | not supplied / unknown | none supplied |
| B-18 | 50 | F | intact | (50-32)*5/9 = 10 C | Outside band; not eligible | HOLD | not supplied / unknown | none supplied |
| C-19 | 41 | missing / unknown | intact | unknown; do not convert | Undecided because unit is unknown | HOLD | not supplied / unknown | none supplied |

The table records the supplied fixture facts. It does not establish that an
operator has physically received or verified a batch. Record any new actual
observation without replacing its raw preimage or presenting an inference as
an observed fact.

## Compare, hold and escalate

1. Confirm the correct batch identity and record its raw reading/unit, seal and
   receipt time. If a required fact is missing or facts conflict, record the
   unresolved fact, keep HOLD and seek human owner **Mira Finch's resolution**.
2. Convert only a reading with a known unit and compare the inclusive band.
   Record the conversion, HOLD/eligibility observation and unresolved facts.
   A-17's 5 C is temperature eligibility only. B-18's 10 C is outside the band.
   C-19's bare 41 has no supported C value.
3. Before RELEASE, require the conjunction of **correct batch identity, known
   in-band temperature, intact seal, AND Mira Finch's signed decision for that
   same batch**. Obtain and retain that decision before release. A check or
   eligibility label does not grant the owner's decision.
4. Outside-band, unknown or conflicting facts, a missing decision, or another
   unresolved release requirement keep the batch HOLD. Seek Mira's resolution.
   Do not guess, ship, supply a signature, or override a requirement. A signed
   decision alone cannot override outside-band or unknown facts.

These instructions grant no release decision to their author. All three
supplied batches remain HOLD at this return.

## Provenance and unfinished outer responsibility

Deciding acquisition: `qualification/T1/views/A.txt`, S0–S5, **1042 bytes**,
SHA256 `54fce1a53e7b69d44090961131a767bcbc4cd17e7768e39bff2d06a06a9116f5`.
The full source digest declared by custody is
`e338f776d73ea41f9b9e53b157c5d9680ac4b8b36ec121f7fe4713a8bc12c065`;
its full body was not acquired.

The complete outer obligations remain O1–O6. O3's release-authority gate is
retained here through S4, while the signed human decision remains absent.
O5/O6 receive local provenance and effects in [RETURN.md](RETURN.md). Deciding
S6 recovery and S7 effects were not acquired; no instructions from those
clauses are invented. Their remaining responsibilities and whole-task
compatibility/coverage stay with the coordinator. This partial authored
candidate requires the frozen assembled candidate's independent assessment
and the existing owner's disposition before it can be accepted.
