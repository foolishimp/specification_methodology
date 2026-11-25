/**
 * A requirement's "From" line cites the product definition only in words it
 * holds. REQ-METHOD-006's cited "and whether it is small work", which the
 * owner struck from the product definition's "Ask" (finding C-21 of the
 * review of release 3.2.0).
 *
 * @uses C14
 * @is REQ-METHOD-006
 */
import { readdirSync, readFileSync } from "node:fs"
import { join } from "node:path"
import { describe, expect, it } from "vitest"
import { tenant } from "./scenario_driver.js"

const specification = join(tenant, "..", "..", "specification")
const flat = (text: string): string => text.replace(/\s+/g, " ")

describe("REQ-METHOD-006 the words a requirement cites from the product definition are its words", () => {
  it("each phrase a requirement's From line quotes from the product definition is in it", () => {
    const product = flat(readFileSync(join(specification, "PRODUCT.md"), "utf8"))
    const cited: string[] = []
    for (const file of readdirSync(join(specification, "requirements")).filter((f) => f.endsWith(".md"))) {
      for (const from of flat(readFileSync(join(specification, "requirements", file), "utf8")).split(/(?=From: )/).slice(1)) {
        const line = from.split(/ (?=#|- |\*\*)/)[0] ?? ""
        for (const part of line.split(";").filter((p) => p.includes("product definition"))) {
          for (const m of part.matchAll(/"([^"]+)"/g)) cited.push(`${file}: ${m[1] ?? ""}`)
        }
      }
    }
    expect(cited.length).toBeGreaterThan(0)
    // A term is cited by its name, which the product definition may write in lower case.
    const missing = cited.filter((c) => !product.toLowerCase().includes(c.slice(c.indexOf(": ") + 2).replace(/[.,]$/, "").toLowerCase()))
    expect(missing).toEqual([])
    expect(cited.some((c) => c.includes("at which node it enters the graph"))).toBe(true)
  })
})
