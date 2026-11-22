"""DB05 — Reverse a list in place (guided)

Reverse the list nums in place with two pointers (no slicing or reversed()) and
return it.

Check: python -m tools.drills check DB05
Hints: python -m tools.drills hint DB05 1
"""

___ = None  # replace every ___ below with your code

def solve(nums):
    i, j = 0, len(nums) - 1
    while ___:
        nums[i], nums[j] = ___
        i += 1
        j -= 1
    return nums
