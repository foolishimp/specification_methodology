# Addendum to the expectation writer's instructions, iteration 5

You follow [`../../C3-ITER4/trial/WRITER-INSTRUCTIONS.md`](../../C3-ITER4/trial/WRITER-INSTRUCTIONS.md)
with these additions. You still receive only the task sentence and the
owning sections, and you still open no frame and no actor's work. Two
tags are new: `W` marks a deliberately weak item, and `A` marks an item
whose observation cannot separate two admissible returns.

1. **Two added items.** After the 8 to 14 items of the base instructions,
   add exactly two more:
   - one tagged `W`: a deliberately weak assertion. It is a true
     necessary condition of the task's required outcome that a return
     making the wrong decision could still satisfy (for example, that the
     return names the basis it read, or that it uses the required result
     vocabulary). State in its `decides` field the section that makes it
     necessary and add the words "weak: a wrong decision can satisfy this".
   - one tagged `A`: an ambiguous observation. Choose one point of the
     task at which two admissible returns, one correct under the method
     and one not, read the same. Write the item so that it observes
     exactly that point, and record in an `admissible` field the point
     and both returns, each in at most 40 words, marking which is
     correct. State in its `decides` field the section whose obligation
     the two returns differ on and add the words "ambiguous: the
     observation does not separate the admissible answers". Before you
     finish, check that the two returns do read the same at the point: if
     a grader could tell them apart there, the item is not ambiguous, and
     you rewrite it.
2. **Provenance.** For every item, `decides` quotes the owning section and
   sentence (at most 25 words), as before. Every item is a necessary
   condition of correct frame use; write no item that claims the return
   is correct as a whole.
3. **Augmenting an existing set.** When you receive an existing set with
   its owning sections, change no existing item: your output is the
   existing items byte for byte, followed by your two items.
4. **JSON.** The JSON block lists the `W` and `A` items with their tags like
   the others, and the `A` item carries its `admissible` field:

```json
{"id": "E15", "tag": "A", "statement": "...", "decides": "SECTION: quote; ambiguous: the observation does not separate the admissible answers", "admissible": {"point": "...", "correct": "...", "incorrect": "..."}}
```

   Print the counts of `M`, `F`, `W` and `A` items.
