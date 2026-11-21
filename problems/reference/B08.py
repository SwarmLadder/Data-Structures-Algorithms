"""Reference answer for B08. See the problem statement before reading.
"""
def solve(nums, k):
    if not nums:
        return []
    k %= len(nums)
    return nums[-k:] + nums[:-k] if k else nums[:]
