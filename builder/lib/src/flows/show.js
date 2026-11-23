/**
 * Where the work stands, and the registry (REQ-ALG-012, REQ-GRAPH-005). The
 * flow gathers the board on main, the tickets' branches, for each active
 * ticket what its file in its checkout shows (`shownBy`: the vector delivered
 * for the user's decision with no answer after it, its question and when it
 * was asked, and whether a confirmation in it stands), the files each ticket
 * changed (C13: main against its branch, or what its merge brought) and one
 * fold of the event log (C10), and hands them to `stands`, which says for each
 * wait whether the ticket or the log gave it (D204). It reads no other record.
 * It gathers no checkout, so it runs no check and makes no identity of a file;
 * the identities of the graph's declarations, made with the graph from their
 * text (D168), and of the ticket's text (`hash-object`) touch no index, and
 * its git calls read lines and commits alone, so it writes no index of git's
 * (D76). It writes nothing. Each command begins with `open` and refuses a
 * graph that is not `well_formed` (design, CALCULUS.md section 5).
 *
 * @uses C3 C4 C8 C10 C13 C14 C17 H5
 * @is REQ-FLOW-001 REQ-ALG-012 REQ-GRAPH-005
 */
import { listing } from "../graph/registry.js";
import { awaiting, bindingOf, declaration, TICKET } from "../algorithms/facts.js";
import { recordsOf } from "../algorithms/passes.js";
import { logStep, startOfLog, stands } from "../algorithms/stands.js";
import { fieldsOf } from "../kit/field_lines.js";
import { hereOf, onCommit } from "./gather.js";
import { linesChanged, questionFor } from "./question.js";
import { decide, each, end, using } from "../kit/calculus.js";
import { Files } from "../services/files.js";
import { Git } from "../services/git.js";
import { EventLog } from "../services/log.js";
import { logOf } from "./events.js";
import { at, boardOf, checkoutOf, foundPath, lineOf, LINES, nodes, open, openWorkspace, ticketLines, userPart, vectors } from "./workspace.js";
const PREFIX = lineOf("");
/** `open`, then main judged `well_formed`, then `then` on the workspace. */
const opening = (folder, then) => decide(open(folder), (opened) => "refused" in opened ? end(opened) : decide(openWorkspace(opened.root, opened.main, opened.within), (ws) => ("refused" in ws ? end(ws) : then(ws))));
/**
 * What an active ticket shows, read from its file in its checkout alone
 * (REQ-ALG-012, D204): the vector delivered for the user's decision with no
 * answer after it, with its question and when it was asked; and whether a
 * confirmation in it stands, by the identities git holds under its commit
 * and of the ticket's text now (`hash-object`), so no index is written (D76).
 */
const shownBy = (ws, checkout, name) => using(Files, (files) => using(Git, (git) => decide(hereOf(ws, name), (here) => decide(here.ticket === undefined ? end(undefined) : files.read(at(checkout, here.ticket)), (written) => {
    if (written === undefined || here.ticket === undefined)
        return end(undefined);
    const lines = ticketLines(written);
    const first = ws.graph.graph.vectors.find((v) => v.first === true);
    const names = (vector) => {
        const v = vectors(ws).find((w) => w.name === vector);
        return v === undefined ? [] : recordsOf(ws.graph, v, "decision");
    };
    const delivered = awaiting(lines, names);
    const v = delivered === undefined ? undefined : vectors(ws).find((w) => w.name === delivered.vector);
    const b = bindingOf(lines);
    const stretch = b !== undefined && v?.first === true && b.ended?.line === "delivered" ? { inducting: { enters: b.bound.enters, ends: b.bound.ends } } : {};
    const seen = { identities: new Map(), ticket: { path: here.ticket, identity: "", ...stretch }, vectors: new Map() };
    // The lines changed are counted up to the commit the delivery names, as the run counted them (D211).
    return decide(v === undefined || delivered === undefined ? end(undefined) : linesChanged(ws, checkout, v, delivered.commit), (counted) => {
        const asked = v === undefined || delivered === undefined ? undefined : {
            vector: v.name,
            asset: v.first === true ? TICKET : names(v.name).join(", "),
            question: questionFor(ws, v, seen, written, name, undefined, counted),
            ...(delivered.when === undefined ? {} : { when: delivered.when })
        };
        const confirmation = first === undefined ? undefined : lines.findLast((l) => l.line === "resolved" && l.by === "user" && l.at === first.name);
        if (first === undefined || fieldsOf(written).get("simplest") === "yes")
            return end({ inducted: true, ...(asked === undefined ? {} : { asked }) });
        if (confirmation === undefined || confirmation.line !== "resolved" || confirmation.says !== "yes")
            return end({ inducted: false, ...(asked === undefined ? {} : { asked }) });
        return decide(onCommit(ws, checkout, confirmation.commit, name), (then) => decide(git.identityOfText(checkout, userPart(written)), (whole) => end({ inducted: then !== undefined && then.get(TICKET) === whole && then.get(declaration(first.name)) === ws.declared.get(declaration(first.name)), ...(asked === undefined ? {} : { asked }) })));
    });
}))));
export const show = (folder) => opening(folder, (ws) => {
    const { root, main } = ws;
    return using(Git, (git) => using(Files, (files) => using(EventLog, (log) => decide(boardOf(root), (board) => decide(git.linesNamed(root, [LINES]), (lines) => {
        const branches = lines.filter((b) => b.startsWith(PREFIX)).map((b) => b.slice(PREFIX.length));
        const active = each(board.active, (t) => {
            const checkout = checkoutOf(root, t.name, ws.within);
            return decide(branches.includes(t.name) ? files.exists(checkout) : end(false), (has) => decide(has ? shownBy(ws, checkout, t.name) : end(undefined), (shows) => decide(has ? git.changedLines(root, `${main}...${lineOf(t.name)}`) : end([]), (changes) => end([t.name, { ...(shows === undefined ? {} : { ticket: shows }), changes }]))));
        });
        return decide(git.mergesOn(root, main), (merges) => decide(active, (activeViews) => decide(each(board.done, (t) => decide(branches.includes(t.name) ? git.tipOf(root, lineOf(t.name)) : end(undefined), (tip) => {
            const merge = tip === undefined ? undefined : merges.find((m) => m.parents[1] === tip);
            const first = merge?.parents[0];
            return decide(merge === undefined || first === undefined ? end([]) : git.changedLines(root, first, merge.commit), (changes) => end([t.name, { changes }]));
        })), (doneViews) => decide(log.fold(logOf(root), startOfLog(), logStep), (logged) => end({ ...stands({ graph: ws.graph, board, branches, views: new Map([...activeViews, ...doneViews]), foundOf: foundPath, ...(logged === undefined ? {} : { log: logged }) }), within: ws.within })))));
    })))));
});
/** The registry of the governing graph: each graph function by name, with the nodes it writes, what it rests on and what it is for. */
export const registryOf = (folder) => opening(folder, (ws) => end(listing(ws.graph.registry, nodes(ws))));
