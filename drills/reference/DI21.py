"""DI21 reference: First true in a monotone predicate. Open after your own attempt."""
def solve(flags):
    lo, hi = 0, len(flags)
    while lo < hi:
        mid = (lo + hi) // 2
        if flags[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo
