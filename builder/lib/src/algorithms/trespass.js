import { difference, paths } from "../kit/map_difference.js";
import { covers } from "../kit/place_containment.js";
import { pathsOf } from "../graph/terms.js";
import { nodesOf, vectorsOf } from "../graph/walk.js";
import { placedOf } from "./well_formed.js";
/** The file at the top of the checkout where what a build leaves is listed for git to ignore. A working session may write it (D99). */
const TOP_IGNORE = ".gitignore";
/**
 * The places a session must not change in one folder, beside the tickets: the
 * files the framework and the definition file name, every asset the vector
 * does not write and every verdict; and those it may write beside its own
 * asset, the findings and verdict of an evaluating session, or the top
 * `.gitignore` for a working session. `trespass` and `brief` both take them
 * from here, so a session that keeps to its brief does not trespass (D88,
 * D99).
 */
export function guarded(graph, vector, kind, places, side = "checkout") {
    const onMain = side === "main";
    // A working session may write each node its vector writes.
    const own = new Set(placedOf(graph, vector).writes);
    const assets = nodesOf(graph.graph, graph.registry)
        .filter((n) => onMain || kind === "evaluation" || !own.has(n.name))
        .flatMap(pathsOf);
    const verdicts = vectorsOf(graph.graph, graph.registry).flatMap((v) => (v.evaluation === undefined ? [] : [v.evaluation.verdict]));
    return {
        fixed: [places.definition, places.settings, places.graph, places.registry, ...places.own, ...assets, ...verdicts],
        free: onMain ? [] : kind === "work" ? [TOP_IGNORE] : vector.evaluation === undefined ? [] : [vector.evaluation.findings, vector.evaluation.verdict]
    };
}
/** What the framework and an evaluating session write between two readings: its own folder, and what `guarded` leaves free to each evaluating session (CALCULUS L2). */
export function apart(graph, places) {
    return [places.folder, ...vectorsOf(graph.graph, graph.registry).flatMap((v) => guarded(graph, v, "evaluation", places).free)];
}
/** The key of the framework's part of the branch's ticket, beside the ticket's path, under which a snapshot holds the identity of that part alone (D202). */
export const PART = "#framework";
export function trespass(s) {
    const { graph, vector, kind, places } = s;
    const onMain = s.side === "main";
    const { fixed, free } = guarded(graph, vector, kind, places, s.side);
    const ownTicket = kind === "work" && vector.first === true ? s.ticket : undefined;
    const tickets = new Set(onMain ? [] : [...s.start.keys()].filter((path) => path !== ownTicket && places.lanes.some((lane) => covers(lane, path))));
    const isProtected = (path) => !free.some((place) => covers(place, path)) && (tickets.has(path) || fixed.some((place) => covers(place, path)));
    const only = (m) => new Map([...m].filter(([path]) => isProtected(path)));
    // Where the framework's part of the branch's ticket differs, the ticket is returned (REQ-ALG-008).
    return [...new Set(paths(difference(only(s.start), only(s.end))).map((path) => (path.endsWith(PART) ? path.slice(0, -PART.length) : path)))];
}
