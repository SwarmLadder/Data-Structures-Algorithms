"""DA42 reference: Check a loop invariant. Open after your own attempt."""
def solve(nums):
    best = nums[0]
    for i in range(1, len(nums)):
        if best != max(nums[:i]):
            return False
        best = max(best, nums[i])
    return best == max(nums)
