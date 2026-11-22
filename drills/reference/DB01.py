"""DB01 reference: Has a duplicate. Open after your own attempt."""
def solve(nums):
    seen = set()
    for value in nums:
        if value in seen:
            return True
        seen.add(value)
    return False
