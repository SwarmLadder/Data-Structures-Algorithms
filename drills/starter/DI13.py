"""DI13 — Height of a tree (guided)

tree is a nested list [value, left, right] with None for missing children (or tree
itself is None). Return the number of nodes on the longest root-to-leaf path (0 for
an empty tree).

Check: python -m tools.drills check DI13
Hints: python -m tools.drills hint DI13 1
"""

___ = None  # replace every ___ below with your code

def solve(tree):
    if tree is None:
        return ___
    return 1 + max(___, ___)
