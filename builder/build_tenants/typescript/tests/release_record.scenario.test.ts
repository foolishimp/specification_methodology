/**
 * The release that builds a product (REQ-FLOW-010), driven through the
 * command-line program alone, as a user would, with the stand-in agent. Two
 * programs are used: the one built from the source, which is no release, and
 * the product installed from its release by the one command its instructions
 * give. Each command names the workspace it is given on, so either program can
 * be given on either workspace, as a user with two installs would.
 *
 * A workspace set up by one release is run by a second, cut from the same
 * source with another version: the run is refused before any step, starts no
 * session and commits nothing. The user gives the command to record the
 * release with the second; it writes the second in place of the first, and
 * the next run by the second goes on, while one by the first is refused. An
 * answer given by the first, which the record does not name, is not refused.
 * The user then edits the record by hand to the first; its next run goes on and
 * commits the edit as the user's change on main.
 *
 * The workspace set up by the first release is also run by the build, by the
 * release under a record the user edited to another release, with no record,
 * and with a record that names no release: each run is refused before any
 * step, starts no session and commits nothing, and says what is recorded and
 * what is running. The other commands are not refused. The user then gives
 * the command to record the release; it changes the record alone and commits
 * nothing, and the next run by that release goes on and commits it as the
 * user's change on main.
 *
 * @uses C14
 * @is REQ-FLOW-010 REQ-FLOW-001 REQ-FLOW-002 REQ-FLOW-003 REQ-INTERFACE-001
 */
import { createHash } from "node:crypto"
import { readFileSync, writeFileSync } from "node:fs"
import { join } from "node:path"
import { afterAll, beforeAll, describe, expect, it } from "vitest"
import { build, clean, installed, RELEASE_VERSION, S1_FIXTURES, S1_TICKET, Workspace, type LogEntry, type Said } from "./scenario_driver.js"

afterAll(clean)

const SETTINGS = [".stdo-builder", "settings.json"] as const

/** What a program prints of a refusal for its release: what is recorded and what is running, in its words. */
const UNRELEASED_WORDS = "an unreleased build of STDO Builder"
const releaseWords = (version: string, sha: string): string => `release ${version} of STDO Builder, whose manifest's sha256 is ${sha}`

let onBuild: Workspace
let onRelease: Workspace
let onSecond: Workspace
let released: { readonly version: string; readonly manifest_sha256: string }
let second: { readonly version: string; readonly manifest_sha256: string }

/** The version of the second release, cut from the same source. */
const SECOND_VERSION = "9.8.8-test.2"
const sha256Of = (file: string): string => createHash("sha256").update(readFileSync(file)).digest("hex")

const settingsOf = (ws: Workspace): Record<string, unknown> => JSON.parse(ws.read(...SETTINGS) ?? "{}") as Record<string, unknown>
const writeSettings = (ws: Workspace, settings: Record<string, unknown>): void => writeFileSync(ws.path(...SETTINGS), `${JSON.stringify(settings, null, 2)}\n`)
/** The settings with the record taken out, by hand. */
const withoutRecord = (settings: Record<string, unknown>): Record<string, unknown> => Object.fromEntries(Object.entries(settings).filter(([k]) => k !== "builder"))

/** Main's commit, what is uncommitted, and how many entries the log holds: what a refused run must leave as it was, but the log. */
interface Left {
  readonly main: string
  readonly status: string
  readonly entries: number
}
const leftOf = (ws: Workspace): Left => ({ main: ws.git(["rev-parse", "main"]).trim(), status: ws.git(["status", "--porcelain"]), entries: ws.log().length })

/** A run refused for its release: what it printed, what the workspace held before and after, and what the log gained. */
interface Refused {
  readonly said: Said
  readonly before: Left
  readonly after: Left
  readonly logged: readonly LogEntry[]
}

const refusedRun = async (by: Workspace, ws: Workspace): Promise<Refused> => {
  const before = leftOf(ws)
  const said = await by.command(["run", ws.root, "--stand-in", S1_FIXTURES])
  const after = leftOf(ws)
  return { said, before, after, logged: ws.log().slice(before.entries) }
}

beforeAll(() => {
  onBuild = new Workspace(build())
  const made = installed()
  onRelease = new Workspace(made.cli, made.bin)
  released = { version: RELEASE_VERSION, manifest_sha256: sha256Of(join(made.release, "manifest.json")) }
  const madeSecond = installed(SECOND_VERSION)
  onSecond = new Workspace(madeSecond.cli, madeSecond.bin)
  second = { version: SECOND_VERSION, manifest_sha256: sha256Of(join(madeSecond.release, "manifest.json")) }
}, 240_000)

describe("REQ-FLOW-010 set-up records the release that builds the product", () => {
  let fromRelease: Said
  let fromBuild: Said
  let again: Said
  let settingsBefore = ""
  let ranFromBuild: Said
  let ranLog: readonly LogEntry[] = []

  beforeAll(async () => {
    fromRelease = await onRelease.setup()
    fromBuild = await onBuild.setup()
    settingsBefore = onBuild.read(...SETTINGS) ?? ""
    // Set-up run again on the build's workspace, by the release.
    again = await onRelease.command(["setup", onBuild.root, "--name", "Hello"])
    await onBuild.ticket(S1_TICKET)
    ranFromBuild = await onBuild.run(S1_FIXTURES)
    ranLog = onBuild.log()
  }, 180_000)

  it("acceptance 1: set-up from a release records that release's version and the sha256 of its manifest, in the settings it commits", () => {
    expect(fromRelease.code, fromRelease.out).toBe(0)
    expect(settingsOf(onRelease).builder).toEqual(released)
    expect((JSON.parse(onRelease.git(["show", "main:.stdo-builder/settings.json"])) as Record<string, unknown>).builder).toEqual(released)
    expect(fromRelease.out).toContain(`The settings record ${releaseWords(released.version, released.manifest_sha256)} as the one that builds this product.`)
  })

  it("acceptance 1: set-up from a build that is no release records an unreleased build, and a run from such a build is not refused for its release", () => {
    expect(fromBuild.code, fromBuild.out).toBe(0)
    expect(settingsOf(onBuild).builder).toBe("unreleased build")
    expect(fromBuild.out).toContain(`The settings record ${UNRELEASED_WORDS} as the one that builds this product.`)
    expect(ranFromBuild.code, ranFromBuild.out).toBe(0)
    expect(ranFromBuild.out).toContain("waits for your answer on induct-ticket")
    expect(ranLog.filter((e) => e.event === "run ended" && e.why === "release")).toEqual([])
  })

  it("REQ-FLOW-002 step 7: set-up writes the command to record the release into the agent instruction files, beside the other commands", () => {
    for (const file of ["AGENTS.md", "CLAUDE.md"]) {
      const block = onRelease.read(file) ?? ""
      for (const command of ["ticket .", "run .", "answer .", "show .", "registry .", "record-release ."]) expect(block, `${file}: ${command}`).toContain(`\`stdo-builder ${command}`)
    }
  })

  it("law: set-up run again, by another release, does not change the record", () => {
    expect(again.code, again.out).toBe(0)
    expect(again.out).toContain("It wrote nothing")
    expect(again.out).not.toContain("The settings record")
    expect(onBuild.read(...SETTINGS)).toBe(settingsBefore)
  })
})

describe("REQ-FLOW-010 a run by another release than the one recorded, or with none recorded, is refused", () => {
  const other = { version: "0.0.1-other", manifest_sha256: "0".repeat(64) }
  let byBuild: Refused
  let byOther: Refused
  let byNone: Refused
  let byNonsense: Refused
  let others: readonly Said[] = []
  let recorded: Said
  let settingsSetUp = ""
  let settingsRecorded = ""
  let diff: readonly string[] = []
  let beforeRecord: Left
  let afterRecord: Left
  let ranAfter: Said
  let mainAfter = ""
  let byHand: readonly string[] = []
  let recordedAgain: Said

  beforeAll(async () => {
    const ws = onRelease
    await ws.setup()
    settingsSetUp = ws.read(...SETTINGS) ?? ""
    const original = settingsOf(ws)
    // What the user leaves uncommitted on main: a note of their own and a ticket.
    writeFileSync(ws.path("NOTES.md"), "A note of the user's own.\n")
    await ws.ticket(S1_TICKET)
    byBuild = await refusedRun(onBuild, ws)
    writeSettings(ws, { ...original, builder: other })
    byOther = await refusedRun(ws, ws)
    writeSettings(ws, { ...original, builder: 42 })
    byNonsense = await refusedRun(ws, ws)
    others = [await ws.show(), await ws.command(["registry", ws.root]), await ws.ticket("Another ticket, written while the record names no release.")]
    // The settings with no record, committed by the user's own hand: as a product set up before the record was made.
    writeSettings(ws, withoutRecord(original))
    ws.git(["-c", "user.name=The user", "-c", "user.email=user@example.invalid", "commit", "-q", "-m", "the settings as they were before the record", "--", ".stdo-builder/settings.json"])
    byNone = await refusedRun(ws, ws)
    beforeRecord = leftOf(ws)
    recorded = await ws.command(["record-release", ws.root])
    afterRecord = leftOf(ws)
    settingsRecorded = ws.read(...SETTINGS) ?? ""
    diff = ws.git(["diff", "--unified=0", "--", ".stdo-builder/settings.json"]).split("\n").filter((l) => /^[-+] /.test(l))
    ranAfter = await ws.run(S1_FIXTURES)
    mainAfter = ws.git(["show", "main:.stdo-builder/settings.json"])
    byHand = ws.git(["log", "--format=%s", "--name-only", "-1", "--grep=what the user changed by hand on main", "main"]).split("\n").filter((l) => l !== "")
    recordedAgain = await ws.command(["record-release", ws.root])
  }, 240_000)

  const refusedAsSaid = (r: Refused, recordedWords: string, runningWords: string): void => {
    expect(r.said.code, r.said.out).toBe(2)
    expect(r.said.out).toContain("The run is refused before any step")
    expect(r.said.out).toContain(`the settings record ${recordedWords} as the one that builds this product, and this is ${runningWords}.`)
    expect(r.said.out).toContain("stdo-builder record-release")
  }

  const leftNothing = (r: Refused): void => {
    // It commits nothing: main is where it was, and what the user left uncommitted is still uncommitted.
    expect(r.after.main).toBe(r.before.main)
    expect(r.after.status).toBe(r.before.status)
    // It starts no session.
    expect(r.logged.filter((e) => e.event === "session started")).toEqual([])
    expect(r.logged.filter((e) => e.event === "run ended").map((e) => [e.ending, e.why])).toEqual([["refused", "release"]])
  }

  it("a run from a build that is no release, where a release is recorded, starts no session, commits nothing and is refused, saying what is recorded and what is running", () => {
    refusedAsSaid(byBuild, releaseWords(released.version, released.manifest_sha256), UNRELEASED_WORDS)
    leftNothing(byBuild)
    expect(byBuild.before.status).toContain("NOTES.md")
  })

  it("law: a record the user edits by hand is read as it stands; one that names another release refuses a run by this one", () => {
    refusedAsSaid(byOther, releaseWords(other.version, other.manifest_sha256), releaseWords(released.version, released.manifest_sha256))
    leftNothing(byOther)
    refusedAsSaid(byNonsense, "42, which names no release of STDO Builder", releaseWords(released.version, released.manifest_sha256))
    leftNothing(byNonsense)
  })

  it("acceptance 2: a run where nothing is recorded starts no session, commits nothing and is refused, saying that nothing is recorded and what is running", () => {
    refusedAsSaid(byNone, "no release of STDO Builder", releaseWords(released.version, released.manifest_sha256))
    leftNothing(byNone)
  })

  it("law: only a run is refused for its release; show, the registry and a ticket are not", () => {
    for (const s of others) {
      expect(s.code, s.out).toBe(0)
      expect(s.out).not.toContain("record-release")
    }
  })

  it("the command to record the release writes it in place of the record there was, changes nothing else, commits nothing, and adds one entry to the log, the release recorded (REQ-FLOW-007)", () => {
    expect(recorded.code, recorded.out).toBe(0)
    expect(recorded.out).toContain(`The settings now record ${releaseWords(released.version, released.manifest_sha256)} as the one that builds this product, in place of no release of STDO Builder.`)
    expect(recorded.out).toContain("Nothing is committed")
    // The record is put where set-up puts it, after the definition file's name, and no other line changes: the settings are as set-up wrote them.
    expect(diff).toEqual(['+  "builder": {', `+    "version": "${released.version}",`, `+    "manifest_sha256": "${released.manifest_sha256}"`, "+  },"])
    expect(settingsRecorded).toBe(settingsSetUp)
    expect(afterRecord.main).toBe(beforeRecord.main)
    expect(afterRecord.entries).toBe(beforeRecord.entries + 1)
    // Given again where the settings already record what is running, it changes nothing.
    expect(recordedAgain.code, recordedAgain.out).toBe(0)
    expect(recordedAgain.out).toContain("already record")
  })

  it("acceptance 3: after the user gives the command to record the release, a run by the release that gave it is not refused for its release, and commits the record as the user's change on main", () => {
    expect(ranAfter.code, ranAfter.out).toBe(0)
    expect(ranAfter.out).toContain("waits for your answer on induct-ticket")
    expect((JSON.parse(mainAfter) as Record<string, unknown>).builder).toEqual(released)
    expect(byHand[0]).toBe("what the user changed by hand on main")
    expect(byHand).toContain(".stdo-builder/settings.json")
    expect(byHand).toContain("NOTES.md")
  })
})

describe("REQ-FLOW-010 a run by another release than the one recorded, and the command to record it", () => {
  let ws: Workspace
  let bySecond: Refused
  let recorded: Said
  let beforeRecord: Left
  let afterRecord: Left
  let diff: readonly string[] = []
  let ranSecond: Said
  let byFirst: Refused
  let mainAfter = ""
  let byHand: readonly string[] = []
  let answeredByFirst: Said
  let answerLogged: readonly LogEntry[] = []
  let settingsAfterAnswer = ""
  let ranUnderHandEdit: Said
  let ranUnderHandEditLogged: readonly LogEntry[] = []
  let mainAfterHandEdit = ""
  let byHandAfterEdit: readonly string[] = []

  beforeAll(async () => {
    // A workspace of its own, set up by the first release, with a ticket the user left uncommitted.
    ws = new Workspace(onRelease.cli, onRelease.bin)
    await ws.setup()
    await ws.ticket(S1_TICKET)
    bySecond = await refusedRun(onSecond, ws)
    beforeRecord = leftOf(ws)
    recorded = await onSecond.command(["record-release", ws.root])
    afterRecord = leftOf(ws)
    diff = ws.git(["diff", "--unified=0", "--", ".stdo-builder/settings.json"]).split("\n").filter((l) => /^[-+] /.test(l))
    ranSecond = await onSecond.command(["run", ws.root, "--stand-in", S1_FIXTURES])
    mainAfter = ws.git(["show", "main:.stdo-builder/settings.json"])
    byHand = ws.git(["log", "--format=%s", "--name-only", "-1", "--grep=what the user changed by hand on main", "main"]).split("\n").filter((l) => l !== "")
    byFirst = await refusedRun(onRelease, ws)
    // The record names the second release, and the ticket waits on induct-ticket: the user answers with the first.
    const beforeAnswer = ws.log().length
    answeredByFirst = await ws.answer("yes")
    answerLogged = ws.log().slice(beforeAnswer)
    settingsAfterAnswer = ws.read(...SETTINGS) ?? ""
    // The user edits the record by hand to the first release, and runs it.
    writeSettings(ws, { ...settingsOf(ws), builder: released })
    const beforeRun = ws.log().length
    ranUnderHandEdit = await ws.run(S1_FIXTURES)
    ranUnderHandEditLogged = ws.log().slice(beforeRun)
    mainAfterHandEdit = ws.git(["show", "main:.stdo-builder/settings.json"])
    byHandAfterEdit = ws.git(["log", "--format=%s", "--name-only", "-1", "--grep=what the user changed by hand on main", "main"]).split("\n").filter((l) => l !== "")
  }, 360_000)

  it("acceptance 2: a run by another release than the one recorded starts no session, commits nothing and is refused, saying what is recorded and what is running", () => {
    expect(bySecond.said.code, bySecond.said.out).toBe(2)
    expect(bySecond.said.out).toContain("The run is refused before any step")
    expect(bySecond.said.out).toContain(`the settings record ${releaseWords(released.version, released.manifest_sha256)} as the one that builds this product, and this is ${releaseWords(second.version, second.manifest_sha256)}.`)
    expect(bySecond.said.out).toContain(`stdo-builder record-release ${ws.root}`)
    expect(bySecond.after.main).toBe(bySecond.before.main)
    expect(bySecond.after.status).toBe(bySecond.before.status)
    expect(bySecond.before.status).toContain(".ai-workspace/")
    expect(bySecond.logged.filter((e) => e.event === "session started")).toEqual([])
    expect(bySecond.logged.filter((e) => e.event === "run ended").map((e) => [e.ending, e.why])).toEqual([["refused", "release"]])
  })

  it("the command to record the release, given with the second, writes it in place of the first, changes nothing else and commits nothing", () => {
    expect(recorded.code, recorded.out).toBe(0)
    expect(recorded.out).toContain(`The settings now record ${releaseWords(second.version, second.manifest_sha256)} as the one that builds this product, in place of ${releaseWords(released.version, released.manifest_sha256)}.`)
    expect(diff).toEqual([
      `-    "version": "${released.version}",`,
      `-    "manifest_sha256": "${released.manifest_sha256}"`,
      `+    "version": "${second.version}",`,
      `+    "manifest_sha256": "${second.manifest_sha256}"`
    ])
    expect(afterRecord.main).toBe(beforeRecord.main)
    // The log gains one entry, the release recorded (REQ-FLOW-007).
    expect(afterRecord.entries).toBe(beforeRecord.entries + 1)
  })

  it("acceptance 3: after the user gives the command, a run by the release that gave it is not refused for its release, and commits the record as the user's change on main; a run by the first is now refused", () => {
    expect(ranSecond.code, ranSecond.out).toBe(0)
    expect(ranSecond.out).toContain("waits for your answer on induct-ticket")
    expect((JSON.parse(mainAfter) as Record<string, unknown>).builder).toEqual(second)
    expect(byHand[0]).toBe("what the user changed by hand on main")
    expect(byHand).toContain(".stdo-builder/settings.json")
    expect(byFirst.said.code, byFirst.said.out).toBe(2)
    expect(byFirst.said.out).toContain(`the settings record ${releaseWords(second.version, second.manifest_sha256)} as the one that builds this product, and this is ${releaseWords(released.version, released.manifest_sha256)}.`)
    expect(byFirst.logged.filter((e) => e.event === "session started")).toEqual([])
  })

  it("law: only a run is refused for its release; an answer given by a release the record does not name is not", () => {
    expect(answeredByFirst.code, answeredByFirst.out).toBe(0)
    expect(answeredByFirst.out).not.toContain("refused before any step")
    expect(answeredByFirst.out).not.toContain("record-release")
    expect(answerLogged.filter((e) => e.event === "answer written").map((e) => [e.vector, e.result])).toEqual([["induct-ticket", "yes"]])
    // The answer leaves the record as it was.
    expect((JSON.parse(settingsAfterAnswer) as Record<string, unknown>).builder).toEqual(second)
  })

  it("law: a record the user edits by hand is read as it stands; edited to what is running, a run goes on and commits it as the user's change on main", () => {
    expect(ranUnderHandEdit.code, ranUnderHandEdit.out).toBe(0)
    expect(ranUnderHandEdit.out).not.toContain("record-release")
    expect(ranUnderHandEditLogged.filter((e) => e.event === "run ended" && e.why === "release")).toEqual([])
    expect(ranUnderHandEditLogged.some((e) => e.event === "session started")).toBe(true)
    expect((JSON.parse(mainAfterHandEdit) as Record<string, unknown>).builder).toEqual(released)
    expect(byHandAfterEdit[0]).toBe("what the user changed by hand on main")
    expect(byHandAfterEdit).toContain(".stdo-builder/settings.json")
  })
})
