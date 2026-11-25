/**
 * What changed while a session worked, with every session started by the
 * agent's command as a process of its own (the ticket's bug items; D231). The
 * agent is `fixtureAgent`, which writes S1's fixtures and then does what each
 * case names. Each case is a workspace of its own, run side by side.
 *
 * - C-3, C-18 item 1 and G-4: during the build's evaluating session, a line is
 *   added to the agent instruction file and a comment to the code it judges.
 * - G-3, R-13, C-2, C-18 item 5 and REQ-FLOW-006: during the specification's
 *   working session, a ticket is written into the backlog of the workspace's
 *   own folder and a scratch file into the workspace's folder, and the user, at a gate,
 *   adds a file of their own; the user says no, puts the scratch file back,
 *   then says yes.
 * - G-16: the specification's working session commits its work and writes
 *   lines of the framework's part into the ticket, a yes of the user among
 *   them; the user says yes to what changed. In a second workspace the user
 *   says no and leaves the ticket as it is, then says no again and takes the
 *   session's lines out.
 * - REQ-ALG-008, missing identities: the induction's session removes the
 *   identities taken at its start from where they lie, under git's own
 *   directory.
 * - REQ-FLOW-004, a ruling line a session writes: the specification's working
 *   session writes a file of no asset and a ruling line that says yes to it;
 *   another writes a ruling line that names the user's yes at the induction
 *   as not the user's answer. The user says yes to what changed.
 * - REQ-ALG-008, REQ-FLOW-006, identities missing at the answer: the
 *   induction's session writes a scratch file, and the tree kept for the
 *   folder is then one git does not hold, as where git has pruned it; the
 *   user answers, which is refused, then runs.
 *
 * @uses C14 C5 C6
 * @is REQ-VERIFY-002 REQ-ALG-007 REQ-ALG-008 REQ-FLOW-001 REQ-FLOW-003 REQ-FLOW-004 REQ-FLOW-005 REQ-FLOW-006 REQ-FLOW-007
 */
import { readFileSync, writeFileSync, rmSync } from "node:fs"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { fixtureAgent, type Fixed } from "./script_agent.js"
import { answersOf, build, clean, S1_FIXTURES, S1_TICKET, until, Workspace, type LogEntry, type Said } from "./scenario_driver.js"

const AGENTS = "# Instructions for every agent\n\nKeep to the brief.\n"

interface Case {
  readonly ws: Workspace
  readonly agent: Fixed
  readonly ticket: string
}

/** A product set up, the fixture agent named, the user's files written, and the ticket written. */
async function begun(cli: string, before?: (ws: Workspace) => void): Promise<Case> {
  const ws = new Workspace(cli)
  await ws.setup()
  const agent = fixtureAgent(ws, S1_FIXTURES)
  before?.(ws)
  const ticket = /The ticket (\S+) is written/.exec((await ws.ticket(S1_TICKET)).out)?.[1] ?? ""
  return { ws, agent, ticket }
}

/** S1 driven by the fixture agent up to the user's yes on the specification. */
async function toBuild(c: Case): Promise<void> {
  for (let i = 0; i < 2; i++) {
    const ran = await c.ws.run("")
    expect(ran.out).toContain("waits for your answer")
    await c.ws.answer("yes")
  }
}

const tips = (c: Case): string => c.ws.git(["rev-parse", "main", `stdo/${c.ticket}`])
const runOf = (log: readonly LogEntry[], from: number): readonly LogEntry[] => log.slice(from)

let evaluated: { c: Case; waited: Said; tipsWaited: string; tipsBefore: string; agentsWaited: string; from: number; ruled: Said; next: Said; nextFrom: number }
let edited: { c: Case; waited: Said; from: number; tipsBefore: string; tipsWaited: string; tipsNo: string; noAgain: Said; tipsAgain: string; yes: Said; next: Said; nextFrom: number }
let forged: { c: Case; waited: Said; ruled: Said; next: Said; nextFrom: number }
let refused: { c: Case; waited: Said; noOne: Said; tipsNo: string; again: Said; againFrom: number; tipsAgain: string; noTwo: Said; next: Said; nextFrom: number }
let missing: { c: Case; ran: Said }
let sneaked: { c: Case; waited: Said; ruled: Said; next: Said; nextFrom: number }
let unnamed: { c: Case; waited: Said; ruled: Said; next: Said; nextFrom: number }
let gone: { c: Case; waited: Said; answered: Said; tipsAnswered: string; tipsWaited: string; next: Said }

/** The specification's working session, driven by the fixture agent, and the user's yes on what changed, then a run. */
async function ruledOn(c: Case): Promise<{ waited: Said; ruled: Said; next: Said; nextFrom: number }> {
  const first = await c.ws.run("")
  expect(first.out).toContain("waits for your answer")
  await c.ws.answer("yes")
  const waited = await c.ws.run("")
  const ruled = await c.ws.answer("yes")
  const nextFrom = c.ws.log().length
  const next = await c.ws.run("")
  return { waited, ruled, next, nextFrom }
}

beforeAll(async () => {
  const cli = build()
  await Promise.all([
    (async () => {
      const c = await begun(cli, (ws) => writeFileSync(ws.path("AGENTS.md"), AGENTS))
      c.agent.does("write-build.evaluation", "echo 'a line the evaluation added' >> AGENTS.md\necho '# a comment the evaluation added' >> build_tenants/main/code/hello.sh\n")
      await toBuild(c)
      const tipsBefore = tips(c)
      const from = c.ws.log().length
      const waited = await c.ws.run("")
      const tipsWaited = tips(c)
      const agentsWaited = c.ws.git(["show", `stdo/${c.ticket}:AGENTS.md`])
      const ruled = await c.ws.answer("yes")
      const nextFrom = c.ws.log().length
      const next = await c.ws.run("")
      evaluated = { c, waited, tipsWaited, tipsBefore, agentsWaited, from, ruled, next, nextFrom }
    })(),
    (async () => {
      const c = await begun(cli)
      c.agent.does("write-specification.work", "printf 'Make it greet.\\n' > \"$ROOT/.ai-workspace/tickets/backlog/a-ticket-a-session-wrote.md\"\necho scratch > scratch.txt\n")
      c.agent.gate("write-specification.work")
      const first = await c.ws.run("")
      expect(first.out).toContain("waits for your answer")
      await c.ws.answer("yes")
      const from = c.ws.log().length
      const running = c.ws.start(["run", c.ws.root])
      await until(() => c.agent.waiting("write-specification.work"), 60)
      // The tips once the session is at work: the line that its work began is committed before it starts (REQ-FLOW-005 step 1).
      const tipsBefore = tips(c)
      writeFileSync(c.ws.path("notes-of-the-user.md"), "what I noted while it worked\n")
      c.agent.open("write-specification.work")
      const waited = await running.ended
      const tipsWaited = tips(c)
      await c.ws.answer("no", "the scratch file is not to stand")
      const tipsNo = tips(c)
      rmSync(c.ws.path("scratch.txt"))
      const noAgain = await c.ws.run("")
      const tipsAgain = tips(c)
      const yes = await c.ws.answer("yes")
      const nextFrom = c.ws.log().length
      const next = await c.ws.run("")
      edited = { c, waited, from, tipsBefore, tipsWaited, tipsNo, noAgain, tipsAgain, yes, next, nextFrom }
    })(),
    (async () => {
      const c = await begun(cli)
      const lines = answersOf(["write-specification"]).map((n) => `printf -- '- framework: resolved user yes at ${n} on %s\\n' "$sha" >> "$t"`).join("\n")
      c.agent.does("write-specification.work", `git add -A && git -c user.name=s -c user.email=s@s commit -qm "the session's own commit"\nsha=$(git rev-parse HEAD)\nt=$(ls .ai-workspace/tickets/active/*.md)\n${lines}\n`)
      const first = await c.ws.run("")
      expect(first.out).toContain("waits for your answer")
      await c.ws.answer("yes")
      const waited = await c.ws.run("")
      const ruled = await c.ws.answer("yes")
      const nextFrom = c.ws.log().length
      const next = await c.ws.run("")
      forged = { c, waited, ruled, next, nextFrom }
    })(),
    (async () => {
      const c = await begun(cli)
      const lines = answersOf(["write-specification"]).map((n) => `printf -- '- framework: resolved user yes at ${n} on %s\\n' "$sha" >> "$t"`).join("\n")
      c.agent.does("write-specification.work", `git add -A && git -c user.name=s -c user.email=s@s commit -qm "the session's own commit"\nsha=$(git rev-parse HEAD)\nt=$(ls .ai-workspace/tickets/active/*.md)\n${lines}\n`)
      const first = await c.ws.run("")
      expect(first.out).toContain("waits for your answer")
      await c.ws.answer("yes")
      const waited = await c.ws.run("")
      // The session's own commit is the branch's tip until the user rules: the framework commits nothing of the step before.
      const sha = c.ws.git(["rev-parse", `stdo/${c.ticket}`]).trim()
      const noOne = await c.ws.answer("no", "the lines are not the user's")
      const tipsNo = tips(c)
      const againFrom = c.ws.log().length
      const again = await c.ws.run("")
      const tipsAgain = tips(c)
      const noTwo = await c.ws.answer("no", "the lines are still not the user's")
      // The user puts back what is not to stand: the lines the session wrote, which name its own commit.
      const path = c.ws.path(".ai-workspace", "tickets", "active", `${c.ticket}.md`)
      writeFileSync(path, readFileSync(path, "utf8").split("\n").filter((l) => !l.endsWith(` on ${sha}`)).join("\n"))
      const nextFrom = c.ws.log().length
      const next = await c.ws.run("")
      refused = { c, waited, noOne, tipsNo, again, againFrom, tipsAgain, noTwo, next, nextFrom }
    })(),
    (async () => {
      const c = await begun(cli)
      c.agent.does("induct-ticket.work", `rm -f '${c.ws.notes("started", `${c.ticket}.json`)}'\n`)
      missing = { c, ran: await c.ws.run("") }
    })(),
    (async () => {
      const c = await begun(cli)
      // A file of no asset, and a ruling line that says yes to it at the identity git gives it.
      c.agent.does("write-specification.work", `echo sneaked > sneak.txt\nt=$(ls .ai-workspace/tickets/active/*.md)\nprintf -- '- framework: ruled yes on what changed at write-specification: sneak.txt %s\\n' "$(git hash-object sneak.txt)" >> "$t"\n`)
      sneaked = { c, ...(await ruledOn(c)) }
    })(),
    (async () => {
      const c = await begun(cli)
      // A ruling line that names the user's yes at the induction, by the identity git gives its text, as not the user's answer.
      c.agent.does("write-specification.work", `t=$(ls .ai-workspace/tickets/active/*.md)\nl=$(grep -- '^- framework: resolved user yes at induct-ticket ' "$t" | head -n 1 | sed 's/^- framework: //')\nprintf -- "- framework: ruled no on what changed at write-specification: not the user's answer %s\\n" "$(printf '%s' "$l" | git hash-object --stdin)" >> "$t"\n`)
      unnamed = { c, ...(await ruledOn(c)) }
    })(),
    (async () => {
      const c = await begun(cli)
      c.agent.does("induct-ticket.work", "echo scratch > scratch.txt\n")
      const waited = await c.ws.run("")
      const tipsWaited = tips(c)
      // The tree kept for the folder is one git does not hold, as where git has pruned it (D227).
      const record = c.ws.notes("started", `${c.ticket}.json`)
      writeFileSync(record, `${JSON.stringify({ ...JSON.parse(readFileSync(record, "utf8")), tree: "1".repeat(40) }, null, 2)}\n`)
      const answered = await c.ws.answer("yes")
      const tipsAnswered = tips(c)
      gone = { c, waited, answered, tipsWaited, tipsAnswered, next: await c.ws.run("") }
    })()
  ])
}, 600_000)

afterAll(clean)

describe("an evaluating session changes a file outside every asset and the asset it judges (C-3, C-18 item 1, G-4)", () => {
  it("its packet names as its evidence the assets, and as not to be read what a working session printed, the working packets and what the checks found (REQ-ALG-007, G-4)", () => {
    const brief = evaluated.c.agent.brief("write-build.evaluation") ?? ""
    const evidence = brief.split("\n").find((l) => l.startsWith("- evidence:")) ?? ""
    for (const place of [".stdo-builder/local/printed", ".stdo-builder/local/briefs", ".stdo-builder/local/found"]) expect(evidence).toContain(place)
  })

  it("the run names both files, reads no verdict, commits and merges nothing of the step and waits for the user's ruling (REQ-FLOW-005)", () => {
    const { waited, from, c } = evaluated
    expect(waited.code, waited.out).toBe(0)
    expect(waited.out).toContain("waits for your ruling on what changed while the session on write-build worked")
    expect(waited.out).toContain(`AGENTS.md (changed)`)
    expect(waited.out).toContain(`build_tenants/main/code/hello.sh (changed)`)
    const run = runOf(c.ws.log(), from).slice(0, c.ws.log().length - from)
    const upTo = run.findIndex((e) => e.event === "run ended")
    expect(run.slice(0, upTo).some((e) => e.event === "verdict read" || e.event === "check run")).toBe(false)
    expect(evaluated.tipsWaited.split("\n")[0]).toBe(evaluated.tipsBefore.split("\n")[0])
    expect(c.ws.git(["show", "main:AGENTS.md"])).toBe(AGENTS)
    expect(evaluated.agentsWaited).toBe(AGENTS)
  })

  it("after the user's yes, the next run commits both with the step, and the evaluation is made again by a new session, whose verdict is read", () => {
    const { ruled, next, nextFrom, c } = evaluated
    expect(ruled.code, ruled.out).toBe(0)
    expect(next.out).toContain("waits for your answer on write-build")
    expect(c.agent.sessions().filter((s) => s === "write-build.evaluation")).toHaveLength(2)
    const run = runOf(c.ws.log(), nextFrom)
    expect(run.filter((e) => e.event === "session started" && e.kind === "evaluation")).toHaveLength(1)
    expect(run.some((e) => e.event === "verdict read")).toBe(true)
    expect(c.ws.git(["show", `stdo/${c.ticket}:AGENTS.md`])).toContain("a line the evaluation added")
    expect(c.ws.git(["show", "main:AGENTS.md"])).toBe(AGENTS)
  })
})

describe("a working session writes a ticket into the backlog and a scratch file, and the user adds a file while it works (G-3, R-13, C-2, C-18 item 5, REQ-FLOW-006)", () => {
  it("the run names all three, in words that do not say the session changed them, and waits for the user's ruling (R-13)", () => {
    const { waited, c } = edited
    expect(waited.code, waited.out).toBe(0)
    expect(waited.out).toContain(".ai-workspace/tickets/backlog/a-ticket-a-session-wrote.md (added)")
    expect(waited.out).toContain(`scratch.txt (added)`)
    expect(waited.out).toContain("notes-of-the-user.md (added)")
    expect(waited.out).toContain("it may have been the session or you")
    expect(waited.out).not.toMatch(/the session (changed|wrote)/)
    expect(edited.tipsWaited).toBe(edited.tipsBefore)
  })

  it("after a no, with the scratch file put back, the next run commits nothing on the ticket or on main, names the other two alone and waits again (C-2, REQ-FLOW-006)", () => {
    const { noAgain } = edited
    expect(noAgain.code, noAgain.out).toBe(0)
    expect(noAgain.out).toContain("waits for your ruling on what changed")
    expect(noAgain.out).not.toContain("scratch.txt")
    expect(noAgain.out).toContain("a-ticket-a-session-wrote.md (added")
    expect(noAgain.out).toContain("notes-of-the-user.md (added")
    expect(edited.tipsAgain).toBe(edited.tipsNo)
  })

  it("the no commits its own line alone, and nothing it is given on (REQ-FLOW-006 step 3)", () => {
    const { c } = edited
    const [mainWaited, branchWaited] = edited.tipsWaited.split("\n")
    const [mainNo, branchNo] = edited.tipsNo.split("\n")
    expect(mainNo).toBe(mainWaited)
    expect(c.ws.git(["diff", "--name-only", branchWaited ?? "", branchNo ?? ""]).trim()).toBe(`.ai-workspace/tickets/active/${c.ticket}.md`)
    expect(c.ws.git(["diff", "-U0", branchWaited ?? "", branchNo ?? ""]).split("\n").filter((l) => l.startsWith("+") && !l.startsWith("+++"))).toEqual(["+- framework: ruled no on what changed at write-specification"])
  })

  it("no run takes up the ticket the session wrote, nor commits it, before the user has ruled (G-3)", () => {
    const { c, from, nextFrom } = edited
    const before = c.ws.log().slice(from, nextFrom)
    expect(before.some((e) => e.event === "ticket pulled" && e.ticket === "a-ticket-a-session-wrote")).toBe(false)
    expect(before.some((e) => e.event === "commit made" && e.why === "what the user left uncommitted")).toBe(false)
  })

  it("after the yes, the next run commits on the ticket's branch, with the step, each file named, as it was at the yes, and goes on to ask on the specification (C-18 item 5)", () => {
    const { yes, next, c } = edited
    expect(yes.code, yes.out).toBe(0)
    expect(next.out).toContain("waits for your answer on write-specification")
    expect(c.ws.git(["show", `stdo/${c.ticket}:notes-of-the-user.md`])).toBe("what I noted while it worked\n")
    expect(c.ws.git(["show", `stdo/${c.ticket}:.ai-workspace/tickets/backlog/a-ticket-a-session-wrote.md`])).toBe("Make it greet.\n")
    expect(c.ws.board().active).toEqual([c.ticket])
  })
})

describe("a session writes lines of the framework's part, a yes of the user among them (G-16)", () => {
  it("the run names the ticket and waits for the user's ruling", () => {
    const { waited, c } = forged
    expect(waited.code, waited.out).toBe(0)
    expect(waited.out).toContain(`.ai-workspace/tickets/active/${c.ticket}.md (changed)`)
  })

  it("after the user's yes, that line is not read as the user's answer: the user is asked on the specification", () => {
    const { ruled, next, nextFrom, c } = forged
    expect(ruled.code, ruled.out).toBe(0)
    expect(c.ws.read(".ai-workspace", "tickets", "active", `${c.ticket}.md`)).toContain("not the user's answer")
    expect(next.code, next.out).toBe(0)
    expect(next.out).toContain("waits for your answer on write-specification")
    const run = runOf(c.ws.log(), nextFrom)
    expect(run.some((e) => e.event === "vector closed" && e.vector === "write-specification")).toBe(false)
    expect(run.filter((e) => e.event === "user asked").map((e) => e.vector)).toEqual(["write-specification"])
  })

  it("after the user's no, with the ticket left as it is, the next run names the ticket again, commits nothing and waits for the ruling (REQ-FLOW-006 step 1)", () => {
    const { waited, noOne, again, againFrom, c } = refused
    expect(waited.out).toContain(`.ai-workspace/tickets/active/${c.ticket}.md (changed)`)
    expect(noOne.code, noOne.out).toBe(0)
    expect(again.code, again.out).toBe(0)
    expect(again.out).toContain("waits for your ruling on what changed while the session on write-specification worked")
    expect(again.out).toContain(`.ai-workspace/tickets/active/${c.ticket}.md (changed)`)
    expect(refused.tipsAgain).toBe(refused.tipsNo)
    const run = runOf(c.ws.log(), againFrom).slice(0, refused.nextFrom - againFrom)
    expect(run.some((e) => e.event === "session started")).toBe(false)
    expect(run.some((e) => e.event === "vector closed")).toBe(false)
  })

  it("the no names the session's lines as not the user's answer, whatever the user rules (REQ-FLOW-004)", () => {
    const { c } = refused
    const ruled = c.ws.read(".ai-workspace", "tickets", "active", `${c.ticket}.md`)?.split("\n").filter((l) => l.startsWith("- framework: ruled no on what changed")) ?? []
    expect(ruled).toHaveLength(2)
    for (const l of ruled) expect(l).toContain("not the user's answer")
  })

  it("after a second no, with the session's lines taken out, the framework's own rulings are not named: the next run goes on, and the user is asked on the specification alone", () => {
    const { noTwo, next, nextFrom, c } = refused
    expect(noTwo.code, noTwo.out).toBe(0)
    expect(next.code, next.out).toBe(0)
    expect(next.out).not.toContain("waits for your ruling on what changed")
    expect(next.out).toContain("waits for your answer on write-specification")
    const run = runOf(c.ws.log(), nextFrom)
    expect(run.filter((e) => e.event === "user asked").map((e) => e.vector)).toEqual(["write-specification"])
    expect(run.some((e) => e.event === "vector closed" && e.vector === "write-specification")).toBe(false)
    expect(run.some((e) => e.event === "session started" && e.vector === "write-build")).toBe(false)
  })
})

describe("the identities taken at a session's start are missing (REQ-ALG-008, REQ-FLOW-005 step 3)", () => {
  it("the run says so in one sentence, puts every file that differs from the commit the session started from to the user, what the step writes among them, and waits for the ruling", () => {
    const { ran, c } = missing
    expect(ran.code, ran.out).toBe(0)
    expect(ran.out).toContain("The identities taken at the start of the session on induct-ticket are missing, so the framework asks you about every file that differs from the commit the session started from.")
    expect(ran.out).toContain("waits for your ruling on what changed while the session on induct-ticket worked")
    expect(ran.out).toContain(`.ai-workspace/tickets/active/${c.ticket}.md (changed)`)
    expect(ran.out).not.toContain("waits for your answer on induct-ticket")
  })
})

describe("a session writes a ruling line of the framework's part (REQ-FLOW-004)", () => {
  it("a ruling line that says yes to a file the session wrote is not read as a yes: the run names the file as well as the ticket", () => {
    const { waited, c } = sneaked
    expect(waited.code, waited.out).toBe(0)
    expect(waited.out).toContain("waits for your ruling on what changed while the session on write-specification worked")
    expect(waited.out).toContain(`sneak.txt (added)`)
    expect(waited.out).toContain(`.ai-workspace/tickets/active/${c.ticket}.md (changed)`)
  })

  it("the user's yes names the file, and the next run goes on to ask on the specification", () => {
    const { ruled, next, c } = sneaked
    expect(ruled.code, ruled.out).toBe(0)
    const lines = c.ws.read(".ai-workspace", "tickets", "active", `${c.ticket}.md`)?.split("\n").filter((l) => l.startsWith("- framework: ruled yes on what changed")) ?? []
    expect(lines.at(-1)).toContain("sneak.txt")
    expect(lines.at(-1)).toContain("not the user's answer")
    expect(next.code, next.out).toBe(0)
    expect(next.out).toContain("waits for your answer on write-specification")
  })

  it("a ruling line that names the user's yes as not the user's answer leaves nothing out once the user has ruled: the user is asked on the specification alone", () => {
    const { waited, ruled, next, nextFrom, c } = unnamed
    expect(waited.out).toContain(`.ai-workspace/tickets/active/${c.ticket}.md (changed)`)
    expect(ruled.code, ruled.out).toBe(0)
    expect(next.code, next.out).toBe(0)
    expect(next.out).toContain("waits for your answer on write-specification")
    const run = runOf(c.ws.log(), nextFrom)
    expect(run.filter((e) => e.event === "user asked").map((e) => e.vector)).toEqual(["write-specification"])
    expect(run.some((e) => e.event === "session started" && e.vector === "induct-ticket")).toBe(false)
  })
})

describe("the identities taken at a session's start go missing before the user's answer (REQ-ALG-008, REQ-FLOW-006)", () => {
  it("the answer is refused, says that a run asks on every file not committed, and writes nothing on the ticket", () => {
    const { waited, answered } = gone
    expect(waited.out).toContain("waits for your ruling on what changed while the session on induct-ticket worked")
    expect(answered.code, answered.out).toBe(2)
    expect(answered.out).toContain("are missing, so a run asks you about every file not committed")
    expect(gone.tipsAnswered).toBe(gone.tipsWaited)
  })

  it("the next run says that they are missing, puts every file that differs from the commit the session started from, as the record names it, to the user and waits for the ruling", () => {
    const { next, c } = gone
    expect(next.code, next.out).toBe(0)
    expect(next.out).toContain("The identities taken at the start of the session on induct-ticket are missing, so the framework asks you about every file that differs from the commit the session started from.")
    expect(next.out).toContain("waits for your ruling on what changed while the session on induct-ticket worked")
    expect(next.out).toContain("scratch.txt (added)")
    expect(next.out).toContain(`.ai-workspace/tickets/active/${c.ticket}.md (changed)`)
  })
})
