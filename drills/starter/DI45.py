"""DI45 — Pick the technique (guided)

Given flags describing a subarray-sum problem, return 'sliding window' if all values
are positive, 'prefix sums' if values may be negative, and 'brute force' if n <= 50
regardless.

Check: python -m tools.drills check DI45
Hints: python -m tools.drills hint DI45 1
"""

___ = None  # replace every ___ below with your code

def solve(n, all_positive):
    if n <= 50:
        return ___
    return "sliding window" if ___ else "prefix sums"
