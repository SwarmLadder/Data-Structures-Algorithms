"""DA29 — 0/1 knapsack in one row (guided)

Return the maximum total value of items (each used at most once) with total weight
<= cap.

Check: python -m tools.drills check DA29
Hints: python -m tools.drills hint DA29 1
"""

___ = None  # replace every ___ below with your code

def solve(weights, values, cap):
    best = [0] * (cap + 1)
    for w, v in zip(weights, values):
        for c in range(___, w - 1, -1):
            best[c] = max(best[c], ___)
    return best[cap]
