"""DB06 — Pair with a target in a sorted list (guided)

nums is sorted ascending. Return [i, j] (i < j) with nums[i] + nums[j] == target
using two pointers, or [] if none exists. If several pairs exist, return the one
found by moving the smaller-sum side first (start from both ends).

Check: python -m tools.drills check DB06
Hints: python -m tools.drills hint DB06 1
"""

___ = None  # replace every ___ below with your code

def solve(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        if total < target:
            ___
        else:
            ___
    return []
