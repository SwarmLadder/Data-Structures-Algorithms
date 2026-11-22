"""Build lesson and worked-example pages from their Markdown source, and check they are current.

    python -m tools.lessons           # run examples, refresh outputs, drill lists and quizzes
    python -m tools.lessons --check   # fail if anything is out of date (CI)

Conventions inside a page:

* Every ```python block runs, in order, in ONE namespace per page, so later
  blocks can use functions defined earlier. If a block prints anything, the
  output is written below it between <!-- output --> and <!-- /output -->.
* ```python norun is shown but never executed (pseudo-code, fragments).
* ```python error must raise; the exception line is shown.
* <!-- drills --> … <!-- /drills --> is filled from drills/<level>.json.
* <!-- quiz --> … <!-- /quiz --> is filled from quizzes/<level>.json.
"""
from __future__ import annotations

import argparse
import contextlib
import io
import json
import re
import sys
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEVELS = ("basics", "intermediate", "advanced")
BLOCK = re.compile(r"```python( norun| error)?\n(.*?)```\n(?:\n?<!-- output -->\n.*?<!-- /output -->\n)?", re.S)
KIND = {"guided": "guided", "independent": "independent"}


def run_page(text: str, where: str) -> str:
    namespace: dict = {"__name__": "__lesson__"}

    def replace(match: re.Match) -> str:
        mode, code = match.group(1), match.group(2)
        fence = f"```python{mode or ''}\n{code}```\n"
        if mode == " norun":
            return fence
        buffer = io.StringIO()
        try:
            with contextlib.redirect_stdout(buffer):
                exec(compile(code, where, "exec"), namespace)
        except Exception as error:  # noqa: BLE001 - shown to the learner
            if mode != " error":
                raise ValueError(f"{where}: example raised {type(error).__name__}: {error}\n{code}") from error
            line = traceback.format_exception_only(type(error), error)[-1].strip()
            output = buffer.getvalue() + line + "\n"
        else:
            if mode == " error":
                raise ValueError(f"{where}: example marked `error` did not raise\n{code}")
            output = buffer.getvalue()
        if not output:
            return fence
        return fence + "\n<!-- output -->\n```text\n" + output.rstrip("\n") + "\n```\n<!-- /output -->\n"

    return BLOCK.sub(replace, text)


def fill(text: str, marker: str, body: str, where: str) -> str:
    start, end = f"<!-- {marker} -->", f"<!-- /{marker} -->"
    if start not in text:
        return text
    if text.count(start) != 1 or end not in text:
        raise ValueError(f"{where}: needs exactly one {start} … {end}")
    before, rest = text.split(start, 1)
    return before + start + "\n" + body.rstrip() + "\n" + end + rest.split(end, 1)[1]


def drill_list(lesson: str, bank: list[dict]) -> str:
    items = [i for i in bank if i["lesson"] == lesson]
    if not items:
        return "*No drills for this lesson.*"
    rows = ["Each drill is graded on six published cases. **Guided** drills give you a skeleton with `___` "
            "blanks; **independent** drills give only the signature.", "",
            "| ID | Drill | Kind |", "|---|---|---|"]
    for item in items:
        rows.append(f"| `{item['id']}` | **{item['title']}.** {item['prompt']} | {KIND[item['kind']]} |")
    first = items[0]["id"]
    rows += ["", "```bash", f"python -m tools.drills show {first}", f"python -m tools.drills check {first}",
             f"python -m tools.drills hint {first} 1", "```"]
    return "\n".join(rows)


def quiz_block(key: str, quiz: dict | None) -> str:
    if not quiz:
        return "*No quiz for this lesson.*"
    lines = ["Answer in your head first, then check. Answers are stored as hashes, so reading the files won't spoil them.", ""]
    for n, question in enumerate(quiz["questions"], 1):
        lines += [f"**{n}.** {question['question']}", ""]
        lines += [f"   - **{letter})** {option}" for letter, option in question["options"].items()]
        lines.append("")
    lines += ["```bash", f"python -m tools.quiz {key} 1 b      # question 1, answer b",
              f"python -m tools.quiz {key}           # list the questions", "```"]
    return "\n".join(lines)


def pages(level: str) -> list[Path]:
    found = sorted((ROOT / "lessons" / level).glob("[0-9][0-9]_*.md"))
    found += sorted((ROOT / "worked_examples" / level).glob("[0-9][0-9]_*.md"))
    return found


def build() -> dict[Path, str]:
    outputs: dict[Path, str] = {}
    for level in LEVELS:
        bank_path = ROOT / "drills" / f"{level}.json"
        bank = json.loads(bank_path.read_text(encoding="utf-8")) if bank_path.exists() else []
        quiz_path = ROOT / "quizzes" / f"{level}.json"
        quizzes = json.loads(quiz_path.read_text(encoding="utf-8")) if quiz_path.exists() else {}
        for md in pages(level):
            where = md.relative_to(ROOT).as_posix()
            text = run_page(md.read_text(encoding="utf-8"), where)
            text = fill(text, "drills", drill_list(where, bank), where)
            if md.parent.parent.name == "lessons":
                key = f"{level}/{md.name[:2]}"
                text = fill(text, "quiz", quiz_block(key, quizzes.get(key)), where)
            outputs[md] = text
    return outputs


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    try:
        outputs = build()
    except ValueError as error:
        print(f"FAIL {error}", file=sys.stderr)
        return 1
    stale = [p for p, text in outputs.items() if p.read_text(encoding="utf-8") != text]
    if args.check:
        if stale:
            print("Out of date (run python -m tools.lessons): "
                  + ", ".join(p.relative_to(ROOT).as_posix() for p in stale), file=sys.stderr)
            return 1
        print(f"lessons up to date ({len(outputs)} pages)")
        return 0
    for path in stale:
        path.write_text(outputs[path], encoding="utf-8")
    print(f"updated {len(stale)} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
