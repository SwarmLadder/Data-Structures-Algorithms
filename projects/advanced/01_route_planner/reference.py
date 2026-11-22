"""Route planner: Dijkstra with deterministic path reconstruction. Reference implementation."""
import heapq


class RoutePlanner:
    def __init__(self):
        self.adj = {}

    def add_road(self, a, b, minutes, two_way=True):
        """Add a road with a non-negative travel time."""
        if minutes < 0:
            raise ValueError("travel times must be non-negative")
        self.adj.setdefault(a, []).append((b, minutes))
        self.adj.setdefault(b, [])
        if two_way:
            self.adj[b].append((a, minutes))

    def fastest(self, start, goal):
        """Return (minutes, path) of the fastest route; among equally fast routes pick the
        lexicographically smallest path. Return (None, []) if unreachable."""
        if start not in self.adj or goal not in self.adj:
            return None, []
        best = {start: (0, [start])}
        heap = [(0, [start])]
        done = set()
        while heap:
            d, path = heapq.heappop(heap)          # (time, path) orders ties by path
            node = path[-1]
            if node in done:
                continue
            done.add(node)
            if node == goal:
                return d, path
            for nxt, w in self.adj[node]:
                cand = (d + w, path + [nxt])
                if nxt not in done and (nxt not in best or cand < best[nxt]):
                    best[nxt] = cand
                    heapq.heappush(heap, cand)
        return None, []

    def reachable_within(self, start, limit):
        """Sorted list of places reachable from start within `limit` minutes."""
        dist = {start: 0}
        heap = [(0, start)]
        while heap:
            d, v = heapq.heappop(heap)
            if d > dist[v]:
                continue
            for w, c in self.adj.get(v, []):
                if d + c < dist.get(w, float("inf")):
                    dist[w] = d + c
                    heapq.heappush(heap, (d + c, w))
        return sorted(v for v, d in dist.items() if d <= limit)
