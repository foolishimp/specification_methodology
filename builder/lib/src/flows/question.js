/**
 * A question and its answer (REQ-FLOW-006). The framework asks the user where
 * a vector declares a decision, no answer stands and every other check
 * passes; the run then ends as waiting. The user answers with the product's
 * command, and the framework adds the answer to the ticket as the user's
 * resolution, with the commit it was given on, and commits it on the ticket's
 * branch. The answer runs no check, and reads no record but the ticket (D204).
 *
 * The command is the term `answer` of the calculus page (section 5): `open`,
 * main judged `well_formed`, a no with no reason refused, the ticket active
 * and its checkout there, and the answer written while the ticket is held.
 *
 * The answer is added at each node the vector writes that the user's yes
 * accepts, for that node, what it declares of itself and the nodes it depends
 * on, so it is read alike whoever wrote the node (D164, D168). The answer on
 * the first vector is read from the branch's ticket alone, so it confirms that
 * ticket alone (REQ-FLOW-004, D203).
 *
 * @uses C1 C2 C3 C5 C6 C17 H1 H5
 * @is REQ-FLOW-006 REQ-METHOD-006 REQ-FLOW-004 REQ-FLOW-007
 */
import { decide, each, end, held, sequence, using } from "../kit/calculus.js";
import { fieldsOf } from "../kit/field_lines.js";
import { pathsOf } from "../graph/terms.js";
import { covers } from "../kit/place_containment.js";
import { Git } from "../services/git.js";
import { awaiting } from "../algorithms/facts.js";
import { keptAt, listed } from "../algorithms/brief.js";
import { identitiesAt, recordsOf, shownTerm, since } from "../algorithms/passes.js";
import { placedOf } from "../algorithms/well_formed.js";
import { Files } from "../services/files.js";
import { Hold } from "../services/hold.js";
import { committed } from "./commit.js";
import { note } from "./events.js";
import { givenOn, hereOf, onCommit } from "./gather.js";
import { addLines, at, boardOf, checkoutOf, holdOf, nodes, open, openWorkspace, seenFrom, ticketLines, vectors } from "./workspace.js";
/**
 * The question, in plain words: what is being decided, what it rests on and
 * what follows from each answer. The work on a ticket lies in its checkout,
 * so where `checkout` names the ticket each path is given from the
 * workspace's folder, as the user opens it. `overturned` is what the
 * induction's checks found where the user changed the ticket after confirming
 * it and it no longer passed them, so the induction ran again: the question
 * says so (REQ-FLOW-004). `counted` is what changed in the nodes the vector
 * writes since main last held them (`linesChanged`, D211).
 */
export function questionFor(ws, v, s, ticketText, checkout, overturned, counted) {
    const places = new Map(nodes(ws).map((n) => [n.name, { ...n, place: pathsOf(n).map((p) => seenFrom(checkout, p, ws.within)).join(", ") }]));
    const ticket = s.ticket === "simplest" ? undefined : s.ticket;
    if (v.first === true) {
        const f = fieldsOf(ticketText);
        const term = shownTerm(ws.graph, f.get("term")) ?? [];
        const stretch = ticket?.inducting;
        return [
            `Is the ticket inducted as you want it? Its file is ${ticket === undefined ? "the ticket" : seenFrom(checkout, ticket.path, ws.within)}.`,
            `It says it is of kind ${f.get("kind") ?? "not given"} and class ${f.get("class") ?? "not given"}, that the work enters at ${f.get("enters") ?? "no node"} and ends at ${f.get("ends") ?? "no node"}, and that it touches ${f.get("scope") ?? "what it does not say"}.`,
            ...(stretch === undefined ? [] : [`In the place of the induction entry over ${stretch.enters} to ${stretch.ends}, which you confirmed before, it names the work from ${stretch.enters} to ${stretch.ends}.`]),
            ...(overturned === undefined ? [] : [`The ticket changed after you confirmed it, and did not pass the induction's checks: ${overturned}. The induction ran again on the ticket as it now is.`]),
            `It is to be carried out by ${term.length === 0 ? "no graph function" : term.join(", then ")}, one step each.`,
            "It rests on your words in the ticket, which are kept as you wrote them.",
            `Yes: the work is built by ${term.length === 1 ? "that step" : "those steps"}, in that order, and by no other.`,
            "No: give your reason; the ticket is inducted again, and the session is told where your reason is kept."
        ].join("\n");
    }
    const { rests, writes } = placedOf(ws.graph, v);
    const one = writes.length === 1;
    const seen = (n) => `${n} at ${places.get(n)?.place ?? n}`;
    // What must be true of each is its node's (D168).
    const results = writes.flatMap((n) => places.get(n)?.result ?? []);
    // Where the answer is kept at fewer nodes than are asked about, the question says at which (D164).
    const kept = keptAt(recordsOf(ws.graph, v, "decision"), writes);
    return [
        `Do you accept ${listed(writes.map(seen))}, as ${one ? "it now stands" : "they now stand"}?`,
        ...(kept === undefined ? [] : [`Your answer is ${kept}.`]),
        `${one ? "It is" : "They are"} to be what the graph says of ${one ? "it" : "them"}: ${results.join(" ")}`,
        `${one ? "It rests" : "They rest"} on ${rests.length === 0 ? "the ticket" : rests.map(seen).join(", ")}.`,
        ...(counted === undefined ? [] : countedWords(counted, (p) => seenFrom(checkout, p, ws.within))),
        "Yes: the run goes on from here when you start it again.",
        `No: give your reason; ${listed(writes)} ${one ? "is" : "are"} written again, and the session is told where your reason is kept.`
    ].join("\n");
}
/**
 * What changed in the nodes `v` writes, from the commit where `commit` and
 * main last met to `commit`: for each node, that it is new where main holds
 * none of it there; else each file of it that changed, how many of its lines
 * changed, the larger of those added and those taken out, and how many remain
 * as they were, those it held less those taken out (D211). It reads commits
 * alone, so it writes no index (D76). None for the first vector, which writes
 * no node, or where git finds no such commit.
 */
export const linesChanged = (ws, folder, v, commit) => {
    const writes = v.first === true ? [] : placedOf(ws.graph, v).writes;
    const pathsAt = (n) => {
        const node = nodes(ws).find((m) => m.name === n);
        return node === undefined ? [] : pathsOf(node);
    };
    if (writes.length === 0)
        return end(undefined);
    return using(Git, (git) => decide(git.mergeBase(folder, commit, ws.main), (base) => base === undefined ? end(undefined) : decide(git.underCommit(folder, base, writes.flatMap(pathsAt)), (held) => decide(git.changedLines(folder, base, commit), (changes) => each(writes, (name) => {
        if (!pathsAt(name).some((p) => held?.has(p) === true))
            return end({ name });
        const mine = changes.filter((c) => pathsAt(name).some((p) => covers(p, c.path)));
        return decide(each(mine, (c) => decide(git.textAt(folder, base, c.path), (was) => {
            const before = was === undefined ? 0 : linesOf(was);
            return end({ path: c.path, changed: Math.max(c.added, c.removed), remain: Math.max(0, before - c.removed), added: c.added, removed: c.removed });
        })), (files) => end({ name, files }));
    })))));
};
/** The lines of a text, as git counts them. */
const linesOf = (text) => (text === "" ? 0 : text.split("\n").length - (text.endsWith("\n") ? 1 : 0));
/** What changed since main last held the nodes, in the question's words (D211). */
const countedWords = (counted, seen) => {
    const lines = (n) => `${n} line${n === 1 ? "" : "s"}`;
    const held = counted.filter((c) => c.files !== undefined);
    return [
        ...counted.filter((c) => c.files === undefined).map((c) => `${c.name} is new: main holds none of it.`),
        ...held.flatMap((c) => (c.files ?? []).map((f) => `In ${c.name}, ${seen(f.path)}: ${lines(f.changed)} changed (${f.added} added, ${f.removed} taken out), and ${lines(f.remain)} remain as they were.`)),
        ...(held.length === 0 ? [] : [`Every other file of ${listed(held.map((c) => c.name))} is as it was when main last held it.`])
    ];
};
/**
 * Adds the user's answer to the ticket as the user's resolution, with the
 * ruling where the user gave one, and commits it on its branch (REQ-FLOW-006,
 * D204). It runs no check and reads no record but the ticket: the answer is
 * for the vector whose work the checklist shows delivered for the user's
 * decision with no answer of the user after it, and is given on the commit
 * that delivery names, where at each name it is kept under the content it
 * stands for is as that commit holds it (`since`, C2). Otherwise it is
 * refused, since the workspace is right where the two disagree.
 */
const answerOn = (ws, ticket, says, reason, ruling) => {
    const checkout = checkoutOf(ws.root, ticket, ws.within);
    const notAsked = { refused: `Nothing is asked on the ticket ${ticket} as it now stands. Start a run, and you are asked again.` };
    const inHold = decide(hereOf(ws, ticket), (here) => using(Files, (files) => decide(here.ticket === undefined ? end(undefined) : files.read(at(here.folder, here.ticket)), (written) => {
        const names = (vector) => {
            const v = vectors(ws).find((w) => w.name === vector);
            return v === undefined ? [] : recordsOf(ws.graph, v, "decision");
        };
        const delivered = written === undefined ? undefined : awaiting(ticketLines(written), names);
        const v = delivered === undefined ? undefined : vectors(ws).find((w) => w.name === delivered.vector);
        if (delivered === undefined || v === undefined || here.ticket === undefined)
            return end(notAsked);
        const path = here.ticket;
        const kept = names(v.name);
        return decide(givenOn(ws, here), (now) => decide(onCommit(ws, here.folder, delivered.commit, ticket), (then) => {
            if (then === undefined || kept.some((node) => since(ws.graph, node, identitiesAt(ws.graph, node, now, (key) => then.get(key)), now).length > 0))
                return end(notAsked);
            const lines = [
                ...kept.map((node) => ({ line: "resolved", by: "user", says, at: node, commit: delivered.commit, ...(reason === undefined ? {} : { reason }) })),
                ...(ruling === undefined || ruling.trim() === "" ? [] : [{ line: "ruling", commit: delivered.commit, words: ruling }])
            ];
            return sequence(addLines(here.folder, path, lines), note(ws.root, { event: "answer written", ticket, vector: v.name, result: says, path, ...(says === "no" ? { why: "the reason is in the ticket" } : {}) }), decide(committed({ folder: checkout, line: here.line }, `answer: ${says} to ${v.name}`, [path]), (commit) => commit === undefined ? end(undefined) : note(ws.root, { event: "commit made", ticket, vector: v.name, commit, why: "the user's answer" })), 
            // The user is asked only when every other outcome passes, so an answer of yes closes the vector.
            says === "yes" ? note(ws.root, { event: "vector closed", ticket, vector: v.name, why: "the user accepted it, and its other checks pass" }) : end(undefined), end({ answered: ticket, vector: v.name, says, paths: [path] }));
        }));
    })));
    return using(Hold, (hold) => decide(held(hold, holdOf(ws.root, ticket), inHold), (h) => end(h === "held" ? { refused: `A run is at work on the ticket ${ticket}. Answer when it has ended.` } : h.done)));
};
/** The command `answer` on the folder the library gives. */
export const answer = (folder, says, reason, named, ruling) => decide(open(folder), (opened) => "refused" in opened
    ? end(opened)
    : decide(openWorkspace(opened.root, opened.main, opened.within), (ws) => {
        if ("refused" in ws)
            return end(ws);
        if (says === "no" && (reason === undefined || reason.trim() === ""))
            return end({ refused: "An answer of no comes with your reason. Give it with --reason." });
        return decide(boardOf(ws.root), (board) => {
            const ticket = board.active.filter((t) => named === undefined || t.name === named)[0]?.name;
            if (ticket === undefined)
                return end({ refused: named === undefined ? "No ticket is active, so nothing is asked." : `The ticket ${named} is not active, so nothing is asked of it.` });
            return using(Files, (files) => decide(files.exists(checkoutOf(ws.root, ticket, ws.within)), (there) => there ? answerOn(ws, ticket, says, reason, ruling) : end({ refused: `The ticket ${ticket} has no checkout yet: start a run first.` })));
        });
    }));
