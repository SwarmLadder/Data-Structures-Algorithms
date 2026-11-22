"""DI06 — Count subarrays with sum k (guided)

Return how many contiguous non-empty subarrays of nums sum to exactly k. Values may
be negative.

Check: python -m tools.drills check DI06
Hints: python -m tools.drills hint DI06 1
"""

___ = None  # replace every ___ below with your code

def solve(nums, k):
    seen = {0: 1}
    total = count = 0
    for x in nums:
        total += x
        count += seen.get(___, 0)
        seen[total] = ___
    return count
