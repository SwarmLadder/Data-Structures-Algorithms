"""DI42 reference: Combinations of size k. Open after your own attempt."""
def solve(n, k):
    out, path = [], []
    def dfs(start):
        if len(path) == k:
            out.append(path.copy())
            return
        for x in range(start, n + 1):
            path.append(x)
            dfs(x + 1)
            path.pop()
    dfs(1)
    return out
