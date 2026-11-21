"""Public tests and deterministic differential checks for the reference."""

import random
import unittest

from reference import move_zeros


class MoveZerosTests(unittest.TestCase):
    def check_case(self, source: list[int]) -> None:
        expected = [value for value in source if value != 0]
        expected.extend([0] * (len(source) - len(expected)))
        actual = source.copy()
        before_id = id(actual)
        self.assertIsNone(move_zeros(actual))
        self.assertEqual(id(actual), before_id)
        self.assertEqual(actual, expected)

    def test_examples_and_edge_cases(self) -> None:
        for values in (
            [], [0], [0, 0], [7], [5, 4, 3],
            [0, 5, 0, 3, 12, 0, 7], [-1, 0, -2],
            [0, 1, 0, 1, 0, 1], [0] * 100,
        ):
            with self.subTest(values=values):
                self.check_case(values)

    def test_randomized_oracle(self) -> None:
        rng = random.Random(73219)
        for _ in range(300):
            values = [rng.randint(-3, 3) for _ in range(rng.randrange(0, 100))]
            self.check_case(values)


if __name__ == "__main__":
    unittest.main()
