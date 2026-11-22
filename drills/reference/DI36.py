"""DI36 reference: Does greedy coin change fail?. Open after your own attempt."""
def solve(coins, limit):
    best = [0] + [float("inf")] * limit
    for a in range(1, limit + 1):
        for c in coins:
            if c <= a:
                best[a] = min(best[a], best[a - c] + 1)
    for a in range(1, limit + 1):
        left, used = a, 0
        for c in sorted(coins, reverse=True):
            used += left // c
            left %= c
        if used > best[a]:
            return a
    return -1
