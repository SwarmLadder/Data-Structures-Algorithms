"""Sliding-window rate limiter and traffic analytics: reference implementation."""
from collections import deque


class SlidingWindowLimiter:
    """Allow at most `limit` requests per client in any window of `window` seconds (half-open (t - window, t])."""

    def __init__(self, limit, window):
        self.limit, self.window = limit, window
        self.recent = {}                       # client -> deque of accepted request times

    def allow(self, client, t):
        """Record a request at time t (non-decreasing per client); return True if it is accepted."""
        q = self.recent.setdefault(client, deque())
        while q and q[0] <= t - self.window:   # expire requests that left the window
            q.popleft()
        if len(q) < self.limit:
            q.append(t)
            return True
        return False


def busiest_window(times, window):
    """Max number of requests inside any half-open window [s, s + window) (times sorted)."""
    best, left = 0, 0
    for right, t in enumerate(times):
        while times[left] <= t - window:
            left += 1
        best = max(best, right - left + 1)
    return best


def requests_between(times, queries):
    """For sorted times, answer each (a, b) query: how many requests have a <= t < b."""
    from bisect import bisect_left
    return [bisect_left(times, b) - bisect_left(times, a) for a, b in queries]
