"""DB31 — Remove the nth node from the end (independent)

Remove the nth node from the end (1 = last) of the list described by values, in one
pass with a dummy head, and return the remaining values. 1 <= n <= len(values).

Check: python -m tools.drills check DB31
Hints: python -m tools.drills hint DB31 1
"""

class Node:
    def __init__(self, value, next=None):
        self.value, self.next = value, next

def solve(values, n):
    raise NotImplementedError("Implement solve")
