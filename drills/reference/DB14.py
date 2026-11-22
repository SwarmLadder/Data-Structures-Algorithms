"""DB14 reference: Range sums with a prefix array. Open after your own attempt."""
def solve(nums, queries):
    prefix = [0]
    for x in nums:
        prefix.append(prefix[-1] + x)
    return [prefix[j] - prefix[i] for i, j in queries]
