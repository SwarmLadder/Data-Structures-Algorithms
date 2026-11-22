"""DB19 reference: Pairs with a given difference. Open after your own attempt."""
def solve(nums, k):
    counts = {}
    total = 0
    for value in nums:
        total += counts.get(value - k, 0) + counts.get(value + k, 0)
        counts[value] = counts.get(value, 0) + 1
    return total
