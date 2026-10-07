# RJW Redux

**RJW Redux** is the public successor to **Rolaand Jayz Wayz - Intelligence Driven Development (RJW-IDD)**.

It is not a rebrand of the old methodology and it is not a claim that the current system existed in finished form from the beginning.

It is the record of what happened after using RJW on real projects, finding where it worked, finding where it broke down, and repeatedly changing the method around those failures.

The result is now a set of distinct components:

- **CCE** controls context quality.
- **Promptitect** decides how an objective should be attacked.
- **Evaluator** independently judges completed work.
- **Tribunal** adversarially challenges important ideas before commitment.
- **Rebrain** is an experimental branch exploring whether reusable reasoning operators can be combined with a base model's native strengths without turning the result into a persona.

The method is not built around "more agents."

It is built around using the **smallest reliable system** that can reach the objective, giving each participant the **cleanest context it actually needs**, and refusing to treat execution as proof of success.

## Core ideas

A few principles show up everywhere in the method:

> More context is not the answer. Better, cleaner context is.

> A component belongs only when removing it would materially increase the chance of an incorrect, incomplete, unsafe, or unusable result.

> A worker saying it is finished is not evidence that the objective was achieved.

> Important ideas should survive opposition before they earn implementation cost.

> Exploration can be broad. Belief still has to be earned.

## Repository map

- [Evolution](docs/EVOLUTION.md)
- [Component map](docs/COMPONENTS.md)
- [Evidence discipline](docs/EVIDENCE.md)
- [Context Curation Engine](components/CCE.md)
- [Promptitect](components/PROMPTITECT.md)
- [Evaluator](components/EVALUATOR.md)
- [Tribunal](components/TRIBUNAL.md)
- [RJW lineage and historical snapshots](history/README.md)

Rebrain is intentionally being developed on a separate `rebrain` branch while its claims and boundaries are still being tested.

## Lineage

RJW Redux descends from the private repository `Rolaand-Jayz/Rolaand-Jayz-Wayz-IDD`.

The historical source revision used to seed this public record is:

`608e27182aa88184db54deb335487f4c2150f059`

The original repository was created on **September 29, 2025**. Selected source documents from that revision are preserved under `history/rjw-idd/` so the evolution can be inspected publicly instead of accepted as a retrospective claim.

## Status

Active methodology work.

Some components are mature enough to document as current practice. Others, especially Rebrain, remain experimental and are labeled accordingly.

## Review paths

- [Architecture](docs/ARCHITECTURE.md)
- [How to review this repository](docs/REVIEW_GUIDE.md)
- [Audited Promptitect engineering specification](design/PROMPTITECT_ENGINEERING_SPEC_2026-09-26.md)
- [Promptitect + CCE design handoff](design/PROMPTITECT_CCE_DESIGN_HANDOFF.md)
- [Evaluator pack specification](design/EVALUATOR_PACK_SPEC.md)
- [Tribunal director skill](design/TRIBUNAL_DIRECTOR_SKILL.md)
