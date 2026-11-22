"""DI25 — Sum of all values (guided)

tree is a nested list [value, left, right] or None. Return the sum of all values (0
for an empty tree).

Check: python -m tools.drills check DI25
Hints: python -m tools.drills hint DI25 1
"""

___ = None  # replace every ___ below with your code

def solve(tree):
    if tree is None:
        return 0
    return tree[0] + ___ + ___
