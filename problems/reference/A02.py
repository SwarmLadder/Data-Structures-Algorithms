"""Reference answer for A02. See the problem statement before reading.
"""
def solve(n, edges, start, target):
    from collections import deque
    graph = [[] for _ in range(n)]
    for a,b in edges:
        graph[a].append(b)
    for values in graph:
        values.sort()
    parent = {start: None}
    queue = deque([start])
    while queue:
        current = queue.popleft()
        if current == target:
            break
        for nxt in graph[current]:
            if nxt not in parent:
                parent[nxt] = current
                queue.append(nxt)
    if target not in parent:
        return []
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = parent[node]
    return path[::-1]
