/**
 * A question and its answer (REQ-FLOW-006). The framework asks the user where
 * a vector declares a decision, no answer stands and every other check
 * passes; the run then ends as waiting. The user answers with the product's
 * command, and the framework adds the answer to the ticket as the user's
 * resolution, with the commit it was given on, and commits it on the ticket's
 * branch. The answer runs no check, and reads no record but the ticket, and
 * the hold and the identities kept from a session's start among the
 * workspace's notes, under git's own directory (D204, D245). Where a run's
 * start would put the commit's identities in place of a session's, the
 * answer is refused, since a run asks the user on every file that differs
 * from the commit that stands in: the one the session started from, or the
 * one the folder is on (D246, D255).
 *
 * The command is the term `answer` of the calculus page (section 5): `open`,
 * main judged `well_formed`, a no with no reason refused, the ticket active
 * and the folder on its branch, and the answer written while the ticket is
 * held.
 *
 * The answer is added at each node the vector writes that the user's yes
 * accepts, for that node, what it declares of itself and the nodes it depends
 * on, so it is read alike whoever wrote the node (D164, D168). The answer on
 * the first vector is read from the branch's ticket alone, so it confirms that
 * ticket alone (REQ-FLOW-004, D203).
 *
 * @uses C1 C2 C3 C5 C6 C17 H1 H5
 * @is REQ-FLOW-006 REQ-METHOD-006 REQ-FLOW-004 REQ-FLOW-007 REQ-ALG-008
 */
import { decide, each, end, sequence, using } from "../kit/calculus.js";
import { fieldsOf } from "../kit/field_lines.js";
import { pathsOf } from "../graph/terms.js";
import { covers } from "../kit/place_containment.js";
import { Git } from "../services/git.js";
import { awaiting, lineText } from "../algorithms/facts.js";
import { elsewhere, mainOf, placedOf as branchesOf } from "./branch.js";
import { keptAt, listed } from "../algorithms/brief.js";
import { identitiesAt, recordsOf, shownTerm, since } from "../algorithms/passes.js";
import { placedOf } from "../algorithms/well_formed.js";
import { Files } from "../services/files.js";
import { Hold } from "../services/hold.js";
import { committed, committedText } from "./commit.js";
import { note } from "./events.js";
import { givenOn, hereOf, onCommit } from "./gather.js";
import { noteRuling, settle, standing, standInRefused, yesOn } from "./changed.js";
import { addLines, at, frameworkPart, holdOf, linesRead, markOf, nodes, open, openWorkspace, vectors, withLines } from "./workspace.js";
/**
 * The identity of each line of a ticket's framework part that is not among
 * those it held at the session's start, as the branch's tip then holds it,
 * nor among the rulings the framework itself added since, which `own` names:
 * the lines that changed while the session worked (REQ-FLOW-004, D230). A
 * line is matched once, so a copy of a line that was there is named too.
 */
const foreignLines = (folder, now, atStart, own) => {
    const { added } = frameworkPart(now).split("\n").reduce((m, w) => {
        const i = m.left.indexOf(w);
        return i < 0 ? { left: m.left, added: w === "" ? m.added : [...m.added, w] } : { left: [...m.left.slice(0, i), ...m.left.slice(i + 1)], added: m.added };
    }, { left: frameworkPart(atStart).split("\n"), added: [] });
    return using(Git, (git) => decide(each(added, (w) => git.identityOfText(folder, w)), (ids) => end(ids.reduce((o, id) => {
        const i = o.own.indexOf(id);
        return i < 0 ? { own: o.own, foreign: [...o.foreign, id] } : { own: [...o.own.slice(0, i), ...o.own.slice(i + 1)], foreign: o.foreign };
    }, { own, foreign: [] }).foreign)));
};
/**
 * The question, in plain words: what is being decided, what it rests on and
 * what follows from each answer. Each path is given from the workspace's
 * folder, as the user opens it. `overturned` is what the
 * induction's checks found where the user changed the ticket after confirming
 * it and it no longer passed them, so the induction ran again: the question
 * says so (REQ-FLOW-004). `counted` is what changed in the nodes the vector
 * writes since main last held them (`linesChanged`, D211).
 */
export function questionFor(ws, v, s, ticketText, overturned, counted) {
    const places = new Map(nodes(ws).map((n) => [n.name, { ...n, place: pathsOf(n).join(", ") }]));
    const ticket = s.ticket === "simplest" ? undefined : s.ticket;
    if (v.first === true) {
        const f = fieldsOf(ticketText);
        const term = shownTerm(ws.graph, f.get("term")) ?? [];
        const stretch = ticket?.inducting;
        return [
            `Is the ticket inducted as you want it? Its file is ${ticket === undefined ? "the ticket" : ticket.path}.`,
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
        ...(counted === undefined ? [] : countedWords(counted, (p) => p)),
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
    const folder = ws.root;
    const notAsked = { refused: `Nothing is asked on the ticket ${ticket} as it now stands. Start a run, and you are asked again.` };
    // Where a file differs from the identities kept from a session's start on which no yes was given, the answer is the user's ruling on what changed: for that session's step, a yes on each file that then differs, as it then is. Only its line is committed, onto the ticket as the branch holds it, and nothing it is given on (REQ-FLOW-006 step 3, D227).
    const ruled = (here, path, kept, changed, now) => using(Files, (files) => using(Git, (git) => decide(files.read(at(here.folder, path)), (written) => decide(kept.commit === undefined ? end(undefined) : git.textAt(here.folder, kept.commit, path), (atStart) => 
    // A ruling on the branch's ticket, a yes or a no, names each line of its framework's part that changed while the session worked, by its identity, so that none is read as the user's answer whatever the user rules (REQ-FLOW-004, D230). The ticket changed on main, the branch it left, is not the branch's ticket (D257).
    decide(changed.some((c) => c.path === path && c.on !== "main") ? foreignLines(here.folder, written ?? "", atStart ?? "", kept.own ?? []) : end([]), (foreign) => {
        const yes = says === "yes" ? yesOn(changed, now, here.ticket) : [];
        const line = { line: "changed", says, vector: kept.vector, files: yes, ...(foreign.length === 0 ? {} : { foreign }) };
        return sequence(addLines(here.folder, path, [line]), 
        // The ruling is the framework's own: the identity of its line is noted, and the comparison takes that line out of the framework's part, so it is not named and the session's lines are, after a no as before it; each file of a yes is noted, where the comparison reads it (D230).
        decide(git.identityOfText(here.folder, lineText(line)), (id) => noteRuling(ws, ticket, kept, id, yes)), note(ws.root, { event: "answer written", ticket, vector: kept.vector, result: says, path, why: `the user's ruling on what changed while a session worked${says === "no" ? "; the reason is in the answer's words" : ""}` }), decide(git.textAt(here.folder, here.line, path), (onLine) => decide(committedText({ folder, line: here.line }, `ruling: ${says} on what changed at ${kept.vector}`, path, withLines(onLine ?? "", [line])), (commit) => commit === undefined ? end(undefined) : note(ws.root, { event: "commit made", ticket, vector: kept.vector, commit, why: "the user's ruling on what changed" }))), end({ answered: ticket, vector: kept.vector, says, paths: [path] }));
    })))));
    // Where the record kept finds nothing that differs, it is settled before the answer is written for a delivery, so the answer's own line is never compared with it (D227).
    // Where a run's start would put the commit's identities in place of a session's, which `standing` says alike for both, the answer is refused and writes nothing: a run asks the user on every file that differs from the commit that stands in (REQ-FLOW-006, D246, D255).
    const inHold = (cut) => decide(hereOf(ws, ticket), (here) => decide(standing(ws, here, ticket, cut), (s) => "standIn" in s
        ? end({ refused: standInRefused(ticket) })
        : "kept" in s && s.changed.length > 0 && here.ticket !== undefined
            ? ruled(here, here.ticket, s.kept, s.changed, s.now)
            : sequence("kept" in s ? settle(ws, ticket, s.kept) : end(undefined), delivery(here, end(undefined)))));
    const delivery = (here, beforeWriting) => using(Files, (files) => decide(here.ticket === undefined ? end(undefined) : files.read(at(here.folder, here.ticket)), (written) => {
        const names = (vector) => {
            const v = vectors(ws).find((w) => w.name === vector);
            return v === undefined ? [] : recordsOf(ws.graph, v, "decision");
        };
        return decide(linesRead(here.folder, written ?? ""), (read) => {
            const delivered = written === undefined ? undefined : awaiting(read, names);
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
                return sequence(beforeWriting, addLines(here.folder, path, lines), note(ws.root, { event: "answer written", ticket, vector: v.name, result: says, path, ...(says === "no" ? { why: "the reason is in the ticket" } : {}) }), decide(committed({ folder, line: here.line }, `answer: ${says} to ${v.name}`, [path]), (commit) => commit === undefined ? end(undefined) : note(ws.root, { event: "commit made", ticket, vector: v.name, commit, why: "the user's answer" })), 
                // The user is asked only when every other outcome passes, so an answer of yes closes the vector.
                says === "yes" ? note(ws.root, { event: "vector closed", ticket, vector: v.name, why: "the user accepted it, and its other checks pass" }) : end(undefined), end({ answered: ticket, vector: v.name, says, paths: [path] }));
            }));
        });
    }));
    // While a run holds the ticket, the answer is refused, naming the hold's file and its process. So it is while a process the framework knows to be of a session on the ticket is alive, or, where a cut-off run left its hold, one it cannot place that started after that run did: the answer looks as the start of a run does, ends no process, and names each (REQ-FLOW-006, D216, D223).
    const hold = holdOf(ws.notes, ticket);
    const seen = hold;
    const heldWords = (by) => ({ refused: `A run is at work on the ticket ${ticket}: the hold ${seen} names the process ${by === undefined ? "that holds it" : `${by.pid}${by.start === undefined ? "" : `, started ${by.start}`}`}. Answer when it has ended.` });
    const aliveWords = (alive, unplaced) => ({
        refused: [
            ...(alive.length === 0 ? [] : [`Processes of a session on the ticket ${ticket} are alive: ${alive.join("; and ")}. The next run on the ticket ends them.`]),
            ...(unplaced.length === 0 ? [] : [`The framework cannot place ${unplaced.join("; and ")}: each started after the run cut off on the ticket did, has no parent left alive, is of the session by neither its parent, its group nor its mark, shows no environment, and works in the workspace's folder. A job of your own there is such a process. It ends no such process.`]),
            "Nothing is written. End each of them, then answer."
        ].join(" ")
    });
    return using(Hold, (holds) => decide(holds.held([hold]), (holders) => holders.length > 0 ? end(heldWords(holders[0]?.by)) : decide(holds.left(hold), (left) => decide(holds.alive({ mark: markOf(ws.root, ticket), folder, ...(left?.since === undefined ? {} : { since: left.since }) }), (found) => "cannot" in found
        // Where the table of processes cannot be read, the answer is refused in the one sentence of D249, as a run is, and names no process (REQ-FLOW-006).
        ? end({ refused: found.table !== undefined ? `The answer is refused, and nothing is written. ${found.cannot} Then answer again.` : `The framework cannot tell whether a process of a session on the ticket ${ticket} is alive: ${found.cannot}. Nothing is written.` })
        : found.alive.length > 0 || found.unplaced.length > 0
            ? end(aliveWords(found.alive, found.unplaced))
            // A hold a cut-off run left is left so, so the next run notes the cut-off and says what it cannot tell (D232).
            : decide(holds.keeping(hold, inHold(left !== undefined)), (h) => end("done" in h ? h.done : heldWords(h.heldBy)))))));
};
/** The command `answer` on the folder the library gives: refused while a ticket is active and the folder is not on its branch, naming both (REQ-FLOW-001, D239). */
export const answer = (folder, says, reason, named, ruling) => decide(open(folder), (opened) => "refused" in opened
    ? end(opened)
    : decide(branchesOf(opened.root, opened.on), (placed) => decide(openWorkspace(opened.root, mainOf(placed) ?? "", opened.within, opened.on), (ws) => {
        if ("refused" in ws)
            return end(ws);
        if (says === "no" && (reason === undefined || reason.trim() === ""))
            return end({ refused: "An answer of no comes with your reason. Give it with --reason." });
        const ticket = placed.active.filter((t) => named === undefined || t.name === named)[0]?.name;
        if (ticket === undefined)
            return end({ refused: named === undefined ? "No ticket is active, so nothing is asked." : `The ticket ${named} is not active, so nothing is asked of it.` });
        const off = elsewhere(placed);
        return off !== undefined ? end({ refused: off }) : answerOn(ws, ticket, says, reason, ruling);
    })));
