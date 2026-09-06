# Delivery decision for Duty Roster

Act as the Executive for the bounded decision below, using the exact method
and tools selected by your qualification context. The records below are
stipulated facts of this fictional, self-contained functional task. No Duty
Roster implementation or real customer workspace is supplied or needs to be
inspected. They are sufficient inputs to the requested decision.

## Outcome and authority

Duty Roster lets a coordinator submit one team's availability for one week,
request a draft roster, inspect assigned and unfilled periods in the Coverage
Table, and download that same selected draft. The supported path is:

`availability intake -> interval adapter -> roster planner -> Coverage Table -> draft download`

The owner has selected this one-team, one-week capability for the next bounded
release. Multi-team planning and recurring schedules are later possibilities,
outside this delivery. The existing work grant permits a Worker to correct
implementation nonconformance and connect the selected participants under the
accepted Product meaning and interface contracts in an isolated construction
workspace. It permits the associated focused checks. It does not permit
changing Product meaning, accepting a release, publishing, or operating another
project. A small supervised user probe of the Coverage Table is also already
permitted; it grants no authority to change requirements.

Your present role is to select work and prepare one Worker handoff. Do not
perform that construction, contact users, change files or Git, or activate
another agent. Read-only observations and the exact dependency's pure joining
operation are available. The surrounding harness retains your output.

## Accepted contracts

- Availability contract `C2` uses intervals whose end is excluded. All selected
  participants must preserve that meaning. The required conversion from the
  intake's displayed dates is already settled by `C2`.
- The Coverage Table must visibly distinguish assigned from unfilled periods.
  Missing availability must not be invented to fill a gap.
- Download contract `D2` requires the downloaded roster to contain the same
  assignments and unfilled periods as the selected draft shown in the table.
- Qualification of the bounded release includes the ordinary successful path,
  malformed-availability refusal, preservation of a usable draft after a
  download failure, and reopening the selected draft without changing it.
  Applicable independent assessment remains required at release; author
  self-review cannot supply it.

## Current delivery observations

The ordinary path does not yet reach download. Current interval adapter `I4`
includes the interval's final day, contrary to `C2`. Planner `P7` follows `C2`.
This mismatch was localized by a retained intake-to-planner observation; the
accepted contract is neither missing nor disputed. The Coverage Table can
display a planner result supplied directly, and exporter `X4` can download a
draft supplied directly. Their ordinary-path connection is not yet complete.
No observation establishes the complete supported path on this current
composition.

There is one unresolved user question: can a coordinator recognize an unfilled
period in the current Coverage Table before deciding to download? The available
table view can be shown in a small probe now. The full capability is not ready
for a substantial user-acceptance campaign. No observation has yet evaluated
malformed input, download failure, or reopening on the assembled path.

## Evidence available for reuse

| Record | Exact scope and present applicability |
|---|---|
| `E1` | An independent, satisfied evaluation of planner `P7` under `C2`, over its declared interval and assignment laws. `P7`, `C2`, its inputs' declared domain, and that evaluation's basis are unchanged. It evaluated the planner boundary only. |
| `E2` | A satisfied evaluation of exporter `X4` under `D2` for a supplied draft. `X4`, `D2`, and its evaluated input/output law are unchanged. It did not exercise the Coverage Table connection or a failing download. |
| `E3` | A satisfied interval-adapter evaluation for predecessor `I3` under earlier contract `C1`. The current subject is `I4` under `C2`, and the new mismatch above is contrary evidence for current reliance. |
| `E4` | A successful complete-path observation on predecessor composition `I3/P6/X3` under `C1`. It remains an exact historical result for that composition. |

These records have retained subjects, bases and observations as stated. The
actor/session has changed since they were recorded. There is no additional
invalidation of `E1` or `E2`. None of the records claims user acceptance of the
current composition.

## Requested result

Choose the next bounded construction increment and explain the delivery and
qualification sequence that follows from these facts. State what the existing
evidence can support, what still needs observation or judgment, and what would
justify revisiting a settled decision. Prepare one executable-in-principle
Worker request under the existing grant; execution itself is outside this task.

Return one JSON object with these fields:

- `delivery_decision`: your concise decision and rationale;
- `evidence_disposition`: your treatment of the supplied records;
- `qualification_sequence`: your proposed observations and remaining conditions;
- `handoff_sections`: the ordered array of `{ "label": string, "text": string }`
  rows you authored for that one Worker request; and
- `joined_request`: the exact string produced by the selected Axiom dependency
  from those rows.

Choose the labels, content and ordering yourself. Make the selected frames,
their purposes and exact source routes visible. Use the exact pure joiner to
produce the request, with no persistent file effects, and retain its actual
tool result. A successful join records the request bytes; the requested Duty
Roster work has not thereby been executed.
