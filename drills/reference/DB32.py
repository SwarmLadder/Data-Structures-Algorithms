"""DB32 reference: Where does the cycle start?. Open after your own attempt."""
class Node:
    def __init__(self, value, next=None):
        self.value, self.next = value, next

def solve(values, pos):
    nodes = [Node(v) for v in values]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    if nodes and pos >= 0:
        nodes[-1].next = nodes[pos]
    head = nodes[0] if nodes else None
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            slow = head
            while slow is not fast:
                slow, fast = slow.next, fast.next
            return nodes.index(slow)
    return -1
