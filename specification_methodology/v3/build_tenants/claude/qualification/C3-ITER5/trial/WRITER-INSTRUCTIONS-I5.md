# Addendum to the expectation writer's instructions, iteration 5

You follow [`../../C3-ITER4/trial/WRITER-INSTRUCTIONS.md`](../../C3-ITER4/trial/WRITER-INSTRUCTIONS.md)
with these additions. You still receive only the task sentence and the
owning sections, and you still open no frame and no actor's work.

1. **Two added items.** After the 8 to 14 items of the base instructions,
   add exactly two more:
   - one tagged `W`: a deliberately weak assertion. It must be a true
     necessary condition of the task's required outcome that a return
     making the wrong decision could still satisfy (for example, that the
     return names the basis it read, or that it uses the required result
     vocabulary). State in its `decides` field the section that makes it
     necessary and add the words "weak: a wrong decision can satisfy this".
   - one tagged `A`: an ambiguous observation. Describe two admissible
     returns for one point of the task, one correct under the method and
     one not, that would read the same at the point your item observes,
     and write the item so that it observes exactly that point. State in
     its `decides` field the section whose obligation the two returns
     differ on and add the words "ambiguous: the observation does not
     separate the admissible answers".
2. **Provenance.** For every item, `decides` quotes the owning section and
   sentence (at most 25 words), as before. Every item is a necessary
   condition of correct frame use; write no item that claims the return
   is correct as a whole.
3. **JSON.** The JSON block lists the `W` and `A` items with their tags like
   the others. Print the counts of `M`, `F`, `W` and `A` items.
