import { difference } from "../kit/map_difference.js";
import { covers } from "../kit/place_containment.js";
import { pathsOf } from "../graph/terms.js";
import { nodesOf, vectorsOf } from "../graph/walk.js";
import { placedOf } from "./well_formed.js";
/** The key a yes and a ruling give a file changed on main, before its path in the workspace: no key of a file of the folder begins so, nor one a ruling of an earlier release gave, which began `main:` or `checkout:` (REQ-FLOW-004, D257). */
export const LEFT = "left:";
/** The file at the top of the workspace's folder where what a build leaves is listed for git to ignore. A working session may write it (D99). */
const TOP_IGNORE = ".gitignore";
/** The keys of the parts of the branch's ticket, beside its path (D202, D226). */
export const PART = "#framework";
export const WORDS = "#words";
export const TRIAGE = "#triage";
/**
 * What a step writes, in the workspace's folder (REQ-ALG-008): for a working
 * session the nodes its vector writes and the top `.gitignore`, and for the
 * first vector's session the triage and the term of the branch's ticket; for
 * an evaluating session its findings and its verdict, and nothing else.
 * `brief` names the same places, so a session that keeps to its packet
 * changes nothing that is named to the user (D88, D99).
 */
export function writes(graph, vector, kind, ticket) {
    if (kind === "evaluation")
        return vector.evaluation === undefined ? [] : [vector.evaluation.findings, vector.evaluation.verdict];
    const own = new Set(placedOf(graph, vector).writes);
    const assets = nodesOf(graph.graph, graph.registry).filter((n) => own.has(n.name)).flatMap(pathsOf);
    return [...assets, TOP_IGNORE, ...(vector.first === true && ticket !== undefined ? [`${ticket}${TRIAGE}`] : [])];
}
/** What the framework and an evaluating session write between two readings: its own folder, and the findings and verdict of each evaluation (CALCULUS L2). */
export function apart(graph, places) {
    return [places.folder, ...vectorsOf(graph.graph, graph.registry).flatMap((v) => (v.evaluation === undefined ? [] : [v.evaluation.findings, v.evaluation.verdict]))];
}
/** The files whose identity differs, as added, changed or removed (C2). */
const differing = (start, end) => {
    const d = difference(start, end);
    return [
        ...d.added.map((path) => ({ path, how: "added" })),
        ...d.changed.map((path) => ({ path, how: "changed" })),
        ...d.removed.map((path) => ({ path, how: "removed" }))
    ];
};
/**
 * Each file that changed while the session worked, outside what its step
 * writes, and whether the identities from its start were missing. Where they
 * were, the commit's stand in, and nothing counts as what the step writes.
 * The branch's ticket is returned once, by its path, where a part of it the
 * step does not write differs.
 */
export function trespass(s) {
    const free = s.stood === true ? [] : writes(s.graph, s.vector, s.kind, s.ticket);
    const left = (path, now) => (now !== undefined && s.framework?.get(path) === now) || s.yes?.get(path) === (now ?? "");
    const inFolder = differing(s.start, s.end).filter((c) => {
        // The ticket's whole file is compared by its parts (D202, D226).
        if (s.ticket !== undefined && c.path === s.ticket && s.start.has(`${s.ticket}${PART}`))
            return false;
        if (free.some((place) => covers(place, c.path) || place === c.path))
            return false;
        return !left(c.path, s.end.get(c.path));
    });
    const ticketPart = s.ticket === undefined ? [] : inFolder.filter((c) => c.path.startsWith(`${s.ticket}#`));
    const files = inFolder.filter((c) => s.ticket === undefined || !c.path.startsWith(`${s.ticket}#`));
    const ticket = ticketPart.length === 0 || s.ticket === undefined ? [] : [{ path: s.ticket, how: "changed" }];
    // What main gained counts as no part of what the step writes, whatever the file; a yes counts at the identity main gave the file then (D257).
    const main = s.main === undefined ? [] : differing(s.main.start, s.main.end)
        .filter((c) => s.yes?.get(`${LEFT}${c.path}`) !== (s.main?.end.get(c.path) ?? ""))
        .map((c) => ({ ...c, on: "main" }));
    return { files: [...ticket, ...files], main, missing: s.stood === true };
}
