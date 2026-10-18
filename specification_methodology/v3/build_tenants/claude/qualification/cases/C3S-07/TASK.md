# TASK: state two build-tenant bindings and judge a faster plan

## Subject

Product `grant-desk` is a foundation's process for awarding small research
grants. The facts below are the whole subject. The record is invented for
this task and is evidence about no real product.

The product owner, Ama, owns these common requirements:

- G1: each application receives two assessments, each a score from 0 to 10
  with written reasons. The two assessors are different people, and neither
  is the applicant. Neither sees the other's score or reasons before both
  assessments are recorded.
- G2: the award decision for each application is made by the panel chair, a
  person, after reading both assessments.
- G3: each decision records its reasons and the two scores it used.
- G4: the applicant is notified of the decision within 20 working days of
  submission.

Two build tenants realise these requirements.

Tenant S is software: a web application with a database. The application:

- assigns two external assessors from a pool;
- hides each assessor's score field from the other until both are
  submitted;
- computes a ranking from the two scores;
- shows the chair both assessments and the ranking;
- records the chair's decision and reasons;
- sends the notification email.

The chair is Hamid. Lu, an operator, runs the nightly assignment job.

Tenant H is a human process:

1. A clerk, Pia, logs each application on paper and assigns two staff
   assessors from a rota.
2. Pia gives each assessor a blank score sheet. Each assessor returns the
   sheet in a sealed envelope.
3. When both envelopes have arrived, Pia opens them and computes the
   ranking with a fixed spreadsheet formula.
4. Pia passes both sheets and the ranking to the chair, Jon.
5. Jon decides and writes the reasons on a decision form.
6. Pia posts the letter.

Jon wrote the description of tenant H's process.

Statements made in the project:

- Tenant H's lead: "Tenant H needs a different computational calculus from
  tenant S, because it uses no software."
- Tenant H's status report: "Ranking in tenant H is a human judgement,
  because Pia computes it."
- A formal model of tenant H's process passes its structural checker with
  zero diagnostics. Jon: "This shows tenant H conforms to G1 to G4."

The finance office proposes Plan F for both tenants. It would cut cost by
30% and time by six working days. Plan F has two parts:

- The second assessor reads the first assessor's recorded score and reasons
  and marks `agree` or `disagree`, instead of scoring separately. In last
  year's 200 applications, the two scores differed by more than one point
  in only four cases.
- In tenant S, when both scores are 8 or higher, the system issues the
  award, and Lu presses `send` on the batch each evening. The chair
  receives a weekly list of these awards. The status report calls Lu's step
  "human adjudication".

Ama asks you to state each tenant's binding and to judge Plan F.

## Instruction

1. Under a heading `Bindings`, give for each tenant:
   - its computational calculus: the operations, how they compose, their
     effects, and the resource measures material to G1 to G4, with units
     and boundaries;
   - its execution environment.

   Say whether the two tenants can share one calculus.
2. Under a heading `Author, actor and operation`, for each of Jon, Pia and
   Lu:
   - name the person's author and actor roles;
   - name the kind of each operation the person performs.

   Then judge the two status-report statements.
3. Under a heading `Model check`, say what the zero-diagnostic result
   establishes and what it does not.
4. Under a heading `Plan F`, give the result value of the predicate "tenant
   S and tenant H under Plan F conform to G1 to G4". Give the facts that
   decide it, and say how the agreement figures and the savings bear on it.
5. Under a heading `No method source`, list anything the task needed that
   the METHOD block did not supply. Write `none` if nothing.

Return only those five parts, in that order. Do not restate the subject.
