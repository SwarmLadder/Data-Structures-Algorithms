"""DB13 — First index at or above target (guided)

nums is sorted ascending. Return the first index i with nums[i] >= target, or
len(nums) if there is none. Don't use the bisect module.

Check: python -m tools.drills check DB13
Hints: python -m tools.drills hint DB13 1
"""

___ = None  # replace every ___ below with your code

def solve(nums, target):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = ___
        else:
            hi = ___
    return lo
