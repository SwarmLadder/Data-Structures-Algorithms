"""DI24 reference: Split into k parts minimising the largest sum. Open after your own attempt."""
def solve(nums, k):
    def parts(limit):
        count, total = 1, 0
        for x in nums:
            if total + x > limit:
                count, total = count + 1, 0
            total += x
        return count
    lo, hi = max(nums), sum(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if parts(mid) <= k:
            hi = mid
        else:
            lo = mid + 1
    return lo
