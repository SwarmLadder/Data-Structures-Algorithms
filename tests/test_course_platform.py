"""Lessons, drills, quizzes, worked examples, projects and level guides stay complete and current."""
import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import drills, quiz  # noqa: E402

LEVELS = ("basics", "intermediate", "advanced")
PREFIX = {"basics": "DB", "intermediate": "DI", "advanced": "DA"}


def run(*args):
    return subprocess.run([sys.executable, "-m", *args], cwd=ROOT, capture_output=True, text=True)


class LessonStructureTests(unittest.TestCase):
    def test_every_lesson_has_the_practice_sections(self):
        for level in LEVELS:
            for md in sorted((ROOT / "lessons" / level).glob("[0-9][0-9]_*.md")):
                text = md.read_text(encoding="utf-8")
                with self.subTest(lesson=md.name):
                    self.assertIn("**Outcome:**", text)
                    self.assertIn("**Study time:**", text)
                    self.assertIn("**Before this:**", text)
                    for section in ("## Try it", "## Common mistakes", "## Your turn", "## Quick quiz", "## Summary"):
                        self.assertIn(section, text)
                    self.assertIn("<!-- output -->", text.split("## Try it", 1)[1])
                    self.assertRegex(text, r"\*\*(Next|Next level):\*\*|You've finished the lessons")

    def test_pages_are_current(self):
        result = run("tools.lessons", "--check")
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_level_indexes_are_current(self):
        result = run("tools.level_index", "--check")
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_level_guides_exist(self):
        for level in LEVELS:
            for name in ("README.md", "ASSESSMENT.md", "GLOSSARY.md"):
                self.assertTrue((ROOT / "lessons" / level / name).is_file(), f"{level}/{name}")


class DrillTests(unittest.TestCase):
    def setUp(self):
        self.items = drills.drills()
        self.cases = drills.cases()

    def test_four_drills_per_lesson_and_ids(self):
        for level in LEVELS:
            ids = [d["id"] for d in self.items.values() if d["level"] == level]
            self.assertEqual(ids, [f"{PREFIX[level]}{n:02d}" for n in range(1, 49)])
            for md in sorted((ROOT / "lessons" / level).glob("[0-9][0-9]_*.md")):
                rel = md.relative_to(ROOT).as_posix()
                kinds = sorted(d["kind"] for d in self.items.values() if d["lesson"] == rel)
                self.assertEqual(kinds, ["guided", "guided", "independent", "independent"], rel)

    def test_files_cases_and_hints(self):
        norm = lambda s: " ".join(s.split()).rstrip(";").lower()
        for did, item in self.items.items():
            with self.subTest(drill=did):
                self.assertEqual(len(self.cases[did]), 6)
                self.assertEqual(len(item["hints"]), 3)
                ref = drills.reference_path(did).read_text(encoding="utf-8")
                starter = drills.starter_path(did).read_text(encoding="utf-8")
                self.assertIn(item["signature"], ref)
                self.assertIn(item["signature"], starter)
                if item["kind"] == "guided":
                    self.assertIn("___", starter)
                else:
                    self.assertIn("NotImplementedError", starter)
                body = norm(ref.split(item["signature"], 1)[1])
                for hint in item["hints"]:
                    self.assertFalse(len(hint) > 40 and norm(hint) in body and len(norm(hint)) > 0.8 * len(body), hint)

    def test_references_pass_and_starters_fail(self):
        result = run("tools.drills", "verify-references")
        self.assertEqual(result.returncode, 0, result.stderr)
        for level in LEVELS:
            result = run("tools.drills", "progress", level)
            self.assertIn(f"0/48 {level} drills pass", result.stdout)


class QuizTests(unittest.TestCase):
    def test_every_lesson_has_a_quiz_with_one_right_answer(self):
        quizzes = quiz.quizzes()
        letters = []
        for level in LEVELS:
            for md in sorted((ROOT / "lessons" / level).glob("[0-9][0-9]_*.md")):
                key = f"{level}/{md.name[:2]}"
                self.assertIn(key, quizzes)
                text = md.read_text(encoding="utf-8")
                for n, q in enumerate(quizzes[key]["questions"], 1):
                    hits = [c for c in q["options"] if quiz.fingerprint(key, n, c) == q["answer"]]
                    self.assertEqual(len(hits), 1, f"{key} Q{n}")
                    letters += hits
                    self.assertIn(q["section"], text, f"{key} Q{n} section")
        self.assertLess(max(letters.count(x) for x in set(letters)), 0.6 * len(letters))


class WorkedExampleAndProjectTests(unittest.TestCase):
    def test_six_worked_examples_per_level(self):
        for level in LEVELS:
            pages = sorted((ROOT / "worked_examples" / level).glob("[0-9][0-9]_*.md"))
            self.assertEqual(len(pages), 6, level)
            for md in pages:
                text = md.read_text(encoding="utf-8")
                for part in ("**Problem.**", "## 1. Plan", "## 2.", "## 3.", "## 4.", "**Practise next:**", "<!-- output -->"):
                    self.assertIn(part, text, f"{md.name}: {part}")

    def test_projects(self):
        for level in LEVELS:
            folders = sorted(p for p in (ROOT / "projects" / level).glob("[0-9][0-9]_*") if p.is_dir())
            self.assertEqual(len(folders), 2, level)
            for folder in folders:
                for name in ("README.md", "starter.py", "reference.py", "test_project.py"):
                    self.assertTrue((folder / name).is_file(), f"{folder.name}/{name}")
        result = run("tools.projects", "verify-references")
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_lab_platform_contract(self):
        # SwarmLadder Lab imports exactly one top-level project per level and 12 lessons per level.
        for number in ("01", "02", "03"):
            self.assertEqual(len(list((ROOT / "projects").glob(f"{number}_*.md"))), 1)
        for level in LEVELS:
            self.assertEqual(len(list((ROOT / "lessons" / level).glob("[0-9][0-9]_*.md"))), 12)


class LinkTests(unittest.TestCase):
    def test_relative_links_resolve(self):
        for md in ROOT.rglob("*.md"):
            if ".git" in md.parts:
                continue
            text = re.sub(r"```.*?```", "", md.read_text(encoding="utf-8"), flags=re.S)
            for target in re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", text):
                if "://" in target or target.startswith("mailto:"):
                    continue
                self.assertTrue((md.parent / target).exists(), f"{md.relative_to(ROOT)} -> {target}")


if __name__ == "__main__":
    unittest.main()
