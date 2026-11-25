/**
 * `done`: yes when `passes` says yes for every vector that takes part, on the
 * workspace as it is; otherwise the vectors and the checks that say no. For a
 * ticket, the vectors that take part are those of the term in force: its own,
 * or the default (REQ-ALG-006).
 *
 * @uses C3
 * @is REQ-ALG-011
 */
import { all } from "../kit/three_valued.js";
import { takesPart } from "./next.js";
import { passes } from "./passes.js";
export function done(graph, snapshot, within = graph.graph) {
    const saysNo = [];
    const results = [];
    for (const v of within.vectors) {
        if (!takesPart(graph, v, snapshot, within === graph.graph))
            continue;
        const p = passes(graph, v, snapshot);
        results.push(p.result);
        if (p.result !== "yes")
            saysNo.push({ vector: v.name, outcomes: p.outcomes.filter((o) => o.result !== "yes") });
    }
    return all(results) === "yes" ? { done: "yes" } : { done: "no", saysNo };
}
