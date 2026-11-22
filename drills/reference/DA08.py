"""DA08 reference: First redundant connection. Open after your own attempt."""
def solve(edges):
    n = max((max(e) for e in edges), default=0)
    parent = list(range(n + 1))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra == rb:
            return [a, b]
        parent[rb] = ra
    return []
