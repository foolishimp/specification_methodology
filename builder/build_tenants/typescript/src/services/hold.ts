/**
 * The hold service: while a run works on a ticket no second run takes that
 * ticket (REQ-FLOW-001, "Hold"). It is carried out by the exclusive hold bound
 * to a process (C11): a killed run leaves nothing that refuses the next.
 *
 * @uses C11
 * @is REQ-FLOW-001 REQ-FLOW-003
 */
import * as Context from "effect/Context"
import * as Effect from "effect/Effect"
import type * as FileSystem from "effect/FileSystem"
import * as Layer from "effect/Layer"
import { held, holding, left } from "../kit/exclusive_hold.js"

export class Hold extends Context.Service<Hold, {
  /** Runs `body` while holding `file`; "held" when another run holds it. */
  readonly holding: <A, E, R>(file: string, body: Effect.Effect<A, E, R>) => Effect.Effect<{ readonly done: A } | "held", E, R>
  /** Of the files named, those a running process holds. */
  readonly held: (files: readonly string[]) => Effect.Effect<readonly string[]>
  /** Whether the hold at `file` was left by a run whose process has ended. */
  readonly left: (file: string) => Effect.Effect<boolean>
}>()("stdo-builder/Hold") {}

export const holdLive: Layer.Layer<Hold, never, FileSystem.FileSystem> = Layer.effect(
  Hold,
  Effect.gen(function*() {
    const context = yield* Effect.context<FileSystem.FileSystem>()
    return Hold.of({
      holding: (file, body) => holding(file, body).pipe(Effect.provideContext(context)),
      held: (files) => held(files).pipe(Effect.provideContext(context)),
      left: (file) => left(file).pipe(Effect.provideContext(context))
    })
  })
)
