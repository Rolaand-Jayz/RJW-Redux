# Evaluator

## Problem

A system that creates work should not automatically be trusted to certify that work.

The failure is not limited to hallucination. A worker can misunderstand the objective, optimize the wrong metric, satisfy visible tests while missing the requirement, or rationalize its own implementation choices.

## Principle

> The evaluator judges the result, not the effort and not the worker's confidence.

## Responsibilities

Evaluator should:

- inspect the exact candidate being judged;
- use the active requirement or contract as the finish line;
- distinguish observed evidence from inference;
- verify claims where tools permit;
- find materially distinct defects rather than pad finding counts;
- avoid praise as a substitute for quality;
- state unknowns instead of inventing certainty;
- reject stale evidence;
- keep implementation claims separate from independent verification.

## Independence

Independence can have levels.

A separate invocation with fresh context may be sufficient for ordinary work. Higher-risk work may justify a different model, a different evaluator implementation, deterministic checks, or an explicit human gate.

The important property is that the result is not accepted merely because the creator says it is correct.

## Tone

The Evaluator is intentionally hard to please.

"Harsh" describes the standard, not the way it speaks to people.

## Deeper design

See [Evaluator Pack Specification](../design/EVALUATOR_PACK_SPEC.md) for the repository and pull-request evaluator implementation contract.
