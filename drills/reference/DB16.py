"""DB16 reference: Integer square root. Open after your own attempt."""
def solve(x):
    lo, hi = 0, x + 1
    while lo < hi:
        mid = (lo + hi) // 2
        if mid * mid <= x:
            lo = mid + 1
        else:
            hi = mid
    return lo - 1
