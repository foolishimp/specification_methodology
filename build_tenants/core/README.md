# Axiom Indexer Core Build Tenant

The core tenant realizes the MVP boundary:

```text
native skill -> LLM-authored program -> resolver/validator -> logical map
  -> Executive-authored labeled sections -> exact string join
```

The LLM owns semantic interpretation and repair. The implementation owns only
symbolic URI resolution, declared consistency checks, diagnostics, and map
instantiation. It also joins caller-supplied labels and text without selecting
or changing them.

Target-specific corpora and future GTL composition remain separate extensions.
