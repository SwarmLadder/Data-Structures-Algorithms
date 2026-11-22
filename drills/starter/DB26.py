"""DB26 — Power by squaring (guided)

Return base ** exp for an integer base and exp >= 0, using recursion that halves exp
(O(log exp) multiplications).

Check: python -m tools.drills check DB26
Hints: python -m tools.drills hint DB26 1
"""

___ = None  # replace every ___ below with your code

def solve(base, exp):
    if exp == 0:
        return 1
    half = solve(base, ___)
    result = half * half
    if exp % 2 == 1:
        result *= ___
    return result
