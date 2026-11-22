"""DB21 — Move zeros to the end (guided)

Move all zeros in nums to the end in place, keeping the order of the non-zero
values, and return nums.

Check: python -m tools.drills check DB21
Hints: python -m tools.drills hint DB21 1
"""

___ = None  # replace every ___ below with your code

def solve(nums):
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write] = ___
            write += 1
    for i in range(___, len(nums)):
        nums[i] = 0
    return nums
