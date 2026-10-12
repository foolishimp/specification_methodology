# TASK B: triage an incoming bug report

## Subject

Product `meter-reports`: a service that produces monthly electricity usage
reports for business customers. The facts below are the whole subject; the
record is invented for this task and is evidence about no real product.

Incoming report `BR-512`, filed by customer support on 2026-10-10 and
entered in the tracker as ticket `T-901` with `type: bug` and no other
triage field: "The October usage report for tenant `acme-berlin` shows
0.00 kWh for the first two hours of 1 October. The customer's own meter
display shows consumption during those hours. The customer's site is in
Europe/Berlin."

Product definition (current, owner Ines, product owner): `meter-reports`
serves tenants in the time zones UTC, Europe/Berlin and America/Chicago;
each tenant record carries its time zone.

Requirements on file for monthly reports (owner Ines). The set consists of
exactly these three:

- R-20: "The monthly usage report lists consumption per calendar day for
  the reporting month."
- R-21: "Report values are in kWh rounded to 0.01."
- R-22: "Reports are generated on the 2nd of each month at 03:00 UTC."

Accepted design (owner Karl, design owner), accepted 2026-06-02 against
R-20 to R-22:

- D-20: "The report job groups meter readings by `date(reading_ts)`, where
  `reading_ts` is stored in UTC."

Realisation and evidence:

- `report.py` at commit `e5d0aa31` implements D-20; code review note
  `CR-77` records that the grouping matches D-20 line for line.
- Test `test_group_by_day` passes on a fixture whose readings are all
  timestamped in UTC (CI run 9012 on commit `e5d0aa31`).
- The readings for `acme-berlin` between 2026-09-30T22:00Z and
  2026-10-01T00:00Z are present in the database and non-zero; the September
  report for `acme-berlin` lists them under 30 September.

Release: the current release `3.4` has the declared scope "report
formatting changes only"; Ines owns the release plan.

Current time for this triage: 2026-10-12T10:00Z.

## Instruction

1. Under a heading `Determinations`, give the six determinations of intake
   triage for `BR-512`, each marked C, J or O as the METHOD block defines
   them.
2. Under a heading `Upward walk`, walk upward from the affected behaviour
   one layer at a time, saying for each layer what the subject shows and
   whether that layer governs the behaviour and suffices, and say where the
   walk stops.
3. Under a heading `Class and re-entry`, give the change class, the
   re-entry point, the layers the change flows through, and the owner who
   is re-entered.
4. Under a heading `Triage metadata`, give the triage fields ticket `T-901`
   must carry, with their values.
5. Under a heading `No method source`, list anything the task needed that
   the METHOD block did not supply; write `none` if nothing.

Return only those five parts, in that order. Do not restate the subject.
Do not propose a fix.
