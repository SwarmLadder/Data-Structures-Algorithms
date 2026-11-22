"""DI48 reference: Count ranges with sum k (any sign). Open after your own attempt."""
def solve(nums, k):
    seen, total, count = {0: 1}, 0, 0
    for x in nums:
        total += x
        count += seen.get(total - k, 0)
        seen[total] = seen.get(total, 0) + 1
    return count
