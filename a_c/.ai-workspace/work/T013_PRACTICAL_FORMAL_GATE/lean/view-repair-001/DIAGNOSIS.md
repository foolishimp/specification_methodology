# View proof diagnosis under the fixed limit

The original public request remains incomplete at GateViews. It selected the
same full 1,987-record, 3,995-edge model, seeds [182, 278], 27 discovery steps,
29 retained records and budget 29. The first six generated modules succeeded;
GateViews exited -6 after 13.031402 seconds with interpreter memory exhaustion.
No model-defect or successful verification conclusion follows from that result.

Exactly three diagnostic compiler invocations used the retained GateModel and
its existing compiled dependencies, -j 1, -M 4096, a 90-second bound, and kernel
checking enabled. No whole gate, generic support or Mathlib replay was run.

| Probe | Observed result | Whole probe seconds | Child high-water field, bytes |
| --- | --- | ---: | ---: |
| ProbeWitness | Exited -6 with interpreter memory exhaustion; included seed/set/range obligations before Witness | 15.672989 | 4,295,131,136 |
| ProbeClosed | Closed theorem kernel-checked and ordinary axiom audit printed; file exited 1 for marker typing errors | 6.043066 | 2,557,329,408 |
| ProbeDecomposed | Compiled; numeric-bound transport and the original trace-range subset decision both passed | 1.325667 | 1,004,634,112 |

The first two files contain a diagnostic instrumentation defect: the IO marker
was inferred at BaseIO and did not typecheck. Their source, logs and unsuccessful
module outcomes remain intact. Probe 1 therefore does not establish a reliable
command boundary or isolate Witness. Its absent second marker cannot be used as
proof of which preceding command exhausted memory. Probe 2 explicitly prints
the successfully checked Closed theorem and its ordinary axiom set, but no valid
complete module is claimed for that file.

Probe 3 uses an explicitly IO-typed marker and compiles a complete module. It
checks seed nonemptiness, trace-set equality, numeric bounds, numeric-bound
transport to the exact universe subsets, and finally the original
`traceSet seeds trace ⊆ Finset.range 1987` kernel decision. All audits contain only
propext, Classical.choice and Quot.sound. This does not support a range-only
repair. Closed is also individually dischargeable within the limit.

The remaining leading hypothesis is the monolithic Witness existential search
or its cumulative interaction with the other CertificateValid decisions. It is
not an isolated allocator root-cause result. Model.dependencies recomputes a
filterMap over all 3,995 edges for a candidate parent; Witness searches a growing
known set. The trace has 27 steps, known-set sizes 2 through 28 (405 total parent
candidates as a structural upper bound), and explicit valid parents are available
for every step. These are source/data observations, not measured reducer counts.

The minimal proposed experiment removes that parent search using explicit
kernel-checked witnesses while preserving the remaining finite checks and the
exact unchanged checkCertificate premise. No dependency-table rewrite is
supported or proposed. The proposal has not been compiled in this activation;
no fourth invocation was made. Exact proof sufficiency and bounded performance
must be tested on the actual failing proposition under the next grant.
