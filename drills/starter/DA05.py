"""DA05 — Union–find: count groups after merges (guided)

n items start in their own groups. Apply every union [a, b] in order and return the
number of groups.

Check: python -m tools.drills check DA05
Hints: python -m tools.drills hint DA05 1
"""

___ = None  # replace every ___ below with your code

def solve(n, unions):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    groups = n
    for a, b in unions:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ___
            groups -= ___
    return groups
