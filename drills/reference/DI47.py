"""DI47 reference: Two sum: sorted or not?. Open after your own attempt."""
def solve(nums, target):
    first = {}
    for j, x in enumerate(nums):
        if target - x in first:
            return [first[target - x], j]
        first.setdefault(x, j)
    return []
