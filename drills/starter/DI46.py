"""DI46 — Feasible complexity for n (guided)

Return the slowest complexity class among ['O(n^2)', 'O(n log n)', 'O(n)'] whose
operation count stays at or under 10**8 for the given n (use n*n, n*log2(n), n). If
none fit, return 'too large'.

Check: python -m tools.drills check DI46
Hints: python -m tools.drills hint DI46 1
"""

___ = None  # replace every ___ below with your code

import math

def solve(n):
    log = math.log2(n) if n > 1 else 1
    for name, ops in [("O(n^2)", n * n), ("O(n log n)", n * log), ("O(n)", n)]:
        if ops <= ___:
            return ___
    return "too large"
