"""Tests for the autocomplete service (python -m tools.projects check intermediate/02_autocomplete_service)."""
import importlib.util
import os
import random
import unittest
from pathlib import Path

_path = Path(os.environ.get("DSA_PROJECT_IMPL", Path(__file__).with_name("reference.py")))
_spec = importlib.util.spec_from_file_location("project_impl", _path)
impl = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(impl)


class AutocompleteTests(unittest.TestCase):
    def setUp(self):
        self.ac = impl.Autocomplete(k=3)
        for q, n in [("deploy", 5), ("delete", 5), ("describe", 2), ("diff", 9), ("de", 1)]:
            self.ac.record(q, n)

    def test_suggest_orders_by_count_then_name(self):
        self.assertEqual(self.ac.suggest("de"), ["delete", "deploy", "describe"])
        self.assertEqual(self.ac.suggest("d"), ["diff", "delete", "deploy"])

    def test_unknown_prefix_and_exact_word(self):
        self.assertEqual(self.ac.suggest("x"), [])
        self.assertEqual(self.ac.suggest("diff"), ["diff"])

    def test_counts_accumulate(self):
        self.ac.record("describe", 10)
        self.assertEqual(self.ac.suggest("des"), ["describe"])
        self.assertEqual(self.ac.top_overall(1), ["describe"])

    def test_random_against_brute_force(self):
        rng = random.Random(404)
        for _ in range(150):
            ac = impl.Autocomplete(k=rng.randint(1, 4))
            counts = {}
            for _ in range(rng.randint(0, 15)):
                q = "".join(rng.choice("ab") for _ in range(rng.randint(1, 4)))
                n = rng.randint(1, 3)
                ac.record(q, n)
                counts[q] = counts.get(q, 0) + n
            for prefix in ["", "a", "b", "ab", "ba", "aaa"]:
                expected = sorted((q for q in counts if q.startswith(prefix)), key=lambda q: (-counts[q], q))[:ac.k]
                self.assertEqual(ac.suggest(prefix), expected)


if __name__ == "__main__":
    unittest.main()
