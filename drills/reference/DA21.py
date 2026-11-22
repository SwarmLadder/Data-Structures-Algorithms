"""DA21 reference: Cycle check with DFS colours. Open after your own attempt."""
def solve(n, edges):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
    colour = [0] * n
    def dfs(v):
        colour[v] = 1
        for w in adj[v]:
            if colour[w] == 1:
                return True
            if colour[w] == 0 and dfs(w):
                return True
        colour[v] = 2
        return False
    return any(colour[v] == 0 and dfs(v) for v in range(n))
