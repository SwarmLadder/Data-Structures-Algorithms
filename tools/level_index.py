"""Refresh the generated tables in lessons/<level>/README.md and worked_examples/<level>/README.md.

    python -m tools.level_index           # rewrite the tables
    python -m tools.level_index --check   # fail if a README is out of date (CI)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEVELS = ("basics", "intermediate", "advanced")
START, END = "<!-- index:start -->", "<!-- index:end -->"


def lesson_table(level: str) -> str:
    drills = json.loads((ROOT / "drills" / f"{level}.json").read_text(encoding="utf-8"))
    quizzes = json.loads((ROOT / "quizzes" / f"{level}.json").read_text(encoding="utf-8"))
    rows = ["| # | Lesson | Study time | Drills | Quiz | Interview problems |", "|---:|---|---|---:|---:|---|"]
    for md in sorted((ROOT / "lessons" / level).glob("[0-9][0-9]_*.md")):
        text = md.read_text(encoding="utf-8")
        title = text.splitlines()[0].lstrip("# ").strip()
        time = re.search(r"\*\*Study time:\*\*\s*([^.·\n]*)", text)
        rel = md.relative_to(ROOT).as_posix()
        n_drills = sum(1 for d in drills if d["lesson"] == rel)
        n_quiz = len(quizzes.get(f"{level}/{md.name[:2]}", {}).get("questions", []))
        problems = re.search(r"\*\*Interview problems for this lesson:\*\* ([^.]*)\.", text)
        rows.append(f"| {md.name[:2]} | [{title}]({md.name}) | {time.group(1).strip() if time else ''} | {n_drills} | {n_quiz} | {problems.group(1) if problems else ''} |")
    return "\n".join(rows)


def example_table(level: str) -> str:
    rows = ["| # | Example | Problem |", "|---|---|---|"]
    for md in sorted((ROOT / "worked_examples" / level).glob("[0-9][0-9]_*.md")):
        text = md.read_text(encoding="utf-8")
        tag, title = text.splitlines()[0].lstrip("# ").split(" · ", 1)
        problem = text.split("**Problem.** ", 1)[1].split("\n", 1)[0]
        rows.append(f"| {tag.replace('Worked example ', '')} | [{title}]({md.name}) | {problem} |")
    return "\n".join(rows)


def targets() -> dict[Path, str]:
    out = {}
    for level in LEVELS:
        out[ROOT / "lessons" / level / "README.md"] = lesson_table(level)
        out[ROOT / "worked_examples" / level / "README.md"] = example_table(level)
    return out


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    stale = []
    for path, table in targets().items():
        text = path.read_text(encoding="utf-8")
        before, rest = text.split(START, 1)
        new = before + START + "\n" + table + "\n" + END + rest.split(END, 1)[1]
        if new != text:
            stale.append(path.relative_to(ROOT).as_posix())
            if not args.check:
                path.write_text(new, encoding="utf-8")
    if args.check and stale:
        print("Out of date (run python -m tools.level_index): " + ", ".join(stale), file=sys.stderr)
        return 1
    print("level indexes up to date" if not stale else "updated: " + ", ".join(stale))
    return 0


if __name__ == "__main__":
    sys.exit(main())
