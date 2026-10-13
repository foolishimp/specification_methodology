# TASK: configure the remaining tide-table work

## Subject

Product `tide-tables` publishes a harbour authority's tide predictions for
three ports: North, East and South. The facts below are the whole subject.
The record is invented for this task and is evidence about no real product.

The product owner, Marta, admitted work item `W-12`: publish the 2027 tables
for all three ports. It states four requirements:

- R1: each port's harmonic constants are fitted from that port's 2026 gauge
  record, following the method notes.
- R2: each port's constants are assessed against that port's 2026 gauge
  record, following the method notes, by an assessor that is not the author
  of those constants. This happens before any table made from them is
  published.
- R3: every table gives heights relative to chart datum CD-2026.
- R4: the three ports are published together, by the holder of the
  publication grant.

Material, in bytes:

| Item | Bytes |
|---|---|
| 2026 gauge record: North, East, South | 70,000; 60,000; 50,000 |
| method notes (fitting and assessment) | 40,000 |
| constants, per port | 10,000 |
| port configuration `ports/<port>.yaml`, per port | 20,000 |
| table template | 15,000 |
| datum offsets `datum/cd2026.csv` (admitted by Marta) | 8,000 |
| task contract and result, per activation | 10,000 |

Dependencies:

- One port's constants depend only on that port's gauge record and the
  method notes.
- One port's tables depend only on its constants, its port configuration
  and the template.
- `north.yaml` and `south.yaml` declare CD-2026.

Actors:

- A1: an agent with a context capacity of 200,000 bytes. Its tools fit
  harmonic constants and compare them numerically with a gauge record.
- A2: an agent with a context capacity of 200,000 bytes. It has the same
  tools as A1, plus the table generator.
- A3: an agent with a context capacity of 64,000 bytes. It has the table
  generator and can edit configuration files. It cannot fit or assess
  constants.
- Ravi: an operations officer, a person. He holds the only grant to publish
  to the public portal and is available for one hour on Thursday.
- You: an agent with a context capacity of 120,000 bytes, and no fitting or
  table tools.

W-12 grants edits to `constants/`, `tables/` and `ports/*.yaml` to whichever
agent activation the configuration assigns to that work. Marta must accept
the configuration before it starts.

Last week Tomas ran a pilot for East only:

- A1 fitted East's constants and committed them as `east-c1`.
- A new A1 session, started with an empty context, compared `east-c1` with
  the 2026 East record. It returned `satisfied`, within 3 cm.
- A3 generated East's tables from `east-c1` and returned to Tomas the
  result `East tables: done, 0 errors`.
- The workspace log `tables/east/run.log` holds the line
  `WARN datum: east.yaml declares CD-2019; heights written relative to CD-2019`.
- Nothing has been done for North or South.

Tomas proposes this for the remaining work: "Use the setup we have used for
three years. A1 is Executive and holds the whole W-12 record. A2 is Writer
for all fitting and all tables. A3 is Reviewer. It is the optimal
configuration; the team knows it."

Marta asks you to propose a configuration for the remaining W-12 work.

## Instruction

1. Under a heading `Configuration`, list each activation, with:
   - its operation;
   - its actor;
   - its inputs, with their total bytes;
   - its result, and where that result goes.

   Then give the dependency order, what each exchange must carry, and who
   holds the authority for each effect, including publication.
2. Under a heading `Justification`:
   - say why this allocation fits the dependencies, the actors' capabilities
     and capacities, and R2;
   - say what you keep from the pilot;
   - judge Tomas's proposal, and his claim that it is optimal.
3. Under a heading `Check`, evaluate the predicate "the East tables from the
   pilot meet R2 and R3 and may be published". Give its result value, the
   facts that decide it, and anything you record as not performed.
4. Under a heading `No method source`, list anything the task needed that
   the METHOD block did not supply. Write `none` if nothing.

Return only those four parts, in that order. Do not restate the subject.
