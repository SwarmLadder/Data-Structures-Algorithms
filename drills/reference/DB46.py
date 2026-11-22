"""DB46 reference: Fast version of the same count. Open after your own attempt."""
def solve(nums):
    seen = {}
    total = 0
    for value in nums:
        total += seen.get(value, 0)
        seen[value] = seen.get(value, 0) + 1
    return total
