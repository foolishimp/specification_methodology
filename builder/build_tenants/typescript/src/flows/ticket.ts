/**
 * A ticket (REQ-FLOW-004): one file, the only record of the ticket, on the
 * board of three lanes. The user writes one with the product's command; the
 * framework writes only the simplest ticket, names a ticket, and moves a
 * ticket from lane to lane: to the active lane on main when it is pulled, and
 * to the done lane on its own branch before that branch is merged.
 *
 * A ticket's name is the date it was written, four characters of the content
 * identity of its text (C1) and its first words, so names need no shared
 * counter and sort by when the ticket was written.
 *
 * The command `ticket` is `open`, then a decision on whether words are given,
 * then the ticket file created (design, CALCULUS.md section 5).
 *
 * @uses C1 C15 C14 C16 C17 H5
 * @is REQ-FLOW-004 REQ-FLOW-007
 */
import { decide, end, sequence, using } from "../kit/calculus.js"
import { now as clock, type Instant } from "../kit/clock.js"
import { writeFields } from "../kit/field_lines.js"
import { Files } from "../services/files.js"
import { Git } from "../services/git.js"
import type { Flow } from "../services/services.js"
import { committed } from "./commit.js"
import { note } from "./events.js"
import { at, lineOf, open, ticketPath, type Fault, type Lane, type Opened, type Workspace } from "./workspace.js"

const two = (n: number): string => String(n).padStart(2, "0")

/** The name a ticket of this text, written now, is given. */
export const nameFor = (root: string, text: string, now: Instant): Flow<string, Fault> =>
  using(Git, (git) =>
    decide(git.identityOfText(root, text), (identity) => {
      // The date and the time to the second come first, so names sort by when the ticket was written.
      const date = `${two(now.local.year % 100)}${two(now.local.month)}${two(now.local.day)}`
      const time = `${two(now.local.hours)}${two(now.local.minutes)}${two(now.local.seconds)}`
      const words = text.toLowerCase().split(/[^a-z0-9]+/).filter((w) => w !== "").slice(0, 4).join("-")
      return end(`${date}-${time}-${identity.slice(0, 4)}${words === "" ? "" : `-${words}`}`)
    }))

export type Written = { readonly written: string } | { readonly there: string }

/** Writes a ticket in the backlog on main, in the user's words. It is not committed: a run commits what the user left. */
export const writeTicket = (root: string, words: string): Flow<Written, Fault> => {
  const text = words.endsWith("\n") ? words : `${words}\n`
  return using(Files, (files) =>
    decide(nameFor(root, text, clock()), (name) =>
      decide(files.create(at(root, ticketPath("backlog", name)), text), (got): Flow<Written, Fault> =>
        got === "written"
          ? sequence(note(root, { event: "ticket written", ticket: name, path: ticketPath("backlog", name) }), end({ written: name }))
          : end({ there: name }))))
}

/** What the command `ticket` gives: why it is refused, or the ticket it wrote or found there. */
export type TicketWritten = Written | Exclude<Opened, { readonly root: string }> | { readonly refused: "no words" }

/** The command `ticket` on the folder the library gives: `open`, words given, and the ticket file created. */
export const ticket = (folder: string, words: string): Flow<TicketWritten, Fault> =>
  decide(open(folder), (opened): Flow<TicketWritten, Fault> =>
    "refused" in opened ? end(opened) : words.trim() === "" ? end({ refused: "no words" }) : writeTicket(opened.root, words))

/** The simplest ticket: build the workspace to the specification as it stands. Written in the backlog on main. */
export const writeSimplest = (root: string): Flow<string, Fault> =>
  using(Files, (files) => {
    const now = clock()
    const text = `Build the workspace to the specification as it stands.\n\n${writeFields([["simplest", "yes"], ["written", now.written]])}`
    return decide(nameFor(root, text, now), (name) => sequence(files.create(at(root, ticketPath("backlog", name)), text), end(name)))
  })

/** Moves a ticket from one lane to another in a checkout, and commits that move and nothing else: on main in main's own folder, on the ticket's branch in its checkout. The run's id names the entry of the commit. */
export const move = (ws: Workspace, folder: string, ticket: string, from: Lane, to: Lane, run: string): Flow<void, Fault> =>
  using(Files, (files) => {
    const line = folder === ws.root ? ws.main : lineOf(ticket)
    return sequence(
      files.move(at(folder, ticketPath(from, ticket)), at(folder, ticketPath(to, ticket))),
      decide(committed({ folder, line }, `board: ${ticket} to ${to}`, [ticketPath(from, ticket), ticketPath(to, ticket)]), (commit) =>
        commit === undefined ? end(undefined) : note(ws.root, { event: "commit made", run, ticket, commit, why: `${ticket} moved to ${to}` }))
    )
  })
