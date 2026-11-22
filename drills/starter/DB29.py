"""DB29 — Reverse a linked list (as values) (guided)

values describes a singly linked list. Build the nodes, reverse the links in place
(no reversed() on the values), and return the reversed values.

Check: python -m tools.drills check DB29
Hints: python -m tools.drills hint DB29 1
"""

___ = None  # replace every ___ below with your code

class Node:
    def __init__(self, value, next=None):
        self.value, self.next = value, next

def solve(values):
    head = None
    for v in reversed(values):
        head = Node(v, head)
    previous, current = None, head
    while current:
        following = current.next
        current.next = ___
        previous = ___
        current = following
    out = []
    while previous:
        out.append(previous.value)
        previous = previous.next
    return out
