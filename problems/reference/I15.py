"""Reference answer for I15. See the problem statement before reading.
"""
def solve(tree, p, q):
    i = 0
    lo, hi = sorted((p,q))
    while i < len(tree):
        x = tree[i]
        if lo <= x <= hi:
            return x
        i = 2*i + 1 if hi < x else 2*i + 2
    raise ValueError('Missing node')
