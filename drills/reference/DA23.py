"""DA23 reference: Number of strongly connected components. Open after your own attempt."""
def solve(n, edges):
    adj = [[] for _ in range(n)]
    radj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        radj[b].append(a)
    order, seen = [], [False] * n
    for s in range(n):
        if seen[s]:
            continue
        stack = [(s, 0)]
        seen[s] = True
        while stack:
            v, i = stack.pop()
            if i < len(adj[v]):
                stack.append((v, i + 1))
                w = adj[v][i]
                if not seen[w]:
                    seen[w] = True
                    stack.append((w, 0))
            else:
                order.append(v)
    assigned = [False] * n
    count = 0
    for s in reversed(order):
        if assigned[s]:
            continue
        count += 1
        stack = [s]
        assigned[s] = True
        while stack:
            v = stack.pop()
            for w in radj[v]:
                if not assigned[w]:
                    assigned[w] = True
                    stack.append(w)
    return count
