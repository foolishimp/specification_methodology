# Method Interpretation Vocabulary

The interpretation preserves source-owned meanings and their explicit relations.
Structured semantic records use canonical JSON string literals because the a_c.text
carrier accepts scalar literals. The record retains field names, list order,
conditions, exceptions, local field references and result mappings. The native
checker follows explicit references; it does not execute these meanings.

## Requires

The bound predicate has the declared applicability, obligations, permitted
choices and exceptions, inputs and result relation together. A constraint is not
a satisfied instance or a grant. Definitions embedded in it retain their type.

## Defines

The record declares data or a consumer-to-owner relation. A definition is not a
Boolean verdict. Embedded obligations retain their declared scope; any assertion
of conformance requires its own bound predicate and admissible evidence.

## Locates

The record names a non-deciding source location. A locator adds no requirement,
permission, unknown task outcome or unfinished-construction obligation.

## Shared contract

The record defines a meaning reused through an exact contract identity. Each use
retains its local binding and conditions. Reuse does not merge distinct owners.

## Semantic record

The literal is the exact current semantic object. Fields such as applicability,
predicate, definition, argument, input contracts and result mapping keep their
own meanings. Row-local source-block names resolve through the row's exact byte-range and
digest pins against its source owner. Local field references select fields in
the same row.
Required future inputs are conditional contracts, not claims that the source is
missing or that an actual task has an unknown result.

## Reference location

The literal encodes an object with scope and pointer. Scope is clause-local:
semantic-record selects the clause's sole semantic record; a contract URI selects
the exact definition registered by a preceding inlined-contract argument in that
clause. Pointer is an RFC 6901 JSON Pointer relative to that explicit base.
The next argument supplies its typed native target. Compilation checks that the
pointer resolves and names that target. Scope never changes implicitly, including
when an occurrence returns to the outer record after an inline definition.
The pointer/ref pair distinguishes an occurrence, its target and its relation.

## Acquisition route

Scope and pointer select the occurrence by the Reference location rules.
The record preserves an exact relation occurrence without making its target an
unconditional acquisition dependency. A provenance route records correspondence,
example or navigation. A flat dependency enumeration retains its named targets
in the semantic record; its typed relation supplies acquisition and conditions
without a second unconditional edge. A conditional route retains its source-owned
condition, binding, target index and exact source coordinates. Establish the
condition for the task: when applicable, select that target index in addition
to the current index; when established inapplicable, retain the reason; when
undecided, retain the unresolved obligation and withhold dependent action.
Route presence establishes neither applicability nor satisfaction. Every target
resolves during compilation even when its body is not selected.

A qualification_ref carries scope, an RFC 6901 pointer and the SHA-256 of the
canonical JSON object at that pointer. It selects the complete qualification
already carried in the same clause's semantic record or registered inline
definition. The separate required_when field exactly reproduces that object's
condition, including null when absent. Resolve the reference before applying
the route. A missing, changed or ambiguous qualification refuses acquisition;
it cannot become unconditional permission. Literal qualification remains valid
when null. Pointer storage preserves the complete object, not an approximation.

## Inlined contract

This exact shared abbreviation has no independently declared semantic owner.
Its scope and pointer locate the use by the Reference location rules. Identity
registers the carried definition as an explicit clause-local pointer base;
definition_pointer locates that same definition in source-account.json.
Repeated registrations of one identity must carry the same exact definition.
Nested definitions declare their parent scope, and each later occurrence names
its own scope. Its real references still acquire their owners.
Inlining adds no owner, authority or instance truth. The complete set of users
does not become a source dependency of every use.

## Declared dependency

The source account declares this dependency. Its typed dependency relation and
local conditions determine why it is relevant; the link alone is not a premise.

## Declared dependency relation

The target belongs to the exact relation record at the referenced pointer.
Its kind, scope and qualifications remain in that record. Governing conditions,
refinements and provenance are not interchangeable relations.

## Scope reference

The target supplies the source-owned scope qualification attached to this row.
Its actual applicability must be established for the task; following the link
never establishes adoption or universal applicability.

## Argument reference

The target participates in the declared argument, with the premise kind,
conditional consequence and additional policy retained. An argument reference
neither proves entailment nor supplies instance evidence.

## Source reference

The target supplies source correspondence or provenance under the declared
relation. Provenance does not confer governing authority or imply entailment.

## Governing owner

The named owner supplies only the meaning assigned to it by the local binding.
A result owner does not supply task truth, disposition authority or performance.

## Foundation premise owner

The target owns the exact F1–F6 premise named at the pointer. The premise name and
conditional argument remain in the record; finite capacity does not establish
purpose, identity, composition or authority without their stated premises.

## Semantic reference

The exact target participates in the named local semantic relation. The record,
not reference closure, determines its meaning and whether it governs an action.
