"""DB38 reference: Counting sort for small ints. Open after your own attempt."""
def solve(nums):
    counts = [0] * 10
    for x in nums:
        counts[x] += 1
    out = []
    for digit in range(10):
        out.extend([digit] * counts[digit])
    return out
