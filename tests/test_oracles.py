"""Independent small-input oracles catch incorrect reference implementations.

No expected values are generated from the submitted function under test.
"""
import itertools
import random
import runpy
import unittest
from collections import Counter, deque
from functools import lru_cache
from pathlib import Path

from tools.practice import ROOT


@lru_cache(None)
def ref(problem_id):
    return runpy.run_path(str(ROOT / 'problems/reference' / f'{problem_id}.py'))['solve']


class DifferentialTests(unittest.TestCase):
    def setUp(self):
        self.rng = random.Random(17304)

    def test_lower_bound(self):
        for _ in range(100):
            data = sorted(self.rng.choices(range(-10, 11), k=self.rng.randint(0, 30)))
            target = self.rng.randint(-12, 12)
            expected = next((i for i, value in enumerate(data) if value >= target), len(data))
            self.assertEqual(ref('B05')(data, target), expected)

    def test_maximum_subarray(self):
        for _ in range(100):
            data = [self.rng.randint(-10, 10) for _ in range(self.rng.randint(1, 14))]
            expected = max(sum(data[i:j]) for i in range(len(data)) for j in range(i+1, len(data)+1))
            self.assertEqual(ref('B07')(data), expected)

    def test_product_without_division(self):
        for _ in range(100):
            nums = [self.rng.randint(-3, 3) for _ in range(self.rng.randint(2, 14))]
            expected = [__import__('math').prod(nums[:i]+nums[i+1:]) for i in range(len(nums))]
            self.assertEqual(ref('B16')(nums), expected)

    def test_minimum_covering_window(self):
        alphabet = 'aabBc'
        for _ in range(120):
            text = ''.join(self.rng.choices(alphabet, k=self.rng.randint(0, 10)))
            need = ''.join(self.rng.choices(alphabet, k=self.rng.randint(0, 5)))
            options = [text[i:j] for i in range(len(text)) for j in range(i+1, len(text)+1)
                       if not (Counter(need) - Counter(text[i:j]))]
            expected = min(options, key=len) if options and need else ''
            self.assertEqual(ref('I02')(text, need), expected, (text, need))

    def test_subarray_count_with_negatives(self):
        for _ in range(100):
            nums = [self.rng.randint(-5, 5) for _ in range(self.rng.randint(0, 12))]
            target = self.rng.randint(-6, 6)
            expected = sum(sum(nums[i:j]) == target for i in range(len(nums))
                           for j in range(i+1, len(nums)+1))
            self.assertEqual(ref('I03')(nums, target), expected)

    def test_concurrent_workers_by_sweep(self):
        for _ in range(100):
            jobs = []
            for _ in range(self.rng.randint(0, 14)):
                start = self.rng.randint(0, 15)
                jobs.append([start, start + self.rng.randint(1, 5)])
            times = [item for job in jobs for item in job]
            expected = max((sum(a <= t < b for a, b in jobs) for t in times), default=0)
            self.assertEqual(ref('I07')(jobs), expected)

    def test_rotated_search(self):
        for _ in range(100):
            data = sorted(self.rng.sample(range(-30, 30), self.rng.randint(0, 20)))
            rotation = self.rng.randint(0, len(data))
            rotated = data[rotation:] + data[:rotation]
            target = self.rng.randint(-30, 30)
            expected = rotated.index(target) if target in rotated else -1
            self.assertEqual(ref('I10')(rotated, target), expected)
            if data:
                self.assertEqual(ref('I11')(rotated), min(data))

    def test_lru_cache_against_simple_model(self):
        for _ in range(100):
            cap = self.rng.randint(0, 4)
            ops = []
            cache = {}
            order = []
            expected = []
            for _ in range(self.rng.randint(0, 40)):
                key = self.rng.randint(0, 5)
                if self.rng.randrange(3) == 0:
                    ops.append(['get', key])
                    expected.append(cache.get(key, -1))
                    if key in order:
                        order.remove(key); order.append(key)
                else:
                    value = self.rng.randint(0, 50)
                    ops.append(['put', key, value])
                    cache[key] = value
                    if key in order: order.remove(key)
                    order.append(key)
                    if len(order) > cap:
                        oldest = order.pop(0)
                        del cache[oldest]
            self.assertEqual(ref('I12')(cap, ops), expected)

    def test_cycle_detection(self):
        for _ in range(100):
            n = self.rng.randint(0, 16)
            next_index = [self.rng.randint(-1, n-1) for _ in range(n)]
            start = self.rng.randint(-1, n-1)
            visited = set()
            node = start
            while node != -1 and node not in visited:
                visited.add(node)
                node = next_index[node]
            self.assertEqual(ref('I16')(next_index, start), node != -1)

    def test_dijkstra_against_bellman_ford(self):
        for _ in range(100):
            n = self.rng.randint(1, 7)
            edges = [[self.rng.randrange(n), self.rng.randrange(n), self.rng.randrange(15)]
                     for _ in range(self.rng.randint(0, 18))]
            src = self.rng.randrange(n)
            distances = [float('inf')] * n
            distances[src] = 0
            for _ in range(n-1):
                for u, v, weight in edges:
                    distances[v] = min(distances[v], distances[u] + weight)
            expected = [-1 if d == float('inf') else int(d) for d in distances]
            self.assertEqual(ref('A04')(n, edges, src), expected)

    def test_mst_against_all_spanning_trees(self):
        for _ in range(60):
            n = self.rng.randint(0, 5)
            pairs = [(i, j) for i in range(n) for j in range(i+1, n)]
            chosen = self.rng.sample(pairs, min(len(pairs), self.rng.randint(0, 7)))
            edges = [[u, v, self.rng.randint(0, 12)] for u, v in chosen]
            if n <= 1:
                expected = 0
            else:
                costs = []
                for subset in itertools.combinations(edges, n-1):
                    graph = [[] for _ in range(n)]
                    for u, v, w in subset:
                        graph[u].append(v); graph[v].append(u)
                    reachable = {0}; stack = [0]
                    while stack:
                        for v in graph[stack.pop()]:
                            if v not in reachable:
                                reachable.add(v); stack.append(v)
                    if len(reachable) == n:
                        costs.append(sum(w for _, _, w in subset))
                expected = min(costs) if costs else -1
            self.assertEqual(ref('A06')(n, edges), expected)

    def test_lis_by_subsequence_enumeration(self):
        for _ in range(100):
            nums = [self.rng.randint(-4, 4) for _ in range(self.rng.randint(0, 11))]
            valid = [len(choice) for r in range(len(nums)+1) for choice in itertools.combinations(nums, r)
                     if all(a < b for a, b in zip(choice, choice[1:]))]
            self.assertEqual(ref('A09')(nums), max(valid))

    def test_knapsack_against_all_subsets(self):
        for _ in range(80):
            upgrades = [[self.rng.randint(1, 8), self.rng.randint(0, 15)]
                        for _ in range(self.rng.randint(0, 10))]
            budget = self.rng.randint(0, 20)
            expected = max((sum(v for _, v in choice) for r in range(len(upgrades)+1)
                            for choice in itertools.combinations(upgrades, r)
                            if sum(cost for cost, _ in choice) <= budget), default=0)
            self.assertEqual(ref('A11')(upgrades, budget), expected)

    def test_prefix_suggestions_against_sorting(self):
        for _ in range(100):
            words = [''.join(self.rng.choices('abc', k=self.rng.randint(0, 5)))
                     for _ in range(self.rng.randint(0, 18))]
            prefix = ''.join(self.rng.choices('abc', k=self.rng.randint(0, 3)))
            k = self.rng.randint(0, 9)
            expected = sorted({word for word in words if word.startswith(prefix)})[:k]
            self.assertEqual(ref('A13')(words, prefix, k), expected)

    def test_sorted_median_against_merge(self):
        for _ in range(100):
            a = sorted(self.rng.choices(range(-15, 16), k=self.rng.randint(0, 16)))
            b = sorted(self.rng.choices(range(-15, 16), k=self.rng.randint(0, 16)))
            if not a and not b: continue
            values = sorted(a + b)
            mid = len(values) // 2
            expected = float(values[mid]) if len(values) % 2 else (values[mid-1]+values[mid])/2.0
            self.assertEqual(ref('A16')(a,b), expected)


if __name__ == '__main__':
    unittest.main()
