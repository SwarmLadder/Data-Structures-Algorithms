"""Lesson drills: short graded Python exercises attached to each lesson.

    python -m tools.drills list --level basics
    python -m tools.drills show DB01
    python -m tools.drills hint DB01 1          # hints unlock one at a time: 1, 2, 3
    python -m tools.drills check DB01           # grades drills/starter/DB01.py
    python -m tools.drills check DB01 mine.py   # or any file you choose
    python -m tools.drills progress basics
    python -m tools.drills verify-references

Guided drills give you a skeleton with ___ blanks; independent drills give
only the function signature. Every drill runs against six published cases
(the first two are the examples in the prompt). Only run code you trust:
the subprocess timeout is not a security sandbox.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from tools.practice import evaluate

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "drills"
LEVELS = ("basics", "intermediate", "advanced")


def drills() -> dict[str, dict]:
    index: dict[str, dict] = {}
    for level in LEVELS:
        for item in json.loads((BANK / f"{level}.json").read_text(encoding="utf-8")):
            if item["id"] in index or item["level"] != level:
                raise ValueError("Invalid or duplicate drill " + item["id"])
            index[item["id"]] = item
    return index


def cases() -> dict[str, list]:
    return json.loads((BANK / "cases.json").read_text(encoding="utf-8"))


def starter_path(did: str) -> Path:
    return BANK / "starter" / f"{did}.py"


def reference_path(did: str) -> Path:
    return BANK / "reference" / f"{did}.py"


def check(did: str, path: Path) -> list[dict]:
    return evaluate(path, cases()[did])


def describe(item: dict) -> str:
    lines = [f"{item['id']} — {item['title']}  [{item['level']}, {item['kind']}]",
             f"Lesson: {item['lesson']}", "", item["prompt"], "",
             f"Signature: {item['signature']}"]
    for n, example in enumerate(cases()[item["id"]][:2], 1):
        args = ", ".join(json.dumps(a, ensure_ascii=False) for a in example["args"])
        lines.append(f"Example {n}: solve({args}) -> {json.dumps(example['expected'], ensure_ascii=False)}")
    lines += ["", f"Write it in drills/starter/{item['id']}.py, then: python -m tools.drills check {item['id']}",
              f"Hints: python -m tools.drills hint {item['id']} 1  (up to {len(item['hints'])})"]
    return "\n".join(lines)


def grade_file(did: str, path: Path) -> tuple[bool, list[dict] | str]:
    try:
        results = check(did, path)
    except (OSError, subprocess.TimeoutExpired, RuntimeError) as error:
        return False, str(error) or type(error).__name__
    return all(r["ok"] for r in results), results


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    lister = sub.add_parser("list")
    lister.add_argument("--level", choices=LEVELS)
    show = sub.add_parser("show")
    show.add_argument("id")
    hint = sub.add_parser("hint")
    hint.add_argument("id")
    hint.add_argument("level", type=int, nargs="?", default=1)
    grade = sub.add_parser("check")
    grade.add_argument("id")
    grade.add_argument("file", type=Path, nargs="?")
    prog = sub.add_parser("progress")
    prog.add_argument("level", choices=LEVELS)
    sub.add_parser("verify-references")
    args = parser.parse_args(argv)
    index = drills()

    if args.command == "list":
        for did, item in index.items():
            if args.level in (None, item["level"]):
                print(f"{did} | {item['kind']:<11} | {item['title']}")
        return 0
    if args.command == "verify-references":
        failed = []
        for did in index:
            ok, detail = grade_file(did, reference_path(did))
            if not ok:
                failed.append(did)
                print(f"FAIL {did}: {detail if isinstance(detail, str) else [r['index'] for r in detail if not r['ok']]}",
                      file=sys.stderr)
        if failed:
            return 1
        print(f"All {len(index)} drill references passed {sum(map(len, cases().values()))} cases.")
        return 0
    if args.command == "progress":
        items = [i for i in index.values() if i["level"] == args.level]
        passed = 0
        for item in items:
            ok, _ = grade_file(item["id"], starter_path(item["id"]))
            passed += ok
            print(f"{'✅' if ok else '❌'} {item['id']} {item['title']}")
        print(f"\n{passed}/{len(items)} {args.level} drills pass")
        return 0 if passed == len(items) else 1

    did = args.id.upper()
    if did not in index:
        parser.error("Unknown drill " + did)
    item = index[did]
    if args.command == "show":
        print(describe(item))
        return 0
    if args.command == "hint":
        level = max(1, min(args.level, len(item["hints"])))
        for n, text in enumerate(item["hints"][:level], 1):
            print(f"Hint {n}: {text}")
        if level < len(item["hints"]):
            print(f"\nStill stuck? python -m tools.drills hint {did} {level + 1}")
        return 0
    ok, detail = grade_file(did, args.file or starter_path(did))
    if isinstance(detail, str):
        print(f"❌ {did}: could not run: {detail}")
        print(f"   Need a nudge? python -m tools.drills hint {did} 1")
        return 1
    for result in detail:
        if not result["ok"]:
            print(f"❌ case {result['index']}: input {json.dumps(result['input'], ensure_ascii=False)}")
            print(f"   expected {json.dumps(result['expected'], ensure_ascii=False)}")
            print(f"   got      {result['error'] or json.dumps(result['actual'], ensure_ascii=False)}")
    passed = sum(r["ok"] for r in detail)
    print(("✅ " if ok else "❌ ") + f"{did}: {passed}/{len(detail)} cases pass")
    if not ok:
        print(f"   Need a nudge? python -m tools.drills hint {did} 1")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
