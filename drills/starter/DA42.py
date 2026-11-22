"""DA42 — Check a loop invariant (guided)

Run the max-finding loop on nums (non-empty) and return True if the invariant 'best
== max(nums[:i])' holds before every iteration i from 1 to len(nums), and at the
end.

Check: python -m tools.drills check DA42
Hints: python -m tools.drills hint DA42 1
"""

___ = None  # replace every ___ below with your code

def solve(nums):
    best = nums[0]
    for i in range(1, len(nums)):
        if best != max(nums[:i]):
            return False
        best = max(best, ___)
    return best == ___
