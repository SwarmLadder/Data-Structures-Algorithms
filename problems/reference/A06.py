"""Reference answer for A06. See the problem statement before reading.
"""
def solve(n, links):
    if n <= 1:
        return 0
    parent = list(range(n)); size = [1]*n
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    total = used = 0
    for u,v,cost in sorted(links,key=lambda e:e[2]):
        a,b = find(u),find(v)
        if a == b: continue
        if size[a] < size[b]: a,b = b,a
        parent[b] = a; size[a] += size[b]
        total += cost; used += 1
        if used == n-1: return total
    return -1
