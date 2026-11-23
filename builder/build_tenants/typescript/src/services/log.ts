/**
 * The event log service: the framework adds one entry at a time to the one
 * event log of the governed product (REQ-FLOW-001, "Add to the event log"), and
 * a person, through `stands`, reads it in one pass. It is carried out by the
 * append-only log (C10); each entry is written and read in its one written
 * form (C14). An entry it cannot read is passed over and left in place.
 *
 * @uses C10 C14
 * @is REQ-FLOW-007
 */
import * as Context from "effect/Context"
import * as Effect from "effect/Effect"
import type * as FileSystem from "effect/FileSystem"
import * as Layer from "effect/Layer"
import { append, exists, fold } from "../kit/append_only_log.js"
import { list, number, optional, read, record, text, writeLine } from "../kit/lossless_encoding.js"

/** One entry: what happened, when, and the names, paths and identities it concerns. It holds no content of an asset. */
export interface Entry {
  readonly at: string
  readonly event: string
  readonly run?: string
  readonly ticket?: string
  readonly vector?: string
  readonly kind?: string
  readonly agent?: string
  readonly check?: string
  readonly result?: string
  readonly seconds?: number
  readonly cost?: string
  /** The cost's unit, as the settings name it (D102). */
  readonly unit?: string
  readonly calls?: number
  readonly ending?: string
  readonly why?: string
  readonly path?: string
  readonly commit?: string
  readonly files?: readonly string[]
  /** The release of this product in force, as the settings record it (REQ-FLOW-007, D205). */
  readonly release?: string
  /** The agent's command as it was run. */
  readonly command?: readonly string[]
  /** Where what a session printed is kept. */
  readonly printed?: string
  /** Where a verdict's findings are. */
  readonly findings?: string
}

const EntryShape = record({
  at: text,
  event: text,
  run: optional(text),
  ticket: optional(text),
  vector: optional(text),
  kind: optional(text),
  agent: optional(text),
  check: optional(text),
  result: optional(text),
  seconds: optional(number),
  cost: optional(text),
  unit: optional(text),
  calls: optional(number),
  ending: optional(text),
  why: optional(text),
  path: optional(text),
  commit: optional(text),
  files: optional(list(text)),
  release: optional(text),
  command: optional(list(text)),
  printed: optional(text),
  findings: optional(text)
})

/** The log could not be added to, and why. */
export class LogRefused {
  readonly _tag = "LogRefused"
  constructor(readonly why: string) {}
}

export class EventLog extends Context.Service<EventLog, {
  readonly append: (file: string, entry: Entry) => Effect.Effect<void, LogRefused>
  readonly exists: (file: string) => Effect.Effect<boolean>
  /** One pass over the entries it can read; undefined when there is no log. */
  readonly fold: <R>(file: string, start: R, step: (running: R, entry: Entry) => R) => Effect.Effect<R | undefined, LogRefused>
}>()("stdo-builder/EventLog") {}

export const eventLogLive: Layer.Layer<EventLog, never, FileSystem.FileSystem> = Layer.effect(
  EventLog,
  Effect.gen(function*() {
    const context = yield* Effect.context<FileSystem.FileSystem>()
    return EventLog.of({
      append: (file, entry) =>
        append(file, writeLine(EntryShape, entry)).pipe(Effect.mapError((e) => new LogRefused(e.why)), Effect.provideContext(context)),
      exists: (file) => exists(file).pipe(Effect.provideContext(context)),
      fold: (file, start, step) =>
        fold(file, start, (running, line) => {
          const got = read(EntryShape, line)
          return "value" in got ? step(running, got.value) : running
        }).pipe(Effect.mapError((e) => new LogRefused(e.why)), Effect.provideContext(context))
    })
  })
)
