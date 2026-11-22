"""DA40 reference: Rollback union–find. Open after your own attempt."""
def solve(n, ops):
    parent, size, history, out = list(range(n)), [1] * n, [], []
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for op in ops:
        if op[0] == "union":
            ra, rb = find(op[1]), find(op[2])
            if ra != rb:
                if size[ra] < size[rb]:
                    ra, rb = rb, ra
                parent[rb] = ra
                size[ra] += size[rb]
                history.append((rb, ra))
        elif op[0] == "same":
            out.append(find(op[1]) == find(op[2]))
        elif history:
            child, root = history.pop()
            parent[child] = child
            size[root] -= size[child]
    return out
