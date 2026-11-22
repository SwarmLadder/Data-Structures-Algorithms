"""DB30 reference: Middle node. Open after your own attempt."""
class Node:
    def __init__(self, value, next=None):
        self.value, self.next = value, next

def solve(values):
    head = None
    for v in reversed(values):
        head = Node(v, head)
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.value
