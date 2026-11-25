/**
 * The sessions service: the framework starts a session with its brief, in the
 * workspace's folder, and ends every process it knows to be of it at its
 * return, when its time is over, and when the run receives a signal
 * (REQ-FLOW-001, "Start and end a session" and "Fail"; REQ-FLOW-003;
 * REQ-FLOW-005). The supervised child knows them by their parent, their group
 * and the ticket's mark, from the agent's own process on (C12, D212, D222). A
 * session's end says how many of its processes were ended and, where one is
 * still alive or the framework finds one it cannot place, why: such a session
 * is not over, and the run goes no further (D221, D223). The session is given the path of its brief and
 * nothing else (REQ-ALG-007).
 *
 * This module holds the command binding: the settings file names a command for
 * each agent, and the framework starts it through the supervised child (C12)
 * in the workspace's folder, with the path of the brief. A session's end gives what it
 * printed, whether it returned or failed. The stand-in agent of the
 * scenarios is a second layer of the same service (`stand_in.ts`).
 *
 * @uses C12 C16 H6
 * @is REQ-FLOW-001 REQ-FLOW-003 REQ-FLOW-005 REQ-ALG-007 REQ-INTERFACE-001
 */
import * as Context from "effect/Context"
import * as Effect from "effect/Effect"
import * as Layer from "effect/Layer"
import type * as ChildProcessSpawner from "effect/process/ChildProcessSpawner"
import { now } from "../kit/clock.js"
import { withPath } from "../kit/path_in_command.js"
import { bindSignals, goNoFurther, inherited, settled, supervise, type Mark, type Signal, type Unread } from "../kit/supervised_child.js"
import type { Brief } from "../algorithms/brief.js"

export type { Mark, Signal }

export interface Call {
  readonly vector: string
  readonly kind: "work" | "evaluation"
  /** The workspace's folder, where the session works, by its absolute path. */
  readonly folder: string
  readonly brief: Brief
  /** Where the brief is written, by its absolute path. */
  readonly briefPath: string
  /** The agent the settings file names, and its command. */
  readonly agent: { readonly name: string; readonly command: readonly string[] }
  /** How long the session may run. */
  readonly minutes: number
  /** The mark every process of the session carries: the ticket's, in its workspace (D212). */
  readonly mark: Mark
}

/** How a session ended, with what it printed: its output and its errors as one text; for one that could not be started, why. What it cost is read from what it printed, by the step (D91). */
export type End = (
  | { readonly ended: "returned"; readonly seconds: number; readonly printed: string }
  | { readonly ended: "failed"; readonly seconds: number; readonly why: string; readonly printed: string }
  /** The run received a signal while the session was at work (REQ-FLOW-003). */
  | { readonly ended: "cut off"; readonly signal: Signal; readonly printed: string }
) & {
  /** How many processes of the session the framework ended, where it ended any (D214). */
  readonly processes?: number
  /** Where the session is not over, why: each process of it still alive, each the framework cannot place, or what it cannot tell (D221, D223). */
  readonly unended?: string
  /** Where the table of processes could not be read, how: `unended` is then the one sentence of D249, which names no process. */
  readonly table?: Unread
}

export class Sessions extends Context.Service<Sessions, {
  /** The name the log gives the agent the settings file names. */
  readonly agentOf: (named: string) => string
  /** Starts a new session and waits until every process it knows to be of it is ended, and looks for one it cannot place (REQ-FLOW-005). */
  readonly start: (call: Call) => Effect.Effect<End>
  /** Once the session's end is recorded: the signal the run received from the session's start, where it received one (D214). */
  readonly settled: () => Effect.Effect<Signal | undefined>
  /** Ends this run, which goes no further: with the exit code of the signal it was cut off by, or 1 where a session could not be ended; saying why, where there are words (REQ-FLOW-003, D221). */
  readonly goNoFurther: (signal: Signal | undefined, words?: string) => Effect.Effect<never>
  /** The workspaces of the sessions this process was started from, by the marks it inherited (REQ-INTERFACE-001, D217). */
  readonly within: () => Effect.Effect<readonly string[]>
}>()("stdo-builder/Sessions") {}

export const commandSessions: Layer.Layer<Sessions, never, ChildProcessSpawner.ChildProcessSpawner> = Layer.effect(
  Sessions,
  Effect.gen(function*() {
    const context = yield* Effect.context<ChildProcessSpawner.ChildProcessSpawner>()
    bindSignals()
    return Sessions.of({
      agentOf: (named) => named,
      goNoFurther,
      settled: () => Effect.sync(settled),
      within: () => Effect.sync(inherited),
      start: (call) =>
        Effect.gen(function*() {
          // The brief's path goes where the command marks it, or last (H6).
          const [command = "", ...args] = withPath(call.agent.command, call.briefPath)
          const began = now().millis
          const o = yield* supervise({ command, args, cwd: call.folder, deadline: call.minutes * 60_000, merged: true, mark: call.mark }).pipe(
            Effect.provideContext(context)
          )
          const seconds = (now().millis - began) / 1000
          if (o.outcome === "could not start") return { ended: "failed", seconds, why: `it could not start: ${o.why}`, printed: o.why } satisfies End
          // How many processes of it were ended, and why not every one, where not every one could be (D213, D221).
          const processes = { ...(o.ended === undefined || o.ended === 0 ? {} : { processes: o.ended }), ...(o.unended === undefined ? {} : { unended: o.unended }), ...(o.table === undefined ? {} : { table: o.table }) }
          if (o.outcome === "cut off") return { ended: "cut off", signal: o.signal, printed: o.printed ?? "", ...processes } satisfies End
          if (o.outcome !== "returned") {
            return { ended: "failed", seconds, why: o.outcome === "ran over" ? "it ran longer than allowed and was ended" : `it ${o.outcome}: ${o.why}`, printed: o.printed ?? "", ...processes } satisfies End
          }
          if (o.code !== 0) return { ended: "failed", seconds, why: `it exited with ${o.code}`, printed: o.output, ...processes } satisfies End
          return { ended: "returned", seconds, printed: o.output, ...processes } satisfies End
        })
    })
  })
)
