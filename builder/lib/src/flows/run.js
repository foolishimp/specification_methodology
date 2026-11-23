import { done } from "../algorithms/done.js";
import { take_up } from "../algorithms/take_up.js";
import { decide, end, held, outcome, repeat, sequence, using } from "../kit/calculus.js";
import { now } from "../kit/clock.js";
import { Files } from "../services/files.js";
import { Git } from "../services/git.js";
import { Hold } from "../services/hold.js";
import { commitOf, committed } from "./commit.js";
import { logFound, note } from "./events.js";
import { gather, hereOf } from "./gather.js";
import { mergeIntoMain, takeMainIn } from "./merge.js";
import { faultEnding, minutesReached, steps } from "./step.js";
import { move, writeSimplest } from "./ticket.js";
import { at, boardOf, builds, checkoutOf, checkoutPlace, checkoutTop, holdOf, laneOfTicket, lineOf, open, openWorkspace, PLACES, recordedIn, releaseWords, running, ticketPath } from "./workspace.js";
/** The limit on active tickets while REQ-FLOW-009 is not in force (REQ-PARAM-001). */
const LIMIT = 1;
const built = (ending, printed) => ({ ending, printed: printed ?? [] });
/** The method release the definition file selects, with where its manager keeps it, where it says (D89). Where it cannot say, the release is named by its identity alone. */
const releaseOf = (ws) => {
    const release = ws.release;
    if (release === undefined)
        return end(undefined);
    return using(Files, (files) => decide(files.methodAt(release.uri, ws.root), (path) => end(path === undefined ? release : { ...release, path })));
};
/** `take-in`: main taken into the ticket's branch, and the ticket read in the active lane on main; the ending where either stops the run. */
const takeIn = (b) => decide(takeMainIn(b.ws, b.checkout, b.ticket, b.run), (taken) => "stopped" in taken
    ? end({ ending: "stopped", ticket: b.ticket, why: taken.stopped, ...(taken.files === undefined ? {} : { files: taken.files }) })
    : decide(boardOf(b.ws.root), (board) => end(laneOfTicket(board, b.ticket) !== "active" ? { ending: "stopped", ticket: b.ticket, why: `the ticket ${b.ticket} no longer lies in the active lane on main` } : undefined)));
/** One round of `build`: the steps on the governing graph, until none may run, where `done` holds; main taken in again where it moved, or the ticket merged. */
const round = (b, here) => (state) => decide(steps({ ws: b.ws, here, ticket: b.ticket, run: b.run, ...(b.release === undefined ? {} : { release: b.release }) }, b.ws.graph.graph, state), ({ traversed, state: after }) => {
    if ("ended" in traversed)
        return end({ leave: built(traversed.ended, after.failed) });
    const merging = using(Git, (git) => decide(git.holdsAll(b.checkout, b.ws.main), (holds) => !holds
        ? decide(takeIn(b), (stopped) => end(stopped === undefined ? { again: after } : { leave: built(stopped, after.failed) }))
        : decide(mergeIntoMain(b.ws, b.checkout, b.ticket, b.run), (m) => end({
            leave: built("stopped" in m ? { ending: "stopped", ticket: b.ticket, why: m.stopped, ...(m.files === undefined ? {} : { files: m.files }) } : { ending: "done", ticket: b.ticket, merged: m.merged }, after.failed)
        }))));
    return decide(outcome(merging), (o) => end("fault" in o ? { leave: built(faultEnding(b.ws.root, o.fault, b.ticket, after.vector), after.failed) } : o.value));
});
/** `build(t)`: the ticket held, pulled where it lies in the backlog, its checkout made, what an interrupted step left committed, main taken in, and the rounds. */
const build = (ws, ticket, lane, run) => {
    const checkout = checkoutOf(ws.root, ticket, ws.within);
    const b = { ws, ticket, run, checkout };
    const inHold = using(Git, (git) => sequence(lane === "backlog" ? sequence(move(ws, ws.root, ticket, "backlog", "active", run), note(ws.root, { event: "ticket pulled", run, ticket })) : end(undefined), git.checkoutOf(ws.root, lineOf(ticket), ws.main, at(ws.root, checkoutTop(ticket))), 
    // What an interrupted step left in the checkout is the result of that step: it is committed, not changed.
    // A merge git could not make is the user's to resolve: the run stays stopped, and commits nothing, until they have.
    decide(commitOf({ folder: checkout, line: lineOf(ticket) }, "the result of an interrupted step"), (left) => {
        if ("unresolved" in left) {
            const { unresolved } = left;
            return end(built({
                ending: "stopped",
                ticket,
                why: `git could not merge ${unresolved.join(", ")}, and the merge is not resolved. Resolve ${unresolved.length === 1 ? "it" : "them"} in the ticket's checkout, ${checkoutPlace(ticket, ws.within)}, and commit there`,
                files: unresolved.map((f) => `${checkoutPlace(ticket, ws.within)}/${f}`)
            }));
        }
        return sequence(left.commit === undefined ? end(undefined) : note(ws.root, { event: "commit made", run, ticket, commit: left.commit, why: "what an interrupted step left" }), decide(takeIn(b), (stopped) => stopped !== undefined
            ? end(built(stopped))
            : decide(hereOf(ws, ticket), (here) => decide(releaseOf(ws), (release) => {
                const state = { attempts: new Map(), began: now().millis, sessions: 0, failed: [] };
                return repeat(state, round({ ...b, ...(release === undefined ? {} : { release }) }, here), {
                    reached: (st) => minutesReached(ws, st) !== undefined,
                    leave: (st) => built({ ending: "stopped", ticket, ...(st.vector === undefined ? {} : { vector: st.vector }), why: minutesReached(ws, st) ?? "" }, st.failed)
                });
            }))));
    })));
    // A hold left by a run whose process ended says that run was cut off, with any session it started that neither returned nor failed (REQ-FLOW-007).
    return using(Hold, (hold) => decide(hold.left(holdOf(ws.root, ticket)), (left) => sequence(left ? note(ws.root, { event: "run cut off", run: b.run, ticket, why: "this run found the hold the cut-off run left; a session it started that neither returned nor failed was cut off with it" }) : end(undefined), decide(held(hold, holdOf(ws.root, ticket), inHold), (h) => end(h === "held" ? built({ ending: "refused", why: "held" }) : h.done)))));
};
/**
 * The release check of `run'` (REQ-FLOW-010): the record the settings on main
 * hold, as it stands, and what is running, from the manifest at the place the
 * library gives. The ending where the record is not there or is not what is
 * running; nothing where it is.
 */
const releaseRefused = (root, manifest) => using(Files, (files) => decide(files.read(at(root, PLACES.settings)), (settings) => decide(running(manifest), (now) => {
    const recorded = recordedIn(settings ?? "");
    return end(builds(recorded, now) ? undefined : { ending: "refused", why: "release", release: { recorded, running: now } });
})));
/** `run'`: refused where the release recorded is not what is running; then main read and judged, what the user left on main committed where no run holds a ticket, the ticket taken up, and built. */
const runOn = (root, main, within, named, run, manifest) => decide(releaseRefused(root, manifest), (refused) => refused !== undefined ? end(built(refused)) : runOnMain(root, main, within, named, run));
/** `run'` past the release check: main read and judged, what the user left on main committed where no run holds a ticket, the ticket taken up, and built. */
const runOnMain = (root, main, within, named, run) => decide(openWorkspace(root, main, within), (opened) => {
    if ("refused" in opened) {
        return end(built({ ending: "refused", why: opened.refused.some((r) => r.where === ".stdo-builder") ? "not set up" : "not well formed", reasons: opened.refused }));
    }
    const ws = opened;
    return using(Hold, (hold) => {
        const heldNow = (board) => decide(hold.held(board.active.map((t) => holdOf(root, t.name))), (files) => end(board.active.filter((t) => files.includes(holdOf(root, t.name))).map((t) => t.name)));
        // While another run holds a ticket, its session may be at work, and what lies in main's folder is judged at its return: nothing of main's is committed until then.
        const commitMain = decide(decide(boardOf(root), heldNow), (heldAtStart) => heldAtStart.length > 0
            ? end(undefined)
            : decide(commitOf({ folder: root, line: main }, "what the user changed by hand on main"), (onMain) => "unresolved" in onMain
                ? end({ ending: "refused", why: "unresolved", files: onMain.unresolved })
                : onMain.commit === undefined
                    ? end(undefined)
                    : sequence(note(root, { event: "commit made", run, commit: onMain.commit, why: "what the user left uncommitted on main" }), end(undefined))));
        return decide(commitMain, (refused) => refused !== undefined ? end(built(refused)) : decide(boardOf(root), (board) => decide(heldNow(board), (heldBy) => {
            const input = { board, held: heldBy, graph: ws.graph, limit: LIMIT, ...(named === undefined ? {} : { named }) };
            const first = take_up({ ...input, mainDone: true });
            // Only where the first two rules give nothing does the third rule of take_up turn on what done says on main.
            const taken = first.take === "none" && board.active.length === 0 && named === undefined
                ? decide(gather(ws, { folder: root, line: main }), (g) => end(take_up({ ...input, mainDone: done(ws.graph, g).done === "yes" })))
                : end(first);
            return decide(taken, (t) => {
                if (t.take === "none")
                    return end(built({ ending: "refused", why: t.why }));
                if (t.take !== "simplest")
                    return build(ws, t.name, t.lane, run);
                return decide(writeSimplest(root), (ticket) => sequence(decide(committed({ folder: root, line: main }, `board: the simplest ticket ${ticket}`, [ticketPath("backlog", ticket)]), (commit) => commit === undefined ? end(undefined) : note(root, { event: "commit made", run, ticket, commit, why: "the simplest ticket written" })), build(ws, ticket, "backlog", run)));
            });
        })));
    });
});
/** The entry of the run's ending, as every ending is logged. */
const ended = (root, run, ending) => note(root, {
    event: "run ended",
    run,
    ending: ending.ending,
    ...("ticket" in ending ? { ticket: ending.ticket } : {}),
    ...("vector" in ending && ending.vector !== undefined ? { vector: ending.vector } : {}),
    why: ending.ending === "refused" ? (ending.fault ?? ending.why) : ending.ending === "stopped" ? ending.why : ending.ending === "waiting" ? "the user is asked" : "the ticket is merged"
});
/**
 * `closing(x)`: `run ended` written, and the run ends as it reached. Where it
 * cannot be written, the run keeps that ending, since the log changes no
 * decision (L5), and says the log could not be written (D75).
 */
const closing = (root, run, ran) => decide(outcome(ended(root, run, ran.ending)), (o) => end("fault" in o ? { ...ran, logUnwritten: true } : ran));
/** The run refused for a fault met outside every repeat (D75). */
const refusedFor = (root, f, logStarted) => ({ ending: faultEnding(root, f, undefined, undefined), logStarted, printed: [] });
/**
 * A run on the workspace in `folder`, on the ticket the user names or the one
 * `take_up` gives, by the release whose manifest would be at `manifest`. It
 * fails with nothing (D75).
 */
export const run = (folder, named, manifest) => decide(outcome(open(folder)), (o) => {
    // `open` writes nothing to the log, so its fault names its own path, and the folder named stands for the root.
    if ("fault" in o)
        return end(refusedFor(folder, o.fault, false));
    const opened = o.value;
    if ("refused" in opened)
        return end(opened);
    const { root, main, within } = opened;
    const runId = now().written;
    const started = decide(logFound(root), (found) => using(Files, (files) => decide(files.read(at(root, PLACES.settings)), (settings) => sequence(note(root, { event: "run started", run: runId, release: releaseWords(recordedIn(settings ?? "")), ...(named === undefined ? {} : { ticket: named }), ...(found ? {} : { why: "the event log was not found; this run starts a new one" }) }), end(!found)))));
    return decide(outcome(started), (s) => {
        // A fault before `run started` is written ends the run as refused, and the log holds nothing of it.
        if ("fault" in s)
            return end(refusedFor(root, s.fault, false));
        const logStarted = s.value;
        return decide(outcome(runOn(root, main, within, named, runId, manifest)), (r) => "fault" in r
            // A fault met outside every repeat ends the run as refused; where it is in writing the log, the log holds nothing of it.
            ? r.fault._tag === "LogRefused" ? end(refusedFor(root, r.fault, logStarted)) : closing(root, runId, refusedFor(root, r.fault, logStarted))
            : closing(root, runId, { ending: r.value.ending, logStarted, printed: r.value.printed }));
    });
});
