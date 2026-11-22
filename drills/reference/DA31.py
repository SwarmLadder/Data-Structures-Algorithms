"""DA31 reference: Longest increasing subsequence (n log n). Open after your own attempt."""
from bisect import bisect_left

def solve(nums):
    tails = []
    for x in nums:
        i = bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)
