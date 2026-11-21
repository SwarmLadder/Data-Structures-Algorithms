"""Reference answer for B01. See the problem statement before reading.
"""
def solve(nums, target):
    seen = {}
    for j, x in enumerate(nums):
        i = seen.get(target - x)
        if i is not None:
            return [i, j]
        seen[x] = j
    raise ValueError('No matching pair')
