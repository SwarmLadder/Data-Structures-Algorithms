"""DA01 reference: Count connected components. Open after your own attempt."""
def solve(n, edges):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    seen, components = set(), 0
    for start in range(n):
        if start in seen:
            continue
        components += 1
        stack = [start]
        seen.add(start)
        while stack:
            v = stack.pop()
            for w in adj[v]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
    return components
