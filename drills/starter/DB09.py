"""DB09 — Only round brackets (guided)

Return True if every '(' in s is closed by a later ')' and no ')' appears without a
matching '('. Other characters are ignored.

Check: python -m tools.drills check DB09
Hints: python -m tools.drills hint DB09 1
"""

___ = None  # replace every ___ below with your code

def solve(s):
    depth = 0
    for ch in s:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if ___:
                return False
    return ___
