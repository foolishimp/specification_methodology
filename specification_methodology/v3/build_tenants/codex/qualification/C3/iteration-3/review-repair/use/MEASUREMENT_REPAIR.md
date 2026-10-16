# Acquisition counter repair

The independent assessor found inconsistent intermediate cumulative byte
counts in all six attempts at `28e46fdd0d751f23f3ae93ea107d05efd393606d`.
Parallel reader processes each read the preceding event list, admitted their
own emission against that list, and appended independently. Each individual
emission remains recorded, but one process could miss another's emission in
its cumulative field. The same race could admit two reads whose combined
size exceeded the shared allowance. First-read time initialization also
belonged inside that shared operation.

The local POSIX reader now holds an operating-system file lock across initial
time selection, cumulative admission, append and emission. Process exit
releases ownership; an empty lock file does not retain a lease. This changes
qualification instrumentation only. The frozen method package remains
`ef5e514f5ffff4176b55ca687e56fe3c8b97efc1`.

[CONCURRENCY_CHECK.json](CONCURRENCY_CHECK.json) records two real competing
processes reading 512 bytes each against a 768-byte shared allowance. The
unlocked control admits 1,024 bytes with inconsistent counters. The repaired
entry admits one 512-byte read and refuses the other before emission, with
an exact cumulative count. The five ordinary refusal/read controls in
[READER_CHECK.json](READER_CHECK.json) also pass. The repaired reader SHA-256
is `3e9ce1f9e2a1ac032144d6456065a86bbe16e1594d48dcf20e7b991ec9371ebd`.

The six recorded attempts are unchanged and were not rerun. Summing their raw
`emitted_bytes` fields gives 606,512; 124,974; 132,755; 68,889; 73,153; and
251,057 bytes for T1–T6 respectively. Every sum is within its admitted
allowance, so this observation supplies no actual allowance violation and
does not change the answers. It does prevent using intermediate cumulative
fields as reliable admission evidence. The final measurement calls include
all prior logged events; their own emitted measurement bytes explain the
difference from each actor's pre-report total.

The frozen acquisition logs and answers retain their original reader hash.
The successor reader controls do not retroactively qualify those calls as
atomic. The independent assessor evaluates task results from the unchanged
answers and recorded raw events, with this measurement limitation retained.

`dispatch_recorded_utc` is the time the parent wrote a record after dispatch;
it is not an observed dispatch or task-start time. Reader elapsed values cover
the selected acquisition interval, not final response generation. Native
host/retained context, attention and spend remain unmeasured. The original
T2 execution has only its actor's returned attestation; an independent replay
of the retained construction establishes reproducibility, not an additional
original execution receipt.
