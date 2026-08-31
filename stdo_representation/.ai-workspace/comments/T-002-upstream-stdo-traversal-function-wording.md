# T-002 Upstream Feedback — Fundamental Traversal Functions

Subject: STDO `v2.4.3-rc.3` wording for `F_D`, `F_P`, and `F_H`

The selected release correctly defines the three exact graph-native ODD concept
identities and their distinct authority boundaries. Some clauses call them
“graph/runtime shorthands.” That wording can be misread as making the concepts
optional notation rather than the fundamental deterministic, probabilistic, and
human function classes of the ODD traversal architecture.

A future STDO successor should clarify:

- the symbols `F_D`, `F_P`, and `F_H` are shorthand names;
- the three function classes and their authority separation are fundamental ODD
  architecture;
- a passive graph-and-constraint Product may be an input to an external `F_P`
  traversal without embedding HoG or ABG runtime realization; and
- absence of embedded runtime does not authorize reuse of `F_P` outside its
  declared ODD traversal contract.

This is downstream feedback only. It does not amend the immutable selected STDO
release and does not block STDO Representation from binding the existing exact
concept identities unchanged.
