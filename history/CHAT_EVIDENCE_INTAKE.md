# Chat history evidence intake

**Status: prepared; export not yet received.** Do not imply the chat archive was ingested or audited.

## Objective

Reconstruct the **actual chronology** of RJW, RJW-IDD, context curation/CCE, Promptitect, Evaluator, Tribunal, and Rebrain. Distinguish (1) an idea being voiced, (2) requirements/design, (3) implementation attempt, (4) demonstrated behavior, (5) revisions/failures, and (6) current plans.

The export is evidence of conversations **present in the export**, not automatically every historical or deleted conversation. An absent conversation must not be treated as proof it never occurred. Deleted custom GPTs and their metadata may require other independent records.

## Procedure after an export is provided

1. **Preserve originals privately.** Archive the source export and record acquisition date, file hashes, extraction method, timezone conversion, and any gaps. Do **not** upload the raw export or personal conversations to this public repository.
2. **Search pre-name concepts.** Search early chats for prompt-building research, prompting frameworks/templates, task-specific context, token limits, compression, forgetting, retrieval, culling, purity, dilution/pollution, authority, freshness, agent roles, review loops, spec ambiguity, and separate evaluators, not just the eventual project names.
3. **Separate speaker and date.** Record whether a proposition originated in a user message, assistant response, pasted third-party content, or imported document. Record the exact original timestamp and timezone, with no guessed first dates.
4. **Recover full passages.** Capture surrounding messages to distinguish proposals from corrections, rejected options, completed work, and mere assistant claims.
5. **Crosswalk to Git history.** Link conceptual milestones to commits, file histories, tests, PRs, and removal/refactor events when genuinely related. Do not label a general RJW tool as CCE implementation without an explicit connection.
6. **Track negative results.** A failed design, stalled implementation, or contradicted assumption is part of the history. Describe what was tried, what blocked it, and what evidence supports that conclusion.
7. **Publish only reviewed excerpts.** Publish the shortest necessary quotation or carefully labeled paraphrase, alongside sufficient date/provenance to be audited. Redact private people, secrets, personal information, unpublished project details, and material the user has not approved for disclosure.

## Record schema

Each candidate finding should contain:

- `id`: stable chronological evidence ID
- `claim`: narrow proposition, not an embellished headline
- `occurred_at`: original timestamp + timezone, or `unknown`
- `source_kind`: user chat / assistant chat / archived GPT artifact / Git commit / repo file / test / later recollection
- `source_locator_private`: chat and message identifiers or Git references kept in a **private** index
- `public_reference`: public commit/doc link, or approved privacy-safe excerpt
- `speaker`: who actually made the claim
- `verbatim_excerpt`: exactly as recorded, if disclosure is approved
- `context_and_corrections`: nearby messages, retractions, disagreement
- `phase`: idea / design / attempted implementation / tested / abandoned / revised
- `assessment`: observed, documented, inference, hypothesis, or unknown
- `confidence_limits`: what this evidence cannot show

## Priority questions

- **Promptitect origins:** What were the prompting-research chats before the surviving July 2025 custom GPT? Which examples predate it, and which later examples show changes in prompt construction? Do not treat a qualitative improvement as a proven causal discontinuity without comparable examples.
- **Context rejection:** Find the first user-originated statement that increasing context capacity or accumulating context is counterproductive; separate it from the assistant's wording.
- **CCE:** First concept, first name, requirements, earliest code attempt, what was incomplete, and how the newer attempt differs.
- **RJW / RJW-IDD:** Distinguish the first research conversation, first method description, first code commit, and subsequent restructure.
- **Evaluator versus Tribunal:** Recover the design evolution of artifact-completeness/ambiguity testing versus adversarial scrutiny of design choices, and how the tools were used beyond ideation.
- **Novel-writing method:** Record private milestones if found; **do not** disclose its unpublished mechanisms, prompts, or canon in the public history.
- **Rebrain:** Mark as an experiment, and separate observed reasoning patterns from untested claims of transfer.

## Publication boundary

This public repo documents **method history**, not the user's private conversations. Maintain a private evidence ledger separately. Before quoting user-authored chat in public, check context, relevance, permission, and privacy. Never rewrite a later understanding into an earlier source or imply historical implementation success where only a proposal existed.
