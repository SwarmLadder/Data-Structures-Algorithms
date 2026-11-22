"""DA43 reference: Find a counterexample to a greedy rule. Open after your own attempt."""
def solve(coins, limit):
    best = [0] + [float("inf")] * limit
    for a in range(1, limit + 1):
        best[a] = min(best[a - c] + 1 for c in coins if c <= a)
    bad = []
    for a in range(1, limit + 1):
        left, used = a, 0
        for c in sorted(coins, reverse=True):
            used += left // c
            left %= c
        if used > best[a]:
            bad.append(a)
    return bad
