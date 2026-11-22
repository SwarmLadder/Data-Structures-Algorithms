"""DB32 — Where does the cycle start? (independent)

values describes a list whose last node links back to index pos (or pos = -1 for no
cycle). Return the index of the node where the cycle begins, or -1, using O(1) extra
space (Floyd's algorithm).

Check: python -m tools.drills check DB32
Hints: python -m tools.drills hint DB32 1
"""

class Node:
    def __init__(self, value, next=None):
        self.value, self.next = value, next

def solve(values, pos):
    raise NotImplementedError("Implement solve")
