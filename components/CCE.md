# Context Curation Engine (CCE)

## Problem

Longer context is not automatically better context.

As project history grows, useful information becomes mixed with stale decisions, superseded specifications, failed approaches, duplicate facts, unrelated material, and lower-authority interpretations. A model can receive more tokens while understanding the task less clearly.

CCE treats this as an information-engineering problem rather than a prompt-writing problem.

## Principle

> More context is not the answer. Better, cleaner context is.

The target is the smallest context package that is still complete for the participant's responsibility.

## Responsibilities

CCE should be able to:

- ingest context from multiple sources;
- classify source type and authority;
- preserve provenance;
- track freshness and version;
- detect duplication;
- detect contradiction;
- identify superseded material;
- distinguish required, supporting, optional, and forbidden context;
- compile task-specific packages;
- service narrow context requests during execution;
- invalidate packages when dependent truth changes;
- assimilate durable discoveries back into project state.

## Non-goals

CCE is not:

- a generic vector-search wrapper;
- "put the whole repository in the context window";
- a summarizer that destroys provenance;
- an excuse to hide missing information behind compression.

## Context pollution

A context package can be polluted even when every individual item in it is factually correct.

Pollution occurs when information is stale, irrelevant to the current responsibility, duplicated enough to distort salience, contradictory without being marked as such, or authoritative in one scope but misleading in another.

This is why context selection and context truth are separate problems.

## Relationship to Promptitect

Promptitect decides what work should happen.

CCE decides what the participant performing that work needs to know.

That boundary is intentional.
