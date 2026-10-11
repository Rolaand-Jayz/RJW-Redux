#!/usr/bin/env python3
"""PCT-001: deterministic validation of a proposed behavioral baseline.

No model is invoked; a green result is NOT evidence that a GPT meets the cases.
Run: python3 baseline/verify.py [--sources /private/source/directory] [--responses results.json]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
HEX64 = re.compile(r"^[0-9a-f]{64}$")
CATEGORY_IDS = {
    "system-developer", "single-use-task", "revision-transformation",
    "research", "analysis-decision", "creative", "educational",
    "coding-repository", "debugging", "api-text", "prd-spec",
    "extraction-classification", "data-analysis", "spreadsheet",
    "image-generation", "image-editing", "document", "presentation",
    "agent-tool", "prompt-pack-context",
}
MODES = {"construct", "rate_this_prompt", "compare_these_prompts"}


def fail(msg: str) -> None:
    raise ValueError(msg)


def load_json(name: str) -> dict:
    with (HERE / name).open(encoding="utf-8") as f:
        return json.load(f)


def check_sha(value: str, context: str) -> None:
    if not isinstance(value, str) or not HEX64.fullmatch(value):
        fail(f"{context}: invalid SHA-256")


def sha256(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def inspect_manifest(doc: dict) -> dict[str, dict]:
    if doc.get("schema_version") != 1:
        fail("manifest schema_version must be 1")
    archives = doc.get("archives", [])
    if len(archives) != 3 or len({x["role"] for x in archives}) != 3:
        fail("expected three distinct pinned source archives")
    if len(doc.get("evaluator", [])) != 11:
        fail("expected Evaluator v2 prompt and exactly ten supplements")
    for item in archives + doc["evaluator"]:
        check_sha(item.get("sha256"), item.get("name", "unknown"))
    names = [x["name"] for x in doc["evaluator"]]
    if len(set(names)) != 11 or not any(x.startswith("THE-EVALUATOR-v2-") for x in names):
        fail("Evaluator source identity/filenames are inconsistent")
    if {f"SUP-{n:02d}" for n in range(1, 11)} != {x["name"][:6] for x in doc["evaluator"] if x["name"].startswith("SUP-")}:
        fail("Evaluator SUP-01..SUP-10 coverage is incomplete")
    categories = doc.get("canonical_categories", [])
    if len(categories) != 20 or {x["category"] for x in categories} != CATEGORY_IDS:
        fail("exactly 20 unique canonical categories are required")
    mapping = {}
    for entry in categories:
        category = entry["category"]
        order = entry["canonical_order"]
        required = entry["required_sections"]
        if not isinstance(order, list) or not all(isinstance(s, str) and s for s in order):
            fail(f"{category}: invalid canonical order")
        if len(set(order)) != len(order):
            fail(f"{category}: duplicate canonical section")
        if not required or not set(required).issubset(set(order)):
            fail(f"{category}: required sections missing from canonical order")
        if not entry["module_path"].startswith("skills/"):
            fail(f"{category}: invalid module reference")
        mapping[category] = entry
    return mapping


def inspect_cases(doc: dict, categories: dict[str, dict]) -> dict[str, dict]:
    if doc.get("schema_version") != 1 or doc.get("status") != "unexecuted":
        fail("fixtures must declare an unexecuted baseline; never imply a GPT run")
    if len(doc.get("promptitect", [])) != 25 or len(doc.get("evaluator", [])) != 18:
        fail("expected 25 Promptitect and 18 Evaluator scenarios")
    cases = {}
    observed_primary = set()
    for engine, prefix in (("promptitect", "PCT"), ("evaluator", "EVT")):
        for index, item in enumerate(doc[engine], 1):
            case_id = f"{prefix}-{index:03d}"
            if item.get("id") != case_id or item.get("engine") != engine:
                fail(f"{case_id}: id/engine mismatch")
            if case_id in cases or not isinstance(item.get("input"), str):
                fail(f"{case_id}: duplicate or missing input")
            expected = item.get("expected", {})
            if not all(isinstance(expected.get(field), str) and expected[field] for field in ("preserve", "must_not")):
                fail(f"{case_id}: expectations must specify concrete preserve/must-not criteria")
            if item.get("verification") != "human_semantic_review_required":
                fail(f"{case_id}: semantic review must remain explicit")
            if engine == "promptitect":
                if item.get("mode") not in MODES:
                    fail(f"{case_id}: unknown Promptitect mode")
                category = expected.get("primary_category")
                if category is not None and category not in categories:
                    fail(f"{case_id}: unknown primary category {category}")
                if item["mode"] == "construct" and category is None:
                    fail(f"{case_id}: construct mode needs a primary category")
                if item["mode"] != "construct" and category is not None:
                    fail(f"{case_id}: gated evaluation must not masquerade as construction")
                if category:
                    observed_primary.add(category)
            else:
                modules = expected.get("modules")
                if not modules or not isinstance(modules, list):
                    fail(f"{case_id}: missing Evaluator module expectations")
                if any(not re.fullmatch(r"SUP-(?:0[1-9]|10)", m) for m in modules):
                    fail(f"{case_id}: invalid evaluator SUP module")
                if not item.get("mode"):
                    fail(f"{case_id}: missing evaluator mode")
            cases[case_id] = item
    if observed_primary != CATEGORY_IDS:
        fail(f"Promptitect category fixture coverage incomplete: {sorted(CATEGORY_IDS - observed_primary)}")
    return cases


def locate_source(sources: Path, name: str) -> Path:
    candidates = [sources / name, sources / "evaluator_v2" / name,
                  sources / "extra" / name]
    matches = [p for p in candidates if p.is_file()]
    if len(matches) != 1:
        fail(f"cannot locate unique private source: {name}")
    return matches[0]


def inspect_sources(manifest: dict, sources: Path) -> None:
    if not sources.is_dir():
        fail(f"source directory missing: {sources}")
    for item in manifest["archives"] + manifest["evaluator"]:
        name = item["name"]
        path = locate_source(sources, name)
        if sha256(path) != item["sha256"]:
            fail(f"SHA-256 mismatch: {name}")
        if name.endswith(".zip"):
            with zipfile.ZipFile(path) as archive:
                entries = [x for x in archive.infolist() if not x.is_dir()]
                if len(entries) != item["entries"] or archive.testzip() is not None:
                    fail(f"ZIP corrupted or entry count mismatch: {name}")
                if item["role"] == "promptitect_plugin":
                    plugin_files = {x.filename.removeprefix("promptitect/") for x in entries}
                    for category in manifest["canonical_categories"]:
                        if category["module_path"] not in plugin_files:
                            fail(f"missing plugin module: {category['module_path']}")


def inspect_responses(path: Path, cases: dict[str, dict]) -> int:
    """Check captured run metadata only, never judge semantic quality."""
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, list):
        fail("responses must be a list of {id, output, selected_category?} objects")
    seen = set()
    for record in raw:
        case_id = record.get("id")
        if case_id not in cases or case_id in seen:
            fail(f"unknown or duplicate response id: {case_id}")
        seen.add(case_id)
        if not isinstance(record.get("output"), str) or not record["output"].strip():
            fail(f"{case_id}: blank output")
        if "selected_category" in record and record["selected_category"] != cases[case_id]["expected"].get("primary_category"):
            fail(f"{case_id}: reported category mismatches expected selection")
    return len(seen)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sources", type=Path, help="private folder holding Library sources; enables SHA and ZIP checks")
    parser.add_argument("--responses", type=Path, help="optional captured model outputs; metadata checks only")
    args = parser.parse_args()

    try:
        manifest = load_json("source-manifest.json")
        categories = inspect_manifest(manifest)
        cases = inspect_cases(load_json("cases.json"), categories)
        print(f"PASS fixture and manifest structure: {len(categories)} categories, {len(cases)} cases")
        if args.sources:
            inspect_sources(manifest, args.sources)
            print("PASS original source SHA-256, ZIP integrity, plugin module coverage")
        else:
            print("SKIP original source verification (--sources was not provided)")
        if args.responses:
            n = inspect_responses(args.responses, cases)
            print(f"PASS response metadata: {n}/{len(cases)} captured outputs")
        else:
            print("SKIP model-output metadata (no --responses)")
        print("NOT TESTED: model behavior, output semantics, quality, T3 integration")
        return 0
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError, zipfile.BadZipFile) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
