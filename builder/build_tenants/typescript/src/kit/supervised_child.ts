/**
 * Supervised child with a deadline: start a process, wait for its return or
 * for the deadline, and end it at the deadline. Each start has exactly one
 * outcome: it returned (with its exit code and what it printed), it could not
 * start, it stopped without returning, or it ran over; the last two with what
 * it printed until then. This is the one module
 * that starts a process; it wraps Effect's process module.
 *
 * @carries C12
 */
import * as Effect from "effect/Effect"
import * as ChildProcess from "effect/process/ChildProcess"
import * as ChildProcessSpawner from "effect/process/ChildProcessSpawner"
import * as Stream from "effect/Stream"

export interface Child {
  readonly command: string
  readonly args: readonly string[]
  /** The folder the child starts in. */
  readonly cwd: string
  /** How long it may run, in milliseconds. */
  readonly deadline: number
  /** Text, or bytes, given on its standard input. Without it the child's input is closed. */
  readonly input?: string | Uint8Array
  /** Added to the environment it inherits; a name set to undefined is taken out. */
  readonly env?: Readonly<Record<string, string | undefined>>
  /** Its output and its errors as one text, in the order printed. Otherwise the output alone, and the errors apart. */
  readonly merged?: boolean
}

/** What the child printed before it was ended, where it printed anything: its output, then its errors where they are apart. */
export interface Printed {
  readonly printed?: string
}

export type Outcome =
  | { readonly outcome: "returned"; readonly code: number; readonly output: string; readonly errors: string }
  | { readonly outcome: "could not start"; readonly why: string }
  | ({ readonly outcome: "stopped without returning"; readonly why: string } & Printed)
  | ({ readonly outcome: "ran over" } & Printed)

type Spawner = ChildProcessSpawner.ChildProcessSpawner

const encoder = new TextEncoder()

/**
 * Starts the child and waits for its one outcome. It never fails: every way it
 * can end is an outcome. What the child prints is read as it comes, into texts
 * kept outside the part the deadline cuts off, so a child that stops without
 * returning, or is ended at its deadline, still gives what it printed until then.
 */
export const supervise = (child: Child): Effect.Effect<Outcome, never, Spawner> =>
  Effect.gen(function*() {
    const read = { output: "", errors: "" }
    const printed = (): Printed => {
      const text = `${read.output}${read.errors}`
      return text === "" ? {} : { printed: text }
    }
    const stopped = (error: { readonly message: string }): Outcome => ({ outcome: "stopped without returning", why: error.message, ...printed() })
    const spawner = yield* ChildProcessSpawner.ChildProcessSpawner
    const command = ChildProcess.make(child.command, [...child.args], {
      cwd: child.cwd,
      env: { ...child.env },
      extendEnv: true,
      stdin: child.input === undefined ? "ignore" : { stream: Stream.make(typeof child.input === "string" ? encoder.encode(child.input) : child.input) },
      forceKillAfter: 2000
    })
    const body = Effect.gen(function*() {
      // A program that cannot be found can reach here as a defect of the platform rather than a failure.
      const handle = yield* spawner.spawn(command).pipe(
        Effect.mapError((error): Outcome => ({ outcome: "could not start", why: error.message })),
        Effect.catchDefect((defect) => Effect.fail<Outcome>({ outcome: "could not start", why: String(defect) }))
      )
      const into = (s: typeof handle.all, kept: "output" | "errors") =>
        Stream.runForEach(Stream.decodeText(s), (text) => Effect.sync(() => void (read[kept] += text))).pipe(Effect.mapError(stopped))
      yield* into(child.merged === true ? handle.all : handle.stdout, "output")
      if (child.merged !== true) yield* into(handle.stderr, "errors")
      const code = yield* handle.exitCode.pipe(Effect.mapError(stopped))
      return { outcome: "returned", code: Number(code), output: read.output, errors: read.errors } satisfies Outcome as Outcome
    })
    return yield* body.pipe(
      Effect.scoped,
      Effect.timeoutOrElse({ duration: child.deadline, orElse: () => Effect.sync((): Outcome => ({ outcome: "ran over", ...printed() })) }),
      Effect.catch((outcome: Outcome) => Effect.succeed(outcome))
    )
  })
