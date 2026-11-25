/**
 * A ticket (REQ-FLOW-004): one file, the only record of the ticket, on the
 * board of three lanes. The user writes one with the product's command; the
 * framework writes only the simplest ticket, names a ticket, and moves a
 * ticket from lane to lane: to the active lane on main when it is pulled, with
 * the branch it leaves (`branch.ts`), and to the done lane on its own branch
 * before that branch is merged. Every move is made in the workspace's folder.
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
import { writtenPath } from "./changed.js"
import { Files } from "../services/files.js"
import { Git } from "../services/git.js"
import type { Flow } from "../services/services.js"
import { elsewhere, placedOf } from "./branch.js"
import { note } from "./events.js"
import { at, open, ticketPath, type Fault, type Opened } from "./workspace.js"

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

/** Writes a ticket in the backlog, in the folder, in the user's words. It is not committed: a run commits what the user left. */
export const writeTicket = (root: string, words: string): Flow<Written, Fault> => {
  const text = words.endsWith("\n") ? words : `${words}\n`
  return using(Files, (files) =>
    decide(nameFor(root, text, clock()), (name) =>
      decide(files.create(at(root, ticketPath("backlog", name)), text), (got): Flow<Written, Fault> =>
        got === "written"
          // The framework notes the identity of the ticket it wrote, so that a comparison of what changed while a session worked does not name it (REQ-ALG-008, D227).
          ? sequence(
            using(Git, (git) => decide(git.identityOfText(root, text), (id) => files.write(at(root, writtenPath(name)), `${id}\n`))),
            note(root, { event: "ticket written", ticket: name, path: ticketPath("backlog", name) }),
            end({ written: name })
          )
          : end({ there: name }))))
}

/** What the command `ticket` gives: why it is refused, or the ticket it wrote or found there. */
export type TicketWritten = Written | Exclude<Opened, { readonly root: string }> | { readonly refused: "no words" } | { readonly elsewhere: string }

/** The command `ticket` on the folder the library gives: `open`, words given, the folder on the active ticket's branch where one is active (REQ-FLOW-001, D239), and the ticket file created. */
export const ticket = (folder: string, words: string): Flow<TicketWritten, Fault> =>
  decide(open(folder), (opened): Flow<TicketWritten, Fault> =>
    "refused" in opened ? end(opened) : words.trim() === "" ? end({ refused: "no words" }) : decide(placedOf(opened.root, opened.on), (placed): Flow<TicketWritten, Fault> => {
      const off = elsewhere(placed)
      return off !== undefined ? end({ elsewhere: off }) : writeTicket(opened.root, words)
    }))

/** The simplest ticket: build the workspace to the specification as it stands. Written in the backlog, in the folder, on main. */
export const writeSimplest = (root: string): Flow<string, Fault> =>
  using(Files, (files) => {
    const now = clock()
    const text = `Build the workspace to the specification as it stands.\n\n${writeFields([["simplest", "yes"], ["written", now.written]])}`
    return decide(nameFor(root, text, now), (name) => sequence(files.create(at(root, ticketPath("backlog", name)), text), end(name)))
  })
