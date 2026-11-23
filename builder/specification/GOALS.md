# Goals

The current wave of work has four goals.

1. **Define the product.** The intent, the product definition and the
   requirements are written, and the product owner has accepted each of them.
2. **Decide the loans.** The graph language, the registry, the higher-order
   graph functions and the event log are each examined in the loaner source and
   tested against the intent's guard rails. For each, the product owner decides
   whether it is taken as code, taken as a design and written new, or left.
3. **First build.** The framework sets up the smallest governed product and has
   the agent build it end to end, as scenario S1 describes. It is the first
   thing built, and every later change keeps it working. The result is verified
   from the workspace alone. The first build is the library and the
   command-line program over it. The program for the Model Context Protocol and
   the service follow, each as a ticket, over the same library. So does
   building several tickets at once.
4. **Use it on itself.** After the first build, the next change to this product
   is asked for in a ticket and built by the installed product.
