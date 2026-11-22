"""DI34 — Assign cookies (guided)

Child i is content with a cookie of size >= greed[i]. Each child gets at most one
cookie. Return the maximum number of content children.

Check: python -m tools.drills check DI34
Hints: python -m tools.drills hint DI34 1
"""

___ = None  # replace every ___ below with your code

def solve(greed, sizes):
    greed, sizes = sorted(greed), sorted(sizes)
    child = 0
    for cookie in sizes:
        if child < len(greed) and cookie >= ___:
            child += 1
    return ___
