"""DB47 reference: Maximum subarray sum (all-negative safe). Open after your own attempt."""
def solve(nums):
    running = best = nums[0]
    for value in nums[1:]:
        running = max(value, running + value)
        best = max(best, running)
    return best
