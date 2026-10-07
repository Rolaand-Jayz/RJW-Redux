# Method history: dated evidence ledger

This is an evidence ledger, not a claim that RJW, CCE, Promptitect, Evaluator, Tribunal, or Rebrain existed in their current form on the earliest date shown.

**Evidence statuses**
- **Verified repository event:** supported by GitHub repository metadata or a particular commit.
- **Historical snapshot:** shows what a document said at a known revision, not when each idea was first conceived.
- **Conversation lead, pending primary-source reconciliation:** surfaced during historical chat review, but not yet anchored to a recoverable exported conversation/message.
- **Unknown:** date, first occurrence, or implementation status not established.

## Repository-verified chronology

| Date (UTC) | Event | What the evidence actually establishes |
| --- | --- | --- |
| **2025-09-29 02:10:13** | Original private `Rolaand-Jayz/Rolaand-Jayz-Wayz-IDD` repository created. | A verifiable repository starting point, **not** the invention date of RJW or any earlier idea. |
| **2025-10-07 13:43:53** | [RJW-IDD master index and prompt library commit](https://github.com/Rolaand-Jayz/Rolaand-Jayz-Wayz-IDD/commit/05043da90b566c4d29f3f48923bb31da10a09154). | Dated additions including a master index, prompt discovery/navigation, multiple prompt assets, agent-response guard, and quickstart material. These are artifacts of an active method, not only retrospective writing. |
| **2025-10-07 18:42:48** | [RJW CLI/starter-kit implementation commit](https://github.com/Rolaand-Jayz/Rolaand-Jayz-Wayz-IDD/commit/5acd0ca77a14c5f2d6e92dd95688aa93444c1b97). | The commit contains actual CLI source, guard/config/doc-sync tooling, install scripts, unit tests, and workflow automation. It demonstrates an attempt to make the **RJW-IDD method** operational. It does **not**, by itself, demonstrate an implemented CCE. The commit message's test-success claims have not been independently rerun. |
| **2025-11-26 00:01:36** | [Restructure to pure methodology](https://github.com/Rolaand-Jayz/Rolaand-Jayz-Wayz-IDD/commit/e585c6b02296bf0aef4ba713d2dd6e68a6d23858). | Code, starter kit, scripts, and workflows were removed from the then-current repository tree. Looking only at its later state would miss that earlier implementation work. The deleted code remains visible in Git history. |
| **2025-12-01 12:50:17** | [Historical source revision `608e271`](https://github.com/Rolaand-Jayz/Rolaand-Jayz-Wayz-IDD/commit/608e27182aa88184db54deb335487f4c2150f059). | The selected `METHOD-0001` and `METHOD-0004` documents in this public repo were copied from this **later** revision. They are snapshots of the method at that time, not proof their full contents existed in September. |

The original repository is private; its commit links may require access. Selected historical text is publicly mirrored under [`history/rjw-idd/`](rjw-idd/README.md).

## Conversation leads requiring archival confirmation

Earlier chat-history retrieval in the reconstruction process surfaced a **2025-10-19** discussion about keeping only task-relevant context, *completely removing* irrelevant information rather than merely telling a model to ignore it, and protecting active context from dilution/pollution.

**Current status:** a promising historical lead, **not yet an export-anchored citation**. The exact chat timestamp, full surrounding conversation, context, and quote transcription should be checked against the user's ChatGPT export before being presented as authenticated primary evidence on this public page.

This matters because it may independently date the thought **before** subsequent CCE documentation, while the Git commits independently show work on RJW-IDD was already underway.

## What is currently established vs. not

**Established by dated Git evidence:** the RJW-IDD project existed by late September 2025; substantial methodology/prompt/tooling work was committed in early October; later restructuring removed earlier code; historical source documents survive.

**Not established by these Git commits alone:** when the user first rejected increasing context as the solution; the first occurrence of the name CCE; the first actual CCE implementation attempt or its technical outcome; the original Promptitect GPT creation date; invention priority against wider industry work.

**User-reported history awaiting primary receipts:** the user independently arrived at the need for *smaller, purer, task-specific active context*, attempted CCE but could not then finish it with his level of agent/context understanding, and is now revisiting the problem. An unreleased novel co-writing method explores deliberate context control independently; no technical details should be published until the user chooses to release them.

## Next evidence step

When the ChatGPT export is available, apply [chat evidence intake](CHAT_EVIDENCE_INTAKE.md): recover original dated exchanges, distinguish what the user said from model paraphrases, cross-reference commits/branches/versions, and only then promote exact quotations, first-mention dates, or strong origin claims into the verified timeline. Keep raw conversations private by default.
