"""DA24 reference: Safe states. Open after your own attempt."""
def solve(n, edges):
    radj = [[] for _ in range(n)]
    outdeg = [0] * n
    for a, b in edges:
        radj[b].append(a)
        outdeg[a] += 1
    ready = [v for v in range(n) if outdeg[v] == 0]
    safe = []
    while ready:
        v = ready.pop()
        safe.append(v)
        for u in radj[v]:
            outdeg[u] -= 1
            if outdeg[u] == 0:
                ready.append(u)
    return sorted(safe)
