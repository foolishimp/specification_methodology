# Successor source findings

Exact subject: revision 2 SOURCE_FREEZE.json `e246c76014a118e04e58b55482660b197ff1e587959514338e155c7de4626a65`, baseline `eb9300a837de00daffe09fff91c6861885334eec`. Frozen pre-exposure expectations remain unchanged. Same-family nonauthor working review; no Product disposition or release approval.

## OP-02 — S2: Named-section projection crosses a real container boundary

Location: `specification_methodology/v3/build_tenants/common/plugins/spec/scripts/read_basis.py:100` through the fence continuation at 102–105, consumed by section selection at 156–159. Reader SHA256 `7ff07c6bce0b9e5bc2d8060190570e9a0108c87950a30bb7a42fd2ca968e6cff`.

Source contract: frozen E03/E12 require prescribed acquisition to preserve its bounded source relation; selected requirement CS-09 (`specification/requirements/COORDINATED_SKILLS.md:20`) requires a unique bounded section or explicit refusal/incomplete result. Design lines 56–60 claims exact ATX sections and refusal of unsupported/ambiguous markup. These are implementation claims, not a new STDO law.

The parser removes quote/list container markers but retains only one global fence marker. It therefore cannot notice that a quoted fenced code block ended with its containing block. A later fence in a new block is mistaken for the first fence's close; a real intervening heading is suppressed. For this valid Markdown specimen, selecting `One` must return lines 1–3 (or explicitly refuse the unsupported structure):

~~~~markdown
## One
> ```
> quoted example
## Two
UNSELECTED TWO
> ```
> another quote
## Three
UNSELECTED THREE
~~~~

The frozen CLI instead exits 0 with `status: checked`, labels lines 1–7 as `One`, and includes the real `Two` heading and `UNSELECTED TWO`. This is not just a missing heading or a conservative refusal. The returned section has a sound digest of the wrong projection. An actor using the exact named-section command can receive source outside that selected section; whole-member digest verification cannot detect that semantic boundary error.

The independent oracle is the [CommonMark 0.31.2 fenced-code rule](https://spec.commonmark.org/0.31.2/#fenced-code-blocks): a containing block's end also ends its fenced code block. The source does not claim arbitrary CommonMark support; a closed subset may reject this input, but may not positively misproject it.

Evidence: `REPRO_SECTION_CONTAINER.py` SHA256 `12c984226142d812770bc47692c38bc741fb7672f080838fe2550b65d2d62a93` and `SECTION_CONTAINER_REPRO.json` SHA256 `54229cc052e9962748534a95af36fc2add274ce0b66ae9621227ef9bfc948176`. Run with `python3 -I -B .../review/successor/REPRO_SECTION_CONTAINER.py`. The harness writes only its own review scratch directory, provides a mock manager with matching definition/manifest/member identities and hashes, and runs the exact frozen reader as a subprocess. All 19 existing mechanical tests passed independently; their quoted/list fence example has an explicit same-container close and does not discriminate this case.

Technical severity S2: a selected functional property is falsified by a successful wrong result; the bounded reader's positive standing is unsound for this supported-looking source shape. Blast radius is the optional reader's projection on this container shape. No released 3.0.3 source or live host trace has yet been shown to contain the shape; this finding is not a claim of an observed native-session disclosure. It does not negate an independently valid projection on ordinary headings. Product priority and current-boundary disposition remain Executive decisions.

Required correction is to preserve the container boundary when selecting sections, or refuse structures the closed subset cannot safely distinguish. Retain this discriminator and re-evaluate exact reader bytes. No implementation repair or acceptance is performed by this reviewer. Repair complexity/regression risk is bounded but not established by the review.
