"""Reference answer for A09. See the problem statement before reading.
"""
def solve(nums):
    from bisect import bisect_left
    tails = []
    for x in nums:
        pos = bisect_left(tails, x)
        if pos == len(tails): tails.append(x)
        else: tails[pos] = x
    return len(tails)
