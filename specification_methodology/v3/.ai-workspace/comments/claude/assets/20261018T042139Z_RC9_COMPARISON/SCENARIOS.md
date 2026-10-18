# Ten scenarios for a route walkthrough

Each scenario is a concrete situation an actor faces while using the method. For each one, enter the
candidate at the entry named, follow only declared routes (links, sections the text names explicitly, a
frame's source lines), and record what the text decides for this situation and where. Do not search the
corpus for words while tracing; a decision you can reach only by search is recorded as "not reachable by
route" and then located by search so it can still be judged.

The entry for every scenario except S5 is the candidate's `standards/README.md`.

S1. A user of a product built with the method reports "the export produces a CSV with the wrong totals".
The team labels the report "bug". It is not yet known whether the code computes totals wrongly, whether the
requirement states the totals rule ambiguously, or whether the user misread the screen. Task: how does this
report enter work, what is decided first, and what repair, if any, is permitted at intake?

S2. An actor resumes a task after a restart. Its retained summary says "migration step 3 succeeded; tests
passed". The current workspace shows step 3's output file present but truncated, and step 4's input depends
on it; whether an external write made in step 3 completed is unknown. Task: what does the actor do before
continuing, and what happens to the summary's claims?

S3. A team builds a feature using only operations its declared calculus admits; every step's check passes;
the delivered behaviour fails the product's stated acceptance condition (response under 200 ms at the
declared load). Task: what has the team established, and what may it claim?

S4. A realisation fails a requirement. A contributor proposes editing the requirement's threshold from
200 ms to 400 ms so that the current realisation passes, and marks the failing test as resolved. Task: is
the edit permitted, by whom, what follows downstream, and what happens to the failing result?

S5. Entry: the candidate's frame (under `standards/frames/`) whose stated task covers evaluating and
reusing results; choose it from the frames' task statements and say which you chose. A governing
requirement changed (a field became mandatory). The expected answers of the test suite and the acceptance
evidence recorded for the previous version are unchanged and are about to be reused for acceptance. Task:
what must happen to the expected answers and to the evidence before acceptance?

S6. A product's Product definition says every export is time-stamped in UTC. Its requirements say nothing
about time zones. In use, exports carry local time. The project's direction and scope are unchanged; nobody
proposes a new goal. Task: what kind of discrepancy is this, at which layer does the work re-enter, what is
changed there and downstream, and may a code patch alone close it?

S7. A team realises a product's requirements entirely as a human process: people, a shared document of
current records, and direct observation. No software is written and no event history is kept. An assessor
must decide whether this realisation conforms. Task: what does the method require the assessor to examine,
and can the absence of code or of a replayable event history by itself fail the realisation?

S8. A checker must decide whether a system's output number is even. Its only observation is an
authenticated parity bit of that output (0 for even, 1 for odd), so it cannot tell 2 from 4 or 1 from 3.
Task: may the checker return a sound satisfied or falsified judgment from this observation, or must it
acquire more evidence, narrow its scope or return indeterminate? Answer also for an observation that is
the same constant whatever the output.

S9. The required answer is 10 and the realisation returns 10. The scenario's decoder is broken and records
1, so the scenario reports a failure. Nobody has yet checked the decoder. Task: what does the reported
failure establish about the realisation's actual behaviour, what does it not establish, and how is the
cause located?

S10. A restated member of a method has passed its review. One of its predecessor claims is marked
superseded with a proposed replacement; the reviewer says the replacement is clear and well argued. No
owner has recorded a decision on that replacement. Task: may the member be accepted, may a release
candidate that includes it be published as accepted, and who decides?
