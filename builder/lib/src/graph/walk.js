/**
 * Walking a graph: the names of graph functions it uses, how they resolve in
 * the registry, every workflow it holds, following each reference to its
 * definition, what is run in a vector's place, and what a ticket's term
 * denotes.
 *
 * @uses C5 C6
 * @is REQ-GRAPH-001 REQ-GRAPH-005 REQ-GRAPH-006 REQ-METHOD-006
 */
import { definitionOf, resolve } from "../kit/name_resolution.js";
import { fold } from "../kit/term_recursion.js";
import { definitions } from "./registry.js";
import { stretchOf, termShape } from "./terms.js";
/** The names of graph functions a term refers to, without following them. */
function namesUsed(term) {
    return fold(termShape, term, (t, inner) => t.term === "reference" ? [t.name] : inner.flat());
}
/** The names of graph functions a term refers to with a stretch, without following them: only a ticket's term may name one (REQ-METHOD-006). */
export function stretched(term) {
    return fold(termShape, term, (t, inner) => t.term === "reference" && stretchOf(t) !== undefined ? [t.name] : inner.flat());
}
/** Each name used, followed through the registry: the names it lacks and the names that lead back to themselves. */
export function resolution(graph, r) {
    return resolve(namesUsed(graph), definitions(r), namesUsed);
}
/** The term that carries a vector's function out: a reference followed through the registry to its definition (C6). */
function carriedOut(term, r) {
    if (term.term !== "reference")
        return term;
    return definitionOf(term.name, definitions(r), (d) => (d.term === "reference" ? d.name : undefined)) ?? term;
}
/**
 * Every workflow the graph holds, the graph first, each once, following
 * references. Only for a graph whose resolution has no unknown or cyclic name.
 */
export function workflows(graph, r) {
    const defs = definitions(r);
    const following = {
        ...termShape,
        parts: (t) => {
            if (t.term !== "reference")
                return termShape.parts(t);
            const definition = defs.get(t.name);
            return definition === undefined ? [] : [definition];
        }
    };
    const all = fold(following, graph, (t, inner) => t.term === "workflow" ? [t, ...inner.flat()] : inner.flat());
    return [...new Set(all)];
}
/** Every node declared in the graph's workflows, in the order met. */
export function nodesOf(graph, r) {
    return workflows(graph, r).flatMap((w) => w.nodes);
}
/** Every vector of the graph's workflows, inner vectors included, in the order met. */
export function vectorsOf(graph, r) {
    return workflows(graph, r).flatMap((w) => w.vectors);
}
/**
 * What is run in a vector's place, in the order written (REQ-FLOW-005 step
 * 2): each session and each workflow its graph function holds, sequences
 * flattened and each reference carried out by its definition (C6). A
 * workflow's own vectors are run by `next`, each by its own graph function,
 * so nothing inside a workflow is listed. Only for a graph whose resolution
 * has no unknown or cyclic name.
 */
export function inPlace(term, r) {
    const outer = {
        ...termShape,
        parts: (t) => {
            if (t.term === "workflow")
                return [];
            if (t.term !== "reference")
                return termShape.parts(t);
            const definition = carriedOut(t, r);
            return definition.term === "reference" ? [] : [definition];
        }
    };
    return fold(outer, term, (t, inner) => t.term === "session" || t.term === "workflow" ? [t] : inner.flat());
}
/** The vector carries out the graph function a reference names: its own graph function is that reference. */
export function carries(v) {
    return v.function.term === "reference" ? v.function.name : undefined;
}
/**
 * What a ticket's term denotes (REQ-METHOD-006): the vectors of `graph`, the
 * governing graph, that it names, in the order written. A reference names the
 * one vector of the graph that carries out the graph function it names, with
 * the stretch it names, where it names one. A reference to an entry that no
 * vector of the graph carries out means the term that entry names, followed
 * through the registry (C6). A sequence denotes its terms one after another,
 * so its normal form denotes what it does (C5). A name the registry does not
 * list, one that leads back to itself, one two vectors carry out, a stretch on
 * a name no vector carries out, and a session or a workflow that no vector
 * carries out denote nothing, and the reason is given.
 */
export function denoted(term, graph, r) {
    const defs = definitions(r);
    const found = resolve(namesUsed(term), defs, namesUsed);
    if (found.unknown.length > 0)
        return { why: `${found.unknown.join(", ")} ${found.unknown.length === 1 ? "is" : "are"} not in the registry` };
    if (found.cyclic.length > 0)
        return { why: `${found.cyclic.join(", ")} ${found.cyclic.length === 1 ? "leads" : "lead"} back to itself` };
    const carrying = (name) => graph.vectors.filter((v) => carries(v) === name);
    const following = {
        ...termShape,
        parts: (t) => {
            if (t.term !== "reference")
                return termShape.parts(t);
            const definition = carrying(t.name).length === 0 ? defs.get(t.name) : undefined;
            return definition === undefined ? [] : [definition];
        }
    };
    const joined = (inner) => inner.find((d) => "why" in d) ?? { entries: inner.flatMap((d) => ("entries" in d ? d.entries : [])) };
    return fold(following, term, (t, inner) => {
        if (t.term === "sequence")
            return joined(inner);
        if (t.term !== "reference")
            return { why: `the term holds a ${t.term} that no vector of the graph carries out` };
        const by = carrying(t.name);
        const stretch = stretchOf(t);
        if (by.length > 1)
            return { why: `${t.name} is carried out by ${by.length} vectors of the graph, and a term names one` };
        if (by[0] !== undefined)
            return { entries: [{ v: by[0], ...(stretch === undefined ? {} : { stretch }) }] };
        if (stretch !== undefined)
            return { why: `${t.name} names a stretch, and is carried out by no vector of the graph` };
        const definition = defs.get(t.name);
        return definition?.term === "session" || definition?.term === "workflow" ? { why: `${t.name} is carried out by no vector of the graph` } : joined(inner);
    });
}
