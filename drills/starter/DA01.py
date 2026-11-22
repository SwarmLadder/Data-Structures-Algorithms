"""DA01 — Count connected components (guided)

n nodes are numbered 0..n-1; edges is a list of undirected [a, b] pairs. Return the
number of connected components.

Check: python -m tools.drills check DA01
Hints: python -m tools.drills hint DA01 1
"""

___ = None  # replace every ___ below with your code

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
                    seen.add(___)
                    stack.append(___)
    return components
