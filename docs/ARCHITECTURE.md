# Architecture

RJW Redux is not one giant agent.

It is a set of separable responsibilities that can be composed only when the objective justifies them.

```text
Human objective
      |
      v
+----------------------+
|     Promptitect      |
| objective + pathway  |
+----------+-----------+
           |
           | asks what each participant needs
           v
+----------------------+
|         CCE          |
| curated task context |
+----------+-----------+
           |
           v
+----------------------+
| Workers / Tools /    |
| Deterministic Code   |
+----------+-----------+
           |
           v
+----------------------+
| Evidence + Candidate |
+----------+-----------+
           |
           v
+----------------------+
|      Evaluator       |
| independent judgment |
+----------+-----------+
           |
           +---- PASS ----> accepted outcome
           |
           +---- repair ---> worker loop
           |
           +---- ceiling --> Promptitect replans
```

For high-leverage decisions, the Tribunal can be inserted before commitment:

```text
candidate decision
      |
      v
 Devil <-> Guardian
      |
      v
    Judge
      |
      v
decision record
```

Rebrain is different. It does not sit in the execution path as another mandatory box. It is an experiment in changing the reasoning policy of a capable model before that model fills one of the roles above.

## Boundaries

### Promptitect does not own truth

Promptitect selects a path and governs execution. It does not get to declare its own path correct merely because it selected it.

### CCE does not own the objective

CCE curates information. It does not redefine what the user asked for.

### Workers do not own acceptance

Workers produce candidates and evidence. They do not certify themselves.

### Evaluator does not implement repairs

Evaluator identifies what is wrong and what must become true. Repair belongs to an implementation path with fresh state.

### Tribunal does not become permanent ceremony

It is reserved for decisions where being wrong is expensive enough to justify adversarial review.

### Rebrain does not replace evidence

A reasoning style can improve search and decision behavior. It does not change the evidence threshold required before a claim is accepted.

## Minimum-sufficient architecture

A central rule applies to the architecture itself:

> If removing a component does not materially increase the probability of an incorrect, incomplete, unsafe, or unusable result, remove it.

That means a simple deterministic script is preferable to an agent when a script can solve the problem reliably.

One capable model is preferable to a swarm when independence or specialization is not needed.

A large context package is preferable to a tiny one when the task genuinely requires the information.

The optimization target is not minimalism for its own sake. It is the least complexity that still reaches the required quality.
