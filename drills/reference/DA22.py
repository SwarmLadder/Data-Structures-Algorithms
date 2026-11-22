"""DA22 reference: Topological order by DFS finish times. Open after your own attempt."""
def solve(n, edges):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
    for lst in adj:
        lst.sort()
    seen, finished = set(), []
    def dfs(v):
        seen.add(v)
        for w in adj[v]:
            if w not in seen:
                dfs(w)
        finished.append(v)
    for v in range(n):
        if v not in seen:
            dfs(v)
    return finished[::-1]
