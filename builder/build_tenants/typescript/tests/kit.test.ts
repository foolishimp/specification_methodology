/**
 * Each kit module tested by its law, as section 1 of the design states it.
 *
 * @uses C2 C3 C4 C5 C6 C8 C9 C14 H5
 * @is REQ-VERIFY-004
 */
import { describe, expect, it } from "vitest"
import { falls, goesOn, within } from "../src/kit/bounded_loop.js"
import { firstMatch } from "../src/kit/first_match.js"
import { fieldsOf } from "../src/kit/field_lines.js"
import { count, list, literal, oneOf, optional, read, record, text, write } from "../src/kit/lossless_encoding.js"
import { difference, isEmpty, paths } from "../src/kit/map_difference.js"
import { memo } from "../src/kit/memo.js"
import { definitionOf, resolve } from "../src/kit/name_resolution.js"
import { fold, normal, type Shape } from "../src/kit/term_recursion.js"
import { all, type Tri } from "../src/kit/three_valued.js"

describe("C2 map difference", () => {
  const a = new Map([["x", "1"], ["y", "2"], ["z", "3"]])
  it("gives the paths added, removed and changed", () => {
    const b = new Map([["x", "1"], ["y", "9"], ["w", "4"]])
    expect(difference(a, b)).toEqual({ added: ["w"], removed: ["z"], changed: ["y"] })
    expect(paths(difference(a, b))).toEqual(["z", "y", "w"])
  })
  it("law: empty exactly when the maps are equal", () => {
    expect(isEmpty(difference(a, new Map(a)))).toBe(true)
    expect(isEmpty(difference(new Map(), new Map()))).toBe(true)
    for (const b of [new Map([["x", "1"], ["y", "2"]]), new Map([...a, ["v", "5"]]), new Map([["x", "1"], ["y", "2"], ["z", "0"]])]) {
      expect(isEmpty(difference(a, b))).toBe(false)
    }
  })
})

describe("C3 three-valued conjunction", () => {
  const values: Tri[] = ["yes", "no", "cannot"]
  it("is cannot if any is cannot, else no if any is no, else yes", () => {
    expect(all([])).toBe("yes")
    expect(all(["yes", "yes"])).toBe("yes")
    expect(all(["yes", "no"])).toBe("no")
    expect(all(["no", "cannot", "yes"])).toBe("cannot")
  })
  it("law: the order of the results makes no difference", () => {
    for (const a of values) for (const b of values) for (const c of values) {
      expect(all([a, b, c])).toBe(all([c, a, b]))
      expect(all([a, b, c])).toBe(all([b, c, a]))
      expect(all([a, b])).toBe(all([b, a]))
    }
  })
})

describe("C4 memo by content key", () => {
  it("law: a result is never read under any other key", () => {
    const m = memo<string>()
    m.keep(["design", "d1", "requirements", "r1"], "yes")
    expect(m.lookup(["design", "d1", "requirements", "r1"])).toBe("yes")
    expect(m.lookup(["design", "d1", "requirements", "r2"])).toBeUndefined()
    expect(m.lookup(["design", "d1"])).toBeUndefined()
    expect(m.lookup(["requirements", "r1", "design", "d1"])).toBeUndefined()
  })
  it("law: keys that would join to the same text are still told apart", () => {
    const m = memo<number>()
    m.keep(["ab", "c"], 1)
    expect(m.lookup(["a", "bc"])).toBeUndefined()
    expect(m.lookup(["abc"])).toBeUndefined()
    m.keep(["1:a;"], 2)
    expect(m.lookup(["a"])).toBeUndefined()
  })
})

type Toy = { readonly kind: "seq"; readonly parts: readonly Toy[] } | { readonly kind: "box"; readonly parts: readonly Toy[] } | { readonly kind: "leaf"; readonly name: string }
const toy: Shape<Toy> = {
  parts: (t) => (t.kind === "leaf" ? [] : t.parts),
  rebuild: (t, parts) => (t.kind === "leaf" ? t : { kind: t.kind, parts }),
  isSequence: (t) => t.kind === "seq",
  isInert: (t) => t.kind !== "leaf" && t.parts.length === 0
}
const leaf = (name: string): Toy => ({ kind: "leaf", name })
const seq = (...parts: Toy[]): Toy => ({ kind: "seq", parts })
const box = (...parts: Toy[]): Toy => ({ kind: "box", parts })
const leaves = (t: Toy): string[] => fold<Toy, string[]>(toy, t, (x, inner) => (x.kind === "leaf" ? [x.name] : inner.flat()))

describe("C5 structural recursion over terms, with a normal form", () => {
  const messy = seq(seq(leaf("a"), seq()), box(seq(leaf("b"), seq(leaf("c")))), box(), leaf("d"))
  it("flattens a sequence inside a sequence and drops a term that does nothing", () => {
    expect(normal(toy, messy)).toEqual(seq(leaf("a"), box(seq(leaf("b"), leaf("c"))), leaf("d")))
  })
  it("law: the rewrites change neither the leaves nor their order", () => {
    expect(leaves(normal(toy, messy))).toEqual(leaves(messy))
    expect(leaves(messy)).toEqual(["a", "b", "c", "d"])
  })
  it("the normal form is its own normal form", () => {
    expect(normal(toy, normal(toy, messy))).toEqual(normal(toy, messy))
  })
})

describe("C6 name resolution with cycle refusal", () => {
  it("follows a name through definitions that are only names, to the first that is not; none for an unknown or cyclic name", () => {
    type D = { readonly to?: string; readonly is?: string }
    const defs = new Map<string, D>([["a", { to: "b" }], ["b", { to: "c" }], ["c", { is: "session" }], ["x", { to: "y" }], ["y", { to: "x" }], ["u", { to: "nowhere" }]])
    const onlyName = (d: D) => d.to
    expect(definitionOf("a", defs, onlyName)).toEqual({ is: "session" })
    expect(definitionOf("c", defs, onlyName)).toEqual({ is: "session" })
    expect(definitionOf("x", defs, onlyName)).toBeUndefined()
    expect(definitionOf("u", defs, onlyName)).toBeUndefined()
  })
  const defs = new Map<string, readonly string[]>([
    ["a", ["b", "c"]],
    ["b", ["c"]],
    ["c", []],
    ["loop", ["round"]],
    ["round", ["loop"]],
    ["self", ["self"]]
  ])
  it("follows every name to its definition", () => {
    expect(resolve(["a"], defs, (d) => d)).toEqual({ unknown: [], cyclic: [] })
    expect(resolve(["a", "missing"], defs, (d) => d)).toEqual({ unknown: ["missing"], cyclic: [] })
  })
  it("law: a name that leads back to itself is refused", () => {
    expect(resolve(["self"], defs, (d) => d).cyclic).toEqual(["self"])
    expect(resolve(["loop"], defs, (d) => d).cyclic).toEqual(["loop"])
  })
})

describe("C8 first-match rule list", () => {
  const rules = [
    { holds: (n: number) => n > 10, gives: () => "big" },
    { holds: (n: number) => n > 0, gives: () => "small" }
  ]
  it("the first rule whose condition holds gives the result", () => {
    expect(firstMatch(rules, 20, () => "none")).toBe("big")
    expect(firstMatch(rules, 5, () => "none")).toBe("small")
    expect(firstMatch(rules, -1, () => "none")).toBe("none")
  })
  it("law: the order is part of the definition", () => {
    expect(firstMatch([...rules].reverse(), 20, () => "none")).toBe("small")
  })
})

describe("C9 bounded loop with a measure", () => {
  it("goes on while the measure strictly falls and the bound is not reached", () => {
    expect(falls(undefined, 5)).toBe(true)
    expect(falls(3, 2)).toBe(true)
    expect(falls(2, 2)).toBe(false)
    expect(goesOn(3, 2, 1, 3)).toBe(true)
    expect(goesOn(3, 2, 3, 3)).toBe(false)
    expect(within(2, 3)).toBe(true)
    expect(within(3, 3)).toBe(false)
  })
  it("law: it ends within the bound, whatever the measure does", () => {
    for (const measures of [[9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [5, 5], [1, 2, 3]]) {
      let rounds = 0
      let before: number | undefined
      for (const now of measures) {
        rounds++
        if (!goesOn(before, now, rounds, 3)) break
        before = now
      }
      expect(rounds).toBeLessThanOrEqual(3)
    }
  })
})

describe("C14 lossless encoding", () => {
  const shape = record({
    name: text,
    kind: oneOf([literal("a"), literal("b")]),
    tags: list(text),
    times: optional(count)
  })
  it("law: a value written and read back is equal to the value", () => {
    const value = { name: "x \"quoted\" é", kind: "b" as const, tags: ["p", "q"], times: 2 }
    const got = read(shape, write(shape, value))
    expect(got).toEqual({ value })
  })
  it("QA-10: a ticket inducted again gives the fields of its last induction, a term in the written form among them", () => {
    const term = '{"term": "sequence", "terms": [{"term": "reference", "name": "write-code"}]}'
    const inductedTwice = `Hello is a command.\n\n- kind: feature\n- enters: intent\n\n- kind: feature\n- enters: code\n- term: ${term}\n`
    expect(fieldsOf(inductedTwice).get("enters")).toBe("code")
    expect(fieldsOf(inductedTwice).get("kind")).toBe("feature")
    expect(fieldsOf(inductedTwice).get("term")).toBe(term)
  })
  it("law: one value has one written form", () => {
    const one = write(shape, { name: "x", kind: "a", tags: [], times: 1 })
    const two = write(shape, { times: 1, tags: [], kind: "a", name: "x" })
    expect(two).toBe(one)
    expect(one.endsWith("\n")).toBe(true)
  })
  it("law: reading refuses anything it does not know", () => {
    const refused = (written: string) => "refused" in read(shape, written)
    expect(refused('{"name":"x","kind":"a","tags":[],"colour":"red"}')).toBe(true)
    expect(refused('{"name":"x","kind":"c","tags":[]}')).toBe(true)
    expect(refused('{"name":"x","kind":"a","tags":[],"times":0}')).toBe(true)
    expect(refused('{"name":"x","kind":"a"}')).toBe(true)
    expect(refused("name: x")).toBe(true)
    expect(refused('{"name":"x","kind":"a","tags":[]}')).toBe(false)
  })
  it("says where a refusal is", () => {
    const got = read(shape, '{"name":"x","kind":"a","tags":[1]}')
    expect("refused" in got && got.refused[0]?.at).toEqual(["tags", 0])
  })
})
