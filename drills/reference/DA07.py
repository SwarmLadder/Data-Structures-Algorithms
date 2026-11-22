"""DA07 reference: Minimum spanning tree cost. Open after your own attempt."""
def solve(n, edges):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    total = used = 0
    for a, b, w in sorted(edges, key=lambda e: e[2]):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra
            total += w
            used += 1
    return total if used == n - 1 else -1
