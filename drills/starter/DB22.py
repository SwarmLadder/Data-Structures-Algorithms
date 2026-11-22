"""DB22 — Rotate right by k (guided)

Return a new list with nums rotated right by k positions (k >= 0 may exceed
len(nums)). An empty list stays empty.

Check: python -m tools.drills check DB22
Hints: python -m tools.drills hint DB22 1
"""

___ = None  # replace every ___ below with your code

def solve(nums, k):
    n = len(nums)
    if n == 0:
        return []
    k = ___
    return nums[n - k:] + nums[:n - k]
