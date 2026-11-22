"""Tests for the rate limiter (python -m tools.projects check intermediate/01_rate_limiter)."""
import importlib.util
import os
import random
import unittest
from pathlib import Path

_path = Path(os.environ.get("DSA_PROJECT_IMPL", Path(__file__).with_name("reference.py")))
_spec = importlib.util.spec_from_file_location("project_impl", _path)
impl = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(impl)


class LimiterTests(unittest.TestCase):
    def test_basic_limit(self):
        lim = impl.SlidingWindowLimiter(2, 10)
        self.assertEqual([lim.allow("a", t) for t in (0, 1, 2, 10, 11, 12)], [True, True, False, True, True, False])

    def test_clients_are_independent(self):
        lim = impl.SlidingWindowLimiter(1, 5)
        self.assertTrue(lim.allow("a", 0))
        self.assertTrue(lim.allow("b", 0))
        self.assertFalse(lim.allow("a", 4))
        self.assertTrue(lim.allow("a", 5))

    def test_busiest_and_counts(self):
        times = [1, 2, 3, 10, 11, 30]
        self.assertEqual(impl.busiest_window(times, 5), 3)
        self.assertEqual(impl.busiest_window([], 5), 0)
        self.assertEqual(impl.requests_between(times, [(0, 4), (3, 11), (31, 40)]), [3, 2, 0])

    def test_random_against_oracle(self):
        rng = random.Random(303)
        for _ in range(300):
            limit, window = rng.randint(1, 3), rng.randint(1, 6)
            lim = impl.SlidingWindowLimiter(limit, window)
            accepted = []
            t = 0
            for _ in range(rng.randint(0, 20)):
                t += rng.randint(0, 3)
                expect = sum(1 for a in accepted if a > t - window) < limit
                self.assertEqual(lim.allow("c", t), expect)
                if expect:
                    accepted.append(t)
            times = sorted(rng.randint(0, 20) for _ in range(rng.randint(0, 10)))
            brute = max([sum(1 for x in times if s <= x < s + window) for s in times] or [0])
            self.assertEqual(impl.busiest_window(times, window), brute)


if __name__ == "__main__":
    unittest.main()
