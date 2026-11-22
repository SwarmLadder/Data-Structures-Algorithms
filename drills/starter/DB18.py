"""DB18 — How many halvings? (guided)

Return how many times you can integer-halve n (n = n // 2) before it reaches 1, for
n >= 1. This is floor(log2 n).

Check: python -m tools.drills check DB18
Hints: python -m tools.drills hint DB18 1
"""

___ = None  # replace every ___ below with your code

def solve(n):
    steps = 0
    while ___:
        n //= 2
        steps += 1
    return steps
