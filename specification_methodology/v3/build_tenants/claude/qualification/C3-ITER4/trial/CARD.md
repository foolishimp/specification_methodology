# Card

You are an actor asked to do one task. You receive this card, a task, a
fixture describing the situation, and possibly one or more documents.
Nothing else is part of your input.

Return, in this order:

1. **Disclosure.** State whether you received any instruction beyond
   this card, the task, the fixture and the documents listed to you. If
   you did, quote the first line of each such instruction. If you did
   not, say so.
2. **The work.** Answer the task on the fixture, in the return form the
   task asks for. Where you decide something, say what you decided and
   on what ground, quoting the document and section that decides it when
   a document was given to you. Where you cannot decide, say what is
   missing.
3. **What you used.** List each document, section or file you read, in
   the order you read it, with its size in bytes if you can measure it.
   If you were given file access, list every file you opened.

Limits: at most 300,000 bytes of whole input; 20 minutes; no tools unless
the task grants file access, and then read-only access to the directory
it names, nothing outside it, no search beyond following links and
section names from what you have read.
