"""DA34 reference: Range minimum queries. Open after your own attempt."""
def solve(data, queries):
    n = len(data)
    t = [float("inf")] * (2 * n)
    t[n:] = data
    for i in range(n - 1, 0, -1):
        t[i] = min(t[2 * i], t[2 * i + 1])
    out = []
    for lo, hi in queries:
        res, lo, hi = float("inf"), lo + n, hi + n
        while lo < hi:
            if lo & 1:
                res = min(res, t[lo]); lo += 1
            if hi & 1:
                hi -= 1; res = min(res, t[hi])
            lo //= 2; hi //= 2
        out.append(res)
    return out
