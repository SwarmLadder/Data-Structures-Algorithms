"""DB04 reference: Most frequent value, smallest on ties. Open after your own attempt."""
def solve(nums):
    counts = {}
    for value in nums:
        counts[value] = counts.get(value, 0) + 1
    return max(counts, key=lambda v: (counts[v], -v))
