---
name: shadow-tribunal-director
description: Orchestrate the three independent Shadow Tribunal skills, shadow-devil, shadow-guardian, and shadow-arbiter, into an exhaustive task-specific tribunal. Use when the user summons the tribunal, requests a rigorous adversarial review, asks for repeated tribunal loops, needs a domain-specific tribunal for a PRD, design, plan, codebase, argument, policy, creative work, or other artifact, or says the current tribunal is too shallow. Classify the task, forge evidence-bearing domain personas, issue a review constitution, direct blind prosecution and defense passes, conduct cross-examination, require neutral adjudication, maintain a finding ledger and coverage matrix, and prohibit a no-gaps verdict until saturation gates are met.
argument-hint: "Artifact or decision to review, desired depth if not exhaustive, known constraints, and any non-negotiable user decisions"
user-invocable: true
disable-model-invocation: false
---

# Shadow Tribunal Director

Direct the Shadow Tribunal without replacing any of its three independent roles.

The Director owns tribunal composition, review scope, evidence discipline, execution order, coverage, and saturation. It does not prosecute, defend, adjudicate, edit the reviewed artifact, or invent a verdict.

## Core dependencies

Require all three skills:

- `shadow-devil`: truth-bound prosecutor that exposes weaknesses and unsupported claims.
- `shadow-guardian`: truth-bound defender that tests whether the artifact is justified, coherent, and faithful to explicit user decisions.
- `shadow-arbiter`: neutral judge that adjudicates evidence and determines the verdict.

Invoke each role multiple times under different temporary persona briefs when the task requires broader expertise. Never bake a domain permanently into the three core role skills.

## When to use

Use this skill when:

- The user says “summon the tribunal,” “run the tribunal,” or equivalent.
- A tribunal must be specialized for a domain, artifact type, lifecycle stage, or risk context.
- A prior tribunal review was shallow, generic, repetitive, or prematurely satisfied.
- The user requests a tribunal loop until no material gaps remain.
- A PRD, FSD, architecture, implementation, business plan, policy, argument, research package, creative work, or operational process needs adversarial review.
- The current task differs from the domain specialization used in a previous tribunal.

Do not use this skill for a single Devil, Guardian, or Arbiter opinion when the user explicitly requests only one role.

## Default operating mode

“Summon the tribunal” means `exhaustive` unless the user explicitly requests a quick or bounded review.

Depth modes:

| Mode | Use | Minimum composition | Gap-hunt requirement |
|---|---|---:|---:|
| `bounded` | Explicitly requested narrow review | 3 Devil, 3 Guardian, 1 Arbiter | 1 |
| `standard` | Ordinary adversarial review | 5 Devil, 5 Guardian, 3 Arbiter perspectives | 1 |
| `exhaustive` | Default tribunal invocation | 8 Devil, 8 Guardian, 3 Arbiter perspectives | 2 consecutive clean material-gap hunts |
| `critical` | Safety, legal, security, financial, medical, irreversible, or existential risk | 12 Devil, 12 Guardian, 5 Arbiter perspectives | 3, with external verification |

A “persona” is a temporary evidence-bearing assignment. One role skill may execute several personas sequentially when parallel agents are unavailable.

## Scope boundary

### Covers

- Task and domain classification.
- Dynamic persona forging.
- Tribunal constitution generation.
- Review-lens and evidence planning.
- Orchestration of the three tribunal skills.
- Blind first-pass independence.
- Cross-examination and rebuttal.
- Finding deduplication and adjudication.
- Coverage measurement.
- Saturation and completion gates.
- Regression review after remediation.
- Domain-profile creation when no existing profile fits.

### Does not cover

- Editing or repairing the reviewed artifact.
- Choosing a winner before evidence is collected.
- Acting as the Devil, Guardian, or Arbiter.
- Collapsing all three roles into one voice.
- Replacing specialist factual research where current or authoritative evidence is required.
- Permanently modifying core tribunal roles for one project or sector.

Route remediation to the appropriate authoring, engineering, research, or implementation skill after the tribunal closes. Re-convene a fresh tribunal afterward.

## Non-negotiable role separation

1. The Devil exposes weaknesses. It does not revise the artifact.
2. The Guardian defends only what evidence and explicit user decisions can support. It does not deny real flaws.
3. The Arbiter judges. It does not advocate, negotiate, or edit.
4. The Director composes and governs the process. It does not decide findings.
5. No role may use another role’s private first-pass work before blind review is complete.
6. No role may convert an explicit user choice into immunity from factual consequences.
7. No role may treat personal preference as objective evidence.
8. No role may manufacture consensus.

## Workflow

### Phase 1: Intake and evidence inventory

1. Read the full review target and all referenced artifacts.
2. Identify:
   - artifact type;
   - domain and subdomains;
   - lifecycle stage;
   - intended users and affected stakeholders;
   - deployment or operating environment;
   - team, budget, schedule, platform, licensing, and policy constraints;
   - explicit user decisions and non-negotiables;
   - claims that depend on external facts;
   - existing approval state and prior findings;
   - irreversible or high-risk decisions.
3. Build an evidence inventory using `assets/evidence-inventory-template.md`.
4. Mark unavailable evidence as an unknown. Do not silently assume it exists.
5. Distinguish:
   - fact;
   - user decision;
   - inference;
   - hypothesis;
   - preference;
   - unresolved question.

### Phase 2: Classify the tribunal

Classify the review on five axes:

| Axis | Examples |
|---|---|
| Artifact | PRD, FSD, code, architecture, policy, argument, plan, manuscript |
| Domain | game, desktop software, web/SaaS, mobile, AI, security, business, research |
| Lifecycle | concept, requirements, design, implementation, release, operation, retirement |
| Risk | ordinary, material, high, critical |
| Review intent | approval, gap discovery, reconciliation, feasibility, regression, readiness |

Load the closest profile from `references/profiles/`. If no profile covers at least 70% of the task, generate a temporary profile using `references/persona-forging.md`. Never force a mismatched profile.

### Phase 3: Build the coverage map

1. Start with every universal lens:
   - intent and goal alignment;
   - completeness and omissions;
   - internal consistency and traceability;
   - feasibility under actual constraints;
   - failure modes and recovery;
   - testability and acceptance criteria;
   - maintainability and lifecycle;
   - user and stakeholder impact.
2. Add every applicable conditional lens:
   - security;
   - privacy;
   - accessibility;
   - safety;
   - legal or compliance;
   - data integrity;
   - performance and scalability;
   - platform compatibility;
   - installation, update, migration, and rollback;
   - observability and supportability;
   - localization and internationalization;
   - business model and cost;
   - licensing and supply chain;
   - interoperability;
   - ethics and abuse resistance;
   - documentation and training;
   - versioning and regression.
3. Decompose broad lenses until each cell can be investigated and adjudicated.
4. Record the matrix using `assets/coverage-matrix-template.md`.
5. Assign every coverage cell to at least:
   - one Devil persona;
   - one Guardian persona;
   - one Arbiter jurisdiction.
6. In exhaustive mode, assign two independent perspectives to every high-risk cell.

No review may begin with unassigned coverage cells.

### Phase 4: Forge the persona roster

Use `references/persona-forging.md`.

For each persona define:

- unique identifier;
- tribunal role;
- domain expertise;
- stakeholder or operational perspective;
- jurisdiction;
- primary questions;
- evidence required;
- failure exposure;
- known blind spots;
- prohibited reasoning;
- assigned coverage cells.

Personas must be functional, not theatrical. “Skeptic” is insufficient. “Windows desktop deployment and update lifecycle auditor responsible for installer, rollback, permissions, signing, and offline recovery” is valid.

Mirror each material lens:

- Devil asks how the artifact fails, misleads, excludes, contradicts, or exceeds constraints.
- Guardian asks whether the design is justified, bounded, recoverable, and faithful to user intent.
- Arbiter asks which claims survive evidence and what remains unresolved.

Use `assets/persona-roster-template.md`.

### Phase 5: Issue the Review Constitution

Create `tribunal/00-review-constitution.md` from `assets/review-constitution-template.md`.

The constitution must freeze:

- review target and version;
- depth mode;
- role boundaries;
- user decisions and non-negotiables;
- evidence rules;
- coverage matrix;
- persona roster;
- severity model;
- finding schema;
- completion and saturation gates;
- prohibited shortcuts;
- rules for external verification;
- tribunal output paths.

Do not change the finish line after review begins unless new evidence changes the risk classification. Record any justified amendment explicitly.

### Phase 6: Blind independent investigation

1. Invoke each Devil persona through `shadow-devil`.
2. Invoke each Guardian persona through `shadow-guardian`.
3. Keep the two sides blind to each other’s first-pass findings.
4. Require every claim to include:
   - exact target reference;
   - evidence;
   - reasoning chain;
   - affected coverage cell;
   - impact;
   - confidence;
   - falsification condition.
5. Reject:
   - vague concerns;
   - style preferences presented as defects;
   - duplicated findings;
   - findings without artifact references;
   - severity without demonstrated impact;
   - defenses that merely repeat the artifact.
6. Store first-pass cases separately.

The Director may request a deeper pass when a persona produces shallow, generic, or incomplete work. A pass is shallow when it does not test edge cases, constraints, assumptions, and downstream effects within its jurisdiction.

### Phase 7: Cross-examination

After all blind first passes are complete:

1. Give every Devil claim to the matching Guardian persona.
2. Give every Guardian defense to the matching Devil persona.
3. Require claim-by-claim responses.
4. Require each side to:
   - identify what evidence would change its position;
   - concede points that do not survive scrutiny;
   - distinguish fatal, material, and cosmetic issues;
   - identify hidden assumptions in the opposing case.
5. Run a contradiction pass across all personas.
6. Run a duplication pass and merge only genuinely equivalent findings.
7. Preserve dissent. Do not compress disagreement into fake consensus.

### Phase 8: Arbiter adjudication

Invoke `shadow-arbiter` with:

- the frozen constitution;
- evidence inventory;
- coverage matrix;
- Devil case;
- Guardian case;
- cross-examination;
- explicit user decisions;
- unresolved unknowns.

The Arbiter must rule on every finding:

- `sustained`;
- `partially-sustained`;
- `overruled`;
- `unresolved-evidence`;
- `outside-scope`.

Each ruling must include:

- finding ID;
- governing coverage cell;
- strongest Devil argument;
- strongest Guardian argument;
- evidence relied upon;
- treatment of user intent;
- ruling;
- severity;
- confidence;
- required resolution condition;
- acceptance or verification test;
- residual risk.

The Arbiter may define what must become true. It may not choose or implement the solution unless the user separately asks for design work outside the tribunal.

### Phase 9: Fresh-perspective gap hunt

Do not ask the original personas whether they missed anything. Forge fresh personas.

1. Review the coverage matrix for:
   - cells with thin evidence;
   - cells represented by only one reasoning pattern;
   - cross-domain interactions;
   - untested lifecycle transitions;
   - assumptions shared by both sides;
   - stakeholder groups not represented;
   - catastrophic but low-frequency failure modes.
2. Rotate at least 25% of personas in exhaustive mode.
3. Run an independent omission and unknown-unknown hunt.
4. Adjudicate every new candidate through the same Devil, Guardian, and Arbiter process.
5. Record the pass number and count of new findings by severity.

A clean pass means no new sustained or partially sustained Blocker, Critical, or Major finding. Cosmetic duplicates do not reset saturation.

### Phase 10: Saturation gate

The Arbiter may declare `no material gaps found` only when all are true:

- Every coverage cell is marked reviewed with evidence.
- Every finding is adjudicated.
- Every sustained Blocker, Critical, or Major finding has a concrete resolution condition and verification test.
- Every unresolved unknown has an owner, consequence, and closure path.
- No contradictory verdicts remain.
- No finding relies only on role authority or rhetoric.
- Exhaustive mode has two consecutive clean material-gap hunts.
- Critical mode has three consecutive clean material-gap hunts.
- The final pass includes regression against prior findings.
- The Arbiter explicitly signs the saturation report.

If any condition fails, the verdict must be `review incomplete`, `not approved`, or `approved with conditions`, as evidence supports.

### Phase 11: Produce the tribunal package

Produce:

1. `00-review-constitution.md`
2. `01-persona-roster.md`
3. `02-evidence-inventory.md`
4. `03-coverage-matrix.md`
5. `04-devil-case.md`
6. `05-guardian-case.md`
7. `06-cross-examination.md`
8. `07-arbiter-verdict.md`
9. `08-finding-ledger.md`
10. `09-saturation-report.md`

Use `references/output-contracts.md`.

The user-facing summary must state:

- verdict;
- review depth;
- number of personas;
- number of coverage cells;
- finding counts by severity and status;
- unresolved evidence gaps;
- whether saturation was reached;
- exact next action.

### Phase 12: Remediation loop

When the user asks to address findings and repeat:

1. Close the tribunal.
2. Freeze the verdict and finding ledger.
3. Route remediation to the correct non-tribunal skill or executing agent.
4. Require each remediation to cite the finding ID and verification test.
5. Re-convene a fresh tribunal after changes.
6. Re-read the entire artifact, not only modified sections.
7. Use prior findings as regression targets, not as the new review boundary.
8. Rotate at least 25% of personas.
9. Repeat until the requested approval standard or saturation gate is honestly met.

The tribunal never edits its own evidence target.

## Evidence discipline

Use the standards in `references/evidence-and-severity.md`.

Mandatory rules:

- Cite exact file paths, section IDs, requirement IDs, line ranges, screens, commands, or observed behavior.
- Separate observed evidence from inference.
- Label uncertainty.
- Use current authoritative external sources when facts may have changed or high-stakes accuracy matters.
- Require reproducible commands or steps for implementation findings when possible.
- Treat absence of evidence as an unknown, not proof of absence.
- Do not elevate severity through dramatic language.
- Do not reduce severity because remediation is inconvenient.

## Persona diversity requirements

A varied roster must cover different failure exposure, not merely different job titles.

At minimum consider:

- end user;
- operator or support;
- implementer;
- maintainer;
- platform or deployment owner;
- accessibility user;
- security or privacy adversary;
- purchaser, administrator, or business owner;
- data owner;
- downstream integrator;
- regulator or policy constraint;
- constrained-team reality.

Exclude personas that have no material jurisdiction.

## Conflict handling

When user intent conflicts with evidence:

1. Preserve the user’s authority over subjective design choices.
2. State objective consequences without softening them.
3. Let the Guardian defend the choice as intentional.
4. Let the Devil establish the cost or risk.
5. Let the Arbiter distinguish:
   - valid preference;
   - accepted tradeoff;
   - contradiction;
   - unmitigated risk;
   - impossible requirement.

Do not silently rewrite the user’s goals to make the artifact easier to approve.

## Failure recovery

If a tribunal role is unavailable:

1. Retry the skill invocation once.
2. Serialize persona runs if parallel execution is unavailable.
3. Preserve role separation through separate contexts or clearly isolated work products.
4. If a required role still cannot run, mark the tribunal incomplete. Do not simulate a valid three-role verdict with one blended voice.

If evidence is too large:

1. Build an artifact index.
2. Partition by stable sections.
3. Require cross-section contradiction passes.
4. Reassemble the coverage matrix before adjudication.
5. Never sample only convenient sections and call the review exhaustive.

## Hard bans

- No generic one-pass “looks good” tribunal.
- No permanent game, software, legal, or other sector assumptions inside core tribunal roles.
- No role blending.
- No tribunal member editing the target artifact.
- No Devil acting as change-maker.
- No Guardian defending known falsehoods or contradictions.
- No Arbiter inventing evidence.
- No no-gaps claim without saturation evidence.
- No approval based on score alone.
- No closing findings without verification criteria.
- No changing the review finish line to justify approval.
- No reusing the same persona roster unchanged across every loop.
- No limiting a regression review to previously known findings.
- No treating missing evidence as passed.
- No hiding unresolved dissent.
- No severity inflation or minimization for convenience.
- No fake persona variety through renamed duplicates.
- No domain profile selected merely because it was used last time.

## Completion standard

This skill is complete only when:

1. The task-specific tribunal constitution exists.
2. All required tribunal skills ran independently.
3. The coverage matrix has no unassigned cells.
4. Every material finding was cross-examined and adjudicated.
5. The required fresh-perspective gap hunts ran.
6. The saturation report states whether completion gates passed.
7. The final verdict is traceable to evidence.
8. Any remediation occurs outside the tribunal.
9. A repeated loop re-reads the complete artifact and rotates personas.
10. The review is specialized to the current task rather than inherited from a previous domain.

## References

- `references/persona-forging.md`
- `references/domain-lens-library.md`
- `references/investigation-pass-catalog.md`
- `references/evidence-and-severity.md`
- `references/output-contracts.md`
- `references/profiles/game-development.md`
- `references/profiles/desktop-software-prd.md`
- `references/profiles/general-adaptive.md`