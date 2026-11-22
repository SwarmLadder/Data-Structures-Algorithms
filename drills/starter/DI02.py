"""DI02 — Shortest subarray with sum at least target (guided)

nums contains positive integers. Return the length of the shortest contiguous
subarray whose sum is >= target, or 0 if none exists.

Check: python -m tools.drills check DI02
Hints: python -m tools.drills hint DI02 1
"""

___ = None  # replace every ___ below with your code

def solve(target, nums):
    left = total = 0
    best = len(nums) + 1
    for right, x in enumerate(nums):
        total += x
        while total >= target:
            best = min(best, ___)
            total -= ___
            left += 1
    return best if best <= len(nums) else 0
