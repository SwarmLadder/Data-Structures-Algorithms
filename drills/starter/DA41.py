"""DA41 — A tiny differential tester (guided)

Return the list of inputs (from inputs) on which candidate(x) != oracle(x), where
oracle sorts x and candidate is 'sorted unless the list has exactly 2 elements, then
unchanged'.

Check: python -m tools.drills check DA41
Hints: python -m tools.drills hint DA41 1
"""

___ = None  # replace every ___ below with your code

def solve(inputs):
    def oracle(x):
        return sorted(x)
    def candidate(x):
        return list(x) if len(x) == 2 else sorted(x)
    return [x for x in inputs if ___ != ___]
