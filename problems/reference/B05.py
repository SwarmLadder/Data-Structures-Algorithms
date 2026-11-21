"""Reference answer for B05. See the problem statement before reading.
"""
def solve(nums, threshold):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < threshold:
            lo = mid + 1
        else:
            hi = mid
    return lo
