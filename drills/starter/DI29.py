"""DI29 — Kth largest (guided)

Return the kth largest value in nums (counting duplicates; 1 <= k <= len(nums))
using a min-heap of size k.

Check: python -m tools.drills check DI29
Hints: python -m tools.drills hint DI29 1
"""

___ = None  # replace every ___ below with your code

import heapq

def solve(nums, k):
    heap = []
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > ___:
            heapq.heappop(heap)
    return ___
