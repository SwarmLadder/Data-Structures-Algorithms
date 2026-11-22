"""DB36 — Recent calls counter (independent)

times is a strictly increasing list of request times in milliseconds. For each
request, return how many requests (including itself) happened in the inclusive
window [t - 3000, t].

Check: python -m tools.drills check DB36
Hints: python -m tools.drills hint DB36 1
"""

from collections import deque

def solve(times):
    raise NotImplementedError("Implement solve")
