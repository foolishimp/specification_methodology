/**
 * The library's public surface (REQ-INTERFACE-001): plain functions that
 * return promises, with nothing of Effect in their types. Each one names the
 * workspace, runs one flow on the services carried by the Node platform, and
 * gives back the flow's result together with the same result in plain words,
 * saying what the user can do next. Every program passes a command to one of
 * these and gives back what it returns.
 *
 * The workspace is named by a path or a `file:` URI on a mounted file system
 * (REQ-INTERFACE-002). Sessions are started by the command the settings give;
 * with `standIn`, by the stand-in agent of the scenarios, a second layer for
 * sessions (REQ-VERIFY-002).
 *
 * The library turns the workspace the user names into a folder, gives the
 * command's term its services, runs it and puts its ending in words. It reads
 * and decides nothing itself: every refusal is the term's (design,
 * CALCULUS.md section 5).
 *
 * @uses C1 C3 C4 C10 C11 C12 C13 C14 C15
 * The library says where the manifest of the release that is running would
 * be: beside its code, where the install puts it. A command that reads what
 * is running reads it there (REQ-FLOW-010, D197).
 *
 * @is REQ-INTERFACE-001 REQ-INTERFACE-002 REQ-FLOW-001 REQ-FLOW-002 REQ-FLOW-003 REQ-FLOW-004 REQ-FLOW-006 REQ-FLOW-010 REQ-ALG-012
 */
import * as NodeServices from "@effect/platform-node/NodeServices";
import * as Effect from "effect/Effect";
import * as Layer from "effect/Layer";
import * as Path from "effect/Path";
import { checksLive } from "../services/checks.js";
import { filesLive } from "../services/files.js";
import { gitLive } from "../services/git.js";
import { holdLive } from "../services/hold.js";
import { eventLogLive } from "../services/log.js";
import { commandSessions } from "../services/sessions.js";
import { standInSessions } from "../services/stand_in.js";
import { answer as answerFlow } from "../flows/question.js";
import { recordRelease as recordFlow } from "../flows/record.js";
import { run as runFlow } from "../flows/run.js";
import { setUp } from "../flows/setup.js";
import { registryOf, show as showFlow } from "../flows/show.js";
import { ticket as ticketFlow } from "../flows/ticket.js";
import { PLACES, seenFrom, UNRELEASED } from "../flows/workspace.js";
/** The method release set-up names where the user names none: the release this build was tested on. */
export const RELEASE = {
    uri: "stdo://releases/v3.1.0-rc.2/",
    manifest: "b691b0249c82ff39033ae636c4eaa0ab44bafee3732c79a227eb9409d53776c4"
};
const layerOf = (options) => {
    const base = NodeServices.layer;
    const files = filesLive.pipe(Layer.provide(base));
    const sessions = options.standIn === undefined ? commandSessions : standInSessions(options.standIn);
    const own = Layer.mergeAll(gitLive, eventLogLive, holdLive, sessions).pipe(Layer.provide(base));
    const onFiles = checksLive.pipe(Layer.provide(Layer.merge(files, base)));
    return Layer.mergeAll(files, own, onFiles);
};
const faultWords = (e) => e._tag === "FileRefused" ? `The file ${e.path} could not be read or written: ${e.why}` : e._tag === "GitRefused" ? `git refused in ${e.folder}: ${e.why}` : `The event log could not be added to: ${e.why}`;
const perform = (program, options = {}) => Effect.runPromise(program.pipe(Effect.catch((e) => Effect.succeed({ exitCode: 4, words: faultWords(e) })), Effect.provide(Layer.merge(layerOf(options), NodeServices.layer))));
/** The folder a workspace URI names. */
const folderOf = (workspace) => Effect.gen(function* () {
    const path = yield* Path.Path;
    if (!workspace.startsWith("file:"))
        return path.resolve(workspace);
    return yield* path.fromFileUrl(new URL(workspace)).pipe(Effect.orElseSucceed(() => path.resolve(workspace)));
});
/** Why `open` refused a command, in words. */
const openWords = (workspace, o) => o.refused === "absent"
    ? `There is no workspace at ${o.folder}.`
    : o.refused === "not set up"
        ? `${o.folder} is not set up. Set it up first: stdo-builder setup ${workspace} --name "<a name for the product>"`
        : `The workspace's own folder, ${o.folder}, is on no line of work: its HEAD names a commit alone. Check out main there, then try again.`;
/**
 * Where the library keeps the method's graph and its registry: set-up reads
 * them, and a refusal of the governing graph names them. And where the
 * manifest of the release that is running would be: at the top of the
 * installed release, two folders above them (D197).
 */
const methodPlaces = Effect.flatMap(Effect.service(Path.Path), (path) => Effect.map(path.fromFileUrl(new URL("../method/", import.meta.url)).pipe(Effect.orElseSucceed(() => "")), (dir) => ({
    graph: path.join(dir, "graph.json"),
    registry: path.join(dir, "registry.json"),
    manifest: path.join(dir, "..", "..", "manifest.json")
})));
/** A release of STDO Builder, or a build that is no release, in words (REQ-FLOW-010). */
const builderWords = (b) => b === UNRELEASED ? "an unreleased build of STDO Builder" : `release ${b.version} of STDO Builder, whose manifest's sha256 is ${b.manifest_sha256}`;
/** What the settings record, in words: no release, the release it names, or the record as written where it names none. */
const recordedWords = (r) => "none" in r ? "no release of STDO Builder" : "builder" in r ? builderWords(r.builder) : `${r.written}, which names no release of STDO Builder`;
/** The term of a command on the folder the user named, its result put in words. */
const command = (workspace, term, words) => Effect.flatMap(methodPlaces, (method) => Effect.flatMap(folderOf(workspace), (folder) => Effect.map(term(folder, method), (got) => words(got, method))));
const reasonsWords = (reasons) => reasons.map((r) => `- ${r.where}: ${r.says}`).join("\n");
/**
 * Why the governing graph is refused, and, where the graph or its registry is,
 * where this release keeps the method's own: a graph the workspace kept from
 * an earlier release is refused like any other (D176).
 */
const notWellFormed = (reasons, method) => [
    `The governing graph is not well formed:\n${reasonsWords(reasons)}`,
    ...(reasons.every((r) => r.where.startsWith(PLACES.settings)) ? [] : [`The method's own graph and registry of this release are at ${method.graph} and ${method.registry}; to work by them, put them in place at ${PLACES.graph} and ${PLACES.registry}.`])
].join("\n");
export const setup = (workspace, options) => {
    const release = options.release ?? RELEASE;
    return perform(command(workspace, (folder, method) => setUp(folder, options.name, release, method), (done) => {
        if ("refused" in done) {
            return {
                exitCode: 2,
                words: `Set-up is refused: ${done.refused.folder} lies inside the git repository at ${done.refused.top}, and that repository ignores it. Set the product up in a folder the repository does not ignore, in a folder that is in no git repository, or in the top folder of one.`
            };
        }
        const lines = [
            `Set up ${options.name} in ${done.root}.`,
            ...(done.inside === undefined ? [] : [`The product lies inside a larger git repository, at ${done.inside}. The framework's commits, checkouts and merges concern only the files under ${done.root}; the repository's other files, what is not committed outside the folder and its other branches are left as they are.`]),
            done.wrote.length === 0 ? "It wrote nothing: the workspace was already set up." : `It wrote: ${done.wrote.join(", ")}.`,
            ...(done.there.length === 0 ? [] : [`These were there already and were left as they are: ${done.there.join(", ")}.`]),
            "installed" in done.method
                ? `The method release ${release.uri} is installed and verified.`
                : `The method release ${release.uri} could not be installed or verified: ${done.method.refused}`,
            ...(done.wrote.includes(PLACES.settings) ? [`The settings record ${builderWords(done.builder)} as the one that builds this product.`] : []),
            ...(done.ticket === undefined ? [] : [`A first ticket is written: ${done.ticket}, to write the intent and the product definition of what is here.`]),
            ...(done.unfound ?? []).map((key) => `Set-up found no ${key} of the system here, so the definition file gives it the folder ${key}, which is not there yet. Where it lies elsewhere, give its paths in the definition file instead.`),
            `Next: write a ticket, stdo-builder ticket ${workspace} "<what the product is to do>", then start a run, stdo-builder run ${workspace}.`
        ];
        return { exitCode: "installed" in done.method ? 0 : 1, words: lines.join("\n"), result: done };
    }));
};
// ---- A ticket
export const ticket = (workspace, words) => perform(command(workspace, (folder) => ticketFlow(folder, words), (got) => {
    if ("folder" in got)
        return { exitCode: 2, words: openWords(workspace, got) };
    if ("refused" in got)
        return { exitCode: 2, words: "A ticket says, in your words, what you want. Give the words." };
    if ("there" in got)
        return { exitCode: 2, words: `The ticket ${got.there} is there already, with these words.`, result: got };
    return {
        exitCode: 0,
        words: `The ticket ${got.written} is written in the backlog, at ${PLACES.lanes.backlog}/${got.written}.md.\nNext: start a run, stdo-builder run ${workspace}.`,
        result: got
    };
}));
// ---- A run
/** Each ending of a run names where what each session that failed in it printed is kept, one line each (D81). */
const endingWords = (workspace, e, printed, method) => {
    const kept = printed.map((p) => `A session failed in this run. What it printed is kept at ${p}.`);
    switch (e.ending) {
        case "done":
            return { exitCode: 0, words: [`The work on the ticket ${e.ticket} is done. It lies in the done lane and its branch is merged into main, at ${e.merged}.`, ...kept].join("\n") };
        case "waiting":
            return {
                exitCode: 0,
                words: [
                    `The run waits for your answer on ${e.vector}, for the ticket ${e.ticket}. The question is given here, and stdo-builder show gives it again:`,
                    "",
                    e.question,
                    "",
                    ...kept,
                    `Answer: stdo-builder answer ${workspace} yes, or stdo-builder answer ${workspace} no --reason "<why>"; with either you may add --ruling "<a ruling that binds every later session of the ticket>". Then start a run again.`
                ].join("\n")
            };
        case "stopped":
            return {
                exitCode: 1,
                words: [
                    `The run stopped on the ticket ${e.ticket}${e.vector === undefined ? "" : `, at ${e.vector}`}: ${e.why}.`,
                    ...(e.checks === undefined || e.checks.length === 0 ? [] : [`What did not pass: ${e.checks.join(", ")}.`]),
                    ...(e.files === undefined || e.files.length === 0 ? [] : [`The files: ${e.files.join(", ")}.`]),
                    ...(e.found === undefined ? [] : [`What the checks found is at ${e.found}.`]),
                    // What the last working session said it needs, where it stopped without its asset, reaches the user here (D97).
                    ...(e.printed === undefined ? [] : [`What the last working session printed is kept at ${e.printed}.`]),
                    ...kept,
                    `Next: see where the work stands, stdo-builder show ${workspace}; change what needs changing; then start a run again.`
                ].join("\n")
            };
        case "refused": {
            const why = {
                release: `the settings record ${recordedWords(e.release?.recorded ?? { none: true })} as the one that builds this product, and this is ${e.release === undefined ? "another" : builderWords(e.release.running)}. To have this one build it, record it: stdo-builder record-release ${workspace}. Then start a run again.`,
                "not well formed": `${notWellFormed(e.reasons ?? [], method).replace(/^The/, "the")}\nPut a graph that is well formed in place, then start a run again.`,
                "not set up": `the workspace is not set up. Set it up first: stdo-builder setup ${workspace} --name "<a name>".`,
                held: "a run already works on every active ticket. Wait for it to end, then start a run again.",
                limit: "the limit on active tickets is reached. Finish an active ticket first.",
                nothing: `there is nothing to build. Write a ticket to change something: stdo-builder ticket ${workspace} "<what you want>".`,
                unresolved: `git could not merge ${(e.files ?? []).join(", ")} on main, and the merge is not resolved. Resolve it in the workspace's own folder and commit there, then start a run again.`,
                fault: `${e.fault ?? "the workspace could not be read or written"}.`
            }[e.why];
            return { exitCode: 2, words: [`The run is refused before any step: ${why}`, ...kept].join("\n") };
        }
    }
};
export const run = (workspace, options = {}) => perform(command(workspace, (folder, method) => runFlow(folder, options.ticket, method.manifest), (ran, method) => {
    if ("folder" in ran)
        return { exitCode: 2, words: openWords(workspace, ran) };
    const said = endingWords(workspace, ran.ending, ran.printed, method);
    const words = [
        ...(ran.logStarted ? [`The event log was not found; this run starts a new one, at ${PLACES.log}.`] : []),
        // The run kept the ending it reached; the log holds nothing of it (D75).
        ...(ran.logUnwritten === true ? [`The event log could not be written at ${PLACES.log}, so it holds nothing of how this run ended. Put that right before you start the next run.`] : []),
        said.words
    ].join("\n");
    return { exitCode: said.exitCode, words, result: ran };
}), options);
export const recordRelease = (workspace) => perform(command(workspace, (folder, method) => recordFlow(folder, method.manifest), (got) => {
    if ("folder" in got)
        return { exitCode: 2, words: openWords(workspace, got) };
    if ("refused" in got)
        return { exitCode: 2, words: `The settings, at ${PLACES.settings}, do not read as an object, so the record cannot be written there. Put them right, then record the release again.` };
    if (!got.changed)
        return { exitCode: 0, words: `The settings already record ${builderWords(got.recorded)} as the one that builds this product. Nothing is changed.`, result: got };
    return {
        exitCode: 0,
        words: [
            `The settings now record ${builderWords(got.recorded)} as the one that builds this product, in place of ${recordedWords(got.was)}.`,
            `Nothing is committed: the next run commits it as your change on main. Next: start a run, stdo-builder run ${workspace}.`
        ].join("\n"),
        result: got
    };
}));
export const answer = (workspace, says, options = {}) => perform(command(workspace, (folder) => answerFlow(folder, says, options.reason, options.ticket, options.ruling), (got, method) => {
    if ("folder" in got)
        return { exitCode: 2, words: openWords(workspace, got) };
    if ("refused" in got) {
        return typeof got.refused === "string"
            ? { exitCode: 2, words: got.refused, result: { refused: got.refused } }
            : { exitCode: 2, words: notWellFormed(got.refused, method) };
    }
    return {
        exitCode: 0,
        words: `Your answer, ${got.says}, to ${got.vector} is written at ${got.paths.join(", ")} and committed on the ticket's branch.\nNext: start a run again, stdo-builder run ${workspace}.`,
        result: got
    };
}));
// ---- Where the work stands
const ticketWords = (within) => (t) => {
    const waits = t.waits === undefined
        ? ""
        : t.waits.on === "answer"
            ? `, waits for your answer on ${t.waits.vector}`
            : t.waits.on === "held up"
                ? `, held up at ${t.waits.vector}: ${t.waits.checks.join(", ")} did not pass${t.waits.found === undefined ? "" : `; what was found is at ${seenFrom(t.lane === "active" ? t.name : undefined, t.waits.found, within)}`}`
                : t.waits.on === "work"
                    ? `, to be built at ${t.waits.vector}`
                    : t.waits.on === "induction"
                        ? ", to be inducted"
                        : t.waits.on === "merge"
                            ? ", ready to merge"
                            : ", and the event log was not found: a run finds what it waits on";
    // Each says what it was read from, the ticket or the event log, with when that was written; a run reads the workspace again (D204).
    const asOf = t.waits === undefined || t.waits.on === "unknown"
        ? ""
        : `, as ${t.waits.from === "ticket" ? "the ticket shows" : "the event log shows"}${"when" in t.waits && t.waits.when !== undefined ? ` (written at ${t.waits.when})` : ""}; a run reads the workspace again`;
    const question = t.waits?.on === "answer" && t.waits.question !== undefined ? `\n  asked:\n${t.waits.question.split("\n").map((l) => `    ${l}`).join("\n")}` : "";
    const changed = t.changed.length === 0 ? "" : `\n  changed: ${t.changed.map((c) => `${c.asset} (${c.lines} lines)`).join(", ")}`;
    const last = t.runs?.last === undefined ? "" : `\n  last run: ${t.runs.last.ending}, ${t.runs.last.why}`;
    // What the agents reported each session cost, with its unit as the settings name it, and the sums for the ticket (D91, D102); a cost that is a number, to the cent as `stands` gives it (D195). The calls, of a session and their sum, are said to be the agent's own report, which leaves out what further agents did (REQ-ALG-012, D199).
    const spent = (cost, unit, calls) => [...(cost === undefined ? [] : [`cost ${cost}${unit === undefined ? "" : ` ${unit}`}`]), ...(calls === undefined ? [] : [`${calls} call${calls === 1 ? "" : "s"} by the agent's own report`])].join(", ");
    const sessions = t.runs === undefined || t.runs.sessions.length === 0
        ? ""
        : `\n  sessions: ${t.runs.sessions.map((s) => {
            const reported = spent(s.cost, s.unit, s.calls);
            return `${s.vector} ${s.kind} ${s.ended}${s.seconds === undefined ? "" : ` ${s.seconds}s`}${reported === "" ? "" : `, ${reported}`}`;
        }).join("; ")}`;
    const sums = t.runs === undefined ? "" : spent(t.runs.cost, t.runs.unit, t.runs.calls);
    return `- ${t.name}: ${t.lane}${waits}${asOf}${question}${changed}${last}${sessions}${sums === "" ? "" : `\n  in all: ${sums}`}`;
};
export const show = (workspace) => perform(command(workspace, showFlow, (got, method) => {
    if ("folder" in got)
        return { exitCode: 2, words: openWords(workspace, got) };
    if ("refused" in got)
        return { exitCode: 2, words: notWellFormed(got.refused, method) };
    const lines = [
        got.tickets.length === 0 ? "No ticket is on the board." : "The tickets:",
        ...got.tickets.map(ticketWords(got.within ?? "")),
        ...(got.withdrawn.length === 0 ? [] : [`Withdrawn: ${got.withdrawn.join(", ")}.`]),
        got.log === "found" ? `The event log is at ${PLACES.log}.` : "The event log was not found."
    ];
    return { exitCode: 0, words: lines.join("\n"), result: got };
}));
// ---- The registry
export const registry = (workspace) => perform(command(workspace, registryOf, (got, method) => {
    if ("folder" in got)
        return { exitCode: 2, words: openWords(workspace, got) };
    if ("refused" in got)
        return { exitCode: 2, words: notWellFormed(got.refused, method) };
    const lines = got.map((e) => `- ${e.name}: ${e.purpose}\n  writes ${e.writes.length === 0 ? "no node" : e.writes.join(", ")}; rests on ${e.rests.length === 0 ? "nothing" : e.rests.join(", ")}`);
    return { exitCode: 0, words: [`The registry holds ${got.length} graph function${got.length === 1 ? "" : "s"}:`, ...lines].join("\n"), result: got };
}));
