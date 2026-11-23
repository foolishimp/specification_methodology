# Reference frames and the activation packet

- kind: feature
- class: requirement_reprice
- enters: requirements

From the product owner, 21 November 2026: "we need to introduce reference frames, we just need to implement STDO within the builder framework".

The Executive's reading, for the product owner to confirm or correct at the placing:

1. A vector declares the reference frame its session is activated on, as the method's REFERENCE_FRAME standard defines a frame. A working session and an evaluating session are activated on different frames.
2. What the framework gives a session is that frame's activation packet (REFERENCE_FRAME section 11): the evaluation and its result, the exact subject and basis, the attention surface by exact reference, the authority and territory, the admissible evidence, the exclusions, and the stop conditions. It is built by reference, and the method is referred to at the pinned release only.
3. The packet is sufficient: a session does not need to read the framework's own source, the graph, or any method source outside the pinned release to do its work (RF-002, RF-003, RF-004).
4. A session returns through the frame's closed result.
5. Withdrawn from this ticket by the Executive: merging frames for small work. It is decided after the products are built again, with the numbers.
6. The framework adds no frame law of its own. The method's optional Executive arrangement stays not adopted.

Evidence. Five small products were built with the installed framework on 20 November 2026: 50 sessions, 49.30 dollars. The framework itself used 7 seconds of 998. A brief was 350 to 885 bytes. Sessions read the graph with scripts of their own about 26 times, the framework's installed source about 18 times, and the method's mutable source about 9 times, once a file of another build. Placing a ticket was the dearest session of each run.

The product owner, 21 November 2026, on how it is built: "builder is too inefficient at this point, do the optimisation work with you as executive, we'll fix builder and then test it with the hello world suite". So this ticket is built by a writer and a reviewer under the Executive, not by the framework.

Also in this ticket: each session's cost and calls, where the agent reports them, are recorded in the event log and shown; and what a build leaves beside the code (compiled output) stays out of the product's history.

Acceptance:

- The same five products are built again, and each passes as before.
- No session of those runs reads the framework's source, or method source outside the pinned release.
- The cost of each run is stated beside the cost of 20 November.

## Result, 21 November 2026

Built by writers and one reviewer under the Executive, in four commits
(`123735529`, `b014a4f2a`, `cc4cb0605`, `2def0593b`). Point 5 of the reading
came back into the ticket after the measurements: small work takes four
sessions, through two registered graph functions (D107 to D119).

The five products, built again with live agents and judged outside the
framework by the same checks as on 20 November:

| Product | 20 November | 21 November |
|---|---|---|
| JavaScript command line | pass, 17 min, 10 sessions, 8.33 USD | pass, 7 min, 4 sessions, 3.28 USD |
| JavaScript module | pass, 16 min, 10 sessions, 8.42 USD | pass, 8 min, 4 sessions, 3.54 USD |
| Rust command line | pass, 26 min, 10 sessions, 10.55 USD | pass, 8 min, 4 sessions, 3.08 USD |
| Rust HTTP service | pass, 32 min, 10 sessions, 12.55 USD | pass, 15 min, 4 sessions, 4.41 USD |
| JavaScript in two branches | pass, 18 min, 10 sessions, 9.46 USD | pass, 9 min, 4 sessions, 3.72 USD |
| In all | 109 min, 49.30 USD | 47 min, 18.03 USD |

In the 20 sessions of 21 November, by the agent's own records: no session
read the framework's installation, the graph file, the event log or the
method's source repository. Only the five placing sessions read the method,
and only the two files their packets name, in the pinned release.

Open for the product owner: D118 (a small ticket that ends at the product
definition stops after the specification is accepted).
