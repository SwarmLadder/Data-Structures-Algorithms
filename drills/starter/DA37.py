"""DA37 — Union by size: largest group (guided)

Apply the unions [a, b] to n singleton groups and return the size of the largest
group.

Check: python -m tools.drills check DA37
Hints: python -m tools.drills hint DA37 1
"""

___ = None  # replace every ___ below with your code

def solve(n, unions):
    parent, size = list(range(n)), [1] * n
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    best = 1 if n else 0
    for a, b in unions:
        ra, rb = find(a), find(b)
        if ra == rb:
            continue
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += ___
        best = max(best, ___)
    return best
