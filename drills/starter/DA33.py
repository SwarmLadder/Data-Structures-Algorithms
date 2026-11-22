"""DA33 — Range sums with point updates (guided)

Start from values. ops is a list of ['add', i, delta] or ['sum', lo, hi] (half-
open). Return the results of every 'sum' in order, using a Fenwick tree.

Check: python -m tools.drills check DA33
Hints: python -m tools.drills hint DA33 1
"""

___ = None  # replace every ___ below with your code

def solve(values, ops):
    tree = [0] * (len(values) + 1)
    def add(i, delta):
        i += 1
        while i < len(tree):
            tree[i] += delta
            i += i & -i
    def prefix(i):
        total = 0
        while i > 0:
            total += tree[i]
            i -= ___
        return total
    for i, v in enumerate(values):
        add(i, v)
    out = []
    for op in ops:
        if op[0] == "add":
            add(op[1], op[2])
        else:
            out.append(___)
    return out
