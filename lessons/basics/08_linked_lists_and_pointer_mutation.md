# Linked lists: pointer mutation, dummy heads and cycle proofs

**Outcome:** update links without losing nodes and choose linked structures only when their tradeoffs justify them. **Study time:** 90 minutes.

## 1. Model the references

A singly linked node stores a value and a reference to the next node. Accessing the ith node costs O(i), unlike O(1) indexing into an array. Insertion **after a known node** is O(1), but locating that node may cost O(n). Each Python node is a separate object, typically with substantial per-node overhead.

```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

head = Node(3, Node(7, Node(9)))
```

Always draw a chain before rewiring. For `3 → 7 → 9 → None`, changing 3's next pointer before saving 7 would disconnect the rest of the list.

## 2. Reverse without allocating nodes

```python
def reverse(head):
    previous = None
    current = head
    while current is not None:
        following = current.next
        current.next = previous
        previous = current
        current = following
    return previous
```

**Invariant:** `previous` heads a fully reversed prefix, while `current` heads an untouched suffix, and together they contain every original node exactly once. The initial prefix is empty. Each step moves one node into the reversed prefix **after** saving the suffix. Once `current` is None, the suffix is empty and `previous` contains the full reversal. O(n) time and O(1) auxiliary space.

Trace: save 7, point 3→None; save 9, point 7→3; point 9→7. Return 9. If you overwrite `current.next` first, the original continuation becomes unreachable.

## 3. Slow/fast pointers and cycles

```python
def has_cycle(head):
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
```

On an acyclic list the fast pointer reaches the end. On a cycle, the relative position of fast to slow advances by one each turn modulo cycle length, so the two eventually meet. Use **node identity** (`is`), not equal values: distinct nodes may hold identical data. Runtime O(n), extra space O(1), compared with O(n) memory for a visited-node set.

To find the cycle **entry**, after meeting reset one pointer to the head and advance both one node at a time. If there are μ nodes before the cycle and λ nodes in it, the meeting offset satisfies a modular relation with μ; the two pointers therefore meet at entry. This fact is subtle: derive it with a diagram, not just memorized steps.

## 4. Dummy heads and deletions

Removing the nth node from the end often deletes the original head. A dummy node before the head prevents special cases. Start fast n+1 links ahead of slow (both at dummy), then advance both until fast is None; slow is the predecessor of the node to remove. Reconnect `slow.next = slow.next.next`. Validate n≥1 and n≤length if not guaranteed.

## 5. Edge tests

- Empty head, one node, two nodes.
- Cycle returning to head, cycle starting in the middle, no cycle.
- Shared tail between two lists: value equality does not mean object identity.
- Reversal twice must recover the original sequence; check this **metamorphic property**.
- Deletion of first, middle and final nodes.

**Practice:** I16 plus reverse/merge/remove duplicates in linked lists. **Mastery checkpoint:** Demonstrate the exact order of pointer assignments and prove no node is lost, duplicated or accidentally reused.
