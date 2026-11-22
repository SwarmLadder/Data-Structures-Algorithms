"""DI10 — Minimum meeting rooms (guided)

meetings are half-open [start, end) intervals. Return the minimum number of rooms
needed so no two overlapping meetings share a room.

Check: python -m tools.drills check DI10
Hints: python -m tools.drills hint DI10 1
"""

___ = None  # replace every ___ below with your code

import heapq

def solve(meetings):
    ends = []
    for start, end in sorted(meetings):
        if ends and ends[0] <= start:
            heapq.heapreplace(ends, ___)
        else:
            heapq.heappush(ends, ___)
    return len(ends)
