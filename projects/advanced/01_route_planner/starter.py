"""Route planner: your implementation. See README.md for the tickets.

Run: python -m tools.projects check advanced/01_route_planner
"""
import heapq

class RoutePlanner:

    def __init__(self):
        pass

    def add_road(self, a, b, minutes, two_way=True):
        """Add a road with a non-negative travel time."""
        raise NotImplementedError('implement add_road')

    def fastest(self, start, goal):
        """Return (minutes, path) of the fastest route; among equally fast routes pick the
lexicographically smallest path. Return (None, []) if unreachable."""
        raise NotImplementedError('implement fastest')

    def reachable_within(self, start, limit):
        """Sorted list of places reachable from start within `limit` minutes."""
        raise NotImplementedError('implement reachable_within')
