"""Reference answer for B07. See the problem statement before reading.
"""
def solve(nums):
    best = running = nums[0]
    for x in nums[1:]:
        running = max(x, running + x)
        best = max(best, running)
    return best
