# Evolution

RJW Redux did not begin as a multi-agent framework.

It began as **RJW-IDD**, a methodology for replacing vague AI-assisted coding with explicit research, requirements, specifications, tests, traceable decisions, and living documentation.

That solved real problems, but using the method exposed other ones.

## 1. RJW-IDD

RJW established several ideas that remain important:

- evidence should drive decisions;
- requirements should exist before implementation claims are accepted;
- important decisions should be traceable;
- documentation should change with the system;
- tests and acceptance criteria should be tied to the work they verify;
- agent work should be governed instead of trusted because it sounds confident.

Historical snapshots are preserved under `history/rjw-idd/`.

## 2. Context became its own problem

As projects became larger, a new failure mode became obvious: giving a model more information could make the result worse.

Old decisions, failed experiments, duplicated facts, superseded specifications, unrelated project history, and valid information from the wrong scope could all compete for attention.

The practical conclusion was:

> More context is not the answer. Better, cleaner context is.

That led to the **Context Curation Engine (CCE)** as a distinct concept. CCE treats context as something that must be classified, ranked, versioned, checked for authority, checked for conflicts, and compiled for a specific task.

## 3. Promptitect moved above prompt writing

Promptitect began as a way to construct better prompts.

That boundary did not survive contact with real work.

The harder question was often not "what prompt should I use?" but:

- should this be deterministic code instead of a model call?
- does this need one model or several?
- which tools are appropriate?
- what context should each participant receive?
- where does human judgment belong?
- what evidence is needed before the result is accepted?
- when should the current path be abandoned instead of refined again?

Promptitect therefore evolved into a decision and orchestration layer.

## 4. Independent evaluation became necessary

A worker saying its own work is correct is weak evidence.

That led to **Evaluator** as an independent role with deliberately high standards, explicit evidence discipline, and a bias against unsupported claims.

## 5. Some decisions needed adversarial pressure before implementation

Evaluation after the fact is not enough for expensive architectural choices.

The **Tribunal** separates attack, defense, and judgment so consequential ideas face serious opposition before implementation cost accumulates.

## 6. Rebrain asks a different question

Rebrain is experimental and intentionally separate.

It asks whether useful reasoning operators observed across a person's real problem-solving history can be combined with a base model's native strengths to create a composite reasoning process.

It is not style transfer and not a persona.

The experimental target is a system that can inherit useful reasoning habits while preserving disagreement, correction, evidence discipline, and the base model's own capabilities.

## Current direction

The current method is not "use more agents."

It is closer to this:

> Use the smallest architecture that can reliably reach the objective, give each participant the cleanest context it needs, separate creation from judgment when independence matters, and let evidence force a change of path.
