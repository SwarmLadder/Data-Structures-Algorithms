"""DA30 — Count coin combinations (guided)

Return the number of combinations (order doesn't matter) of coins (unlimited supply)
that sum to amount.

Check: python -m tools.drills check DA30
Hints: python -m tools.drills hint DA30 1
"""

___ = None  # replace every ___ below with your code

def solve(amount, coins):
    ways = [1] + [0] * amount
    for c in coins:
        for a in range(___, amount + 1):
            ways[a] += ___
    return ways[amount]
