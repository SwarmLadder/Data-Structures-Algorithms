"""DB44 reference: The missing number. Open after your own attempt."""
def solve(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)
