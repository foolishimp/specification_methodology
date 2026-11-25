import { ASKED } from "./facts.js";
import { passes, recordAt, recordsOf, since } from "./passes.js";
import { placedOf } from "./well_formed.js";
export function open(graph, vector, snapshot) {
    return passes(graph, vector, snapshot).result !== "yes";
}
/** The nodes it rests on, and the ticket without its term under ASKED, whose content changed since its verdict or answer was given, each compared on what that record stands for. */
export function changed(graph, vector, snapshot) {
    const kind = vector.evaluation !== undefined ? "evaluation" : "decision";
    const keys = [...placedOf(graph, vector).rests, ASKED];
    const differs = new Set(recordsOf(graph, vector, kind).flatMap((at) => {
        const record = recordAt(at, kind, snapshot);
        return record === undefined ? [] : since(graph, at, record.on, snapshot);
    }));
    return keys.filter((key) => differs.has(key));
}
