"""Sliding-window rate limiter and traffic analytics: your implementation. See README.md for the tickets.

Run: python -m tools.projects check intermediate/01_rate_limiter
"""
from collections import deque

class SlidingWindowLimiter:
    """Allow at most `limit` requests per client in any window of `window` seconds (half-open (t - window, t])."""

    def __init__(self, limit, window):
        pass

    def allow(self, client, t):
        """Record a request at time t (non-decreasing per client); return True if it is accepted."""
        raise NotImplementedError('implement allow')

def busiest_window(times, window):
    """Max number of requests inside any half-open window [s, s + window) (times sorted)."""
    raise NotImplementedError('implement busiest_window')

def requests_between(times, queries):
    """For sorted times, answer each (a, b) query: how many requests have a <= t < b."""
    raise NotImplementedError('implement requests_between')
