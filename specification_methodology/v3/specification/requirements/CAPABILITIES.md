# Tentative Capability Questions

These are questions about which capabilities the method needs, not accepted obligations. A capability's acceptance contract is selected separately, as for [Categorical Construction](../PRODUCT.md#categorical-construction).

Which capabilities follow from the accepted principles, and with which assumptions?

- Foundational derivation: can a reader tell which commitments are independent, which are derived from others, which generalise others, and which are unresolved?
- Purpose and specification: can one common specification (WHAT) admit different conforming realisations (HOWs)? It must do so without confusing two things that mean the same with two things that compute the same.
- Bounded work: can an actor get enough context, refine its work, combine results, and stop truthfully with an unknown when it must?
- Evidence and authority: can real claims be evaluated, material failures kept on record, and owner decisions reused without widening their scope?
- Progress and recovery: can interruption, changed dependencies, persistent work state and effects of unknown completion be handled without discarding valid progress?
- Method usability: can a fresh actor apply the method given only one reference frame and a subject? It must do so without private knowledge of the validator or the author's memory.
- Optional profiles: can a domain add the meaning it needs while generic rules and test subjects stay separate?
- Self-improvement: can observations identify the right owner of a repair, then support a successor release that is evaluated independently?

The previous release's [thirteen logical capabilities](../../../v2/specification/SCENARIOS.md#logical-functions), the logical functions its scenarios define, are inputs when deciding which capabilities the new release keeps. They are read under that release's [rule for agent-performed construction](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#agentic-construction-execution-stdo-up-020), STDO-UP-020. They are not thirteen mandatory stages, and they are not automatically accepted features.

Every selected capability identifies:

- the principles that require it;
- the current obligations it preserves;
- its applicable scope;
- its observable adequate outcome;
- its conformance expectations, specified independently of the author.

Cost measures are selected where a claim needs them. Selecting a capability introduces no universal budget, no requirement that all work in the method starts from a ticket, and no fixed number of actors. The construction of this release does run from tickets, under [Development Isolation](../PRODUCT.md#development-isolation).

The steel thread is the one named in [Categorical Construction](../PRODUCT.md#categorical-construction). Its selection is an open owner decision.
