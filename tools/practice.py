"""Command-line DSA interview trainer; only run files you trust locally."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEVELS = ("basics", "intermediate", "advanced")


def bank():
    result = {}
    for level in LEVELS:
        for problem in json.loads((ROOT / "problems" / (level + ".json")).read_text(encoding="utf-8")):
            if problem["id"] in result:
                raise ValueError("Duplicate ID: " + problem["id"])
            result[problem["id"]] = problem
    return result


def cases():
    return json.loads((ROOT / "tests" / "cases.json").read_text(encoding="utf-8"))


def canonical(value):
    # JSON keeps booleans distinct from integers. Dict key order is irrelevant.
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def evaluate(path: Path, cases: list, timeout: int = 5):
    if not path.is_file():
        raise FileNotFoundError(path)
    process = subprocess.run(
        [sys.executable, "-I", str(ROOT / "tools" / "_runner.py"), str(path.resolve())],
        input=json.dumps({"cases": [case["args"] for case in cases]}),
        text=True, capture_output=True, timeout=timeout, check=False,
        cwd=ROOT,
    )
    if process.returncode:
        raise RuntimeError((process.stderr or "Submission failed").strip()[:1500])
    try:
        results = json.loads(process.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError("Invalid output from practice runner") from exc
    if not isinstance(results, list) or len(results) != len(cases):
        raise RuntimeError("Runner produced the wrong number of test results")
    return [
        {"index": i, "ok": "value" in result and canonical(result["value"]) == canonical(case["expected"]),
         "input": case["args"], "expected": case["expected"],
         "actual": result.get("value"), "error": result.get("error")}
        for i, (result, case) in enumerate(zip(results, cases), 1)
    ]


def show(problem: dict, hints: bool = False):
    print(f"{problem['id']} | {problem['title']} [{problem['difficulty']}] | {problem['pattern']}")
    print("\n" + problem["prompt"] + "\n")
    print("Constraints: " + problem["constraints"])
    print("Signature: " + problem["signature"])
    for i, example in enumerate(problem["examples"], 1):
        print(f"Example {i}: {json.dumps(example['args'], ensure_ascii=False)} -> {json.dumps(example['expected'], ensure_ascii=False)}")
    if hints:
        for i, hint in enumerate(problem["hints"], 1):
            print(f"Hint {i}: {hint}")
    print(f"\nStarter: problems/starter/{problem['id']}.py")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    listing = sub.add_parser("list", help="List problem IDs and titles")
    listing.add_argument("--level", choices=LEVELS)
    details = sub.add_parser("show", help="Read one complete problem")
    details.add_argument("id")
    details.add_argument("--hints", action="store_true")
    checking = sub.add_parser("check", help="Check a trusted local Python file")
    checking.add_argument("id")
    checking.add_argument("file", type=Path)
    sub.add_parser("verify-references", help="Run every reference against all published cases")
    args = parser.parse_args(argv)
    problems = bank()
    if args.command == "list":
        for p in problems.values():
            if args.level is None or p["level"] == args.level:
                print(f"{p['id']}: {p['title']} ({p['difficulty']}; {p['pattern']})")
        return 0
    if args.command in ("show", "check"):
        id = args.id.upper()
        if id not in problems:
            parser.error("Unknown problem " + id)
        if args.command == "show":
            show(problems[id], args.hints)
            return 0
        tests = cases()[id]
        try:
            results = evaluate(args.file, tests)
        except (OSError, subprocess.TimeoutExpired, RuntimeError) as error:
            print(f"{id}: could not run: {error}")
            return 1
        for result in results:
            label = "PASS" if result["ok"] else "FAIL"
            print(f"{label}  {id} case {result['index']}/{len(results)}")
            if not result["ok"]:
                print("  input:", json.dumps(result["input"], ensure_ascii=False))
                print("  expected:", json.dumps(result["expected"], ensure_ascii=False))
                print("  actual:", result["error"] or json.dumps(result["actual"], ensure_ascii=False))
        passed = sum(result["ok"] for result in results)
        print(f"{id}: {passed}/{len(results)} tests passed")
        return 0 if passed == len(results) else 1
    failed = []
    all_cases = cases()
    for id in problems:
        try:
            verdicts = evaluate(ROOT / "problems" / "reference" / (id + ".py"), all_cases[id])
            passed = sum(v["ok"] for v in verdicts)
            if passed != len(verdicts):
                failed.append(f"{id}: {passed}/{len(verdicts)}")
        except (RuntimeError, subprocess.TimeoutExpired, OSError) as error:
            failed.append(f"{id}: {error}")
    if failed:
        print("Reference failures:\n" + "\n".join(failed))
        return 1
    print(f"All {len(problems)} references passed {sum(map(len, all_cases.values()))} cases.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
