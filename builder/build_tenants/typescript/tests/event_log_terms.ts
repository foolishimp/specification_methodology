/**
 * The check of the event log (design, CALCULUS.md section 8): it reads the log
 * a workspace leaves and refuses one that the flow terms do not allow. It
 * reads the log in three parts. The entries that name no run form a word of
 * `{ set-up | answer }`. The entries of one run that are not a step's form a
 * word of `run`. The step entries of one run that name one vector form a word
 * of `{ step }`, and lie after that run's first `main taken in` and before its
 * `ticket merged` or its `run ended`.
 *
 * A term may be cut off after any effect (L11). So a run's entries may be the
 * start of a word, or that start followed by `run ended` where the run met a
 * fault; the last step of each vector in a run, and the last answer, may be
 * cut short. Where the log a run was adding to was gone, the new log begins
 * with that run's `new log started`, and the rest of its word lies there: the
 * check reads of such a run only that `new log started` is its first entry
 * there, and its only one (D247). Two runs that share an id are refused (D75). A line the check
 * cannot read as an entry is passed over: one that is not an object with
 * `at` and `event` as text, and `run` and `vector` as text where it has them.
 * The log service passes over a line it cannot read too; it reads by the full
 * shape of an entry, so it passes over a few lines more than the check does.
 *
 * Beside the grammar, `strays` refuses a session the term in force does not
 * denote: the sessions of a ticket are on the first vector for a ticket or on
 * the vectors its term names, and within a run in the term's order (CALCULUS.md
 * section 8; REQ-METHOD-006).
 *
 * @uses C14
 * @is REQ-FLOW-007 REQ-VERIFY-003 REQ-METHOD-006
 */
import { anything, names, read } from "../src/kit/lossless_encoding.js"

/** A term of a grammar: one event, a sequence, a choice, or `{ t }`, the term any number of times. */
type Term =
  | { readonly event: string }
  | { readonly seq: readonly Term[] }
  | { readonly alt: readonly Term[] }
  | { readonly many: Term }

/** The choice of nothing, which no word matches. */
const NONE: Term = { alt: [] }
const none = (t: Term): boolean => "alt" in t && t.alt.length === 0

type Part = Term | string
const term = (p: Part): Term => (typeof p === "string" ? { event: p } : p)

/** `a b`. */
function seq(...parts: readonly Part[]): Term {
  const terms = parts.map(term).flatMap((t) => ("seq" in t ? t.seq : [t]))
  if (terms.some(none)) return NONE
  return terms.length === 1 && terms[0] !== undefined ? terms[0] : { seq: terms }
}

/** `a | b`, each choice once. */
function either(...parts: readonly Part[]): Term {
  const terms = new Map(parts.map(term).flatMap((t) => ("alt" in t ? t.alt : [t])).map((t) => [JSON.stringify(t), t] as const))
  const kept = [...terms.values()]
  return kept.length === 1 && kept[0] !== undefined ? kept[0] : { alt: kept }
}

/** `[ a ]`. */
const maybe = (p: Part): Term => either(seq(), p)
/** `{ a }`. */
const any = (p: Part): Term => ({ many: term(p) })

const nullable = (t: Term): boolean =>
  "event" in t ? false : "seq" in t ? t.seq.every(nullable) : "alt" in t ? t.alt.some(nullable) : true

/** What may follow `event` in a word of `t`. */
function after(t: Term, event: string): Term {
  if ("event" in t) return t.event === event ? seq() : NONE
  if ("alt" in t) return either(...t.alt.map((a) => after(a, event)))
  if ("many" in t) return seq(after(t.many, event), t)
  const [head, ...rest] = t.seq
  if (head === undefined) return NONE
  return either(seq(after(head, event), ...rest), nullable(head) ? after(seq(...rest), event) : NONE)
}

/** Whether the events are the start of a word of `t`: a whole word, or one cut off. */
export const begins = (t: Term, events: readonly string[]): boolean => !none(events.reduce(after, t))
/** Whether the events are a whole word of `t`. */
export const isWord = (t: Term, events: readonly string[]): boolean => nullable(events.reduce(after, t))

// The grammar of section 8, as the page writes it.
const COMMIT = "commit made"

// set-up  = "set-up" [ "commit made" ] | "ticket written" | "release recorded"
const setUp = either(seq("set-up", maybe(COMMIT)), "ticket written", "release recorded")
// answer  = "answer written" { "answer written" } [ "commit made" ] [ "vector closed" ]
const answer = seq("answer written", any("answer written"), maybe(COMMIT), maybe("vector closed"))

// merge   = [ "commit made" ] "ticket merged"
const merge = seq(maybe(COMMIT), "ticket merged")
// last    = "commit made" | merge
const last = either(COMMIT, merge)
// take-in = [ "commit made" ] "main taken in"
const takeIn = seq(any(COMMIT), "main taken in")
// build   = [ "commit made" ] ( take-in { take-in } [ last ] | [ "commit made" ] )
const build = seq(maybe(COMMIT), either(seq(takeIn, any(takeIn), maybe(last)), maybe(COMMIT)))
// pull    = [ "commit made" ] "ticket pulled"
const pull = seq(maybe(COMMIT), "ticket pulled")
// run     = "run started" { "session processes ended" } [ "run cut off" ] [ "commit made" ] [ "user asked" ]
//           [ "commit made" ] [ "commit made" ] [ "commit made" ] [ "run cut off" ] [ pull ] [ build ] "run ended"
export const RUN = seq("run started", any("session processes ended"), maybe("run cut off"), maybe(COMMIT), maybe("user asked"), maybe(COMMIT), maybe(COMMIT), maybe(COMMIT), maybe("run cut off"), maybe(pull), maybe(build), "run ended")

// session = "session started" [ "session processes ended" ] ( "session returned" | "session failed" )
const session = seq("session started", maybe("session processes ended"), either("session returned", "session failed"))
// judged  = { "check run" } { "commit made" }
//           ( "vector closed" | "vector left open" | "user asked" )
const judged = seq(any("check run"), any(COMMIT), either("vector closed", "vector left open", "user asked"))
// step    = { session [ "verdict not written" | "verdict read" ] | "commit made" } [ judged ]
const step = seq(any(either(seq(session, maybe(either("verdict not written", "verdict read"))), COMMIT)), maybe(judged))

/** The three parts of the log, each as a word of its terms. */
export const NO_RUN = any(either(setUp, answer))
export const STEPS = any(step)

/** The events of a step, besides a commit that names a vector. */
const STEP_EVENTS = new Set(["session started", "session processes ended", "session returned", "session failed", "verdict not written", "verdict read", "check run", "vector closed", "vector left open", "user asked"])

/** One entry as the check reads it: what happened, and the run, vector, ticket and commit it names. */
export interface Read {
  readonly event: string
  readonly run?: string
  readonly vector?: string
  readonly ticket?: string
  readonly commit?: string
}

const isStep = (e: Read): boolean => (STEP_EVENTS.has(e.event) && ((e.event !== "session processes ended" && e.event !== "user asked") || e.vector !== undefined)) || (e.event === COMMIT && e.vector !== undefined)

/** The entries of a log, in its order. A line that is not an object (C14) with `at` and `event` as text, and `run` and `vector` as text where given, is passed over. */
export function entriesOf(log: string): readonly Read[] {
  return log.split("\n").flatMap((line) => {
    const got = read(names(anything), line)
    if (!("value" in got)) return []
    const { at, event, run, vector, ticket, commit } = got.value
    const named = (v: unknown) => v === undefined || typeof v === "string"
    if (typeof at !== "string" || typeof event !== "string" || !named(run) || !named(vector)) return []
    return [{
      event,
      ...(typeof run === "string" ? { run } : {}),
      ...(typeof vector === "string" ? { vector } : {}),
      ...(typeof ticket === "string" ? { ticket } : {}),
      ...(typeof commit === "string" ? { commit } : {})
    }]
  })
}

/** The entry that starts a new log where the one a run was adding to is gone (D247). */
const NEW_LOG = "new log started"

/** What the check refuses in a log, one line each. None where the flow terms allow it. */
export function refusals(log: string): readonly string[] {
  const entries = entriesOf(log).map((e, i) => ({ ...e, i }))
  const out: string[] = []

  const noRun = entries.filter((e) => e.run === undefined).map((e) => e.event)
  if (!begins(NO_RUN, noRun)) out.push(`the entries that name no run are not a word of { set-up | answer }: ${noRun.join(", ")}`)

  for (const id of new Set(entries.flatMap((e) => (e.run === undefined ? [] : [e.run])))) {
    const of = entries.filter((e) => e.run === id)
    const starts = of.filter((e) => e.event === "run started").length
    if (starts > 1) out.push(`${starts} runs share the id ${id}`)

    // The run's word began in a log that is gone: its entries here are the rest of it (D247).
    const anew = of.filter((e) => e.event === NEW_LOG).length
    if (anew > 1 || (anew === 1 && of[0]?.event !== NEW_LOG)) out.push(`the run ${id} has a new log started that is not the first of its entries, or more than one`)
    if (anew === 1) continue
    const own = of.filter((e) => !isStep(e)).map((e) => e.event)
    const cut = own.at(-1) === "run ended" ? own.slice(0, -1) : own
    if (!begins(RUN, cut)) out.push(`the entries of the run ${id} are not a word of run, nor the start of one: ${own.join(", ")}`)

    const from = of.find((e) => e.event === "main taken in")?.i
    const to = of.find((e) => e.event === "ticket merged" || e.event === "run ended")?.i ?? entries.length
    const steps = of.filter(isStep)
    for (const e of steps) {
      if (from === undefined || e.i < from || e.i > to) {
        out.push(`the entry ${e.i + 1}, ${e.event} of ${e.vector ?? "no vector"}, lies outside the run ${id} between its first main taken in and its ticket merged or run ended`)
      }
    }
    for (const v of new Set(steps.map((e) => e.vector))) {
      const word = steps.filter((e) => e.vector === v).map((e) => e.event)
      if (!begins(STEPS, word)) out.push(`the step entries of ${v ?? "no vector"} in the run ${id} are not a word of { step }: ${word.join(", ")}`)
    }
  }
  return out
}

/**
 * The term in force for a ticket in a commit: the first vector for a ticket,
 * and the vectors that take part, in order, each with the vectors of the inner
 * workflows it holds, which are stepped on within it: those of the ticket's
 * term, or of the default (REQ-ALG-006); none where it cannot be known.
 */
export type InForce = (ticket: string, commit: string) => { readonly first?: string; readonly simplest?: boolean; readonly order: readonly (readonly string[])[] } | undefined

/**
 * Where the sessions of a run are not those the term in force denotes, one
 * line each (REQ-METHOD-006). The term in force at a session is the one the
 * ticket holds in the commit of its step, the next commit of that vector in
 * the run; else in the last commit of the ticket before it. Each session is on
 * the first vector, but for the simplest ticket, or a vector the term names,
 * or an inner vector of one; and
 * within a run, the sessions under one term follow its order, a vector
 * repeated as often as its attempts need. A vector the term names may have
 * no session: its work may be done already. A session whose term cannot be
 * known is passed over.
 */
export function strays(log: string, inForce: InForce): readonly string[] {
  const entries = entriesOf(log)
  const out: string[] = []
  const at = new Map<string, { readonly term: ReturnType<InForce>; readonly index: number; readonly vector: string }>()
  entries.forEach((e, i) => {
    if (e.event !== "session started" || e.ticket === undefined || e.vector === undefined) return
    const later = entries.slice(i + 1).find((c) => c.event === COMMIT && c.run === e.run && c.vector === e.vector && c.commit !== undefined)
    const before = entries.slice(0, i).reverse().find((c) => c.event === COMMIT && c.ticket === e.ticket && c.commit !== undefined)
    const commit = later?.commit ?? before?.commit
    const term = commit === undefined ? undefined : inForce(e.ticket, commit)
    if (term === undefined) return
    // The simplest ticket is never inducted (REQ-METHOD-006): a session on the first vector for it strays.
    if (e.vector === term.first) {
      if (term.simplest === true) out.push(`the entry ${i + 1}: a session on ${e.vector} for ${e.ticket}, the simplest ticket, which is never inducted`)
      return
    }
    const index = term.order.findIndex((group) => group.includes(e.vector ?? ""))
    if (index < 0) {
      out.push(`the entry ${i + 1}: a session on ${e.vector} for ${e.ticket}, which its term does not name (${term.order.map((group) => group[0] ?? "").join(", ")})`)
      return
    }
    const key = `${e.run ?? ""} ${e.ticket}`
    const last = at.get(key)
    if (last !== undefined && JSON.stringify(last.term) === JSON.stringify(term) && index < last.index) {
      out.push(`the entry ${i + 1}: a session on ${e.vector} for ${e.ticket} after one on ${last.vector}, out of its term's order`)
    }
    at.set(key, { term, index, vector: e.vector })
  })
  return out
}
