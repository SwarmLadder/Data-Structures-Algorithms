"""DB38 — Counting sort for small ints (guided)

Sort nums, whose values are integers from 0 to 9, using counting (no sorted or
.sort).

Check: python -m tools.drills check DB38
Hints: python -m tools.drills hint DB38 1
"""

___ = None  # replace every ___ below with your code

def solve(nums):
    counts = [0] * 10
    for x in nums:
        counts[x] += 1
    out = []
    for digit in range(10):
        out.extend([___] * ___)
    return out
