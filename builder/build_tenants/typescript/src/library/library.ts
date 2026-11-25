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
 * @is REQ-INTERFACE-001 REQ-INTERFACE-002 REQ-FLOW-001 REQ-FLOW-002 REQ-FLOW-003 REQ-FLOW-004 REQ-FLOW-006 REQ-FLOW-008 REQ-FLOW-010 REQ-ALG-012 REQ-PARAM-001
 */
import * as NodeServices from "@effect/platform-node/NodeServices"
import * as Effect from "effect/Effect"
import * as Layer from "effect/Layer"
import * as Path from "effect/Path"
import type { Listed } from "../graph/registry.js"
import type { Standing, TicketStands } from "../algorithms/stands.js"
import type { Reason } from "../algorithms/well_formed.js"
import { checksLive } from "../services/checks.js"
import { filesLive } from "../services/files.js"
import { gitLive } from "../services/git.js"
import { holdLive } from "../services/hold.js"
import { eventLogLive } from "../services/log.js"
import { commandSessions } from "../services/sessions.js"
import type { Services } from "../services/services.js"
import { standInSessions } from "../services/stand_in.js"
import { atMost } from "../flows/changed.js"
import { answer as answerFlow, type AnswerGiven, type Answered } from "../flows/question.js"
import { recordRelease as recordFlow, type RecordGiven } from "../flows/record.js"
import { run as runFlow, type Ending, type Ran, type RunGiven } from "../flows/run.js"
import { setUp, type Method, type Refused, type Release, type SetUp } from "../flows/setup.js"
import { registryOf, show as showFlow } from "../flows/show.js"
import { ticket as ticketFlow, type TicketWritten, type Written } from "../flows/ticket.js"
import { GIT_NEEDED, PLACES, UNRELEASED, type Builder, type BuilderRecord, type Fault, type Opened } from "../flows/workspace.js"

/** What every command gives back: its result, the same in plain words, and the exit code a program gives. */
export interface Said<A> {
  readonly exitCode: number
  readonly words: string
  readonly result?: A
}

/** The exit code of a command the program does not know, or one not given what it needs, once the usage is printed: 2, the code of a command refused (REQ-INTERFACE-001, D251). */
export const NOT_GIVEN = 2

/** The method release set-up names where the user names none: the release this build was tested on. */
export const RELEASE: Release = {
  uri: "stdo://releases/v3.1.0-rc.3/",
  manifest: "2b3a7391dfb731219e64240199fe2e1b2736b9d5a44d030602fe7f07dd6c7a9a"
}

export interface Options {
  /** A folder of the stand-in agent's fixtures; sessions are then started by the stand-in. */
  readonly standIn?: string
}

const layerOf = (options: Options): Layer.Layer<Services> => {
  const base = NodeServices.layer
  const files = filesLive.pipe(Layer.provide(base))
  const sessions = options.standIn === undefined ? commandSessions : standInSessions(options.standIn)
  const own = Layer.mergeAll(gitLive, eventLogLive, holdLive, sessions).pipe(Layer.provide(base))
  const onFiles = checksLive.pipe(Layer.provide(Layer.merge(files, base)))
  return Layer.mergeAll(files, own, onFiles)
}

const faultWords = (e: Fault): string =>
  e._tag === "FileRefused" ? `The file ${e.path} could not be read or written: ${e.why}` : e._tag === "GitRefused" ? `git refused in ${e.folder}: ${e.why}` : `The event log could not be added to: ${e.why}`

type Program<A> = Effect.Effect<Said<A>, Fault, Services | Path.Path>

const perform = <A>(program: Program<A>, options: Options = {}): Promise<Said<A>> =>
  Effect.runPromise(
    program.pipe(
      Effect.catch((e: Fault) => Effect.succeed<Said<A>>({ exitCode: 4, words: faultWords(e) })),
      Effect.provide(Layer.merge(layerOf(options), NodeServices.layer))
    )
  )

/** The folder a workspace URI names. */
const folderOf = (workspace: string) =>
  Effect.gen(function*() {
    const path = yield* Path.Path
    if (!workspace.startsWith("file:")) return path.resolve(workspace)
    return yield* path.fromFileUrl(new URL(workspace)).pipe(Effect.orElseSucceed(() => path.resolve(workspace)))
  })

/** Why a command given from inside a session is refused (REQ-INTERFACE-001, D217). */
const insideWords = (root: string): string =>
  `This command is refused, and nothing is changed: it was given from inside a session that STDO Builder started on the workspace at ${root}, and names that workspace or a folder inside it. The framework runs that workspace's commands itself; a session works on the files its packet names.`

/** Why a command is refused where git's version reads as older than the product needs, in one sentence naming the version found and the version needed (REQ-INTERFACE-001, D248). */
const gitWords = (found: string): string =>
  `This command is refused, and nothing is changed: STDO Builder needs git ${GIT_NEEDED} or later, and the git on your PATH gives its version as ${found}.`

/** Why `open` refused a command, in words. */
const openWords = (workspace: string, o: Exclude<Opened, { readonly root: string }>): string =>
  o.refused === "older git"
    ? gitWords(o.found)
    : o.refused === "inside a session"
    ? insideWords(o.folder)
    : o.refused === "absent"
    ? `There is no workspace at ${o.folder}.`
    : `${o.folder} is not set up. Set it up first: stdo-builder setup ${workspace} --name "<a name for the product>"`

/**
 * Where the library keeps the method's graph and its registry: set-up reads
 * them, and a refusal of the governing graph names them. And where the
 * manifest of the release that is running would be: at the top of the
 * installed release, two folders above them (D197).
 */
const methodPlaces = Effect.flatMap(Effect.service(Path.Path), (path) =>
  Effect.map(path.fromFileUrl(new URL("../method/", import.meta.url)).pipe(Effect.orElseSucceed(() => "")), (dir): Method => ({
    graph: path.join(dir, "graph.json"),
    registry: path.join(dir, "registry.json"),
    manifest: path.join(dir, "..", "..", "manifest.json")
  })))

/** A release of STDO Builder, or a build that is no release, in words (REQ-FLOW-010). */
const builderWords = (b: Builder): string =>
  b === UNRELEASED ? "an unreleased build of STDO Builder" : `release ${b.version} of STDO Builder, whose manifest's sha256 is ${b.manifest_sha256}`

/** What the settings record, in words: no release, the release it names, or the record as written where it names none. */
const recordedWords = (r: BuilderRecord): string =>
  "none" in r ? "no release of STDO Builder" : "builder" in r ? builderWords(r.builder) : `${r.written}, which names no release of STDO Builder`

/** The term of a command on the folder the user named, its result put in words. */
const command = <A, B>(workspace: string, term: (folder: string, method: Method) => Effect.Effect<A, Fault, Services>, words: (got: A, method: Method) => Said<B>): Program<B> =>
  Effect.flatMap(methodPlaces, (method) => Effect.flatMap(folderOf(workspace), (folder) => Effect.map(term(folder, method), (got) => words(got, method))))

const reasonsWords = (reasons: readonly Reason[]): string => reasons.map((r) => `- ${r.where}: ${r.says}`).join("\n")

/**
 * Why the governing graph is refused, and, where the graph or its registry is,
 * where this release keeps the method's own: a graph the workspace kept from
 * an earlier release is refused like any other (D176).
 */
const notWellFormed = (reasons: readonly Reason[], method: Method): string => [
  `The governing graph is not well formed:\n${reasonsWords(reasons)}`,
  ...(reasons.every((r) => r.where.startsWith(PLACES.settings)) ? [] : [`The method's own graph and registry of this release are at ${method.graph} and ${method.registry}; to work by them, put them in place at ${PLACES.graph} and ${PLACES.registry}.`])
].join("\n")

// ---- Set up

export interface SetupOptions {
  readonly name: string
  readonly release?: Release
}

export const setup = (workspace: string, options: SetupOptions): Promise<Said<SetUp>> => {
  const release = options.release ?? RELEASE
  return perform(
    command(workspace, (folder, method) => setUp(folder, options.name, release, method), (done: SetUp | Refused): Said<SetUp> => {
      if ("refused" in done) {
        const r = done.refused
        if ("olderGit" in r) return { exitCode: 2, words: gitWords(r.olderGit) }
        if ("inside" in r) return { exitCode: 2, words: insideWords(r.inside) }
        return {
          exitCode: 2,
          words: `Set-up is refused: ${r.folder} lies inside the git repository at ${r.top}, and that repository ignores it. Set the product up in a folder the repository does not ignore, in a folder that is in no git repository, or in the top folder of one.`
        }
      }
      const lines = [
        `Set up ${options.name} in ${done.root}.`,
        ...(done.inside === undefined ? [] : [`The product lies inside a larger git repository, at ${done.inside}. The framework commits only the files under ${done.root}, on the branch the folder is on; what is not committed outside the folder and the repository's other branches are left as they are. A merge of a ticket's branch carries the whole of the branch's tree, so a commit of yours outside the folder, made on the ticket's branch, reaches the branch the ticket left with it.`]),
        done.wrote.length === 0 ? "It wrote nothing: the workspace was already set up." : `It wrote: ${done.wrote.join(", ")}.`,
        ...(done.there.length === 0 ? [] : [`These were there already and were left as they are: ${done.there.join(", ")}.`]),
        "installed" in done.method
          ? `The method release ${release.uri} is installed and verified.`
          : `The method release ${release.uri} could not be installed or verified: ${done.method.refused}`,
        ...(done.wrote.includes(PLACES.settings) ? [`The settings record ${builderWords(done.builder)} as the one that builds this product.`] : []),
        ...(done.ticket === undefined ? [] : [`A first ticket is written: ${done.ticket}, to write the intent and the product definition of what is here.`]),
        ...(done.unfound ?? []).map((key) => `Set-up found no ${key} of the system here, so the definition file gives it the folder ${key}, which is not there yet. Where it lies elsewhere, give its paths in the definition file instead.`),
        `Next: write a ticket, stdo-builder ticket ${workspace} "<what the product is to do>", then start a run, stdo-builder run ${workspace}.`
      ]
      return { exitCode: "installed" in done.method ? 0 : 1, words: lines.join("\n"), result: done }
    }))
}

// ---- A ticket

export const ticket = (workspace: string, words: string): Promise<Said<Written>> =>
  perform<Written>(command(workspace, (folder) => ticketFlow(folder, words), (got: TicketWritten): Said<Written> => {
    if ("folder" in got) return { exitCode: 2, words: openWords(workspace, got) }
    if ("refused" in got) return { exitCode: 2, words: "A ticket says, in your words, what you want. Give the words." }
    if ("elsewhere" in got) return { exitCode: 2, words: `${got.elsewhere}. Nothing is written.` }
    if ("there" in got) return { exitCode: 2, words: `The ticket ${got.there} is there already, with these words.`, result: got }
    return {
      exitCode: 0,
      words: `The ticket ${got.written} is written in the backlog, at ${PLACES.lanes.backlog}/${got.written}.md.\nNext: start a run, stdo-builder run ${workspace}.`,
      result: got
    }
  }))

// ---- A run

/** Each ending of a run names where what each session that failed in it printed is kept, one line each (D81). */
const endingWords = (workspace: string, e: Ending, printed: readonly string[], method: Method): { readonly exitCode: number; readonly words: string } => {
  const kept = printed.map((p) => `A session failed in this run. What it printed is kept at ${p}.`)
  switch (e.ending) {
    case "done":
      return {
        exitCode: 0,
        words: [
          `The work on the ticket ${e.ticket} is done. It lies in the done lane and its branch is merged into ${e.into}, the branch it left, at ${e.merged}.`,
          // Inside a larger repository, each file outside the workspace's folder the merge took in, at most as many as a run names, with how many there are (REQ-FLOW-008 step 2, REQ-PARAM-001, D256).
          ...(e.outside === undefined || e.outside.length === 0 ? [] : [`The merge took these files outside the workspace's folder into ${e.into}, the branch the ticket left: ${atMost(e.outside)}.`]),
          ...kept
        ].join("\n")
      }
    case "waiting":
      if (e.ruling !== undefined) {
        return {
          exitCode: 0,
          words: [
            `The run waits for your ruling on what changed while the session on ${e.vector} worked, for the ticket ${e.ticket}. Nothing of the step is judged or committed until you rule. The question is given here, and stdo-builder show gives it again:`,
            "",
            e.question,
            "",
            ...kept,
            `Rule: stdo-builder answer ${workspace} yes, or put back what is not to stand and give stdo-builder answer ${workspace} no --reason "<why>". Then start a run again.`
          ].join("\n")
        }
      }
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
      }
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
      }
    case "refused": {
      const why = {
        release: `the settings record ${recordedWords(e.release?.recorded ?? { none: true })} as the one that builds this product, and this is ${e.release === undefined ? "another" : builderWords(e.release.running)}. To have this one build it, record it: stdo-builder record-release ${workspace}. Then start a run again.`,
        "not well formed": `${notWellFormed(e.reasons ?? [], method).replace(/^The/, "the")}\nPut a graph that is well formed in place, then start a run again.`,
        "not set up": `the workspace is not set up. Set it up first: stdo-builder setup ${workspace} --name "<a name>".`,
        held: `a run already works on every active ticket${(e.holds ?? []).map((h) => `; the hold ${h.file} names the process ${h.by === undefined ? "that holds it" : `${h.by.pid}${h.by.start === undefined ? "" : `, started ${h.by.start}`}`}`).join("")}. Wait for it to end, then start a run again.`,
        "cannot tell": `${e.fault ?? ""}. Nothing is started, and nothing is ended where the framework cannot tell. See that the current folders of processes can be read, and end any process named here that is of a session on the ticket, then start a run again.`,
        // The one sentence that `ps` was not found or could not read the table of processes, and what to install; it names no process (REQ-FLOW-001, D249).
        ps: `no session is started, and nothing is ended or committed. ${e.fault ?? ""} Then start a run again.`,
        alive: `${e.fault ?? ""}. Nothing is started on the ticket while one of them is alive. End them, then start a run again.`,
        branch: `${e.fault ?? ""}. Then start a run again.`,
        main: `${e.fault ?? ""}.${(e.files ?? []).length === 0 ? "" : ` The files: ${(e.files ?? []).join(", ")}.`}`,
        limit: "the limit on active tickets is reached. Finish an active ticket first.",
        nothing: `there is nothing to build. Write a ticket to change something: stdo-builder ticket ${workspace} "<what you want>".`,
        unresolved: `git could not merge ${(e.files ?? []).join(", ")}, and the merge is not resolved. ${e.fault ?? "Resolve it in the workspace's folder, and commit there"}, then start a run again.`,
        fault: `${e.fault ?? "the workspace could not be read or written"}.`
      }[e.why]
      return { exitCode: 2, words: [`The run is refused before any step: ${why}`, ...kept].join("\n") }
    }
  }
}

export interface RunOptions extends Options {
  /** The ticket to work on, by name. */
  readonly ticket?: string
}

export const run = (workspace: string, options: RunOptions = {}): Promise<Said<Ran>> =>
  perform(command(workspace, (folder, method) => runFlow(folder, options.ticket, method.manifest), (ran: RunGiven, method): Said<Ran> => {
    if ("folder" in ran) return { exitCode: 2, words: openWords(workspace, ran) }
    const said = endingWords(workspace, ran.ending, ran.printed, method)
    const words = [
      ...(ran.logStarted ? [`The event log was not found; this run starts a new one, at ${PLACES.log}.`] : []),
      // The log the run was adding to was gone when it next added to it: said once (D247).
      ...(ran.logRestarted === true ? [`The event log this run was adding to was not found; this run started a new one, at ${PLACES.log}.`] : []),
      // The run kept the ending it reached; the log holds nothing of it (D75).
      ...(ran.logUnwritten === true ? [`The event log could not be written at ${PLACES.log}, so it holds nothing of how this run ended. Put that right before you start the next run.`] : []),
      said.words,
      // What changed among the branches, tags and stash, or outside the workspace's folder, while a session worked; none of it holds the ticket (D228).
      ...(ran.noted ?? [])
    ].join("\n")
    return { exitCode: said.exitCode, words, result: ran }
  }), options)

// ---- The release that builds the product

/** What the command to record the release gives: what is now recorded, what was, and whether the settings changed (REQ-FLOW-010). */
export type ReleaseRecorded = Extract<RecordGiven, { readonly recorded: Builder }>

export const recordRelease = (workspace: string): Promise<Said<ReleaseRecorded>> =>
  perform<ReleaseRecorded>(command(workspace, (folder, method) => recordFlow(folder, method.manifest), (got: RecordGiven): Said<ReleaseRecorded> => {
    if ("folder" in got) return { exitCode: 2, words: openWords(workspace, got) }
    if ("elsewhere" in got) return { exitCode: 2, words: `${got.elsewhere}. Nothing is changed.` }
    if ("refused" in got) return { exitCode: 2, words: `The settings, at ${PLACES.settings}, do not read as an object, so the record cannot be written there. Put them right, then record the release again.` }
    if (!got.changed) return { exitCode: 0, words: `The settings already record ${builderWords(got.recorded)} as the one that builds this product. Nothing is changed.`, result: got }
    return {
      exitCode: 0,
      words: [
        `The settings now record ${builderWords(got.recorded)} as the one that builds this product, in place of ${recordedWords(got.was)}.`,
        `Nothing is committed: the next run commits it as your change by hand, on the branch the folder is on. Next: start a run, stdo-builder run ${workspace}.`
      ].join("\n"),
      result: got
    }
  }))

// ---- An answer

export interface AnswerOptions {
  readonly reason?: string
  readonly ticket?: string
  /** A ruling the user gives with the answer, which binds every later session of the ticket (REQ-FLOW-006). */
  readonly ruling?: string
}

export const answer = (workspace: string, says: "yes" | "no", options: AnswerOptions = {}): Promise<Said<Answered>> =>
  perform<Answered>(command(workspace, (folder) => answerFlow(folder, says, options.reason, options.ticket, options.ruling), (got: AnswerGiven, method): Said<Answered> => {
    if ("folder" in got) return { exitCode: 2, words: openWords(workspace, got) }
    if ("refused" in got) {
      return typeof got.refused === "string"
        ? { exitCode: 2, words: got.refused, result: { refused: got.refused } }
        : { exitCode: 2, words: notWellFormed(got.refused, method) }
    }
    return {
      exitCode: 0,
      words: `Your answer, ${got.says}, to ${got.vector} is written at ${got.paths.join(", ")} and committed on the ticket's branch.\nNext: start a run again, stdo-builder run ${workspace}.`,
      result: got
    }
  }))

// ---- Where the work stands

const ticketWords = (t: TicketStands): string => {
  const waits = t.waits === undefined
    ? ""
    : t.waits.on === "ruling"
    ? `, waits for your ruling on what changed while the session on ${t.waits.vector} worked`
    : t.waits.on === "answer"
    ? `, waits for your answer on ${t.waits.vector}`
    : t.waits.on === "held up"
    ? `, held up at ${t.waits.vector}: ${t.waits.checks.join(", ")} did not pass${t.waits.found === undefined ? "" : `; what was found is at ${t.waits.found}`}`
    : t.waits.on === "work"
    ? `, to be built at ${t.waits.vector}`
    : t.waits.on === "induction"
    ? ", to be inducted"
    : t.waits.on === "merge"
    ? ", ready to merge"
    : ", and the event log was not found: a run finds what it waits on"
  // Each says what it was read from, the ticket or the event log, with when that was written; a run reads the workspace again (D204).
  const asOf = t.waits === undefined || t.waits.on === "unknown"
    ? ""
    : `, as ${t.waits.from === "ticket" ? "the ticket shows" : "the event log shows"}${"when" in t.waits && t.waits.when !== undefined ? ` (written at ${t.waits.when})` : ""}; a run reads the workspace again`
  const question = (t.waits?.on === "answer" || t.waits?.on === "ruling") && t.waits.question !== undefined ? `\n  asked:\n${t.waits.question.split("\n").map((l) => `    ${l}`).join("\n")}` : ""
  const changed = t.changed.length === 0 ? "" : `\n  changed: ${t.changed.map((c) => `${c.asset} (${c.lines} lines)`).join(", ")}`
  const last = t.runs?.last === undefined ? "" : `\n  last run: ${t.runs.last.ending}, ${t.runs.last.why}`
  // What the agents reported each session cost, with its unit as the settings name it, and the sums for the ticket (D91, D102); a cost that is a number, to the cent as `stands` gives it (D195). The calls, of a session and their sum, are said to be the agent's own report, which leaves out what further agents did (REQ-ALG-012, D199).
  const spent = (cost: string | undefined, unit: string | undefined, calls: number | undefined): string =>
    [...(cost === undefined ? [] : [`cost ${cost}${unit === undefined ? "" : ` ${unit}`}`]), ...(calls === undefined ? [] : [`${calls} call${calls === 1 ? "" : "s"} by the agent's own report`])].join(", ")
  const sessions = t.runs === undefined || t.runs.sessions.length === 0
    ? ""
    : `\n  sessions: ${t.runs.sessions.map((s) => {
      const reported = spent(s.cost, s.unit, s.calls)
      return `${s.vector} ${s.kind} ${s.ended}${s.seconds === undefined ? "" : ` ${s.seconds}s`}${reported === "" ? "" : `, ${reported}`}`
    }).join("; ")}`
  const sums = t.runs === undefined ? "" : spent(t.runs.cost, t.runs.unit, t.runs.calls)
  return `- ${t.name}: ${t.lane}${waits}${asOf}${question}${changed}${last}${sessions}${sums === "" ? "" : `\n  in all: ${sums}`}`
}

export const show = (workspace: string): Promise<Said<Standing>> =>
  perform(command(workspace, showFlow, (got, method): Said<Standing> => {
    if ("folder" in got) return { exitCode: 2, words: openWords(workspace, got) }
    if ("refused" in got) return { exitCode: 2, words: notWellFormed(got.refused, method) }
    const lines = [
      ...(got.elsewhere === undefined ? [] : [`${got.elsewhere}.`]),
      got.tickets.length === 0 ? "No ticket is on the board." : "The tickets:",
      ...got.tickets.map(ticketWords),
      ...(got.withdrawn.length === 0 ? [] : [`Withdrawn: ${got.withdrawn.join(", ")}.`]),
      got.log === "found" ? `The event log is at ${PLACES.log}.` : "The event log was not found."
    ]
    return { exitCode: 0, words: lines.join("\n"), result: got }
  }))

// ---- The registry

export const registry = (workspace: string): Promise<Said<readonly Listed[]>> =>
  perform(command(workspace, registryOf, (got, method): Said<readonly Listed[]> => {
    if ("folder" in got) return { exitCode: 2, words: openWords(workspace, got) }
    if ("refused" in got) return { exitCode: 2, words: notWellFormed(got.refused, method) }
    const lines = got.map((e) => `- ${e.name}: ${e.purpose}\n  writes ${e.writes.length === 0 ? "no node" : e.writes.join(", ")}; rests on ${e.rests.length === 0 ? "nothing" : e.rests.join(", ")}`)
    return { exitCode: 0, words: [`The registry holds ${got.length} graph function${got.length === 1 ? "" : "s"}:`, ...lines].join("\n"), result: got }
  }))
