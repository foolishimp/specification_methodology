/**
 * The terms of the graph language (a session, a sequence, a workflow and a
 * reference), what a node and a vector declare, and the constructors that are
 * the only way to make a term. A term that exists has been checked, is in
 * normal form and cannot be changed.
 *
 * @uses C5 H1 H3
 * @is REQ-GRAPH-001 REQ-GRAPH-002 REQ-GRAPH-003
 */
import { covers } from "../kit/place_containment.js";
import { normal } from "../kit/term_recursion.js";
import { holdsWhiteSpace } from "../kit/white_space.js";
/** The paths of a node's asset: those its name gives it, or its place (REQ-GRAPH-003). */
export function pathsOf(node) {
    return node.paths ?? [node.place];
}
/**
 * What a graph function that writes `writes` rests on: every node those nodes
 * depend on that it does not write itself, in the order the nodes are declared
 * (REQ-GRAPH-005).
 */
export function restsOn(nodes, writes) {
    const needed = new Set(nodes.filter((n) => writes.includes(n.name)).flatMap((n) => n.depends ?? []));
    return nodes.map((n) => n.name).filter((name) => needed.has(name) && !writes.includes(name));
}
/**
 * The paths a definition file gives each name: every reference in it whose
 * fragment is the name, as a path from the workspace's folder: `./bin/#x`
 * gives the name x the path bin.
 */
export function namedPlaces(definition) {
    const named = new Map();
    const visit = (value) => {
        if (typeof value === "object" && value !== null)
            for (const inner of Object.values(value))
                visit(inner);
        if (typeof value !== "string")
            return;
        const at = value.indexOf("#");
        const path = value.slice(0, Math.max(0, at)).replace(/^\.\//, "").replace(/\/$/, "");
        if (at > 0 && isPlace(path))
            named.set(value.slice(at + 1), [...(named.get(value.slice(at + 1)) ?? []), path]);
    };
    visit(definition);
    return named;
}
/** A node whose place is a name, with the paths `named` gives it; any other node as it is. */
export function placed(node, named) {
    if (named === undefined || !node.place.startsWith("#"))
        return node;
    const paths = named.get(node.place.slice(1)) ?? [];
    if (paths.length === 0)
        throw new TermRefused("places", `node '${node.name}'`, `the definition file gives '${node.place}' no path`);
    return { ...node, paths };
}
/** The attempts at a vector, and the minutes of each of its sessions, where it declares none (REQ-PARAM-003, D94). */
export const ATTEMPTS = 3;
export const MINUTES = 60;
/** The stretch a reference names, where it names one. */
export function stretchOf(term) {
    return term.enters === undefined || term.ends === undefined ? undefined : { enters: term.enters, ends: term.ends };
}
/** Why a term could not be made: the kind of fault, where it is, and what it says. */
export class TermRefused extends Error {
    fault;
    where;
    says;
    constructor(fault, where, says) {
        super(`${where}: ${says}`);
        this.fault = fault;
        this.where = where;
        this.says = says;
    }
}
function freeze(value) {
    if (typeof value === "object" && value !== null && !Object.isFrozen(value)) {
        for (const inner of Object.values(value))
            freeze(inner);
        Object.freeze(value);
    }
    return value;
}
/** A name of a node, a vector or a graph function: at least one character, and no white space. */
export function isName(name) {
    return name !== "" && !holdsWhiteSpace(name);
}
/** A place is a path relative to the workspace: parts joined by "/", none empty, "." or "..". A path does not start with `#`. */
function isPlace(place) {
    return !place.startsWith("#") && place.split("/").every((part) => part !== "" && part !== "." && part !== "..");
}
/** One of two places lies inside the other. */
export function nests(a, b) {
    return covers(a, b) || covers(b, a);
}
/** The files of the workspace that an asset at `paths` covers (REQ-GRAPH-003). */
export function covered(paths, files) {
    return files.filter((file) => paths.some((path) => covers(path, file)));
}
function makeSequence(terms) {
    return freeze({ term: "sequence", terms: [...terms] });
}
function makeWorkflow(nodes, vectors) {
    return freeze({ term: "workflow", nodes: [...nodes], vectors: [...vectors] });
}
/** The shape of terms for the structural recursion, without following references. */
export const termShape = {
    parts: (term) => term.term === "sequence" ? term.terms : term.term === "workflow" ? term.vectors.map((v) => v.function) : [],
    rebuild: (term, parts) => {
        if (term.term === "sequence") {
            return parts.length === term.terms.length && parts.every((p, i) => p === term.terms[i]) ? term : makeSequence(parts);
        }
        if (term.term === "workflow") {
            if (parts.every((p, i) => p === term.vectors[i]?.function))
                return term;
            return makeWorkflow(term.nodes, term.vectors.map((v, i) => ({ ...v, function: parts[i] ?? v.function })));
        }
        return term;
    },
    isSequence: (term) => term.term === "sequence",
    isInert: (term) => (term.term === "sequence" && term.terms.length === 0) || (term.term === "workflow" && term.vectors.length === 0)
};
export function session() {
    return freeze({ term: "session" });
}
/** A sequence, in normal form: inner sequences flattened and terms that do nothing dropped. */
export function sequence(terms) {
    return normal(termShape, makeSequence(terms));
}
/** A reference; with a stretch, both its nodes named, an induction entry of a ticket's term (REQ-METHOD-006). */
export function reference(name, stretch = {}) {
    if (!isName(name))
        throw new TermRefused("terms", `reference '${name}'`, "is not a name");
    const { enters, ends } = stretch;
    if ((enters === undefined) !== (ends === undefined))
        throw new TermRefused("terms", `reference '${name}'`, "names where its stretch enters or where it ends, and not both");
    if (enters === undefined || ends === undefined)
        return freeze({ term: "reference", name });
    for (const node of [enters, ends])
        if (!isName(node))
            throw new TermRefused("terms", `reference '${name}'`, `'${node}' is not a name`);
    return freeze({ term: "reference", name, enters, ends });
}
function checkOf(check, where) {
    if (check.name.trim() === "")
        throw new TermRefused("checks", where, "has no name");
    const run = check.run;
    if (run.kind === "ticket_field" && run.is !== undefined && run.is_not !== undefined) {
        throw new TermRefused("checks", `${where} '${check.name}'`, "says both is and is_not");
    }
    if (run.kind === "command" && run.argv.length === 0) {
        throw new TermRefused("checks", `${where} '${check.name}'`, "names no command");
    }
    return check;
}
function vectorOf(v) {
    const where = `vector '${v.name}'`;
    if (!isName(v.name))
        throw new TermRefused("terms", where, `'${v.name}' is not a name`);
    if (v.result !== undefined && v.first !== true)
        throw new TermRefused("terms", where, "declares what must be true of its result: each node it writes declares that of itself");
    if (v.checks !== undefined && v.first !== true)
        throw new TermRefused("checks", where, "declares checks: each node it writes declares its own");
    for (const check of v.checks ?? [])
        checkOf(check, `check of ${where}`);
    if (v.evaluation !== undefined) {
        for (const place of [v.evaluation.findings, v.evaluation.verdict]) {
            if (!isPlace(place))
                throw new TermRefused("places", where, `'${place}' is not a place in the workspace`);
        }
    }
    if (v.frames?.evaluation !== undefined && v.evaluation === undefined) {
        throw new TermRefused("terms", where, "declares a frame for an evaluating session, and no evaluation");
    }
    for (const frame of [v.frames?.work, v.frames?.evaluation])
        if (frame !== undefined)
            frameOf(frame, where);
    return v;
}
function frameOf(frame, where) {
    if (!isName(frame.name))
        throw new TermRefused("terms", where, `the frame '${frame.name}' is not a name`);
    if (!Number.isInteger(frame.revision) || frame.revision < 1)
        throw new TermRefused("terms", where, `the frame '${frame.name}' has no revision above zero`);
    for (const m of frame.method ?? []) {
        if (m.term.trim() === "" || m.section.trim() === "")
            throw new TermRefused("terms", where, `the frame '${frame.name}' names a term of the method with no words`);
        if (!isPlace(m.file))
            throw new TermRefused("terms", where, `the frame '${frame.name}' names '${m.file}', which is not a place in the method release`);
    }
    return frame;
}
/** A workflow: nodes and the vectors between them, each vector with its own graph function. */
export function workflow(nodes, vectors) {
    const nodeNames = new Set();
    for (const node of nodes) {
        if (!isName(node.name))
            throw new TermRefused("terms", `node '${node.name}'`, "is not a name");
        if (nodeNames.has(node.name))
            throw new TermRefused("terms", `node '${node.name}'`, "is declared twice");
        nodeNames.add(node.name);
        if (!(isPlace(node.place) || (node.place.startsWith("#") && isName(node.place.slice(1))))) {
            throw new TermRefused("places", `node '${node.name}'`, `'${node.place}' is not a place in the workspace`);
        }
        for (const name of node.depends ?? [])
            if (!isName(name))
                throw new TermRefused("terms", `node '${node.name}'`, `depends on '${name}', which is not a name`);
        const accepted = node.accepted ?? [];
        if (new Set(accepted).size < accepted.length)
            throw new TermRefused("terms", `node '${node.name}'`, "declares what accepts it twice");
        if (node.given === true && accepted.length > 0)
            throw new TermRefused("terms", `node '${node.name}'`, "is given, and declares what accepts it, which no vector records");
        for (const check of node.checks ?? [])
            checkOf(check, `check of node '${node.name}'`);
    }
    const vectorNames = new Set();
    for (const v of vectors) {
        if (vectorNames.has(v.name))
            throw new TermRefused("terms", `vector '${v.name}'`, "is declared twice");
        vectorNames.add(v.name);
        vectorOf(v);
    }
    return makeWorkflow(nodes, vectors);
}
