"""Tests for the inventory reconciler (run with python -m tools.projects check basics/01_inventory_reconciler)."""
import importlib.util
import os
import random
import unittest
from pathlib import Path

_path = Path(os.environ.get("DSA_PROJECT_IMPL", Path(__file__).with_name("reference.py")))
_spec = importlib.util.spec_from_file_location("project_impl", _path)
impl = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(impl)


class InventoryTests(unittest.TestCase):
    def test_parse(self):
        lines = ["# warehouse A", "P1, 3", "", "P2,5", "P1,2"]
        self.assertEqual(impl.parse(lines), {"P1": 5, "P2": 5})
        self.assertEqual(impl.parse([]), {})

    def test_diff(self):
        self.assertEqual(impl.diff({"A": 1, "B": 2}, {"B": 3, "C": 1}), [("A", 1, 0), ("B", 2, 3), ("C", 0, 1)])
        self.assertEqual(impl.diff({"A": 1}, {"A": 1}), [])

    def test_merge_sorted(self):
        self.assertEqual(impl.merge_sorted_skus(["A", "C"], ["B", "C", "D"]), ["A", "B", "C", "D"])
        self.assertEqual(impl.merge_sorted_skus([], []), [])

    def test_worst(self):
        d = [("A", 1, 0), ("B", 2, 9), ("C", 5, 12)]
        self.assertEqual(impl.worst(d, 2), [("B", 2, 9), ("C", 5, 12)])
        self.assertEqual(impl.worst([], 3), [])

    def test_random_against_oracles(self):
        rng = random.Random(101)
        for _ in range(300):
            a = sorted(set(rng.choice("ABCDEFG") for _ in range(rng.randint(0, 6))))
            b = sorted(set(rng.choice("ABCDEFG") for _ in range(rng.randint(0, 6))))
            self.assertEqual(impl.merge_sorted_skus(a, b), sorted(set(a) | set(b)))
            exp = {s: rng.randint(0, 3) for s in a}
            cnt = {s: rng.randint(0, 3) for s in b}
            expected = [(s, exp.get(s, 0), cnt.get(s, 0)) for s in sorted(set(exp) | set(cnt)) if exp.get(s, 0) != cnt.get(s, 0)]
            self.assertEqual(impl.diff(exp, cnt), expected)


if __name__ == "__main__":
    unittest.main()
