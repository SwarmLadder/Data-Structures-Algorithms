"""DA10 — Fewest coins (guided)

Return the fewest coins (unlimited supply of each denomination) that sum to amount,
or -1 if impossible. amount >= 0.

Check: python -m tools.drills check DA10
Hints: python -m tools.drills hint DA10 1
"""

___ = None  # replace every ___ below with your code

def solve(coins, amount):
    INF = float("inf")
    best = [0] + [INF] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                best[a] = min(best[a], ___)
    return best[amount] if best[amount] != INF else ___
