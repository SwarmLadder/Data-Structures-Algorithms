"""DB22 reference: Rotate right by k. Open after your own attempt."""
def solve(nums, k):
    n = len(nums)
    if n == 0:
        return []
    k = k % n
    return nums[n - k:] + nums[:n - k]
