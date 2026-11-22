# Linked lists: pointer mutation, dummy heads and cycle proofs

**Outcome:** update links without losing nodes and choose linked structures only when their tradeoffs justify them. **Study time:** 90 minutes.

**Before this:** [Recursion: base cases, induction, stack frames and backtracking](07_recursion_call_stack_and_base_cases.md)

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

<!-- lesson-practice -->

## Try it

Run this block (or `python -m tools.lessons` to refresh every page), then change one input and predict the new output before running it again.

```python
class ListNode:
    def __init__(self, value, next=None):
        self.value, self.next = value, next

def build(values):
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head

def to_list(head):
    out = []
    while head:
        out.append(head.value)
        head = head.next
    return out

def reverse_links(head):
    previous = None
    while head:
        head.next, previous, head = previous, head, head.next
    return previous

print(to_list(reverse_links(build([3, 7, 9]))))

def remove_value(head, target):
    dummy = ListNode(None, head)          # removing the head needs no special case
    prev = dummy
    while prev.next:
        if prev.next.value == target:
            prev.next = prev.next.next
        else:
            prev = prev.next
    return dummy.next

print(to_list(remove_value(build([1, 2, 1, 3, 1]), 1)))
```

<!-- output -->
```text
[9, 7, 3]
[2, 3]
```
<!-- /output -->

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Overwriting `current.next` before saving it | The rest of the list is lost | Save `following = current.next` first |
| Special-casing deletion of the head | Branches and bugs | Use a dummy node before the head |
| Comparing nodes with `==` instead of `is` | Two nodes with equal values look like the same node | Use identity (`is`) for node equality |
| Checking `fast.next.next` without checking `fast.next` | AttributeError at the end of the list | `while fast and fast.next:` |
| Using a list where O(1) middle insertion is the point | O(n) shifts | Linked nodes give O(1) insert after a known node |

## Your turn

<!-- drills -->
Each drill is graded on six published cases. **Guided** drills give you a skeleton with `___` blanks; **independent** drills give only the signature.

| ID | Drill | Kind |
|---|---|---|
| `DB29` | **Reverse a linked list (as values).** values describes a singly linked list. Build the nodes, reverse the links in place (no reversed() on the values), and return the reversed values. | guided |
| `DB30` | **Middle node.** Return the value of the middle node of the non-empty list described by values. For an even length, return the second of the two middle nodes. Use slow/fast pointers. | guided |
| `DB31` | **Remove the nth node from the end.** Remove the nth node from the end (1 = last) of the list described by values, in one pass with a dummy head, and return the remaining values. 1 <= n <= len(values). | independent |
| `DB32` | **Where does the cycle start?.** values describes a list whose last node links back to index pos (or pos = -1 for no cycle). Return the index of the node where the cycle begins, or -1, using O(1) extra space (Floyd's algorithm). | independent |

```bash
python -m tools.drills show DB29
python -m tools.drills check DB29
python -m tools.drills hint DB29 1
```
<!-- /drills -->

**Interview problems for this lesson:** `I16`. Read one with `python -m tools.practice show I16 --hints`.

## Quick quiz

<!-- quiz -->
Answer in your head first, then check. Answers are stored as hashes, so reading the files won't spoil them.

**1.** Reversing a list, what must you save before `current.next = previous`?

   - **a)** previous
   - **b)** current.next (the rest of the list)
   - **c)** the head

**2.** Why use a dummy head?

   - **a)** To make the list longer
   - **b)** So deleting or inserting at the front needs no special case
   - **c)** For cycles

**3.** Why do slow and fast pointers meet inside a cycle?

   - **a)** Fast closes the gap by one node per step
   - **b)** They start together
   - **c)** Lists are short

**4.** Accessing the i-th node of a linked list costs…

   - **a)** O(1)
   - **b)** O(i)
   - **c)** O(log i)

```bash
python -m tools.quiz basics/08 1 b      # question 1, answer b
python -m tools.quiz basics/08           # list the questions
```
<!-- /quiz -->

## Summary

- Linked lists trade O(1) indexing for O(1) insertion and deletion at a known node.
- Save the next pointer before rewiring; draw the chain first.
- A dummy head removes special cases when the first node changes.
- Slow/fast pointers detect cycles in O(n) time and O(1) space.

**Next:** [Queues and deques: ordering as an algorithmic tool](09_queues_deques_and_bfs_frontiers.md)
