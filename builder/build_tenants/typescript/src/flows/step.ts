/**
 * A step (REQ-FLOW-005): one attempt at one vector, in the workspace's folder,
 * on the ticket's branch.
 *
 * Each reading the step decides on is `snapshot(v)`, and the one a verdict's
 * identities are taken from runs no check (CALCULUS L3, section 5).
 *
 * On the first entry to a vector under the ticket's confirmed term, the
 * checklist shows that its work began and its working session starts, with
 * nothing judged before it (D209). Otherwise, where the vector's asset is
 * there, `passes` is asked first, and a working session follows only where a check says no, a verdict or the user's answer
 * says no, the ticket without its term is `changed`, or an asset is `changed` and the vector
 * declares no evaluation. A session is started with its `brief`, the
 * activation packet of its frame, which holds references only (D88); on its
 * return `trespass` is asked against the identities of the files at its start
 * (C1, C2). What the agent printed is read for the cost and the calls it
 * reported, which go into the log and into no decision (D91). Files it
 * returns stop the run; the framework puts nothing back. A session is over
 * when every process the framework knows to be of it is ended and it finds
 * none it cannot place, and the log holds how many the framework ended (D213,
 * D214, D222, D223); where the run receives a signal while a session is at
 * work, it notes that and goes no further (REQ-FLOW-003); where a process it
 * knows is still alive, or it finds one it cannot place, the session is not
 * over, and the run commits, judges and starts nothing more on the ticket and
 * is cut off, leaving its hold, naming each (REQ-FLOW-005, D221). What a session
 * printed is kept in a file of its own in the workspace's folder when it
 * returns or fails, which its entry names, and the run keeps where it is for
 * each session that failed (D81, D218). Where the vector declares an evaluation, its
 * asset is there (D97) and each check of the nodes it writes says yes (D173), and its verdict
 * does not stand, or says that it cannot judge, a new session makes it. A
 * yes or a no is committed, and the framework then adds a `resolved
 * evaluation` line to the ticket at each node the vector writes that an
 * evaluation accepts, on the commit that holds what the verdict judged
 * (D164, D203).
 * A verdict that says it cannot judge stops the run, which names where the
 * findings are (D90). Then `passes` is asked and
 * what the checks found is written; where a decision is declared and no answer
 * stands, the user is asked. The result is committed whether or not the
 * vector closed (C13), and the event log is added to.
 *
 * Before a working session bound to a stretch starts, `session` adds a
 * `bound` line to the ticket's checklist and commits it. The next reading
 * finds the binding from that line (`boundNow`, `gather.ts`), and holds what
 * that session left as its own, whether it returned, failed or was killed
 * (D204).
 *
 * Where the vector's graph function is not a single session, its inner terms
 * are run in its place, in the order written (C5): a session is a working
 * session on the vector, and a workflow's vectors are stepped on as `next`
 * gives them among them, until none may run (REQ-GRAPH-006). The vector is
 * then judged by its own evaluation and checks, whatever its inner vectors
 * did.
 *
 * `steps` makes the steps on one workflow, the governing graph or an inner
 * one: again on a vector after its evaluation said no, within the attempts
 * the graph allows (C9); after a check said no, while `progress` says yes;
 * after a session failed, unless the one before it failed too (D210); until
 * none may run or the run ends, and within the bound `rounds` of the
 * workflow.
 *
 * No session is started past a limit the settings set on the run, of sessions
 * or of minutes (C9, C16); the run then ends as stopped.
 *
 * The state of a run passes into a step and into the `steps` of an inner
 * workflow, and comes back out with their ending (design, CALCULUS.md section
 * 5). Each repeat decides on the outcome of its body: a fault met inside it
 * ends the run as stopped, naming the vector of the state it carries, or
 * refused where that state names none. Every entry names the run.
 *
 * @uses C1 C2 C3 C4 C5 C6 C9 C12 C13 C14 C16 C17 H1 H6
 * @is REQ-FLOW-001 REQ-FLOW-005 REQ-FLOW-006 REQ-FLOW-007 REQ-ALG-007 REQ-ALG-008 REQ-GRAPH-006 REQ-PARAM-003 REQ-METHOD-006
 */
import { ATTEMPTS, MINUTES, pathsOf, type Vector, type Workflow } from "../graph/terms.js"
import { inPlace } from "../graph/walk.js"
import { brief, lines, type Basis, type Release } from "../algorithms/brief.js"
import { ASKED, type Given, type Recorded, type Snapshot, type TicketLine } from "../algorithms/facts.js"
import { changed } from "../algorithms/open.js"
import { next } from "../algorithms/next.js"
import { asksUser, cannotRun, firstEntry, identitiesAt, isDone, overturned, passes, recordsOf, standsFor, type Outcome } from "../algorithms/passes.js"
import { progress } from "../algorithms/progress.js"
import { declaredAt, placedOf, type Reason, type WellFormed } from "../algorithms/well_formed.js"
import { within } from "../kit/bounded_loop.js"
import { decide, each, end, fault, outcome, repeat, sequence, using, type Round } from "../kit/calculus.js"
import { now as clock } from "../kit/clock.js"
import { Files } from "../services/files.js"
import { Git } from "../services/git.js"
import { Sessions } from "../services/sessions.js"
import type { Flow, Services } from "../services/services.js"
import { read } from "../kit/lossless_encoding.js"
import { withPath } from "../kit/path_in_command.js"
import { BY_HAND, committed } from "./commit.js"
import { logOf, note } from "./events.js"
import { gather, type Here } from "./gather.js"
import { afterSession, changedQuestion, noteNow, notedWords, settle, take } from "./changed.js"
import { linesChanged, questionFor } from "./question.js"
import { addLines, agentFor, at, foundPath, frameworkPlaces, markOf, nodes, PLACES, VerdictShape, printedPath, reported, type Builder, type BuilderRecord, type Fault, type Workspace } from "./workspace.js"

/** How a run ends: in exactly one of four ways (REQ-FLOW-003). */
export type Ending =
  /** The work done; inside a larger repository, with each file outside the workspace's folder the merge took in (REQ-FLOW-003, REQ-FLOW-008 step 2, D256). */
  | { readonly ending: "done"; readonly ticket: string; readonly merged: string; readonly into: string; readonly outside?: readonly string[] }
  /** Waiting for the user's answer; or, with `ruling`, for the user's ruling on what changed while a session worked, with how many files were named (REQ-FLOW-006). */
  | { readonly ending: "waiting"; readonly ticket: string; readonly vector: string; readonly question: string; readonly ruling?: number }
  | {
    readonly ending: "stopped"
    readonly ticket: string
    readonly vector?: string
    readonly why: string
    readonly files?: readonly string[]
    readonly checks?: readonly string[]
    readonly found?: string
    /** Where what the last working session of the vector printed is kept, for a vector that could not close (D97). */
    readonly printed?: string
  }
  | {
    readonly ending: "refused"
    readonly why: "release" | "not well formed" | "held" | "limit" | "nothing" | "not set up" | "unresolved" | "fault" | "cannot tell" | "ps" | "alive" | "branch" | "main"
    /** For "held": each hold, by its file, and the process it names (REQ-FLOW-001, D216). */
    readonly holds?: readonly { readonly file: string; readonly by?: { readonly pid: number; readonly start?: string } }[]
    /** For "release": what the settings record, and what is running (REQ-FLOW-010). */
    readonly release?: { readonly recorded: BuilderRecord; readonly running: Builder }
    readonly reasons?: readonly Reason[]
    /** For "unresolved": the files on main git could not merge; for "main", the files git named where it refused to take main in. */
    readonly files?: readonly string[]
    /** For "fault": what failed and what the user does next, in plain words (D75); for "cannot tell" and "alive", what the framework found (D215); for "ps", the one sentence that `ps` was not found or could not read the table of processes, and what to install (D249); for "main", git's refusal to take main in or to merge into it, before any step (REQ-FLOW-008); for "unresolved", where the user resolves the files (D240). */
    readonly fault?: string
  }

/**
 * The attempts made at one vector in this run, each a no of its evaluation
 * (REQ-PARAM-003); and what the last working session of the attempt under way
 * left failing, for `progress`. Which sessions failed in a row is the run's
 * `inRow` (D219).
 */
export interface Tried {
  readonly used: number
  readonly before?: readonly Outcome[]
}

/**
 * What a run carries from one step to the next and nowhere else (L4): the
 * attempts made at each vector, by the workflow the vector is in; when it
 * began, and how many sessions it has started, for the limits the settings
 * set (REQ-PARAM-003); and, for the ending's words, the vector of the step
 * under way or of the last step made (D75) and where what each session that
 * failed in this run printed is kept, from the workspace's folder, once each
 * (D81).
 */
export interface RunState {
  readonly attempts: ReadonlyMap<Workflow, ReadonlyMap<string, Tried>>
  readonly began: number
  readonly sessions: number
  readonly vector?: string
  readonly failed: readonly string[]
  /** By vector, how many sessions on it in this run failed one after another, up to the last; a session that returns sets it to none (REQ-FLOW-005, D210, D219). */
  readonly inRow?: ReadonlyMap<string, number>
  /** Where what the last working session printed is kept, from the workspace's folder (D97, D218). */
  readonly lastWork?: string
  /** What differed among the branches, tags and stash, and outside the workspace's folder, while a session worked, in the run's words; it holds no ticket (REQ-FLOW-001, D228). */
  readonly noted?: readonly string[]
}

/** What the steps are on, read in the terms that enclose them: the workspace, its folder, the ticket, the run's id and the method release, with where it is installed where the run found it (D89). */
export interface On {
  readonly ws: Workspace
  readonly here: Here
  readonly ticket: string
  readonly run: string
  readonly release?: Release
}

/** What a fault says in plain words: what failed, then what the user does next. */
const faultWhy = (root: string, f: Fault): string => {
  const first = f._tag === "GitRefused" ? (f.why.split("\n")[0] ?? "") : ""
  const what = f._tag === "GitRefused"
    ? `git refused: ${first.endsWith(".") ? first.slice(0, -1) : first}`
    : `the workspace cannot be read or written at ${f._tag === "FileRefused" ? f.path : logOf(root)}`
  return `${what}. Put right what it names, then start a run again`
}

/** The ending a fault gives: stopped, naming the vector, where the state names one; refused where it names none (D75). */
export const faultEnding = (root: string, f: Fault, ticket: string | undefined, vector: string | undefined): Ending => {
  const why = faultWhy(root, f)
  return ticket !== undefined && vector !== undefined ? { ending: "stopped", ticket, vector, why } : { ending: "refused", why: "fault", fault: why }
}

/** The limit the settings set on a run that a new session would pass, in words; or undefined where it may start (C9). */
const limitReached = (ws: Workspace, run: RunState): string | undefined => {
  const limits = ws.settings.limits
  if (limits?.sessions !== undefined && !within(run.sessions, limits.sessions)) return `the run reached the limit the settings set, ${limits.sessions} session${limits.sessions === 1 ? "" : "s"}`
  return minutesReached(ws, run)
}

/** The limit of minutes the settings set on a run, in words, where the run has reached it (C9, C16). */
export const minutesReached = (ws: Workspace, run: RunState): string | undefined => {
  const minutes = ws.settings.limits?.minutes
  if (minutes !== undefined && !within(clock().millis - run.began, minutes * 60_000)) return `the run reached the limit the settings set, ${minutes} minute${minutes === 1 ? "" : "s"}`
  return undefined
}

export type StepEnd =
  | { readonly step: "closed" }
  /** Inner terms run in the vector's place ended the run. */
  | { readonly step: "ended"; readonly ending: Ending }
  /** The checks or the verdict said no; `judged` where an evaluation of this step said no, which is one attempt (D210); where a working session worked in the step, where what it printed is kept (D97). */
  | { readonly step: "open"; readonly failing: readonly Outcome[]; readonly found: string; readonly printed?: string; readonly judged?: true }
  | { readonly step: "failed"; readonly why: string }
  | { readonly step: "asks"; readonly question: string; readonly ruling?: number }
  | { readonly step: "stopped"; readonly why: string; readonly files?: readonly string[] }
  /** A fault met after a session of the step, which keeps the places of what the step's sessions printed. */
  | { readonly step: "fault"; readonly fault: Fault }

/** How a step ended, and the run's state after it. */
export interface Stepped {
  readonly end: StepEnd
  readonly state: RunState
}

const stepped = (e: StepEnd, state: RunState): Stepped => ({ end: e, state })

/** `rest`, where a fault it meets is the step's ending, with the state as the session before it left it (D81). */
const keeping = (state: RunState, rest: Flow<Stepped, Fault>): Flow<Stepped, Fault> =>
  decide(outcome(rest), (o) => end("fault" in o ? { end: { step: "fault", fault: o.fault }, state } : o.value))

/** What one session gave the step. */
type Ran =
  | { readonly limit: string }
  | { readonly failed: string }
  /** Files that changed while the session worked, outside what its step writes: the question on them, and how many (REQ-ALG-008). */
  | { readonly changed: string; readonly count: number }
  /** The folder was found on another branch than the ticket's (REQ-FLOW-005 step 3). */
  | { readonly elsewhere: string }
  | { readonly returned: true; readonly wroteVerdict: boolean }
  | { readonly faulted: Fault }

/** Starts one session of a kind on the vector, where no limit of the run is reached, and waits for its return; then looks at the branch the folder is on and compares the workspace with the identities kept from the session's start (REQ-ALG-008, D226). */
const session = (on: On, v: Vector, kind: "work" | "evaluation", s: Snapshot, state: RunState): Flow<{ readonly ran: Ran; readonly state: RunState }, Fault> => {
  const { ws, here, ticket, run } = on
  const limits = ws.settings.limits
  // Inside a larger repository, the packet says so (REQ-ALG-007, D256).
  const basis: Basis = { places: frameworkPlaces(ws), ...(on.release === undefined ? {} : { release: on.release }), ...(limits === undefined ? {} : { limits }), ...(ws.within === "" ? {} : { inside: true as const }) }
  const limit = limitReached(ws, state)
  if (limit !== undefined) return end({ ran: { limit }, state })
  // An evaluating packet names, at each node it judges, main's content of it where the branch and main last met (REQ-ALG-007, D208).
  const judged = kind === "evaluation" && here.line !== ws.main ? recordsOf(ws.graph, v, "evaluation") : []
  const pathsAt = (n: string): readonly string[] => {
    const node = nodes(ws).find((m) => m.name === n)
    return node === undefined ? [] : pathsOf(node)
  }
  // With each commit on the branch since then that holds the user's change by hand at the node (D244).
  const read: Flow<Snapshot, Fault> = judged.length === 0 ? end(s) : using(Git, (git) =>
    decide(git.mergeBase(here.folder, "HEAD", ws.main), (base) =>
      base === undefined ? end(s) : decide(git.underCommit(here.folder, base, judged.flatMap(pathsAt)), (held) =>
        decide(each(judged, (n) => decide(git.commitsWith(here.folder, base, here.line, BY_HAND, pathsAt(n)), (commits) => end([n, commits] as const))), (byHand) =>
          end({ ...s, main: { commit: base, holds: judged.filter((n) => pathsAt(n).some((p) => held?.has(p) === true)), byHand: new Map(byHand.filter(([, c]) => c.length > 0)) } })))))
  return decide(read, (withMain) => {
  const b = brief(ws.graph, v, kind, withMain, basis)
  const counted: RunState = { ...state, sessions: state.sessions + 1 }
  const briefFile = `${PLACES.briefs}/${v.name}.${kind}.md`
  const agent = agentFor(ws.settings, v.name, kind)
  const verdict = kind === "evaluation" && v.evaluation !== undefined ? at(here.folder, v.evaluation.verdict) : undefined
  // A file of its own for what each session printed, which its entry in the log names (REQ-FLOW-001, D218).
  const printed = printedPath(v.name, kind, run, counted.sessions)
  const kept = printed
  // A working session on a stretch is bound to it by a line of the checklist, committed before the session starts (REQ-FLOW-004, D204).
  const stretch = kind === "work" && v.first === true && s.ticket !== "simplest" ? s.ticket.inducting : undefined
  // On the first entry to the vector, the checklist shows that its work began, committed before the session starts (REQ-FLOW-005 step 1, D209).
  const began = kind === "work" && here.ticket !== undefined && firstEntry(ws.graph, v, s)
  const binding: Flow<unknown, Fault> = stretch !== undefined && s.ticket !== "simplest" && here.ticket !== undefined
    ? recorded(on, v, "a session is bound to a stretch", (commit) => [{ line: "bound", vector: v.name, enters: stretch.enters, ends: stretch.ends, commit }])
    : began
    ? recorded(on, v, "the work began", (commit) => [{ line: "began", vector: v.name, commit }])
    : end(undefined)
  return using(Files, (files) =>
    using(Sessions, (sessions) => {
      const named = sessions.agentOf(agent.name)
      const stamp = verdict === undefined ? end(undefined) : files.stamp(verdict)
      return sequence(
        files.write(at(here.folder, briefFile), `${lines(b).join("\n")}\n`),
        binding,
        // The agent's command as it is run, and the commit the session starts from (REQ-FLOW-007), which the run carries to the comparison after the session, where it stands in for identities that cannot serve (REQ-ALG-008, D255).
        using(Git, (git) => decide(git.tipOf(here.folder, here.line), (from) => sequence(
          note(ws.root, { event: "session started", run, ticket, vector: v.name, kind, agent: named, path: briefFile, command: withPath(agent.command, at(here.folder, briefFile)), ...(from === undefined ? {} : { commit: from }) }),
        // The identities of both folders are taken and kept at the session's start, until its result is committed or ruled on (D227).
        decide(noteNow(ws, ticket), (notedBefore) =>
        decide(take(ws, here, ticket, v, kind), () =>
          decide(stamp, (stampBefore) =>
            decide(sessions.start({ vector: v.name, kind, folder: here.folder, brief: b, briefPath: at(here.folder, briefFile), agent, minutes: v.minutes ?? MINUTES, mark: markOf(ws.root, ticket) }), (ended): Flow<{ readonly ran: Ran; readonly state: RunState }, Fault> => {
              // Each time the framework ends processes of the session, the log holds how many (REQ-FLOW-007, D214).
              const stopped = (why: string): Flow<void, Fault> =>
                ended.processes === undefined ? end(undefined) : note(ws.root, { event: "session processes ended", run, ticket, vector: v.name, kind, processes: ended.processes, why })
              const how = ended.ended === "cut off" ? `the run received the ${ended.signal} signal` : ended.ended === "returned" ? "the session returned, and these were still alive" : "the session failed, and these were still alive"
              // Where a process it knows to be of the session is still alive, or it finds one it cannot place, the session is not over: nothing is committed, judged or started on the ticket, and the run is cut off, leaving its hold (REQ-FLOW-003, REQ-FLOW-005, D221).
              // Where the table of processes could not be read, the words are the one sentence of D249, and name no process (REQ-FLOW-005).
              const unended = ended.unended === undefined
                ? undefined
                : ended.table !== undefined
                ? `The run is cut off on the ticket ${ticket}, at ${v.name}: its ${kind === "work" ? "working" : "evaluating"} session is not over, since the framework cannot read the table of processes. ${ended.unended} Until it can, nothing is committed, judged or started on the ticket. What the session printed is kept at ${kept}. Then start a run again: it ends what is left of the session before anything else.`
                : `The run is cut off on the ticket ${ticket}, at ${v.name}: its ${kind === "work" ? "working" : "evaluating"} session is not over: ${ended.unended}. While one of them is alive, nothing is committed, judged or started on the ticket. What the session printed is kept at ${kept}. End each process named here, then start a run again.`
              // What it printed is kept, and the processes ended noted, before the run asks whether it received a signal: a signal from the session's start on is kept until then (D214).
              const recordedEnd = sequence(files.write(at(here.folder, printed), ended.printed), stopped(unended === undefined ? how : `${how}; the session is not over: ${ended.unended ?? ""}`))
              return decide(outcome(recordedEnd), (r) => decide(sessions.settled(), (signal): Flow<{ readonly ran: Ran; readonly state: RunState }, Fault> => {
              // The run received a signal, or the session is not over: the run goes no further, leaving its hold for the next run to find (REQ-FLOW-003).
              if (signal !== undefined || unended !== undefined || ended.ended === "cut off") return sessions.goNoFurther(signal, unended)
              if ("fault" in r) return fault(r.fault)
              // What the agent reported of its cost and its calls, read from what it printed by the fields the settings name (D91); it enters no decision (L5, L9).
              const spent = reported(agent.reports, ended.printed)
              // What it printed is kept in a file of its own, whether it returned or failed (D81, D218); how many sessions on the vector failed in a row, a return setting it to none (D219).
              const inRow = new Map([...(counted.inRow ?? []), [v.name, ended.ended === "failed" ? (counted.inRow?.get(v.name) ?? 0) + 1 : 0]])
              const counts: RunState = { ...counted, inRow, ...(kind === "work" ? { lastWork: kept } : {}) }
              const placed: RunState = ended.ended === "failed" && !counts.failed.includes(kept) ? { ...counts, failed: [...counts.failed, kept] } : counts
              const rest: Flow<{ readonly ran: Ran; readonly noted: readonly string[] }, Fault> = decide(noteNow(ws, ticket, notedBefore), (notedAfter) => decide(stamp, (stampAfter) =>
                using(Git, (git) => decide(git.currentLine(here.folder), (branch): Flow<{ readonly ran: Ran; readonly noted: readonly string[] }, Fault> => {
                  const said = ended.ended === "failed"
                    ? note(ws.root, { event: "session failed", run, ticket, vector: v.name, kind, agent: named, seconds: ended.seconds, why: ended.why, printed, ...spent })
                    : note(ws.root, { event: "session returned", run, ticket, vector: v.name, kind, agent: named, seconds: ended.seconds, printed, ...spent })
                  // The folder on a branch that is not the ticket's: the run names it and goes no further on the ticket (REQ-FLOW-005 step 3).
                  const noted = notedWords(v.name, ws.main, notedBefore, notedAfter)
                  if (branch !== here.line) return sequence(said, end({ ran: { elsewhere: branch ?? "no branch" }, noted }))
                  // Where the identities taken at the session's start are missing, cannot be read, are not its own, name a step the graph does not hold or name what git no longer holds, those of the commit the session started from stand in, and each file that differs from it is put to the user; where git no longer holds that commit, the flow fails (REQ-ALG-008, REQ-FLOW-005 step 3, D246, D255).
                  return decide(afterSession(ws, here, ticket, v.name, kind, from), ({ kept, changed }): Flow<{ readonly ran: Ran; readonly noted: readonly string[] }, Fault> => {
                      // The session wrote its verdict where the file is there now and is not the one that was there at its start, by its writing (N7).
                      const wrote = v.evaluation?.verdict !== undefined && stampAfter !== undefined &&
                        (stampBefore === undefined || stampAfter.written !== stampBefore.written || stampAfter.node !== stampBefore.node)
                      const ran: Ran = changed.length > 0
                        ? { changed: changedQuestion(v.name, changed, kept.stood, ws.main), count: changed.length }
                        : ended.ended === "failed"
                        ? { failed: ended.why }
                        : { returned: true, wroteVerdict: wrote }
                      // Nothing differs on which no yes was given: the identities are no longer kept (D227).
                      return sequence(said, changed.length === 0 ? settle(ws, ticket, kept) : end(undefined), end({ ran, noted }))
                    })
                }))))
              return decide(outcome(rest), (o) => end("fault" in o ? { ran: { faulted: o.fault }, state: placed } : { ran: o.value.ran, state: o.value.noted.length === 0 ? placed : { ...placed, noted: [...(placed.noted ?? []), ...o.value.noted] } }))
            }))
            })))))))
      )
    }))
  })
}

const commitStep = (on: On, v: Vector, how: string): Flow<void, Fault> =>
  decide(committed({ folder: on.here.folder, line: on.here.line }, `step ${v.name}: ${how}`), (commit) =>
    commit === undefined ? end(undefined) : note(on.ws.root, { event: "commit made", run: on.run, ticket: on.ticket, vector: v.name, commit, why: `the result of the step: ${how}` }))

/**
 * Commits what the step left, then adds to the framework's part of the
 * branch's ticket the lines that name that commit, and commits them: what a
 * line names is committed before the line names it (REQ-FLOW-001, D202). It
 * gives the commit the lines name.
 */
const recorded = (on: On, v: Vector, how: string, lines: (commit: string) => readonly TicketLine[]): Flow<string | undefined, Fault> => {
  const { ws, here, run, ticket } = on
  return sequence(
    commitStep(on, v, how),
    using(Git, (git) =>
      decide(git.tipOf(here.folder, here.line), (tip): Flow<string | undefined, Fault> =>
        tip === undefined || here.ticket === undefined
          ? end(tip)
          : sequence(
            addLines(here.folder, here.ticket, lines(tip)),
            decide(committed({ folder: here.folder, line: here.line }, `ticket ${ticket}: ${how}, at ${tip.slice(0, 12)}`, [here.ticket]), (commit) =>
              commit === undefined ? end(undefined) : note(ws.root, { event: "commit made", run, ticket, vector: v.name, commit, why: `the framework's part of the ticket: ${how}` })),
            end(tip)
          )))
  )
}

/** The step's end after a session that did not return as it should: what it did is committed, and the step ends. */
const leftBy = (on: On, v: Vector, ran: Ran, state: RunState, session: "working session" | "evaluating session"): Flow<Stepped, Fault> | undefined => {
  const how = session === "working session" ? "the session" : "the evaluation"
  if ("faulted" in ran) return end({ end: { step: "fault", fault: ran.faulted }, state })
  if ("limit" in ran) return keeping(state, sequence(commitStep(on, v, "a limit of the run was reached"), end(stepped({ step: "stopped", why: ran.limit }, state))))
  if ("failed" in ran) return keeping(state, sequence(commitStep(on, v, `${how} failed`), end(stepped({ step: "failed", why: ran.failed }, state))))
  // What changed while the session worked, outside what its step writes, is put to the user: no verdict is read, no check is run and nothing of the step is committed until the user has ruled (REQ-FLOW-005 step 3, REQ-FLOW-006).
  if ("changed" in ran) {
    return keeping(state, sequence(
      note(on.ws.root, { event: "user asked", run: on.run, ticket: on.ticket, vector: v.name, why: "what changed while a session worked", named: ran.count }),
      end(stepped({ step: "asks", question: ran.changed, ruling: ran.count }, state))
    ))
  }
  if ("elsewhere" in ran) {
    return end(stepped({ step: "stopped", why: `the workspace's folder is on ${ran.elsewhere === "no branch" ? "no branch" : `the branch ${ran.elsewhere}`}, which is not the ticket's, ${on.here.line}. Put it back on ${on.here.line}, git switch ${on.here.line}; nothing is committed, judged or started on the ticket until then` }, state))
  }
  return undefined
}

/** What the checks found, written for the user and the next session to read. */
function foundText(v: Vector, s: Snapshot, outcomes: readonly Outcome[]): string {
  const parts = outcomes.map((o) => {
    const detail = o.source === "check" ? s.checks?.get(o.name)?.detail : undefined
    return `## ${o.name}: ${o.result}\n\n${o.found ?? ""}\n${detail === undefined || detail.trim() === "" ? "" : `\n\`\`\`\n${detail}\n\`\`\`\n`}`
  })
  return `# What the checks of ${v.name} found\n\n${parts.join("\n")}`
}

/** Where the working sessions are: the next part of the vector's graph function, and the run's state. */
interface Parts {
  readonly i: number
  readonly state: RunState
}

/** The working part of a step: each part of the vector's graph function, in the order written (C5, C6). A session works on this vector; a workflow's vectors are stepped on in its place. */
const working = (on: On, v: Vector, s: Snapshot, state: RunState): Flow<Stepped | { readonly worked: RunState }, Fault> => {
  const parts = inPlace(v.function, on.ws.graph.registry)
  return repeat<Parts, Stepped | { readonly worked: RunState }, Fault, Services>(
    { i: 0, state },
    ({ i, state: st }): Flow<Round<Parts, Stepped | { readonly worked: RunState }>, Fault> => {
      const part = parts[i]
      if (part === undefined) return end({ leave: { worked: st } })
      if (part.term === "workflow") {
        return decide(steps(on, part, st), (inner) =>
          end("ended" in inner.traversed ? { leave: { end: { step: "ended", ending: inner.traversed.ended }, state: inner.state } } : { again: { i: i + 1, state: { ...inner.state, vector: v.name } } }))
      }
      // Between parts, the folder is read again; a change to the ticket stays that session's while the last `bound` line is not ended (D204).
      return decide(i === 0 ? end(s) : gather(on.ws, on.here), (now) =>
        decide(session(on, v, "work", now, st), ({ ran, state: after }): Flow<Round<Parts, Stepped | { readonly worked: RunState }>, Fault> => {
          const left = "limit" in ran && i === 0 ? end(stepped({ step: "stopped", why: ran.limit }, after)) : leftBy(on, v, ran, after, "working session")
          return left === undefined ? end({ again: { i: i + 1, state: after } }) : decide(left, (stepped) => end({ leave: stepped }))
        }))
    },
    { rounds: parts.length + 1, leave: (p) => ({ worked: p.state }) }
  )
}

/**
 * The judging part of a step: what the checks found is written and logged, and the step ends by what `passes` says. `worked` says a working session
 * worked in the step; `before` is the step's first reading.
 */
const judging = (on: On, v: Vector, state: RunState, worked: boolean, before: Snapshot, cannot?: string, judgedNo?: boolean): Flow<Stepped, Fault> => {
  const { ws, here, ticket, run } = on
  return decide(gather(ws, here, v.name), (read): Flow<Stepped, Fault> => {
    // A verdict that says the evaluation cannot judge is no resolution: it gives cannot in the step that read it (REQ-ALG-004, D203).
    const last: Snapshot = cannot === undefined ? read : {
      ...read,
      records: new Map<string, Recorded>([...(read.records ?? []), ...recordsOf(ws.graph, v, "evaluation").map((node) => [node, { ...read.records?.get(node), verdict: { says: "cannot", on: identitiesAt(ws.graph, node, read), at: cannot } satisfies Given }] as const)])
    }
    const result = passes(ws.graph, v, last)
    const found = foundPath(v.name)
    const printed = state.lastWork
    const closing = (how: string, event: "vector closed" | "vector left open", why: string, stepEnd: StepEnd): Flow<Stepped, Fault> =>
      sequence(
        // A vector that closes is delivered: the checklist names the commit that holds its work (REQ-FLOW-004).
        event === "vector closed" ? recorded(on, v, how, (commit) => [{ line: "delivered", vector: v.name, commit }]) : commitStep(on, v, how),
        note(ws.root, { event, run, ticket, vector: v.name, why }),
        end({ end: stepEnd, state }))
    const done = result.outcomes.filter(isDone) // a check not done is neither logged as run nor failing (CALCULUS L3)
    const failing = done.filter((o) => o.source !== "answer" && o.result !== "yes")
    const findings = v.evaluation?.findings ?? ""
    const judged: Flow<Stepped, Fault> = cannotRun(result).length > 0
      ? closing("a check could not be run", "vector left open", "a check could not be run", { step: "stopped", why: `a check of ${v.name} could not be run; what it found is kept at ${found}` })
      : result.outcomes.some((o) => o.source === "verdict" && o.result === "cannot")
      // The evaluator's words stay in its findings: the ending names where they are, and the log holds none of them (D90).
      ? closing("the evaluation cannot judge", "vector left open", "the evaluation cannot judge", { step: "stopped", why: `the evaluation of ${v.name} cannot judge; why is in its findings at ${findings}` })
      : result.result === "yes"
      ? closing("closed", "vector closed", "its checks pass on the folder as it is", { step: "closed" })
      : asksUser(ws.graph, v, last)
      ? using(Files, (files) =>
          decide(here.ticket === undefined ? end(undefined) : files.read(at(here.folder, here.ticket)), (text) => {
            // Where the user's change left a ticket the induction's checks did not pass, the induction ran again, and the question says so (REQ-FLOW-004).
            const told = worked && v.first === true ? overturned(ws.graph, before) : undefined
            // The question is given in the run's ending, and no file holds it; the checklist shows the work delivered for the user's decision, and the question counts the lines changed up to that commit (REQ-FLOW-006, D211).
            return decide(recorded(on, v, "the user is asked", (commit) => [{ line: "delivered", vector: v.name, commit, decision: true, when: clock().written }]), (commit) =>
              decide(commit === undefined ? end(undefined) : linesChanged(ws, here.folder, v, commit), (counted) =>
                sequence(
                  note(ws.root, { event: "user asked", run, ticket, vector: v.name }),
                  end({ end: { step: "asks" as const, question: questionFor(ws, v, last, text ?? "", told, counted) }, state })
                )))
          }))
      : closing("left open", "vector left open", failing.map((o) => o.name).join(", "), { step: "open", failing, found, ...(worked && printed !== undefined ? { printed } : {}), ...(judgedNo === true ? { judged: true as const } : {}) })
    return sequence(
      using(Files, (files) => files.write(at(here.folder, foundPath(v.name)), foundText(v, last, result.outcomes))),
      each(done.filter((o) => o.source === "check"), (o) =>
        note(ws.root, { event: "check run", run, ticket, vector: v.name, check: o.name, result: o.result, ...(last.checks?.get(o.name)?.seconds === undefined ? {} : { seconds: last.checks.get(o.name)?.seconds ?? 0 }) })),
      judged
    )
  })
}

/**
 * The evaluating part of a step, where the vector declares an evaluation and a session worked, or no verdict stands, or the one that stands says it
 * cannot judge (D90), its asset is there (D97) and each check of the nodes it writes says yes; then the judging part. Where a check says no, the step is left open
 * with what the checks found, for the next working session, so no verdict is given over a check that fails (D173).
 */
const evaluating = (on: On, v: Vector, first: Snapshot, wrote: boolean, state: RunState): Flow<Stepped, Fault> => {
  const { ws, here, ticket, run } = on
  const evaluation = v.evaluation
  const stands = standsFor(ws.graph, v, "evaluation", first)
  if (evaluation === undefined || !(wrote || stands === undefined || stands.says === "cannot")) return judging(on, v, state, wrote, first)
  const checked = (s: Snapshot): boolean => passes(ws.graph, v, s).outcomes.every((o) => o.source !== "check" || o.result === "yes")
  return decide(wrote ? gather(ws, here, v.name) : end(first), (now) =>
    // An asset that is not there is not judged: the checks say what is missing (D97); nor is one a check says no of (D173).
    !assetThere(ws, v, now) || !checked(now) ? judging(on, v, state, wrote, first) : decide(session(on, v, "evaluation", now, state), ({ ran, state: after }): Flow<Stepped, Fault> => {
      const left = leftBy(on, v, ran, after, "evaluating session")
      if (left !== undefined) return left
      // A verdict stands only for content this session judged: where it wrote none, no resolution is added, and the last one in the ticket stays on the commit it names (D203).
      // It is given at each node the vector writes that an evaluation accepts, for that node, what it declares and the nodes it depends on, so that it is read alike whoever wrote the node (D164, D168).
      // A yes or a no is the evaluation's resolution, added to the ticket with the commit that holds what it judged (REQ-FLOW-005 step 4, D203).
      const given: Flow<{ readonly cannot?: string; readonly no?: true }, Fault> = "returned" in ran && ran.wroteVerdict
        ? using(Files, (files) =>
          decide(files.read(at(here.folder, evaluation.verdict)), (text): Flow<{ readonly cannot?: string; readonly no?: true }, Fault> => {
            const got = text === undefined ? undefined : read(VerdictShape, text)
            const says = got === undefined || "refused" in got ? undefined : got.value.verdict
            const seen = note(ws.root, { event: "verdict read", run, ticket, vector: v.name, result: says ?? "not readable", path: evaluation.verdict, findings: evaluation.findings })
            if (says === "cannot") return sequence(seen, end({ cannot: evaluation.verdict }))
            if (says === undefined) return sequence(seen, end({}))
            return sequence(seen, recorded(on, v, "the evaluation judged", (commit) =>
              recordsOf(ws.graph, v, "evaluation").map((node): TicketLine => ({ line: "resolved", by: "evaluation", says, at: node, commit, verdict: evaluation.verdict, findings: evaluation.findings }))), end(says === "no" ? { no: true as const } : {}))
          }))
        : sequence(note(ws.root, { event: "verdict not written", run, ticket, vector: v.name, path: evaluation.verdict, why: "the evaluating session wrote no verdict, so none stands for the content as it is now" }), end({}))
      return keeping(after, decide(given, (g) => judging(on, v, after, wrote, first, g.cannot, g.no === true)))
    }))
}

/** The vector's asset is there: the branch's ticket for the first vector, otherwise each node it writes has an identity. */
const assetThere = (ws: Workspace, v: Vector, s: Snapshot): boolean => v.first === true || placedOf(ws.graph, v).writes.every((n) => s.identities.has(n))

/** One attempt at one vector. */
export const step = (on: On, v: Vector, state: RunState): Flow<Stepped, Fault> =>
  decide(gather(on.ws, on.here, v.name), (s): Flow<Stepped, Fault> => {
    const p = passes(on.ws.graph, v, s)
    // A check that cannot be run stops the run (REQ-FLOW-005). A verdict that says it cannot judge is made again (D90).
    const cannot = cannotRun(p)
    if (cannot.length > 0) {
      return end({ end: { step: "stopped", why: `a check of ${v.name} could not be run: ${cannot.map((o) => `${o.name} (${o.found ?? ""})`).join("; ")}` }, state })
    }
    const differs = changed(on.ws.graph, v, s)
    // On the first entry to a vector the ticket's term names, its working session starts with nothing judged before it (REQ-FLOW-005 step 1, D209).
    const work = firstEntry(on.ws.graph, v, s) || !assetThere(on.ws, v, s) || p.outcomes.some((o) => o.source === "check" && o.result === "no") ||
      standsFor(on.ws.graph, v, "evaluation", s)?.says === "no" ||
      standsFor(on.ws.graph, v, "decision", s)?.says === "no" ||
      differs.includes(ASKED) ||
      (v.evaluation === undefined && differs.some((k) => k !== ASKED))
    const worked: Flow<Stepped | { readonly worked: RunState | undefined }, Fault> = work ? working(on, v, s, state) : end({ worked: undefined })
    return decide(worked, (w): Flow<Stepped, Fault> =>
      "end" in w ? end(w) : evaluating(on, v, s, w.worked !== undefined, w.worked ?? state))
  })

/** How the steps on one workflow ended: the run ended, or no vector of it may run. */
export type Traversed = { readonly ended: Ending } | { readonly none: true }

/** The attempts at each vector with those at `name`, in `workflow`, replaced. */
const withTried = (state: RunState, workflow: Workflow, name: string, tried: Tried): RunState => ({
  ...state,
  attempts: new Map([...state.attempts, [workflow, new Map([...(state.attempts.get(workflow) ?? []), [name, tried]])]])
})

/** What one step on `v` gives the steps on its workflow: again, or the end of the steps. */
const afterStep = (on: On, workflow: Workflow, v: Vector, stepped: Stepped): Round<RunState, { readonly traversed: Traversed; readonly state: RunState }> => {
  const { ticket } = on
  const { end: e, state } = stepped
  const ended = (ending: Ending) => ({ leave: { traversed: { ended: ending }, state } })
  if (e.step === "closed") return { again: state }
  if (e.step === "ended") return ended(e.ending)
  if (e.step === "fault") return ended(faultEnding(on.ws.root, e.fault, ticket, state.vector))
  if (e.step === "asks") return ended({ ending: "waiting", ticket, vector: v.name, question: e.question, ...(e.ruling === undefined ? {} : { ruling: e.ruling }) })
  if (e.step === "stopped") return ended({ ending: "stopped", ticket, vector: v.name, why: e.why, ...(e.files === undefined ? {} : { files: e.files }) })
  const so = state.attempts.get(workflow)?.get(v.name) ?? { used: 0 }
  const bound = v.attempts ?? ATTEMPTS
  const stopped = (why: string, tried: RunState, open?: Extract<StepEnd, { step: "open" }>): Round<RunState, { readonly traversed: Traversed; readonly state: RunState }> => ({
    leave: {
      traversed: {
        ended: {
          ending: "stopped",
          ticket,
          vector: v.name,
          why,
          ...(open === undefined ? {} : { checks: open.failing.map((o) => o.name), found: open.found, ...(open.printed === undefined ? {} : { printed: open.printed }) })
        }
      },
      state: tried
    }
  })
  // A session that failed is made again in the same attempt, unless the session before it on the vector in this run failed too; one that returned between them breaks the row (REQ-FLOW-005, D210, D219).
  if (e.step === "failed") return (state.inRow?.get(v.name) ?? 0) < 2 ? { again: state } : stopped(`the session on ${v.name} failed twice in a row: ${e.why}`, state)
  // An evaluation that said no is one attempt; the step is made again while the attempts the graph allows are not used up (REQ-PARAM-003).
  if (e.judged === true) {
    const used = so.used + 1
    const tried = withTried(state, workflow, v.name, { used })
    return within(used, bound) ? { again: tried } : stopped(`${v.name} could not close after ${used} attempt${used === 1 ? "" : "s"}: its evaluation said no each time`, tried, e)
  }
  // A check said no, so no evaluation was made: the working session is made again in the same attempt while `progress` says yes (REQ-ALG-009).
  const tried = withTried(state, workflow, v.name, { used: so.used, before: e.failing })
  return progress(so.before, e.failing)
    ? { again: tried }
    : stopped(`${v.name} could not close: the same number of checks failed twice in a row`, tried, e)
}

/**
 * `rounds(w)`, the bound of the steps on `w` (design, CALCULUS.md section 5,
 * D210): over the vectors of `w`, for each of its attempts and one more, two
 * rounds for each count of failing outcomes its working sessions can pass
 * through, since the count must fall from one to the next and no two sessions
 * fail in a row; and one round more for the reading that finds none.
 */
const rounds = (graph: WellFormed, workflow: Workflow): number =>
  workflow.vectors.reduce((sum, v) => {
    const p = placedOf(graph, v)
    const outcomes = [v.name, ...p.writes].flatMap((n) => declaredAt(graph, n)).length + p.writes.length + p.rests.length + 2
    return sum + ((v.attempts ?? ATTEMPTS) + 1) * 2 * (outcomes + 2)
  }, 1)

/**
 * The steps on one workflow, the governing graph or one inside a vector's
 * graph function: `next` gives the vector among its vectors, in the
 * workspace's folder, and a step is made on it; again while `progress` says yes
 * within the attempts the graph allows (C9), until none may run or the run
 * ends. The `repeat` is bounded by `rounds(w)` and has no measure: which
 * vectors are open is read in each round. Where the bound is reached, the run
 * stops, naming the vector of the state (L6). A step on a vector of an inner
 * workflow appears in the event log as any other (REQ-GRAPH-006). A fault met
 * in a round ends the steps, naming the vector of the state the round carries.
 */
export const steps = (on: On, workflow: Workflow, state: RunState): Flow<{ readonly traversed: Traversed; readonly state: RunState }> => {
  type Left = { readonly traversed: Traversed; readonly state: RunState }
  const faulted = (f: Fault, st: RunState): Round<RunState, Left> => ({ leave: { traversed: { ended: faultEnding(on.ws.root, f, on.ticket, st.vector) }, state: st } })
  return repeat<RunState, Left, never, Services>(
    state,
    (st) =>
      decide(outcome(gather(on.ws, on.here)), (g): Flow<Round<RunState, Left>> => {
        if ("fault" in g) return end(faulted(g.fault, st))
        const v = next(on.ws.graph, g.value, workflow)
        if (v === undefined) return end({ leave: { traversed: { none: true }, state: st } })
        const stepping: RunState = { ...st, vector: v.name }
        return decide(outcome(step(on, v, stepping)), (o) => end("fault" in o ? faulted(o.fault, stepping) : afterStep(on, workflow, v, o.value)))
      }),
    {
      rounds: rounds(on.ws.graph, workflow),
      leave: (st) => ({ traversed: { ended: { ending: "stopped", ticket: on.ticket, ...(st.vector === undefined ? {} : { vector: st.vector }), why: "the steps reached their bound" } }, state: st })
    }
  )
}
