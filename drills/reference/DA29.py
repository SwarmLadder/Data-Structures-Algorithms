"""DA29 reference: 0/1 knapsack in one row. Open after your own attempt."""
def solve(weights, values, cap):
    best = [0] * (cap + 1)
    for w, v in zip(weights, values):
        for c in range(cap, w - 1, -1):
            best[c] = max(best[c], best[c - w] + v)
    return best[cap]
