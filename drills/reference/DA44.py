"""DA44 reference: Metamorphic check for a sort. Open after your own attempt."""
def solve(nums):
    s = sorted(nums)
    return sorted(s) == s and len(s) == len(nums) and sorted(nums[::-1]) == s
