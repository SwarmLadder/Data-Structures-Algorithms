"""DI22 — Ship within d days (guided)

Packages with the given weights must ship in order, at most one day's capacity per
day. Return the smallest daily capacity that ships everything within days days.

Check: python -m tools.drills check DI22
Hints: python -m tools.drills hint DI22 1
"""

___ = None  # replace every ___ below with your code

def solve(weights, days):
    def feasible(cap):
        need, load = 1, 0
        for w in weights:
            if load + w > cap:
                need, load = need + 1, 0
            load += w
        return need <= days
    lo, hi = max(weights), sum(weights)
    while lo < hi:
        mid = (lo + hi) // 2
        if ___:
            hi = mid
        else:
            lo = mid + 1
    return ___
