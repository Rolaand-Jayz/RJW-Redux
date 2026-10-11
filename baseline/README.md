# PCT-001 — Reproducible behavioral baseline

**Status: fixture construction complete; live behavioral baseline NOT YET EXECUTED.**

This is the first implementation milestone for the [RJW Redux Promptitect](../components/PROMPTITECT.md) and [Evaluator](../components/EVALUATOR.md) evolution. It preserves the separation between Promptitect (prompt construction and future decision routing), Evaluator v2 (independent judgment), and RJW execution infrastructure.

## What is in this directory?

- `source-manifest.json` — SHA-256s and canonical section contracts for the user-confirmed Library sources. Contains no original GPT prompt contents.
- `cases.json` — 25 Promptitect and 18 Evaluator input scenarios, expectations, and prohibited outcomes.
- `verify.py` — dependency-free static test for fixture integrity, file hashes, ZIP contents, and optionally captured response metadata.

The latest selected Promptitect source set is the relevant preserved sources were saved **October 4–8, 2026**, and include `promptitect.zip`, `promptitect-plugin-v0.2.0(1).zip`, and `promptitect-prompting-skill-v1.0.0.zip`. Evaluator's newest verified GPT source family is the April 28, 2026 **v2 system prompt plus SUP-01 through SUP-10**. Older GPT-5.5 and EV-00...EV-09 materials are historical, not this baseline.

## Run

```bash
python3 baseline/verify.py
python3 baseline/verify.py --sources /path/to/private/Library-source-copies
```

The private source directory must contain the archives at its root and Evaluator's eleven Markdown files at root or in `evaluator_v2/`; `SUP-10` may also live in `extra/`.

A live runner may save a JSON array to `results.json`:

```json
[{"id":"PCT-001","selected_category":"system-developer","output":"[captured model output]"}]
```

Then run:

```bash
python3 baseline/verify.py --responses results.json
```

**Critical:** This validates response collection metadata only. It does *not* grade the output, trust that a model selected a category correctly, compare rubric reasoning, or declare that a GPT passed. A live run requires an independent human or separately calibrated evaluator to adjudicate the `preserve` and `must_not` criteria for every case, and track original model/provider/version, source hashes, timestamp, and evaluator decision.

## Acceptance gate

PCT-001 is complete only after:
1. Exact source hashes pass with `--sources` against private Library originals.
2. All 43 cases are run against the original GPT sources or a faithful controlled instantiation.
3. Every case is adjudicated with factual output evidence (not assumed success).
4. Observed failures and unknowns are retained in a separate results ledger.
5. The same cases can be replayed against any migrated Promptitect/Evaluator adapter, with differences reviewed rather than requiring identical prose.

Until those conditions are satisfied, **only the source manifest and fixture structure are validated**. No claim of behavioral parity, model quality, independence, or T3 integration is justified.

## Security and source boundaries

This is a public repository. Do not commit private user Library archives, user prompts containing personal data, secrets, captured execution logs, or evaluator raw outputs without explicit approval. Source checks run against private local copies. No global skill symlinks or agent discovery changes are made here.

This milestone does not implement or imply acceptance authority, GitHub merge permission, autonomous agent execution, or a T3/Pi runtime.
