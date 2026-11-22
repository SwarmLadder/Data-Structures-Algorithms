"""DI14 — Values by level (guided)

tree is a nested list [value, left, right] (None for missing). Return a list of
levels, each a list of values left to right.

Check: python -m tools.drills check DI14
Hints: python -m tools.drills hint DI14 1
"""

___ = None  # replace every ___ below with your code

def solve(tree):
    out, level = [], [tree] if tree else []
    while level:
        out.append([node[0] for node in level])
        level = [child for node in level for child in (___, ___) if child]
    return out
