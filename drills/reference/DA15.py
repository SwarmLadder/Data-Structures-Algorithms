"""DA15 reference: Median of two sorted lists. Open after your own attempt."""
def solve(a, b):
    if len(a) > len(b):
        a, b = b, a
    total, lo, hi = len(a) + len(b), 0, len(a)
    while True:
        i = (lo + hi) // 2
        j = (total + 1) // 2 - i
        al = a[i - 1] if i else float("-inf")
        ar = a[i] if i < len(a) else float("inf")
        bl = b[j - 1] if j else float("-inf")
        br = b[j] if j < len(b) else float("inf")
        if al <= br and bl <= ar:
            if total % 2:
                return float(max(al, bl))
            return (max(al, bl) + min(ar, br)) / 2
        if al > br:
            hi = i - 1
        else:
            lo = i + 1
