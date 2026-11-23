/**
 * Item 4 of the ticket `261121-005043-reference-frames-and-the-activation-packet`
 * (D91): what a session's agent reports of its cost and its calls is read from
 * what it printed, by the fields the settings name for that agent. An agent
 * that reports nothing is read as before.
 *
 * @uses C14
 * @is REQ-FLOW-002 REQ-FLOW-007
 */
import { describe, expect, it } from "vitest"
import { agentFor, defaultSettings, UNRELEASED, reported } from "../src/flows/workspace.js"

const CLAUDE = { cost: "total_cost_usd", calls: "num_turns" }
const IN_USD = { ...CLAUDE, unit: "USD" }

describe("REQ-FLOW-007 the cost and the calls an agent reports", () => {
  it("are read from the one object the agent prints, by the fields the settings name", () => {
    const printed = "{\"type\":\"result\",\"num_turns\":7,\"result\":\"done\",\"total_cost_usd\":0.2513}\n"
    expect(reported(CLAUDE, printed)).toEqual({ cost: "0.2513", calls: 7 })
  })
  it("where the agent's errors are printed with its output, the last line that reads as one object is read", () => {
    const printed = "Warning: an update is available.\n{\"num_turns\":3,\"total_cost_usd\":0.5}\nA hook said something.\n"
    expect(reported(CLAUDE, printed)).toEqual({ cost: "0.5", calls: 3 })
  })
  it("the cost is given with its unit where the settings name one (D102)", () => {
    const printed = "{\"num_turns\":7,\"total_cost_usd\":0.2513}"
    expect(reported(IN_USD, printed)).toEqual({ cost: "0.2513", unit: "USD", calls: 7 })
    expect(reported(IN_USD, "{\"num_turns\":7}")).toEqual({ calls: 7 })
  })
  it("a cost given as text is kept as it is", () => {
    expect(reported({ cost: "cost" }, "{\"cost\":\"0.40 USD\"}")).toEqual({ cost: "0.40 USD" })
  })
  it("calls that are not a whole number at or above zero are not read", () => {
    expect(reported(CLAUDE, "{\"num_turns\":2.5,\"total_cost_usd\":1}")).toEqual({ cost: "1" })
    expect(reported(CLAUDE, "{\"num_turns\":\"seven\"}")).toEqual({})
  })
  it("an agent that prints no object, or lacks the fields, or has none named, reports nothing", () => {
    expect(reported(CLAUDE, "The code is written.\n")).toEqual({})
    expect(reported(CLAUDE, "[1, 2]")).toEqual({})
    expect(reported(CLAUDE, "{\"result\":\"done\"}")).toEqual({})
    expect(reported(undefined, "{\"total_cost_usd\":0.25}")).toEqual({})
  })
})

describe("REQ-FLOW-002 step 5: the settings name, for each agent, the fields that report its cost and its calls", () => {
  it("set-up's default agent prints one object, and its settings name the two fields and the cost's unit", () => {
    const settings = defaultSettings("stdo_hello.json", UNRELEASED)
    const agent = agentFor(settings, "write-code", "work")
    expect(agent.command).toContain("--output-format")
    expect(agent.command[agent.command.indexOf("--output-format") + 1]).toBe("json")
    expect(agent.reports).toEqual(IN_USD)
  })
  it("an agent the settings give no fields reports nothing", () => {
    const settings = { ...defaultSettings("stdo_hello.json", UNRELEASED), agents: { other: ["other"] }, work: "other" }
    expect(agentFor(settings, "write-code", "work").reports).toBeUndefined()
  })
})
