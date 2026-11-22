"""DA05 reference: Union–find: count groups after merges. Open after your own attempt."""
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
            parent[rb] = ra
            groups -= 1
    return groups
