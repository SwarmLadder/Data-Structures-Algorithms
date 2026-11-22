"""DB30 — Middle node (guided)

Return the value of the middle node of the non-empty list described by values. For
an even length, return the second of the two middle nodes. Use slow/fast pointers.

Check: python -m tools.drills check DB30
Hints: python -m tools.drills hint DB30 1
"""

___ = None  # replace every ___ below with your code

class Node:
    def __init__(self, value, next=None):
        self.value, self.next = value, next

def solve(values):
    head = None
    for v in reversed(values):
        head = Node(v, head)
    slow = fast = head
    while fast and fast.next:
        slow = ___
        fast = ___
    return slow.value
