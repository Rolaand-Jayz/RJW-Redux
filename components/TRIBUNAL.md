# Tribunal

## Problem

Some ideas are too expensive to challenge only after implementation.

Architecture choices, major product assumptions, research interpretations, and high-leverage plans can accumulate cost quickly if the reasoning that selected them was never forced to face its strongest opposition.

## Structure

### Devil

Attacks the proposal.

It searches for unsupported assumptions, hidden failure modes, contradictions, bad incentives, missing constraints, and reasons the idea may fail.

### Guardian

Defends only what is actually defensible.

It steelmans the proposal, preserves strong ideas, and distinguishes fatal objections from fixable or non-material ones.

### Judge

Resolves the dispute.

The Judge compares both sides against evidence, constraints, authority, and the actual objective. It does not reward rhetorical force.

## Principle

> Important ideas should survive opposition before they earn implementation cost.

## Use

Tribunal is appropriate when:

- a decision would cause substantial rework if wrong;
- the evidence is contested;
- an architecture is expensive or difficult to reverse;
- a preferred idea may be receiving too much protection;
- evaluator findings and implementation reasoning materially disagree.

It should not become ceremony for routine local decisions.

## Relationship to Evaluator

Tribunal primarily challenges decisions before or during commitment.

Evaluator primarily judges completed results.

They overlap in skepticism but solve different problems.

## Deeper design

See [Tribunal Director Skill](../design/TRIBUNAL_DIRECTOR_SKILL.md) for the executable review constitution, role separation, coverage mapping, cross-examination, adjudication, and saturation loop.
