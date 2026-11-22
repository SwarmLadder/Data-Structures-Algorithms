"""Source integrity: every exercise is discoverable and executable."""
import ast
import json
import unittest
from pathlib import Path

from tools.practice import ROOT, LEVELS, bank, cases, canonical


class CurriculumTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.problems = bank()
        cls.cases = cases()

    def test_coverage_and_ids(self):
        self.assertEqual(len(self.problems), 48)
        self.assertEqual(set(self.cases), set(self.problems))
        for prefix, level in [('B', 'basics'), ('I', 'intermediate'), ('A', 'advanced')]:
            self.assertEqual(
                [p['id'] for p in self.problems.values() if p['level'] == level],
                [f'{prefix}{number:02}' for number in range(1, 17)],
            )

    def test_prompts_starters_hints_and_edge_fixtures(self):
        for id, p in self.problems.items():
            with self.subTest(id=id):
                self.assertTrue(p['prompt'] and p['constraints'] and p['signature'])
                self.assertGreater(len(p['prompt']), 75)
                self.assertGreaterEqual(len(p['hints']), 2)
                self.assertEqual(len(p['examples']), 2)
                self.assertGreaterEqual(len(self.cases[id]), 6)
                self.assertEqual(p['examples'], self.cases[id][:2])
                for case in self.cases[id]:
                    self.assertIsInstance(case['args'], list)
                    canonical(case['args'])
                    canonical(case['expected'])
                starter = (ROOT / 'problems/starter' / f'{id}.py').read_text()
                reference = (ROOT / 'problems/reference' / f'{id}.py').read_text()
                self.assertIn('NotImplementedError', starter)
                self.assertNotIn('NotImplementedError', reference)
                self.assertIn(p['signature'], starter)
                ast.parse(starter)
                ast.parse(reference)

    def test_lesson_coverage_and_mock_interviews(self):
        for level in LEVELS:
            articles = list((ROOT / 'lessons' / level).glob('[0-9][0-9]_*.md'))
            self.assertGreaterEqual(len(articles), 4, level)
            for article in articles:
                content = article.read_text()
                self.assertGreater(len(content.split()), 220, article.name)
                self.assertIn('##', content)
        self.assertTrue((ROOT / 'interview/MOCK_INTERVIEWS.md').is_file())


if __name__ == '__main__':
    unittest.main()
