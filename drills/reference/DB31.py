"""DB31 reference: Remove the nth node from the end. Open after your own attempt."""
class Node:
    def __init__(self, value, next=None):
        self.value, self.next = value, next

def solve(values, n):
    head = None
    for v in reversed(values):
        head = Node(v, head)
    dummy = Node(None, head)
    lead = trail = dummy
    for _ in range(n + 1):
        lead = lead.next
    while lead:
        lead, trail = lead.next, trail.next
    trail.next = trail.next.next
    out, node = [], dummy.next
    while node:
        out.append(node.value)
        node = node.next
    return out
