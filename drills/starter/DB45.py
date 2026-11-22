"""DB45 — Brute-force oracle: count equal pairs (guided)

Return how many index pairs i < j have nums[i] == nums[j], by checking every pair
(this is the oracle; clarity beats speed).

Check: python -m tools.drills check DB45
Hints: python -m tools.drills hint DB45 1
"""

___ = None  # replace every ___ below with your code

def solve(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(___, len(nums)):
            if ___:
                count += 1
    return count
