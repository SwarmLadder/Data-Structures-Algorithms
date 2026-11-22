"""DB34 — Distances from a start node (guided)

graph maps each node (a string) to a list of neighbours. Return a dict of the BFS
distance (number of edges) from start to every reachable node.

Check: python -m tools.drills check DB34
Hints: python -m tools.drills hint DB34 1
"""

___ = None  # replace every ___ below with your code

from collections import deque

def solve(graph, start):
    dist = {start: 0}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for nxt in graph.get(node, []):
            if nxt not in dist:
                dist[nxt] = ___
                queue.append(___)
    return dist
