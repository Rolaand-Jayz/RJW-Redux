# Promptitect + CCE: Design Handoff for Continued Ideation

## Purpose of This Document

This document captures the current vision for a future system that fuses **Promptitect** with the most valuable parts of the **Context Curation Engine (CCE)**.

It is intended to be given to a fresh AI conversation whose job is to continue designing the system.

This is not an evaluation, a scorecard, a test plan, or a release checklist. It is a design handoff for open-ended ideation.

The goal is to preserve the concept accurately while leaving room for the next conversation to challenge assumptions, improve the architecture, name missing layers, and turn the vision into a coherent system design.

---

# 1. Origin of the Idea

## Promptitect

Promptitect began as a prompt-engineering system designed to convert a user’s objective into a strong prompt for GPT-5.5 and the GPT-5.6 family.

Its central philosophy is that modern models usually benefit from:

- outcome-first instructions
- only the context that materially affects the task
- clear constraints
- clear evidence boundaries
- clear output expectations
- clear completion conditions
- minimal unnecessary scaffolding
- model and harness awareness
- freedom for the model to choose its own method when the method does not need to be prescribed

Promptitect has continued to evolve beyond its early versions. The current concept is stronger than a simple prompt improver, but it is still far from the final form described here.

## CCE

The Context Curation Engine was an earlier and more programmatic concept.

The valuable idea behind the CCE was not documentation or prompt-writing rules. It was the ability to deterministically:

- ingest context
- classify it
- organize it
- rank it
- resolve authority
- detect duplication
- identify conflicts
- track freshness
- preserve provenance
- compress it
- package it for a specific task

The CCE’s purpose was to construct the best possible context package for whatever an agent needed to do.

Unlike a conversational prompt improver, the CCE was imagined as software infrastructure.

## The Fusion

The final system should fuse the two ideas.

Promptitect becomes the conversational and semantic interface.

CCE becomes the programmatic context runtime.

The result is not merely a prompt generator and not merely a retrieval system.

It becomes the interface between a human objective and one or more agents capable of completing the objective from end to end.

---

# 2. Core Vision

The final system is a conversational control layer that allows a person to speak naturally to an agent system without manually constructing prompts, gathering context, selecting models, coordinating tools, or managing agent handoffs.

The user describes what they want.

The system determines:

- the actual objective
- the desired final state
- the work required
- which agents or models should perform each part
- what context each agent needs
- what prompt each agent should receive
- what tools each agent may use
- what state must be preserved
- what actions require approval
- how outputs should be verified
- when the work is complete

The user normally does not see the generated prompts.

The user normally does not see the complete internal context packages.

The user interacts with one coherent chat interface.

The hidden system performs prompt engineering, context engineering, model routing, orchestration, and state management behind that interface.

A concise description is:

> A conversational operating layer that translates human intent into optimized agent execution by generating task-specific prompts and immaculate context packages invisibly.

Another possible description is:

> An intent-to-execution context operating system.

These are working descriptions, not final names.

---

# 3. The Defining Standard

The defining capability of the system should be:

> Every agent receives exactly the instructions and context it needs for its current task—nothing essential omitted, nothing irrelevant included, nothing authoritative misclassified, and nothing silently distorted.

This is more important than merely creating short prompts.

The real optimization target is not minimum token count by itself.

The target is:

- minimum wasted model attention
- minimum redundant context
- minimum reconstruction work
- maximum task relevance
- maximum source integrity
- maximum clarity of execution
- maximum continuity across an end-to-end task

A longer context package may be correct when the task genuinely requires it.

A short context package may be correct when the task is tightly bounded.

The ideal package is the smallest package that is still complete for the agent’s responsibility.

---

# 4. What the User Experience Should Feel Like

The user should feel as though they are talking to one capable system.

They should not need to think in terms of:

- system prompts
- user prompts
- agent roles
- retrieval chunks
- context windows
- embeddings
- model tiers
- tool schemas
- multi-agent orchestration
- approval-state machines
- provenance records
- context compression
- prompt templates

The user should be able to say something such as:

> Review the repository, determine why deployment is failing, fix it, update the documentation, and prepare a pull request.

The system should handle the hidden work:

1. Understand the real objective.
2. Inspect the available environment.
3. Break the objective into dependent tasks.
4. Decide which steps require code agents, research agents, deterministic software, or direct reasoning.
5. Ask the CCE for the exact context needed for each step.
6. Generate the best prompt for each agent and model.
7. Control tool access and approval boundaries.
8. Track state as work progresses.
9. Verify outputs.
10. Recover from failures or reroute work.
11. Present one coherent result to the user.

The user should only be interrupted when their input is genuinely necessary.

---

# 5. High-Level Architecture

A possible architecture is:

```text
Human
  ↓
Conversational Interface
  ↓
Intent and Objective Interpreter
  ↓
Task and Execution Planner
  ↓
Agent / Model / Tool Router
  ↓
Context Requirement Generator
  ↓
CCE Context Runtime
  ↓
Agent-Specific Context Package
  ↓
Invisible Prompt Compiler
  ↓
Selected Agent or Model
  ↓
Tool Execution
  ↓
Verification and State Update
  ↓
Next Task, Recovery Path, or Final Response
```

The system should not be forced into this exact diagram if a better architecture emerges.

The important separation is between:

- understanding the human
- planning the work
- determining context requirements
- curating context programmatically
- compiling agent instructions
- executing work
- preserving state
- returning a coherent result

---

# 6. Promptitect’s Role in the Fused System

Promptitect becomes more than a prompt writer.

It becomes the semantic control layer.

Its responsibilities may include the following.

## 6.1 Human Intent Interpretation

Promptitect determines:

- what the user actually wants
- what artifact, decision, action, or state should exist at the end
- what matters most
- what is optional
- what can be inferred
- what requires clarification
- what would count as failure
- what completion looks like

It should preserve the user’s real objective rather than substitute a more convenient or familiar task.

## 6.2 Task Decomposition

Promptitect converts the objective into an executable structure.

That structure may include:

- tasks
- subtasks
- dependencies
- parallel work
- sequential work
- decision points
- approval gates
- tool needs
- model needs
- completion states
- fallback paths
- escalation conditions

The planning depth should match the task.

A simple request should not become an elaborate workflow.

A complex end-to-end objective should not be flattened into one vague prompt.

## 6.3 Agent and Model Routing

Promptitect chooses the most suitable execution unit for each task.

Possible execution units include:

- GPT-5.5
- GPT-5.6 Sol
- GPT-5.6 Terra
- GPT-5.6 Luna
- coding agents
- research agents
- document agents
- image systems
- deterministic software
- specialized tools
- isolated subagents
- future models or runtimes

Routing should consider:

- task complexity
- ambiguity
- consequence of failure
- context volume
- tool requirements
- autonomy
- duration
- latency
- cost
- throughput
- need for judgment
- need for strict structure

The models should not be treated as requiring fundamentally different prompt languages.

The same core semantic contract should be adapted through:

- scope
- context density
- autonomy
- decomposition
- verification
- runtime settings
- tool permissions
- output strictness

## 6.4 Context Requirement Definition

Promptitect should not retrieve context blindly.

It should determine what the current task needs.

For example:

```text
Provide:
- the current deployment architecture
- the most recent relevant failures
- environment-specific constraints
- approved infrastructure decisions
- unresolved conflict between documentation and implementation
- the files most likely to control the failure
```

This context request is then fulfilled by the CCE.

Promptitect decides what information would make the agent successful.

CCE determines which exact context objects satisfy that need.

## 6.5 Prompt Compilation

Promptitect generates the hidden prompt or instruction package for each agent.

The prompt should be derived from:

- the current objective
- the agent’s task boundary
- the curated context
- the target model
- the target harness
- available tools
- risk and approval rules
- dependencies
- the required output
- the completion condition

The final prompt should be model-native, concise where possible, and complete where necessary.

## 6.6 Execution Governance

Promptitect controls:

- what each agent is responsible for
- what it is allowed to access
- what it may change
- what requires approval
- what it must verify
- what it must return
- when it should stop
- when it should escalate
- what information should be passed to the next agent

## 6.7 User Communication

Promptitect converts internal execution into one understandable conversation.

The user may receive:

- a necessary clarification
- a decision requiring approval
- a meaningful progress update
- an explanation of a blocker
- the completed outcome

The user should not receive internal machinery unless they ask for inspection, debugging, or transparency.

---

# 7. CCE’s Role in the Fused System

CCE is the programmatic context runtime.

Its purpose is not to produce a bag of semantically similar chunks.

Its purpose is to construct the best possible context package for the current agent and task.

## 7.1 Ingestion

CCE may ingest:

- files
- conversations
- repositories
- databases
- documents
- policies
- source code
- research
- tool output
- execution logs
- prior decisions
- generated artifacts
- user preferences
- project state
- agent outputs

Ingestion should preserve original source identity and lineage.

## 7.2 Semantic and Structural Segmentation

The system should not rely only on arbitrary fixed-size chunks.

Different information should become different kinds of context objects.

Examples:

- requirement
- decision
- source claim
- code function
- class
- API contract
- error trace
- policy clause
- user preference
- unresolved question
- historical artifact
- superseded instruction
- generated summary
- tool result

Segmentation should respect the natural operational unit of the information.

## 7.3 Classification

Every context object should have metadata describing what it is.

Possible fields include:

```text
id
content
source
type
authority
freshness
scope
entities
dependencies
task relevance
sensitivity
confidence
supersession state
provenance
```

Possible types include:

```text
governing instruction
task fact
requirement
decision
authoritative evidence
supporting evidence
example
style reference
user assertion
hypothesis
tool result
historical record
unverified claim
embedded instruction
```

## 7.4 Authority and Supersession

CCE must understand that two relevant sources may not be equally authoritative.

Examples of possible precedence:

```text
current explicit user instruction
approved project decision
current specification
official documentation
current implementation
historical design note
generated summary
unverified claim
```

Authority may be domain-specific rather than globally fixed.

A repository implementation may describe what the software currently does.

A specification may describe what it is supposed to do.

A later approved decision may supersede both.

CCE should preserve these distinctions instead of flattening them.

## 7.5 Relevance Selection

Retrieval should be task-aware rather than similarity-only.

Selection may consider:

- direct relevance
- causal relevance
- authority
- freshness
- uniqueness
- dependency value
- contradiction value
- execution impact
- cost of omission
- sensitivity
- agent permission
- context budget

A context object should be included because it changes what the agent should know or do.

## 7.6 Conflict Detection and Preservation

CCE must detect disagreements among:

- requirements
- decisions
- documentation
- implementation
- user instructions
- historical records
- external sources
- generated summaries

It should not merge conflicting sources into false consensus.

A good context package may explicitly state:

```text
Conflict:
- The current specification requires X.
- The implementation performs Y.
- Decision record Z may explain the divergence.
- No later approval resolving the conflict was found.
```

This allows the agent to act intelligently without rediscovering the conflict from raw documents.

## 7.7 Deduplication

CCE should remove:

- exact duplicates
- near duplicates
- repeated restatements
- superseded copies
- redundant summaries

It should preserve duplicates only when their repetition or source diversity is itself meaningful.

## 7.8 Compression

Compression should reduce repetition without losing:

- facts
- numbers
- exceptions
- qualifications
- causal relationships
- uncertainty
- dependencies
- disagreement
- provenance
- source identity

Compression should be deterministic whenever possible.

Model-assisted compression should be used when semantic judgment is necessary.

Derived summaries should remain traceable to their original sources.

## 7.9 Context Packaging

CCE should return a structured package rather than unordered chunks.

A possible package is:

```text
context_package:
  governing_context
  task_context
  evidence_context
  dependencies
  conflicts
  uncertainties
  source_map
  excluded_context
  freshness_status
  compression_notes
```

The exact format can evolve.

The central requirement is that the package be organized around execution.

## 7.10 State Integration

After an agent acts, CCE should update the persistent state.

Possible updates include:

- new decisions
- changed files
- resolved conflicts
- unresolved failures
- created artifacts
- new source relationships
- new task dependencies
- superseded information
- changed relevance
- verification results

This allows future agents to receive current context without replaying the entire history.

---

# 8. Agent Execution Packages

Every agent should receive a purpose-built package for its current responsibility.

A possible package contains:

```text
Objective
Task Boundary
Current State
Governing Instructions
Curated Context
Source Map
Tools and Permissions
Dependencies
Output Contract
Completion Condition
Escalation Conditions
```

## Objective

The exact result the agent must produce.

## Task Boundary

What belongs to the agent and what does not.

## Current State

Only the project or task state needed for the current step.

## Governing Instructions

The rules that outrank the rest of the package.

## Curated Context

The smallest complete body of useful information.

## Source Map

Where material facts, requirements, and decisions came from.

## Tools and Permissions

What the agent may inspect, change, execute, send, publish, or delete.

## Dependencies

Inputs from prior agents, tools, decisions, or external processes.

## Output Contract

What the agent must return and in what form.

## Completion Condition

The observable condition that means the task is complete.

## Escalation Conditions

The conditions requiring:

- clarification
- user approval
- rerouting
- another agent
- more context
- failure recovery
- termination

---

# 9. Invisible Prompt Engineering

The generated prompts are infrastructure.

They should normally remain hidden from the user.

The user should not be forced to review prompt syntax unless they want to.

An inspection or development mode may expose:

- the generated prompt
- the context package
- routing decisions
- task decomposition
- source authority
- exclusions
- assumptions
- agent handoffs

This is useful for:

- debugging
- design work
- auditing
- reproducing execution
- manual intervention
- advanced users
- system improvement

The normal interface should remain outcome-oriented.

---

# 10. Invisible Context Engineering

The user should not have to manually rebuild context.

They should be able to say:

> Use the authentication decisions we approved, but ignore the abandoned design from last month.

The system should determine:

- which decisions were approved
- which design was abandoned
- what superseded it
- whether current implementation conflicts with the approved direction
- which information the next agent actually needs

The user should be able to refer naturally to project history without acting as the retrieval system.

---

# 11. Deterministic First, Generative Where Necessary

The fused system should not use a model for work that ordinary software can perform more reliably and cheaply.

## Good candidates for deterministic handling

- hashing
- exact deduplication
- file lineage
- permissions
- timestamps
- recency comparison
- metadata filtering
- schema validation
- token budgeting
- source access control
- known-source precedence
- state transitions
- dependency tracking
- exact structured extraction
- artifact indexing
- content addressing
- caching
- change detection

## Good candidates for model-assisted handling

- implicit intent
- semantic relevance
- nuanced contradiction analysis
- difficult source classification
- task decomposition
- conceptual compression
- synthesis
- prompt construction
- adaptive planning
- judgment under ambiguity
- natural-language communication

The boundary should remain pragmatic.

Some tasks may use both deterministic and model-assisted passes.

---

# 12. Token and Efficiency Model

The CCE’s programmatic nature is a major advantage.

The system may still incur costs for:

- storage
- indexing
- embeddings or other representations
- retrieval
- optional model-assisted classification
- optional model-assisted compression
- the final context sent to an agent

However, it can avoid repeatedly spending model tokens on:

- rereading irrelevant files
- reconstructing project state
- rediscovering source authority
- detecting the same duplicates
- resolving known conflicts again
- parsing full conversation histories
- sending every source to every agent
- repeatedly summarizing unchanged material

The system should pay to understand information once, preserve that understanding structurally, and reuse it.

The goal is not zero token use.

The goal is that every token sent to a model has a reason to be there.

---

# 13. Persistent Knowledge and Working State

The system may need to distinguish several forms of memory.

## Source Memory

Original files, documents, code, messages, records, and external material.

## Semantic Memory

Structured facts, entities, relationships, requirements, decisions, and concepts derived from sources.

## Episodic Memory

What happened during previous tasks and agent executions.

## Decision Memory

Approved choices, rejected alternatives, reasons, owners, and supersession.

## Working State

The current task graph, open dependencies, approvals, errors, agent outputs, and next actions.

## User Preference Memory

Stable preferences that should affect future interaction or artifact generation.

These forms of memory should not be collapsed into one undifferentiated conversation history.

---

# 14. End-to-End Task Execution

The system should support tasks that continue until a real outcome exists.

A possible lifecycle is:

```text
understand objective
identify required final state
inspect available environment
build task graph
determine agent and tool needs
request curated context
compile agent execution package
execute task
verify result
update state
choose next task
repeat
deliver final outcome
```

The system should distinguish:

- generating a plan
- generating instructions
- performing the work
- verifying that the work succeeded

It should not claim completion merely because it generated a plausible answer or plan.

---

# 15. Human Control and Approval

The system should remain capable of autonomous execution while respecting meaningful approval boundaries.

Possible action classes include:

## Read-Only

Inspection, search, analysis, retrieval, and diagnosis.

## Reversible Modification

Edits that can be rolled back or restored.

## External Communication

Messages, posts, pull requests, publications, and notifications.

## Financial or Privileged Action

Purchases, transfers, permissions, account changes, secrets, and administrative actions.

## Destructive or Irreversible Action

Deletion, irreversible migration, destructive deployment, or permanent external effect.

Approval requirements should be based on consequence, not arbitrary tool categories.

The user should not be asked for confirmation repeatedly when they have already authorized a clearly defined scope.

---

# 16. Source Integrity

The system must preserve the difference between:

- what a source literally says
- what the system inferred
- what an agent concluded
- what the user decided
- what was verified
- what remains uncertain

The context package should make these distinctions available to agents.

The system should never silently turn:

- a guess into a fact
- a summary into an authoritative source
- an old decision into a current decision
- an example into a requirement
- retrieved content into a governing instruction
- a model-generated statement into verified knowledge

---

# 17. Security and Trust Boundaries

Because the system ingests arbitrary context, it must distinguish data from instructions.

Files, web pages, repository content, tool output, quoted prompts, and prior agent messages may contain instructions that are not authorized to govern the system.

The architecture should define:

- instruction authority
- data authority
- agent permissions
- tool permissions
- source permissions
- user permissions
- isolation boundaries
- secret handling
- context visibility
- cross-agent leakage controls

This should be solved structurally rather than by adding increasingly elaborate warning text to prompts.

---

# 18. The Role of Rules and Documentation

The earlier Rolaand Jayz Wayz toolbox contained rules and documentation standards.

In the fused system, the valuable rules should become implemented behavior.
Examples:

- authority rules become context metadata and resolution logic
- documentation standards become artifact contracts
- prompt rules become compiler behavior
- context rules become CCE algorithms
- task-state rules become orchestration logic
- approval rules become execution policy
- provenance rules become source lineage

The product should enforce the doctrine instead of requiring the user to remember it.

Documentation remains useful for maintainers, but documentation is no longer the main mechanism of control.

---

# 19. What This System Is Not

It is not merely:

- a prompt improver
- a prompt library
- a Custom GPT
- a chatbot
- a vector database
- a RAG wrapper
- a multi-agent framework
- a workflow engine
- a context-window optimizer
- a memory plugin
- a tool router
- a project manager

It may contain aspects of all of them.

Its central identity is:

> A system that compiles human intent and accumulated knowledge into agent-specific execution environments.

---

# 20. Open Design Questions for the Next Conversation

The following questions are intentionally unresolved.

They should be explored rather than answered automatically.

## Product Identity

- What is the best name for the fused system?
- Should Promptitect remain the product name, the interface name, or one internal component?
- Should CCE remain a named subsystem?
- Is “intent-to-execution context operating system” the right category?

## Core Abstractions

- What is the canonical task object?
- What is the canonical context object?
- What is the canonical agent execution package?
- What is the canonical task graph?
- What is the canonical project-state representation?
- Which abstractions must remain model-independent?

## Context Model

- How should authority be represented?
- How should supersession work?
- How should contradictory sources be stored?
- How should relevance be computed?
- How should context be budgeted?
- How should compression preserve fidelity?
- How should context packages differ by agent type?
- What should be indexed once versus derived on demand?

## Prompt Compilation

- What is the minimum semantic representation needed before rendering?
- How should prompts differ by harness?
- What should remain hidden?
- When should the user be able to inspect or override generated prompts?
- How should the system represent output and completion contracts?

## Orchestration

- How are tasks decomposed?
- How does the system decide between one agent and many agents?
- How are dependencies represented?
- How are failed tasks retried, repaired, or rerouted?
- How are agent outputs merged into persistent state?
- How does the system avoid unnecessary agent proliferation?

## Model Routing

- What characteristics belong in the model capability registry?
- How should the router balance quality, cost, latency, and risk?
- How should the system respond when model capabilities change?
- When should deterministic software replace a model call?
- When should one model review another?

## User Interaction

- When should the system ask a question?
- When should it infer?
- How much progress should the user see?
- How should approvals be requested?
- How should the system communicate uncertainty?
- How should advanced users inspect or modify internal execution?

## Persistence

- What should be remembered permanently?
- What should expire?
- What should remain task-local?
- How should abandoned ideas be marked?
- How should approved decisions supersede earlier discussion?
- How should privacy and deletion work?

## Security

- How are untrusted instructions contained?
- How are secrets detected and protected?
- How are agent permissions enforced?
- How is data isolated between users, projects, and agents?
- How are external actions authorized?

## Implementation Path

- What is the smallest architecture that preserves the final vision?
- Which parts should be programmatic first?
- Which parts require models?
- What can be built around the existing Promptitect?
- What parts of the old CCE design can be recovered?
- What should be prototyped before deeper infrastructure is built?
- What should remain conceptual until the core abstractions are stable?

---

# 21. Guidance for the Next AI Conversation

The next conversation should operate as a design partner.

It should:

- treat this as open ideation
- preserve the ambition of the concept
- challenge weak assumptions
- identify missing architectural layers
- distinguish product vision from implementation detail
- avoid reducing the idea to a conventional RAG system
- avoid reducing the idea to a prompt generator
- avoid treating testing as the definition of the design
- avoid forcing a premature implementation stack
- avoid adding complexity for its own sake
- separate deterministic infrastructure from model judgment
- look for the simplest architecture capable of supporting the final vision
- maintain the distinction between user-visible conversation and invisible execution machinery
- help turn the concept into a coherent system design

The next conversation should not begin by scoring the concept.

It should begin by understanding it, improving it, and deciding what must be designed first.

---

# 22. Suggested Opening Prompt for the New Conversation

Use this document as the complete design handoff for a system that fuses Promptitect with the Context Curation Engine.

Do not evaluate or score the idea. Work as a product architect, systems designer, and ideation partner.

First, restate the system in your own words to confirm the concept without shrinking it into a prompt generator, RAG wrapper, or ordinary multi-agent framework.

Then identify:

1. the essential product identity,
2. the minimum set of core subsystems,
3. the canonical data structures the system needs,
4. the boundaries between deterministic software and model-based judgment,
5. the most important unresolved architectural decisions,
6. the best sequence for finishing the design.

Preserve the core vision: one conversational interface translates human intent into end-to-end agent execution, while a programmatic context engine invisibly curates the exact prompt and context package needed by every agent at every step.

Treat this as pure design work. Do not make test coverage, benchmarks, or release validation part of the definition of the ideal system.