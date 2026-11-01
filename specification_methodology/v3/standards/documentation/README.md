# STDO 3.0.3 documentation

Open the [documentation home](index.html), then choose:

- [Constraints](constraint-explorer/index.html): STDO's historical common model.
- [Code example](code-explorer/index.html): ABIogenesis requirements, selected
  canonicalization code and test sources, with attributed proposed traces.
- [Lean proofs](proofs/index.html): proof statements, source and retained results.
- [Use the tools](../tooling/README.md): create a writable copy to build your own.

All three readers open in a browser.
These files are installed with STDO 3.0.3; no additional download or
Graphify, Lean, a_c or Node installation is needed to read them.

## Open an installed copy

The ordinary manager resolves the local file:

```sh
stdo resolve stdo://releases/v3.0.3/standards/documentation/index.html
```

Open the returned `path` in a desktop browser. The file and its explorer work
offline. A browser with WebGL supports 3D and 2D. The initial Layered view,
search, Files navigation and full text reader remain available without WebGL.
No service is needed.

## Read and follow constraints

1. Search the constraints, select another record family, or use **Files** to
   browse the represented source folders and files.
2. Select a result to read its complete statement, conditions and exceptions.
3. Follow labelled authored relations or required-retention links. They have
   different meanings; a graph edge does not assert a proved implication.
4. Read attached caveats and source quotations. Open a quotation to see its
   embedded source file and highlighted lines.
5. Use the reading trail and Back to revisit exact steps, including parallel
   and self-relations. Selecting an unrelated result begins a new trail.
6. Switch **3D**, **2D** or **Layered** to view the same selected record,
   relationships and reading trail. Focus, expand or show the overview. Drag
   to orbit in force views; scroll and use zoom controls in Layered.
7. Use **Show in files** or **Back to file** to move between source discovery
   and logical connections. Folder order does not create a semantic relation.

## Code and proof examples

The ABI example is the reviewed T-019 artifact: a frozen representation of
ABIogenesis and a four-file code/test selection. Its five proposed trace links
cover part of canonical ordering and serialization. They do not establish the
broader roundtrip/admission clauses, executed tests or semantic satisfaction.
The reader names its source, author, parser and unresolved endpoints. Use the
browser's Back button or open readers in separate tabs to return to this home.

The Lean reader shows exact T-011 proof sources and its retained independent
report. It explains finite closure and record-preserving projection, premises
and limits. This historical report is not a new Lean run or a proof of the
code overlay. The [proof catalog](proofs/PROOFS.json) binds its sources.

## Represented source and current method

**Distributed with STDO 3.0.3; represented source: historical common cut
35fb4824.** This preserves the T-014 representation and source data
with the current unified reader. It contains 1,987 local records (841 constraints), 1,021 external
resolutions and 58 embedded source files. It is not a source-matched map of
the 3.0.3 standards and has not acquired that authority by being bundled.

Use the [installed current method](../README.md) and
[Getting Started](../../plugins/spec/references/GETTING_STARTED.md) for current
method decisions. The explorer's embedded source remains the historical source
it names. Lean's structural closure and projection proofs do not prove the
English constraint predicates. [DOCUMENTATION.json](DOCUMENTATION.json) binds
the distributing version, represented source and exact documentation bytes.
