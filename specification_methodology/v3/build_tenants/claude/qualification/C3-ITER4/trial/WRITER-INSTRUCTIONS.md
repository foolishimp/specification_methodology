# Instructions for the expectation writer

You write, for one task, the fixture and the expectations an independent
grader will use. You receive the task sentence and the owning sections
of a method that the task applies. You have not seen, and must not open,
any frame, any actor's work or any other file.

Write one Markdown file at the path the activation names:

1. **Fixture.** A concrete situation of about 150 to 400 words: the
   subject (a named artefact, candidate, member, surface or step), the
   facts an actor is given, the grant the actor holds (what it may
   decide), and what it is asked to return. The fixture must be decidable
   from the sections you were given plus its own facts, and it must
   contain at least one trap: a fact that a careless actor would treat
   as decisive when the method says it is not, or an omission the method
   says must be returned as missing.
2. **Expectations.** Between 8 and 14 items. Each item is one checkable
   statement about the actor's return ("the return records X", "the
   return does not treat Y as Z", "the return names what is missing: W").
   Tag each item `M` if only the method text decides it, or `F` if the
   fixture's own facts decide it. Include at least two negative items (a
   wrong move the method forbids) and one item on what the actor must
   report as unresolved or missing. Quote, for each `M` item, the
   section and sentence of the method that decides it (at most 25
   words).
3. **JSON block** at the end:

```json
{"task": "TT-nn", "items": [{"id": "E1", "tag": "M", "statement": "...", "decides": "SECTION: quote"}]}
```

Write nothing else anywhere. Then print the count of `M` and `F` items.
