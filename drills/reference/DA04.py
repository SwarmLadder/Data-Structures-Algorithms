"""DA04 reference: Does a directed graph have a cycle?. Open after your own attempt."""
def solve(n, edges):
    out = [[] for _ in range(n)]
    indegree = [0] * n
    for a, b in edges:
        out[a].append(b)
        indegree[b] += 1
    ready = [v for v in range(n) if indegree[v] == 0]
    seen = 0
    while ready:
        v = ready.pop()
        seen += 1
        for w in out[v]:
            indegree[w] -= 1
            if indegree[w] == 0:
                ready.append(w)
    return seen != n
