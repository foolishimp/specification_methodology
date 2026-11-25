/**
 * The combinators of the calculus (design, CALCULUS.md section 2): K5 to K8,
 * a sequence, a decision on what was read, a repeat under C9 and a hold
 * through the hold service, with the two terms that do nothing. It is the one
 * place a flow reaches Effect. A flow built from these and the services alone
 * is one term of the calculus page.
 *
 * @carries C17
 */
import * as Effect from "effect/Effect"
import { goesOn } from "./bounded_loop.js"

/** A term: an effect with its value, its fault and the services it needs. */
type Term<A, E, R> = Effect.Effect<A, E, R>
// A term of any type, for the typing of a sequence alone.
type AnyTerm = Effect.Effect<any, any, any>
type Last<T extends readonly AnyTerm[]> = T extends readonly [...AnyTerm[], infer L] ? L : never

/** The term that does nothing and gives `value`. */
export const end = <A>(value: A): Term<A, never, never> => Effect.succeed(value)

/** The term that does nothing and fails with `f`. */
export const fault = <E>(f: E): Term<never, E, never> => Effect.fail(f)

/** K5: the terms written, each after the one before; the value of the last. */
export const sequence = <const T extends readonly [AnyTerm, ...AnyTerm[]]>(
  ...terms: T
): Term<Effect.Success<Last<T>>, Effect.Error<T[number]>, Effect.Services<T[number]>> =>
  terms.reduce((done: AnyTerm, next: AnyTerm) => Effect.flatMap(done, () => next))

/** K5 over a finite list, in its order: the values of the terms, in that order. */
export const each = <A, B, E, R>(values: Iterable<A>, term: (value: A, index: number) => Term<B, E, R>): Term<readonly B[], E, R> =>
  Effect.forEach(values, term)

/** K6: does `read`, then the term the pure function `then` selects from what it gave. */
export const decide = <A, E, R, B, E2, R2>(read: Term<A, E, R>, then: (value: A) => Term<B, E2, R2>): Term<B, E | E2, R | R2> =>
  Effect.flatMap(read, then)

/** What a term gave: its value, or the fault it failed with. */
export type Outcome<A, E> = { readonly value: A } | { readonly fault: E }

/** The read of K6 that gives `term`'s value or its fault. */
export const outcome = <A, E, R>(term: Term<A, E, R>): Term<Outcome<A, E>, never, R> =>
  Effect.match(term, { onFailure: (f: E): Outcome<A, E> => ({ fault: f }), onSuccess: (value: A): Outcome<A, E> => ({ value }) })

/** The term over one of the services, given by its key, which is the term that gives the service: it reads nothing and decides nothing. */
export const using = <I, S, B, E, R>(service: Term<S, never, I>, term: (s: S) => Term<B, E, R>): Term<B, E, I | R> =>
  Effect.flatMap(service, term)

/** What one round of a `repeat` gives: the state for the next round, or the value it leaves with. */
export type Round<S, A> = { readonly again: S } | { readonly leave: A }

/**
 * How a `repeat` is bounded: at most `rounds` rounds (C9's bound), none where
 * it is left out, and not again where `reached` says so of the state for the
 * next round. Where the bound or the measure ends it, it leaves with what
 * `leave` gives of that state.
 */
export interface Bound<S, A> {
  readonly rounds?: number
  readonly reached?: (state: S) => boolean
  readonly leave: (state: S) => A
}

/**
 * K7: does `body` on `state`, and again on each state it gives for the next
 * round, while the bound is not reached and, where a measure is given, the
 * measure strictly falls (C9). The state is the only value carried from one
 * round to the next.
 */
export const repeat = <S, A, E, R>(state: S, body: (state: S) => Term<Round<S, A>, E, R>, bound: Bound<S, A>, measure?: (state: S) => number): Term<A, E, R> => {
  const round = (s: S, made: number, before: number | undefined): Term<A, E, R> =>
    Effect.flatMap(body(s), (r): Term<A, E, R> => {
      if ("leave" in r) return Effect.succeed(r.leave)
      const now = measure === undefined ? 0 : measure(r.again)
      const goes = goesOn(measure === undefined ? undefined : before, now, made + 1, bound.rounds ?? Number.POSITIVE_INFINITY) && bound.reached?.(r.again) !== true
      return goes ? round(r.again, made + 1, now) : Effect.succeed(bound.leave(r.again))
    })
  return round(state, 0, measure === undefined ? undefined : measure(state))
}

/** The hold service as C17 knows it, by its shape: a thing that does a term while holding a name, or says another holds it. */
export interface Holds {
  readonly holding: <A, E, R>(name: string, term: Term<A, E, R>) => Term<{ readonly done: A } | { readonly heldBy?: { readonly pid: number; readonly start?: string } }, E, R>
}

/** K8: does `term` while holding `name`; where another process holds it, that process, where one is found. */
export const held = <A, E, R>(hold: Holds, name: string, term: Term<A, E, R>): Term<{ readonly done: A } | { readonly heldBy?: { readonly pid: number; readonly start?: string } }, E, R> =>
  hold.holding(name, term)
