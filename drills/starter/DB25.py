"""DB25 — Sum of digits, recursively (guided)

Return the sum of the decimal digits of a non-negative integer n using recursion.

Check: python -m tools.drills check DB25
Hints: python -m tools.drills hint DB25 1
"""

___ = None  # replace every ___ below with your code

def solve(n):
    if n < 10:
        return ___
    return n % 10 + ___
