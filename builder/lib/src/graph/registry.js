/**
 * The registry: the published list of named graph functions, one entry for
 * each name, with the nodes it writes, what it is for in one sentence, and its
 * definition as a term; and, where it declares one, the default term: the
 * term a ticket that carries none is built by (REQ-METHOD-006).
 *
 * What an entry rests on is not declared: it is every node the nodes it
 * writes depend on that it does not write itself (`restsOn`).
 *
 * @uses C5
 * @is REQ-GRAPH-005
 */
import { isName, restsOn, TermRefused } from "./terms.js";
/** A registry; refused when two entries share a name or an entry says nothing of what it is for. */
export function registry(entries, byDefault) {
    const names = new Set();
    for (const entry of entries) {
        if (!isName(entry.name))
            throw new TermRefused("registry", `registry entry '${entry.name}'`, "is not a name");
        if (names.has(entry.name))
            throw new TermRefused("registry", `registry entry '${entry.name}'`, "is listed twice");
        names.add(entry.name);
        if (entry.purpose.trim() === "") {
            throw new TermRefused("registry", `registry entry '${entry.name}'`, "does not say what it is for");
        }
    }
    const list = entries.map((entry) => Object.freeze({ ...entry }));
    return Object.freeze({ entries: Object.freeze(list), ...(byDefault === undefined ? {} : { default: byDefault }) });
}
/** The definition of each name. */
export function definitions(r) {
    return new Map(r.entries.map((entry) => [entry.name, entry.definition]));
}
/** The list a user reads, which the registry command gives: each entry with what it rests on, derived from the nodes of the graph. */
export function listing(r, nodes) {
    return r.entries.map(({ name, writes, purpose }) => ({ name, writes, rests: restsOn(nodes, writes), purpose }));
}
