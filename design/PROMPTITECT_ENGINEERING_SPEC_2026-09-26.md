# Promptitect — Engineering Specification

**Status:** **FINAL AUDITED ENGINEERING SPEC — THREE CONSECUTIVE CLEAN LOOPS PASS**  
**Date:** 2026-09-26  
**Authority:** Current September 23 Promptitect architecture and `PROMPTITECT_SYSTEM_PROMPT_v2.md`; older Promptitect/RJ Harness materials are supporting historical sources only where explicitly incorporated here.  
**Method:** Matt Pocock `to-spec` synthesis from existing decisions; no new discovery interview.  
**Primary test seam:** Objective in → governed execution/evidence out.

---

## Problem Statement

Promptitect began as a prompt and context architect: given a human objective, it produced the smallest reliable instruction-and-context package needed for a downstream model to succeed. That behavior remains valuable, but it is now too narrow for the role Promptitect is intended to play.

The larger recurring problem is one layer above prompting. A user often knows the outcome they want but does not know which execution architecture should exist to achieve it. The correct solution may be deterministic software, a prompt, a reusable Skill, a tool call, a workflow, a coding worker, a reasoning model, a single agent, multiple agents, or a hybrid. Existing agent builders and orchestration frameworks typically begin after that decision has already been made. Promptitect must own the decision that comes before construction.

The product must therefore become a central decision and orchestration layer that:

1. converts human intent into a governed execution contract;
2. selects the smallest reliable intelligence architecture capable of accomplishing the objective;
3. distinguishes deterministic rules from probabilistic judgment;
4. routes bounded judgment to the cheapest/smallest competent decision mechanism;
5. compiles fresh task-specific context rather than accumulating context sludge;
6. allows workers to request narrowly scoped context during execution;
7. assimilates useful discoveries back into durable project state;
8. separates capability from authorization;
9. preserves provenance, freshness, authority, and supersession;
10. coordinates implementation without becoming dependent on one model vendor or one agent framework;
11. verifies outcomes rather than equating execution success with objective success;
12. replans when evidence shows that the current pathway cannot reach the required quality;
13. preserves a discoverable second semantic layer of Promptitect “wedding harness” lore inside real executable production code without compromising maintainability, security, correctness, or performance.

Promptitect must not become an architecture generator that rewards visible sophistication. Its central invariant is:

> A component belongs only when removing it would materially increase the probability of an incorrect, incomplete, unsafe, or unusable result.

The architecture must apply that rule to itself.

---

## Solution

Promptitect will be implemented as a provider-neutral **Decision Layer** surrounded by a small number of explicit contracts.

The system receives an objective plus available project state and produces an `ExecutionContract`. The contract records what must happen, what must not happen, what is known, what remains unresolved, what may be delegated, what requires human judgment, what evidence is required, what capabilities are needed, what context must be compiled, and what constitutes completion.

Promptitect chooses among deterministic logic, Jev-style bounded judgment, stronger reasoning models, tools, Skills, workers, workflows, and hybrids. It does not default to agents. Every escalation in sophistication must be justified by a requirement or observed failure.

The **Context Curation Engine (CCE)** is the authoritative context plane. Promptitect decides what needs to happen; CCE decides what each participant needs to know. CCE compiles fresh task-specific context, preserves authority and provenance, services live context requests, invalidates stale packages, and assimilates worker discoveries into durable project state.

The orchestration loop is:

```text
human objective
      ↓
intent normalization / unresolved-decision classification
      ↓
ExecutionContract
      ↓
Decision Layer
  ├─ deterministic rule
  ├─ Jev bounded judgment
  └─ deeper reasoning only when justified
      ↓
CCE context compilation
      ↓
work graph / worker execution
      ↓
evidence + discoveries
      ↓
verification
      ↓
accept / retry / replan / escalate / stop
      ↓
durable project state
```

The highest-level product seam is:

```text
Objective + Project State
          ↓
      Promptitect
          ↓
Governed Outcome + Evidence
```

All lower-level modules exist to make that seam reliable.

### Core architectural boundaries

**Promptitect Decision Layer**
- owns execution semantics;
- chooses architecture class;
- decides HITL vs AFK;
- chooses deterministic vs probabilistic handling;
- chooses worker/model/tool/Skill route;
- controls retry/replan/escalation/stop;
- owns completion judgment subject to required independent evidence.

**CCE**
- owns context compilation and delivery;
- resolves authority, provenance, freshness, conflict, duplication, and supersession;
- emits task-specific context packages;
- services live context requests;
- invalidates stale packages;
- assimilates durable discoveries.

**Jev**
- handles bounded non-deterministic judgments;
- receives compact decision capsules instead of whole transcripts;
- does not decide deterministic facts;
- does not grant authority;
- escalates when the capsule is insufficient.

**Workers**
- execute bounded tasks;
- receive fresh context at task start;
- may request more context through CCE;
- cannot silently change project truth or governing contracts;
- return evidence and discoveries in structured form.

**Verification**
- judges exact candidate outcomes against the active contract;
- remains distinct from implementation authority where independence is required;
- prevents “command succeeded” from being treated as “objective succeeded.”

**Durable Project State**
- resides primarily in repository artifacts and explicit project state, not conversational accumulation;
- contains accepted requirements, decisions, ADRs, specs, tickets, evidence, tests, and implementation facts.

---

## User Stories

1. As a user, I want to describe an outcome in ordinary language, so that I do not need to know Promptitect's internal architecture vocabulary.

2. As a user, I want Promptitect to preserve my objective and hard constraints, so that implementation convenience cannot silently redefine what I asked for.

3. As a user, I want Promptitect to distinguish what I explicitly decided from what it inferred, so that assumptions remain inspectable and reversible.

4. As a user, I want harmless ambiguity resolved automatically, so that I am not interrogated about routine engineering details.

5. As a user, I want consequential ambiguity surfaced to me, so that choices involving taste, authority, cost, irreversible action, or hard constraints remain mine.

6. As a user, I want Promptitect to decide whether digital intelligence is required at all, so that deterministic software remains a first-class solution.

7. As a user, I want Promptitect to compare materially different architecture classes, so that an agentic design is not selected merely because agents are available.

8. As a user, I want every increase in orchestration complexity justified, so that complexity has a visible reason to exist.

9. As a user, I want Promptitect to select the smallest competent architecture, so that I do not pay coordination, token, state, and debugging costs without benefit.

10. As a user, I want Promptitect to stop using a pathway when evidence shows it cannot reach the required quality, so that the system does not endlessly polish a structurally bad approach.

11. As a user, I want Promptitect to replan when assumptions, requirements, or implementation facts change, so that execution remains aligned with current truth.

12. As a user, I want Promptitect to distinguish HITL work from AFK work, so that my judgment is requested only where it is actually needed.

13. As a user, I want Promptitect to preserve protected-action boundaries, so that autonomous execution cannot grant itself permission.

14. As a user, I want availability and authorization modeled separately, so that a tool being installed does not imply permission to use it.

15. As a user, I want expensive or externally consequential actions governed by explicit authorization, so that cost and side effects remain under control.

16. As a user, I want Promptitect to work with local, remote, deterministic, and model-based capabilities, so that the architecture is not tied to one vendor.

17. As a user, I want model selection based on task fit and evidence, so that provider preference cannot replace engineering judgment.

18. As a user, I want Promptitect to choose cheap bounded decision mechanisms before expensive general reasoning when they are sufficient, so that cost and latency scale with actual difficulty.

19. As a user, I want Jev to receive only the information necessary for a bounded decision, so that its attention is not diluted by irrelevant project history.

20. As a user, I want Jev to escalate when its decision capsule is insufficient, so that bounded judgment does not become false certainty.

21. As a user, I want deterministic rules to remain deterministic, so that probabilistic judgment is not inserted into decisions code can resolve exactly.

22. As a user, I want Promptitect to record why a major route or worker was selected, so that consequential orchestration choices are auditable.

23. As a user, I want each task to begin with fresh task-specific context, so that stale assumptions from previous work do not contaminate new tasks.

24. As a user, I want context compiled for the target worker, so that different participants receive representations appropriate to their role and capability.

25. As a user, I want CCE to distinguish required, supporting, optional, and forbidden context, so that relevance alone cannot force unsafe or distracting information into a worker context.

26. As a user, I want forbidden context to override relevance, so that sensitive or unauthorized information cannot leak merely because retrieval found it useful.

27. As a user, I want context to preserve provenance, so that workers and evaluators can determine where claims came from.

28. As a user, I want context to preserve authority level, so that a model inference cannot silently override an accepted project decision.

29. As a user, I want context to preserve freshness and source version, so that stale architectural truth is detectable.

30. As a user, I want superseded context invalidated, so that obsolete decisions do not remain active accidentally.

31. As a user, I want CCE to identify contradictory context, so that conflicts are surfaced or resolved according to authority rather than flattened into a summary.

32. As a user, I want context packages to track their dependencies, so that only affected packages are rebuilt when source state changes.

33. As a user, I want a worker to request additional context during execution, so that initial context can remain small without starving implementation.

34. As a user, I want live context requests bounded by task scope, so that a worker cannot turn “need one interface” into an uncontrolled repository dump.

35. As a user, I want CCE to distinguish context starvation from worker reasoning failure, so that the system does not solve every failure by adding more context.

36. As a user, I want CCE to prefetch likely-needed context when evidence supports doing so, so that workers do not repeatedly stall on predictable dependencies.

37. As a user, I want worker discoveries classified as task-local or project-wide, so that useful new truth is retained without polluting global state.

38. As a user, I want discoveries that contradict accepted specs escalated, so that implementation cannot silently rewrite architecture.

39. As a user, I want discoveries that affect other tasks to invalidate dependent context, so that downstream workers do not operate on stale assumptions.

40. As a user, I want durable project state to live in explicit repository/project artifacts, so that correctness does not depend on hidden chat history.

41. As a user, I want accepted decisions to survive across sessions, so that project continuity does not require rereading an entire conversation.

42. As a user, I want Promptitect to preserve a provider-neutral semantic representation of execution intent, so that provider-specific adapters do not become the source of truth.

43. As a user, I want target-specific prompts, agent definitions, tool calls, or configurations treated as lowerings of canonical semantics, so that changing providers does not rewrite the objective.

44. As a user, I want Skills treated as methodology providers rather than governing authorities, so that a reusable workflow cannot override project requirements.

45. As a user, I want Promptitect to compose multiple Skills only when each contributes something necessary, so that methodology stacking does not become another form of bloat.

46. As a user, I want roles treated as responsibility contracts rather than automatically as separate model processes, so that role count does not equal agent count.

47. As a user, I want parallelism used only when dependencies and shared state make it safe, so that speed does not create merge, context, or correctness failures.

48. As a user, I want Promptitect to track evidence required for task closure, so that workers cannot declare themselves done merely because code was produced.

49. As a user, I want implementation success separated from objective success, so that a successful tool call is not confused with a successful outcome.

50. As a user, I want independent verification where the decision risk justifies it, so that high-impact work is not self-certified.

51. As a user, I want Promptitect to retry when the pathway remains valid but execution was defective, so that recoverable implementation failures do not trigger unnecessary redesign.

52. As a user, I want Promptitect to replan when failure indicates the architecture or assumptions are wrong, so that retries do not become infinite repetition.

53. As a user, I want Promptitect to escalate when the remaining decision belongs to me or requires deeper reasoning, so that autonomy stops at the right boundary.

54. As a user, I want explicit stop semantics, so that workers and workflows know when continued effort is no longer justified.

55. As a user, I want a quality contract for material deliverables, so that “good enough” has task-specific meaning.

56. As a user, I want critical quality dimensions to have independent floors, so that a strong aggregate score cannot hide a catastrophic failure in one dimension.

57. As a user, I want visible placeholders and incomplete work marked as such, so that partial output cannot masquerade as final work.

58. As a user, I want Promptitect to detect low-ceiling pathways, so that quality failures caused by the chosen method trigger a pathway change instead of superficial refinement.

59. As a user, I want the architecture to be testable through stable public seams, so that implementation can evolve without rewriting tests around internal call choreography.

60. As a developer, I want the highest-value integration test to exercise objective-in through governed-outcome/evidence-out, so that the product's actual promise is tested.

61. As a developer, I want deterministic decisions tested with deterministic fixtures, so that identical inputs produce identical policy outcomes.

62. As a developer, I want probabilistic decisions tested against frozen scenarios and acceptance boundaries, so that judgment quality can be measured without asserting exact phrasing.

63. As a developer, I want CCE package compilation replayable from recorded inputs, so that context bugs can be reproduced.

64. As a developer, I want context invalidation behavior tested from dependency changes, so that stale-package failures are detectable.

65. As a developer, I want authority-conflict tests, so that lower-authority evidence can never silently override higher-authority truth.

66. As a developer, I want prompt-injected repository or retrieved content treated as untrusted data, so that retrieved text cannot acquire governing authority.

67. As a developer, I want worker context requests recorded, so that context starvation and over-fetch behavior can be analyzed.

68. As a developer, I want execution and verification evidence bound to the exact candidate revision, so that a passing test cannot accidentally certify different code.

69. As a developer, I want architecture components subject to ablation tests, so that subsystems that do not improve outcomes can be simplified or removed.

70. As a developer, I want Jev placement subject to controlled evaluation, so that bounded-judgment calls remain only where they improve reliability enough to justify themselves.

71. As a developer, I want model routing policy replaceable, so that new models can be introduced without changing Promptitect's semantic contracts.

72. As a developer, I want provider capability facts versioned and freshness-aware, so that routing does not rely on outdated assumptions.

73. As a developer, I want the implementation language and framework subordinate to frozen contracts, so that implementation choice does not redefine product behavior.

74. As a developer, I want lore encoding isolated to deliberately selected stable production seams, so that ordinary refactors do not turn the entire codebase into a puzzle.

75. As a developer, I want lore-bearing code to remain valid, tested, maintainable production code, so that the hidden layer never becomes decorative dead code.

76. As a developer, I want the wedding-harness lore encoded through real program structure, so that the second semantic layer is genuinely part of the executable source.

77. As a developer, I want lore encoding to use legitimate identifiers, token choices, operators, layout, state transitions, or control-flow structure, so that decoding reveals a deliberate second interpretation rather than comments explaining a joke.

78. As a developer, I want the strongest lore encoding confined to small stable surfaces, so that readability and security remain acceptable.

79. As a developer, I want decoding documentation kept outside the runtime critical path and not required for program behavior, so that the machine semantics remain independent of the lore.

80. As a maintainer, I want tests that detect accidental destruction of lore-bearing invariants, so that formatting or refactors do not silently erase the second semantic layer.

81. As a maintainer, I want lore-preservation tests separate from functional correctness tests, so that the software can distinguish “program broken” from “encoded layer broken.”

82. As a user, I want internal sophistication hidden during normal use, so that I can work in outcome language instead of Promptitect jargon.

83. As a user, I want inspection available when I ask for it, so that decisions, context, evidence, and routing do not become an opaque black box.

84. As a user, I want Promptitect to remain neutral about its own methods, so that Promptitect terminology or complexity does not receive favorable treatment during evaluation.

85. As a user, I want every substantial subsystem to earn its continued existence through evidence, so that Promptitect does not become more complex than the systems it is meant to simplify.

---

## Implementation Decisions

### 1. Authority and source-of-truth hierarchy

The current September architecture governs implementation. `PROMPTITECT_SYSTEM_PROMPT_v2.md` remains the behavioral foundation. Older Promptitect Final PRDs and the RJ Harness PRD are historical design sources, not co-equal normative specifications.

When older concepts are included by this spec, their semantics are explicitly restated here. No implementation may import an older subsystem merely because it existed in the RJ Harness.

### 2. Promptitect is the Decision Layer

Promptitect is not the default implementer. It owns the semantic decision about what should happen and the contract under which execution proceeds.

Its primary artifact for material work is an `ExecutionContract`.

The contract must include, at minimum:

- objective;
- success statement;
- hard constraints;
- soft constraints;
- non-goals;
- known facts;
- unresolved facts/decisions;
- required quality/evidence;
- architecture/pathway decision;
- task/work graph;
- role/responsibility plan;
- context requirements;
- capability requirements;
- authorization requirements;
- verification requirements;
- retry/replan/escalation rules;
- stop/completion semantics;
- version/provenance binding.

The wire serialization format is an implementation choice; the semantic fields and invariants in this specification are frozen.

### 3. Minimum-sufficient architecture is normative

Promptitect must consider simpler alternatives before escalating architecture complexity.

The candidate space must allow at least:

- deterministic code;
- direct model call;
- prompt + bounded context;
- reusable Skill;
- deterministic workflow;
- LLM-assisted workflow;
- hybrid deterministic/probabilistic workflow;
- single autonomous worker;
- multi-worker architecture;
- orchestrated distributed execution.

This is not a maturity ladder.

A more complex candidate may be selected only when the simpler candidate is insufficient against an explicit requirement, hard constraint, evidence obligation, or demonstrated failure mode.

### 4. Complexity justification contract

Every material escalation must record:

- the simpler alternative;
- the requirement or observed failure it cannot satisfy;
- the expected benefit of the added component;
- the added burden: latency, cost, state, permissions, coordination, context, maintenance, or evaluation;
- an ablation/falsification condition that could prove the escalation unnecessary.

### 5. Deterministic before probabilistic where possible

Deterministic mechanisms should own:

- schema validation;
- type/reference integrity;
- graph consistency;
- hard policy;
- authorization enforcement;
- capability-state checks;
- cache invalidation predicates;
- source-version checks;
- dependency bookkeeping;
- contract-version matching;
- exact stop conditions where formally expressible.

Probabilistic mechanisms may own:

- ambiguous intent interpretation;
- bounded relevance judgment;
- sufficiency judgment;
- architecture tradeoff reasoning;
- semantic conflict analysis;
- worker/model fit;
- pathway quality assessment;
- adversarial critique.

Probabilistic output must not silently become authority.

### 6. Jev is the bounded-judgment layer

Jev is eligible at every material non-deterministic decision point, but no Jev call exists merely because one is possible.

A Jev request must use a `DecisionCapsule` with:

- decision type;
- bounded facts/features;
- valid choices;
- relevant constraints;
- optional evidence references;
- confidence/sufficiency contract;
- escalation rule.

The capsule should prefer dense structured features before prose.

Jev cannot:
- grant capabilities;
- alter hard constraints;
- create authorization;
- overwrite accepted project truth;
- certify objective completion without the required evidence.

### 7. Progressive decision-context expansion

Jev and other decision mechanisms begin with the smallest useful capsule.

If confidence/sufficiency is below the required threshold:

1. add narrowly relevant evidence;
2. retry the bounded decision;
3. escalate to deeper reasoning or HITL only if still unresolved.

The system must not default from “uncertain” to “send the whole project.”

### 8. CCE is the context compiler and live broker

CCE has eight logical responsibilities:

- Collector;
- Resolver;
- Curator;
- Compiler;
- Planner;
- Broker;
- Cache;
- Assimilator.

These are logical responsibilities, not necessarily eight runtime services or classes. The implementation should merge responsibilities where doing so preserves the contracts and reduces complexity.

### 9. Canonical Context Unit

All durable/retrievable project context that may participate in compilation must be representable as a `ContextUnit`.

A Context Unit must carry enough metadata to determine:

- stable identity;
- source identity;
- source version/hash;
- provenance;
- authority level;
- sensitivity/authorization class;
- freshness;
- applicability/scope;
- supersession state;
- conflict relationships where known;
- content or content reference.

### 10. Context inclusion classes

Every candidate context item can be classified as:

- `REQUIRED`
- `SUPPORTING`
- `OPTIONAL`
- `FORBIDDEN`

`FORBIDDEN` wins over relevance.

An unauthorized item cannot become model-visible merely because retrieval or semantic ranking rates it highly.

### 11. Context authority is orthogonal to relevance

CCE must keep authority and relevance as separate dimensions.

A high-relevance, low-authority model inference cannot override a lower-relevance explicit user requirement.

The default precedence order is:

1. external/platform safety and authorization controls;
2. explicit current user intent and explicit protected-action approval;
3. accepted project constitution/profile constraints;
4. canonical requirements, ADRs, and accepted decisions;
5. accepted verified project evidence;
6. methodology/Skill defaults;
7. retrieved project/external content;
8. model hypotheses and suggestions.

Same-level conflicts require explicit resolution behavior; lower levels cannot silently overwrite higher levels.

### 12. Fresh context per task

Every executable task begins with a newly compiled `TaskContextPackage`.

Workers must not inherit unrelated accumulated history from previous tasks.

A package binds to:
- task identity/version;
- relevant ExecutionContract version;
- relevant project-state versions/hashes;
- included Context Unit identities;
- compilation policy/version.

### 13. Project Control Capsule

CCE should maintain or compile a compact `ProjectControlCapsule` containing the project truths that govern multiple tasks, such as:

- objective;
- accepted hard constraints;
- current architectural decisions;
- authority boundaries;
- active quality floor;
- relevant glossary/domain semantics;
- current spec/ticket versions;
- prohibited actions/context.

Task packages reference this material without requiring the full project corpus.

### 14. Live context request protocol

Workers can issue a bounded context request after execution begins.

A request must state:

- task identity;
- what information is missing;
- why it is needed;
- desired depth or evidence type;
- affected decision/implementation step;
- optional known symbols/files/entities.

CCE responds with:
- granted context;
- omitted/forbidden items;
- provenance;
- authority;
- freshness;
- package revision;
- reason for denial or partial grant;
- follow-up/escalation state if necessary.

A worker cannot directly demand an unrestricted repository dump through this interface.

### 15. Context budget is an optimization objective, not a fixed token target

The objective is minimum sufficient context for reliable execution.

Workers may express desired depth such as `minimal`, `normal`, or `deep`, but CCE owns the actual package.

The compiler optimizes for:
- sufficiency;
- authority correctness;
- relevance;
- freshness;
- attention efficiency;
- provider context limits;
- cost/latency where material.

### 16. Context dependency graph and invalidation

Compiled packages must track the source state that their conclusions depend on.

Dependency examples include:
- file hash/revision;
- ADR version;
- spec version;
- ticket version;
- commit/branch;
- accepted project decision;
- policy version;
- capability record version.

When a dependency changes, only affected packages/decisions should be invalidated.

Cached judgments may be reused only when the normalized capsule and all relevant dependency/policy versions remain valid.

### 17. Bidirectional assimilation

Worker discoveries return through CCE and are classified:

- task-local fact;
- durable project fact;
- hypothesis;
- contradiction;
- superseding evidence;
- dependency-impacting discovery.

Durable assimilation cannot silently modify higher-authority truth.

A discovery that contradicts an accepted spec/ADR must escalate rather than self-merge into project truth.

A discovery that changes assumptions for dependent tasks must trigger dependency invalidation.

### 18. Distinguish context starvation from reasoning failure

The system must maintain explicit failure classification sufficient to distinguish at least:

- missing context;
- stale context;
- conflicting context;
- worker reasoning failure;
- implementation defect;
- pathway/architecture failure;
- capability mismatch;
- authorization block;
- external/tool failure.

“Give the worker more context” is not an acceptable universal recovery strategy.

### 19. Canonical semantic representation

Promptitect must maintain a provider-neutral semantic layer for consequential architecture/execution decisions.

Provider-specific prompts, agent manifests, tool configurations, workflow files, and model settings are lowerings/projections.

The implementation may evolve the prior Architecture IR concept into a narrower execution-oriented IR if that is sufficient, but provider artifacts must not become the canonical source of truth.

### 20. Role is not process

A role is a responsibility and authority contract.

One model/process may satisfy multiple roles if independence is not required.

Separate execution contexts are required only where:
- independence is part of the evidence contract;
- information barriers are required;
- authority separation requires it;
- parallelism materially improves time-to-quality.

This prevents role proliferation from becoming agent proliferation.

### 21. Skill Fabric remains provider-level

Skills/methodologies are versioned providers.

A Skill may define:
- domain;
- preconditions;
- required context;
- required capabilities;
- expected outputs;
- verification hooks;
- known conflicts;
- source/trust;
- version;
- license where applicable.

A Skill cannot override:
- hard constraints;
- accepted project decisions;
- authority;
- protected-action rules;
- quality floors;
- required independent verification.

### 22. Capability Registry/Broker remains a logical contract

Promptitect must be able to reason over capabilities without hardcoding model/vendor assumptions.

A capability descriptor should represent:
- capability identity/type;
- availability;
- modality;
- platform/hardware constraints;
- authorization state;
- cost class;
- latency class;
- context/tool limits;
- known limitations;
- source/version/freshness;
- measured domain performance where available.

Provider marketing and empirical results remain distinguishable.

### 23. Pathway search is conditional, not universal ceremony

For material, quality-critical, architecture-changing, unknown-root-cause, or new-subsystem work, Promptitect should consider materially distinct solution pathways unless a path is deterministically required.

Potential pathway classes include:
- current local capability;
- alternate methodology;
- alternate model/worker;
- existing tool or open-source component;
- deterministic technique;
- custom automation/tool creation;
- hybrid human/model/tool execution.

The system should stop broad pathway search when:
- a path is proven sufficient;
- remaining alternatives cannot plausibly improve the decision enough to justify more search;
- active search/resource bounds are reached;
- user or policy constraints rule alternatives out.

### 24. Pathway ceiling detection

Promptitect must distinguish:
- defective execution on a viable path;
- a path whose plausible quality ceiling is below the required target.

The first permits retry/refinement.

The second requires replan/pathway change.

Repeated refinement without evidence of a reachable quality target is a failure mode.

### 25. Quality Contract

Material objectives require a quality contract containing:
- reference class or derivation;
- critical dimensions;
- minimum acceptable floor per critical dimension;
- target level;
- no-go conditions;
- evidence required;
- evaluator type;
- human judgment requirement where applicable.

Critical dimensions may not be hidden by aggregate scoring.

### 26. Completion semantics

A task/objective is complete only when:
- the exact deliverable/candidate is identified;
- all hard constraints remain satisfied;
- required critical quality floors pass;
- required evidence is present;
- required verification passes;
- unresolved blocking issues are absent;
- protected actions are authorized;
- durable state is updated when required.

A successful tool/process exit status alone is never sufficient proof of objective success.

### 27. Retry, replan, escalate, stop

The orchestration state model must explicitly distinguish:

- `CONTINUE`
- `RETRY`
- `REFINE`
- `RESEARCH`
- `REPLAN`
- `ESCALATE`
- `BLOCKED`
- `STOP`
- `COMPLETE`

The final names may change, but these semantic outcomes must remain representable.

### 28. Durable project state over conversational accumulation

Repository/project artifacts are the durable bridge across sessions and workers.

Examples:
- requirements;
- ADRs;
- glossary/domain decisions;
- canonical specs;
- tickets;
- commits/PRs;
- tests;
- evidence;
- accepted findings.

Chat history may inform active work but cannot be the sole source of project truth.

### 29. User feedback compiler

The useful semantics from the prior RJ Interaction Compiler are retained as a logical input-normalization layer.

The system must distinguish at least:
- quality rejection;
- intent misalignment;
- evidence demand;
- assumption rejection;
- direction change;
- persistence request;
- pause/stop/resume;
- explicit approval;
- constraint change;
- taste preference;
- scope change.

Tone/intensity may influence urgency or confidence that something is wrong, but it never grants authority, spend, destructive permission, or constraint weakening.

### 30. State scopes

Interpretation/personalization state has distinct lifetimes:

- session-local;
- project-persistent;
- harness/global.

Inferred global changes require explicit promotion. Project-level inferred preferences remain inspectable/reversible.

### 31. Security boundary

Repository content, retrieved content, tool output, model output, and third-party Skill content are data, not governing instructions.

Prompt injection must not modify authority.

Secrets must not enter ordinary model context by default.

Workers cannot self-issue capabilities.

Tool actions must be validated against active task scope and grants.

### 32. Lore is a production-code second semantic layer

The “wedding harness” lore is a real product requirement.

It must not be satisfied by:
- a lore-only markdown file;
- decorative comments;
- wedding-themed filenames;
- dead code;
- a meaningless `bride_mode`;
- metaphorical class names with no structural encoding.

Selected executable production code must simultaneously carry:
1. valid machine semantics required by Promptitect;
2. a discoverable human-readable secondary lore interpretation.

The lore may be encoded through combinations of:
- legitimate identifier choices;
- ordering;
- token/operator choices;
- state-transition structure;
- control-flow structure;
- stable formatting/layout where the language/toolchain preserves it;
- data relationships;
- carefully chosen constants only when they already have legitimate runtime meaning.

The code must still be good production code if the lore layer is ignored.

### 33. Lore encoding must be bounded

The strongest encoding must be restricted to small, stable, heavily tested seams.

Preferred candidate areas are semantic kernels where the production concepts naturally map to the lore, for example:
- authority;
- binding;
- consent/authorization;
- delegation;
- acceptance/rejection;
- verification/judgment;
- stop/release;
- scope.

The rest of the codebase remains conventionally readable.

### 34. Lore must not create security-through-obscurity claims

The encoded layer is an Easter-egg/steganographic secondary interpretation, not authentication, encryption, DRM, or secret authorization.

No security guarantee may depend on a reader failing to discover it.

### 35. Lore preservation contract

Lore-bearing code receives two independent test categories:

**Functional tests**
- prove runtime behavior.

**Lore integrity tests**
- prove the secondary encoding remains decodable according to the frozen encoding contract.

A formatting/refactoring change may break lore integrity without breaking product behavior; that must be reported separately.

### 36. Local Harness Fitting Room

A small local evaluation harness should exist once the core orchestration path works.

It is for controlled comparison of Promptitect configurations, including:
- context strategy;
- Jev placement;
- model routing;
- worker count;
- retries/replans;
- token/context consumption;
- latency;
- quality;
- failure rate;
- complexity.

A subsystem remains required only when removing/merging it produces a material regression against frozen scenarios.

This fitting room is not required to sit in the production critical path.

### 37. No Agent Builder dependency

The architecture must not require a paid API-only visual Agent Builder environment.

Promptitect should work with the user's available local/subscription/coding tooling where feasible and remain provider-neutral.

### 38. Implementation freedom

Exact programming language, framework, persistence engine, queue system, CLI framework, or UI toolkit are implementation choices unless later frozen by an ADR.

The contracts in this spec are authoritative over convenience choices.

### 39. Normative vocabulary and conformance

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** express normative strength. Earlier lower-case “must/must not/should/may” statements retain their plain-language normative meaning; capitalization is not a loophole for ignoring an explicit requirement. Where two statements differ in strength, the more specific later frozen contract governs.

An implementation conforms only when:
- every MUST/MUST NOT behavior is implemented and externally testable at the highest practical seam;
- every persisted canonical object satisfies its field contract and version rules;
- provider-specific lowering cannot silently change canonical semantics;
- unresolved runtime facts are represented explicitly rather than guessed;
- implementation freedom does not alter authority, context, evidence, completion, or lore semantics.

### 40. Canonical identity, version, and provenance rules

Every consequential canonical object MUST carry:
- `id`: stable identity for the logical object;
- `version`: monotonically increasing object revision or immutable revision identifier;
- `schema_version`: contract version used to interpret the object;
- `created_at`;
- `source/provenance`: origin sufficient to reconstruct why the object exists;
- `status`: active, superseded, invalidated, rejected, or other type-specific state;
- `content_hash` where canonicalized content can be hashed deterministically.

Historical accepted objects MUST be superseded rather than silently rewritten. References between canonical objects MUST target stable IDs plus the revision/version required by the contract.

### 41. Canonical `ExecutionContract`

Every material objective MUST compile to one active `ExecutionContract`. Required semantic fields are:

- identity/version/provenance fields from Decision 40;
- `objective`;
- `success_statement`;
- `hard_constraints[]`;
- `soft_constraints[]`;
- `non_goals[]`;
- `known_facts[]` with evidence/provenance refs;
- `unresolved_items[]` with owner class (`AFK`, `HITL`, `RESEARCH`) and blocking state;
- `quality_contract_ref`;
- `architecture_decision` containing selected architecture class and rejected materially simpler alternatives;
- `work_graph` containing task IDs and dependency edges;
- `role_bindings[]`;
- `context_requirements[]`;
- `capability_requirements[]`;
- `authorization_requirements[]`;
- `evidence_requirements[]`;
- `verification_requirements[]`;
- `retry_replan_escalation_policy`;
- `stop_conditions[]`;
- `completion_conditions[]`;
- `binding_versions` for governing project/spec/policy state.

A contract is `EXECUTABLE` only when no blocking unresolved item remains and required authorization preconditions for the next executable step are satisfiable. It may still contain non-blocking unknowns when their treatment is explicit.

### 42. Canonical `DecisionCapsule` and `DecisionRecord`

A `DecisionCapsule` MUST contain:
- `decision_type`;
- `decision_id`;
- `facts[]` as compact typed facts/features;
- `choices[]` or an explicitly open decision domain;
- `constraints[]`;
- `evidence_refs[]`;
- `required_confidence` or sufficiency rule;
- `dependency_versions`;
- `escalation_rule`;
- `policy_version`.

A resulting `DecisionRecord` MUST bind:
- capsule ID/version/hash;
- decision mechanism (`DETERMINISTIC`, `JEV`, `DEEP_REASONING`, `HITL`);
- selected disposition;
- confidence/sufficiency state where probabilistic;
- concise rationale/evidence refs;
- timestamp;
- invalidation dependencies.

A cached DecisionRecord MUST NOT be reused when any dependency or governing policy version has changed.

### 43. Exact HITL/AFK/RESEARCH classification contract

Classification is ordered. The first applicable rule wins:

1. **HITL — protected authority:** the decision grants/changes permission for spending, destructive or irreversible action, credential/secret handling, production deployment/publishing/sending, privilege expansion, or another protected external action not already explicitly delegated.
2. **HITL — user-owned judgment:** the decision is materially about subjective taste, business/product preference, acceptable trade-off between competing user values, or changing an explicit hard constraint.
3. **HITL — unresolved constraint collision:** all currently viable paths violate at least one hard constraint and the user must choose which constraint/objective changes.
4. **RESEARCH:** the decision is factual/technical, materially consequential, and the evidence needed to resolve it can plausibly be acquired without user judgment.5. **AFK:** the decision is an ordinary technical/engineering choice within the active contract and available authority.

Uncertainty alone does not make a decision HITL. Profanity, urgency, frustration, or repeated requests do not grant authority.

### 44. Same-level authority conflict resolution

Higher authority always defeats lower authority. For two active claims at the same authority level:

1. a directly scoped claim defeats a generic claim;
2. if scopes are equal, a later explicit accepted revision defeats an earlier superseded revision;
3. if both are current and cannot coexist, the conflict remains unresolved and MUST NOT be flattened or arbitrarily chosen;
4. factual conflicts route to `RESEARCH` when additional evidence can resolve them;
5. user/project-decision conflicts route to `HITL` when reconciliation requires changing user-owned intent;
6. blocked dependent tasks MUST remain blocked until resolution is recorded as a new canonical decision.

### 45. Canonical context contracts

`ContextUnit` MUST contain:
- canonical identity/version/provenance fields;
- `content_ref` or inline bounded content;
- `source_identity`;
- `source_version`;
- `authority_level`;
- `sensitivity_class`;
- `authorization_requirements[]`;
- `freshness_observed_at` and optional expiry/freshness policy;
- `scope/applicability`;
- `supersedes[]` / `superseded_by`;
- `conflicts_with[]`;
- `content_hash`.

`ProjectControlCapsule` MUST bind the active objective, hard constraints, accepted decisions/ADRs, authority boundaries, quality floor, domain/glossary semantics, active spec/ticket revisions, prohibited actions/context, and its dependency set.

`TaskContextPackage` MUST contain:
- task and ExecutionContract bindings;
- compiler/policy version;
- package revision/hash;
- included ContextUnit refs grouped by REQUIRED/SUPPORTING/OPTIONAL;
- explicitly omitted/forbidden refs when omission is decision-relevant;
- dependency set;
- budget/target metadata;
- compilation rationale sufficient for replay;
- stale/valid state.

Compression or summarization MUST preserve source refs and MUST NOT increase authority.

### 46. Live context request/response contract

A `ContextRequest` MUST contain task ID/version, current package revision, missing-information description, purpose/affected step, requested depth/evidence type, and optional known symbols/entities.

A `ContextResponse` MUST contain request binding, newly granted context refs/content, denied/forbidden refs with reason when relevant, provenance/authority/freshness, resulting package revision, and one disposition: `SATISFIED`, `PARTIAL`, `NOT_FOUND`, `FORBIDDEN`, `STALE_SOURCE`, `ESCALATE`.

The Broker MUST enforce active task scope and authorization before content becomes worker-visible. Repeated substantially identical requests without new evidence MUST contribute to reasoning-failure classification rather than unlimited context expansion.

### 47. Worker task/result/discovery contract

A worker receives a `WorkerTaskContract` containing task ID/version, objective, bounded scope, allowed actions/capabilities, TaskContextPackage ref, expected artifact/result type, evidence obligations, stop conditions, and parent ExecutionContract binding.

A `WorkerResult` MUST contain:
- task/version binding;
- candidate artifact/revision refs;
- status (`SUCCEEDED`, `PARTIAL`, `FAILED`, `BLOCKED`);
- produced evidence refs;
- discoveries[];
- assumptions introduced;
- actions actually taken;
- remaining blockers;
- context requests made;
- exact candidate identity/hash where applicable.

A `Discovery` MUST declare proposed class (`TASK_LOCAL_FACT`, `DURABLE_FACT`, `HYPOTHESIS`, `CONTRADICTION`, `SUPERSEDING_EVIDENCE`, `DEPENDENCY_IMPACT`) plus evidence/provenance. CCE/Promptitect owns acceptance into durable state.

### 48. Completion and verification binding

A `VerificationReceipt` MUST bind to:
- ExecutionContract ID/version;
- task/objective ID;
- exact candidate artifact/revision/hash;
- exact test/evaluator/quality-contract versions;
- evidence refs;
- critical-dimension results;
- hard-constraint result;
- verifier identity/type and independence class;
- timestamp;
- disposition (`PASS`, `FAIL`, `INCONCLUSIVE`).

`COMPLETE` is permitted only when every required receipt is `PASS` for the exact candidate and contract versions, no blocking unresolved item remains, and required durable-state updates have committed successfully. `INCONCLUSIVE` MUST NOT be treated as PASS.

### 49. Execution state machine

The orchestration state MUST be representable as:

```text
INTAKE → CONTRACTING → READY → EXECUTING → VERIFYING → COMPLETE
                     ↘ BLOCKED ↗        ↘ REPLAN ─────┘
                         ↘ ESCALATED
                         ↘ STOPPED
```

`RETRY` and `REFINE` are transitions back into execution on the same viable pathway. `RESEARCH` is a bounded evidence-acquisition subflow that returns to the blocked decision. `REPLAN` creates a new architecture/work-plan revision while preserving the prior one. `STOPPED` is terminal unless an explicit resume/control event creates a new active run revision.

### 50. Context starvation vs reasoning failure contract

A failure is `CONTEXT_STARVATION` only when all are true:
- the worker identifies a specific missing fact/interface/dependency;
- that information is relevant and authorized;
- CCE can locate or plausibly acquire it;
- possession of it could materially change the blocked step.

A failure is `REASONING_FAILURE` when sufficient relevant context is already present and the worker repeats the same faulty inference/implementation, issues repeated equivalent requests, or cannot use the supplied evidence correctly.

`STALE_CONTEXT`, `CONFLICTING_CONTEXT`, `CAPABILITY_MISMATCH`, `IMPLEMENTATION_DEFECT`, `PATHWAY_FAILURE`, `AUTHORIZATION_BLOCK`, and `EXTERNAL_FAILURE` remain distinct dispositions. The recovery policy MUST branch on this classification rather than treating all failures as missing context.

### 51. Canonical semantic IR boundary

V1 MUST retain a compact provider-neutral **Execution IR** rather than the full historical Architecture IR. The Execution IR is the canonical machine-readable projection of the active ExecutionContract and MUST represent at least:
- requirements/constraints;
- unresolved items;
- selected architecture/pathway;
- tasks/dependencies;
- roles;
- context requirements;
- capability/authorization requirements;
- evidence/verification requirements;
- stop/completion semantics;
- provenance/version bindings.

Provider prompts/manifests/configurations are lowerings from this IR. A lowering MUST report unsupported semantics instead of silently dropping or changing them.

### 52. Capability and Skill persistence boundary for v1

V1 does **not** require a large autonomous registry service. It MUST expose stable descriptor interfaces for `CapabilityDescriptor` and `SkillDescriptor`, and MAY initially load them from versioned configuration/adapters. Persist measured capability evidence only when it affects routing or future reproducibility.

This decision prevents registry infrastructure from entering the critical path before it earns its complexity.

### 53. Minimum viable Harness Fitting Room

The v1 Fitting Room is an offline/replay evaluation harness, not a production service. It MUST be able to:
- run the same frozen scenario against two or more configuration variants;
- bind each run to Promptitect/policy/model/context-strategy versions;
- collect objective correctness, hard-constraint compliance, evidence completeness, quality-floor results, user-correction count where simulated/available, retries/replans, latency/TTQ, token/context consumption, and stale/unauthorized-context failures;
- emit a comparison record and ablation disposition;
- replay without granting production-side effects.

Anything beyond that is deferred until measured need exists.

### 54. Frozen lore-bearing seam and encoding constraints

V1 MUST place the strongest wedding-harness encoding in **one small semantic kernel at the boundary between decision disposition and governed execution**, because that seam naturally contains binding, authority, delegation, judgment, acceptance/rejection, and release/stop semantics.

The exact source file/module name is implementation choice, but the seam MUST:
- execute on the normal production path;
- contain no dead-code carrier;
- remain understandable without decoding lore;
- expose ordinary tests for machine semantics;
- expose a separate deterministic lore decoder/integrity fixture;
- use only behavior-preserving choices among already legitimate identifiers/order/operators/control-flow/layout;
- avoid runtime secrets, hidden permissions, or values whose only purpose is encoding;
- be exempted narrowly from automatic refactors/formatters only where the lore contract requires stable syntax;
- fail lore-integrity tests without falsely reporting product-functional failure.

The frozen secondary narrative for v1 is the **wedding harness transition**: Promptitect moves from supporting other systems to binding and directing governed execution, while itself remaining bound by authority, evidence, scope, judgment, and release/stop conditions. Exact prose encoding is an implementation artifact, but its semantic beats MUST be recoverable in that order from the frozen decoder.

### 55. Capability grants and protected-action enforcement

A capability being known or available MUST NOT make it executable. Runtime authority is represented by an explicit `CapabilityGrant` bound to:
- grantee task/worker ID and version;
- capability descriptor ID/version;
- permitted operation set;
- resource/scope boundaries;
- read/write/execute/network classification as applicable;
- secret-handle access, never raw secret values by default;
- monetary/external-side-effect ceiling where applicable;
- grant issuer/authority source;
- expiry/revocation conditions;
- protected-action approval ref when required.

Tool/action dispatch MUST validate the proposed operation against both the active `WorkerTaskContract` and `CapabilityGrant`. Workers and model output cannot mint, widen, or renew their own grants.

Protected approval is action-specific. Approval of one deployment, send, purchase, destructive change, or credential action MUST NOT generalize to adjacent actions unless the user's explicit grant says so.

### 56. Canonical `QualityContract` and `PathwayCandidate`

A `QualityContract` MUST contain:
- contract ID/version;
- objective/reference-class binding;
- critical dimensions with individual floor and target;
- no-go conditions;
- required evidence;
- evaluator/verifier requirements;
- human-judgment requirement where applicable;
- placeholder/incompleteness policy;
- pathway-ceiling criteria;
- aggregation method only for non-critical summary reporting.

A critical-dimension failure MUST fail the contract regardless of aggregate score.

A material `PathwayCandidate` MUST record:
- pathway class and description;
- hard-constraint compliance state;
- predicted attainable quality and confidence;
- expected TTQ/latency and resource/cost class;
- capability/context dependencies;
- risk/reversibility;
- reuse value where material;
- evidence supporting the estimate;
- disposition (`VIABLE`, `NON_VIABLE`, `SELECTED`, `REJECTED`, `UNKNOWN`).

Pathway search MAY be omitted only when an existing rule/contract deterministically mandates the path or the work is below the configured materiality threshold. The omission reason MUST be recordable.

### 57. Verification independence policy

Verification independence is risk-based, not ceremonial. Each evidence requirement declares one of:
- `SELF_CHECK_ALLOWED`;
- `SEPARATE_CONTEXT_REQUIRED`;
- `SEPARATE_MODEL_OR_PROCESS_REQUIRED`;
- `HUMAN_REQUIRED`;
- `DETERMINISTIC_CHECK_REQUIRED`;
- a composition of the above.

At minimum, separate-context or stronger independence MUST be used when the implementer could plausibly hide its own defect through interpretation, when protected external effects are involved, when a critical quality dimension is subjective/high-impact, or when the active QualityContract requires it.

The verifier MUST NOT receive an implementer-generated PASS as authoritative evidence. It may receive implementation artifacts and factual evidence, but owns its disposition independently.

### 58. Durable-state commit, concurrency, and recovery semantics

Canonical project state MUST use compare-and-swap/version preconditions or an equivalent mechanism so a writer cannot silently overwrite a newer accepted revision.

A durable mutation MUST record an append-only `StateEvent` containing actor/task, prior object version, proposed/new version, reason, evidence refs, timestamp, and outcome.

When a state mutation spans repository/Git state and Promptitect's ledger/index, the operation MUST be recoverable. The system MUST record intent before the external mutation and a completion/rollback/reconciliation event afterward. Startup/recovery logic MUST detect incomplete mutations and either complete them safely or restore/retain the last known trusted state.

Parallel tasks MUST NOT write the same canonical object revision concurrently without conflict detection. Independent tasks MAY run in parallel when their declared write sets and dependency graph do not overlap materially.

### 59. User interruption and contract revision semantics

`PAUSE`, `STOP`, `RESUME`, `DIRECTION_CHANGE`, `SCOPE_CHANGE`, `CONSTRAINT_CHANGE`, and explicit `APPROVAL` are first-class control events.

A material user change MUST:
1. create a new intent/ExecutionContract revision rather than rewriting history;
2. compute impact across active tasks, context packages, cached decisions, capability grants, pathway selection, and verification obligations;
3. cancel, supersede, block, or recompile affected work;
4. preserve unaffected work only when dependency analysis demonstrates independence;
5. revoke grants that are no longer valid under the new contract.

`PAUSE` prevents new side effects while preserving recoverable state. `STOP` prevents new execution and moves active work to a safe stopped disposition. `RESUME` MUST bind to the current contract revision rather than blindly continuing stale work.

### 60. Lowering conformance and semantic-loss reporting

Every provider/worker lowering from the Execution IR MUST produce a `LoweringReport` that records:
- target provider/surface/capability versions;
- canonical semantics represented directly;
- semantics represented approximately;
- unsupported semantics;
- required external enforcement not expressible in the target;
- adapter assumptions;
- compatibility/freshness evidence.

Unsupported or approximate handling of a hard constraint, authorization boundary, critical context rule, or completion requirement MUST block executable-ready status unless an external deterministic enforcement path is explicitly bound. Silent semantic loss is prohibited.

### 61. Normative document authority

For implementation of Promptitect v1, authority among project documents is:

1. higher-priority platform/safety/legal controls that actually govern the runtime;
2. explicit current user authorization and current accepted project constraints for the active objective;
3. this **Final Audited Engineering Spec** once its clean-loop gate passes;
4. accepted project ADRs that narrow an implementation choice without contradicting this spec;
5. `PROMPTITECT_SYSTEM_PROMPT_v2.md` for original prompt/context behavior not superseded or narrowed by this spec;
6. September 23 handoff as design provenance;
7. older Promptitect/RJ Harness documents as historical reference only.

An ADR MAY choose among implementation freedoms but MUST NOT silently weaken a frozen semantic contract. A contradiction between this spec and a historical source is resolved in favor of this spec.

### 62. Materiality classification

A decision/objective/task is `MATERIAL` if any of the following is true:
- it changes the selected architecture/pathway or a canonical contract;
- it can affect a hard constraint or critical QualityContract dimension;
- it grants, consumes, or changes protected authority/capabilities;
- it causes externally visible, irreversible, destructive, costly, publishing/sending/deployment, credential, or secret-related effects;
- it changes durable project truth used by other tasks;
- it crosses subsystem/task boundaries such that an error can invalidate dependent work;
- it determines completion/verification for a material objective;
- failure would require user-visible rework or rollback beyond the local task.

Everything else is `LOCAL` unless policy explicitly raises its class. Materiality MUST be recorded when it changes pathway-search, verification-independence, evidence, or authorization requirements.

### 63. Jev is a logical bounded-judgment capability, not an irreplaceable provider

`Jev` names the bounded-judgment role in this architecture. A concrete Jev implementation/provider is selected through the Capability Broker.

If the preferred Jev capability is unavailable, unauthorized, incompatible, or empirically below the active requirement, Promptitect MUST choose one of:
- a deterministic rule if the decision can be made exactly;
- another compatible bounded-judgment provider;
- deeper reasoning with the same DecisionCapsule semantics;
- HITL when the decision is user-owned or no competent authorized reasoning path remains.

The `DecisionRecord` MUST record the actual mechanism/provider used. The architecture MUST NOT fail solely because one named Jev provider is absent unless the active project explicitly requires that provider.

### 64. Minimum context sensitivity classes

Every ContextUnit MUST use at least one of these sensitivity classes:
- `PUBLIC`: safe for any authorized project participant/provider;
- `PROJECT`: ordinary non-public project information;
- `RESTRICTED`: may be exposed only to explicitly authorized roles/providers/tasks;
- `SECRET`: secret values/credentials/keys; excluded from ordinary model context and accessed only through approved secret-handle/tool boundaries.

A deployment MAY define stricter subclasses, but MUST preserve these minimum semantics. Sensitivity is independent from authority and relevance. Compression, retrieval, or model output MUST NOT downgrade sensitivity.

---

## Testing Decisions

### Testing philosophy

Tests must target externally meaningful behavior and stable contracts rather than implementation choreography.

The preferred seam is the highest one that can prove the behavior:

> **objective + project state → governed outcome + evidence**

Lower-level tests exist only when they protect semantics that cannot be diagnosed cleanly from the top seam.

Avoid tests that assert:
- exact internal method call order;
- exact prompt wording;
- exact number of internal model calls unless that is itself a contract;
- class/module decomposition;
- incidental serialization formatting outside canonical schemas;
- internal implementation names.

### 1. End-to-end Decision Layer tests

Frozen scenarios must prove that materially different objectives produce the appropriate architecture class.

Fixtures must include cases where the correct answer is:
- deterministic only;
- direct model call;
- prompt + context;
- Skill;
- workflow;
- coding worker;
- hybrid;
- multiple workers.

Tests must fail if Promptitect escalates complexity without a recorded reason.

### 2. Architecture ablation tests

For every subsystem designated `REQUIRED`, controlled ablation must answer:

> What materially breaks if this component is removed or merged?

Disposition:
- KEEP;
- SIMPLIFY;
- REMOVE;
- INCONCLUSIVE.

`INCONCLUSIVE` cannot be treated as KEEP.

### 3. Deterministic policy tests

Fixtures must prove stable behavior for:
- authority precedence;
- capability vs authorization;
- forbidden-context blocking;
- version matching;
- stale-package invalidation;
- protected-action gates;
- dependency invalidation;
- stop conditions that are formally deterministic.

Same input + same policy version must produce the same result.

### 4. Jev decision tests

Use frozen decision capsules with expected acceptable decision sets rather than exact prose.

Test:
- correct bounded choice;
- escalation under insufficient evidence;
- refusal to decide deterministic facts as judgment;
- refusal to grant authority;
- sensitivity to narrowly added evidence;
- absence of regression when irrelevant prose is removed.

Ablate Jev placements. Keep only placements that materially improve quality/reliability.

### 5. CCE compilation tests

Given identical:
- project state;
- task;
- policy version;
- source versions;

the compiler must produce semantically equivalent context packages.

Tests must cover:
- required context inclusion;
- optional context exclusion under budget;
- forbidden context exclusion;
- provenance preservation;
- authority preservation;
- freshness;
- supersession;
- conflict surfacing;
- compression without authority inflation.

### 6. Context dependency/invalidation tests

Change one source dependency and assert:
- affected package invalidates;
- unrelated package remains valid;
- cached Jev decisions invalidate only when their dependency capsule/policy becomes stale.

### 7. Live context broker tests

Workers must be able to request narrowly scoped additional context.

Fixtures must test:
- valid narrow request;
- overbroad request;
- unauthorized request;
- request for superseded context;
- request where information does not exist;
- repeated request that indicates reasoning failure rather than starvation.

### 8. Assimilation tests

Worker discoveries must be correctly classified:
- local;
- durable;
- hypothesis;
- contradiction;
- supersession;
- cross-task dependency change.

A worker inference must not overwrite an explicit accepted decision.

### 9. HITL/AFK tests

Fixtures must cover:
- ordinary engineering choice → AFK;
- subjective taste choice → HITL;
- protected external action → HITL/approval;
- hard-constraint collision → HITL;
- recoverable technical ambiguity → AFK;
- insufficient evidence with material consequence → research/escalation.

### 10. Pathway ceiling tests

Provide scenarios where:
- current path has a correctable defect;
- current path structurally cannot meet the quality floor.

Promptitect must refine/retry the first and replan the second.

### 11. Verification independence tests

For risk classes that require independent verification:
- implementer output alone cannot close the task;
- verifier/evidence must bind to the exact candidate revision;
- stale or mismatched evidence fails closure.

### 12. Objective-success tests

Include cases where:
- command succeeds but objective is not recovered;
- implementation builds but critical quality dimension fails;
- tests pass on a different revision;
- output appears complete but contains unresolved placeholders.

All must remain non-complete.

### 13. Prompt injection / authority tests

Retrieved or repository text must be unable to:
- change authority order;
- grant capabilities;
- disable verification;
- mark itself REQUIRED by instruction;
- approve protected actions;
- rewrite the ExecutionContract.

### 14. Provider replacement tests

Swap one model/provider/capability descriptor while holding canonical semantics constant.

The system should require only bounded adapter/routing changes, not a rewrite of project intent or contracts.

### 15. Lore functional tests

Lore-bearing code must pass all ordinary functional tests with no special runtime mode.

Deleting the lore decoder/documentation must not change production behavior.

### 16. Lore integrity tests

A frozen decoder/specification must verify the intended second semantic layer from the actual production source.

Tests should detect:
- destructive auto-formatting;
- identifier refactor;
- control-flow simplification;
- token/operator change;
- ordering change;

only where that element participates in the encoding.

Lore tests must not freeze unrelated code.

### 17. Lore maintainability test

A reviewer unfamiliar with the lore should still be able to understand the production behavior of the lore-bearing module without decoding the Easter egg.

If the code becomes materially harder to maintain solely for the encoding, simplify the encoding.

### 18. Fitting Room comparative tests

After the core path works, compare:
- CCE on/off or simplified variants;
- Jev at candidate decision points;
- alternate context budgets;
- alternate model routing;
- worker-count variants.

Metrics:
- objective correctness;
- hard-constraint compliance;
- evidence completeness;
- critical quality pass rate;
- number of user corrections;
- retries/replans;
- latency/time-to-quality;
- token/context use;
- unauthorized-action rate;
- stale-context failures.

Optimization must prefer reliability/quality first, then time/cost among solutions that meet the floor.

---

## Out of Scope

This specification does not require:

- a universal visual agent builder;
- a full IDE;
- arbitrary desktop automation;
- autonomous global self-modification;
- a marketplace for third-party Skills;
- support for every operating system in v1;
- enterprise-wide IAM implementation;
- provider hosting;
- a hosted Promptitect control plane;
- mandatory paid API services;
- exhaustive search over every theoretically possible solution;
- maximizing agent count;
- maximizing parallelism;
- maximizing token use;
- preserving every subsystem from the historical RJ Harness;
- implementing the historical Devil/Guardian/Judge Tribunal as mandatory runtime architecture;
- implementing a large Evaluator Mesh unless risk/evidence proves it necessary;
- treating prior PRDs as co-equal normative authorities;
- relying on chat history as durable project state;
- hiding security-sensitive behavior through lore or obfuscation;
- making the entire repository lore-encoded;
- sacrificing maintainability, correctness, security, performance, or tooling compatibility for the second semantic layer;
- requiring a human to decode the lore for ordinary operation;
- using wedding-themed names as a substitute for the executable encoding requirement.

---

## Further Notes

### A. Canonical project principle

The entire system should remain reducible to:

> **Promptitect decides the smallest reliable way to accomplish the objective, gives each participant the minimum sufficient authorized context, and requires evidence that the objective was actually achieved.**

Everything else must justify itself against that sentence.

### B. Product lineage

Promptitect's original prompt/context architecture is not deprecated. It becomes one lowering of the Decision Layer.

A prompt is now one possible architecture output rather than the product boundary.

### C. Current authority boundary

The current architecture deliberately supersedes the older monolithic RJ Harness topology.

However, the following older concepts have been explicitly retained because they support the current design:
- Execution Contract semantics;
- authority precedence;
- Context Units/Capsules;
- Skill/provider separation;
- capability descriptors;
- pathway ceiling detection;
- quality contracts;
- verification independence;
- interaction-feedback signal taxonomy;
- state scopes;
- ablation discipline.

Anything else from older documents remains historical until separately re-adopted.

### D. Lore intent

The wedding-harness layer is not decorative branding. It is a deliberate dual-semantics engineering artifact.

The machine reads legitimate production logic.

A human who knows the decoding scheme can discover the lore.

The preferred artistic constraint is that the lore should arise from concepts Promptitect genuinely implements — authority, binding, delegation, consent/authorization, judgment, acceptance, rejection, stop/release — rather than forcing unrelated metaphors into identifiers.

### E. Spec-to-tickets gate

The previously unresolved pre-ticket questions are now frozen by Implementation Decisions 39–54: canonical object contracts, HITL/AFK/RESEARCH classification, same-level conflict handling, dependency invalidation, failure classification, exact verification binding, the compact Execution IR boundary, v1 adapter-level Capability/Skill persistence, the minimum Fitting Room, and the lore-bearing seam.

This specification may proceed to `to-tickets` only after the recorded adversarial audit reaches **three consecutive clean loops** with no new material implementation ambiguity, authority/security defect, contract gap, or testability blocker. Editorial improvements do not reset the clean-loop count unless they alter semantics.

The first dependency-aware tracer-bullet ticket sequence begins with the smallest end-to-end vertical slice:

```text
objective
→ ExecutionContract
→ one deterministic/Jev decision
→ CCE package
→ one worker
→ worker result
→ verification
→ durable accepted state
```

That vertical slice should prove the architecture before broad subsystem expansion.


---

## Audit Closure

**Audit result:** THREE CONSECUTIVE CLEAN LOOPS — PASS.

The audit hardened the candidate specification until no new material implementation ambiguity, authority/security defect, contract gap, stale-state/recovery defect, semantic-loss path, or testability blocker was found in three consecutive unchanged semantic passes.

The clean-loop gate is therefore satisfied. This document is ready for dependency-aware `to-tickets` decomposition.