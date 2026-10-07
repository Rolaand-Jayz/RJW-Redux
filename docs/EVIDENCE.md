# Evidence Discipline

The method treats fluent explanation as weak evidence.

## Evidence classes

Keep these distinct:

1. **Observed** - directly inspected, measured, or reproduced.
2. **Documented** - stated by a primary or authoritative source.
3. **Inference** - supported by evidence but not directly observed.
4. **Hypothesis** - a live explanation that remains testable.
5. **Speculation** - useful search-space material with little or no evidentiary weight.
6. **Unknown** - not established.

A plausible inference must not silently become a fact.

## Authority

When sources conflict, resolve the conflict instead of averaging them into a smooth narrative.

A typical engineering order is:

1. explicit current user decisions and protected constraints;
2. accepted requirements and governing contracts;
3. observed behavior at the exact revision under review;
4. reproducible tests and measurements;
5. current implementation and configuration;
6. current documentation;
7. historical documentation;
8. model inference.

The exact order may change by task, but it should be explicit when the difference matters.

## Context

Relevant does not mean authoritative.

Authoritative does not mean relevant.

Fresh does not mean correct.

Large does not mean complete.

CCE exists because context quality depends on several dimensions at once.

## Verification

Execution success is not objective success.

A command returning zero, a worker saying "done," a generated artifact existing, or a CI job passing can all be necessary without being sufficient.

Verification should target the actual objective and bind evidence to the exact candidate being accepted.

## Contradictions

Do not erase contradictory evidence to make the history cleaner.

Preserve what was believed, what evidence supported it, what contradicted it, what changed the conclusion, and what remains unresolved.
