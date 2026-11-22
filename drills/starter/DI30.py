"""DI30 — Last stone weight (guided)

Repeatedly smash the two heaviest stones: equal stones both vanish, otherwise the
lighter vanishes and the heavier loses the lighter's weight. Return the last stone's
weight, or 0.

Check: python -m tools.drills check DI30
Hints: python -m tools.drills hint DI30 1
"""

___ = None  # replace every ___ below with your code

import heapq

def solve(stones):
    heap = [-s for s in stones]
    heapq.heapify(heap)
    while len(heap) > 1:
        a = -heapq.heappop(heap)
        b = -heapq.heappop(heap)
        if a != b:
            heapq.heappush(heap, ___)
    return ___ if heap else 0
