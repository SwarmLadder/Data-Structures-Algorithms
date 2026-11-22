"""Tests for the route planner (python -m tools.projects check advanced/01_route_planner)."""
import importlib.util
import itertools
import os
import random
import unittest
from pathlib import Path

_path = Path(os.environ.get("DSA_PROJECT_IMPL", Path(__file__).with_name("reference.py")))
_spec = importlib.util.spec_from_file_location("project_impl", _path)
impl = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(impl)


class RouteTests(unittest.TestCase):
    def planner(self):
        p = impl.RoutePlanner()
        for a, b, m in [("A", "B", 4), ("A", "C", 1), ("C", "B", 2), ("B", "D", 1), ("C", "D", 6)]:
            p.add_road(a, b, m)
        return p

    def test_fastest_route(self):
        self.assertEqual(self.planner().fastest("A", "D"), (4, ["A", "C", "B", "D"]))

    def test_ties_choose_smallest_path(self):
        p = impl.RoutePlanner()
        p.add_road("S", "Y", 1); p.add_road("Y", "T", 1)
        p.add_road("S", "X", 1); p.add_road("X", "T", 1)
        self.assertEqual(p.fastest("S", "T"), (2, ["S", "X", "T"]))

    def test_unreachable_and_validation(self):
        p = self.planner()
        p.add_road("E", "F", 1)
        self.assertEqual(p.fastest("A", "F"), (None, []))
        self.assertEqual(p.fastest("A", "Z"), (None, []))
        with self.assertRaises(ValueError):
            p.add_road("A", "B", -1)

    def test_one_way_roads(self):
        p = impl.RoutePlanner()
        p.add_road("A", "B", 1, two_way=False)
        self.assertEqual(p.fastest("B", "A"), (None, []))

    def test_reachable_within(self):
        self.assertEqual(self.planner().reachable_within("A", 3), ["A", "B", "C"])

    def test_random_against_path_enumeration(self):
        rng = random.Random(505)
        for _ in range(150):
            nodes = "ABCDE"[:rng.randint(2, 5)]
            p = impl.RoutePlanner()
            roads = {}
            for a, b in itertools.combinations(nodes, 2):
                if rng.random() < 0.6:
                    w = rng.randint(0, 4)
                    p.add_road(a, b, w)
                    roads[(a, b)] = roads[(b, a)] = w
            for n in nodes:
                p.adj.setdefault(n, [])
            s, t = nodes[0], nodes[-1]
            best = None
            for k in range(len(nodes) - 1):
                for mid in itertools.permutations(nodes[1:-1], k):
                    path = [s, *mid, t]
                    if all((x, y) in roads for x, y in zip(path, path[1:])):
                        cand = (sum(roads[(x, y)] for x, y in zip(path, path[1:])), path)
                        best = cand if best is None or cand < best else best
            self.assertEqual(p.fastest(s, t), best if best else (None, []))


if __name__ == "__main__":
    unittest.main()
