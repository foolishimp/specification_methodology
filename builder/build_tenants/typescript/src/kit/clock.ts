/**
 * The clock: the present time, read in one place. A flow or a service reads
 * it by a plain call, and no pure module does. Its value enters only a bound,
 * a stamp of the event log, a run's id, a ticket's name, the simplest
 * ticket's `written` field and the time a reading of the folder is kept with,
 * which `show` gives; so it decides the order of tickets by name, and
 * reaches no content identity but that of the simplest ticket's text (L9 of
 * the calculus page). A session's seconds are a field of a stamped entry, and
 * the time it may still take is a bound.
 *
 * @carries C16
 */

/** The present time: in milliseconds since 1970, written in UTC, and by the parts of the local date and time. */
export interface Instant {
  readonly millis: number
  /** ISO 8601, in UTC. */
  readonly written: string
  readonly local: {
    readonly year: number
    /** 1 to 12. */
    readonly month: number
    readonly day: number
    readonly hours: number
    readonly minutes: number
    readonly seconds: number
  }
}

/** The present time, read once. */
export function now(): Instant {
  const at = new Date()
  return {
    millis: at.getTime(),
    written: at.toISOString(),
    local: { year: at.getFullYear(), month: at.getMonth() + 1, day: at.getDate(), hours: at.getHours(), minutes: at.getMinutes(), seconds: at.getSeconds() }
  }
}
