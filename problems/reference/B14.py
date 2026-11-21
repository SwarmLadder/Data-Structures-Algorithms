"""Reference answer for B14. See the problem statement before reading.
"""
def solve(nums):
    nonzero = [x for x in nums if x != 0]
    return nonzero + [0] * (len(nums) - len(nonzero))
