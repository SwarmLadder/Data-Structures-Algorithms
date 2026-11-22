"""DB46 — Fast version of the same count (guided)

Same contract as the oracle: count pairs i < j with nums[i] == nums[j], but in O(n)
expected time.

Check: python -m tools.drills check DB46
Hints: python -m tools.drills hint DB46 1
"""

___ = None  # replace every ___ below with your code

def solve(nums):
    seen = {}
    total = 0
    for value in nums:
        total += ___
        seen[value] = seen.get(value, 0) + 1
    return total
