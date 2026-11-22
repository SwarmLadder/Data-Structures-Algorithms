"""Tests for the undo editor (python -m tools.projects check basics/02_undo_editor)."""
import importlib.util
import os
import random
import unittest
from pathlib import Path

_path = Path(os.environ.get("DSA_PROJECT_IMPL", Path(__file__).with_name("reference.py")))
_spec = importlib.util.spec_from_file_location("project_impl", _path)
impl = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(impl)


class EditorTests(unittest.TestCase):
    def test_typing_and_cursor(self):
        e = impl.Editor()
        e.type("helo")
        e.move(-1)
        e.type("l")
        self.assertEqual((e.text, e.cursor), ("hello", 4))

    def test_backspace_clamps(self):
        e = impl.Editor()
        e.type("ab")
        e.backspace(5)
        self.assertEqual((e.text, e.cursor), ("", 0))
        self.assertTrue(e.undo())            # the backspace itself is undoable
        self.assertEqual(e.text, "ab")

    def test_undo_redo(self):
        e = impl.Editor()
        e.type("a"); e.type("b"); e.type("c")
        self.assertTrue(e.undo()); self.assertEqual(e.text, "ab")
        self.assertTrue(e.undo()); self.assertEqual(e.text, "a")
        self.assertTrue(e.redo()); self.assertEqual(e.text, "ab")
        e.type("X")
        self.assertFalse(e.redo())           # new change clears redo
        self.assertEqual(e.text, "abX")

    def test_nothing_to_undo(self):
        e = impl.Editor()
        self.assertFalse(e.undo())
        self.assertFalse(e.redo())

    def test_random_against_history_oracle(self):
        rng = random.Random(202)
        for _ in range(200):
            e = impl.Editor()
            history = [("", 0)]                # oracle: list of states, pointer into it
            pos = 0
            for _ in range(25):
                op = rng.choice(["type", "back", "move", "undo", "redo"])
                if op == "type":
                    s = rng.choice(["a", "bc", ""])
                    e.type(s)
                    if s:
                        t, c = history[pos]
                        history = history[:pos + 1] + [(t[:c] + s + t[c:], c + len(s))]
                        pos += 1
                elif op == "back":
                    n = rng.randint(1, 3)
                    t, c = history[pos]
                    e.backspace(n)
                    if min(n, c):
                        n = min(n, c)
                        history = history[:pos + 1] + [(t[:c - n] + t[c:], c - n)]
                        pos += 1
                elif op == "move":
                    k = rng.randint(-2, 2)
                    e.move(k)
                    t, c = history[pos]
                    history[pos] = (t, max(0, min(len(t), c + k)))
                elif op == "undo":
                    ok = e.undo()
                    self.assertEqual(ok, pos > 0)
                    if pos > 0:
                        pos -= 1
                else:
                    ok = e.redo()
                    self.assertEqual(ok, pos < len(history) - 1)
                    if ok:
                        pos += 1
                self.assertEqual(e.text, history[pos][0])


if __name__ == "__main__":
    unittest.main()
