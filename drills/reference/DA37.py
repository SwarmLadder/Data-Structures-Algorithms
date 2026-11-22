"""DA37 reference: Union by size: largest group. Open after your own attempt."""
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
        size[ra] += size[rb]
        best = max(best, size[ra])
    return best
