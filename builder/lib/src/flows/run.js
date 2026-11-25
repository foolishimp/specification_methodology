import { done } from "../algorithms/done.js";
import { take_up } from "../algorithms/take_up.js";
import { readLine } from "../algorithms/facts.js";
import { decide, each, end, held, outcome, repeat, sequence, using } from "../kit/calculus.js";
import { now } from "../kit/clock.js";
import { Files } from "../services/files.js";
import { Git } from "../services/git.js";
import { Hold } from "../services/hold.js";
import { BY_HAND, commitOf, committed } from "./commit.js";
import { logFound, logsStarted, note } from "./events.js";
import { gather, hereOf } from "./gather.js";
import { pull, placedOf, takeUp } from "./branch.js";
import { changedQuestion, recordOf, resultPaths, settle, standing, stoodIn } from "./changed.js";
import { fromTop, mergeIntoMain, resolveWhere, takeMainIn } from "./merge.js";
import { faultEnding, minutesReached, steps } from "./step.js";
import { writeSimplest } from "./ticket.js";
import { at, boardAt, boardOf, builds, frameworkPart, holdOf, markOf, open, openWorkspace, PLACES, recordedIn, releaseWords, running, ticketPath, vectors } from "./workspace.js";
/** The limit on active tickets while REQ-FLOW-009 is not in force (REQ-PARAM-001). */
const LIMIT = 1;
const built = (ending, printed, noted) => ({ ending, printed: printed ?? [], ...(noted === undefined || noted.length === 0 ? {} : { noted }) });
/** The run's words on what it cannot tell, before those of its ending (D228). */
const withSaid = (said, f) => said.length === 0 ? f : decide(f, (b) => end({ ...b, noted: [...said, ...(b.noted ?? [])] }));
/** The method release the definition file selects, with where its manager keeps it, where it says (D89). Where it cannot say, the release is named by its identity alone. */
const releaseOf = (ws) => {
    const release = ws.release;
    if (release === undefined)
        return end(undefined);
    return using(Files, (files) => decide(files.methodAt(release.uri, ws.root), (path) => end(path === undefined ? release : { ...release, path })));
};
/**
 * Git's refusal to take main in or to merge, as an ending: the run is refused where it has made no step, and stops otherwise; a step is made
 * where a session of the run started (REQ-FLOW-008, REQ-FLOW-003, D240).
 */
const refusedOrStopped = (b, stepped, why, files) => stepped
    ? { ending: "stopped", ticket: b.ticket, why, ...(files === undefined ? {} : { files }) }
    : { ending: "refused", why: "main", fault: why, ...(files === undefined ? {} : { files }) };
/** `take-in`: main taken into the ticket's branch, and the ticket read in the active lane on main, by git; the ending where either ends the run, `stepped` where a step of the run was made. */
const takeIn = (b, stepped) => decide(takeMainIn(b.ws, b.ticket, b.run), (taken) => "stopped" in taken
    ? end(taken.refused === true ? refusedOrStopped(b, stepped, taken.stopped, taken.files) : { ending: "stopped", ticket: b.ticket, why: taken.stopped, ...(taken.files === undefined ? {} : { files: taken.files }) })
    : using(Git, (git) => decide(git.textAt(b.ws.root, b.ws.main, ticketPath("active", b.ticket)), (onMain) => end(onMain === undefined ? { ending: "stopped", ticket: b.ticket, why: `the ticket ${b.ticket} no longer lies in the active lane on ${b.ws.main}, the branch it left` } : undefined))));
/** One round of `build`: the steps on the governing graph, until none may run, where `done` holds; main taken in again where it moved, or the ticket merged. */
const round = (b, here) => (state) => decide(steps({ ws: b.ws, here, ticket: b.ticket, run: b.run, ...(b.release === undefined ? {} : { release: b.release }) }, b.ws.graph.graph, state), ({ traversed, state: after }) => {
    if ("ended" in traversed)
        return end({ leave: built(traversed.ended, after.failed, after.noted) });
    const merging = using(Git, (git) => decide(git.holdsAll(b.ws.root, b.ws.main), (holds) => !holds
        ? decide(takeIn(b, after.sessions > 0), (stopped) => end(stopped === undefined ? { again: after } : { leave: built(stopped, after.failed, after.noted) }))
        : decide(mergeIntoMain(b.ws, b.ticket, b.run), (m) => end({
            leave: built("stopped" in m
                ? m.refused === true ? refusedOrStopped(b, after.sessions > 0, m.stopped, m.files) : { ending: "stopped", ticket: b.ticket, why: m.stopped, ...(m.files === undefined ? {} : { files: m.files }) }
                : { ending: "done", ticket: b.ticket, merged: m.merged, into: m.into, ...(m.outside === undefined ? {} : { outside: m.outside }) }, after.failed, after.noted)
        }))));
    return decide(outcome(merging), (o) => end("fault" in o ? { leave: built(faultEnding(b.ws.root, o.fault, b.ticket, after.vector), after.failed) } : o.value));
});
/** `build(t)`: the ticket held, pulled where it lies in the backlog, with the folder put on its branch, main taken in, and the rounds. */
const build = (ws, ticket, lane, run) => {
    const b = { ws, ticket, run };
    const rounds = decide(takeIn(b, false), (stopped) => stopped !== undefined
        ? end(built(stopped))
        : decide(hereOf(ws, ticket), (here) => decide(releaseOf(ws), (release) => {
            const state = { attempts: new Map(), began: now().millis, sessions: 0, failed: [] };
            return repeat(state, round({ ...b, ...(release === undefined ? {} : { release }) }, here), {
                reached: (st) => minutesReached(ws, st) !== undefined,
                leave: (st) => built({ ending: "stopped", ticket, ...(st.vector === undefined ? {} : { vector: st.vector }), why: minutesReached(ws, st) ?? "" }, st.failed)
            });
        })));
    const inHold = lane === "backlog"
        ? decide(pull(ws, ticket, run), (refused) => (refused !== undefined ? end(built({ ending: "refused", why: "branch", fault: refused })) : rounds))
        : rounds;
    // A hold left by a run whose process ended says that run was cut off, with any session it started that neither returned nor failed (REQ-FLOW-007). On an active ticket, `run'` has noted it and taken that hold already (D232); so this finds one the start of the run did not see.
    return using(Hold, (hold) => decide(hold.left(holdOf(ws.notes, ticket)), (left) => sequence(left !== undefined ? note(ws.root, { event: "run cut off", run: b.run, ticket, why: "this run found the hold the cut-off run left; a session it started that neither returned nor failed was cut off with it" }) : end(undefined), decide(held(hold, holdOf(ws.notes, ticket), inHold), (h) => end("done" in h ? h.done : built({ ending: "refused", why: "held", holds: [{ file: holdOf(ws.notes, ticket), ...(h.heldBy === undefined ? {} : { by: h.heldBy }) }] }))))));
};
/** The vector of a session whose record of its start cannot serve and gives no step the graph holds: the last whose work began, by the ticket's checklist, of those the graph holds; else the first (D241, D246). */
const lastBegun = (ws, written) => frameworkPart(written ?? "").split("\n").reduce((v, l) => {
    const line = readLine(l);
    return (line?.line === "began" || line?.line === "bound" || line?.line === "delivered") && vectors(ws).some((w) => w.name === line.vector) ? line.vector : v;
}, undefined) ?? vectors(ws).find((v) => v.first === true)?.name ?? vectors(ws)[0]?.name ?? "";
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
/** `run'`: refused where the release recorded is not what is running; then the branch looked at, what is not committed told apart and committed where no run holds a ticket, the ticket taken up, and built. */
const runOn = (root, on, within, named, run, manifest) => decide(releaseRefused(root, manifest), (refused) => refused !== undefined ? end(built(refused)) : runOnMain(root, on, within, named, run));
/** `run'` past the release check. */
const runOnMain = (root, on, within, named, run) => decide(openWorkspace(root, on ?? "", within, on), (opened) => {
    if ("refused" in opened) {
        return end(built({ ending: "refused", why: opened.refused.some((r) => r.where === ".stdo-builder") ? "not set up" : "not well formed", reasons: opened.refused }));
    }
    const found = opened;
    // The hold's file lies among the workspace's notes, under git's own directory, and is named by its path (D245).
    const notes = found.notes;
    return using(Hold, (hold) => {
        const holdsNow = (board) => hold.held(board.active.map((t) => holdOf(notes, t.name)));
        const heldNow = (board) => decide(holdsNow(board), (files) => end(board.active.filter((t) => files.some((f) => f.file === holdOf(notes, t.name))).map((t) => t.name)));
        const seen = (t) => holdOf(notes, t);
        const leftOver = decide(boardOf(root), (board) => decide(each(board.active.map((t) => t.name), (t) => decide(hold.held([holdOf(notes, t)]), (holders) => holders.length > 0 ? end(undefined) : decide(hold.left(holdOf(notes, t)), (left) => {
            // The session's folder is the workspace's own, and, where a run was cut off on the ticket, when it started: a process the framework cannot place started no earlier (D223).
            const sought = { mark: markOf(root, t), folder: root, ...(left?.since === undefined ? {} : { since: left.since }) };
            const where = left === undefined ? `its hold, ${seen(t)}, is free` : `the run cut off on it left its hold at ${seen(t)}`;
            return decide(hold.alive(sought), (alive) => {
                // Where the table cannot be read, the words are the one sentence of D249, and name no process.
                if ("cannot" in alive)
                    return end(alive.table !== undefined ? { cannot: alive.cannot, table: true } : { cannot: `the framework cannot tell whether a process of a session on the ticket ${t} is alive, where ${where}: ${alive.cannot}` });
                if (left === undefined && alive.alive.length === 0)
                    return end(undefined);
                return decide(hold.end(sought), (e) => sequence(e.ended === 0 ? end(undefined) : note(root, { event: "session processes ended", run, ticket: t, processes: e.ended, why: `${where}, and these processes of a session on the ticket were alive${e.unended === undefined ? "" : `; the session is not over: ${e.unended}`}` }), end(e.unended === undefined ? undefined : { alive: `a session on the ticket ${t} is not over, where ${where}: ${e.unended}` })));
            });
        }))), (all) => {
            const table = all.find((f) => f !== undefined && "cannot" in f && f.table === true);
            if (table !== undefined && "cannot" in table)
                return end({ ending: "refused", why: "ps", fault: table.cannot });
            const cannot = all.flatMap((f) => (f !== undefined && "cannot" in f ? [f.cannot] : []));
            const alive = all.flatMap((f) => (f !== undefined && "alive" in f ? [f.alive] : []));
            return end(cannot.length > 0 ? { ending: "refused", why: "cannot tell", fault: [...cannot, ...alive].join("; ") } : alive.length > 0 ? { ending: "refused", why: "alive", fault: alive.join("; ") } : undefined);
        }));
        const cutOff = decide(boardOf(root), (board) => decide(each(board.active.map((t) => t.name), (t) => decide(hold.left(holdOf(notes, t)), (left) => decide(left === undefined ? end(undefined) : recordOf(found, t), (r) => end(left === undefined ? { said: [], cut: [] } : {
            said: r !== undefined && "kept" in r ? [`A run was cut off on the ticket ${t} while its session on ${r.kept.vector} worked: the framework cannot tell what changed then among the repository's branches, tags and stash${within === "" ? "" : ", nor outside the workspace's folder"}.`] : [],
            cut: r !== undefined && "settled" in r ? [] : [t]
        })))), (all) => end({ said: all.flatMap((c) => c.said), cut: all.flatMap((c) => c.cut) })));
        // Then, where a run cut off on an active ticket left its hold, the run notes that it was cut off, before it compares, whether it then waits, is refused or goes on; it takes the hold and lets it go, so the cut-off is noted once, and neither `build` nor a later run finds that hold left (REQ-FLOW-007, D232).
        const cutOffNoted = decide(boardOf(root), (board) => decide(each(board.active.map((t) => t.name), (t) => decide(hold.left(holdOf(notes, t)), (left) => left === undefined ? end(undefined) : sequence(note(root, { event: "run cut off", run, ticket: t, why: "this run found the hold the cut-off run left; a session it started that neither returned nor failed was cut off with it" }), decide(held(hold, holdOf(notes, t), end(undefined)), () => end(undefined))))), () => end(undefined)));
        // The table of processes is read once before anything else on a ticket and before any session is started; where it cannot be read, the run starts nothing and is refused, in the one sentence of D249 (REQ-FLOW-003 step 1).
        const tableRead = decide(hold.table(), (t) => end(t === undefined ? undefined : { ending: "refused", why: "ps", fault: t.cannot }));
        return decide(decide(tableRead, (t) => t !== undefined ? end(t) : leftOver), (cannot) => cannot !== undefined ? end(built(cannot)) : decide(cutOff, (cut) => decide(sequence(cutOffNoted, placedOf(root, on)), (placed) => 
        // Then, before anything is committed, the branch the folder is on is looked at, and taken up where the run can (REQ-FLOW-003 step 1, D239).
        decide(takeUp(root, placed, run), (up) => {
            if ("refused" in up)
                return withSaid(cut.said, end(built({ ending: "refused", why: "branch", fault: up.refused })));
            const ws = { ...found, main: up.main, on: up.on };
            return decide(told(ws, placed.active[0]?.name, cut.cut, run, heldNow), (t0) => withSaid([...cut.said, ...t0.said], t0.ending !== undefined ? end(built(t0.ending)) : decide(boardAt(root, ws.main), (board) => decide(holdsNow(board), (holds) => {
                const heldBy = board.active.filter((t) => holds.some((f) => f.file === holdOf(notes, t.name))).map((t) => t.name);
                const input = { board, held: heldBy, graph: ws.graph, limit: LIMIT, ...(named === undefined ? {} : { named }) };
                const first = take_up({ ...input, mainDone: true });
                // Only where the first two rules give nothing does the third rule of take_up turn on what done says on main.
                const taken = first.take === "none" && board.active.length === 0 && named === undefined
                    ? decide(gather(ws, { folder: root, line: ws.main }), (g) => end(take_up({ ...input, mainDone: done(ws.graph, g).done === "yes" })))
                    : end(first);
                return decide(taken, (t) => {
                    if (t.take === "none")
                        return end(built({ ending: "refused", why: t.why, ...(t.why === "held" ? { holds } : {}) }));
                    if (t.take !== "simplest")
                        return build(ws, t.name, t.lane, run);
                    return decide(writeSimplest(root), (ticket) => sequence(decide(committed({ folder: root, line: ws.main }, `board: the simplest ticket ${ticket}`, [ticketPath("backlog", ticket)]), (commit) => commit === undefined ? end(undefined) : note(root, { event: "commit made", run, ticket, commit, why: "the simplest ticket written" })), build(ws, ticket, "backlog", run)));
                });
            }))));
        }))));
    });
});
const told = (ws, ticket, cut, run, heldNow) => decide(decide(boardOf(ws.root), heldNow), (heldAtStart) => {
    if (heldAtStart.length > 0)
        return end({ said: [] });
    // Below the top of a larger repository, the merge in progress this commit completes is the take-in's alone, of main into the active ticket's branch; a merge of the user's own is left as it is (D201, D240).
    const byHand = (said) => decide(commitOf({ folder: ws.root, line: ws.on ?? ws.main }, BY_HAND, undefined, ticket === undefined ? undefined : ws.main), (c) => "unresolved" in c
        // A merge git could not make, left in the folder while a ticket is active, keeps the run on it stopped until the user resolves it (REQ-FLOW-008); each file is named as the take-in named it, from the repository's top and said so where it lies outside the folder (D240).
        ? end({ ending: ticket === undefined ? { ending: "refused", why: "unresolved", files: fromTop(ws, c.unresolved), fault: resolveWhere(ws, c.unresolved) } : { ending: "stopped", ticket, why: `git could not merge ${fromTop(ws, c.unresolved).join(", ")}, and the merge is not resolved. ${resolveWhere(ws, c.unresolved)}`, files: fromTop(ws, c.unresolved) }, said })
        : c.commit === undefined ? end({ said }) : sequence(note(ws.root, { event: "commit made", run, commit: c.commit, why: "what the user left uncommitted" }), end({ said })));
    if (ticket === undefined)
        return byHand([]);
    const wasCut = cut.includes(ticket);
    return decide(hereOf(ws, ticket), (here) => {
        // Where the identities kept cannot serve, the commit's stand in, kept as that session's: by the record's step where the graph holds it, else by the ticket's checklist (D246); the commit the session started from, where the record names one git holds (D255).
        const keptNow = decide(standing(ws, here, ticket, wasCut), (s) => "none" in s ? end(undefined)
            : "kept" in s ? end({ kept: s.kept, changed: s.changed })
                : using(Files, (files) => decide(files.read(at(ws.root, ticketPath("active", ticket))), (written) => stoodIn(ws, here, ticket, s.standIn.vector ?? lastBegun(ws, written), s.standIn.kind ?? "work", s.standIn.from))));
        return decide(keptNow, (first) => {
            if (first === undefined)
                return byHand([]);
            // A place the step writes that is neither in the folder nor in the commit it is on is no path to commit.
            const there = (paths) => using(Files, (files) => using(Git, (git) => decide(each(paths, (p) => files.exists(at(ws.root, p))), (found) => decide(git.presentAt(ws.root, paths.map((p) => ["HEAD", p])), (held) => end(paths.filter((_, i) => found[i] === true || held.has(i)))))));
            const result = (k, said) => sequence(decide(there(resultPaths(ws, k, here.ticket)), (paths) => paths.length === 0 ? end(undefined) : decide(committed({ folder: ws.root, line: here.line }, `the result of the step on ${k.vector}`, paths), (commit) => commit === undefined ? end(undefined) : note(ws.root, { event: "commit made", run, ticket, commit, why: `the result of the step on ${k.vector}` }))), settle(ws, ticket, k), byHand(said));
            const k = first.kept;
            if (first.changed.length === 0)
                return result(k, []);
            return sequence(
            // Asked at the start of the run, before any step, the entry names no vector (CALCULUS section 8, D227).
            note(ws.root, { event: "user asked", run, ticket, why: `what changed while the session on ${k.vector} worked`, named: first.changed.length }), end({ ending: { ending: "waiting", ticket, vector: k.vector, question: changedQuestion(k.vector, first.changed, k.stood, ws.main), ruling: first.changed.length }, said: [] }));
        });
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
const closing = (root, run, ran) => decide(outcome(ended(root, run, ran.ending)), (o) => decide(logsStarted(root), (anew) => end({ ...("fault" in o ? { ...ran, logUnwritten: true } : ran), ...(anew > 0 ? { logRestarted: true } : {}) })));
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
    const { root, on, within } = opened;
    const runId = now().written;
    const started = decide(logFound(root), (found) => using(Files, (files) => decide(files.read(at(root, PLACES.settings)), (settings) => sequence(note(root, { event: "run started", run: runId, release: releaseWords(recordedIn(settings ?? "")), ...(named === undefined ? {} : { ticket: named }), ...(found ? {} : { why: "the event log was not found; this run starts a new one" }) }), end(!found)))));
    return decide(outcome(started), (s) => {
        // A fault before `run started` is written ends the run as refused, and the log holds nothing of it.
        if ("fault" in s)
            return end(refusedFor(root, s.fault, false));
        const logStarted = s.value;
        return decide(outcome(runOn(root, on, within, named, runId, manifest)), (r) => "fault" in r
            // A fault met outside every repeat ends the run as refused; where it is in writing the log, the log holds nothing of it.
            ? r.fault._tag === "LogRefused" ? end(refusedFor(root, r.fault, logStarted)) : closing(root, runId, refusedFor(root, r.fault, logStarted))
            : closing(root, runId, { ending: r.value.ending, logStarted, printed: r.value.printed, ...(r.value.noted === undefined ? {} : { noted: r.value.noted }) }));
    });
});
