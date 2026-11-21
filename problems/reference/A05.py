"""Reference answer for A05. See the problem statement before reading.
"""
def solve(n, commands):
    parent = list(range(n)); size = [1] * n
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    out = []
    for kind,u,v in commands:
        a,b = find(u),find(v)
        if kind == 'linked':
            out.append(a == b)
        elif a != b:
            if size[a] < size[b]: a,b = b,a
            parent[b] = a
            size[a] += size[b]
    return out
