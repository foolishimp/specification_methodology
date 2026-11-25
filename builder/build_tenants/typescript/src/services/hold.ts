/**
 * The hold service: while a run works on a ticket no second run takes that
 * ticket (REQ-FLOW-001, "Hold"). It is carried out by the exclusive hold bound
 * to a process (C11): a killed run leaves nothing that refuses the next, but
 * a process of its session still alive after the next run has tried to end
 * it, or a process the framework cannot place (C12, D215, D223).
 *
 * @uses C11 C12
 * @is REQ-FLOW-001 REQ-FLOW-003
 */
import * as Context from "effect/Context"
import * as Effect from "effect/Effect"
import type * as FileSystem from "effect/FileSystem"
import * as Layer from "effect/Layer"
import type * as ChildProcessSpawner from "effect/process/ChildProcessSpawner"
import { held, holding, keeping, left, type Holder, type Left } from "../kit/exclusive_hold.js"
import { endMarked, marked, named, tableRead, type Ended, type Mark, type Sought, type Unread } from "../kit/supervised_child.js"

export type { Ended, Holder, Left, Mark, Sought, Unread }

/** Why the framework cannot tell, ending nothing; with how the table of processes could not be read, where that is why: the words are then the one sentence of D249, which names no process. */
export interface Cannot {
  readonly cannot: string
  readonly table?: Unread
}

/** What the framework finds of the sessions on a ticket, ending nothing: each process it knows to be of them that is alive, and each it cannot place, named by its number, when it started and its command (D222, D223). */
export interface Alive {
  readonly alive: readonly string[]
  readonly unplaced: readonly string[]
}

export class Hold extends Context.Service<Hold, {
  /** Runs `body` while holding `file`; where another run holds it, that run's process, where one is found. */
  readonly holding: <A, E, R>(file: string, body: Effect.Effect<A, E, R>) => Effect.Effect<{ readonly done: A } | { readonly heldBy?: Holder }, E, R>
  /** Runs `body` while holding `file`, as `holding` does; where the hold was left by a run whose process has ended, it is left so after, so the next run still finds it (D232). */
  readonly keeping: <A, E, R>(file: string, body: Effect.Effect<A, E, R>) => Effect.Effect<{ readonly done: A } | { readonly heldBy?: Holder }, E, R>
  /** Of the files named, those a running process holds, with that process. */
  readonly held: (files: readonly string[]) => Effect.Effect<readonly { readonly file: string; readonly by: Holder }[]>
  /** Where the hold at `file` was left by a run whose process has ended, that run, with when it started (D223). */
  readonly left: (file: string) => Effect.Effect<Left | undefined>
  /** The live processes of the sessions on a ticket, known by their mark and from there by their parents and groups, and those the framework cannot place, where it is given when the cut-off run started (D222, D223); why not, where it cannot tell: the process table cannot be read. */
  readonly alive: (sought: Sought) => Effect.Effect<Alive | Cannot>
  /** Reads the table of processes once: none where it can be read; why not, where it cannot (REQ-FLOW-003 step 1, D249). */
  readonly table: () => Effect.Effect<Cannot | undefined>
  /** Ends every live process it knows to be of the sessions on a ticket: how many, and, where one is still alive or it finds one it cannot place, why, naming each (D213, D215, D223). */
  readonly end: (sought: Sought) => Effect.Effect<Ended>
}>()("stdo-builder/Hold") {}

export const holdLive: Layer.Layer<Hold, never, FileSystem.FileSystem | ChildProcessSpawner.ChildProcessSpawner> = Layer.effect(
  Hold,
  Effect.gen(function*() {
    const context = yield* Effect.context<FileSystem.FileSystem | ChildProcessSpawner.ChildProcessSpawner>()
    return Hold.of({
      holding: (file, body) => holding(file, body).pipe(Effect.provideContext(context)),
      keeping: (file, body) => keeping(file, body).pipe(Effect.provideContext(context)),
      held: (files) => held(files).pipe(Effect.provideContext(context)),
      left: (file) => left(file).pipe(Effect.provideContext(context)),
      alive: (sought) =>
        marked(sought).pipe(
          Effect.map((f): Alive => ({ alive: f.alive.map(named), unplaced: f.unplaced.map(named) })),
          Effect.catch((e) => Effect.succeed<Cannot>({ cannot: e.why, ...(e.table === undefined ? {} : { table: e.table }) })),
          Effect.provideContext(context)
        ),
      table: () =>
        tableRead().pipe(
          Effect.map((e): Cannot | undefined => (e === undefined ? undefined : { cannot: e.why, ...(e.table === undefined ? {} : { table: e.table }) })),
          Effect.provideContext(context)
        ),
      end: (sought) => endMarked(sought).pipe(Effect.provideContext(context))
    })
  })
)
