import { covered, pathsOf } from "../graph/terms.js";
import { nodesOf } from "../graph/walk.js";
export function startOfLog() {
    return new Map();
}
/** One step of the fold. An entry it does not know is passed over and left as it is. */
export const logStep = (fold, entry) => {
    const ticket = entry.ticket;
    if (ticket === undefined)
        return fold;
    const runs = fold.get(ticket) ?? { sessions: [], attempts: {} };
    fold.set(ticket, runs);
    if (entry.event === "run ended" && entry.ending !== undefined) {
        runs.last = { ending: entry.ending, why: entry.why ?? "", ...(entry.at === undefined ? {} : { at: entry.at }) };
    }
    else if ((entry.event === "check run" || entry.event === "check passed" || entry.event === "check did not pass") && entry.vector !== undefined && entry.check !== undefined) {
        // The last step's vector, and the checks that did not say yes in it.
        if (runs.step?.vector !== entry.vector)
            runs.step = { vector: entry.vector, failing: [] };
        if (entry.result !== "yes" && !runs.step.failing.includes(entry.check))
            runs.step.failing.push(entry.check);
    }
    else if (entry.event === "verdict read" && entry.vector !== undefined) {
        // A verdict that does not say yes is among what said no in the step (D204).
        if (runs.step?.vector !== entry.vector)
            runs.step = { vector: entry.vector, failing: [] };
        if (entry.result !== "yes" && !runs.step.failing.includes("verdict"))
            runs.step.failing.push("verdict");
    }
    else if ((entry.event === "vector closed" || entry.event === "vector left open") && entry.vector !== undefined) {
        if (runs.step?.vector !== entry.vector)
            runs.step = { vector: entry.vector, failing: [] };
    }
    else if (entry.event === "session started" && entry.vector !== undefined && entry.kind !== undefined) {
        if (runs.step?.vector !== entry.vector)
            runs.step = { vector: entry.vector, failing: [] };
        runs.sessions.push({ vector: entry.vector, kind: entry.kind, ended: "under way", ...(entry.agent === undefined ? {} : { agent: entry.agent }) });
        if (entry.kind === "work")
            runs.attempts[entry.vector] = (runs.attempts[entry.vector] ?? 0) + 1;
    }
    else if ((entry.event === "session returned" || entry.event === "session failed") && entry.vector !== undefined) {
        const at = runs.sessions.findLastIndex((s) => s.vector === entry.vector && s.kind === entry.kind && s.ended === "under way");
        const seen = runs.sessions[at];
        if (seen !== undefined) {
            runs.sessions[at] = {
                ...seen,
                ended: entry.event === "session returned" ? "returned" : "failed",
                ...(entry.seconds === undefined ? {} : { seconds: entry.seconds }),
                ...(entry.cost === undefined ? {} : { cost: entry.cost }),
                ...(entry.unit === undefined ? {} : { unit: entry.unit }),
                ...(entry.calls === undefined ? {} : { calls: entry.calls })
            };
        }
    }
    return fold;
};
/** A cost as reported, where it is a plain number: text that reads as a finite number (D91). An older cost such as `0.40 USD` is none. */
function plainNumber(cost) {
    if (cost === undefined || cost.trim() === "")
        return undefined;
    const n = Number(cost);
    return Number.isFinite(n) ? n : undefined;
}
/** A cost as given: two places after the decimal point, rounded to the nearest (D195). */
const toCent = (n) => n.toFixed(2);
/** A session as `stands` gives it: a cost that is a plain number to the cent, any other as reported (D195). */
function given(session) {
    const n = plainNumber(session.cost);
    return n === undefined ? session : { ...session, cost: toCent(n) };
}
/** The sums of what a ticket's sessions reported: the costs that are plain numbers, where they share one unit or none (D102), summed as reported and the sum given to the cent (D195); and the calls (D91). Neither enters a decision. */
function spent(sessions) {
    const priced = sessions.flatMap((s) => {
        const n = plainNumber(s.cost);
        return n === undefined ? [] : [{ n, unit: s.unit }];
    });
    const units = new Set(priced.map((p) => p.unit));
    const [unit] = units;
    const calls = sessions.flatMap((s) => (s.calls === undefined ? [] : [s.calls]));
    return {
        ...(priced.length === 0 || units.size > 1 ? {} : { cost: toCent(priced.reduce((sum, p) => sum + p.n, 0)), ...(unit === undefined ? {} : { unit }) }),
        ...(calls.length === 0 ? {} : { calls: calls.reduce((sum, c) => sum + c, 0) })
    };
}
/**
 * What an active ticket waits on: the user's answer, or its induction, as the
 * ticket shows; otherwise as the event log shows the last run on it: held up
 * where it ended stopped, to be merged where it ended done, and otherwise in
 * build at the vector of its last step. Without the log, what a run finds.
 */
function waitsOf(shows, runs, logFound, foundOf) {
    if (shows?.ruling !== undefined)
        return { on: "ruling", vector: shows.ruling.vector, question: shows.ruling.question, from: "kept" };
    if (shows?.asked !== undefined) {
        const a = shows.asked;
        return { on: "answer", vector: a.vector, asset: a.asset, from: "ticket", ...(a.question === undefined ? {} : { question: a.question }), ...(a.when === undefined ? {} : { when: a.when }) };
    }
    if (shows !== undefined && !shows.inducted)
        return { on: "induction", from: "ticket" };
    const step = runs?.step;
    const last = runs?.last;
    const when = last?.at === undefined ? {} : { when: last.at };
    if (!logFound || step === undefined)
        return { on: "unknown" };
    if (last?.ending === "stopped")
        return { on: "held up", vector: step.vector, checks: step.failing, ...(foundOf === undefined ? {} : { found: foundOf(step.vector) }), from: "log", ...when };
    if (last?.ending === "done")
        return { on: "merge", from: "log", ...when };
    return { on: "work", vector: step.vector, from: "log", ...when };
}
export function stands(input) {
    const nodes = nodesOf(input.graph.graph, input.graph.registry);
    const lanes = [["backlog", input.board.backlog], ["active", input.board.active], ["done", input.board.done]];
    const onBoard = new Set();
    const tickets = [];
    for (const [lane, list] of lanes) {
        for (const t of list) {
            onBoard.add(t.name);
            const view = input.views.get(t.name);
            const changed = nodes.flatMap((node) => {
                const touched = covered(pathsOf(node), (view?.changes ?? []).map((c) => c.path));
                return touched.length === 0 ? [] : [{ asset: node.name, lines: (view?.changes ?? []).filter((c) => touched.includes(c.path)).reduce((sum, c) => sum + c.lines, 0) }];
            });
            const runs = input.log?.get(t.name);
            tickets.push({
                name: t.name,
                lane,
                ...(lane === "active" ? { waits: waitsOf(view?.ticket, input.log?.get(t.name), input.log !== undefined, input.foundOf) } : {}),
                changed,
                ...(runs === undefined ? {} : { runs: { ...(runs.last === undefined ? {} : { last: runs.last }), sessions: runs.sessions.map(given), attempts: runs.attempts, ...spent(runs.sessions) } })
            });
        }
    }
    return {
        tickets,
        withdrawn: input.branches.filter((b) => !onBoard.has(b)),
        log: input.log === undefined ? "not found" : "found"
    };
}
