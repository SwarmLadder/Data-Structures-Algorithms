"""DI05 — Running totals (guided)

Return the list of prefix sums of nums: entry i is nums[0] + … + nums[i].

Check: python -m tools.drills check DI05
Hints: python -m tools.drills hint DI05 1
"""

___ = None  # replace every ___ below with your code

def solve(nums):
    out, total = [], 0
    for x in nums:
        total += ___
        out.append(___)
    return out
