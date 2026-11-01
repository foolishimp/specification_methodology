# Use a_c on a user's project

These requirements make the existing a_c capabilities usable as one Product
for projects built under an exact selected STDO 3.0.x release. They refine
[AC-R-001–015](README.md), [formalisation](formalisation.md),
[actor support](fd-support-tools.md) and [composition](fd-composition.md).
Those owners retain their definitions. STDO owns project organisation and the
method of construction, review and acceptance; a_c supplies representations,
inspection, declared verification and context support.

An **axiomatic program** here is the project's source-owned description of
entities, assumptions, constraints, permitted constructions and their declared
relationships. The representation makes that description inspectable and
usable during construction. Ordinary prose does not become executable logic
or a proved theorem merely by appearing as a record. Algorithms, concrete
realizations and evidence keep their own identities and correspondence.

## User outcome

A project owner can start from their own STDO Product Definition and source,
create a source-linked proposed representation, read its constraints and
relationships, request the supported checks, and give builders or reviewers
selected context. They can repeat that work after change without mistaking an
old model, proof, assessment or exported document for the current one. A reader
can receive the resulting documentation without installing its authoring stack.

| ID | Required behaviour and discriminator |
|---|---|
| PU-01 Project binding | Select the existing Product Definition, exact consumer-method release and source cut, tenant/profile and requested operations. Preserve WHAT, HOW and WORK ownership. A new project must not require an STDO-subject allowlist, tenant-source edit or copied private study script. An unsupported profile is reported explicitly. |
| PU-02 Source interpretation | Offer the existing declared F_P creation path and a supported authored-model input path. Retain source grounding, coverage, assumptions, uncertainties and external references. Missing interpretation or an unmodelled source obligation remains visible. A discovered code edge cannot silently become a normative dependency. |
| PU-03 Readable project documentation | Generate portable documentation for the selected project: full records, constraints, conditions, exceptions, sources, relation meanings and reading trails, with 2D/3D navigation. Name the represented source and model, document generation cut and any distributing release separately. No mandatory STDO subject identity or branding. No network or authoring tool is required merely to read an exported view. |
| PU-04 Bounded validation | Expose the existing structural and formal contracts, exact checked subject, assumptions and evidence. Distinguish checked, refused, unsupported and incomplete outcomes as defined by the selected operation. A closure proof proves the declared closure; it cannot establish that an omitted source obligation should have been declared. Semantic review, executable tests and mathematical proof remain different evidence. |
| PU-05 Builder and reviewer use | Let the caller select task records and the required governing closure, then verify the selected view and its actual delivery when that gate is required. Preserve residuals and currentness. Reuse the method's activation and admission contracts and the FD tools; do not introduce an a_c executive or an alternative workflow. Human-readable exports and agent context are views of the same identified model, each with its declared selection. |
| PU-06 Change and continuation | Observe changed source, model, selection, profile, authority or checking machinery and invalidate the affected reusable claims. Preserve previous evidence as history with its original subject. Provide affected-scope information to the actor; do not silently carry old acceptance forward or discard unresolved obligations. |
| PU-07 Leaves and composition | A leaf remains usable and releasable as its own Product. A higher-level project names the exact children, shared providers and edge contracts it consumes. Preserve recursive ownership and cross-project references without flattening all source into one authority. Use FC-01–07 for recipient routes, exports, exclusions and retained provenance: visibility of a graph path grants no read, disclosure or operation permission. Unsupported recursion/cycles receive explicit outcomes. |
| PU-08 Public operation and installation | Supply documented public entry points and an installable, versioned package with declared optional engines. The same interfaces work outside this repository. State which features work without Graphify execution or Lean and which require a checked external toolchain. A viewer-only installation must not be advertised as the authoring or formal-verification installation. |
| PU-09 Integrated qualification | Demonstrate the complete user path on a non-STDO subject, from a fresh installation, without private developer fixtures or tenant-source changes. Include one composed subject and negative controls below. Retain quality, time and resource observations; declare no efficiency or fidelity improvement without an appropriate comparison. |

These are active required outcomes. Existing component evidence does not mark
the integrated user product satisfied. Concrete descriptors, adapters, command
names, UI, packaging and execution design belong to the tenant HOW. The current
browser viewer is the reading UI; this requirement does not prescribe a new
browser editor or orchestration service.

## Concrete acceptance exercise

Use a small invoice-export project, rather than another methodology corpus.
Its source defines decimal-value preservation and deterministic column ordering.
It retains an unresolved rounding-policy question. One leaf provides decimal
formatting; another produces the export using that provider's named contract.
The parent owns composition requirements. Synthetic fixtures contain no private
customer data.

1. Bind and interpret the new leaf using the public tool installation. Inspect
   source-linked constraints and the unresolved policy in the generated reader.
   Record an independent semantic assessment of this interpretation.
2. Select the export requirement. Its declared closure includes the formatting
   obligation and the unresolved policy record. Omitting either from a submitted
   view must fail the selected closure check; an insufficient budget must refuse
   rather than silently shorten the context.
3. Deliver the checked view through the ordinary Worker path. Retain evidence
   of the actual received bytes. Test the produced implementation against the
   source's numeric examples. Report implementation correctness separately from
   the view's structural verification.
4. Change the source's rounding rule. The old representation and evidence must
   remain historical; the refreshed model, documentation and selected context
   name the new cut and retain any unresolved consequences.
5. Compose the two leaves. Give the export Worker access to the provider's
   public contract but exclude an internal source. Direct reads and retained
   inline content must obey the same recipient route. A shared ancestor or a
   visible dependency must not grant the excluded read.
6. Install elsewhere and open the exported documentation with the generating
   workspace unavailable. Repeat the public check where its toolchain is
   installed. Read-only viewing does not require running Lean or an LLM.

The semantic assessment must also consider a representation that fails to
declare the rounding dependency at all. Structural closure alone can accept
that incomplete interpretation. Keeping this case explicit tests the combined
review-and-tool workflow without attributing semantic discovery to Lean.
