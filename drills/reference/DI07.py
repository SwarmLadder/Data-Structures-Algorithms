"""DI07 reference: Pivot index. Open after your own attempt."""
def solve(nums):
    total, left = sum(nums), 0
    for i, x in enumerate(nums):
        if left == total - left - x:
            return i
        left += x
    return -1
