"""DB14 — Range sums with a prefix array (guided)

Return a list with the sum of nums[i:j] for each [i, j] pair in queries (half-open
ranges). Build a prefix array once.

Check: python -m tools.drills check DB14
Hints: python -m tools.drills hint DB14 1
"""

___ = None  # replace every ___ below with your code

def solve(nums, queries):
    prefix = [0]
    for x in nums:
        prefix.append(___)
    return [___ for i, j in queries]
