"""Tests for the build system (python -m tools.projects check advanced/02_build_system)."""
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


def sample():
    g = impl.BuildGraph()
    g.add("app", 4, ["lib", "assets"])
    g.add("lib", 3, ["codegen"])
    g.add("codegen", 2)
    g.add("assets", 1)
    g.add("tests", 2, ["app"])
    return g


class BuildTests(unittest.TestCase):
    def test_order(self):
        self.assertEqual(sample().order(), ["assets", "codegen", "lib", "app", "tests"])

    def test_cycle_is_reported(self):
        g = impl.BuildGraph()
        g.add("a", 1, ["b"]); g.add("b", 1, ["a"]); g.add("c", 1)
        with self.assertRaises(ValueError) as ctx:
            g.order()
        self.assertIn("a", str(ctx.exception))

    def test_critical_path(self):
        self.assertEqual(sample().critical_path(), (11, ["codegen", "lib", "app", "tests"]))
        self.assertEqual(impl.BuildGraph().critical_path(), (0, []))

    def test_to_rebuild(self):
        g = sample()
        self.assertEqual(g.to_rebuild(["codegen"]), ["codegen", "lib", "app", "tests"])
        self.assertEqual(g.to_rebuild(["tests"]), ["tests"])
        self.assertEqual(g.to_rebuild([]), [])

    def test_random_order_respects_dependencies(self):
        rng = random.Random(606)
        for _ in range(200):
            names = [f"t{i}" for i in range(rng.randint(1, 7))]
            g = impl.BuildGraph()
            for i, n in enumerate(names):
                deps = [m for m in names[:i] if rng.random() < 0.4]
                g.add(n, rng.randint(0, 5), deps)
            order = g.order()
            pos = {t: k for k, t in enumerate(order)}
            self.assertEqual(sorted(order), sorted(names))
            for t, ds in g.deps.items():
                for d in ds:
                    self.assertLess(pos[d], pos[t])
            # critical path equals the brute-force longest chain
            def longest(t):
                return g.cost[t] + max([longest(d) for d in g.deps[t]] or [0])
            self.assertEqual(g.critical_path()[0], max(longest(t) for t in names))


if __name__ == "__main__":
    unittest.main()
