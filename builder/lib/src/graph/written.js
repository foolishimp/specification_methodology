/**
 * The written form of graphs and registries: data a person can read, read and
 * written through the lossless encoding, with every term made by its
 * constructor on the way in.
 *
 * @uses C14 C5
 * @is REQ-GRAPH-002 REQ-GRAPH-004 REQ-GRAPH-005
 */
import { count, later, list, literal, names, oneOf, optional, read, record, text, write, writeLine } from "../kit/lossless_encoding.js";
import { registry } from "./registry.js";
import { placed, reference, sequence, session, TermRefused, workflow } from "./terms.js";
const RunShape = oneOf([
    record({ kind: literal("command"), argv: list(text) }),
    record({ kind: literal("ticket_field"), field: text, is: optional(text), is_not: optional(text) }),
    record({ kind: literal("ticket_kept") }),
    record({ kind: literal("traced"), pattern: text, from: text, into: text, deferred: text, others: optional(list(text)) })
]);
const CheckShape = record({ name: text, run: RunShape });
const AcceptedShape = list(oneOf([literal("evaluation"), literal("decision")]));
const NodeShape = record({
    name: text,
    place: text,
    result: list(text),
    checks: optional(list(CheckShape)),
    depends: optional(list(text)),
    given: optional(literal(true)),
    accepted: optional(AcceptedShape)
});
/** What a node declares of itself and what its acceptance means: what must be true of it, what accepts it and what it depends on. */
const DeclarationShape = record({ result: list(text), accepted: optional(AcceptedShape), depends: optional(list(text)) });
const FrameShape = record({ name: text, revision: count, method: optional(list(record({ term: text, file: text, section: text }))) });
const VectorShape = record({
    name: text,
    first: optional(literal(true)),
    result: optional(list(text)),
    checks: optional(list(CheckShape)),
    evaluation: optional(record({ findings: text, verdict: text })),
    // A decision declares nothing: a record that holds no field, so a key on it is refused (an empty record would let one through).
    decision: optional(names(oneOf([]))),
    attempts: optional(count),
    minutes: optional(count),
    frames: optional(record({ work: optional(FrameShape), evaluation: optional(FrameShape) })),
    function: later(() => TermShape)
});
const TermShape = oneOf([
    record({ term: literal("session") }),
    record({ term: literal("sequence"), terms: list(later(() => TermShape)) }),
    record({ term: literal("workflow"), nodes: list(NodeShape), vectors: list(VectorShape) }),
    record({ term: literal("reference"), name: text, enters: optional(text), ends: optional(text) })
]);
const RegistryShape = record({
    entries: list(record({ name: text, writes: list(text), purpose: text, definition: TermShape })),
    default: optional(TermShape)
});
function build(t, named) {
    switch (t.term) {
        case "session":
            return session();
        case "sequence":
            return sequence(t.terms.map((inner) => build(inner, named)));
        case "reference":
            return reference(t.name, t);
        case "workflow":
            return workflow(t.nodes.map((n) => placed(n, named)), t.vectors.map((v) => ({ ...v, function: build(v.function, named) })));
    }
}
/** A refusal inside a check is a check that does not say what runs it; in a registry outside a definition, a fault of the registry; else a term. */
function faultsOf(refused, outside) {
    return refused.map(({ at, says }) => ({
        fault: at.includes("run") ? "checks" : outside === "registry" && !at.includes("definition") ? "registry" : "terms",
        where: at.length === 0 ? "the whole" : at.map((key, i) => (typeof key === "number" ? `[${key}]` : i === 0 ? key : `.${key}`)).join(""),
        says
    }));
}
function made(make) {
    try {
        return { value: make() };
    }
    catch (error) {
        if (error instanceof TermRefused)
            return { faults: [{ fault: error.fault, where: error.where, says: error.says }] };
        throw error;
    }
}
/** Reads a governing graph, which is a workflow; `named` gives the paths of the places that are names. */
export function readGraph(written, named) {
    const got = read(TermShape, written);
    if ("refused" in got)
        return { faults: faultsOf(got.refused, "terms") };
    const term = made(() => build(got.value, named));
    if ("faults" in term)
        return term;
    if (term.value.term !== "workflow") {
        return { faults: [{ fault: "terms", where: "the whole", says: "a governing graph is a workflow" }] };
    }
    return { graph: term.value };
}
/** Reads one term, such as the term a ticket carries (REQ-METHOD-006), each part made by its constructor. */
export function readTerm(written) {
    const got = read(TermShape, written);
    if ("refused" in got)
        return { faults: faultsOf(got.refused, "terms") };
    const term = made(() => build(got.value, undefined));
    return "faults" in term ? term : { term: term.value };
}
/** One term in the written form, on one line, as a ticket's field holds it. */
export function writeTerm(term) {
    return writeLine(TermShape, term);
}
export function readRegistry(written, named) {
    const got = read(RegistryShape, written);
    if ("refused" in got)
        return { faults: faultsOf(got.refused, "registry") };
    const value = got.value;
    const r = made(() => registry(value.entries.map((entry) => ({ ...entry, definition: build(entry.definition, named) })), value.default === undefined ? undefined : build(value.default, named)));
    return "faults" in r ? r : { registry: r.value };
}
/**
 * The one written form of what a node declares of itself: what must be true of
 * it, what accepts it and what it depends on, on one line (C14). Its identity
 * is what a verdict or an answer at the node stands on beside the content
 * (REQ-ALG-004); its place, its name and the vectors that write it are no part
 * of it. The first vector declares the same of the ticket, which is no node:
 * its results, and the user's yes where it ends in a decision (D175).
 */
export function writeDeclaration(node) {
    return writeLine(DeclarationShape, {
        result: node.result,
        ...(node.accepted === undefined ? {} : { accepted: node.accepted }),
        ...(node.depends === undefined ? {} : { depends: node.depends })
    });
}
export function writeGraph(graph) {
    return write(TermShape, graph);
}
export function writeRegistry(r) {
    return write(RegistryShape, { entries: r.entries, ...(r.default === undefined ? {} : { default: r.default }) });
}
