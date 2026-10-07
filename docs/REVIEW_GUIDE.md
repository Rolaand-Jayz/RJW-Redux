# How to Review RJW Redux

This repository is designed so a reviewer does not have to read everything.

## Three-minute path

Read:

1. [README](../README.md)
2. [Evolution](EVOLUTION.md)
3. [Architecture](ARCHITECTURE.md)
4. [Component map](COMPONENTS.md)

That is enough to understand what the method claims and how the pieces relate.

## Technical path

Then inspect:

- [Promptitect engineering specification](../design/PROMPTITECT_ENGINEERING_SPEC_2026-09-26.md)
- [Promptitect + CCE design handoff](../design/PROMPTITECT_CCE_DESIGN_HANDOFF.md)
- [Evaluator pack specification](../design/EVALUATOR_PACK_SPEC.md)
- [Tribunal director skill](../design/TRIBUNAL_DIRECTOR_SKILL.md)
- [Evidence discipline](EVIDENCE.md)

These are working design artifacts, not marketing summaries.

## Historical path

To judge whether the current system is a retrospective story or an actual evolution, inspect:

- [Lineage record](../history/README.md)
- [Historical RJW core method](../history/rjw-idd/METHOD-0001-core-method.md)
- [Historical RJW agent handbook](../history/rjw-idd/METHOD-0004-ai-agent-workflows.md)

The historical documents are preserved as evidence. They are not presented as current doctrine.

## Experimental path

Checkout the `rebrain` branch.

Rebrain is intentionally not merged into the current method yet. The branch contains the working cognitive profile and the reasoning operators extracted from historical interaction evidence.

## What to challenge

A useful review should ask:

- Are the component boundaries real or cosmetic?
- Does CCE solve context quality beyond ordinary retrieval?
- Does Promptitect actually justify architecture choices instead of defaulting to agent complexity?
- Is Evaluator meaningfully independent?
- Does Tribunal improve decisions enough to justify its cost?
- Can Rebrain be evaluated without merely testing whether a model imitates its source person?
- Which pieces should be removed?

The method should survive those questions. If it cannot, the repository should change.
