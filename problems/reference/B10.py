"""Reference answer for B10. See the problem statement before reading.
"""
def solve(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)
