"""DA32 reference: Partition into equal sums. Open after your own attempt."""
def solve(nums):
    total = sum(nums)
    if total % 2:
        return False
    target = total // 2
    reachable = [True] + [False] * target
    for x in nums:
        for s in range(target, x - 1, -1):
            reachable[s] = reachable[s] or reachable[s - x]
    return reachable[target]
