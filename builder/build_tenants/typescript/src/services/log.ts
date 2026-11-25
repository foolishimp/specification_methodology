/**
 * The event log service: the framework adds one entry at a time to the one
 * event log of the governed product (REQ-FLOW-001, "Add to the event log"), and
 * a person, through `stands`, reads it in one pass. It is carried out by the
 * append-only log (C10); each entry is written and read in its one written
 * form (C14). An entry it cannot read is passed over and left in place.
 *
 * For the one command it serves, it keeps which logs it has added to, so it
 * can say where one of them is gone when it is next added to, and how many
 * times it started one anew so (REQ-FLOW-003, REQ-FLOW-007, D247).
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
  /** How many files the user was asked on, as what changed while a session worked; never which (REQ-FLOW-007, D227). */
  readonly named?: number
  /** How many processes of a session the framework ended (REQ-FLOW-007, D214). */
  readonly processes?: number
  /** Main's name: for a ticket pulled, the branch it left; for a ticket merged, the branch it was merged into; for main taken in, main (REQ-FLOW-007, D239). */
  readonly main?: string
  /** For a ticket pulled, its own branch (REQ-FLOW-007, D239). */
  readonly branch?: string
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
  findings: optional(text),
  processes: optional(number),
  named: optional(number),
  main: optional(text),
  branch: optional(text)
})

/** The log could not be added to, and why. */
export class LogRefused {
  readonly _tag = "LogRefused"
  constructor(readonly why: string) {}
}

export class EventLog extends Context.Service<EventLog, {
  readonly append: (file: string, entry: Entry) => Effect.Effect<void, LogRefused>
  readonly exists: (file: string) => Effect.Effect<boolean>
  /** Whether the log at `file`, which this command added to before, is not there now; once it says so, the log is counted as started anew (D247). */
  readonly gone: (file: string) => Effect.Effect<boolean>
  /** How many times this command found the log at `file` gone and started it anew (D247). */
  readonly startedAnew: (file: string) => Effect.Effect<number>
  /** One pass over the entries it can read; undefined when there is no log. */
  readonly fold: <R>(file: string, start: R, step: (running: R, entry: Entry) => R) => Effect.Effect<R | undefined, LogRefused>
}>()("stdo-builder/EventLog") {}

export const eventLogLive: Layer.Layer<EventLog, never, FileSystem.FileSystem> = Layer.effect(
  EventLog,
  Effect.gen(function*() {
    const context = yield* Effect.context<FileSystem.FileSystem>()
    // The logs this command added to, and how many times it found each gone (D247).
    const added = new Set<string>()
    const anew = new Map<string, number>()
    return EventLog.of({
      append: (file, entry) =>
        append(file, writeLine(EntryShape, entry)).pipe(Effect.mapError((e) => new LogRefused(e.why)), Effect.provideContext(context), Effect.tap(() => Effect.sync(() => added.add(file)))),
      exists: (file) => exists(file).pipe(Effect.provideContext(context)),
      gone: (file) =>
        exists(file).pipe(
          Effect.provideContext(context),
          Effect.map((there) => added.has(file) && !there),
          Effect.tap((lost) => Effect.sync(() => (lost ? anew.set(file, (anew.get(file) ?? 0) + 1) : anew)))
        ),
      startedAnew: (file) => Effect.sync(() => anew.get(file) ?? 0),
      fold: (file, start, step) =>
        fold(file, start, (running, line) => {
          const got = read(EntryShape, line)
          return "value" in got ? step(running, got.value) : running
        }).pipe(Effect.mapError((e) => new LogRefused(e.why)), Effect.provideContext(context))
    })
  })
)
