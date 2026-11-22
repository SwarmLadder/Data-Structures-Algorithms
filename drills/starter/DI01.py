"""DI01 — Maximum sum of k consecutive values (guided)

Return the largest sum of any k consecutive values in nums (1 <= k <= len(nums)), in
O(n).

Check: python -m tools.drills check DI01
Hints: python -m tools.drills hint DI01 1
"""

___ = None  # replace every ___ below with your code

def solve(nums, k):
    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += ___
        best = max(best, window)
    return best
