# Claude a_c Interpretation

This territory holds a_c interpretations of exact frozen states of this
tenant's standards. Each is a validated a_c.text program with its map, its
bindings and its projected frames, bound to the digests of the members it
encodes. None has an author-independent fidelity judgment, and none is
accepted.

## Status

The current interpretation is [i3/](i3/README.md), bound to the members at
the iteration 3 source-settlement commit `3ab7ef9`. It is a partial
encoding: its README states what it covers and the tasks for which it is
insufficient. Every other directory here is historical.

The historical programs are bound to member digests from before the C3
cross-synthesis rebuild. They are not current interpretations of the
rebuilt members. Checked on 2026-10-14 against the current members:
set-2, set-3 and set-4 match no current member's digest, and set-5 and
set-6 match only POSTING_GUIDE and WRITING_GUIDE among the 23 members each
binds. Their projected frames, the set-6 bootstrap frame among them, carry
the earlier text. Re-encoding the rebuilt members is open work.

The activation unit for the rebuilt members is the set of verbatim frames
in [standards/frames/](../standards/frames/FRAME_INPUTS.json). Each frame
copies, byte for byte, the owning sections one task needs, names each
source with its digest, and owns no determination. When an actor reads a
frame and when it reads the owning sections instead is
[ACTIVATION §2](../standards/ACTIVATION.md#2-context-construction-under-an-envelope),
Acquisition. The disposition of the predecessor's compressed summaries
stays `unresolved` in the [frontier](../frontier/PREDECESSOR_CLAIMS.md),
pending the product owner's ruling; nothing here decides it.

## Contents

| Directory | Subject it binds | Frames |
|---|---|---|
| [i3/](i3/README.md) | current: the members at `3ab7ef9`; shared-owner determinations of G1 to G4 only (64 clauses) | 4 frame indexes, no published frame |
| [t1/](t1/README.md) | the T1.2 increment: FOUNDATIONS, CALCULUS §1–3, EVALUATION §1–4 | 1 |
| [t2/](t2/README.md) | the T2 increment: adds CALCULUS §4–7 and SPEC_METHOD | 2 |
| [t3/](t3/README.md) | the T3 increment: adds EVALUATION §5–8, CONFORMANCE and PROFILES | 3 |
| [set/](set/README.md) | the seven-file set (T4), one frame per reading route | 5 |
| [set-2/](set-2/README.md) | eight standards at `1a68fd5`: REFERENCE_FRAME added, CALCULUS renamed ACTIVATION | 7 |
| [set-3/](set-3/README.md) | eight standards at `ac3ec5f`: the three W2c repairs | 7 |
| [set-4/](set-4/README.md) | thirteen members at `978d324`; a partial encoding for the F-02 task frames | 4 |
| [set-5/](set-5/README.md) | twenty-three members at `3824752`; a partial encoding for the F-03 task frames and a candidate bootstrap frame | 10 |
| [set-6/](set-6/README.md) | twenty-three members at `9be9f57`; set-5 after a Writer fidelity pass ([FIDELITY.md](set-6/FIDELITY.md)) | 16 |

The T1 version failed an author-independent fidelity check on four points,
since repaired. The set-6 fidelity pass is a Writer self-check, not an
author-independent judgment.

Use the
[dependency and proof contract](../../../specification/requirements/A_C_DEPENDENCY.md).
Keep source-to-model dispositions, signature, program, maps and bindings,
mechanical output, independent fidelity judgment and actual-use claim
distinct. This tenant output cannot be relabelled as the distributed STDO
Representation.
