"""DA34 — Range minimum queries (guided)

Return the minimum of data[lo:hi] for each [lo, hi] in queries (half-open, non-
empty), using an iterative segment tree.

Check: python -m tools.drills check DA34
Hints: python -m tools.drills hint DA34 1
"""

___ = None  # replace every ___ below with your code

def solve(data, queries):
    n = len(data)
    t = [float("inf")] * (2 * n)
    t[n:] = data
    for i in range(n - 1, 0, -1):
        t[i] = min(t[2 * i], ___)
    out = []
    for lo, hi in queries:
        res, lo, hi = float("inf"), lo + n, hi + n
        while lo < hi:
            if lo & 1:
                res = min(res, t[lo]); lo += 1
            if hi & 1:
                hi -= 1; res = min(res, ___)
            lo //= 2; hi //= 2
        out.append(res)
    return out
