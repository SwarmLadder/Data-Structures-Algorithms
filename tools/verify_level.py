"""Check a whole level: every lesson drill and every interview problem, from your own files.

    python -m tools.verify_level basics
    python -m tools.verify_level advanced --json report.json

Drills are read from drills/starter/<ID>.py and problems from problems/starter/<ID>.py.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from tools import drills, practice

ROOT = Path(__file__).resolve().parents[1]


def problem_ok(pid: str) -> bool:
    try:
        results = practice.evaluate(ROOT / "problems" / "starter" / f"{pid}.py", practice.cases()[pid])
    except (OSError, subprocess.TimeoutExpired, RuntimeError):
        return False
    return all(r["ok"] for r in results)


def verify(level: str) -> dict:
    drill_rows = [{"id": d["id"], "pass": drills.grade_file(d["id"], drills.starter_path(d["id"]))[0]}
                  for d in drills.drills().values() if d["level"] == level]
    problem_rows = [{"id": p["id"], "pass": problem_ok(p["id"])}
                    for p in practice.bank().values() if p["level"] == level]
    rows = drill_rows + problem_rows
    passed = sum(r["pass"] for r in rows)
    return {"level": level, "passed": passed, "total": len(rows), "complete": passed == len(rows),
            "drills": drill_rows, "problems": problem_rows}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("level", choices=drills.LEVELS)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args(argv)
    report = verify(args.level)
    for name in ("drills", "problems"):
        rows = report[name]
        print(f"\n{name.title()} ({sum(r['pass'] for r in rows)}/{len(rows)})")
        print("  " + " ".join(("✅" if r["pass"] else "❌") + r["id"] for r in rows))
    print(f"\n{args.level}: {report['passed']}/{report['total']} pass. " + ("COMPLETE" if report["complete"] else "NOT COMPLETE"))
    if args.json:
        args.json.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return 0 if report["complete"] else 1


if __name__ == "__main__":
    sys.exit(main())
