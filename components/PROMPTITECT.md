# Promptitect

Promptitect began as prompt engineering and evolved past that boundary.

## Problem

A user often knows the outcome they want without knowing what execution architecture should exist to produce it.

Starting with "which agent should do this?" is already too late.

The correct answer may be:

- deterministic software;
- a direct tool call;
- one strong model;
- a reusable skill;
- a coding worker;
- a bounded judgment model;
- multiple independent workers;
- a human decision;
- or a hybrid.

## Principle

> Use the smallest reliable architecture capable of reaching the objective.

A component belongs only when removing it would materially increase the probability of an incorrect, incomplete, unsafe, or unusable result.

## Responsibilities

Promptitect should:

- normalize the actual objective;
- preserve hard constraints;
- identify unresolved consequential decisions;
- distinguish deterministic work from probabilistic judgment;
- select models, tools, skills, workers, or software by task fit;
- decide whether multiple agents are justified;
- request task-specific context from CCE;
- define completion evidence;
- preserve authorization boundaries;
- retry when execution failed but the pathway remains valid;
- replan when evidence says the pathway itself is wrong;
- stop when further effort is not justified.

## What changed

Early Promptitect tried to improve the prompt.

Current Promptitect tries to improve the entire path from human objective to verified outcome.

The prompt is now one compiled artifact inside a larger decision system, not the product itself.

## Deeper design

See [Promptitect Engineering Specification](../design/PROMPTITECT_ENGINEERING_SPEC_2026-09-26.md) for the audited architecture, contracts, quality governor, routing model, and verification design.
