"""DA22 — Topological order by DFS finish times (guided)

Return a topological order of the DAG (nodes 0..n-1, edges [a, b] meaning a before
b) as the reverse of DFS finish order, visiting start nodes and neighbours in
increasing order.

Check: python -m tools.drills check DA22
Hints: python -m tools.drills hint DA22 1
"""

___ = None  # replace every ___ below with your code

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
        finished.append(___)
    for v in range(n):
        if v not in seen:
            dfs(v)
    return ___
