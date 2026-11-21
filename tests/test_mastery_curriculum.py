"""Mastery course must remain deep, navigable and technically executable."""
from pathlib import Path
import ast
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class MasteryCurriculumTests(unittest.TestCase):
    def test_36_detailed_lessons(self):
        all_docs = []
        for level in ('basics', 'intermediate', 'advanced'):
            docs = sorted((ROOT / 'lessons' / level).glob('[0-9][0-9]_*.md'))
            self.assertEqual(len(docs), 12, level)
            self.assertEqual([int(doc.name[:2]) for doc in docs], list(range(1, 13)), level)
            all_docs.extend(docs)
        for path in all_docs:
            with self.subTest(lesson=str(path.relative_to(ROOT))):
                content = path.read_text(encoding='utf-8')
                self.assertGreaterEqual(len(content.split()), 450, path)
                self.assertIn('```python', content)
                self.assertIn('O(', content)
                self.assertTrue(any(word in content.lower() for word in
                                    ('invariant', 'proof', 'induction', 'correctness')), path)
                self.assertTrue(any(word in content.lower() for word in
                                    ('practice', 'drill', 'exercise')), path)
                for snippet in re.findall(r'```python\n(.*?)\n```', content, flags=re.S):
                    ast.parse(snippet, filename=str(path))

    def test_48_full_problem_walkthroughs(self):
        for prefix in 'BIA':
            for i in range(1, 17):
                problem_id = f'{prefix}{i:02}'
                path = ROOT / 'problems' / f'{problem_id}.md'
                content = path.read_text(encoding='utf-8')
                with self.subTest(problem_id=problem_id):
                    self.assertGreaterEqual(len(content.split()), 450)
                    self.assertIn('## Deep solution study (open after attempting)', content)
                    self.assertIn('### B. Invariant or recurrence', content)
                    self.assertIn('### C. Work through a real example', content)
                    self.assertIn('### D. Executable reference implementation', content)
                    self.assertIn('### E. Complexity derivation', content)
                    self.assertIn('### F. Failure modes', content)
                    self.assertIn('### G. Transfer the technique', content)
                    self.assertIn('</details>', content)
                    self.assertIn('```python', content)
                    for snippet in re.findall(r'```python\n(.*?)\n```', content, flags=re.S):
                        ast.parse(snippet)

    def test_advanced_projects_and_mastery_resources(self):
        for name in ('01_log_signal_analyzer.md', '02_job_scheduling_engine.md',
                     '03_dependency_planner.md'):
            text = (ROOT / 'projects' / name).read_text(encoding='utf-8')
            self.assertGreaterEqual(len(text.split()), 700, name)
            self.assertIn('oracle', text.lower())
            self.assertIn('complexity', text.lower())
        for document in ('MASTERY_ROADMAP.md', 'PROOF_TECHNIQUES.md',
                         'PATTERN_ATLAS.md', 'MASTERY_ASSESSMENT.md'):
            text = (ROOT / document).read_text(encoding='utf-8')
            self.assertGreaterEqual(len(text.split()), 400, document)
        self.assertIn('12-week', (ROOT / 'README.md').read_text())
        self.assertIn('Fenwick', (ROOT / 'lessons/README.md').read_text())


if __name__ == '__main__':
    unittest.main()
