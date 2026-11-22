"""Run a portfolio project's test suite against your implementation or the reference.

    python -m tools.projects list
    python -m tools.projects check basics/01_inventory_reconciler            # tests starter.py
    python -m tools.projects check basics/01_inventory_reconciler my_impl.py
    python -m tools.projects verify-references                              # CI: every reference passes

Each project folder under projects/<level>/ holds README.md (the brief),
starter.py (your file), reference.py and test_project.py. The tests load the
implementation named by the DSA_PROJECT_IMPL environment variable.
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEVELS = ("basics", "intermediate", "advanced")


def projects() -> list[Path]:
    return sorted(p for level in LEVELS for p in (ROOT / "projects" / level).glob("[0-9][0-9]_*") if p.is_dir())


def run(project: Path, implementation: Path, quiet: bool = False) -> bool:
    env = dict(os.environ, DSA_PROJECT_IMPL=str(implementation.resolve()))
    result = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", str(project), "-p", "test_*.py"]
                            + ([] if quiet else ["-v"]), env=env, cwd=ROOT, capture_output=quiet, text=True)
    return result.returncode == 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("list")
    check = sub.add_parser("check")
    check.add_argument("project", help="e.g. basics/01_inventory_reconciler")
    check.add_argument("file", type=Path, nargs="?")
    sub.add_parser("verify-references")
    args = parser.parse_args(argv)
    if args.command == "list":
        for p in projects():
            print(p.relative_to(ROOT / "projects").as_posix())
        return 0
    if args.command == "verify-references":
        failed = [p for p in projects() if not run(p, p / "reference.py", quiet=True)]
        for p in failed:
            print("FAIL", p.relative_to(ROOT).as_posix(), file=sys.stderr)
        if not failed:
            print(f"All {len(projects())} project references pass their test suites.")
        return 1 if failed else 0
    project = ROOT / "projects" / args.project
    if not (project / "test_project.py").is_file():
        parser.error("Unknown project " + args.project)
    return 0 if run(project, args.file or project / "starter.py") else 1


if __name__ == "__main__":
    sys.exit(main())
