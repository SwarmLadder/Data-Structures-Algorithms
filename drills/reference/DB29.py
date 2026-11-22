"""DB29 reference: Reverse a linked list (as values). Open after your own attempt."""
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
        current.next = previous
        previous = current
        current = following
    out = []
    while previous:
        out.append(previous.value)
        previous = previous.next
    return out
