"""DA09 — House robber (guided)

Return the maximum sum of non-adjacent values in nums (values >= 0; 0 for an empty
list).

Check: python -m tools.drills check DA09
Hints: python -m tools.drills hint DA09 1
"""

___ = None  # replace every ___ below with your code

def solve(nums):
    prev2 = prev1 = 0
    for x in nums:
        prev2, prev1 = prev1, max(___, ___)
    return prev1
