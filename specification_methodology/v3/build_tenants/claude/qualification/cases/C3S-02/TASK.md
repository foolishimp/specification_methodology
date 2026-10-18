# TASK A: record one transformation and its judgment

## Subject

Workspace `W-invoice-rounding`: the billing model of a small invoicing
service. The facts below are the whole subject; the record is invented for
this task and is evidence about no real product.

Input model `M-billing@r3`: signature `sig-billing-1`, calculus basis
`calc-1`, source basis spec commit `4a1f9e20`, serialised in the canonical
record grammar `cj-1`. Its complete local population is three records:

| Id | Kind | Content | Owner | `cj-1` digest |
|---|---|---|---|---|
| REQ-12 | requirement object | "Every invoice total is rounded to the nearest cent, half away from zero, after tax is applied." | Lena (product owner, billing) | `a1…01` |
| LAT-12a | latitude | applies_to REQ-12; allowed variation: rounding may be performed in the database or in the service; forbidden variation: rounding before tax; scope invoice totals; basis `4a1f9e20`; invalidation: any change to REQ-12 | Lena | `a1…02` |
| RES-4 | residual | kind ambiguity; subject REQ-12; uncertainty: whether credit notes are invoices for REQ-12; consequence: credit-note totals may round differently; re_entry Requirements | Lena | `a1…03` |

Its external reference set is one identity, `ext:iso-4217-minor-units`,
resolved to target `iso4217@2024-06` (kind: published table, reference
domain: currency data, basis relation: pinned, resolution basis `4a1f9e20`,
evidence `EV-iso-pin-2`).

Proposed successor `M-billing@r4`: same signature, calculus basis and source
basis, serialised in `cj-1`. Its local population is four records:

| Id | Kind | Content | Owner | `cj-1` digest |
|---|---|---|---|---|
| REQ-12 | requirement object | unchanged text | Lena | `a1…01` |
| LAT-12a | latitude | unchanged | Lena | `a1…02` |
| RES-4 | residual | as in r3, except the consequence now reads "credit-note totals may round differently; design DES-12.1 assumes credit notes are excluded" | Lena | `b2…03` |
| DES-12.1 | design clause | "InvoiceService.total() applies tax, then rounds once, half away from zero on the absolute value with the sign restored, to the currency's minor units from `ext:iso-4217-minor-units`." | Tomas (design owner, billing) | `b2…04` |

Its external reference set is the same identity, resolved to the same
target with every resolution field as in r3.

The step from r3 to r4 was performed by Tomas on 2026-10-11 under traversal
record `v-req-to-design-3` (context `W-invoice-rounding`, owner Tomas,
scope: design records derived from REQ-12, basis `4a1f9e20`, operation
authority grant `G-88`, stop contract: stop on any change to a requirement
record). Grant `G-88`, issued by the billing lead Ravi, permits Tomas to
add design records under REQ-12; it does not permit edits to requirement,
latitude or residual records. The step's evidence on file is the review
note `RN-31`; no disposition of RES-4 by anyone is on file.

Judgment: on 2026-10-12T09:00Z Nadia, the independent design reviewer who
holds evaluation authority over the billing design records, examined
`M-billing@r4` (digest `sha256:7d…e9`) against REQ-12 and LAT-12a, with
evidence `RN-31` and test run `TR-205` on build `b-40`, and decided that
DES-12.1 conforms to REQ-12 within LAT-12a. Ravi holds acceptance authority
for billing design records.

## Instruction

1. Under a heading `Transformation record`, write the transformation record
   for the step from r3 to r4 in the shape the METHOD block gives, with
   every field filled from the subject, including the preserved, introduced
   and removed identities and the external partitions. Where a field needs
   something the subject does not state, write what is missing rather than
   inventing it.
2. Under a heading `Application`, state in at most three sentences which
   application outcome the record supports and why.
3. Under a heading `Judgment record`, write Nadia's judgment in the shape
   the METHOD block gives.
4. Under a heading `Promotion`, state in at most three sentences what
   promoting r4 would require and who holds it.
5. Under a heading `No method source`, list anything the task needed that
   the METHOD block did not supply; write `none` if nothing.

Return only those five parts, in that order. Do not restate the subject.
